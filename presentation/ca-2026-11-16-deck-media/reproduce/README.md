# How to reproduce the deck clips

App: `kerktaiheng/visualgo-plus-design`, `main` at `346e84b838e87ae8affacdc54f0e0eb75eab1529`, working tree clean. Recorded on 16 November 2026 (Asia/Singapore).

## Setup

- Start a dev server of your own from `prototypes`: `npm run dev -- --host 127.0.0.1 --port 5205 --strictPort`. Any free port works.
- The script loads `@playwright/test` from the app checkout, so it needs no install of its own. Use the app's Node version (22.12 or later). The encode step needs a full ffmpeg build with libx264.
- Each clip gets a fresh, headless Chromium context: 1440 × 900, device scale 1, Light theme, `en-US`, reduced motion `no-preference`, and default app settings (Animate paused steps on, speed 0.50s). The Inter font loads from Google Fonts, so the run needs network access.

```powershell
$env:CA_APP_REPO = 'C:\path\to\visualgo-plus-design'
$env:CA_BASE_URL = 'http://127.0.0.1:5205'
$env:CA_DECK_OUTPUT = 'C:\path\outside\any\synced\folder\deck'
$env:CA_FFMPEG = 'C:\path\to\ffmpeg.exe'
node .\capture-deck.mjs 01_lca_equal_ancestors 01b_lca_keep_then_jump 02_v10_move_panel 02b_v10_split_left_bottom 03_graph_drag_then_edit 03b_graph_drag_edit_parallel 04_dijkstra_note_pause_hover 04b_dijkstra_big_note_pause_hover 05_bst_preview_apply 06_dfs_recursive_recap
```

The script writes `clips/`, `posters/`, `checks/` and `raw/<clip>/` under `CA_DECK_OUTPUT`. Each `raw/<clip>/` folder holds the screencast JPEGs and the `list.ffconcat` used for the encode. Clips run one after another. The script only drives the UI: it edits no source, injects no state, hides nothing with CSS and adds no overlay.

## Recording and clip boundaries

1. Everything that sets up a clip happens before recording starts. Recording then starts with `Page.startScreencast` (JPEG, quality 92, at most 1440 × 900, every frame acknowledged). The clip clock `t0` starts 0.15 s after the first frame arrives.
2. Every action is scheduled at a fixed offset from `t0`. Each one is logged with the time its input was sent and the time it finished. The largest delay against the schedule was 0.073 s, in 01. The clip ends at the fixed offset `end`.
3. Each screencast frame keeps Chrome's own swap timestamp. Output frame n, at 30 fps, shows the newest screencast frame swapped at or before `t0 + n/30`. As a result:
   - the first output frame is the paused start state, and the last one is the state at `end`;
   - a hold is real time;
   - nothing is sped up.
4. Repeated picks of the same frame are merged into one ffconcat entry whose duration is a multiple of 1/30 s. With N = round((end − t0) × 30), the script runs:

```text
ffmpeg -y -f concat -safe 0 -i list.ffconcat -vf "fps=30,scale=in_range=pc:out_range=tv:in_color_matrix=bt601:out_color_matrix=bt709:flags=accurate_rnd+full_chroma_int,format=yuv420p" -frames:v N -r 30 -c:v libx264 -profile:v high -preset slow -crf 18 -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -movflags +faststart -an clip.mp4
```

5. Posters come from `page.screenshot()` during the clip, at the time recorded in each check file.
6. QA:
   - every MP4 was decoded in full with ffmpeg, with no errors, and its frame count matches N;
   - the first, last and key frames were extracted and looked at (`framesInspected` in `../manifest.json`);
   - no page errors occurred in any clip.

## Common graph setup (02, 02b, 03, 03b, 04, 06)

1. Open `/graph-editor/dijkstra` (for 06, `/graph-editor/dfs-recursive`) and untick Live force layout.
2. Enter nodes `S A B T`, one per line, and these edges, then tick Directed graph:

   ```text
   S A 4
   S B 1
   B A 1
   A T 2
   B T 6
   ```

