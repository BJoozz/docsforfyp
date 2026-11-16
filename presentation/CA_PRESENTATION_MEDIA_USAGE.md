# Media in the CA deck (16 November 2026)

This file maps every image and clip in [`VisuAlgo_CA_Presentation.pptx`](VisuAlgo_CA_Presentation.pptx) and in the backup file [`VisuAlgo_CA_QA_Backup.pptx`](VisuAlgo_CA_QA_Backup.pptx) (pages B1–B4) to its source. On the slides a capture is labelled only "Real app capture"; the dates and commits are here and in the speaker notes. [`CA_DECK_CHANGELOG.md`](CA_DECK_CHANGELOG.md) says what changed from the draft.

All app images and clips are real captures; none is generated or composited. The only additions are coloured outlines drawn on the slide over an image: around V2 and V7 in the wireframe grid on slide 7, and around the regions of the app on slide 8. The sources are:

- the [Codex pack](ca-2026-11-16/README.md): app `346e84b`, captured 15–16 November;
- the [deck media](ca-2026-11-16-deck-media/README.md): app `346e84b`, recorded 16 November. It holds the clips with their posters, the [standalone prototype stills](ca-2026-11-16-deck-media/early-prototypes/README.md) and five stills in `stills/` (the home page, the Trie page and three of the LCA run);
- the [design-history stills](ca-2026-11-16-deck-media/design-history/README.md): Kerk's UI kit (`634b5be`, 3 September) and wireframes (`69aa8e4`, 4 September), and Bao's working V2 and V7 builds (`ae63a62`), each rendered from its own commit on 16 November;
- the [historical figures](../figures/README.md): app `662e7b3`, 1 November.

