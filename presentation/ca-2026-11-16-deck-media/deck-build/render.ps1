param(
  [Parameter(Mandatory = $true)][string]$Deck,
  [Parameter(Mandatory = $true)][string]$OutDir,
  [int]$Width = 1600,
  [int]$Height = 900,
  [string]$Slides = '',
  [string]$Pdf = ''
)
# Renders a COPY of a deck through PowerPoint. Never closes other presentations
# and only quits PowerPoint if this script started it.
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force $OutDir | Out-Null
$started = $false
try { $app = [Runtime.InteropServices.Marshal]::GetActiveObject('PowerPoint.Application') }
catch { $app = New-Object -ComObject PowerPoint.Application; $started = $true }
$before = $app.Presentations.Count
# Open(FileName, ReadOnly, Untitled, WithWindow)
$pres = $app.Presentations.Open($Deck, -1, 0, 0)
try {
  $count = $pres.Slides.Count
  $wanted = if ($Slides) { $Slides.Split(',') | ForEach-Object { [int]$_ } } else { 1..$count }
  foreach ($i in $wanted) {
    $name = Join-Path $OutDir ("slide-{0:D2}.png" -f $i)
    $pres.Slides.Item($i).Export($name, 'PNG', $Width, $Height)
  }
  if ($Pdf) { $pres.SaveAs($Pdf, 32) }
  "rendered $($wanted.Count) of $count slides"
  foreach ($i in 1..$count) {
    $s = $pres.Slides.Item($i)
    $media = @()
    foreach ($sh in $s.Shapes) { if ($sh.Type -eq 16) { $media += ("{0}:{1:N1}s" -f $sh.Name, ($sh.MediaFormat.Length / 1000.0)) } }
    if ($media.Count) { "slide {0} media: {1}" -f $i, ($media -join ', ') }
  }
}
finally {
  $pres.Close()
  if ($started -and $app.Presentations.Count -eq 0) { $app.Quit() }
  "presentations open before/after: $before/$($app.Presentations.Count)"
}
