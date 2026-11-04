// Turns the review-panel journal into Markdown sections and a JSON archive.
// Usage: node gen-handoff.js <journal.jsonl> <outDir>
const fs = require('fs');
const path = require('path');
const [journal, outDir] = process.argv.slice(2);
const L = fs.readFileSync(journal, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l));

const TASKS = {
  timeline: 'Fact-check every date, period and sequence claim (pp. 2, 4, 11, 13, 14, 16; Table 1) against git, PR dates, the standalone clones and evidence doc 01; check the Week 10 / floating-text chronology.',
  counts: 'Fact-check every number in the report (algorithm counts, catalogue cards, Table 3 test totals, versions, chunk size, CI runs, randomized-test sizes, layout minimums, sorting buffers, note timings) against evidence docs and code at 662e7b3.',
  architecture: 'Fact-check the architecture and design claims of pp. 5-8 (sections 4.1-4.5, Figure 1, Table 2, Figure 2) against evidence doc 03, research note 06, ARCHITECTURE.md files and the code.',
  algorithms: 'Fact-check the algorithm, validation and figure claims of pp. 9-10 (sections 4.6-4.7) and every screenshot caption (Figures 3-9) against code, tests, figures/README.md and the PNGs.',
  floating: 'Fact-check the floating-text / step-note claims (section 4.8, p. 11, p. 13, abstract) against the code, design records and PRs #29, #30, #32, including the "following the Week 10 trial" chronology and terminology.',
  contributions: 'Fact-check contribution and collaboration statements (pp. 2, 4-5, 9, 13, 16) against evidence docs 01/02/05, research note 09, the V10 proposal choices 1-48 and git authorship.',
  literature: 'Verify each bibliography entry and the claims attributed to external works on the web; check whether the evidence-pack URLs resolve; suggest verified additional works.',
  official: 'Research the official NUS SoC CP4101 CA requirements (length, cover page, components and weights, AI declaration) and the AY2026/27 Semester 1 calendar on the web; compare the report against each official requirement.',
  'crit-problem': 'Criterion review: Problem Understanding (claimed 30%) - motivation, problem statement, objectives, scope, limitations.',
  'crit-technical': 'Criterion review: Technical Achievement (claimed 40%) - methodology, design rationale, implementation, individual contribution, preliminary results.',
  'crit-literature': 'Criterion review: Literature Review - coverage, critical comparison, justification of the approach, self-citation of the evidence pack.',
  'crit-management': 'Criterion review: Project Management (claimed 10-20%) - Semester 1 progress, initiative, challenges, realism of the Semester 2 plan, risks.',
  'crit-report': 'Criterion review: Report and communication plus PDF presentation - page count, cover, figures, captions, tables, typography, repetition, abbreviations, references; cut list to reach 15 pages.',
  'crit-accuracy': 'Criterion review: Accuracy and evidence discipline - completed vs ongoing vs planned vs collaborator work, consistency across pages, claims stated as fact that the evidence docs mark open.',
  qa: 'CA presentation and Q&A readiness - likely evaluator questions and where the report answers them, slide outline, live demo script.',
};
const ORDER = Object.keys(TASKS);

const label = {};
for (const o of L) if (o.type === 'started') label[o.agentId] = o.label;
const finder = {}, verifier = {}, failed = [];
for (const o of L) {
  if (o.type === 'failed') failed.push(o);
  if (o.type !== 'result') continue;
  const lab = label[o.agentId] || '';
  const [kind, key] = lab.split(':');
  if (kind === 'find') finder[key] = { agentId: o.agentId, ...o.result };
  if (kind === 'verify') verifier[key] = { agentId: o.agentId, ...o.result };
}

