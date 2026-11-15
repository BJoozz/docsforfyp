# Early standalone prototypes: stills

These stills come from the four early standalone prototype repositories, captured on 16 November 2026 for the CA presentation. They are not screenshots of the current VisuAlgo+ app. Each image comes from the prototype's own build at its last documented snapshot. `manifest.json` records the repository, commit, input, actions, what each image shows and a short caption.

| File | Prototype and snapshot | Caption |
| --- | --- | --- |
| `01_graph_v1_edit.png` | Graph prototype 1, `5fc06a0` (19 Aug 2026) | Graph prototype 1 (Aug 2026): separate editor view |
| `02_graph_v1_run.png` | Graph prototype 1, `5fc06a0` (19 Aug 2026) | Graph prototype 1 (Aug 2026): separate run view |
| `03_graph_v2_workspace.png` | Standalone Graph rewrite, `c8b14e6` (11 Sep 2026) | Standalone Graph rewrite (Sep 2026): one shared canvas |
| `04_tree_binary_lifting_table.png` | Tree Visualizer, `46ce0a7` (17 Sep 2026) | Standalone Tree prototype (Sep 2026): Binary Lifting table |
| `05_sorting_two_panes.png` | Sorting Room, `9236a65` (19 Aug 2026) | Sorting Room prototype (Aug 2026): panes share input |

The `*_crop.png` files contain the same pixels, cropped to the region that matters for a slide. The crop rectangles are listed in the manifest. Image 03 has no crop, because its canvas, editor and playback bar span the whole viewport.

## Reproduce

1. Clone each repository (`BJoozz/graph-algorithm-visualizer`, `BJoozz/graph-visualizer-v2`, `BJoozz/tree-visualizer`, `BJoozz/sorting-algorithm-visualizer`; all private) and check out the full SHA from the manifest. Each SHA is the tip of its repository's default branch.
2. In each repository run `npm ci`, then `npx vite --host 127.0.0.1 --port <port> --strictPort`. The capture used Node 24.17.0 and the Vite version locked by each repository.
3. Open `/` in Chromium (Playwright 1.64.1, Chromium 156) with a 1440×900 viewport, device scale factor 1, light colour scheme and the `en-US` locale. Wait for network idle and for the fonts to load.
4. Follow the `actions` listed for the image in `manifest.json`. They use only the visible controls. Steps are taken with Next and never with Play, so each run stays paused on a fixed step. Move the pointer away from the controls and screenshot the viewport or the full page, as the manifest states.

The captures used no source edits, injected state, CSS changes or added annotations. In image 05, the header badge "05 · Four-way" is a static milestone label in that build and stays the same with two panes.
