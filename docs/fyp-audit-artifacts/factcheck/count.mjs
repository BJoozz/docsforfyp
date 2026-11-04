import fs from 'node:fs'
const j = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))
console.log('numTotalTestSuites', j.numTotalTestSuites, 'numTotalTests', j.numTotalTests, 'passed', j.numPassedTests, 'failed', j.numFailedTests, 'pending', j.numPendingTests, 'files', j.testResults.length, 'success', j.success)
const BS = String.fromCharCode(92)
const per = {}
for (const f of j.testResults) {
  const name = f.name.split(BS).join('/')
  const m = name.match(/prototypes[/]src[/]([^/]+)[/]/)
  const k = m ? m[1] : 'other:' + name
  per[k] ??= { files: 0, tests: 0, passed: 0, failed: 0 }
  per[k].files++
  for (const a of f.assertionResults) { per[k].tests++; if (a.status === 'passed') per[k].passed++; else per[k].failed++ }
}
console.log(per)
