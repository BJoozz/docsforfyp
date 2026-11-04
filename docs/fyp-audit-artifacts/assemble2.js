// Assembles FYP_AUDIT_HANDOFF.md (v2, ten-section layout) from hand.md and the generated parts.
// Usage: node assemble2.js <genDir> <outFile>
const fs = require('fs');
const [g, outFile] = process.argv.slice(2);
const r = f => fs.readFileSync(g + '/' + f, 'utf8');
let doc = r('hand.md')
  .replace('{{STATS}}', r('gen-stats.md').trim())
  .replace('{{GEN_AGENTS}}', r('gen-agents.md').trim())
  .replace('{{GEN_INDEX}}', r('gen-index.md').trim())
  .replace('{{GEN_UNCERTAIN}}', r('gen-uncertain.md').trim());
if (/\{\{[A-Z_]+\}\}/.test(doc)) throw new Error('unreplaced placeholder');
doc += '\n## Appendix A. Full confirmed findings with evidence (generated)\n\n' +
  'Page, severity and fix are as the verifier corrected them; a different finder severity is shown in brackets. The **Verifier** line is the verifier reasoning.\n\n' + r('gen-findings.md') +
  '\n---\n\n## Appendix B. Refuted findings (generated; do not re-raise without new evidence)\n\n' + r('gen-refuted.md') +
  '\n---\n\n## Appendix C. Positives noted by the finders (generated; strengths to keep)\n\n' + r('gen-positives.md') +
  '\n---\n\n*End of handoff. Generated parts come from workflow run wf_976de5d7-7c7; its journal is local to Bao machine, and its full content is in fyp-audit-panel-results.json.*\n';
fs.writeFileSync(outFile, doc);
console.log('bytes', Buffer.byteLength(doc), 'lines', doc.split('\n').length);
