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
node .\capture-deck.mjs 01_lca_equal_ancestors 01b_lca_keep_then_jump 02_v10_move_panel 03_graph_drag_then_edit 04_dijkstra_note_pause_hover 05_bst_preview_apply 06_dfs_recursive_recap
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

## Common graph setup (02, 03, 04, 06)

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
