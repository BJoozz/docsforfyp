// Deck clips for the CA presentation, recorded from the real VisuAlgo+ app.
//
// Drives the real UI only (mouse, keyboard, the app's own controls). No source
// edits, no state injection, no CSS hiding, no overlays. Each clip runs in a
// fresh browser context; only the clip segment is recorded, with the Chrome
// DevTools screencast, and every frame keeps its own timestamp, so the video is
// rebuilt at the real speed (constant 30 fps) from exactly that segment.
//
// Usage (PowerShell):
//   $env:CA_APP_REPO = 'C:\path\to\visualgo-plus-design'   # repo root; @playwright/test is loaded from it
//   $env:CA_BASE_URL = 'http://127.0.0.1:5205'              # your own dev server of that checkout
//   $env:CA_DECK_OUTPUT = 'C:\path\outside\onedrive\deck'    # frames, clips, posters, checks
//   $env:CA_FFMPEG = 'C:\path\to\ffmpeg.exe'                 # optional: a full build with libx264
//   node .\capture-deck.mjs 01_lca_equal_ancestors 01b_lca_keep_then_jump 02_v10_move_panel ...
//   node .\capture-deck.mjs all
import { createRequire } from 'node:module';
import { mkdir, writeFile, rm } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import path from 'node:path';

const APP = process.env.CA_APP_REPO;
const OUT = process.env.CA_DECK_OUTPUT;
if (!APP) throw new Error('Set CA_APP_REPO to the app checkout.');
if (!OUT) throw new Error('Set CA_DECK_OUTPUT to an output folder (keep it outside a synced folder).');
const require = createRequire(path.join(APP, 'package.json'));
const { chromium } = require('@playwright/test');
const BASE = process.env.CA_BASE_URL ?? 'http://127.0.0.1:5205';
const FFMPEG = process.env.CA_FFMPEG;
const FPS = 30;
const VIEWPORT = { width: 1440, height: 900 };
const git = (...args) => spawnSync('git', ['-C', APP, ...args], { encoding: 'utf8' }).stdout.trim();
const APP_COMMIT = git('rev-parse', 'HEAD');
const APP_DIRTY = git('status', '--porcelain') !== '';
const now = () => Date.now() / 1000;
const sleep = (ms) => new Promise((r) => setTimeout(r, Math.max(0, ms)));
const round = (x, d = 3) => Math.round(x * 10 ** d) / 10 ** d;

// ---------- recorder: CDP screencast of the clip segment only ----------
async function startRecorder(page, dir) {
  await rm(dir, { recursive: true, force: true });
  await mkdir(dir, { recursive: true });
  const cdp = await page.context().newCDPSession(page);
  const frames = [];
  const writes = [];
  cdp.on('Page.screencastFrame', ({ data, metadata, sessionId }) => {
    const file = `f${String(frames.length).padStart(5, '0')}.jpg`;
    frames.push({ file, ts: metadata.timestamp, recv: now(), w: metadata.deviceWidth, h: metadata.deviceHeight });
    writes.push(writeFile(path.join(dir, file), Buffer.from(data, 'base64')));
    cdp.send('Page.screencastFrameAck', { sessionId }).catch(() => {});
  });
  await cdp.send('Page.startScreencast', { format: 'jpeg', quality: 92, maxWidth: VIEWPORT.width, maxHeight: VIEWPORT.height, everyNthFrame: 1 });
  const waitFrom = now();
  while (frames.length === 0 && now() - waitFrom < 5) await sleep(20);
  if (frames.length === 0) throw new Error('No screencast frame arrived.');
  await sleep(150);
  const rec = { dir, frames, t0: now(), tEnd: null, pendingWrites: () => writes.length - settled.count };
  const settled = { count: 0 };
  writes.push = ((push) => function (p) { p.then(() => settled.count++); return push.call(this, p); })(writes.push);
  rec.stop = async () => {
    rec.tEnd = rec.tEnd ?? now();
    await sleep(120); // let the frames up to tEnd arrive
    await cdp.send('Page.stopScreencast');
    await Promise.all(writes);
    await cdp.detach();
  };
  return rec;
}

// Constant 30 fps: output frame n shows the newest screencast frame swapped at or before t0 + n/30.
function encode(rec, mp4) {
  const frames = rec.frames.slice().sort((a, b) => a.ts - b.ts);
  const n = Math.round((rec.tEnd - rec.t0) * FPS);
  const pick = [];
  let j = 0;
  for (let i = 0; i < n; i++) {
    const t = rec.t0 + i / FPS;
    while (j + 1 < frames.length && frames[j + 1].ts <= t) j++;
    pick.push(j);
  }
  const lines = ['ffconcat version 1.0'];
  for (let i = 0; i < n;) {
    let k = i;
    while (k + 1 < n && pick[k + 1] === pick[i]) k++;
    lines.push(`file '${frames[pick[i]].file}'`, `duration ${((k - i + 1) / FPS).toFixed(6)}`);
    i = k + 1;
  }
  lines.push(`file '${frames[pick[n - 1]].file}'`);
  const list = path.join(rec.dir, 'list.ffconcat');
  return writeFile(list, lines.join('\n') + '\n').then(() => {
    const args = ['-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', list,
      '-vf', 'fps=30,scale=in_range=pc:out_range=tv:in_color_matrix=bt601:out_color_matrix=bt709:flags=accurate_rnd+full_chroma_int,format=yuv420p',
      '-frames:v', String(n), '-r', '30', '-c:v', 'libx264', '-profile:v', 'high', '-preset', 'slow', '-crf', '18',
      '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv',
      '-movflags', '+faststart', '-an', mp4];
    const r = spawnSync(FFMPEG, args, { encoding: 'utf8' });
    if (r.status !== 0) throw new Error('ffmpeg failed: ' + r.stderr);
    return { outputFrames: n, durationSeconds: n / FPS, sourceFramesUsed: new Set(pick).size, ffmpegArgs: args.map((a) => (a === list ? 'list.ffconcat' : a === mp4 ? path.basename(mp4) : a)) };
  });
}

// ---------- page helpers ----------
async function ready(page, route) {
  await page.goto(BASE + route);
  await page.locator('.viz-page').waitFor();
  await page.locator('.workspace-loading__message').waitFor({ state: 'hidden' });
  const fonts = await page.evaluate(async () => {
    await document.fonts.load('700 14px Inter');
    await document.fonts.ready;
    return [...document.fonts].filter((f) => f.family === 'Inter' && f.status === 'loaded').length;
  });
  if (fonts === 0) throw new Error('Inter did not load');
  await page.waitForTimeout(500);
}
const footerButton = (page, name) => page.locator('.footer-bar').getByRole('button', { name, exact: true });
/** The Status panel's sentence: its first line ending in a full stop. */
const sentence = (text) => (text ?? '').split('\n').map((x) => x.trim()).filter(Boolean).find((x) => /[.]$/.test(x)) ?? null;
const frameText = (page) => page.locator('.footer-bar__frame').innerText();
const graphNode = (page, label) => page.locator('.react-flow__node').filter({ has: page.getByText(label, { exact: true }) });
const treeNode = (page, id) => page.locator(`.react-flow__node[data-id="${id}"]`);
async function center(locator) {
  const b = await locator.boundingBox();
  if (!b) throw new Error('No box for ' + locator);
  return { x: b.x + b.width / 2, y: b.y + b.height / 2 };
}
async function dragPath(page, from, to, ms, steps = 12) {
  await page.mouse.move(from.x, from.y);
  await page.mouse.down();
  for (let i = 1; i <= steps; i++) {
    await page.mouse.move(from.x + (to.x - from.x) * i / steps, from.y + (to.y - from.y) * i / steps);
    await page.waitForTimeout(ms / steps);
  }
  await page.mouse.up();
}

