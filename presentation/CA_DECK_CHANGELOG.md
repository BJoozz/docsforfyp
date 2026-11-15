# CA deck changelog, 16 November 2026

This file lists how the CA deck changed from the GPT draft, [`drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx`](drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx) (26 slides), to [`VisuAlgo_CA_Presentation.pptx`](VisuAlgo_CA_Presentation.pptx) (27 slides).

- Rebuild steps: [`ca-2026-11-16-deck-media/deck-build/`](ca-2026-11-16-deck-media/deck-build/README.md).
- Preview: a [PDF](ca-2026-11-16-deck-media/deck-preview/VisuAlgo_CA_Presentation_preview.pdf) and three contact sheets in [`deck-preview/`](ca-2026-11-16-deck-media/deck-preview/). The videos show as their posters.

The following are unchanged:
- slide order and titles;
- the 33-minute timing and the speaker for each section;
- every on-slide claim (the draft's lines are kept as headings);
- the speaker notes, except on the slides marked below.

Slides 9–12 were restyled only, and slides 7–8 were rewritten for the design history (see below). Kerk still has to confirm the content of slides 7–12.

## Embedded clips

There are seven embedded MP4s, all real recordings of app `346e84b`.
- Each clip has a poster frame as its static fallback.
- Press → (or click the video) to start a clip. It plays once and stops on its last frame.
- On 16 November, PowerPoint decoded a frame from inside each embedded clip.

| Slide | Clip | Length | Shows |
|---|---|---:|---|
| 14 | `02b_v10_split_left_bottom.mp4` | 16.3 s | The Status tab splits the right group in two, joins the left group, then docks under the drawing; frame 12/21 throughout |
| 15 | `03b_graph_drag_edit_parallel.mp4` | 16.2 s | B dragged at frame 12/21 (the run is kept); B → A changed from 1 to 5 (NO RUN); a second B → A edge drawn on the canvas, then given weight 2 in the Edges text, so the two parallel edges read 5 and 2 |
| 16 | `02_sorting_shared_clock.mp4` (Codex pack) | 10.4 s | Bubble and Selection on the same 12 values; both pause at operation 48; Last |
| 17 | `01c_lca_reroot_8_20.mp4` | 25.7 s | LCA(8, 20) on Balanced · 10 nodes re-rooted at 16: u lifts from 8 to 4, both cursors stay at k = 3, 2, 1 (ancestor 16), both lift at k = 0, answer 16 |
| 18 | `04b_dijkstra_big_note_pause_hover.mp4` | 14.0 s | Dijkstra on the nine-vertex Big preset (visualgo.net's TESSELLATION): paused motion at 17/53 on edge 2 → 3, the note `12 + 14 < 33 · update` at 18/53, then hover 8 (distance 42) and 4 (distance 46) at 53/53 |
| 24 (backup) | `05_bst_preview_apply.mp4` | 8.6 s | BST Insert(5): preview, step back, Apply; the tree text gains `6 5` |
| 27 (backup, new) | `06_dfs_recursive_recap.mp4` | 8.5 s | Recursive DFS on the same graph and its final recap |

The main talk uses five clips (slides 14–18), about 83 seconds in total. They replace the live actions the draft planned for those slides. The live demo stays on slide 20.

## Algorithm-coverage context (added 16 November)

Bao added one piece of context after the first build: in early discussions Prof. Halim also encouraged widening the range of algorithms VisuAlgo+ supports. This rests on Bao's account; the repository holds no written record of it, and no specific topic is attributed to Prof. Halim.

What was checked before the slides changed:
- **LCA with Binary Lifting and Trie in the standalone Tree prototype:** confirmed in `BJoozz/tree-visualizer`. LCA came with the first commit (`e687099`, 3 September 2026), Trie Insert and Search with `015469e` (8 September) and Binary Lifting with `f10d6d1` (10 September). All 50 commits are Bao's.
- **Both in the current app:** confirmed at `346e84b`. The catalogue has `/lca` and `/trie` cards, and Trie offers Insert and Search. The Trie still on slides 2 and 13 was captured from that build.
- **Heavy-Light Decomposition and Centroid Decomposition:** not in the app and not in any record. The deck names them only as possible later extensions.
- **The original VisuAlgo:** the deck makes no claim about whether it has Trie or LCA pages. A comment in the app's `modules.ts` says it has both, while Bao's copy of its source (`BJoozz/visualgo`) has no view named for either.

Slides changed for this: 2, 4, 5, 13, the LCA slide (notes only; slide 16 then, slide 17 now), 22 and 26 (notes only). No slide was added and the LCA clip was not changed by it.

## Design history on slides 6–8 (added 16 November)

Bao asked for slides 6–8 to tell the collaborative design process: two parallel foundations, nine wireframes to two working layouts, and V2 and V7 to V10. Slide 5 is unchanged.

What the records support, and how the slides word it:
- **Kerk's design system and UI kit:** committed on 3 September 2026 (`634b5be`). The UI kit describes itself as a recreation of visualgo.net's pages in the new style, so the slides say "restyled visualgo.net" and never "designed from scratch".
- **Nine wireframes:** Kerk's file of 4 September (`69aa8e4`) has nine frames, V1–V9. V8 and V9 are V7 mid-drag and after the drop, so the slides say "nine wireframes" with "seven panel layouts and two drag states", not "nine layouts". Only V2 and V7 were built.
- **Student feedback:** it rests on Bao's account that Kerk organised it. No date, size or result is on record, so the slides give no numbers and credit the choice of V2 and V7 to Kerk and Bao.
- **Working builds:** Bao built Graph, Tree and Sorting in both layouts in PRs #1–#3, 20–27 September: six apps, from his standalone prototypes, on Kerk's design tokens and themes.
- **V10:** it came out of joint discussion, and the slides say "Discussed together". The written proposal of 16 October is Bao's, but on 16 November he asked that the slides not single that out. Bao built the panel-group model and shell in PRs #15–#17 (16–18 October). Kerk implemented the later refinements agreed with Bao and merged everything into one application on 18 October (`0394b64`).
- **Prof. Halim:** his part in the discussion rests on Bao's account, so the slides say "with Prof. Halim's feedback" and nothing stronger.
- **Naming:** "standalone Graph rewrite" is Bao's own repository; "V2 (split rails)" is the team layout.

A review pass then changed the first version of these slides (three reviewers read the text against the records, for flow and timing, and as the evaluators would):
- **Slide 6:** "engines" for Bao's TypeScript code was replaced, because the deck uses "engine" only for Kerk's C++/WebAssembly work. A sentence that read the UI kit's visualisation page as Kerk's own design was removed; that page recreates visualgo.net's layout. The UI kit point now names visualgo.net, the left card shows one still instead of repeating slide 5's three, and the notes mention Kerk's engine foundation of the same days.
- **Slide 7:** the title says "two working layouts" (two layouts, six builds). The caption says the builds were made on 20–27 September and are shown as of 17 October. The notes use "layout survey", the term slide 21 uses, and no longer count apps by date.
- **Slide 8:** the V10 points now answer slide 6's three requirements (canvas, tab groups, one playback bar), the left thumbnails are the Tree builds, and Kerk's credit line names what he refined.
- **Slide 18 (notes):** one sentence credits Kerk for suggesting paused motion, as the CA report does.

The images are real artifacts rendered from their own commits; see [`design-history/`](ca-2026-11-16-deck-media/design-history/README.md). The text was checked against the records by a separate fact-checking pass before it went on the slides.

## Order and LCA test case (added 16 November)

Bao asked for two changes:
- **Order:** Sorting now comes before LCA, because it stands apart from the two explanation slides (LCA, then Dijkstra). Sorting is slide 16 and LCA is slide 17. Where an earlier section of this file says "slide 16" for LCA, it means today's slide 17.
- **LCA test case:** the preset Balanced · 10 nodes, re-rooted at 16, with the query LCA(8, 20), and more weight on what floating text is for.

What the new run shows, read from the page while recording:
- The run has 12 frames. The depths are 4 and 2, so u first lifts from 8 to 4 (the depth loop checks k = 3 and k = 2 before it lifts at k = 1).
- Both cursors then stay at k = 3, 2 and 1, where both ancestors are 16, and lift at k = 0, where the ancestors are 10 and 18. LCA(8, 20) = 16, as worked out by hand beforehand.
- Nine of the twelve frames carry a floating note and no node moves in any of them. The slide says so, and shows three of the notes as crops beside the clip.

The slide still says that the benefit of floating text is a design intention and has not been measured.

## Slide by slide

| Slide | Draft | Now | Notes |
|---|---|---|---|
| 1 | Title text | Course line and a current app screenshot (a Dijkstra step with its note) | unchanged |
| 2 | Three numbered lines | Four cards, each with a one-line detail and a crop of today's prototype; the fourth, "A wider range of algorithms", was added with the coverage context below | one sentence replaced (coverage) |
| 3 | Three lines | Simplified diagram of the original graph topics over one shared widget, and the three points with details | unchanged |
| 4 | Three lines | Objective cards with NOW and NEXT, and a band stating the TypeScript/engine boundary; objective 1 now says LCA and Trie already run on the shell and that topics are added on the same foundations | one phrase replaced (coverage) |
| 5 | Three lines | Stills of the standalone Graph (prototype 1 and rewrite), Tree and Sorting builds, and what each tested; the Tree card names LCA and Trie | VISUAL cue and media source added; the Tree sentences rewritten (coverage) |
| 6 | Three lines ("A common direction") | "Two parallel foundations": Bao's standalone visualizers (one still of the Graph rewrite) beside Kerk's design system and UI kit (real renders from commit 634b5be), and the three requirements carried forward | rewritten |
| 7 | Three lines ("Layout exploration") | "From nine wireframes to two working layouts": Kerk's real wireframe grid V1–V9 with V2 and V7 outlined, the two chosen wireframes, and Bao's working V2 and V7 builds; it replaces a schematic drawn for the first build | rewritten; Kerk to confirm |
| 8 | Small historical still (F3), "The V10 panel layout" | "From V2 and V7 to V10": what V10 keeps from V2 and from V7 (with Bao's Tree builds in each), the current app with outlined regions, and a credit band for the discussion, Bao's part and Kerk's part | rewritten; Kerk to confirm |
| 9 | Four lines | Layered diagram: site host, three visualizers, shared layer, separate engine | unchanged |
| 10 | Four lines | Flow diagram: page ⇄ protocol messages ⇄ worker (WebAssembly, Pyodide) | unchanged |
| 11 | Three lines | Two history models (≠) over the three things integration must preserve | unchanged |
| 12 | Three lines | Site frame with three visualizer slots, the infrastructure card, an attribution line | unchanged |
| 13 | Four lines | 2×2 cards with details and thumbnails; card 02 leads with LCA (Binary Lifting) and Trie and shows the current Trie page | first sentences rewritten (coverage) |
| 14 | Three lines | Points and the V10 clip (split, join, dock; it replaced a shorter first take, `02_v10_move_panel.mp4`, which is kept) | rewritten around the clip |
| 15 | Historical BFS still (F2) | State-ownership diagram, three outcome cards (the third: "Add a parallel edge: a separate edge") and the drag, re-weight and parallel-edge clip (it replaced a first take without the parallel edge, `03_graph_drag_then_edit.mp4`, which is kept) | rewritten around the clip |
| 16 | Historical four-pane still (F7); it was slide 17 in the draft | Points and the Codex sorting clip, moved before LCA | clip section added |
| 17 | Historical LCA(6, 2) still (F5); it was slide 16 in the draft | A card on what floating text is for, three notes cropped from the run, and the LCA(8, 20) clip on a tree re-rooted at 16; moved after Sorting | rewritten for the new query; LCA(6, 10) and LCA(6, 2) kept as alternatives |
| 18 | Historical Dijkstra still (F4) | Points (a note-on-arrival point added) and the Dijkstra clip on the nine-vertex Big preset (it replaced a first take on the four-vertex graph, `04_dijkstra_note_pause_hover.mp4`, which is kept) | rewritten around the clip; one sentence credits Kerk for suggesting paused motion |
| 19 | Historical home page (F1) | Current Editors section above a three-step flow and a limits line | screenshot source updated |
| 20 | Three lines | Demo timeline with time ranges and a fallback card | fallback sentence added |
| 21 | Four lines | Stat callouts (dated snapshot), Week 10 card, design-response and limits bands | unchanged |
| 22 | Four lines | Four-step roadmap with details; a second limits line names Heavy-Light Decomposition and Centroid Decomposition as possible later extensions, not commitments | one sentence expanded (coverage) |
| 23 | Questions | Evidence link added | unchanged |
| 24 | Historical heap still (F6) | BST preview/Apply clip | rewritten for BST; heap mentioned as the same contract |
| 25 | Small historical still (F8) | Larger still with details | unchanged |
| 26 | Four lines | Evidence cards | media provenance paragraph rewritten |
| 27 | — | New backup: recursive DFS recap clip, a fallback for slide 20 | new |
