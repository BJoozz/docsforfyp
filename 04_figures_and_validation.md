# 04 · Figures and validation evidence

Audit date: 2026-11-01/02\
Repository: `kerktaiheng/visualgo-plus-design`, `main` at `662e7b3`\
Evidence labels: VERIFIED / DOCUMENTED / INFERENCE / QUESTION\
The owner's answers of 2026-11-01 and 2026-11-03 are applied (doc 01, the table at its top): week 0 runs from 2026-07-28 to about 08-09 and all the standalone work is in scope; AI-assisted work is Bao's; the checklists were run but not recorded; Kerk's early layout survey has no record with Bao. Ids C1–C14 and Q1–Q17 follow note 09 (`evidence/research-notes/09-candidate-contributions.md`).

**Checked for this document on 2026-11-02 (read-only).** (a) I viewed the eight captures in `figures/` one by one and replayed their steps against the deployed build of `662e7b3`. (b) I re-queried GitHub with `gh` for the workflow runs, the 37 PRs and the standalone repositories' runs. (c) I counted test files, specs, records and checklists with `git` at `662e7b3`. I re-ran no test suite for this document; doc 02 reports a run of seven graph test files on 2026-11-02 (67 of 67 passed). Every other test result below comes from the runs of 2026-11-01: the app's check run (note 07 §2), whose logs I re-read, and the standalone unit runs (note 02). `git status` stayed clean.

## 1. Figures for the report

### 1.1 The set

Seven screenshots (F1–F4 and F6–F8) and the two diagrams D1 and D2 are the set, as Bao chose on 2026-11-03; F5 is a spare. All eight screenshots were captured; the two diagrams still have to be drawn.

| Id | Figure | Supports | File in `figures/` | Status |
|---|---|---|---|---|
| F1 | The homepage catalogue | C5, C12 | `F1-home-catalogue.png`, `F1-home-catalogue-fullpage.png` | captured, recommended |
| F2 | A visualizer page in the groups shell (BFS, frame 8) | C6 (BFS itself: C1) | `F2-dfsbfs-bfs-frame8.png` | captured, recommended |
| F3 | A tab held over another group | C6 | `F3-tab-drag-preview.png` | captured, recommended |
| F4 | Dijkstra's step note (frame 24) | C10 (Dijkstra itself: C1) | `F4-sssp-dijkstra-frame24-note.png` | captured, recommended |
| F5 | LCA Query(6, 2) and its note (frame 2) | C8, C10 | `F5-lca-query-6-2-frame2-note.png` | captured, spare |
| F6 | Binary Heap Insert: a climb and its note (frame 3) | C8, C10 | `F6-heap-insert-climb-note.png` | captured, recommended |
| F7 | Sorting Compare with four panes (operation 150) | C9 | `F7-sorting-compare-4-panes.png` | captured, recommended |
| F8 | Cut Vertex & Bridge on CP4 4.7 (last frame) | C7, C12 | `F8-cut-vertex-bridge-cp4-4-7-last.png` | captured, recommended |
| D1 | Architecture: from a URL to the canvas | C5, C6, C14 | none | to draw: doc 03's Diagram 1 plus the parts in §1.4 |
| D2 | The groups model: regions, groups, minimums, drop targets | C6 | none | to draw from §1.4 (no Mermaid exists yet) |

`figures/README.md` describes each PNG as it appears and holds the replay script.

### 1.2 Provenance and common setup