// What the page shows now, read from the DOM.
function domState(page) {
  return page.evaluate(() => {
    const q = (s) => document.querySelector(s);
    const status = q('[data-panel-body="status"]');
    const notes = [...document.querySelectorAll('.step-notes')].map((e) => e.innerText.trim()).filter(Boolean);
    // Which node each visible note sits above: the nearest node centre below the note.
    // A tree node's React Flow id is its value; a graph node's label is its one leaf text made of letters (badges are numbers).
    const isTree = location.pathname.startsWith('/tree-editor');
    const nodes = [...document.querySelectorAll('.react-flow__node')].map((e) => {
      const r = e.getBoundingClientRect();
      // A graph node's own label element (letters or digits), never its distance badge.
      const label = isTree ? e.dataset.id : e.querySelector('[class*="nodeLabel"]')?.textContent.trim() ?? null;
      return { label, x: r.x + r.width / 2, y: r.y + r.height / 2 };
    });
    const noteItems = [...document.querySelectorAll('.step-notes *')].filter((e) => e.children.length === 0 && e.textContent.trim()).map((e) => {
      const r = e.getBoundingClientRect();
      const cx = r.x + r.width / 2;
      const cy = r.y + r.height / 2;
      const near = nodes.filter((n) => n.y >= cy).sort((a, b) => Math.hypot(a.x - cx, a.y - cy) - Math.hypot(b.x - cx, b.y - cy))[0];
      return { text: e.textContent.trim(), opacity: getComputedStyle(e.closest('[style]') ?? e).opacity, nearestNodeBelow: near?.label ?? null };
    });
    const strip = q('.binary-strip__line');
    const vp = q('.react-flow__viewport');
    return {
      footerFrame: q('.footer-bar__frame')?.innerText ?? null,
      status: status ? status.innerText : null,
      statusRegion: status?.closest('[data-region]')?.dataset.region ?? null,
      notes,
      noteItems,
      strip: strip ? strip.innerText.replace(/\n/g, ' | ') : null,
      graphViewport: vp ? vp.getAttribute('style') : null,
    };
  });
}

// ---------- clip runner ----------
const lag = { max: 0, last: now() };
setInterval(() => { const n = now(); lag.max = Math.max(lag.max, n - lag.last - 0.05); lag.last = n; }, 50).unref();
async function runClip(id, spec) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: VIEWPORT, deviceScaleFactor: 1, reducedMotion: 'no-preference', colorScheme: 'light', locale: 'en-US' });
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', (e) => errors.push(e.message));
  const log = { id, route: spec.route, base: BASE, appCommit: APP_COMMIT, appWorkingTreeDirty: APP_DIRTY, viewport: VIEWPORT, setup: [], observations: [], actions: [] };
  let rec = null;
  let scheduled = null;
  const t = () => (rec ? round(now() - rec.t0) : null);
  const ctx = {
    page,
    clock: () => t(),
    note: (text) => log.setup.push(text),
    async observe(name, extra = {}) {
      const d = await domState(page);
      const o = { t: t(), name, ...d, ...extra };
      log.observations.push(o);
      console.log(id, o.t, name, d.footerFrame, JSON.stringify(d.notes), d.statusRegion, JSON.stringify(extra), 'lag', round(lag.max, 3), 'pending', rec?.pendingWrites?.());
      lag.max = 0;
      return o;
    },
    async at(seconds) { scheduled = seconds; if (rec) await sleep((rec.t0 + seconds - now()) * 1000); },
    act(name, fn) {
      return (async () => {
        const start = t();
        await fn();
        log.actions.push({ t: start, tDone: t(), scheduled, action: name });
      })();
    },
    async click(name, locator) {
      const c = await center(locator);
      await ctx.act(name, async () => { await page.mouse.move(c.x, c.y); await page.mouse.down(); await page.mouse.up(); });
    },
    async hover(name, locator) {
      const c = await center(locator);
      await ctx.act(name, () => page.mouse.move(c.x, c.y));
    },
    async poster() {
      await mkdir(path.join(OUT, 'posters'), { recursive: true });
      const file = path.join(OUT, 'posters', id + '.png');
      const time = t();
      await page.screenshot({ path: file, caret: 'initial' });
      log.poster = { file: 'posters/' + id + '.png', t: time, state: await domState(page) };
    },
    /** A full-page still for the deck, besides the poster, with what it shows. */
    async still(name, extra = {}) {
      await mkdir(path.join(OUT, 'stills'), { recursive: true });
      const time = t();
      await page.screenshot({ path: path.join(OUT, 'stills', name + '.png'), caret: 'initial' });
      (log.stills ??= []).push({ file: 'stills/' + name + '.png', t: time, state: await domState(page), ...extra });
    },
  };
  try {
    await spec.setup(ctx);
    rec = await startRecorder(page, path.join(OUT, 'raw', id));
    log.recording = { method: 'CDP Page.startScreencast (jpeg, quality 92, 1440x900, every frame acked)', t0Epoch: rec.t0 };
    await spec.clip(ctx, spec);
    await ctx.at(spec.end);
    rec.tEnd = now();
    await ctx.observe('end');
    await rec.stop();
    log.recording.tEndEpoch = rec.tEnd;
    log.recording.screencastFrames = rec.frames.length;
    log.recording.firstFrameBeforeStart = rec.frames[0].ts <= rec.t0;
    log.recording.medianFrameLatency = round([...rec.frames.map((f) => f.recv - f.ts)].sort((a, b) => a - b)[Math.floor(rec.frames.length / 2)], 4);
    log.recording.frameSize = [...new Set(rec.frames.map((f) => `${f.w}x${f.h}`))];
    if (FFMPEG) {
      await mkdir(path.join(OUT, 'clips'), { recursive: true });
      log.encode = await encode(rec, path.join(OUT, 'clips', id + '.mp4'));
    }
    log.maxActionLateness = round(Math.max(0, ...log.actions.map((a) => a.t - (a.scheduled ?? a.t))));
    console.log(id, 'max action lateness', log.maxActionLateness, 's');
    log.pageErrors = errors;
    if (errors.length) throw new Error('page errors: ' + errors.join('; '));
  } catch (error) {
    await page.screenshot({ path: path.join(OUT, id + '-failed.png') }).catch(() => {});
    log.failure = String(error?.stack ?? error);
    throw error;
  } finally {
    await mkdir(path.join(OUT, 'checks'), { recursive: true });
    await writeFile(path.join(OUT, 'checks', id + '.json'), JSON.stringify(log, null, 2) + '\n');
    await context.close();
    await browser.close();
  }
}

