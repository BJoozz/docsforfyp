# CA deck clips, 16 November 2026

Short screen recordings of the real VisuAlgo+ app for the CA deck, recorded on 16 November 2026 from `main` at `346e84b` with a clean working tree. Every clip has a poster PNG under `posters/` with the same name. The poster is the still to show if PowerPoint cannot play the video, taken at the clip's most informative moment.

All clips: H.264 High, 1440 × 900, constant 30 fps, no audio, real speed (no speed change, no freeze frames), each under 0.9 MB. Frame numbers below are the app's own footer counter, read from the DOM.

| Clip | Length | For | What it shows |
| --- | --- | --- | --- |
| `clips/01_lca_equal_ancestors.mp4` | 9.6 s | Alternative for slide 16 (not in the deck) | Binary Lifting Query, u = 6, v = 2, on the default tree (root 8). Starts paused at frame 1/6 ("depths 2 and 2"). Frame 2/6: k = 2, both ancestors are 8, and "same ancestor · keep u, v" appears above 8. Frame 3/6: k = 1, still 8. Frame 4/6: k = 0, both are 4. Frame 5/6: same parent, 4. Frame 6/6: LCA(6, 2) = 4. Ends with a hover on 6 that shows its path to the root and its 2^k ancestors. |
| `clips/01b_lca_keep_then_jump.mp4` | 10.3 s | Slide 16 (in the deck) | u = 6, v = 10. Starts paused at frame 2/7 (k = 2, both 8). Frame 3/7: k = 1, both 8, keep note. Frame 4/7: k = 0, ancestors 4 and 12 differ, "differ · lift both". Frame 5/7: u = 4 and v = 12, "↑ 1 level" over each. Frame 6/7: same parent, 8. Frame 7/7: LCA(6, 10) = 8. |
| `clips/02_v10_move_panel.mp4` | 7.3 s | Earlier slide-14 clip (replaced by 02b) | Dijkstra paused at frame 12/21. The Status tab is dragged onto the left group (drop preview shown) and released. The frame stays 12/21 and the drawing does not move. Settings → Reset panel layout puts Status back; still 12/21. |
| `clips/02b_v10_split_left_bottom.mp4` | 16.3 s | Slide 14 | Dijkstra paused at frame 12/21. The right column starts as one group with Pseudocode and Status as tabs (set up before recording). Three slow drags of the Status tab, each with a live drop preview:<br>1. Down into the lower half of its own group: the column splits into Pseudocode above and Status below, in equal halves.<br>2. Into the left group, beside Action and E-Lecture.<br>3. To the bottom row, under the drawing and as wide as it.<br>After every drop the frame is still 12/21 and the React Flow canvas is the same element (no remount). The drawing moves only after the bottom drop, when it re-fits the shorter canvas. Ends with Status under the drawing. |
| `clips/03_graph_drag_then_edit.mp4` | 8.0 s | Slide 15 | Paused at frame 12/21. Vertex B is dragged and the frame stays 12/21. In Draw graph → Edges, "B A 1" becomes "B A 5": the edge label reads 5, the footer says NO RUN and Status says NO ACTIVE RUN. |
| `clips/04_dijkstra_note_pause_hover.mp4` | 10.2 s | Earlier slide-18 clip (replaced by 04b) | Frame 11/21 (Inspect edge B → A) held 2.5 s while the edge streak and B's glow keep moving. Next → 12/21: "1 + 1 < 4 · update" above A. Last → 21/21. Hover T: "S → B → A → T · distance 4". Hover A: "S → B → A · distance 2". |
| `clips/04b_dijkstra_big_note_pause_hover.mp4` | 14.0 s | Slide 18 | Dijkstra on the preset Big (visualgo.net's TESSELLATION: vertices 0–8, 16 directed weighted arcs, preset positions). Start 0, End node left at All vertices.<br>Frame 17/53, "Inspect edge 2 → 3, weight 14.", is held 3 s while the paused streak and glow keep moving.<br>Next → 18/53: "12 + 14 < 33 · update" beside 3, badge 33→26, "Relax 2 → 3: 12 + 14 = 26 is shorter than 33, so update 3's distance to 26."<br>Last → 53/53, "Dijkstra complete. Settled 9 nodes."<br>Hover 8: "0 → 2 → 3 → 8 · distance 42". Hover 4: "0 → 2 → 3 → 4 · distance 46". |
| `clips/05_bst_preview_apply.mp4` | 8.6 s | Backup slide 24 | The Insert 5 preview at frame 8/8, with node 5 marked INSERTED and Apply insertion shown. Back to frames 7 and 6, then forward to 8. Apply insertion → NO RUN. Edit tree opens, and its text now ends with `6 5`. |
| `clips/06_dfs_recursive_recap.mp4` | 8.5 s | Backup slide 27 (live-demo fallback) | Recursive DFS on the same graph. Last → 21/21, visited S, A, T, B. The final frame replays the DFS tree (S → A → T, then S → B) with a glow and a streak about every 3 s. |

## Limits

- No mouse pointer is visible: headless Chromium does not draw one. The drags and hovers are real pointer events.
- The graph clips use the same graph and diamond as `../ca-2026-11-16/`, but the setup presses the canvas Fit view control before and after placing the nodes. Nodes therefore sit about 10 px from where they are in those stills.
- On this tree, two LCA steps have both ancestors equal to 8 (k = 2 and k = 1). Neither query needs a depth lift, because u and v are both at depth 2. 01b starts after k = 2, so its first keep note is the one for k = 1.
- The LCA clips keep the default layout. The Ancestor table tab is behind Status, and the strip under the drawing shows the two table reads instead (for example `k = 2: up[6][2] = 8, up[2][2] = 8, equal: keep`).
- 02 drops Status into the left group, not the bottom region, so the drawing keeps its size. The Settings menu stays open after Reset panel layout, so Escape closes it on camera.
- 02b, three app behaviours worth knowing before narrating it:
  - The bottom drop shortens the canvas from 798 to 521 px, so the drawing re-fits: it moves up 138 px at the same zoom.
  - When Status leaves the left group, that group shows E-Lecture, the tab next in line, not Action. The last frame therefore has the Dijkstra e-Lecture on the left.
  - Splitting a group with its own tab offers only two zones, the upper half and the lower half.
- 04b: the Fit view zoom is 0.78. Vertex numbers read well at 1440 × 900, but the edge weights and distance badges are about 10 px tall, so they get hard to read if the video is shown much smaller than full screen. The step note sits to the right of 3, not above it. Because End node is All vertices, the final frame's Path box asks for a hover until the pointer reaches 8.
- 05: stepping back to frame 6 removes node 5 and the drawing re-centres, then it moves back up at frame 8. This is the app's own behaviour.
- Playback inside PowerPoint: on 16 November, PowerPoint decoded a frame from inside each clip embedded in the deck (at 3 s; for 02b at 6 s; `deck-build/decode_test.ps1`). A full slideshow click-through on the presenting computer is still a preflight step.

`manifest.json` lists, for each clip, its bytes, sha256, inputs, settings, timed actions, DOM observations, captions and time-coded narration. It covers `clips/` and `posters/` only.

## Folders

| Folder | Contents |
| --- | --- |
| `clips/`, `posters/` | The nine clips above and their poster stills. |
| `reproduce/` | The capture script, its recipe and the raw DOM checks. |
| `early-prototypes/` | Stills of the standalone Graph, Tree and Sorting prototypes. The builds were rebuilt at their last documented commits and captured on 16 November 2026. That folder has its own README and manifest. |
| `deck-crops/` | Crops of Codex's stills (`../ca-2026-11-16/`), used on slides 1, 2 and 13. `deck-build/build_deck.py` generates them. |
| `deck-build/` | The scripts that built `../VisuAlgo_CA_Presentation.pptx` from the GPT draft, and how to rerun them. |
| `deck-preview/` | A PDF of the finished deck (videos show as their posters) and three contact sheets. |
