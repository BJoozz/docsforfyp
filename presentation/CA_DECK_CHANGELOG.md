# CA deck changelog, 16 November 2026

This file lists how the CA deck changed from the GPT draft, [`drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx`](drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx) (26 slides), to [`VisuAlgo_CA_Presentation.pptx`](VisuAlgo_CA_Presentation.pptx) (27 slides).

- Rebuild steps: [`ca-2026-11-16-deck-media/deck-build/`](ca-2026-11-16-deck-media/deck-build/README.md).
- Preview: a [PDF](ca-2026-11-16-deck-media/deck-preview/VisuAlgo_CA_Presentation_preview.pdf) and three contact sheets in [`deck-preview/`](ca-2026-11-16-deck-media/deck-preview/). The videos show as their posters.

The following are unchanged:
- slide order and titles;
- the 33-minute timing and the speaker for each section;
- every on-slide claim (the draft's lines are kept as headings);
- the speaker notes, except on the slides marked below.

Slides 7–12 were restyled only. Kerk still has to confirm their content.

## Embedded clips

There are seven embedded MP4s, all real recordings of app `346e84b`.
- Each clip has a poster frame as its static fallback.
- Press → (or click the video) to start a clip. It plays once and stops on its last frame.
- On 16 November, PowerPoint decoded a frame from inside each embedded clip.

| Slide | Clip | Length | Shows |
|---|---|---:|---|
| 14 | `02b_v10_split_left_bottom.mp4` | 16.3 s | The Status tab splits the right group in two, joins the left group, then docks under the drawing; frame 12/21 throughout |
| 15 | `03_graph_drag_then_edit.mp4` | 8.0 s | B dragged at frame 12/21 (the run is kept), then B → A changed from 1 to 5 (NO RUN) |
| 16 | `01b_lca_keep_then_jump.mp4` | 10.3 s | LCA(6, 10): keep at k = 1 with its note, lift at k = 0, answer 8 |
| 17 | `02_sorting_shared_clock.mp4` (Codex pack) | 10.4 s | Bubble and Selection on the same 12 values; both pause at operation 48; Last |
| 18 | `04b_dijkstra_big_note_pause_hover.mp4` | 14.0 s | Dijkstra on the nine-vertex Big preset (visualgo.net's TESSELLATION): paused motion at 17/53 on edge 2 → 3, the note `12 + 14 < 33 · update` at 18/53, then hover 8 (distance 42) and 4 (distance 46) at 53/53 |
| 24 (backup) | `05_bst_preview_apply.mp4` | 8.6 s | BST Insert(5): preview, step back, Apply; the tree text gains `6 5` |
| 27 (backup, new) | `06_dfs_recursive_recap.mp4` | 8.5 s | Recursive DFS on the same graph and its final recap |

The main talk uses five clips (slides 14–18), about 59 seconds in total. They replace the live actions the draft planned for those slides. The live demo stays on slide 20.

## Slide by slide

| Slide | Draft | Now | Notes |
|---|---|---|---|
| 1 | Title text | Course line and a current app screenshot (a Dijkstra step with its note) | unchanged |
| 2 | Three numbered lines | Three cards, each with a one-line detail and a crop of today's prototype | unchanged |
| 3 | Three lines | Simplified diagram of the original graph topics over one shared widget, and the three points with details | unchanged |
| 4 | Three lines | Objective cards with NOW and NEXT, and a band stating the TypeScript/engine boundary | unchanged |
| 5 | Three lines | Stills of the standalone Graph (prototype 1 and rewrite), Tree and Sorting builds, and what each tested | VISUAL cue and media source added |
| 6 | Three lines | Bao and Kerk cards, a joint-decisions band, three requirement chips | unchanged |
| 7 | Three lines | Schematic flow: nine wireframes → V2 rails and V7 docks → V10 | unchanged |
| 8 | Small historical still (F3) | Current Tree Editor screenshot with outlined tab groups, canvas and playback bar | screenshot source updated |
| 9 | Four lines | Layered diagram: site host, three visualizers, shared layer, separate engine | unchanged |
| 10 | Four lines | Flow diagram: page ⇄ protocol messages ⇄ worker (WebAssembly, Pyodide) | unchanged |
| 11 | Three lines | Two history models (≠) over the three things integration must preserve | unchanged |
| 12 | Three lines | Site frame with three visualizer slots, the infrastructure card, an attribution line | unchanged |
| 13 | Four lines | 2×2 cards with details and thumbnails | unchanged |
| 14 | Three lines | Points and the V10 clip (split, join, dock; it replaced a shorter first take, `02_v10_move_panel.mp4`, which is kept) | rewritten around the clip |
| 15 | Historical BFS still (F2) | State-ownership diagram and the drag/edit clip | rewritten around the clip |
| 16 | Historical LCA(6, 2) still (F5) | Points and the LCA(6, 10) clip | rewritten for the new query; LCA(6, 2) kept as an alternative |
| 17 | Historical four-pane still (F7) | Points and the Codex sorting clip | clip section added |
| 18 | Historical Dijkstra still (F4) | Points (a note-on-arrival point added) and the Dijkstra clip on the nine-vertex Big preset (it replaced a first take on the four-vertex graph, `04_dijkstra_note_pause_hover.mp4`, which is kept) | rewritten around the clip |
| 19 | Historical home page (F1) | Current Editors section above a three-step flow and a limits line | screenshot source updated |
| 20 | Three lines | Demo timeline with time ranges and a fallback card | fallback sentence added |
| 21 | Four lines | Stat callouts (dated snapshot), Week 10 card, design-response and limits bands | unchanged |
| 22 | Four lines | Four-step roadmap with details | unchanged |
| 23 | Questions | Evidence link added | unchanged |
| 24 | Historical heap still (F6) | BST preview/Apply clip | rewritten for BST; heap mentioned as the same contract |
| 25 | Small historical still (F8) | Larger still with details | unchanged |
| 26 | Four lines | Evidence cards | media provenance paragraph rewritten |
| 27 | — | New backup: recursive DFS recap clip, a fallback for slide 20 | new |