| Slide | Asset | What it shows | If a clip will not play, the poster shows |
|---|---|---|---|
| 1 | [`stills/home_page.png`](ca-2026-11-16-deck-media/stills/home_page.png) | The home page of the current app at 1440 × 900, uncropped: the logo, the sponsors, the credit line, the Editors row and the top of the catalogue | — |
| 2 | Crops of Codex `06`, `02`, `05`, and of [`stills/trie_insert_care_frame5.png`](ca-2026-11-16-deck-media/stills/trie_insert_care_frame5.png) | A graph, a step note, two sorting panes, and the current Trie page (Insert "care" on car, cart, cat, dog, dot; frame 5/7, "Create edge e and prefix care") | — |
| 5 | `early-prototypes/02_graph_v1_run_crop.png`, `03_graph_v2_workspace.png`, `04_tree_binary_lifting_table_crop.png`, `05_sorting_two_panes_crop.png` | The standalone builds at 5fc06a0, c8b14e6, 46ce0a7 and 9236a65, rebuilt and captured on 16 November; not the current app | — |
| 6 | `early-prototypes/03_graph_v2_workspace.png`; `design-history/C1_ui_kit_home.png`, `C2_ui_kit_visualisation.png` | Left: Bao's standalone Graph rewrite. Right: the home and visualisation screens of Kerk's design-system UI kit, which recreate visualgo.net's pages (commit 634b5be, 3 September) | — |
| 7 | `design-history/A1_wireframes_at_a_glance_v1-v9_crop.png`, `A2_wireframe_v2_split_rails.png`, `A3_wireframe_v7_docks.png`, `B1_graph_v2_split_rails.png`, `B2_graph_v7_docks.png` | Kerk's nine wireframes V1–V9 (commit 69aa8e4, 4 September) with V2 and V7 outlined; the two chosen wireframes; Bao's working Graph builds in V2 and V7, made 20–27 September and shown as of 17 October (commit ae63a62) | — |
| 8 | `design-history/B3_tree_v2_split_rails.png`, `B4_tree_v7_docks.png`; Codex `04_tree_insert_preview.png`, with outlines | Bao's V2 and V7 Tree builds (as of 17 October) beside the current app's V10 regions: tab groups, the canvas, the playback bar | — |
| 13 | Crops of Codex `03`, `06`, `02`, and of the Trie still | Thumbnails | — |
| 14 | [`02b_v10_split_left_bottom.mp4`](ca-2026-11-16-deck-media/clips/02b_v10_split_left_bottom.mp4), 16.3 s | While the run stays at frame 12/21, the Status tab is dragged down its group to split the right column in two, then into the left group, then to the bottom row under the drawing. The drawing re-fits when the canvas gets shorter. Set-up before recording, also by a real drag: Status beside Pseudocode as a tab | Status under the drawing at 12/21 |
| 15 | [`03b_graph_drag_edit_parallel.mp4`](ca-2026-11-16-deck-media/clips/03b_graph_drag_edit_parallel.mp4), 16.2 s | Dragging B keeps frame 12/21. Changing B → A from 1 to 5 in the Edges text ends the run (NO RUN). A second B → A edge is then drawn on the canvas from B's handle to A's; it appears as a new `B A` line with no weight (the app counts it as 1 and says so) until ` 2` is typed. The two parallel edges end up curved apart and labelled 5 and 2 | the graph with both B → A edges, labelled 5 and 2 |
| 16 | Codex [`02_sorting_shared_clock.mp4`](ca-2026-11-16/02_short_clips/02_sorting_shared_clock.mp4), 10.4 s | Bubble and Selection on the same 12 values pause together at operation 48 and resume; Last seeks to the end | both panes at operation 48 |
| 17 | [`01d_lca_reroot_on_camera_8_20.mp4`](ca-2026-11-16-deck-media/clips/01d_lca_reroot_on_camera_8_20.mp4), 27.9 s; crops of `stills/lca_8_20_depth_lift.png`, `lca_8_20_keep.png`, `lca_8_20_lift_both.png` | The Balanced · 10 nodes preset loads with root 10; typing 16 in Structure → Root moves the root to 16 and the tree is laid out again. Then LCA(8, 20): u lifts from 8 to 4 ("gap 2 ≥ 2 · lift u"); at k = 3, 2 and 1 both ancestors are 16 ("same ancestor · keep u, v"); at k = 0 the ancestors 10 and 18 differ ("differ · lift both"); answer 16. Nine of the twelve frames carry a note and no node moves during the query | frame 9/12 with "differ · lift both" |
| 18 | [`04b_dijkstra_big_note_pause_hover.mp4`](ca-2026-11-16-deck-media/clips/04b_dijkstra_big_note_pause_hover.mp4), 14.0 s | Dijkstra from 0 on the nine-vertex Big preset (visualgo.net's TESSELLATION). Frame 17/53 stays fixed while edge 2 → 3 is emphasised; Next gives frame 18 with `12 + 14 < 33 · update` beside 3 (badge 33→26); Last, then hover 8 (0 → 2 → 3 → 8, distance 42) and 4 (0 → 2 → 3 → 4, distance 46) | frame 18/53 with the note |
| 19 | Codex `01_editor_entry_points.png` | The Editors section of the home page | — |
| B1 (backup file) | [`06_dfs_recursive_recap.mp4`](ca-2026-11-16-deck-media/clips/06_dfs_recursive_recap.mp4), 8.5 s | Recursive DFS on the S, A, B, T graph; the final frame replays the DFS tree (S → A → T, then S → B) | the final frame |
| B2 (backup file) | [`05_bst_preview_apply.mp4`](ca-2026-11-16-deck-media/clips/05_bst_preview_apply.mp4), 8.6 s | BST Insert(5) preview, two steps back and forward, then Apply; the tree text gains `6 5` | the preview with Apply insertion |
| B3 (backup file) | `figures/F8-cut-vertex-bridge-cp4-4-7-last.png` | Historical, 1 November (app `662e7b3`) | — |

Kept outside the deck for Q&A or rehearsal:
- [`01c_lca_reroot_8_20.mp4`](ca-2026-11-16-deck-media/clips/01c_lca_reroot_8_20.mp4): the same LCA(8, 20) query, starting after the re-root.
- [`01b_lca_keep_then_jump.mp4`](ca-2026-11-16-deck-media/clips/01b_lca_keep_then_jump.mp4): the earlier LCA clip, LCA(6, 10) = 8 on the default tree.
- [`03_graph_drag_then_edit.mp4`](ca-2026-11-16-deck-media/clips/03_graph_drag_then_edit.mp4): the first take for slide 15; it stops after the weight edit.
- [`04_dijkstra_note_pause_hover.mp4`](ca-2026-11-16-deck-media/clips/04_dijkstra_note_pause_hover.mp4): the first take for slide 18, on the four-vertex S, A, B, T graph.
- [`02_v10_move_panel.mp4`](ca-2026-11-16-deck-media/clips/02_v10_move_panel.mp4): the first take for slide 14. Status moves to the left group, then Settings → Reset panel layout.
- [`01_lca_equal_ancestors.mp4`](ca-2026-11-16-deck-media/clips/01_lca_equal_ancestors.mp4): LCA(6, 2); every step keeps u and v, then a hover on 6 shows its 2^k ancestors.
- Codex's [`01_graph_paused_step.mp4`](ca-2026-11-16/02_short_clips/01_graph_paused_step.mp4).
- Codex's final-path and BST stills.

## Playing the clips

- **Start:** once the slide is up, press → or click the video. Pressing → again moves to the next slide. Each clip plays once and stops on its last frame.
- **If a clip does not play:** its poster is already on the slide. Narrate from the CLIP section of the speaker notes, which lists the frame numbers.
- **Zoom:** share the whole screen, not one PowerPoint window, with "Optimize for video clip" ticked. The backup slides are in a second file, and a shared window would not show it. The paused motion on slide 18 is subtle, so point at the 2 → 3 edge while the counter shows 17.
- **Before the talk:** open both files, and click through slides 14–18 and backup B1–B2 once in slideshow mode on the presenting computer.

## Presentation decisions

- Clips replace the live actions on slides 14–18, so there is no window switching; the live demo stays on slide 20. Each clip is used once, and the clips stay within the existing slide times.
- Slide 17 uses LCA(8, 20) on the Balanced · 10 nodes preset re-rooted at 16, Bao's choice of 16 November. At his request the clip starts with the root at 10 and shows the re-root, so one more operation is on screen. One query shows a depth lift, three keeps and a lift, and nine of its twelve frames carry a note while no node moves. The earlier clips, LCA(6, 10) and LCA(6, 2) on the default tree, are kept. Sorting (slide 16) now comes before LCA, also Bao's choice.
- Keep the claims accurate:
  - The visualizers run TypeScript today; the engine is a separate foundation.
  - Operation counts are not CPU time, and the clip lengths are not timings.
  - Paused motion does not advance the algorithm.
  - The final hover reads the stored result; it does not rerun Dijkstra.
  - The Week 10 findings are formative.
- Finalised on 16 November, at Bao's request: short captions on the slides, slide 20 reduced to "Live demo", and the backup slides in their own file with the recursive DFS recap first.
- Slides 7–12 are Kerk's to confirm.
- This index is not proof of a new test-suite run, an A/B study, measured learning impact or a Zoom rehearsal.