3. Set Dijkstra Start S and End T. For 06 the start stays at its default, S.
4. Click Draw graph to collapse it, then click the canvas Fit view control.
5. Drag S, A, B and T to the screen points (445, 440), (710, 275), (710, 595) and (980, 440). Click Fit view again.

These are Codex's steps plus the two Fit view presses, which make the framing the same on every run.

## Per clip (times are seconds inside the delivered clip)

### 01_lca_equal_ancestors (9.6 s)

**Setup:**
- Open `/tree-editor/lca-binary-lifting`.
- The default tree is checked to be `12 8 / 4 8 / 14 12 / 10 12 / 6 4 / 2 4` with root 8.
- Query is selected and u = 6, v = 2 (the defaults).
- Next starts the run at frame 1/6; then wait 2.3 s.

**Recorded:**
- 0.87 Next → 2/6, "k = 2: both ancestors are 8, so u and v stay." The note "same ancestor · keep u, v" is above 8.
- 2.81 Next → 3/6, "k = 1: both ancestors are 8, so u and v stay."
- 4.02 Next → 4/6, "k = 0: both ancestors are 4, so u and v stay." The note is above 4.
- 5.26 Next → 5/6, "Both cursors now have the same parent, 4."
- 6.32 Next → 6/6, "LCA(6, 2) = 4."
- 8.04 the pointer moves onto node 6.
- End at 9.6.

Poster at 1.30 s, frame 2/6, with the note showing.

### 01b_lca_keep_then_jump (10.3 s)

**Setup:** as in 01 with u = 6, v = 10. Next starts the run, then one more Next reaches 2/7 ("k = 2: both ancestors are 8, so u and v stay."). Wait 2.3 s so that note has faded.

**Recorded:**
- 0.85 Next → 3/7, "k = 1: both ancestors are 8, so u and v stay." The keep note is above 8.
- 2.83 Next → 4/7, "k = 0: ancestors 4 and 12 differ, so both lift 1 level." The note "differ · lift both" is above 4.
- 4.92 Next → 5/7, "Lift both by 2^0: u = 4, v = 12." "↑ 1 level" is above 4 and 12.
- 6.72 Next → 6/7, "Both cursors now have the same parent, 8."
- 8.02 Next → 7/7, "LCA(6, 10) = 8."
- End at 10.3.

Poster at 3.30 s, frame 4/7.

### 02_v10_move_panel (7.3 s)

**Setup:** the common graph setup, then Next until frame 12/21. The pointer is parked on empty canvas, and a 2.3 s wait lets the frame-12 note fade.

**Recorded:**
- 1.00 the pointer is pressed on the Status tab.
- 1.02–1.94 the tab is dragged in 12 steps to (150, 450), the left group's body (drop target `group:g1`, which is hot at 2.31).
- 2.60 release. Status is now in the left region, the frame is still 12/21 and the canvas viewport transform is unchanged.
- 4.52 Settings is opened.
- 5.21 Reset panel layout is pressed. Status is back in the right region, and the menu stays open.
- 5.70 Escape closes the menu.
- End at 7.3.

The frame reads 12/21 and the viewport is `translate(42.0449px, 77.5px) scale(1)` at every check. Poster at 3.11 s, after the drop.

This clip is now the earlier slide-14 take; 02b replaces it on the slide.

### 02b_v10_split_left_bottom (16.3 s, slide 14)

**Setup:**
1. The common graph setup, then Next until frame 12/21.
2. Off camera, a real drag moves the Status tab into the Pseudocode group's tab strip, after Pseudocode (drop target `group:g2:1`). The script clicks the Status tab only if it is not already in front.
3. The script checks that the right column is now one group, `g2`, with tabs Pseudocode | Status*.
4. The pointer is parked on empty canvas and a 2.3 s wait lets the frame-12 note fade.

**Recorded.** Each drag moves at constant speed for 2.2 s towards the centre of the drop target, measured once the drag is live. Every change of the hot target is logged.

1. Drag 1, 1.54–3.89: from the strip (1268, 55) down to (1280, 646).
   - Hot target: `group:g2:2` (own strip), then `split:g2:before` from 1.74 (preview over the upper half), then `split:g2:after` from 3.19 (preview over the lower half, box 1120,443 320×395).
   - Release at 4.40. The right column is two groups: `g2` Pseudocode at 1120,40 320×396 and `g4` Status at 1120,443 320×395. That is equal halves with a 7 px splitter.
