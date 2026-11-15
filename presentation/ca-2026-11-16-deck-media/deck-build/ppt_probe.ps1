param([int]$TimeoutSec = 20)
# Read-only check: can PowerPoint be automated right now? Runs the COM call in a
# job so a busy PowerPoint (for example one showing a Protected View window)
# cannot hang the caller. Prints PPT_OK, PPT_NOT_RUNNING or PPT_BLOCKED.
$procs = Get-Process POWERPNT -ErrorAction SilentlyContinue
if (-not $procs) { 'PPT_NOT_RUNNING'; exit 0 }
$job = Start-Job -ScriptBlock {
  try {
    $a = [Runtime.InteropServices.Marshal]::GetActiveObject('PowerPoint.Application')
    $n = $a.Name
    if ($n) { "OK|$n|" + $a.Presentations.Count } else { 'EMPTY' }
  } catch { 'ERR|' + $_.Exception.Message.Split("`n")[0] }
}
if (Wait-Job $job -Timeout $TimeoutSec) {
  $r = Receive-Job $job
  if ("$r" -like 'OK|*') { "PPT_OK $r" } else { "PPT_BLOCKED $r" }
} else {
  Stop-Job $job
  'PPT_BLOCKED timeout'
}
Remove-Job $job -Force
$procs | ForEach-Object { "  pid {0} '{1}'" -f $_.Id, $_.MainWindowTitle }
