# How the CA deck was built

`presentation/VisuAlgo_CA_Presentation.pptx` (23 slides) and `presentation/VisuAlgo_CA_QA_Backup.pptx` (the four backup slides, B1–B4) were built on 16 November 2026 from the GPT draft, which is kept unchanged as `presentation/drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx`. The build keeps the draft's timing, speakers and claims, and its slide order and titles except where the changelog says otherwise. It restyles the slide bodies, embeds the real-app media, and rewrites the speaker notes only where the visuals changed. [`../../CA_DECK_CHANGELOG.md`](../../CA_DECK_CHANGELOG.md) lists every slide's change.

## Steps

Run from the repository root on Windows with Python 3.12 (`python-pptx`, `lxml`, `Pillow`) and PowerPoint installed.

```powershell
py -3.12 presentation/ca-2026-11-16-deck-media/deck-build/build_deck.py presentation/drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx $env:TEMP\deck-built.pptx $env:TEMP\backup-built.pptx
powershell -File presentation/ca-2026-11-16-deck-media/deck-build/finalize.ps1 -In $env:TEMP\deck-built.pptx -Out $env:TEMP\deck-final.pptx
powershell -File presentation/ca-2026-11-16-deck-media/deck-build/finalize.ps1 -In $env:TEMP\backup-built.pptx -Out $env:TEMP\backup-final.pptx
powershell -File presentation/ca-2026-11-16-deck-media/deck-build/render.ps1 -Deck $env:TEMP\deck-final.pptx -OutDir $env:TEMP\deck-png -Pdf $env:TEMP\deck.pdf
```

1. `build_deck.py` uses `pptlib.py`. With two output paths it writes the 23-slide deck to the first and the four backup slides (recursive DFS recap first, pages B1–B4) to the second; with one it writes all 27 slides to a single file. It edits the draft with python-pptx, writes the crops it uses to `../deck-crops/`, and embeds each MP4 with its poster PNG as the static fallback.
2. `finalize.ps1` opens the result in PowerPoint with the window hidden. It adds a Play effect to each video as the first click on its slide, so → or a click starts the clip, and saves a PowerPoint-written copy.
3. `render.ps1` exports slide PNGs, and a PDF when `-Pdf` is given. `sheet.py` turns the PNGs into contact sheets.
4. `decode_test.ps1` runs on a throwaway copy. It asks PowerPoint to take a poster frame from inside every embedded video, then exports those slides. On 16 November it decoded a frame at 3 s from all seven clips: five in the deck and two in the backup file.

The PowerPoint scripts attach to a running PowerPoint if there is one. They close only the presentation they opened, and quit PowerPoint only if they started it.

## Other files

- `speaking_script.json` holds what the presenters say: for each slide a main message, talking points, a script, cues and a transition. `build_deck.py` writes it into the speaker notes. `make_script_docs.py`, run from the repository root, writes it into `presentation/VisuAlgo_CA_Master_Script.md` and `presentation/VisuAlgo_CA_Cheat_Sheet.md`. Change the wording there, then run both.
- `slides_6_8.py` lays out slides 6–8 (the design history) and `slides_6_8_copy.json` holds their text. `build_deck.py` calls it.
- `apply_slides_6_8.py` applies only those three slides to an already finalised deck, for when PowerPoint cannot be automated.
- `ppt_probe.ps1` says whether PowerPoint accepts automation right now. A PowerPoint that is showing a Protected View window rejects it; the three PowerPoint scripts then stop without changing anything.
- `approx_render.py` draws slides with Pillow for a rough layout check when PowerPoint is not available. It is not a substitute for `render.ps1`.
- Always give the PowerPoint scripts a scratch copy of the deck, never the file in the repository.

## Inputs

- Codex's verified pack: `../../ca-2026-11-16/`, app `346e84b`.
- New clips, posters and early-prototype stills in this folder (see `../README.md` and `../early-prototypes/README.md`).
- Historical stills in `../../../figures/`, app `662e7b3`, 1 November 2026.