- **Captures.** A Playwright script in headless Chromium took them at 1440 × 900 at `662e7b3`, on 2026-11-01 between 23:52:47 and 23:53:07 (UTC+07:00, the machine's clock that day; 16:52–16:53 UTC; file times). The script was lost when its agent was cut off, so the steps below are a reconstruction. VERIFIED: the files, their sizes and their times. The tool and the commit are what the capture run reported.
- **Replay.** On 2026-11-02, between 13:57 and 14:15 (UTC+08:00), I ran the reconstructed steps against `https://kerktaiheng.github.io/visualgo-plus-design/`. Pages run 41095633645 deployed that site from `662e7b3` on 2026-10-30, and no workflow has run since. I used Chromium 156 (headless) through the repository's Playwright 1.64.1. Every replay reached the same frame and showed the same texts. F1 matched pixel for pixel. F2–F8 differed in 0.01–0.35% of their pixels, all of them in animated marks (a node's glow, a rising note, the final-frame motion), in the pointer's hover state or in where the ghost sits. VERIFIED. That the captures show the `662e7b3` interface is an INFERENCE from this match.
- **Setup.** Viewport 1440 × 900 at device scale 1, in an English locale. This PC's default locale is `vi`, under which F7's counter reads 1.825 instead of 1,825. Use a fresh profile, so that no theme, layout or dataset is restored from `localStorage`. The page needs network access to load the Inter font. A local build serves the same app: run `npm install`, then `npm run dev` at the repository root, and open http://127.0.0.1:5186 (`README.md`; DOCUMENTED, not run here).
- **Transport.** The footer buttons are, left to right: First, Previous, Next, Last, Autoplay and Stop. With no run, Next starts a paused run on Frame 1 (DD-24, Kerk's `a074f50`). Each further Next adds one frame, and Last jumps to the end. VERIFIED (replay).
- **Notes.** A step note appears when Next brings its step, then fades on its own. It is fully opaque about 0.5 s after the step arrives, down to 40% opacity by about 1.2 s and gone by about 1.9 s. It runs the `floating-text-rise` animation, 1.6 s long (`FLOATING_NOTE_MS = 1600` in `prototypes/src/shared/visualization/floatingTextTiming.ts`). Capture within about a second; if the note has gone, Previous then Next brings it back. VERIFIED (replay, 2026-11-02).

### 1.3 Each figure

**F1 · The homepage catalogue** (C5, C12). Captured: `F1-home-catalogue.png` (1440 × 900) and `F1-home-catalogue-fullpage.png` (1440 × 3076).
- Purpose: the site that hosts the three visualizers under one bar. It shows the editor cards and the catalogue, with what is built and what is not.
- Screen: route `/`, rendered by `prototypes/src/site/HomePage.tsx`. The cards come from `prototypes/src/site/modules.ts`: 30 cards, of which 8 are full, 4 partial and 18 "soon". Sample: none; the default light theme.
- Steps: open `/`, wait for the font, and capture the viewport. Then take a full-page capture.
- Check: 12 cards open (2 editors and 10 modules) and 18 carry "Coming soon". Four cards carry a count badge: "1 of 3", "5 of 7", "2 of 3" and "1 of 4".
- Caption: *"The VisuAlgo+ homepage at commit 662e7b3: the two editors, then the module catalogue taken from visualgo.net's list; 12 of 30 cards open and 18 are not built yet. The page is built on Kerk Tai Heng's design system and UI kit."*
- Credit: the design system, the UI kit, the NUS Computing and Optiver logos and the card list are not Bao's work (C5, C12). Prof Halim knows of and agrees to the use of visualgo.net's material (owner, 2026-11-03).

**F2 · A visualizer page in the groups shell** (C6). Captured: `F2-dfsbfs-bfs-frame8.png`. It shows a run in progress, not an idle page.
- Purpose: the anatomy of a page. The site bar is at the top, the panel groups sit around the canvas and the footer holds the transport.
- Screen: route `/dfsbfs`. Rendered by `prototypes/src/graph/app/App.tsx` inside `GroupsLayout` (`prototypes/src/shared/components/layout`), using `DEFAULT_LAYOUT`.
- Sample: the default graph `INITIAL_GRAPH` (`prototypes/src/graph/graph/samples/initialGraph.ts`): vertices A–F and 8 weighted, directed edges. The picker calls it "Custom graph". BFS runs from A, with End node "All vertices".
- Steps: open `/dfsbfs`, which opens on Breadth-First Search, and press Next 8 times.
- Check: the footer reads Frame 8 / 22, the Status panel says "Dequeue B and visit it." and pseudocode line 4 is lit.
- Caption: *"A visualizer page in the panel-groups layout (V10). Action and e-Lecture share a tab group on the left; Pseudocode and Status are stacked on the right; the canvas in the middle is never a tab. Breadth-first search from A on the default graph, frame 8 of 22."*
- Credit: BFS is inherited from graph-visualizer-v2 (C1). The layout is C6.

**F3 · A tab held over another group** (C6; DD-52; V10 choices 21 and 26, which are Bao's, as their Vietnamese quotation shows). Captured: `F3-tab-drag-preview.png`.
- Purpose: the shell's drag feedback. The preview draws the layout that a release would make, as choice 21 asked on 2026-10-17: "the drag must show what the release will change" (translated from the Vietnamese in `design/proposals/viz-shell-v10/README.md`).
- Screen: route `/dfsbfs` with no run. The preview pieces are `.groups__preview`, `.groups__preview-caret`, `.groups__ghost` and `.groups__target--edge` in `prototypes/src/shared/components/layout/GroupsLayout.tsx`. The drag starts after 6 px (`DRAG_THRESHOLD_PX` in `useGroupDrag.ts`), and Escape cancels it.
- Steps: open `/dfsbfs` and press the ACTION tab. Hold the button and move the pointer to the middle of the Pseudocode group's body (x ≈ 1280, y ≈ 316). Capture while still holding.
- Check: the Pseudocode body is framed in the accent colour and labelled "ACTION". A caret sits after the PSEUDOCODE tab, a ghost "ACTION" sits beside the pointer, and a dashed band runs along the drawing's bottom edge.
- Caption: *"Moving a panel: the Action tab is held over the Pseudocode group. The labelled frame and the caret in the tab strip show what a release does (the tab joins that group). The ghost follows the pointer, and the dashed band marks the empty bottom region as another drop target."*
- Credit: the shell code is Bao's (`72450e1`, `a876206`). 41 lines of `dropTargets.ts` are Kerk's (`c59c155`, `ae63a62`; choices 27 and 33, decided by Kerk and Bao together).

**F4 · Dijkstra's step note** (C10; DD-61, PR #32; Dijkstra itself is inherited from v2, C1). Captured: `F4-sssp-dijkstra-frame24-note.png`.
- Purpose: the shared note layer (`prototypes/src/shared/components/canvas/StepNoteLayer.tsx`) on the graph. It writes the verdict of a relax step on the drawing (`6b1a4fc`).
- Screen and sample: route `/sssp`, which opens on Dijkstra. Default graph, start A, End node "All vertices".
- Steps: press Next 24 times, then capture within about a second.
- Check: Frame 24 / 31. The green note "4 + 3 < 8 · update" sits between B → E's weight 3 and E's "8→7" badge. Status reads "Relax B → E: 4 + 3 = 7 is shorter than 8, so update E's distance to 7."
- Caption: *"A step note (DD-61). At frame 24 of 31, Dijkstra relaxes B → E and writes "4 + 3 < 8 · update" in green over E; the Status panel gives the same verdict in words. The note rises and fades on its own within about 2 s."*
- Note: DD-61 measures this same frame at 1440 × 900. The note sits between `3` and `8→7` and rises 0.39 px (DOCUMENTED).

**F5 · LCA Query and its note, spare** (C8, C10; TP-31, TP-34, PR #29). Captured: `F5-lca-query-6-2-frame2-note.png`.
- Purpose: Binary Lifting's Query run. It shows the note, the step strip and the extra "Ancestor table" tab beside Status.
- Screen and sample: route `/lca`, which opens on Query. The default tree is the "Balanced BST" sample text drawn as a rooted tree with root 8, which the picker calls "Custom tree". The defaults are u = 6 and v = 2, the last two nodes (`resolveLcaQuerySelection`).
- Steps: press Next twice, then capture within about a second.
- Check: Frame 2 / 6. The red note "same ancestor · keep u, v" sits over 8. Status reads "k = 2: both ancestors are 8, so u and v stay."
- Caption: *"Binary Lifting, Query(6, 2), frame 2 of 6: at k = 2 both ancestors read are 8, so the note says to keep u and v. The strip under the drawing shows the same comparison, and the ancestor table is a tab beside Status."*

**F6 · Binary Heap Insert and its note** (C8, C10; TP-33, TP-36). Captured: `F6-heap-insert-climb-note.png`.
- Purpose: one deep tree case, as note 09 advises. It shows the Binary Heap round (PR #25: Min/Max, 1-based indices, operation groups) and its notes (`94ec5db`).
- Screen and sample: route `/heap`. The default min heap is 2, 5, 3, 9, 7, 6, 8, 12, 10 (`MIN_HEAP_SAMPLE_VALUES`, `prototypes/src/tree/heap/sample.ts`). The default operation is Insert, with value 1.
- Steps: press Next 3 times, then capture within about a second.
- Check: Frame 3 / 9. The note reads "1 < 7 · swap up". Status reads "1 at index 10 is smaller than parent 7 at index 5, so swap upward."
- Caption: *"Binary Heap, Insert 1 into the default min heap, frame 3 of 9. The new item at index 10 is compared with its parent 7 at index 5, and the note says "1 < 7 · swap up". The array strip under the drawing shows the same items by index."*

**F7 · Sorting Compare** (C9). Captured: `F7-sorting-compare-4-panes.png`.
- Purpose: the multi-pane comparator inside the shared page. Four algorithms run on one dataset and one operation clock; in Compare mode only Status is shown.
- Screen and sample: route `/sorting`. The defaults are Random, size 48, seed `sorting-room-01` (`useSortingExperiment.ts`). The panes are Merge, Bubble, Quick and Radix (`DEFAULT_PANE_SET`), with Merge carried over from Study.
- Steps: press 4 in the Panes control in the bar, then press Next, which gives Op 0 / 1,825. Type 150 into the "Go to operation" box and press Enter.
- Check: the counter reads Op 150 / 1,825 and every pane says "Paused". Numbers must use English formatting.
- Caption: *"Sorting in Compare mode: Merge, Bubble, Quick and Radix Sort on one dataset (48 random values, seed sorting-room-01) and one clock, paused at operation 150 of 1,825. Each pane counts its own comparisons, swaps and writes."*
- Credit: the sorting core (generators, operations, renderer) is inherited from Bao's standalone repository (C2). C9 covers only the integration.

**F8 · Cut Vertex & Bridge** (C7; DD-60, PR #28). Captured: `F8-cut-vertex-bridge-cp4-4-7-last.png`.
- Purpose: a graph algorithm added in VisuAlgo+ (`0fc105c`), shown on one of visualgo.net's example graphs (DD-48).
- Screen and sample: route `/dfsbfs/cut-vertex-bridge`. The sample is "CP4 4.7", which is visualgo.net's example `CP3_4_9` in `prototypes/src/graph/algorithms/visualgoExamples.ts`. The algorithm reads it as undirected.
- Steps: press Select preset, then CP4 4.7. The list stays open, as DD-29 intends. Then press Next and Last.
- Check: Frame 51 / 51. Status ends "Done: 3 cut vertices (4, 3, 1) and 2 bridges (3 — 4, 0 — 1)."
- Caption: *"Cut Vertex & Bridge on visualgo.net's example graph CP4 4.7, last frame (51 of 51). Each vertex shows num,low. Vertices 1, 3 and 4 are cut vertices (double ring), and edges 0–1 and 3–4 are bridges (green)."*
- Credit: the sample graph comes from visualgo.net (used with Prof Halim's agreement, owner 2026-11-03).

### 1.4 Diagrams to draw (not captured)

D1 extends doc 03's Diagram 1 (module boundaries), which lacks the homepage branch, `useTheme.ts` and Pages. D2 has no Mermaid yet: doc 03's Diagram 2 shows the shell's state cycle, not its regions, minimums and targets. Before using a drawing, check each box against the paths below. If boxes are shaded by origin, use only the attributions of C1, C2, C5, C6 and C14.

| Id | It must show (VERIFIED at `662e7b3`) | Suggested caption |
|---|---|---|
| D1 | The routes `/`, `/:slug` and `/:slug/:algorithm` go to `prototypes/src/main.tsx` and then `prototypes/src/site/App.tsx`, which holds the router and the only theme writer, `prototypes/src/site/useTheme.ts`. From there the path splits two ways: `HomePage` with the cards from `prototypes/src/site/modules.ts`, or `ModulePage` → `HostedModule` (`HostChromeContext`, `renderTopBar` → `ModuleBar`). `HostedModule` mounts one of `prototypes/src/graph/app/App.tsx`, `prototypes/src/tree/app/App.tsx` and `prototypes/src/sorting/app/App.tsx`. All three import `GroupsLayout`/`useGroups` from `prototypes/src/shared/components/layout`, and the graph and tree also mount `prototypes/src/shared/components/canvas/StepNoteLayer.tsx`. The design system is `design/design-system` (through `@ds`). `.github/workflows/pages.yml` serves the app at `/` and Kerk's `wasm-arch` demo at `/engine/`; the app does not use the engine | *"How a URL becomes a visualizer page. The site's router and top bar host one of three visualizers, which share the groups shell and the canvas layers in src/shared. GitHub Pages serves the build; Kerk's engine demo is deployed beside it and is not used by the app."* |
| D2 | `LayoutState` holds three regions (`left`, `right`, `bottom`; `REGION_SIDES`) around a drawing that is never a tab. Each region is a stack of groups (`Region`, `Group`), and each group is a set of tabs (`PANEL_IDS`: action, electure, pseudocode, status, plus `extra:*` such as the LCA ancestor table). `DEFAULT_LAYOUT` puts g1 [Action, e-Lecture] on the left (300 px) and g2 [Pseudocode] over g3 [Status] on the right (320 px), with the bottom empty. `resolveLayout` keeps a 360 × 320 drawing (`DEFAULT_MIN_DRAWING`) and groups at least 240 px wide (`GROUP_MIN_WIDTH`) and 120 px high (`GROUP_MIN_HEIGHT`). A drop target (DD-52) is one of four kinds: a strip slot or a group's body (both `group`), a `split` before or after a group, or a `region`. `canDrop` and `dropTransition` judge a drop. `useGroups` saves the layout in `localStorage` | *"The groups model. Three regions, each a stack of tab groups, around a fixed drawing; the default layout; the minimums the resolver keeps; and the four kinds of drop target."* |

## 2. Test and validation evidence

### 2.1 The check run of 2026-11-01

All results below are VERIFIED from the logs of this run (note 07 §2). Environment: Windows 11, Node v24.17.0, npm 11.13.0 and Playwright 1.64.1, on `main` at `662e7b3`; the working tree was clean before and after. Times are UTC+07:00. A script ran the steps one after another from the repository root; the browser step ran from `prototypes/` with `VA_PORT=5950`.

| Step | Command | Start | Time | Result |
|---|---|---|---|---|
| Types | `npm run typecheck` (`tsc -b`) | 22:34:58 | 24 s | exit 0, no diagnostics |
| Lint | `npm run lint` (`oxlint`) | 22:35:22 | 2 s | exit 0; 0 errors, 2 warnings (`react(only-export-components)` at `prototypes/src/site/ModuleBar.tsx:46` and `:66`) |
| Unit | `npm test` | 22:35:24 | 50 s | `node:test` 654/654 (3.3 s); vitest 235 files, 2,619/2,619 (42.8 s) |
| Build | `npm run build` | 22:36:14 | 19 s | 874 modules; `prototypes/dist/404.html` and `prototypes/dist/_redirects` written; a warning that one chunk is over 500 kB (704.99 kB, gzip 206.24 kB) |
| Browser | `npx playwright test --output C:/Users/123ba/AppData/Local/Temp/pw-fyp-audit` | 22:36:33 | 112 s | **151 passed (1.8 m)**, 3 workers, Chromium, 0 failed, 0 flaky |
| Unit (JSON) | `npx vitest run --reporter=json` | 22:38:59 | 39 s | the same 2,619 cases in 235 files (578 suites) |

- The browser suite needs network access: `prototypes/e2e/ready.ts:40-47` fails a case when Inter cannot load. The log also shows console noise that failed nothing (four ResizeObserver messages and some React Flow warnings).
- At 22:46 the deployed site answered `curl` with HTTP 200 at `/` and at `/engine/`.
- CI on the same commit (VERIFIED, run logs): `app` run 41095633732 passed 654 + 2,619 unit cases and 151 browser cases (7.5 m, 1 worker, Node v22.23.4). `ci` run 41095633621 and `pages` run 41095633645 also passed.
- Not run: Kerk's `wasm-arch` engine suite (which `ci.yml` runs), the 130 Node tests at `053064f`, the tip of the local branch `bj/engine-package-spike` (loop-generated tests included: 105 in the 9 files the study added, 25 in Kerk's own; counted on 2026-11-02), `npm run screenshots` and the manual checklists.

### 2.2 Unit suites per folder

| Folder | Runner | Test files | Cases (2026-11-01) | Passed |
|---|---|---:|---:|---:|
| `prototypes/src/graph` | `node:test` (`--experimental-strip-types`) | 93 | 654 | 654 |
| `prototypes/src/tree` | vitest 4 | 187 | 1,881 | 1,881 |
| `prototypes/src/shared` | vitest | 15 | 143 | 143 |
| `prototypes/src/sorting` | vitest | 32 | 571 | 571 |
| `prototypes/src/site` | vitest | 1 | 24 | 24 |
| **Total** | | **328** | **3,273** | **3,273** |

I re-counted the files on 2026-11-02; the cases come from the 2026-11-01 log and JSON. From note 07 (VERIFIED there): 47 files run in happy-dom rather than a real browser; about 13 files generate seeded random inputs; one type-level contract (`prototypes/src/graph/tests/primContracts.typecheck.ts`) is checked by `tsc -b`; TypeScript runs in `strict` mode. There is no property-testing library: the random tests are hand-written.

### 2.3 Browser specs (`prototypes/e2e`)

There is one Playwright project, `chromium` (Desktop Chrome at 1280 × 900). The case counts come from `playwright test --list` on 2026-11-01; I re-counted the lines on 2026-11-02.

| Spec | Cases | Lines | What the cases cover |
|---|---:|---:|---|
| `tree.spec.ts` | 62 | 2,291 | tree routes and the Tree Editor; LCA two runs (TP-31), hover (TP-32), notes (TP-34, TP-36), legend (TP-35); Binary Heap operations (TP-33); centre-to-centre edges (TP-30) |
| `graph.spec.ts` | 15 | 397 | each graph card's route and switching; a run under the site chrome; the Speed timer (DD-17); legend pass-through (DD-13); the Graph Editor through eleven algorithms; the tab strip keeps its front tab in view (DD-54) |
| `home.spec.ts` | 12 | 226 | homepage grid, editor cards, search, links, unknown routes, theme persistence |
| `sorting.spec.ts` | 11 | 213 | mount, nav, deep links, Compare panes, run lifecycle, restart plays (SP-01), theme on the canvas |
| `graph-traversal.spec.ts` | 10 | 421 | Topological Sort (DFS, Kahn), Bipartite Check and Cut Vertex & Bridge on CP4 samples |
| `dijkstra.spec.ts` | 8 | 309 | Dijkstra's notes (DD-61): text, colour, placement, 1366 × 768 with the legend open |
| `journey.spec.ts` | 8 | 245 | every card in one session, back and forward, full screen, asset base, favicon, card pictures |
| `prim.spec.ts` | 5 | 172 | Prim routes, MST defaults to Kruskal, cancelled runs, nav reachable at desktop widths |
| `themes.spec.ts` | 5 | 283 | WCAG contrast ≥ 4.5:1 for sampled text on three pages and the homepage in all nine themes; partner logos |
| `chrome.spec.ts` | 4 | 93 | search text in every theme, the Privacy panel, a modal by keyboard, footer and bar contents |
| `drawing.spec.ts` | 4 | 114 | the tree, graph and sorting canvases really draw; React Flow follows the site theme |
| `paused-motion.spec.ts` | 4 | 75 | "Animate paused steps", reduced motion, sorting without it |
| `bellman-ford.spec.ts` | 2 | 32 | deep links to Bellman-Ford run the signed sample |
| `play.spec.ts` | 1 | 81 | Autoplay starts a run in each visualizer; a refused start brings back the Action panel |
| **14 specs** | **151** | **4,952** | all passed on 2026-11-01 |

The suite runs in Chromium only, at desktop viewports only (720 × 900 to 1920 × 1080 in the specs), with no retries. On 2026-10-18 the browser suite went from 208 spec files to 12 (Kerk's `0394b64`); the kept layout alone had 74. Bao has since added `graph-traversal` and `dijkstra`. VERIFIED.

### 2.4 Property and oracle tests (VERIFIED in code; passed on 2026-11-01, and the five graph files again on 2026-11-02, doc 02 §2.2)

| Test (under `prototypes/src/`) | Inputs | Checked against |
|---|---|---|
| `graph/algorithms/topologicalSort/topologicalSortProperty.test.ts` | seeded (mulberry32): 300 random DAGs; 400 mixed random graphs, over 100 of them with a cycle | every edge runs forward; an independent three-colour cycle search |
| `graph/algorithms/bipartiteCheck/bipartiteCheckProperty.test.ts` | 400 random undirected multigraphs (84 not bipartite), 300 directed ones | an independent BFS 2-colouring |
| `graph/algorithms/cutVertexBridge/cutVertexBridgeProperty.test.ts` | seeds 1–400, random multigraphs | brute force: does removing the vertex or edge raise the number of components? |
| `graph/algorithms/bellmanFord/createBellmanFordSequence.test.ts:241` | signed multigraph fixtures, directed and undirected, every source | an all-pairs oracle (line 224), including reachability through negative cycles |
| `graph/algorithms/prim/primEngine.test.ts:278` | seeded signed multigraphs, every start | exhaustive search for the minimum spanning forest weight |
| `tree/algorithms/heap/createHeapCreateSequence.test.ts:166` | 200 random lists per order and method | a valid heap of the same values |
| `shared/components/layout/groupsModel.test.ts:1210` | 4,000 seeded random layout operations on 5 page sizes and 3 drawing floors | every model invariant after every step |

### 2.5 Standalone repositories (week 0 and the first FYP weeks; in scope)

| Repository @ commit | Unit run on 2026-11-01 (note 02, on `git archive` copies) | CI history (`gh`, 2026-11-02) |
|---|---|---|
| graph-algorithm-visualizer @ `5fc06a0` | 24 files, 162/162 | "Quality checks": 7 runs (6 success, 1 cancelled); the last, on `5fc06a0` (2026-08-19), passed |
| graph-visualizer-v2 @ `c8b14e6` | 276/276 | "CI": 19 runs (18 success, 1 cancelled); the last, on `c8b14e6` (2026-09-10 UTC), passed |
| tree-visualizer @ `46ce0a7` | 90 files, 664/664 | no CI (0 runs) |
| sorting-algorithm-visualizer @ `9236a65` | 18 files, 334/335; the one failure is `Metrics.test.tsx`, which expects "1,234" where this PC's `vi-VN` locale prints "1.234" | no CI (0 runs) |

### 2.6 CI history (GitHub Actions; re-queried 2026-11-02; dates UTC)

| Workflow | Written by | Runs | Success | Failure | Cancelled | Period |
|---|---|---:|---:|---:|---:|---|
| `app` (lint, types, unit, build, browser) | Kerk, `0394b64` | 55 | 49 | 1 | 5 | 2026-10-18 to 10-30 |
| `prototypes` (per app copy; graph and tree suites) | Bao, `37075b1`; replaced on 2026-10-18 | 50 | 41 | 4 | 5 | 2026-09-20 to 10-18 |
| `ci` (Kerk's engine tests in Docker) | Kerk | 113 | 112 | 1 | 0 | 2026-09-04 to 10-30 |
| `pages` (build and deploy) | Kerk | 48 | 43 | 2 | 3 | 2026-09-04 to 10-30 |
| **Total** | | **266** | **245** | **8** | **13** | |

| Date | Workflow, commit (author) | What failed | Fixed by |
|---|---|---|---|
| 2026-09-04 | `pages`, `69aa8e4` (Kerk) | the deploy step | green again at `df99dac` (Kerk, 2026-09-14) |
| 2026-09-13 | `ci` and `pages`, `598193b` (Kerk) | the Docker build step | `df99dac` |
| 2026-09-23 | `prototypes`, PR branch, `05b4b4a` (Bao) | the whitespace check | `1af2c72`, whose run started about 6 minutes later |
| 2026-10-10, 10-14, 10-14 | `prototypes`, `main`: `c620145`, `c3f6508`, `f510477` (Bao) | tree browser suites: "BST Traversal at 864x768 with long values" | PR #7 (`3a6443b`): the test assumed that a 20-character label overflows, but it fits with Linux fonts; `main` was green at `fb0b6a9` |
| 2026-10-25 | `app`, PR #32, `b47d437` (Bao) | 1 of 148 browser cases: `tree.spec.ts:1112` (an LCA note over the open legend) | `b309309`, 11 minutes later: a pixel pin became a bound |

`main` was red in the old workflow for three pushes in a row (2026-10-10 to 10-14). Both browser-suite failures came from text metrics that differ between Windows and CI's Linux (the cause is DOCUMENTED in PR #7 and `b309309`). Every merged PR shows green checks on its last commit; failures earlier inside a PR appear only in the run list (VERIFIED [07]).

**Test growth.** The PR bodies record the implementer's local counts (DOCUMENTED, not re-run). They grow from 545 + 2,217 unit cases and 83 browser cases in #20 (Kerk, 2026-10-18), through 626 + 2,421 and 117 in #28, to 654 + 2,619 and 150 in #37 (2026-10-30). The check run's 151st browser case is PR #35's tab-strip test (`graph.spec.ts:299`), which joined #37's branch in the merge `6fa4981`.

### 2.7 Measured numbers in the records (dated observations)

These are numbers that someone measured once, on one machine and one build. They are not benchmarks, and none of them runs in CI.

| Date | Where | What | Numbers as written | Caveat |
|---|---|---|---|---|
| 2026-08-13 | `prototypes/docs/sorting/sorting-performance-milestone.md` (copied from the standalone repository, `9236a65`) | eager generation of a whole run, single post-warm-up readings, Node v24.17.0 | n = 10,000: 33.65 ms (Counting) to 1,328.1 ms (Random Quick) | "development diagnostics"; measures the standalone engine; the app caps generated input at 160 values; its `npm run profile` script is not in the app |
| 2026-09-25 | `design/proposals/sorting-v2-v7/README.md:349` (`ee4bb72`) | producing the default set at n = 240 | "about 5 ms warm" | a single reading in a proposal |
| 2026-10-03 | `prototypes/docs/graph/BELLMAN_FORD_ACCEPTANCE.md` | sequence generation, four 40-node cases, median of 3 | 243–25,684 frames; 1.94–139.16 ms; 0.30–32.05 MiB retained | "observations, not guarantees or supported limits"; the frame counts predate DD-44; the script was removed on 2026-10-18 |
| 2026-10-05 | `prototypes/docs/graph/PRIM_ACCEPTANCE.md` | 4 fixtures, warm medians, i9-13900H | timeline 1.363–27.495 ms; inspector render 0.7–26.6 ms; contrast: text ≥ 4.5:1, strokes ≥ 3:1, one exception at 2.84:1 | "does not establish an input cap or guarantee a frame budget"; "not a full accessibility certification"; scripts removed on 2026-10-18 |
| 2026-10-16 | `design/proposals/viz-shell-v10/README.md:608` (`55f3387`) | the tree canvas refitting after a size change | 382–401 ms | a single reading |
| 2026-10-24 | `prototypes/docs/tree/DESIGN_DECISIONS.md:3420` (TP-36, `7180d81`) | badge widths for note placement | 70.1–78.3 px | layout geometry |
| 2026-10-25 | `prototypes/docs/graph/DESIGN_DECISIONS.md:2734-2742` (DD-61, `b47d437`) | note placement at 1440 × 900 | each note centred within 0.01 px; the placement options move 88 of 444 notes | layout geometry; the browser suite pins it as bounds |

Lines that mention a measurement: 14 in the graph records, 16 in the tree records and 6 in the sorting records (VERIFIED, `grep -c`). Most are pixel geometry. Durations such as "each wave at most 420ms" are chosen design values, not measurements.

### 2.8 Acceptance records and manual checklists

| Record | Date | What it records | Can it be re-run today? |
|---|---|---|---|
| `prototypes/docs/graph/BELLMAN_FORD_ACCEPTANCE.md` | 2026-10-04 (`6417767`) | checks "the original A-E plan, Codex's, which the owner asked for but has not reviewed" against the code; unit, browser and hosted-route gates; the timings of §2.7 | no: its profile script went with the standalone builds on 2026-10-18 |
| `prototypes/docs/graph/PRIM_ACCEPTANCE.md` | 2026-10-05 (`490e1d1`) | the final gates; a nine-theme contrast sweep; profiles; "eight engine mutants were caught again using the V2 mutation tool" | no: the profile, mutation and acceptance scripts went on 2026-10-18 |

Both were written with Codex in the stage commits `6417767` and `490e1d1`, at Bao's request (DD-38, DD-39); their last edit is `02c4e12` (2026-10-30). The tree and sorting have no acceptance record. VERIFIED (commits).

| Manual checklist | Section (line) | Items | Ticked |
|---|---|---:|---:|
| `prototypes/docs/graph/DEVELOPER_GUIDE.md` | "Manual checklist for the page" (266) | 20 boxes | 0 |
| `prototypes/docs/sorting/DEVELOPER_GUIDE.md` | "Manual checklist for the page" (111) | 10 boxes | 0 |
| `prototypes/docs/tree/DEVELOPER_GUIDE.md` | "Checklist for a page change" (493) | 26 bullets | no boxes |

No file records a dated run of any checklist (VERIFIED). Per Bao (2026-11-03), they were run partly by him by hand and partly by agents, and nothing was recorded (DOCUMENTED). The shell's drag, split and splitter scenarios appear in the graph and tree checklists, not in the sorting one. Bao's PR #36 records them as manual (review S2-02, 2026-10-28; DOCUMENTED); one browser case, `prototypes/e2e/graph.spec.ts:299` (PR #35), drives a column splitter by keyboard and pointer (VERIFIED).

### 2.9 Review sessions

| Session (review date) | Findings | PR, commit | Tests that hold the fix (exist and passed) |
|---|---|---|---|
| 1 (2026-10-26) | F01 a browser case failed without Google Fonts; F02 the Node floor; F03 root scripts swallowed flags; F04 CI uploaded traces that were never written | #34, `a5bb08f` | `prototypes/e2e/ready.ts:40-47`; F02–F04 are configuration |
| 2 (2026-10-27) | S2-01 a narrowed side strip hid its front tab; S2-02 the shell drag scenarios stay manual; a docs sweep, and S2-03 the shell copy rule retired | #35 `fd9ff5c`; #36 `02c4e12` | `prototypes/e2e/graph.spec.ts:299` (DD-54) |
| 3 (2026-10-29) | S3-01 the graph stalled while Speed kept changing; S3-02 a sorting restart did not always play; S3-03 stale records | #37, `9baa117` | `prototypes/src/graph/visualization/playbackCountdown.test.ts`, `prototypes/e2e/graph.spec.ts:113` (DD-17), `prototypes/e2e/sorting.spec.ts:107` (SP-01) |

PRs #34, #35 and #37 say each finding was "reproduced before the fix"; #36 is docs only (DOCUMENTED). Earlier review findings appear in two places. PR #17 fixed "three verified findings of a review" of the V10 shell (choices 24–26). PR #27 fixed a defect from "Codex's review of #25/#26". The repository holds no review document. Per Bao (2026-11-03), the three sessions were Codex reviews that he read first; Claude verified each finding before fixing it, and the fix options were Bao's choices (DOCUMENTED).

### 2.10 Who wrote the tests

`git blame -w -M` at `662e7b3` (VERIFIED [07]):
- Bao (`123baoek31@gmail.com`) last changed 4,887 of the 4,952 spec lines and almost all unit-test lines. Kerk last changed 65 spec lines.
- 159 of Bao's non-merge commits on `main` touch a test or spec file, and 148 of these carry a `Co-Authored-By: Claude` trailer (re-checked on 2026-11-02).

The tests were written with Claude under Bao's direction and are his (owner, 2026-11-03). This audit states that they exist and passed; it did not measure what they cover.

## 3. What does not exist

| Missing | How it was checked | Label | What the report can say instead |
|---|---|---|---|
| A user study, usability test, survey, interview, participant data or any measure of learning | `git grep` over the whole repository (note 07 §6). "participants" matches only AVL rotation nodes, and "survey" only "surveyed from visualgo.net". Outside the repository: Kerk organised a survey of a group of users that informed the choice of V2 and V7 (owner, 2026-11-03); Bao holds no record of it | VERIFIED (repository); DOCUMENTED (owner) | "VisuAlgo+ has not yet been evaluated with users; an early survey of a group of users, run by Kerk, informed the choice of two layouts." Cite its data only once Kerk provides it |
| Feedback from students, Kerk or the supervisor | no feedback record in the repository; 0 comments on 37 PRs. The V10 choices 27 to 48 record Kerk's and Bao's joint decisions after testing the deployed build (owner, 2026-11-03). The supervisor's early direction is in Bao's project description (doc 05 §1.1) | VERIFIED (no record); DOCUMENTED (owner) | the joint V10 fixes, and the layout survey, as Bao describes them |
| A benchmark or performance test | no profile or benchmark script in `prototypes/package.json` or `prototypes/scripts`, and no workflow runs one; the dated profiles' scripts are gone | VERIFIED | quote a §2.7 number with its date, build and caveat |
| A code-coverage figure | no coverage package is installed (`@vitest/coverage-*` appear only as vitest's optional peer dependencies in `package-lock.json`; no `c8`, no `nyc`) and nothing is configured | VERIFIED (2026-11-02) | "3,273 unit cases and 151 browser cases passed on 2026-11-01." |
| Cross-browser and mobile runs | `playwright.config.ts` has one project, `chromium`. The stated targets are desktop and laptop windows, with "the phone version … designed separately" (`prototypes/docs/graph/AGENTS.md:36-43`) | VERIFIED; DOCUMENTED | "Tested in Chromium at desktop window sizes." |
| An accessibility audit | no axe-core, Lighthouse or pa11y. Contrast is sampled in `themes.spec.ts` and three unit tests; the Prim sweep says it is "not a full accessibility certification"; graph backlog item 14 lists shared colours below the minimums | VERIFIED | "Text contrast is tested at 4.5:1 for sampled chrome text in nine themes." |
| PR reviews | 37 PRs (36 merged, 1 closed) with 0 reviews and 0 comments (`gh`, 2026-11-02). 90 of Bao's commits reached `main` without a merge commit (2026-09-29 to 10-15) | VERIFIED | describe §2.9 as Codex review findings that Bao read, that were reproduced, and whose fixes he chose |
| A recorded run of the manual checklists, or browser tests of the shell's drag and split | §2.8; the drag and split scenarios are manual by choice | VERIFIED; DOCUMENTED | "Manual checklists exist and were run by hand and by agents; no run was recorded." |

## 4. Proposed future evaluation (proposals only, not claimed)

None of these exists or has been run. They would suit the rest of the FYP after the CA report (due 2026-11-04 17:00 SGT).

| # | Proposal | Question it answers | Outline | Prerequisites |
|---|---|---|---|---|
| P1 | A small user study | Can students do typical tasks, and where do they struggle? | 6–10 students who have taken a data-structures course. Four or five tasks, with think-aloud, for example: say when and why E's distance changes in Dijkstra; find LCA(6, 2) and the k values used; insert 1 into the heap and count the swaps; put Status beside Pseudocode. Record task success, time, errors and comments, then give the System Usability Scale questionnaire | the supervisor's agreement; check which NUS ethics approval applies before recruiting (QUESTION); a consent form |
| P2 | A task comparison with visualgo.net | For the same tasks, is VisuAlgo+ quicker or slower, and is it preferred? | within-subjects, with the order of the two sites counterbalanced; only tasks both sites support, on the same example graphs (DD-48 copied them); record completion, time, errors and the reasons for any preference | P1's setup; Prof Halim's agreement to the use of visualgo.net's material (owner, 2026-11-03) |
| P3 | Performance measurement on large inputs | How does the app behave at its input caps? | a Playwright script against a production build. It records sequence generation, time to first frame, frame intervals during Autoplay and JS heap. Inputs: the Large samples, generated graphs of growing size, sorting at 160 generated and 240 typed values, and a 31-item heap. Take the median of at least 5 runs on two machines, and restore the removed profile scripts in the app | none |
| P4 | An accessibility audit | Does the app meet WCAG 2.2 AA where it matters? | run `@axe-core/playwright` on every route in all nine themes. Do a keyboard-only pass (the tab menu as the drag alternative, DD-54) and a screen-reader pass (NVDA). Then fix graph backlog item 14 | none |
| P5 | Cross-browser and window-size runs | Do the 151 cases hold in Firefox and WebKit, and at the target windows? | add `firefox` and `webkit` projects to `playwright.config.ts`, and run at the windows listed in `prototypes/docs/graph/AGENTS.md:36-43` | CI time |
| P6 | Coverage | Which code do the tests reach? | `@vitest/coverage-v8` for the vitest suites and Node's `--experimental-test-coverage` for the graph suite, reported per folder. Coverage measures how much code the tests reach, not how good they are | none |
| P7 | Dated manual checks and code review | Close the "never recorded" gaps | run the three checklists at 1440 × 900 and 1280 × 800, recording the date, build, result and screenshots; ask one reviewer per PR and keep the review on GitHub | a reviewer |

## 5. Open questions that touch this document

- **Q1**: the exact date of Week 1 of the semester (about 2026-08-10), which ends week 0. The standalone evidence (§2.5) is included in line with Bao's answer.
- **Q8**: Kerk's survey data behind V2 and V7, if the report is to cite it rather than mention it.
- **Q11**: whether the dated profiles of §2.7 should be cited.
- Everything else that touched this document was settled on 2026-11-03 (doc 01, the table at its top).