// ---------- the graph used by Codex's stills: directed Dijkstra S, A, B, T ----------
async function setupGraph(ctx, algorithm = 'dijkstra') {
  const { page } = ctx;
  await ready(page, '/graph-editor/' + algorithm);
  await page.getByRole('checkbox', { name: 'Live force layout', exact: true }).uncheck();
  await page.locator('#graph-nodes-text').fill('S\nA\nB\nT');
  await page.locator('#graph-edges-text').fill('S A 4\nS B 1\nB A 1\nA T 2\nB T 6');
  await page.getByRole('checkbox', { name: 'Directed graph', exact: true }).check();
  if (algorithm === 'dijkstra') {
    await page.getByRole('combobox', { name: 'Dijkstra start node', exact: true }).selectOption({ label: 'S' });
    await page.getByRole('combobox', { name: 'Dijkstra end node', exact: true }).selectOption({ label: 'T' });
  }
  await page.getByRole('button', { name: 'Draw graph', exact: true }).click(); // collapses Draw graph
  await page.waitForTimeout(500);
  // The app's own Fit view before and after the drags, so the framing is the same on every run.
  await page.getByRole('button', { name: 'Fit view', exact: true }).click();
  await page.waitForTimeout(900);
  for (const [label, p] of [['S', { x: 445, y: 440 }], ['A', { x: 710, y: 275 }], ['B', { x: 710, y: 595 }], ['T', { x: 980, y: 440 }]]) {
    await dragPath(page, await center(graphNode(page, label)), p, 300);
  }
  await page.getByRole('button', { name: 'Fit view', exact: true }).click();
  await page.waitForTimeout(900);
  if ((await page.locator('.react-flow__node').count()) !== 4) throw new Error('expected 4 nodes');
  if ((await page.locator('.react-flow__edge').count()) !== 5) throw new Error('expected 5 edges');
  ctx.note('Graph Editor /graph-editor/' + algorithm + ': Live force layout off; nodes S A B T; directed edges S A 4, S B 1, B A 1, A T 2, B T 6' +
    (algorithm === 'dijkstra' ? '; start S, end T' : '') + '; Draw graph collapsed; Fit view; nodes dragged to S(445,440) A(710,275) B(710,595) T(980,440); Fit view.');
}
async function graphToFrame(ctx, target) {
  const { page } = ctx;
  for (let i = 0; i < 40; i++) {
    await footerButton(page, 'Next').click();
    if ((await frameText(page)).startsWith(`FRAME ${target} /`)) return;
  }
  throw new Error('did not reach frame ' + target);
}
// The weight label of edge from -> to: the label nearest the midpoint of the two node centres.
async function edgeLabel(page, from, to) {
  const a = await center(graphNode(page, from));
  const b = await center(graphNode(page, to));
  return page.evaluate(({ a, b }) => {
    const mx = (a.x + b.x) / 2;
    const my = (a.y + b.y) / 2;
    const labels = [...document.querySelectorAll('.react-flow__edgelabel-renderer [class*="edgeLabel"]')].map((e) => {
      const r = e.getBoundingClientRect();
      return { text: e.textContent.trim(), d: Math.hypot(r.x + r.width / 2 - mx, r.y + r.height / 2 - my) };
    }).sort((p, q) => p.d - q.d);
    return labels[0] ? { text: labels[0].text, distanceFromMidpoint: Math.round(labels[0].d) } : null;
  }, { a, b });
}

// ---------- LCA (Tree Editor, Binary Lifting, Query) ----------
const DEFAULT_TREE = '12 8\n4 8\n14 12\n10 12\n6 4\n2 4';
async function setupLca(ctx, u, v, startFrame) {
  const { page } = ctx;
  await ready(page, '/tree-editor/lca-binary-lifting');
  const text = await page.locator('#tree-edges-text').inputValue();
  if (text !== DEFAULT_TREE) throw new Error('unexpected default tree: ' + JSON.stringify(text));
  if ((await page.locator('[aria-label="Root node"]').inputValue()) !== '8') throw new Error('root is not 8');
  const checked = await page.locator('[aria-label="Binary Lifting operation"] [aria-checked="true"]').innerText();
  if (checked.trim() !== 'Query') throw new Error('operation is not Query: ' + checked);
  await page.locator('[aria-label="Binary Lifting node u"]').selectOption(u);
  await page.locator('[aria-label="Binary Lifting node v"]').selectOption(v);
  await footerButton(page, 'Next').click(); // Next starts the Query run at frame 1
  for (let f = 1; f < startFrame; f++) await footerButton(page, 'Next').click();
  await page.waitForTimeout(2300); // any arrival note (1.6 s) has gone
  const frame = await frameText(page);
  if (!frame.startsWith(`FRAME ${startFrame} /`)) throw new Error('start frame ' + frame);
  ctx.note(`Tree Editor /tree-editor/lca-binary-lifting, default tree (${DEFAULT_TREE.replace(/\n/g, ', ')}), root 8, default layout; Query; u = ${u}, v = ${v}; Next started the run; paused at ${frame}.`);
}

// ---------- V10 layout helpers (read-only DOM reads, real pointer drags) ----------
// Regions, their groups and tabs (* = the group's front tab), and where Status is.
function layoutInfo(page) {
  return page.evaluate(() => {
    const box = (e) => { const r = e.getBoundingClientRect(); return [r.x, r.y, r.width, r.height].map(Math.round); };
    const regions = {};
    for (const region of document.querySelectorAll('[data-region]')) {
      const groups = [...region.querySelectorAll('section.group[data-group]')];
      regions[region.dataset.region] = {
        box: box(region),
        groupCount: groups.length,
        groups: groups.map((g) => ({
          id: g.dataset.group,
          tabs: [...g.querySelectorAll('[data-panel-tab]')].map((tab) => tab.dataset.panelTab + (tab.getAttribute('aria-selected') === 'true' ? '*' : '')),
          box: box(g),
        })),
      };
    }
    const status = document.querySelector('[data-panel-tab="status"]');
    return {
      statusRegion: status?.closest('[data-region]')?.dataset.region ?? null,
      statusGroup: status?.closest('[data-group]')?.dataset.group ?? null,
      statusFront: status?.getAttribute('aria-selected') === 'true',
      regions,
    };
  });
}
// The drawing: same React Flow element as at the clip start (no remount), its box, viewport and node centres.
function canvasInfo(page, flowAtStart) {
  return page.evaluate((start) => {
    const flow = document.querySelector('.react-flow');
    const r = flow.getBoundingClientRect();
    const nodes = {};
    for (const node of document.querySelectorAll('.react-flow__node')) {
      const label = node.querySelector('[class*="nodeLabel"]')?.textContent.trim();
      const b = node.getBoundingClientRect();
      nodes[label] = [Math.round(b.x + b.width / 2), Math.round(b.y + b.height / 2)];
    }
    return {
      sameFlowElement: start === flow,
      flowStillConnected: start.isConnected,
      canvasBox: [r.x, r.y, r.width, r.height].map(Math.round),
      viewport: document.querySelector('.react-flow__viewport')?.getAttribute('style'),
      nodes,
    };
  }, flowAtStart);
}
// Press a tab, then move at constant speed for `ms` to the centre of the drop target `key`
// (measured once the drag is live), logging every change of the hot target on the way.
async function slowTabDrag(ctx, name, tabId, key, ms) {
  const { page } = ctx;
  const from = await center(page.locator(`[data-panel-tab="${tabId}"]`));
  const hot = [];
  let to = null;
  await ctx.act(name, async () => {
    await page.mouse.move(from.x, from.y);
    await page.mouse.down();
    await page.mouse.move(from.x, from.y + 8); // past the 6px threshold: the targets are drawn
    const targets = await page.locator('[data-drop-target]').evaluateAll((es) => es.map((e) => ({ key: e.dataset.dropTarget, box: e.getBoundingClientRect().toJSON() })));
    const target = targets.find((t) => t.key === key);
    if (!target) throw new Error(`no drop target ${key}; have ${targets.map((t) => t.key).join(', ')}`);
    to = { x: Math.round(target.box.x + target.box.width / 2), y: Math.round(target.box.y + target.box.height / 2) };
    const start = now();
    for (let f = 0; f < 1;) {
      f = Math.min(1, (now() - start) / (ms / 1000));
      await page.mouse.move(from.x + (to.x - from.x) * f, from.y + 8 + (to.y - from.y - 8) * f);
      const h = await page.evaluate(() => document.querySelector('[data-drop-target][data-hot="true"]')?.dataset.dropTarget ?? null);
      if (hot.length === 0 || hot.at(-1).target !== h) hot.push({ t: ctx.clock(), target: h });
      if (f < 1) await sleep(25);
    }
  });
  return { from: { x: Math.round(from.x), y: Math.round(from.y) }, to, hotTargets: hot };
}
const previewInfo = (page) => page.evaluate(() => {
  const p = document.querySelector('.groups__preview');
  if (!p) return { preview: null, hotTarget: document.querySelector('[data-drop-target][data-hot="true"]')?.dataset.dropTarget ?? null };
  const r = p.getBoundingClientRect();
  return {
    hotTarget: document.querySelector('[data-drop-target][data-hot="true"]')?.dataset.dropTarget ?? null,
    preview: { kind: p.dataset.kind, refused: p.dataset.refused, label: p.innerText.trim(), box: [r.x, r.y, r.width, r.height].map(Math.round) },
  };
});

