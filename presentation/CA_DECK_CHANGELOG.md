# CA deck changelog, 16 November 2026

This file lists how the CA deck changed from the GPT draft, [`drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx`](drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx) (26 slides), to [`VisuAlgo_CA_Presentation.pptx`](VisuAlgo_CA_Presentation.pptx) (23 slides) and [`VisuAlgo_CA_QA_Backup.pptx`](VisuAlgo_CA_QA_Backup.pptx) (4 backup slides, B1–B4).

- Rebuild steps: [`ca-2026-11-16-deck-media/deck-build/`](ca-2026-11-16-deck-media/deck-build/README.md).
- Preview: a [PDF](ca-2026-11-16-deck-media/deck-preview/VisuAlgo_CA_Presentation_preview.pdf) and three contact sheets of the main deck, and a [PDF](ca-2026-11-16-deck-media/deck-preview/VisuAlgo_CA_QA_Backup_preview.pdf) and one contact sheet of the backup file, in [`deck-preview/`](ca-2026-11-16-deck-media/deck-preview/). The videos show as their posters.

The following are unchanged, except where a later section of this file says otherwise:
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
| 17 | `01d_lca_reroot_on_camera_8_20.mp4` | 27.9 s | On Balanced · 10 nodes the root is moved from 10 to 16 on camera, then LCA(8, 20) runs: u lifts from 8 to 4, both cursors stay at k = 3, 2, 1 (ancestor 16), both lift at k = 0, answer 16 |
| 18 | `04b_dijkstra_big_note_pause_hover.mp4` | 14.0 s | Dijkstra on the nine-vertex Big preset (visualgo.net's TESSELLATION): paused motion at 17/53 on edge 2 → 3, the note `12 + 14 < 33 · update` at 18/53, then hover 8 (distance 42) and 4 (distance 46) at 53/53 |
| B1 (backup file, new) | `06_dfs_recursive_recap.mp4` | 8.5 s | Recursive DFS on the S, A, B, T graph and its final recap |
| B2 (backup file) | `05_bst_preview_apply.mp4` | 8.6 s | BST Insert(5): preview, step back, Apply; the tree text gains `6 5` |

The main talk uses five clips (slides 14–18), about 85 seconds in total. They replace the live actions the draft planned for those slides. The live demo stays on slide 20.

## Algorithm-coverage context (added 16 November)

Bao added one piece of context after the first build: in early discussions Prof. Halim also encouraged widening the range of algorithms VisuAlgo+ supports. This rests on Bao's account; the repository holds no written record of it, and no specific topic is attributed to Prof. Halim.

What was checked before the slides changed:
- **LCA with Binary Lifting and Trie in the standalone Tree prototype:** confirmed in `BJoozz/tree-visualizer`. LCA came with the first commit (`e687099`, 3 September 2026), Trie Insert and Search with `015469e` (8 September) and Binary Lifting with `f10d6d1` (10 September). All 50 commits are Bao's.
- **Both in the current app:** confirmed at `346e84b`. The catalogue has `/lca` and `/trie` cards, and Trie offers Insert and Search. The Trie still on slides 2 and 13 was captured from that build.
- **Heavy-Light Decomposition and Centroid Decomposition:** not in the app and not in any record. The deck names them only as possible later extensions.
- **The original VisuAlgo:** the deck makes no claim about whether it has Trie or LCA pages. A comment in the app's `modules.ts` says it has both, while Bao's copy of its source (`BJoozz/visualgo`) has no view named for either.

Slides changed for this: 2, 4, 5, 13, the LCA slide (notes only; slide 16 then, slide 17 now), 22 and the evidence backup (notes only; slide 26 then, B4 now). No slide was added and the LCA clip was not changed by it.

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

The slide still says that the benefit of floating text is a design intention and has not been measured. Its script is about 215 words, so 15 seconds moved from the Sorting slide to it: Sorting has 60 seconds and LCA 115, and the section still ends at 25:10.

Bao then asked for the clip to start one step earlier: the preset as it loads, with root 10, and the root moved to 16 by hand under Structure, so the talk also shows the re-root operation. The clip is now `01d_lca_reroot_on_camera_8_20.mp4` (27.9 s). The query, its 12 frames and its notes are the same as in `01c`, which is kept as an alternative. The script gained one sentence for the re-root and is about 235 words.

## Finalising the deck (added 16 November)

Bao asked for a final pass with three changes, and later for the home page on slide 1. A draft from GPT proposed the first three; each was checked against the deck before it was applied.
- **Short captions.** The line under a capture now says only "Real app capture". Dates, commits and "press → or click to play" are in the speaker notes and the [media map](CA_PRESENTATION_MEDIA_USAGE.md). Two captions keep a date, on slide 21 and backup B3, because their numbers and image are a snapshot of 1 November. The labels that say whose work a picture shows (slides 5–8) are kept, without commits.
- **Slide 20 is "Live demo".** It says only "A short demo of VisuAlgo+". The timeline, the second marks and the fallback card moved to the notes; the plan is settled in the script and in rehearsal.
- **Slide 1 shows the home page.** The title slide is shared, and the home page is the product both presenters built; the Dijkstra step it showed before is also on slide 2. The image is a new capture of the current app (`346e84b`), uncropped.
- **Backups in their own file.** The main deck ends on slide 23, Questions. The four backup slides are in [`VisuAlgo_CA_QA_Backup.pptx`](VisuAlgo_CA_QA_Backup.pptx) as B1 recursive DFS recap (first, because it is the fallback for the live demo), B2 preview before Apply, B3 correctness and limitations, and B4 evidence and ownership. Slide 23's notes name the file.

Where an earlier section of this file says slide 24, 25, 26 or 27, it means B2, B3, B4 and B1. Both files were validated, rendered and decode-tested again after the split.

## Final QA pass (added 16 November)

An independent review read the finished deck four ways: every slide as rendered, the notes against the slides and clips, every claim against the records, and the whole talk as the evaluator would. A second reviewer re-checked each finding at its source before anything changed. What changed:
- **Slide 2 (notes):** the spoken list of Prof. Halim's directions now includes interaction with the canvas, as the slide and the record do, and one sentence says that LCA and Trie are topics Bao added.
- **Slide 3:** "across every topic" became "across several topics"; the check covered three graph modules.
- **Slide 4:** "V10" is no longer used before slide 8 introduces it.
- **Slide 5:** the Tree card says the ancestor table is under the tree, as the still shows, on three lines; "transport" became "playback bar"; the rewrite is dated Aug–Sep.
- **Slide 8:** the bullets have a hanging indent.
- **Slide 13:** "more topics:" became "implemented:", because visualgo.net already has several of the listed topics; "paused focus" became "paused motion".
- **Slides 15, 17 and 18 (notes):** the narration was shortened so each sentence is said while the clip shows it. Slide 18 now gives short cues during its 14-second clip and the explanation after it, and fits its 80 seconds.
- **Slide 16 (notes):** "Generators produce operations as needed" became "Generators produce the operations"; this run is generated up front.
- **Slide 17:** the card says "no node moves during the query", since the clip opens with a re-root that does move the nodes; the third crop now shows both 10 and 18; the Week 10 remark is worded as Bao's recollection, as on slide 21.
- **Slide 19:** the middle heading fits two lines; "clearer" became "more explicit".
- **Slide 21:** the second tile says "cases passing"; "a formative observation" now sits with the observation.
- **Backup file:** B1 names the S, A, B, T graph of slides 14–15; B3 says "keeps the connection"; B4 marks the application repository as private and its notes credit slide 6's prototype still.

Left as they are, for the presenters to decide: slide 12's "supplies operation and query" for Tree (Kerk's slide), the shared "Both:" paragraph on slide 22, mixed -ise/-ize spellings, and the small footer counters in the clips, which the speaker should read out.

