import { createRequire } from 'node:module';
const app = process.env.CA_APP_REPO;
const { chromium } = createRequire(app + '/package.json')('@playwright/test');
const base = process.env.CA_BASE_URL ?? 'http://127.0.0.1:5205';
const out = process.argv[2];
const steps = Number(process.argv[3] ?? 0);
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, reducedMotion: 'no-preference' });
const page = await context.newPage();
const errors = []; page.on('pageerror', (e) => errors.push(e.message));
try {
  await page.goto(base + '/trie');
  await page.locator('.viz-page').waitFor();
  await page.locator('.workspace-loading__message').waitFor({ state: 'hidden' });
  await page.evaluate(async () => { await document.fonts.load('700 14px Inter'); await document.fonts.ready; });
  await page.waitForTimeout(600);
  const next = page.locator('.footer-bar').getByRole('button', { name: 'Next', exact: true });
  for (let i = 0; i < steps; i++) { await next.click(); await page.waitForTimeout(350); }
  await page.waitForTimeout(500);
  const info = {
    frame: await page.locator('.footer-bar__frame').innerText(),
    status: (await page.locator('[data-panel-body="status"]').innerText()).slice(0, 400),
    action: (await page.locator('[data-panel-body="action"]').innerText()).slice(0, 500),
    notes: await page.locator('.step-notes').allInnerTexts(),
    nodes: await page.locator('.react-flow__node').count(),
    errors,
  };
  await page.screenshot({ path: out });
  console.log(JSON.stringify(info, null, 1));
} finally { await browser.close(); }