// ---------- LCA step details: pseudocode line, node centres, notes with their boxes ----------
function lcaState(page) {
  return page.evaluate(() => {
    const nodes = {};
    for (const n of document.querySelectorAll('.react-flow__node')) {
      const r = n.getBoundingClientRect();
      nodes[n.dataset.id] = [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)];
    }
    const lines = [...document.querySelectorAll('.pseudocode-panel__listing li')];
    const notes = [...document.querySelectorAll('.step-notes *')].filter((e) => e.children.length === 0 && e.textContent.trim()).map((e) => {
      const r = e.getBoundingClientRect();
      const cx = r.x + r.width / 2;
      const cy = r.y + r.height / 2;
      // The node the note belongs to: the nearest node centre; dx, dy say where the note sits from it.
      const [id, [nx, ny]] = Object.entries(nodes).sort(([, a], [, b]) => Math.hypot(a[0] - cx, a[1] - cy) - Math.hypot(b[0] - cx, b[1] - cy))[0];
      return {
        text: e.textContent.trim(),
        box: [r.x, r.y, r.width, r.height].map(Math.round),
        nearestNode: id,
        fromNode: [Math.round(cx - nx), Math.round(cy - ny)],
        opacity: Number(getComputedStyle(e.closest('[style]') ?? e).opacity),
      };
    });
    return {
      pseudocodeHint: document.querySelector('.pseudocode-panel__hint')?.textContent.trim() ?? null,
      pseudocodeLit: lines.map((li, i) => (li.classList.contains('pseudocode-panel__line--active') ? `${i + 1}${li.getAttribute('aria-current') === 'step' ? '*' : ''}: ${li.textContent.trim()}` : null)).filter(Boolean),
      nodes,
      noteBoxes: notes,
    };
  });
}

