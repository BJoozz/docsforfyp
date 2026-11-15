param(
  [Parameter(Mandatory = $true)][string]$Deck,
  [Parameter(Mandatory = $true)][string]$OutDir,
  [int]$AtMs = 3000
)
# Decode test on a COPY: ask PowerPoint to take a poster frame from inside each
# embedded video (needs a real H.264 decode), then export those slides.
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force $OutDir | Out-Null
$started = $false
try { $app = [Runtime.InteropServices.Marshal]::GetActiveObject('PowerPoint.Application') }
catch { $app = New-Object -ComObject PowerPoint.Application; $started = $true }
$before = $app.Presentations.Count
$pres = $app.Presentations.Open($Deck, 0, 0, 0)
try {
  foreach ($s in $pres.Slides) {
    foreach ($sh in $s.Shapes) {
      if ($sh.Type -ne 16) { continue }
      $sh.MediaFormat.SetDisplayPicture($AtMs)
      $name = Join-Path $OutDir ("decoded-{0:D2}.png" -f $s.SlideIndex)
      $s.Export($name, 'PNG', 1600, 900)
      "slide {0}: frame at {1} ms decoded -> {2}" -f $s.SlideIndex, $AtMs, (Split-Path $name -Leaf)
    }
  }
}
finally {
  $pres.Close()
  if ($started -and $app.Presentations.Count -eq 0) { $app.Quit() }
  "presentations open before/after: $before/$($app.Presentations.Count)"
}