2. Drag 2, 6.33–8.72: from the lower right strip (1156, 458) to (150, 454).
   - Hot target: own strip, then nothing over the drawing, then `group:g1` from 8.44 (preview box 0,71 300×767).
   - Release at 9.20. The left group `g1` has Action | E-Lecture | Status*, and the right column is `g2` Pseudocode alone, full height.
3. Drag 3, 11.13–13.52: from the left strip (202, 55) to (710, 778).
   - Hot target: own strip, then `split:g1:before` from 11.33, then nothing from 11.74, then `region:bottom` from 13.27 (preview box 307,568 806×270).
   - Release at 14.01. The bottom row opens as group `g5` with Status, box 307,568 806×270. That is exactly the drawing column's width, under the drawing.
   - The left group's front tab becomes E-Lecture, the tab next in line, per the layout model's `withoutTab`.
4. End at 16.3.

**Verified after every drop:**
- The footer reads `FRAME 12 / 21`.
- The `.react-flow` element is the same node as at the clip start, so the canvas never remounted.
- After drops 1 and 2 the canvas box (307,40 806×798), the viewport (`translate(42.0449px, 77.5px) scale(1)`) and the node centres are unchanged.
- After drop 3 the canvas box is 307,40 806×521. The viewport animates through `scale(0.9856)` at +0.2 s and settles at `translate(42.0449px, -61px) scale(1)`. That is the app's fit after a size change: every node moves up 138 px at the same zoom.

Poster at 15.42 s: the final state.

### 03_graph_drag_then_edit (8.0 s)

**Setup:** as in 02, at frame 12/21.

**Recorded:**
- 0.81–1.77 B is dragged by (+35, −35) px. The frame stays 12/21 and the B → A label still reads 1.
- 3.03 Draw graph is opened.
- 3.90 a click lands right of line 3 of the Edges text, putting the caret at the end of `B A 1`.
- 4.06 Shift+ArrowLeft selects the `1`.
- 4.50 typing `5` commits the edit straight away:
  - the edges text is `S A 4 / S B 1 / B A 5 / A T 2 / B T 6`;
  - the B → A label reads 5;
  - the footer reads `NO RUN`, Status reads `NO ACTIVE RUN`, and Pseudocode reads "No run".
- End at 8.0.

Poster at 5.10 s.

This clip is now the earlier slide-15 take; 03b replaces it on the slide.

### 03b_graph_drag_edit_parallel (16.2 s, slide 15)

**Setup:** as in 02, at frame 12/21.

**Recorded:**
- 1.00–1.63 B is dragged by (+35, −35) px. The frame stays 12/21.
- 3.51 Draw graph is opened.
- 4.40 click at the end of `B A 1`; 4.55 Shift+ArrowLeft; 5.00 type `5`:
  - the footer reads `NO RUN` and Status reads `NO ACTIVE RUN`;
  - the B → A label reads 5;
  - the Edges text is `S A 4 / S B 1 / B A 5 / A T 2 / B T 6`.
- 7.20 the pointer moves onto B's source handle (its right side). The handles show on hover.
- 7.60–9.04 a press and a 15-step drag to A's target handle (its left side), with React Flow's connection line following the pointer.
- 9.20 release. 9.50 the pointer moves to empty canvas.
- 10.81 click at the end of the new last line `B A`. The line's position is measured from the textarea, which the notice had moved down. The script checks the caret is at the end of the text (33 of 33) before typing.
- 11.22–11.59 type ` 2` (150 ms between keys).
- 12.21 the pointer moves to empty canvas.
- End at 16.2.

**Checked at 9.71, after the new edge:**
- 6 edges. Two are B → A: `edge-4`, with path control point (330.4, 309.2), and the new `edge-7`, with control point (365.6, 301.8). They bow to opposite sides, about 20 px apart at the middle.
- Still 5 weight labels. Each label is matched to the edge curve nearest it; each sits 14–15 px from its curve.
  - `edge-4` has 5, which moved with the curve from (703, 382) to (666, 389).
  - `edge-7` has none, because the app gives a canvas-drawn edge no weight.
