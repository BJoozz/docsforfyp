import fs from 'node:fs'
const runs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))
console.log('total runs', runs.length)
const by = {}
for (const r of runs) {
  const k = r.workflowName
  by[k] ??= { runs: 0, success: 0, failure: 0, cancelled: 0, other: 0, first: r.createdAt, last: r.createdAt }
  const b = by[k]
  b.runs++
  if (r.conclusion === 'success') b.success++
  else if (r.conclusion === 'failure') b.failure++
  else if (r.conclusion === 'cancelled') b.cancelled++
  else b.other++
  if (r.createdAt < b.first) b.first = r.createdAt
  if (r.createdAt > b.last) b.last = r.createdAt
}
console.log(by)
console.log('runs after 2026-10-31:', runs.filter(r => r.createdAt > '2026-10-31').length)
for (const r of runs.filter(r => r.conclusion === 'failure')) console.log('FAIL', r.createdAt, r.workflowName, r.headSha.slice(0,7), r.event)
