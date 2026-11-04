// Assembles FYP_AUDIT_HANDOFF.md from the hand-written and generated parts.
// Usage: node assemble.js <genDir> <outFile>
const fs = require('fs');
const [g, outFile] = process.argv.slice(2);
const r = f => fs.readFileSync(g + '/' + f, 'utf8');
const mid = r('mid.md').replace('{{STATS}}', r('gen-stats.md').trim());
if (mid.includes('{{')) throw new Error('unreplaced placeholder in mid.md');
const parts = [
  r('head.md'),
  mid,
  '## 9. Agent-by-agent progress (generated)\n\n' +
    'Each slice had one finder and one adversarial verifier, both Opus at max effort, and **all 30 completed**. ' +
    'The finder notes are verbatim. They hold each criterion reviewer\'s verdict, the `crit-report` cut list, the `official` source list, and the `qa` slide outline and demo script.\n\n' +
    r('gen-agents.md'),
  '\n---\n\n## 10. Index of confirmed findings (generated; sorted by severity, then slice)\n\n' +
    'This index covers the verifier-confirmed findings and the ones the verifiers added. The full text of each, with evidence and the verifier\'s reasoning, is in Appendix A.\n\n' +
    r('gen-index.md'),
  '\n---\n\n## 11. Unverified claims: uncertain findings and items needing the owner (generated)\n\n' +
    'The verifiers could not settle these from the repositories. Each hinges on something only Bao knows. Section 5 restates them as questions.\n\n' +
    r('gen-uncertain.md'),
  '\n---\n\n## Appendix A. Full confirmed findings with evidence (generated)\n\n' +
    'The page, severity and fix are as the verifier corrected them; any severity the finder gave differently is shown in brackets. The **Verifier** line is the verifier\'s own reasoning.\n\n' +
    r('gen-findings.md'),
  '\n---\n\n## Appendix B. Refuted findings (generated; do not re-raise without new evidence)\n\n' + r('gen-refuted.md'),
  '\n---\n\n## Appendix C. Positives noted by the finders (generated; strengths to keep)\n\n' + r('gen-positives.md'),
  '\n---\n\n*End of handoff. The generated sections come from workflow run wf_976de5d7-7c7. Its journal is on Bao\'s machine only: ~/.claude/projects/<project>/<session>/subagents/workflows/wf_976de5d7-7c7/journal.jsonl. Everything in it is in fyp-audit-panel-results.json.*\n',
];
const out = parts.join('');
fs.writeFileSync(outFile, out);
console.log('bytes', Buffer.byteLength(out), 'lines', out.split('\n').length);