## Speaking script (added 16 November)

Bao asked for a script that is easy to say and easy to follow: plain spoken English, short and complete, with talking points so that the speaker can adjust while speaking. The format follows a suggestion from GPT that he passed on.
- **Five parts per slide:** a main message, three to five talking points, the script, cues and a transition to the next slide.
- **One source:** [`speaking_script.json`](ca-2026-11-16-deck-media/deck-build/speaking_script.json). `build_deck.py` writes it into the speaker notes of both files, above the CLIP, VISUAL and SOURCE blocks that were already there. `make_script_docs.py` writes it into the [master script](VisuAlgo_CA_Master_Script.md) and the new [cheat sheet](VisuAlgo_CA_Cheat_Sheet.md).
- **Same claims, simpler words.** No fact, number or attribution changed. Sentences were shortened and the order follows what is on screen. On the clip slides (14–18) the sentence said during the clip is short enough to keep pace with it.
- **Length.** Every script fits its slot at about 130 words per minute; the master script shows the count for each slide. The talk is still 33 minutes.
- **Kerk's slides (7–12)** were reworded in the same style with their technical content kept. They are his to confirm.
- **Slide 22:** the closing paragraph was marked "Both". It is now split: Kerk takes the release target and the transition plan, Bao the wider ambition and the last sentence. This is a proposal for Kerk to confirm.
- **Slide 20, the live demo:** the notes hold a proposed three-minute plan with no typing: the Graph Editor's default graph, Dijkstra, then recursive DFS on the same graph, then the Tree Editor with the Ancestor table and a hover. Every step and value was run on app `346e84b` on 16 November. It replaces the earlier cue line and is still to be settled in rehearsal.

