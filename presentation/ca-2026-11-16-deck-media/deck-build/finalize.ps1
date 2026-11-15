param(
  [Parameter(Mandatory = $true)][string]$In,
  [Parameter(Mandatory = $true)][string]$Out
)
# Opens a built deck in PowerPoint (hidden window), makes every embedded video start
# on the next click/arrow key (In Click Sequence, first effect on its slide), and saves
# a PowerPoint-written copy. Never closes other presentations; quits only if it started PowerPoint.
$ErrorActionPreference = 'Stop'
$started = $false
try { $app = [Runtime.InteropServices.Marshal]::GetActiveObject('PowerPoint.Application') }
catch { $app = New-Object -ComObject PowerPoint.Application; $started = $true }
$before = $app.Presentations.Count
$pres = $app.Presentations.Open($In, 0, 0, 0)
if (-not $pres) { throw 'PowerPoint did not return the presentation (it is busy, for example showing a Protected View window). Nothing was changed. Close that window and run again.' }
try {
  foreach ($s in $pres.Slides) {
    $seq = $s.TimeLine.MainSequence
    foreach ($sh in $s.Shapes) {
      if ($sh.Type -ne 16) { continue }
      $has = $false
      for ($i = 1; $i -le $seq.Count; $i++) {
        $e = $seq.Item($i)
        if ($e.Shape.Name -eq $sh.Name -and $e.EffectType -eq 83) { $has = $true }
      }
      if (-not $has) {
        # msoAnimEffectMediaPlay = 83, level none = 0, msoAnimTriggerOnPageClick = 1, index 1 = first
        $null = $seq.AddEffect($sh, 83, 0, 1, 1)
      }
      "slide {0}: {1} {2:N1}s, embedded={3}, effects={4}" -f $s.SlideIndex, $sh.Name, ($sh.MediaFormat.Length / 1000.0), $sh.MediaFormat.IsEmbedded, $seq.Count
    }
  }
  $pres.SaveAs($Out)
  "saved $Out"
}
finally {
  $pres.Close()
  if ($started -and $app.Presentations.Count -eq 0) { $app.Quit() }
  "presentations open before/after: $before/$($app.Presentations.Count)"
}
