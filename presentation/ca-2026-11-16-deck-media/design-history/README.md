# Design history: stills

These stills come from the shared repository `kerktaiheng/visualgo-plus-design` (private), captured on 16 November 2026 for the CA presentation. They show how the visualisation page developed:

- Kerk's low-fidelity wireframes
- Bao's working builds of layouts V2 and V7
- Kerk's design-system UI kit

They are not screenshots of the current app. `manifest.json` records for each image the commit, author, path, input, actions, viewport, what it shows and a short caption. It also lists the exact wireframe titles V1–V9.

| Files | Source | Whose work |
| --- | --- | --- |
| `A1`–`A4` | `design/wireframes/wireframe 2 viz desktop.html` at `69aa8e4` (4 Sep 2026) | Kerk |
| `B1`–`B6` | `prototypes/{graph,tree,sorting}-visualizer-{split-rails,docks}` at `ae63a62` (18 Oct 2026, the last commit before those folders were deleted) | Bao; every commit to these folders is his |
| `C1`, `C2` | `design/design-system/ui_kits/visualgo-web/index.html` at `634b5be` (3 Sep 2026) | Kerk |

`A1_wireframes_at_a_glance.png` is the whole "At a glance" sheet as committed. It has twelve thumbnails: V1–V9 and the V1 states V1a–V1c. `A1_wireframes_at_a_glance_v1-v9_crop.png` holds the same pixels, cropped to the nine thumbnails V1–V9.

## Reproduce

Clone the repository with `git -c core.longpaths=true` and use the commits listed in the manifest.

- **A (wireframes).** Extract `design/wireframes` at `69aa8e4`. The tree at that commit contains `*:Zone.Identifier` files, which Windows cannot write; `git -c core.protectNTFS=false archive 69aa8e4 design/wireframes`, with those entries excluded on extraction, avoids them. Open the HTML file through `file://` in Chromium at 1600×1000 with device scale factor 2. Then take element screenshots of `.sheet` (A1), `#V2` (A2), `#V7` (A3) and `#V8` (A4).
- **B (V2/V7 builds).** Check out `ae63a62`. In each of the six folders run `npm ci`, then `npx vite --host 127.0.0.1 --port <port> --strictPort`. No submodule is needed, because each build imports the design system from `design/design-system` in the same checkout. Open `/` at 1440×900. Next is disabled until a run exists, so click Play once to start the run, pause at once, click First, then click Next the number of times given in the manifest. For sorting, first set Size to 24 and click Generate.
- **C (UI kit).** Extract `design/design-system` at `634b5be`, excluding the `*:Zone.Identifier` files as for A. Serve that folder with any static file server and open `/ui_kits/visualgo-web/index.html` at 1280×900 with network access, because React, ReactDOM and Babel load from the unpkg CDN. Capture the home screen (C1). Then click the "Binary Search Tree, AVL Tree" card for the visualisation screen (C2).

All captures used Chromium (Playwright 1.64.1), the light colour scheme and the `en-US` locale. They used no source edits, injected state, CSS changes or added annotations. The UI kit's fixed Theme switcher at the bottom right is part of the kit.
