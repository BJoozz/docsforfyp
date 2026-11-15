# How the CA deck was built

`presentation/VisuAlgo_CA_Presentation.pptx` was built on 16 November 2026 from the GPT draft, which is kept unchanged as `presentation/drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx`. The build keeps the draft's slide order, titles, timing, speakers and claims. It restyles the slide bodies, embeds the real-app media, and rewrites the speaker notes only where the visuals changed. [`../../CA_DECK_CHANGELOG.md`](../../CA_DECK_CHANGELOG.md) lists every slide's change.

## Steps

Run from the repository root on Windows with Python 3.12 (`python-pptx`, `lxml`, `Pillow`) and PowerPoint installed.

```powershell
py -3.12 presentation/ca-2026-11-16-deck-media/deck-build/build_deck.py presentation/drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx $env:TEMP\deck-built.pptx
powershell -File presentation/ca-2026-11-16-deck-media/deck-build/finalize.ps1 -In $env:TEMP\deck-built.pptx -Out $env:TEMP\deck-final.pptx
powershell -File presentation/ca-2026-11-16-deck-media/deck-build/render.ps1 -Deck $env:TEMP\deck-final.pptx -OutDir $env:TEMP\deck-png -Pdf $env:TEMP\deck.pdf
```

1. `build_deck.py` uses `pptlib.py`. It edits the draft with python-pptx, writes the crops it uses to `../deck-crops/`, and embeds each MP4 with its poster PNG as the static fallback.
2. `finalize.ps1` opens the result in PowerPoint with the window hidden. It adds a Play effect to each video as the first click on its slide, so → or a click starts the clip, and saves a PowerPoint-written copy.
3. `render.ps1` exports slide PNGs, and a PDF when `-Pdf` is given. `sheet.py` turns the PNGs into contact sheets.
4. `decode_test.ps1` runs on a throwaway copy. It asks PowerPoint to take a poster frame from inside every embedded video, then exports those slides. On 16 November it decoded a frame at 3 s from all seven clips.

The PowerPoint scripts attach to a running PowerPoint if there is one. They close only the presentation they opened, and quit PowerPoint only if they started it.

## Inputs

- Codex's verified pack: `../../ca-2026-11-16/`, app `346e84b`.
- New clips, posters and early-prototype stills in this folder (see `../README.md` and `../early-prototypes/README.md`).
- Historical stills in `../../../figures/`, app `662e7b3`, 1 November 2026.