const esc = s => String(s == null ? '' : s).replace(/\|/g, '/').replace(/\r?\n/g, ' ');
const sevRank = { Critical: 0, Important: 1, Minor: 2 };
const confirmed = [], uncertain = [], refuted = [], positives = [];
for (const key of ORDER) {
  const f = finder[key], v = verifier[key];
  if (!f) continue;
  for (const p of f.positives || []) positives.push({ key, text: p });
  const list = (f.findings || []).map(x => ({ ...x, id: x.id.startsWith(key) ? x.id : key + '-' + x.id }));
  const byId = new Map(list.map(x => [x.id, x]));
  if (!v) { for (const x of list) uncertain.push({ ...x, slice: key, verdict: 'NOT VERIFIED', verify_reason: 'verifier result unavailable' }); continue; }
  const seen = new Set();
  for (const r of v.results || []) {
    const x = byId.get(r.id) || byId.get(key + '-' + r.id);
    if (!x) continue;
    seen.add(x.id);
    const merged = { ...x, finder_severity: x.severity, severity: r.severity || x.severity, page: r.page || x.page, fix: r.fix || x.fix, verdict: r.verdict, verify_reason: r.reason, slice: key };
    (r.verdict === 'CONFIRMED' ? confirmed : r.verdict === 'UNCERTAIN' ? uncertain : refuted).push(merged);
  }
  for (const x of list) if (!seen.has(x.id)) uncertain.push({ ...x, slice: key, verdict: 'NO VERDICT', verify_reason: 'the verifier returned no verdict for this id' });
  (v.missed || []).forEach((m, i) => confirmed.push({ ...m, id: key + '-added-' + (i + 1), slice: key, verdict: 'ADDED BY VERIFIER', verify_reason: 'raised by the verifier; not separately re-verified' }));
}
const bySev = a => a.slice().sort((p, q) => (sevRank[p.severity] ?? 3) - (sevRank[q.severity] ?? 3) || ORDER.indexOf(p.slice) - ORDER.indexOf(q.slice));

// JSON archive
fs.writeFileSync(path.join(outDir, 'fyp-audit-panel-results.json'), JSON.stringify({
  source: 'workflow wf_976de5d7-7c7 (ca-report-review), 2026-11-04; 15 finders + 15 verifiers completed; synthesis agent failed on a usage limit',
  tasks: TASKS, finder, verifier, failed,
  derived: { confirmed: bySev(confirmed), uncertain: bySev(uncertain), refuted: bySev(refuted), positives },
}, null, 1));

// Stats
const count = (a, s) => a.filter(x => x.severity === s).length;
const stats = [
  '| Bucket | Critical | Important | Minor | Total |', '|---|---|---|---|---|',
  ...[['Confirmed by a verifier', confirmed.filter(x => x.verdict === 'CONFIRMED')], ['Added by a verifier (not re-verified)', confirmed.filter(x => x.verdict !== 'CONFIRMED')], ['Uncertain (owner must confirm)', uncertain], ['Refuted (do not re-raise)', refuted]]
    .map(([n, a]) => `| ${n} | ${count(a, 'Critical')} | ${count(a, 'Important')} | ${count(a, 'Minor')} | ${a.length} |`),
].join('\n');
fs.writeFileSync(path.join(outDir, 'gen-stats.md'), stats + '\n');

// Agent-by-agent
let ag = '';
ORDER.forEach((key, i) => {
  const f = finder[key], v = verifier[key];
  const vc = v ? (v.results || []).reduce((a, r) => (a[r.verdict] = (a[r.verdict] || 0) + 1, a), {}) : null;
  const sev = f ? (f.findings || []).reduce((a, x) => (a[x.severity] = (a[x.severity] || 0) + 1, a), {}) : null;
  const unc = uncertain.filter(x => x.slice === key).map(x => x.id);
  ag += `### ${i + 1}. \`${key}\`\n\n`;
  ag += `- **Assigned task:** ${TASKS[key]}\n`;
  ag += `- **Finder:** ${f ? `completed; ${f.findings.length} findings (${Object.entries(sev).map(([k, n]) => `${n} ${k}`).join(', ')}); ${(f.positives || []).length} positives` : 'RESULT UNAVAILABLE'}\n`;
  ag += `- **Verifier:** ${v ? `completed; ${Object.entries(vc).map(([k, n]) => `${n} ${k}`).join(', ')}; ${(v.missed || []).length} added` : 'RESULT UNAVAILABLE'}\n`;
  ag += `- **Unresolved (owner or further check):** ${unc.length ? unc.map(x => '`' + x + '`').join(', ') : 'none'}\n`;
  if (f && f.notes) ag += `- **Finder notes (verbatim):**\n\n${f.notes.split(/\r?\n/).map(l => '  > ' + l).join('\n')}\n`;
  ag += '\n';
});
ag += `### 16. \`synthesize\` (not part of the 15)\n\n- **Assigned task:** merge the confirmed findings into one Vietnamese review (readiness, top 5, findings by severity, claim-check table, add/cut lists, owner questions, presentation prep, strengths).\n- **Status:** FAILED before producing output ("You've hit your 5-hour limit · resets 2:40pm (Asia/Singapore)"). Nothing from it exists.\n`;
fs.writeFileSync(path.join(outDir, 'gen-agents.md'), ag);