- The Edges text ends with `B A`.
- The Action panel adds "1 edge has no weight, so it counts as 1. Set one under Draw graph → Edges, as in “B A 4”."
- Footer `NO RUN`; Status `NO ACTIVE RUN`.

**Checked at 11.72 and 12.41, after typing:**
- The Edges text is `S A 4 / S B 1 / B A 5 / A T 2 / B T 6 / B A 2`.
- 6 edges and 6 labels. `edge-4` has 5, and `edge-7` has the new label 2, at (712, 379).
- The notice is gone.
- Footer `NO RUN`; Status `NO ACTIVE RUN`.

**Throughout:**
- No text on the page says "parallel".
- The viewport stays `translate(42.0449px, 77.5px) scale(1)`, so there is no re-fit.

Poster at 13.20 s: the final state, with both B → A edges labelled (5 and 2).

### 04_dijkstra_note_pause_hover (10.2 s)

**Setup:** the common graph setup, then Next until frame 11/21, then wait 1.8 s. The pointer stays on Next.

**Recorded:**
- 0–2.5 hold at 11/21, "Inspect edge B → A, weight 1." The paused animations `edge-paused-streak` and `node-paused-glow` move from about 2.07 s to 4.45 s of their own time while the frame stays 11.
- 2.53 Next → 12/21, "Relax B → A: 1 + 1 = 2 is shorter than 4, so update A's distance to 2." The note "1 + 1 < 4 · update" is above A.
- 4.72 Last → 21/21, "Dijkstra complete. Settled 4 nodes."
- 5.92 hover T: "S → B → A → T · distance 4".
- 7.92 hover A: "S → B → A · distance 2".
- End at 10.2.

Poster at 2.95 s, frame 12/21 with the note.

This clip is now the earlier slide-18 take; 04b replaces it on the slide.

### 04b_dijkstra_big_note_pause_hover (14.0 s, slide 18)