A second reviewer then read the rewrite against the earlier script, the clips and the records. It found the meaning and every accuracy rule kept, and these points, which were fixed:
- **Clip narration (slides 14, 15, 17, 18 and B2):** some sentences were still said a few seconds after the clip had moved on. They are now short lines named as each action lands, with the reasons given after the clip.
- **Hedges restored:** slide 10 says what the engine *should* describe (it is a plan); slides 17 and 21 say "often", not "very often", for the Status recollection; slide 19 says a user "may" have a graph in mind; slide 21 says "checked", not "confirmed"; B4 says "main evidence".
- **Attribution and scope:** slide 8's talking point says Kerk merged the site and the visualizers, not "everything"; slide 7's message says Bao built both layouts; slide 5's transition names only the prototypes that overlapped with Kerk's design work.
- **Fit with the slides:** on slides 2 and 4 the spoken list now follows the numbered cards.

Only the notes changed in the two PowerPoint files; the slides are as they were after the QA pass.

## New order from Kerk's file (added 16 November, about 12:30)

Kerk rearranged the deck by hand in PowerPoint, and Bao adopted his file. The deck now has 24 slides.
- **Order:** the title, then the live demo, then Bao's slides (to 14), then Kerk's (15–23), then Questions.
- **Kerk's new slides (15–20):** Wireframing, three Prototyping slides and two Architecture slides replace the earlier slides 7, 8 and 9. They carry his own pictures and figures: 61 survey respondents, 8 prototype testers, a table of feedback and an architecture diagram.
- **Gone from the deck:** the earlier slides 21 (Evaluation and design response) and 22 (Semester 2 priorities). The test snapshot is now said on slide 8, the Week 10 trial on slides 17 and 18, and the Semester 2 plan over slide 23.
- **Two titles changed:** "Visualization contributions" (slide 8) and "Graph/Tree Editors" (slide 14).

| Earlier slide | Now |
|---|---|
| 1 Title | 1 |
| 20 Live demo | 2 |
| 2–6 Motivation to Two parallel foundations | 3–7 |
| 13–19 Visualization contributions to Editors | 8–14 |
| 7, 8, 9 (wireframes, V2/V7 to V10, application boundaries) | replaced by Kerk's 15–20 |
| 10–12 Engine foundation to Website integration | 21–23 |
| 21 Evaluation, 22 Semester 2 priorities | not in the deck |
| 23 Questions | 24 |

Three things were fixed in a copy of his file, with `adopt_rearranged_deck.py` and `write_notes.py`; no slide design was touched:
- **Motivation slide:** five shapes left over from an older version sat on top of the current ones, so the caption read as two overlapping lines. They were removed.
- **Page numbers:** they still showed the earlier order (for example 20 on the second slide, and 08 three times). They now run 01 to 24.
- **Speaker notes:** his file had the notes from before the script was rewritten. The notes now hold the speaking script in the new order, with new transitions where the order changed (after slides 1, 2, 7, 14 and 23). For his remade slides the script is a draft from the slide text and his earlier script.

