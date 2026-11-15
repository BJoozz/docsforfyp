# Media in the CA deck (16 November 2026)

This file maps every image and clip in [`VisuAlgo_CA_Presentation.pptx`](VisuAlgo_CA_Presentation.pptx) to its source; [`CA_DECK_CHANGELOG.md`](CA_DECK_CHANGELOG.md) says what changed from the draft.

All app images and clips are real captures; none is generated or composited. The only additions are the coloured outlines on slide 8, drawn on the slide over the screenshot. The sources are:

- the [Codex pack](ca-2026-11-16/README.md): app `346e84b`, captured 15–16 November;
- the [deck media](ca-2026-11-16-deck-media/README.md): app `346e84b`, recorded 16 November. It holds seven clips with posters and the [standalone prototype stills](ca-2026-11-16-deck-media/early-prototypes/README.md);
- the [historical figures](../figures/README.md): app `662e7b3`, 1 November.

| Slide | Asset | What it shows | If a clip will not play, the poster shows |
|---|---|---|---|
| 1 | Codex `02_dijkstra_decision.png`, cropped | A Dijkstra step with its note | — |
| 2 | Crops of Codex `06`, `02`, `05` | A graph, a step note, two sorting panes | — |
| 5 | `early-prototypes/02_graph_v1_run_crop.png`, `03_graph_v2_workspace.png`, `04_tree_binary_lifting_table_crop.png`, `05_sorting_two_panes_crop.png` | The standalone builds at 5fc06a0, c8b14e6, 46ce0a7 and 9236a65, rebuilt and captured on 16 November; not the current app | — |
| 8 | Codex `04_tree_insert_preview.png`, with outlines | V10 regions: tab groups, the canvas, the playback bar | — |
| 13 | Crops of Codex `03`, `04`, `06`, `02` | Thumbnails | — |
| 14 | [`02b_v10_split_left_bottom.mp4`](ca-2026-11-16-deck-media/clips/02b_v10_split_left_bottom.mp4), 16.3 s | While the run stays at frame 12/21, the Status tab is dragged down its group to split the right column in two, then into the left group, then to the bottom row under the drawing. The drawing re-fits when the canvas gets shorter. Set-up before recording, also by a real drag: Status beside Pseudocode as a tab | Status under the drawing at 12/21 |
| 15 | [`03_graph_drag_then_edit.mp4`](ca-2026-11-16-deck-media/clips/03_graph_drag_then_edit.mp4), 8.0 s | Dragging B keeps frame 12/21; changing B → A from 1 to 5 in the Edges text ends the run (NO RUN) | the graph after the edit |
| 16 | [`01b_lca_keep_then_jump.mp4`](ca-2026-11-16-deck-media/clips/01b_lca_keep_then_jump.mp4), 10.3 s | LCA(6, 10): at k = 1 both ancestors are 8, so u and v are kept (note "same ancestor · keep u, v"); at k = 0, 4 and 12 differ, so both are lifted ("differ · lift both"); answer 8 | frame 4/7 with "differ · lift both" |
| 17 | Codex [`02_sorting_shared_clock.mp4`](ca-2026-11-16/02_short_clips/02_sorting_shared_clock.mp4), 10.4 s | Bubble and Selection on the same 12 values pause together at operation 48 and resume; Last seeks to the end | both panes at operation 48 |
| 18 | [`04b_dijkstra_big_note_pause_hover.mp4`](ca-2026-11-16-deck-media/clips/04b_dijkstra_big_note_pause_hover.mp4), 14.0 s | Dijkstra from 0 on the nine-vertex Big preset (visualgo.net's TESSELLATION). Frame 17/53 stays fixed while edge 2 → 3 is emphasised; Next gives frame 18 with `12 + 14 < 33 · update` beside 3 (badge 33→26); Last, then hover 8 (0 → 2 → 3 → 8, distance 42) and 4 (0 → 2 → 3 → 4, distance 46) | frame 18/53 with the note |
| 19 | Codex `01_editor_entry_points.png` | The Editors section of the home page | — |
| 24 (backup) | [`05_bst_preview_apply.mp4`](ca-2026-11-16-deck-media/clips/05_bst_preview_apply.mp4), 8.6 s | BST Insert(5) preview, two steps back and forward, then Apply; the tree text gains `6 5` | the preview with Apply insertion |
| 25 (backup) | `figures/F8-cut-vertex-bridge-cp4-4-7-last.png` | Historical, 1 November (app `662e7b3`) | — |
| 27 (backup) | [`06_dfs_recursive_recap.mp4`](ca-2026-11-16-deck-media/clips/06_dfs_recursive_recap.mp4), 8.5 s | Recursive DFS on the same graph; the final frame replays the DFS tree (S → A → T, then S → B) | the final frame |

Kept outside the deck for Q&A or rehearsal:
- [`04_dijkstra_note_pause_hover.mp4`](ca-2026-11-16-deck-media/clips/04_dijkstra_note_pause_hover.mp4): the first take for slide 18, on the four-vertex S, A, B, T graph.
- [`02_v10_move_panel.mp4`](ca-2026-11-16-deck-media/clips/02_v10_move_panel.mp4): the first take for slide 14. Status moves to the left group, then Settings → Reset panel layout.
- [`01_lca_equal_ancestors.mp4`](ca-2026-11-16-deck-media/clips/01_lca_equal_ancestors.mp4): LCA(6, 2); every step keeps u and v, then a hover on 6 shows its 2^k ancestors.
- Codex's [`01_graph_paused_step.mp4`](ca-2026-11-16/02_short_clips/01_graph_paused_step.mp4).
- Codex's final-path and BST stills.

## Playing the clips

- **Start:** once the slide is up, press → or click the video. Pressing → again moves to the next slide. Each clip plays once and stops on its last frame.
- **If a clip does not play:** its poster is already on the slide. Narrate from the CLIP section of the speaker notes, which lists the frame numbers.
- **Zoom:** share the screen or the PowerPoint window with "Optimize for video clip" ticked. The paused motion on slide 18 is subtle, so point at the 2 → 3 edge while the counter shows 17.
- **Before the talk:** click through slides 14–18, 24 and 27 once in slideshow mode on the presenting computer.

## Presentation decisions

- Clips replace the live actions on slides 14–18, so there is no window switching; the live demo stays on slide 20. Each clip is used once, and the clips stay within the existing slide times.
- Slide 16 uses LCA(6, 10) because it shows both a keep, where nothing moves and the note explains why, and a lift. Its alternative is LCA(6, 2), the report's F5 example; swap it in by setting `LCA_VARIANT` in `deck-build/build_deck.py`.
- Keep the claims accurate:
  - The visualizers run TypeScript today; the engine is a separate foundation.
  - Operation counts are not CPU time, and the clip lengths are not timings.
  - Paused motion does not advance the algorithm.
  - The final hover reads the stored result; it does not rerun Dijkstra.
  - The Week 10 findings are formative.
- Slides 7–12 are Kerk's to confirm.
- This index is not proof of a new test-suite run, an A/B study, measured learning impact or a Zoom rehearsal.