**Setup:**
1. Open `/graph-editor/dijkstra` and untick Live force layout first, so the preset keeps its own positions.
2. Select preset → **Big** (visualgo.net's TESSELLATION). The script checks for 9 vertices (0–8) and 16 directed arcs:

   ```text
   0 1 8, 0 2 12, 1 2 13, 1 3 25, 4 1 9, 2 3 14, 2 6 21, 3 4 20,
   3 5 8, 3 6 12, 3 7 12, 3 8 16, 4 5 19, 5 7 11, 6 8 11, 7 8 9
   ```

3. Close the preset list and collapse Draw graph.
4. Start node is 0 (the default). End node stays "All vertices", because the UI allows it. The script checks both.
5. Click Fit view. The viewport is `translate(-4.47778px, -4.43333px) scale(0.777778)`.
6. Next until frame 17/53, where the script checks for "Inspect edge 2 → 3, weight 14.", then wait 1.8 s. The pointer stays on Next.

**Recorded:**
- 0–3.0 hold at 17/53. The paused animations move from about 2.10 s to 5.02 s of their own time while the frame stays 17.
- 3.03 Next → 18/53, "Relax 2 → 3: 12 + 14 = 26 is shorter than 33, so update 3's distance to 26." The note "12 + 14 < 33 · update" sits to the right of 3, next to its 33→26 badge.
- 6.05 Last → 53/53, "Dijkstra complete. Settled 9 nodes." The Path box reads "Choose an End node in the Action panel, or hover a vertex, to see its path from the start."
- 7.63 the pointer moves straight to 8: "PATH TO 8 / 0 → 2 → 3 → 8 · distance 42".
- 10.62 the pointer moves straight to 4: "PATH TO 4 / 0 → 2 → 3 → 4 · distance 46".
- End at 14.0.

The run has 53 frames. Frames 15–18 are: select 2, settle 2, inspect 2 → 3, relax 2 → 3.

The final table matches a hand trace:

| Vertex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Distance | 0 | 8 | 12 | 26 | 46 | 34 | 33 | 38 | 42 |

Poster at 3.45 s: frame 18/53 with the note fully shown.

### 05_bst_preview_apply (8.6 s)

**Setup:**
- Open `/tree-editor/bst` with the default tree.
- Choose Insert and enter value 5, then collapse Edit tree.
- Next starts the run; Last goes to 8/8; then wait 1.5 s.

**Recorded:**
- 0–1.5 frame 8/8, "Insertion preview is complete. Apply it to update the tree document." Apply insertion is visible. The committed text still has its 6 original lines while the canvas shows 8 nodes.
- 1.55 Previous → 7/8, "Node 6 has no left child: create node 5 there."
- 2.44 Previous → 6/8, "5 is smaller than 6; inspect the left child." The canvas shows 7 nodes.
- 3.32 Next → 7/8.
- 4.13 Next → 8/8. Apply insertion is shown only on this final frame.
- 5.22 Apply insertion: the footer reads `NO RUN` and Status reads `NO ACTIVE RUN`. The text gains `6 5`, and 8 nodes remain.
- 6.23 Edit tree is expanded: NODES 8, EDGES 7, DEPTH 3, with the text ending `6 5`.
- End at 8.6.

Poster at 0.52 s, the preview with Apply insertion.

### 06_dfs_recursive_recap (8.5 s)

**Setup:** the common graph setup on `/graph-editor/dfs-recursive`, then Next starts the run at 1/21 ("Initialize recursive DFS from S.").

**Recorded:**
- 0.83 Last → 21/21, "Recursive DFS complete. Visited 4 nodes." The visited order is S, A, T, B.
- After that, the final frame loops about every 3 s:
  - a glow on S;
  - a streak along S → A;
  - a glow on A;
  - a streak along A → T;
  - a glow on T;
  - a streak along S → B;
  - a glow on B;
  - a pause.
- End at 8.5.

Poster at 3.01 s.

## Where this differs from the brief

- **LCA, k = 2:** this tree has two steps where both ancestors are 8 (k = 2 and k = 1). For (6, 2) the k = 0 step also keeps u and v, with both ancestors 4. 01 starts just before k = 2. 01b starts at k = 2 already shown, so its first new note is the one for k = 1.
- **No on-canvas weight editing:** the app has none, so 03 uses Draw graph → Edges. That text commits on every valid change.
- **Panel move in 02:** the Status tab goes into the left group, not the bottom region, so the drawing size and viewport stay the same. Reset panel layout also asks for a fit; it changes nothing here because setup already pressed Fit view.
- **02b:** the three drops follow the requested order, and all of them were allowed.
  - Over Status's own group the app offers only two zones, the upper half (split before) and the lower half (split after); there is no middle zone. On the way down the preview first frames the upper half (from 1.74 s) and switches to the lower half at 3.19 s.
  - The bottom drop re-fits the drawing, as the app does whenever the drawing's size changes, so the nodes move up 138 px.
  - The left group falls back to E-Lecture, not Action, when Status leaves it.
- **03b: the parallel edge is drawn on the canvas, the preferred way, then given weight 2.**
  - Why the canvas: it took one real drag (B's source handle to A's target handle), it worked first time, and React Flow draws the connection line while dragging.
  - The app gives a canvas-drawn edge no weight. So the clip briefly shows that edge unlabelled, with the "counts as 1" notice.
  - The owner asked for a fourth step: click at the end of the new `B A` line and type ` 2`. The click landed at the end of the text as intended, and the textarea did not scroll.
  - The new edge then shows label 2 and the notice disappears. That also moves Draw graph back up by about 77 px.
- **04b:** the frames, Status sentences, final distances and both hovered paths all match the hand trace. A few details for the narration:
  - The note reads "12 + 14 < 33 · update" and sits to the right of 3, not above it.
  - The Keep steps say, for example, "Keep the distance to 2: 8 + 13 = 21 is longer than 12."
  - The two arcs out of 4, inspected last, say "Keep 1 unchanged because it is already settled." (frame 50) and "Keep 5 unchanged because it is already settled." (frame 52).
  - End node stays "All vertices", so no path shows until a vertex is hovered.