// Index table
const idx = ['| ID | Sev. | Page | Section | Issue (first sentence) | Basis | Owner? |', '|---|---|---|---|---|---|---|',
  ...bySev(confirmed).map(x => `| \`${x.id}\` | ${x.severity} | ${esc(x.page)} | ${esc(x.section)} | ${esc(String(x.issue).split(/(?<=\.)\s/)[0]).slice(0, 220)} | ${x.basis || ''} | ${x.needs_owner_confirmation ? 'yes' : ''} |`)].join('\n');
fs.writeFileSync(path.join(outDir, 'gen-index.md'), idx + '\n');

// Full findings
const full = x => {
  let s = `#### \`${x.id}\` (${x.severity}${x.finder_severity && x.finder_severity !== x.severity ? `, finder said ${x.finder_severity}` : ''}; ${x.verdict})\n\n`;
  s += `- **Where:** page ${esc(x.page)}; ${esc(x.section)}${x.category ? `; category ${esc(x.category)}` : ''}\n`;
  s += `- **Issue:** ${esc(x.issue)}\n`;
  s += `- **Evidence (${x.basis || 'basis not given'}):** ${esc(x.evidence)}\n`;
  s += `- **Proposed fix:** ${esc(x.fix)}\n`;
  if (x.needs_owner_confirmation) s += `- **Owner must confirm:** ${esc(x.confirmation_question || 'yes (no question text given)')}\n`;
  s += `- **Verifier:** ${esc(x.verify_reason)}\n\n`;
  return s;
};
let fl = '';
for (const sev of ['Critical', 'Important', 'Minor']) {
  const a = bySev(confirmed).filter(x => x.severity === sev);
  fl += `### ${sev} (${a.length})\n\n` + a.map(full).join('');
}
fs.writeFileSync(path.join(outDir, 'gen-findings.md'), fl);

// Uncertain + owner questions
let un = bySev(uncertain).map(full).join('');
const oq = bySev(confirmed).filter(x => x.needs_owner_confirmation);
un += `### Confirmed findings that still need the owner's answer (${oq.length})\n\n` + oq.map(x => `- \`${x.id}\` (${x.severity}, p. ${esc(x.page)}): ${esc(x.confirmation_question || x.issue)}`).join('\n') + '\n';
fs.writeFileSync(path.join(outDir, 'gen-uncertain.md'), un);

// Refuted
const rf = ['| ID | Finder sev. | Page | Claimed issue | Why the verifier refuted it |', '|---|---|---|---|---|',
  ...bySev(refuted).map(x => `| \`${x.id}\` | ${x.finder_severity} | ${esc(x.page)} | ${esc(x.issue).slice(0, 300)} | ${esc(x.verify_reason).slice(0, 500)} |`)].join('\n');
fs.writeFileSync(path.join(outDir, 'gen-refuted.md'), rf + '\n');

// Positives
fs.writeFileSync(path.join(outDir, 'gen-positives.md'), positives.map(p => `- [${p.key}] ${esc(p.text)}`).join('\n') + '\n');

// Critical headline list for the hand-written summary
console.log(stats);
console.log('\nCRITICAL / IMPORTANT ids:');
for (const x of bySev(confirmed)) if (x.severity !== 'Minor') console.log(x.severity[0], x.id, '| p.' + x.page, '|', esc(x.issue).slice(0, 230));
console.log('\nUNCERTAIN:');
for (const x of bySev(uncertain)) console.log(x.severity, x.id, '| p.' + x.page, '|', esc(x.issue).slice(0, 200));