const CLIPS = {
  '01_lca_equal_ancestors': {
    route: '/tree-editor/lca-binary-lifting',
    end: 9.6,
    setup: (ctx) => setupLca(ctx, '6', '2', 1),
    async clip(ctx) {
      const { page } = ctx;
      const next = footerButton(page, 'Next');
      await ctx.observe('start: Query paused at frame 1');
      await ctx.at(0.8); await ctx.click('Next', next); await ctx.at(0.95); await ctx.observe('k = 2 compare');
      await ctx.at(1.3); await ctx.poster();
      await ctx.at(2.8); await ctx.click('Next', next); await ctx.at(2.95); await ctx.observe('k = 1 compare');
      await ctx.at(4.0); await ctx.click('Next', next); await ctx.at(4.15); await ctx.observe('k = 0 compare');
      await ctx.at(5.2); await ctx.click('Next', next); await ctx.at(5.35); await ctx.observe('return parent');
      await ctx.at(6.3); await ctx.click('Next', next); await ctx.at(6.45); await ctx.observe('complete');
      await ctx.at(8.0); await ctx.hover('hover node 6', treeNode(page, '6')); await ctx.at(8.3); await ctx.observe('hover node 6 on the final frame');
    },
  },
  '01c_lca_reroot_8_20': {
    route: '/tree-editor/lca-binary-lifting',
    end: 30, // replaced in clip() once the last frame is reached: the clip ends 2.5 s after the answer
    async setup(ctx) {
      const { page } = ctx;
      await ready(page, '/tree-editor/lca-binary-lifting');
      const checked = await page.locator('[aria-label="Binary Lifting operation"] [aria-checked="true"]').innerText();
      if (checked.trim() !== 'Query') throw new Error('operation is not Query: ' + checked);
      await page.locator('.action-panel__picker').click();
      await page.getByRole('group', { name: 'Samples', exact: true }).getByRole('button').filter({ hasText: 'Balanced · 10 nodes' }).click();
      await page.waitForTimeout(800);
      if ((await page.locator('.action-panel__picker').getAttribute('aria-expanded')) === 'true') await page.locator('.action-panel__picker').click();
      const text = await page.locator('#tree-edges-text').inputValue();
      const expected = '10 4\n4 2\n4 6\n6 8\n10 16\n16 12\n12 14\n16 18\n18 20';
      if (text !== expected) throw new Error('unexpected preset text: ' + JSON.stringify(text));
      if ((await page.locator('[aria-label="Root node"]').inputValue()) !== '10') throw new Error('preset root is not 10');
      await page.locator('[aria-label="Root node"]').selectOption('16'); // Edit tree → Structure → Root
      await page.waitForTimeout(1200);
      await page.locator('[aria-label="Binary Lifting node u"]').selectOption('8');
      await page.locator('[aria-label="Binary Lifting node v"]').selectOption('20');
      await page.waitForTimeout(600);
      await page.getByRole('button', { name: 'Fit view', exact: true }).click();
      await page.waitForTimeout(1200);
      await footerButton(page, 'Next').click(); // Next starts the Query run at frame 1
      await page.waitForTimeout(2300);
      const frame = await frameText(page);
      if (!frame.startsWith('FRAME 1 /')) throw new Error('start frame ' + frame);
      ctx.note(`Tree Editor /tree-editor/lca-binary-lifting, Query; Select preset → "Balanced · 10 nodes" (${expected.replace(/\n/g, ', ')}; preset root 10); Root changed to 16 with Edit tree → Structure → Root; u = 8, v = 20; Fit view; default panel layout; Next started the run; paused at ${frame}; mouse left on the Next button.`);
    },
    async clip(ctx, spec) {
      const { page } = ctx;
      const next = footerButton(page, 'Next');
      const sentenceOf = async () => sentence(await page.locator('[data-panel-body="status"]').innerText());
      const step = async (name) => ctx.observe(name, { statusSentence: await sentenceOf(), ...(await lcaState(page)) });
      const start = await step('start');
      // The three decision moments get a full-page still while their note is shown.
      const stillFor = (status, notes) => (/depth gap .* ≥ .*lifts/.test(status) ? 'lca_8_20_depth_lift'
        : /^k = 1: both ancestors are/.test(status) ? 'lca_8_20_keep'
        : notes.some((n) => n.text === 'differ · lift both') ? 'lca_8_20_lift_both' : null);
      let at = 1.0;
      for (let i = 0; i < 20; i++) {
        await ctx.at(at); await ctx.click('Next', next);
        const arrived = ctx.clock();
        await ctx.at(arrived + 0.15);
        const o = await step('after Next');
        const [, shown, total] = o.footerFrame.match(/FRAME (\d+) \/ (\d+)/);
        const hasNote = o.noteBoxes.length > 0;
        const still = stillFor(o.statusSentence ?? '', o.noteBoxes);
        if (still) { await ctx.at(arrived + 0.45); await ctx.still(still, { frame: o.footerFrame, notes: (await lcaState(page)).noteBoxes }); }
        if (still === 'lca_8_20_lift_both') { await ctx.at(arrived + 0.7); await ctx.poster(); }
        if (shown === total) { spec.end = arrived + 2.5; break; }
        at = arrived + (hasNote ? 2.15 : 1.2);
      }
      ctx.note('Node centres at the start: ' + JSON.stringify(start.nodes));
    },
  },
  '01d_lca_reroot_on_camera_8_20': {
    route: '/tree-editor/lca-binary-lifting',
    end: 40, // set in clip(): 2.5 s after the answer
    async setup(ctx) {
      const { page } = ctx;
      await ready(page, '/tree-editor/lca-binary-lifting');
      const checked = await page.locator('[aria-label="Binary Lifting operation"] [aria-checked="true"]').innerText();
      if (checked.trim() !== 'Query') throw new Error('operation is not Query: ' + checked);
      await page.locator('.action-panel__picker').click();
      await page.getByRole('group', { name: 'Samples', exact: true }).getByRole('button').filter({ hasText: 'Balanced · 10 nodes' }).click();
      await page.waitForTimeout(800);
      if ((await page.locator('.action-panel__picker').getAttribute('aria-expanded')) === 'true') await page.locator('.action-panel__picker').click();
      if ((await page.locator('[aria-label="Root node"]').inputValue()) !== '10') throw new Error('preset root is not 10');
      if (!(await page.locator('[aria-label="Root node"]').isVisible())) throw new Error('Root control not visible (Edit tree shut?)');
      await page.locator('[aria-label="Binary Lifting node u"]').selectOption('8');
      await page.locator('[aria-label="Binary Lifting node v"]').selectOption('20');
      await page.getByRole('button', { name: 'Fit view', exact: true }).click();
      await page.waitForTimeout(1200);
      await page.mouse.move(1050, 760); // empty canvas
      await page.waitForTimeout(800);
      ctx.note('Tree Editor /tree-editor/lca-binary-lifting, Query; Select preset → "Balanced · 10 nodes" (root 10); preset list closed; Edit tree open (default), so Structure → Root is in view; u = 8, v = 20; Fit view; no run; mouse parked on empty canvas.');
    },
    async clip(ctx, spec) {
      const { page } = ctx;
      // Before/after facts of the re-root, read from the page.
      const treeFacts = () => page.evaluate(() => {
        const tiles = {};
        for (const e of document.querySelectorAll('[data-panel-body="action"] *')) {
          const m = e.innerText?.trim().match(/^(NODES|EDGES|DEPTH)\s+(\d+)$/);
          if (m && e.children.length >= 1 && e.children.length <= 3) tiles[m[1]] = Number(m[2]);
        }
        const nodes = {};
        for (const n of document.querySelectorAll('.react-flow__node')) {
          const r = n.getBoundingClientRect();
          nodes[n.dataset.id] = [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)];
        }
        return {
          root: document.querySelector('[aria-label="Root node"]')?.value,
          rootFocused: document.activeElement?.getAttribute('aria-label') === 'Root node',
          picker: document.querySelector('.action-panel__picker-name')?.textContent.trim(),
          u: document.querySelector('[aria-label="Binary Lifting node u"]')?.value,
          v: document.querySelector('[aria-label="Binary Lifting node v"]')?.value,
          tiles,
          nodeCount: Object.keys(nodes).length,
          edgesText: document.querySelector('#tree-edges-text')?.value,
          footer: document.querySelector('.footer-bar__frame')?.innerText,
          viewport: document.querySelector('.react-flow__viewport')?.style.transform,
          nodes,
        };
      });
      const before = await treeFacts();
      await ctx.observe('start: root 10', { tree: before });
      // 1. Focus the Root control with the keyboard: a click at the end of the Edges text, then Tab.
      const box = await page.locator('#tree-edges-text').boundingBox();
      await ctx.at(1.5);
      await ctx.act('click at the end of the Edges text', async () => { await page.mouse.move(box.x + box.width - 20, box.y + box.height - 15); await page.mouse.down(); await page.mouse.up(); });
      await ctx.at(1.75); await ctx.act('Tab to Structure → Root', () => page.keyboard.press('Tab'));
      await ctx.at(1.9); await ctx.observe('Root focused', { tree: await treeFacts() });
      // 2. Type "16": the closed select's type-ahead moves 10 → 16 in one change (options run 10, 4, 2, 6, 8, 16, …).
      await ctx.at(2.4);
      const typed = ctx.clock();
      await ctx.act('type "16" in the Root control', () => page.keyboard.type('16', { delay: 150 }));
      // Track the re-layout until the node centres and viewport hold still for 0.3 s.
      const track = [];
      let rerootAt = null;
      let last = null;
      let stillSince = null;
      for (let i = 0; i < 40; i++) {
        const f = await treeFacts();
        const now2 = ctx.clock();
        if (rerootAt === null && f.root === '16') rerootAt = now2;
        const key = JSON.stringify([f.nodes, f.viewport]);
        track.push({ t: now2, root: f.root, n16: f.nodes['16'], n8: f.nodes['8'], viewport: f.viewport });
        if (rerootAt !== null && key === last) { stillSince ??= now2; if (now2 - stillSince >= 0.3) break; } else stillSince = null;
        last = key;
        await sleep(80);
      }
      const after = await treeFacts();
      await ctx.observe('after the re-root', { tree: after, typedAt: typed, rootChangedBy: rerootAt, settledBy: stillSince, track });
      if (after.u !== '8' || after.v !== '20') throw new Error('u/v were not kept: ' + after.u + ', ' + after.v);
      // 3. Next starts the run; every step as in 01c, holds 2.0 s with a note, 1.2 s without, 2.5 s on the answer.
      const next = footerButton(page, 'Next');
      const sentenceOf = async () => sentence(await page.locator('[data-panel-body="status"]').innerText());
      const runStart = await lcaState(page);
      let at = Math.max(ctx.clock() + 0.1, typed + 2.6);
      for (let i = 0; i < 20; i++) {
        await ctx.at(at); await ctx.click('Next', next);
        await ctx.at(at + 0.15);
        const o = await ctx.observe('after Next', { statusSentence: await sentenceOf(), ...(await lcaState(page)) });
        const [, shown, total] = o.footerFrame.match(/FRAME (\d+) \/ (\d+)/);
        if (o.noteBoxes.some((n) => n.text === 'differ · lift both')) { await ctx.at(at + 0.7); await ctx.poster(); }
        if (shown === total) { spec.end = at + 2.5; break; }
        at += o.noteBoxes.length > 0 ? 2.0 : 1.2;
      }
      ctx.note('Node centres when the run started: ' + JSON.stringify(runStart.nodes));
    },
  },
  '01b_lca_keep_then_jump': {
    route: '/tree-editor/lca-binary-lifting',
    end: 10.3,
    setup: (ctx) => setupLca(ctx, '6', '10', 2),
    async clip(ctx) {
      const { page } = ctx;
      const next = footerButton(page, 'Next');
      await ctx.observe('start: paused at frame 2 (k = 2, both 8)');
      await ctx.at(0.8); await ctx.click('Next', next); await ctx.at(0.95); await ctx.observe('k = 1 compare');
      await ctx.at(2.8); await ctx.click('Next', next); await ctx.at(2.95); await ctx.observe('k = 0 compare');
      await ctx.at(3.3); await ctx.poster();
      await ctx.at(4.9); await ctx.click('Next', next); await ctx.at(5.05); await ctx.observe('lift both');
      await ctx.at(6.7); await ctx.click('Next', next); await ctx.at(6.85); await ctx.observe('return parent');
      await ctx.at(8.0); await ctx.click('Next', next); await ctx.at(8.15); await ctx.observe('complete');
    },
  },
  '02_v10_move_panel': {
    route: '/graph-editor/dijkstra',
    end: 7.3,
    async setup(ctx) {
      await setupGraph(ctx);
      await graphToFrame(ctx, 12);
      await ctx.page.mouse.move(1050, 720); // empty canvas, nothing hovered
      await ctx.page.waitForTimeout(2300);
      ctx.note('Next to frame 12; mouse parked on empty canvas.');
    },
    async clip(ctx) {
      const { page } = ctx;
      await ctx.observe('start');
      const tab = await center(page.locator('[data-panel-tab="status"]'));
      const target = { x: 150, y: 450 }; // the left group's body: the drop target "group:g1"
      await ctx.at(1.0);
      await ctx.act('press Status tab', async () => { await page.mouse.move(tab.x, tab.y); await page.mouse.down(); });
      await ctx.act('drag Status tab to the left group', async () => {
        for (let i = 1; i <= 12; i++) {
          await page.mouse.move(tab.x + (target.x - tab.x) * i / 12, tab.y + (target.y - tab.y) * i / 12);
          await sleep(40);
        }
      });
      await ctx.at(2.3);
      const hot = await page.evaluate(() => ({
        hotTarget: document.querySelector('[data-drop-target][data-hot="true"]')?.dataset.dropTarget ?? null,
        preview: !!document.querySelector('.groups__preview, .groups__preview-caret'),
        dragging: document.querySelector('.viz-page__body.groups')?.dataset.dragging ?? null,
      }));
      await ctx.observe('drop preview', hot);
      await ctx.at(2.6); await ctx.act('release', () => page.mouse.up());
      await ctx.at(2.75); await ctx.observe('dropped');
      await ctx.at(3.1); await ctx.poster();
      await ctx.at(4.5); await ctx.click('open Settings', page.getByRole('button', { name: 'Settings', exact: true }));
      await ctx.at(4.65); await ctx.observe('Settings open', { menu: await page.getByRole('menu').innerText().catch(() => null) });
      await ctx.at(5.2); await ctx.click('Reset panel layout', page.getByRole('menuitem', { name: 'Reset panel layout', exact: true }));
      await ctx.at(5.35); await ctx.observe('after Reset panel layout');
      await ctx.at(5.7); await ctx.act('Escape closes the menu', () => page.keyboard.press('Escape'));
      await ctx.at(5.9); await ctx.observe('menu closed', { menuOpen: await page.locator('.va-settings__menu').isVisible() });
    },
  },
  '02b_v10_split_left_bottom': {
    route: '/graph-editor/dijkstra',
    end: 16.3,
    async setup(ctx) {
      const { page } = ctx;
      await setupGraph(ctx);
      await graphToFrame(ctx, 12);
      // Off camera: Status into the Pseudocode group as its second tab (that group's strip slot 1), with real drags.
      const pseudo = await page.locator('[data-panel-tab="pseudocode"]').evaluate((e) => e.closest('[data-group]').dataset.group);
      const tab = await center(page.locator('[data-panel-tab="status"]'));
      await page.mouse.move(tab.x, tab.y);
      await page.mouse.down();
      await page.mouse.move(tab.x, tab.y - 10, { steps: 2 });
      const slots = await page.locator('[data-drop-target]').evaluateAll((es) => es.map((e) => ({ key: e.dataset.dropTarget, box: e.getBoundingClientRect().toJSON() })));
      const slot = slots.find((s) => s.key === `group:${pseudo}:1`);
      if (!slot) throw new Error('no strip slot after Pseudocode');
      await page.mouse.move(slot.box.x + 40, slot.box.y + slot.box.height / 2, { steps: 15 });
      await page.waitForTimeout(300);
      await page.mouse.up();
      await page.waitForTimeout(800);
      let layout = await layoutInfo(page);
      if (!layout.statusFront) {
        await page.locator('[data-panel-tab="status"]').click();
        await page.waitForTimeout(500);
        layout = await layoutInfo(page);
      }
      const right = layout.regions.right;
      if (right.groupCount !== 1 || right.groups[0].tabs.join('|') !== 'pseudocode|status*') throw new Error('setup layout: ' + JSON.stringify(right));
      await page.mouse.move(1050, 720); // empty canvas, nothing hovered
      await page.waitForTimeout(2300);
      ctx.note(`Next to frame 12; then, off camera, the Status tab dragged into the Pseudocode group's tab strip after Pseudocode (drop target group:${pseudo}:1); Status is the front tab: right column = one group ${right.groups[0].id} with tabs Pseudocode | Status. Mouse parked on empty canvas.`);
    },
    async clip(ctx) {
      const { page } = ctx;
      const flow = await page.evaluateHandle(() => document.querySelector('.react-flow'));
      const snap = async (name, extra = {}) => ctx.observe(name, { layout: await layoutInfo(page), canvas: await canvasInfo(page, flow), ...extra });
      const drags = [];
      await snap('start');
      // 1. Down from the tab strip into the lower part of its own group: the group splits.
      const own = (await layoutInfo(page)).statusGroup;
      await ctx.at(1.5);
      drags.push(await slowTabDrag(ctx, 'drag 1: Status down into the lower part of its own group', 'status', `split:${own}:after`, 2200));
      await ctx.at(3.95); await ctx.observe('drag 1 over its target', await previewInfo(page));
      await ctx.at(4.4); await ctx.act('release 1', () => page.mouse.up());
      await ctx.at(4.6); await snap('just after drop 1');
      await ctx.at(6.0); await snap('settled after drop 1');
      // 2. Into the left group, beside Action and E-Lecture.
      const left = (await layoutInfo(page)).regions.left.groups[0].id;
      await ctx.at(6.3);
      drags.push(await slowTabDrag(ctx, 'drag 2: Status into the left group', 'status', `group:${left}`, 2200));
      await ctx.at(8.7); await ctx.observe('drag 2 over its target', await previewInfo(page));
      await ctx.at(9.2); await ctx.act('release 2', () => page.mouse.up());
      await ctx.at(9.4); await snap('just after drop 2');
      await ctx.at(10.8); await snap('settled after drop 2');
      // 3. To the bottom region, centred under the drawing.
      await ctx.at(11.1);
      drags.push(await slowTabDrag(ctx, 'drag 3: Status to the bottom region', 'status', 'region:bottom', 2200));
      await ctx.at(13.5); await ctx.observe('drag 3 over its target', await previewInfo(page));
      await ctx.at(14.0); await ctx.act('release 3', () => page.mouse.up());
      await ctx.at(14.2); await snap('just after drop 3');
      await ctx.at(15.4); await snap('settled after drop 3');
      await ctx.poster();
      await ctx.at(16.2); await snap('final', { drags });
    },
  },
  '03_graph_drag_then_edit': {
    route: '/graph-editor/dijkstra',
    end: 8.0,
    async setup(ctx) {
      await setupGraph(ctx);
      await graphToFrame(ctx, 12);
      await ctx.page.mouse.move(1050, 720);
      await ctx.page.waitForTimeout(2300);
      ctx.note('Next to frame 12; mouse parked on empty canvas.');
    },
    async clip(ctx) {
      const { page } = ctx;
      const edges = page.locator('#graph-edges-text');
      // The Edges text exists only while Draw graph is open.
      const label = async () => ({ edgeBA: await edgeLabel(page, 'B', 'A'), edgesText: (await edges.count()) ? await edges.inputValue() : '(Draw graph collapsed)' });
      await ctx.observe('start', await label());
      const b = await center(graphNode(page, 'B'));
      await ctx.at(0.8);
      await ctx.act('drag B up-right by (35, -35)', () => dragPath(page, b, { x: b.x + 35, y: b.y - 35 }, 300));
      await ctx.observe('after drag', { ...(await label()), bCentre: await center(graphNode(page, 'B')), bBefore: b });
      await ctx.at(3.0); await ctx.click('open Draw graph', page.getByRole('button', { name: 'Draw graph', exact: true }));
      await ctx.at(3.2); await ctx.observe('Draw graph open', await label());
      const geo = await page.locator('#graph-edges-text').evaluate((e) => {
        const cs = getComputedStyle(e);
        const r = e.getBoundingClientRect();
        return { x: r.x, y: r.y, w: r.width, top: parseFloat(cs.borderTopWidth) + parseFloat(cs.paddingTop), lh: parseFloat(cs.lineHeight) };
      });
      const line3 = { x: geo.x + geo.w - 30, y: geo.y + geo.top + geo.lh * 2.5 }; // right of "B A 1": the caret lands at the line end
      await ctx.at(3.9);
      await ctx.act('click at the end of line "B A 1"', async () => { await page.mouse.move(line3.x, line3.y); await page.mouse.down(); await page.mouse.up(); });
      await ctx.at(4.05); await ctx.act('Shift+ArrowLeft selects "1"', () => page.keyboard.press('Shift+ArrowLeft'));
      await ctx.at(4.5); await ctx.act('type 5', () => page.keyboard.type('5'));
      await ctx.at(4.7); await ctx.observe('after edit', await label());
      await ctx.at(5.1); await ctx.poster();
    },
  },
  '03b_graph_drag_edit_parallel': {
    route: '/graph-editor/dijkstra',
    end: 16.2,
    async setup(ctx) {
      await setupGraph(ctx);
      await graphToFrame(ctx, 12);
      await ctx.page.mouse.move(1050, 720);
      await ctx.page.waitForTimeout(2300);
      ctx.note('Next to frame 12; mouse parked on empty canvas.');
    },
    async clip(ctx) {
      const { page } = ctx;
      const edges = page.locator('#graph-edges-text');
      // Edges with their endpoints' labels and drawn paths, the weight labels, and the run notices.
      const graphInfo = async () => ({
        edgesText: (await edges.count()) ? await edges.inputValue() : '(Draw graph collapsed)',
        ...(await page.evaluate(() => {
          const names = new Map([...document.querySelectorAll('.react-flow__node')].map((n) => [n.dataset.id, n.querySelector('[class*="nodeLabel"]')?.textContent.trim()]));
          const list = [...document.querySelectorAll('.react-flow__edge')].map((e) => {
            const m = (e.getAttribute('aria-label') ?? '').match(/^Edge from (.+) to (.+)$/);
            return { id: e.dataset.id, from: m ? names.get(m[1]) : null, to: m ? names.get(m[2]) : null, path: e.querySelector('path')?.getAttribute('d') };
          });
          const labels = [...document.querySelectorAll('.react-flow__edgelabel-renderer [class*="edgeLabel"]')].map((l) => {
            const r = l.getBoundingClientRect();
            return { text: l.textContent.trim(), at: [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)] };
          });
          // Labels carry no edge id: give each label to the edge whose drawn curve passes nearest it (screen pixels).
          const flow = document.querySelector('.react-flow').getBoundingClientRect();
          const t = (document.querySelector('.react-flow__viewport')?.style.transform ?? '').match(/translate\(([-\d.]+)px, ([-\d.]+)px\) scale\(([-\d.]+)\)/);
          const [tx, ty, s] = t ? [Number(t[1]), Number(t[2]), Number(t[3])] : [0, 0, 1];
          const curve = (d) => {
            const n = (d ?? '').match(/-?\d+(\.\d+)?/g)?.map(Number) ?? [];
            const [x0, y0, cx, cy, x1, y1] = n.length >= 6 ? n : [n[0], n[1], (n[0] + n[2]) / 2, (n[1] + n[3]) / 2, n[2], n[3]];
            return Array.from({ length: 41 }, (_, i) => {
              const u = i / 40;
              const x = (1 - u) ** 2 * x0 + 2 * u * (1 - u) * cx + u ** 2 * x1;
              const y = (1 - u) ** 2 * y0 + 2 * u * (1 - u) * cy + u ** 2 * y1;
              return [flow.x + tx + s * x, flow.y + ty + s * y];
            });
          };
          const curves = list.map((e) => ({ id: e.id, points: curve(e.path) }));
          for (const label of labels) {
            const near = curves.map((c) => ({ id: c.id, d: Math.min(...c.points.map(([x, y]) => Math.hypot(x - label.at[0], y - label.at[1]))) })).sort((a, b) => a.d - b.d)[0];
            label.edge = near?.id ?? null;
            label.distance = near ? Math.round(near.d) : null;
          }
          for (const e of list) e.labels = labels.filter((l) => l.edge === e.id).map((l) => l.text);
          return {
            edgeCount: list.length,
            edgesBA: list.filter((e) => e.from === 'B' && e.to === 'A'),
            labelCount: labels.length,
            labels,
            notices: [...new Set([...document.querySelectorAll('.action-panel__notice, .viz-alert, [role="alert"]')].map((e) => e.innerText.trim()).filter(Boolean))],
            mentionsParallel: /parallel/i.test(document.body.innerText),
          };
        })),
      });
      await ctx.observe('start', await graphInfo());
      // 1. Drag B a short way: the run stays at frame 12.
      const b = await center(graphNode(page, 'B'));
      await ctx.at(1.0);
      await ctx.act('drag B up-right by (35, -35)', () => dragPath(page, b, { x: b.x + 35, y: b.y - 35 }, 300));
      await ctx.observe('after drag', { ...(await graphInfo()), bCentre: await center(graphNode(page, 'B')), bBefore: b });
      // 2. Draw graph → Edges: "B A 1" becomes "B A 5", which ends the run.
      await ctx.at(3.5); await ctx.click('open Draw graph', page.getByRole('button', { name: 'Draw graph', exact: true }));
      await ctx.at(3.7); await ctx.observe('Draw graph open', await graphInfo());
      const geo = await edges.evaluate((e) => {
        const cs = getComputedStyle(e);
        const r = e.getBoundingClientRect();
        return { x: r.x, y: r.y, w: r.width, top: parseFloat(cs.borderTopWidth) + parseFloat(cs.paddingTop), lh: parseFloat(cs.lineHeight) };
      });
      const line3 = { x: geo.x + geo.w - 30, y: geo.y + geo.top + geo.lh * 2.5 };
      await ctx.at(4.4);
      await ctx.act('click at the end of line "B A 1"', async () => { await page.mouse.move(line3.x, line3.y); await page.mouse.down(); await page.mouse.up(); });
      await ctx.at(4.55); await ctx.act('Shift+ArrowLeft selects "1"', () => page.keyboard.press('Shift+ArrowLeft'));
      await ctx.at(5.0); await ctx.act('type 5', () => page.keyboard.type('5'));
      await ctx.at(5.2); await ctx.observe('after weight edit', await graphInfo());
      // 3. A parallel edge on the canvas: drag from B's source handle (right) to A's target handle (left).
      const src = await center(graphNode(page, 'B').locator('.react-flow__handle.source'));
      await ctx.at(7.2); await ctx.act('pointer onto B\'s source handle', () => page.mouse.move(src.x, src.y));
      const dst = await center(graphNode(page, 'A').locator('.react-flow__handle.target'));
      await ctx.at(7.6);
      await ctx.act('drag a new edge from B to A', async () => {
        await page.mouse.down();
        for (let i = 1; i <= 15; i++) {
          await page.mouse.move(src.x + (dst.x - src.x) * i / 15, src.y + (dst.y - src.y) * i / 15);
          await sleep(80);
        }
      });
      await ctx.at(9.2); await ctx.act('release on A\'s target handle', () => page.mouse.up());
      await ctx.at(9.5); await ctx.act('pointer to empty canvas', () => page.mouse.move(1050, 720));
      await ctx.at(9.7); await ctx.observe('after the parallel edge', { ...(await graphInfo()), handles: { from: src, to: dst } });
      // 4. Give the new edge weight 2: click at the end of the new last line "B A" and type " 2".
      const geo6 = await edges.evaluate((e) => {
        const cs = getComputedStyle(e);
        const r = e.getBoundingClientRect();
        return { x: r.x, y: r.y, w: r.width, top: parseFloat(cs.borderTopWidth) + parseFloat(cs.paddingTop), lh: parseFloat(cs.lineHeight), scrollTop: e.scrollTop };
      });
      const line6 = { x: geo6.x + geo6.w - 30, y: geo6.y + geo6.top + geo6.lh * 5.5 - geo6.scrollTop };
      await ctx.at(10.8);
      await ctx.act('click at the end of the new line "B A"', async () => { await page.mouse.move(line6.x, line6.y); await page.mouse.down(); await page.mouse.up(); });
      const caret = await edges.evaluate((e) => ({ selectionStart: e.selectionStart, selectionEnd: e.selectionEnd, length: e.value.length }));
      if (caret.selectionStart !== caret.length || caret.selectionEnd !== caret.length) throw new Error('caret not at the end of "B A": ' + JSON.stringify(caret));
      await ctx.at(11.2); await ctx.act('type " 2"', () => page.keyboard.type(' 2', { delay: 150 }));
      await ctx.at(11.7); await ctx.observe('after typing 2', { ...(await graphInfo()), click: line6, caretBeforeTyping: caret });
      // 5. Pointer off to empty canvas; hold on the result.
      await ctx.at(12.2); await ctx.act('pointer to empty canvas', () => page.mouse.move(1050, 720));
      await ctx.at(12.4); await ctx.observe('final state', await graphInfo());
      await ctx.at(13.2); await ctx.poster();
    },
  },
  '04_dijkstra_note_pause_hover': {
    route: '/graph-editor/dijkstra',
    end: 10.2,
    async setup(ctx) {
      await setupGraph(ctx);
      await graphToFrame(ctx, 11);
      await ctx.page.waitForTimeout(1800);
      ctx.note('Next to frame 11; mouse left on the Next button.');
    },
    async clip(ctx) {
      const { page } = ctx;
      const paused = () => page.evaluate(() => document.getAnimations().map((a) => ({ name: a.animationName, time: Math.round(a.currentTime) })).filter((a) => a.name?.includes('paused')));
      await ctx.observe('start', { pausedAnimations: await paused() });
      await ctx.at(2.4); await ctx.observe('end of hold', { pausedAnimations: await paused() });
      await ctx.at(2.5); await ctx.click('Next', footerButton(page, 'Next'));
      await ctx.at(2.65); await ctx.observe('frame 12');
      await ctx.at(2.95); await ctx.poster();
      await ctx.at(4.7); await ctx.click('Last', footerButton(page, 'Last'));
      await ctx.at(4.85); await ctx.observe('Last');
      await ctx.at(5.9); await ctx.hover('hover T', graphNode(page, 'T'));
      await ctx.at(6.1); await ctx.observe('hover T');
      await ctx.at(7.9); await ctx.hover('hover A', graphNode(page, 'A'));
      await ctx.at(8.1); await ctx.observe('hover A');
    },
  },
  '04b_dijkstra_big_note_pause_hover': {
    route: '/graph-editor/dijkstra',
    end: 14.0,
    async setup(ctx) {
      const { page } = ctx;
      await ready(page, '/graph-editor/dijkstra');
      // Live force layout off first, so the preset keeps its own positions.
      await page.getByRole('checkbox', { name: 'Live force layout', exact: true }).uncheck();
      await page.locator('.action-panel__picker').click();
      await page.getByRole('group', { name: 'Graph samples' }).getByRole('button', { name: 'Big', exact: true }).click();
      await page.waitForTimeout(800);
      if ((await page.locator('.action-panel__picker').getAttribute('aria-expanded')) === 'true') await page.locator('.action-panel__picker').click();
      const draw = page.getByRole('button', { name: 'Draw graph', exact: true });
      if ((await draw.getAttribute('aria-expanded')) === 'true') await draw.click(); // collapse, as in the other graph clips
      const start = await page.getByRole('combobox', { name: 'Dijkstra start node', exact: true }).inputValue();
      const endSelect = page.getByRole('combobox', { name: 'Dijkstra end node', exact: true });
      const endLabel = await endSelect.evaluate((e) => e.options[e.selectedIndex]?.text);
      if (start !== '0' || endLabel !== 'All vertices') throw new Error(`start ${start}, end ${endLabel}`);
      if ((await page.locator('.react-flow__node').count()) !== 9 || (await page.locator('.react-flow__edge').count()) !== 16) throw new Error('expected 9 nodes, 16 arcs');
      await page.getByRole('button', { name: 'Fit view', exact: true }).click();
      await page.waitForTimeout(900);
      await graphToFrame(ctx, 17);
      const inspect = sentence(await page.locator('[data-panel-body="status"]').innerText());
      if (inspect !== 'Inspect edge 2 → 3, weight 14.') throw new Error('frame 17 is ' + inspect);
      await page.waitForTimeout(1800);
      ctx.note('Graph Editor /graph-editor/dijkstra: Live force layout off; Select preset → Big (visualgo.net TESSELLATION: vertices 0–8, 16 directed weighted arcs, preset positions); preset list closed; Draw graph collapsed; Start node 0, End node left at "All vertices"; Fit view; Next to frame 17 (Inspect edge 2 → 3); mouse left on the Next button.');
    },
    async clip(ctx) {
      const { page } = ctx;
      const node = (id) => page.locator(`.react-flow__node[data-id="${id}"]`);
      const paused = () => page.evaluate(() => document.getAnimations().map((a) => ({ name: a.animationName, time: Math.round(a.currentTime) })).filter((a) => a.name?.includes('paused')));
      await ctx.observe('start', { pausedAnimations: await paused() });
      await ctx.at(2.9); await ctx.observe('end of hold', { pausedAnimations: await paused() });
      await ctx.at(3.0); await ctx.click('Next', footerButton(page, 'Next'));
      await ctx.at(3.15); await ctx.observe('frame 18');
      await ctx.at(3.45); await ctx.poster();
      await ctx.at(6.0); await ctx.click('Last', footerButton(page, 'Last'));
      await ctx.at(6.15); await ctx.observe('Last');
      await ctx.at(7.6); await ctx.hover('hover 8', node('8'));
      await ctx.at(7.8); await ctx.observe('hover 8');
      await ctx.at(10.6); await ctx.hover('hover 4', node('4'));
      await ctx.at(10.8); await ctx.observe('hover 4');
    },
  },
  '05_bst_preview_apply': {
    route: '/tree-editor/bst',
    end: 8.6,
    async setup(ctx) {
      const { page } = ctx;
      await ready(page, '/tree-editor/bst');
      const text = await page.locator('#tree-edges-text').inputValue();
      if (text !== DEFAULT_TREE) throw new Error('unexpected default tree');
      await page.getByRole('radio', { name: 'Insert', exact: true }).click();
      await page.getByRole('textbox', { name: 'BST Insert value', exact: true }).fill('5');
      await page.getByRole('button', { name: 'Edit tree', exact: true }).click(); // collapse
      await footerButton(page, 'Next').click();
      await footerButton(page, 'Last').click();
      await page.waitForTimeout(1500);
      ctx.note('Tree Editor /tree-editor/bst, default tree, Insert, value 5, Edit tree collapsed; Next started the run; Last.');
    },
    async clip(ctx) {
      const { page } = ctx;
      const committed = async () => ({
        committedText: await page.locator('#tree-edges-text').inputValue(),
        canvasNodes: await page.locator('.react-flow__node').count(),
        applyVisible: await page.getByRole('button', { name: 'Apply insertion', exact: true }).isVisible(),
      });
      await ctx.observe('start: completed preview', await committed());
      await ctx.at(0.5); await ctx.poster();
      await ctx.at(1.5); await ctx.click('Previous', footerButton(page, 'Previous')); await ctx.at(1.65); await ctx.observe('back 1', await committed());
      await ctx.at(2.4); await ctx.click('Previous', footerButton(page, 'Previous')); await ctx.at(2.55); await ctx.observe('back 2', await committed());
      await ctx.at(3.3); await ctx.click('Next', footerButton(page, 'Next')); await ctx.at(3.45); await ctx.observe('forward 1', await committed());
      await ctx.at(4.1); await ctx.click('Next', footerButton(page, 'Next')); await ctx.at(4.25); await ctx.observe('forward 2', await committed());
      await ctx.at(5.2); await ctx.click('Apply insertion', page.getByRole('button', { name: 'Apply insertion', exact: true }));
      await ctx.at(5.4); await ctx.observe('applied', await committed());
      await ctx.at(6.2); await ctx.click('expand Edit tree', page.getByRole('button', { name: 'Edit tree', exact: true }));
      await ctx.at(6.45); await ctx.observe('Edit tree open', { ...(await committed()), textareaVisible: await page.locator('#tree-edges-text').isVisible() });
    },
  },
  '06_dfs_recursive_recap': {
    route: '/graph-editor/dfs-recursive',
    end: 8.5,
    async setup(ctx) {
      await setupGraph(ctx, 'dfs-recursive');
      ctx.note('Same graph, Graph Editor /graph-editor/dfs-recursive (default start).');
      await footerButton(ctx.page, 'Next').click();
      await ctx.page.waitForTimeout(800);
    },
    async clip(ctx) {
      const { page } = ctx;
      await ctx.observe('start: run started');
      await ctx.at(0.8); await ctx.click('Last', footerButton(page, 'Last'));
      await ctx.at(1.0); await ctx.observe('final frame');
      await ctx.at(3.0); await ctx.poster();
      await ctx.at(4.5); await ctx.observe('final frame, later');
    },
  },
};

const wanted = process.argv.slice(2);
const ids = wanted.length === 0 || wanted.includes('all') ? Object.keys(CLIPS) : wanted;
for (const id of ids) {
  if (!CLIPS[id]) throw new Error('unknown clip ' + id);
  console.log('== ' + id);
  await runClip(id, CLIPS[id]);
}
