# Reproduce the selected captures

Source: `kerktaiheng/visualgo-plus-design`, `main` at **346e84b838e87ae8affacdc54f0e0eb75eab1529**. Capture preparation started against `docsforfyp` **99990d0**. Media was captured 15–16 November 2026, Asia/Singapore.

## Common setup

- Use an isolated browser profile, Chromium, **1440 × 900**, device scale 1, 100% browser zoom, Light theme, English. Do not reuse a profile with saved experiments/layouts.
- OS/browser reduced motion: `no-preference`; leave “Animate paused steps” at its default on. Graph/tree speed is 0.50s; graph note emphasis can extend an individual step. Sorting target: 12 operations/s.
- Wait for the real workspace and loaded **Inter** font before measuring/capturing. Internet access to Google Fonts is needed by this revision.
- Start this app with `npm run dev -- --host 127.0.0.1 --port 5205 --strictPort` from `prototypes` (or use another unused port). No source edits, state injection, CSS hiding or fake text are used.

## Manual recipes

### Homepage / Editors

Open `/`, scroll to Editors. Capture only the real Editors region. The delivered image is a crop of the page, 1370 × 205; the visualizer images are full 1440 × 900 viewports.

### One Dijkstra example, reused

1. Open `/graph-editor/dijkstra`; turn **Live force layout off**. In Draw graph, enter nodes `S A B T`, one per line, then these directed edges:

   ```text
   S A 4
   S B 1
   B A 1
   A T 2
   B T 6
   ```

2. Set Start S, End T. Collapse Draw graph. Drag the four nodes into a diamond: S left, A above, B below, T right. The automation uses actual mouse drags, not injected coordinates/state.
3. Use Next to start, then advance to **frame 11/21**, Inspect B → A. Hold for ~2s: the frame must stay 11 while emphasis moves.
4. Next → **frame 12/21**, Relax B → A. Capture about 0.3s after arrival, while `1 + 1 < 4 · update` is visible above A. Status must say A changes to 2. Seeking directly to frame 12 will not reproduce a forward-arrival note.
5. While paused, drag B a little to the upper-right. The frame must stay 12. The graph MP4 ends here, before Last.
6. Last → **frame 21/21**. Hover T: Status must show `S → B → A → T · distance 4`. Hover A: `S → B → A · distance 2`; frame remains 21. These are the main/backup still pair.
7. Move the Status tab to the bottom-region target. Frame remains 21. This makes the V10 layout image; the resizing can refit the drawing normally.

### BST preview and Apply

1. Open `/tree-editor/bst` with the default seven-node tree (root 8).
2. Select Insert, value 5, collapse Edit tree. Next starts the run; Last reaches **frame 8/8**.
3. Capture the green insertion preview and Apply button. The canvas has 8 nodes, but the committed editor text still has only the original 6 edges.
4. Apply insertion. Capture the backup: node 5 remains, footer says No run, editor text has gained `6 5`. The preview is over.

Original tree text:

```text
12 8
4 8
14 12
10 12
6 4
2 4
```

### Two-pane sorting

1. Open `/sorting`, choose **2** panes, keep Dataset expanded. Distribution Custom input; values `8, 3, 10, 1, 6, 4, 12, 2, 9, 5, 11, 7`; seed remains `sorting-room-01` (the explicit custom values determine the input).
2. Generate. Set pane 2 to Selection **before** pane 1 to Bubble: the initial second pane uses Bubble and the UI refuses duplicate algorithms.
3. Next initializes the comparison at operation 0. Target speed 12 ops/s. Autoplay for about four seconds; Pause.
4. The delivered screenshot is at **Op 48/92**, both panes at 48, with different compare/swap/write counts. Timing can land a neighboring operation on a different machine. For an exact still, use the numeric operation field to set 48; this static screenshot does not depend on arrival notes.
5. Hold ~1s, resume ~3.5s, then Last. The last jump is an explicit seek, not measured execution speed.

## Automated recapture

The app already contains `@playwright/test`; this folder does not add another dependency tree. In PowerShell:

```powershell
$env:CA_APP_REPO = 'C:\path\to\visualgo-plus-design'
$env:CA_BASE_URL = 'http://127.0.0.1:5205'
$env:CA_CAPTURE_OUTPUT = 'C:\path\to\scratch\ca-recapture'
node .\capture.mjs graph
node .\capture.mjs tree
node .\capture.mjs sort
node .\capture.mjs home
```

Run sequentially. Recapture goes to the output folder, not over the ready-to-use files. The script drives real controls and reads DOM state for checks. It records raw WebM during setup too; only the final selected MP4s belong in the presentation pack. It may need a network-enabled process for Google Fonts/browser launch.

## Video export and QA

The delivered MP4s use H.264, yuv420p, 25fps, 1440 × 900, no audio and fast-start metadata. Encoding changes only format, not playback speed. No compositing, fake cursor, labels or UI overlays were added.

Original trim windows, selected by inspecting the recorded frame counter:

- Graph raw video: start 5.00s, duration 7.80s (11 → Next → 12; no final-frame jump).
- Sorting raw video: start 1.50s, duration 10.40s (play → pause → resume → Last).

**Recaptured videos need their own trim points.** Browser encoder startup means recording metadata time is not a reliable first-visible-frame time. Do not mechanically reuse those offsets. Select the boundaries against the actual UI counter.

Example conversion with a full ffmpeg build:

```text
ffmpeg -ss START -i raw.webm -t DURATION -an -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -movflags +faststart output.mp4
ffmpeg -v error -i output.mp4 -f null -
```

Both exports were decoded fully and sampled visually. Raw recordings, failed automation attempts, codec tooling and QA images are excluded from the delivered folder. Final workflow observations are retained in the four `*-checks.json` files; they are capture checks, not a complete project test report. Machine-specific raw-video paths are removed.