Backup B1 names the S, A, B, T graph of slides 9–10, and the notes of B1 and B4 use the new numbers.

Left for Kerk to decide:
- Slides 19 and 20 are identical in his file.
- The deck has no Future Work slide, although he plans to speak about it.
- "Layout is validated" on slide 18 rests on eight testers.
- The Architecture diagram does not say which parts run today; the script keeps the sentence that the demo runs TypeScript in the browser.
- On slide 15 the large picture reaches the top and bottom edges and covers the page number.

The sections above and the table below use the earlier slide numbers. `build_deck.py` still rebuilds the deck as it was before this rearrangement.

## The opening demo as a tour (added 16 November, about 13:15)

Because the demo now opens the talk, Bao asked for it to give the whole picture with a few typical examples, and gave an outline. The script for slide 2 follows it:
- the home page, built like the original VisuAlgo with one card per topic;
- the two editors, then the Graph Editor: many algorithms on one input, the Algorithms menu and its search;
- the four panels (Action, e-Lecture, Pseudocode, Status) and the canvas;
- drawing a graph: drag a vertex, add a node, draw an edge, type its weight;
- a Dijkstra run, read in three places: the pseudocode line, the Status sentence and the note on the canvas;
- the Tree Editor, briefly: LCA with Binary Lifting, and moving the root.

Every step and value was run on app `346e84b` before it was written into the notes; the master script lists them under "Demo input: the opening tour". The earlier plan (Dijkstra, then recursive DFS, then a hover in the Tree Editor) is kept there as an alternative. The demo has 4:30. The title slide gave it 10 seconds and the Graph/Tree Editors slide 20, since the demo now introduces the editors; the talk is still 33 minutes. Backup B1 is no longer the fallback for the demo: slides 9 to 13 show the same features as clips.

## Slide by slide

| Slide | Draft | Now | Notes |
|---|---|---|---|
| 1 | Title text | Course line and the current app's home page (the first build showed a Dijkstra step with its note) | unchanged |
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
| 17 | Historical LCA(6, 2) still (F5); it was slide 16 in the draft | A card on what floating text is for, three notes cropped from the run, and the clip that moves the root from 10 to 16 and then runs LCA(8, 20); moved after Sorting | rewritten for the new query; LCA(6, 10) and LCA(6, 2) kept as alternatives |
| 18 | Historical Dijkstra still (F4) | Points (a note-on-arrival point added) and the Dijkstra clip on the nine-vertex Big preset (it replaced a first take on the four-vertex graph, `04_dijkstra_note_pause_hover.mp4`, which is kept) | rewritten around the clip; one sentence credits Kerk for suggesting paused motion |
| 19 | Historical home page (F1) | Current Editors section above a three-step flow and a limits line | screenshot source updated |
| 20 | Three lines ("Demo: one example, several questions") | A divider slide: "Live demo", "A short demo of VisuAlgo+" | fallback sentence added; the cue is marked as a working plan |
| 21 | Four lines | Stat callouts (dated snapshot), Week 10 card, design-response and limits bands | unchanged |
| 22 | Four lines | Four-step roadmap with details; a second limits line names Heavy-Light Decomposition and Centroid Decomposition as possible later extensions, not commitments | one sentence expanded (coverage) |
| 23 | Questions | Evidence link added | a paragraph names the backup file |
| B1 (backup file) | — | New backup: recursive DFS recap clip, a fallback for slide 20 | new |
| B2 (backup file; slide 24 in the draft) | Historical heap still (F6) | BST preview/Apply clip | rewritten for BST; heap mentioned as the same contract |
| B3 (backup file; slide 25 in the draft) | Small historical still (F8) | Larger still with details | unchanged |
| B4 (backup file; slide 26 in the draft) | Four lines | Evidence cards | media provenance paragraph rewritten |
