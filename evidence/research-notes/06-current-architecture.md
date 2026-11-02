# 06 · Architecture of the current app (main at 662e7b3)

Evidence audit for the FYP report. Student: Bao (Truong Van Quoc Bao, GitHub BJoozz). Collaborator and repository owner: Kerk Tai Heng (GitHub kerktaiheng). Written 2026-11-01.

**Labels.** VERIFIED = I saw it in code, a diff, a log or a test run. DOCUMENTED = a doc, commit message or code comment says it, and I did not check it against code. INFERENCE = my reading. QUESTION = Bao needs to answer.

## 0. How this was checked

- VERIFIED: the repository was on `main` at `662e7b3` with a clean working tree. I read the three ARCHITECTURE docs and a few files (`vite.config.ts`, `package.json`, `src/main.tsx`, `src/site/App.tsx`, `src/site/modules.ts`) directly from that clean tree, read-only. For everything else I extracted `git archive 662e7b3 prototypes` (and later `design/design-system`, which two tests read) into a folder under `%TEMP%` and read from there, so every line cited is `662e7b3`. `git status` was still clean at the end.
- I read `prototypes/docs/{graph,tree,sorting}/ARCHITECTURE.md` and `prototypes/AGENTS.md` first. Then I checked each claim in the code with grep and short line ranges. Paths below are relative to `prototypes/` unless they start with another top folder.
- **Tests I ran myself** (2026-11-01, about 22:48 +07:00, Node v24.17.0, on the archive copy, with packages read through a link to the installed `node_modules`):
  - `node --experimental-strip-types --test src/graph/visualization/*.test.ts`: 7 files, **45 of 45 passed** (VERIFIED).
  - vitest 4.1.11 on 29 files: everything under `src/shared` and `src/site`, `src/sorting/comparison/*`, `src/sorting/app/usePageLayout.test.tsx`, `src/tree/visualization/*` and `src/tree/components/layout/useGroups.test.tsx`: **295 of 295 passed** (VERIFIED). My first run had 2 failures only because my copy had no `design/design-system` (`floatingTextTones.test.ts` and `modules.test.ts` read files there). After I added that folder, all of them passed.
  - Not run by me: the Playwright e2e suite (`e2e/*.spec.ts`), the graph and tree algorithm unit tests, `tsc -b`, `vite build`. If a test is named below and not in the lists above, all I know is that it exists.
  - Side effect to know about: to run vitest on the copy I linked it to the repository's installed `node_modules` (a Windows junction under `%TEMP%`) and pointed Vite's `cacheDir` to `%TEMP%`. When Vite loads a config file it may write a short-lived bundled copy into the nearest `node_modules/.vite-temp/` and delete it after loading, so my run may have done that inside the repository's git-ignored `node_modules/.vite-temp/`. That folder existed before (its parent has not changed since 2026-10-23) and it is empty now; its time stamp, 22:51, is later than my runs. I removed the junction afterwards; the installed packages are untouched (INFERENCE, from the time stamps).

## 1. The picture in one paragraph

VERIFIED: the app is **one Vite + React 19 single-page app** in `prototypes/`. Its only entry is `src/main.tsx`. `src/site` routes `/`, `/:slug` and `/:slug/:algorithm`. Three visualizers (`src/graph`, `src/tree`, `src/sorting`) are mounted as routes by `src/site/ModulePage.tsx`. `src/shared` holds what they share, mainly the panel-groups shell. A run is a precomputed list of steps for graph and tree, and a lazily pulled stream of operations for sorting. Graph and tree draw with React Flow (`@xyflow/react`). Sorting draws on a Canvas 2D. Nothing calls the network: `fetch`, XHR and WebSocket appear nowhere in `src`. All state lives in React and in `localStorage`. The design system comes in through the `@ds` alias (`vite.config.ts`, pointing at `../design/design-system`). The site uses its components; the visualizers use only its CSS tokens. VERIFIED: nothing in `src`, `vite.config.ts` or `package.json` mentions `wasm-arch` (Kerk's engine prototype); it is a separate project, as `prototypes/AGENTS.md` says (DOCUMENTED).

## 2. Folder map

VERIFIED (`git ls-tree -r 662e7b3 prototypes`: 1,066 tracked files). The repository root `package.json` sets up npm workspaces with `["prototypes"]` and `node >=22.12`. The dev server port, 5186, is `config.port` in `prototypes/package.json`, and `VA_PORT` overrides it.

```text
visualgo-plus-design/
├─ package.json            npm workspaces root; scripts forward to prototypes/
├─ design/design-system/   tokens, components, assets (imported as @ds)
├─ wasm-arch/              Kerk's engine prototype; not imported by the app
└─ prototypes/             THE app
   ├─ index.html, vite.config.ts (@ds alias, React dedupe, port), playwright.config.ts
   ├─ scripts/   sync-assets.mjs (DS assets → public/ds), static-fallback.mjs (404.html for deep links)
   ├─ e2e/       14 Playwright specs + 5 helpers, against the site's routes
   ├─ docs/      graph | tree | sorting: ARCHITECTURE, DESIGN_DECISIONS (DD-/TP-/SP-), AGENTS (records)
   └─ src/
      ├─ main.tsx, index.css   the only entry (loads @ds/styles.css, React Flow's css)
      ├─ site/       12 files + art/: routes, module catalogue, bar, settings, theme
      ├─ shared/     app/ components/{layout,canvas,chrome,panels,workspace} visualization/ styles/
      ├─ graph/      313 files: app/ algorithms/ components/ editor/ graph/ styles/ visualization/
      ├─ tree/       523 files: app/ algorithms/ components/ editor/ heap/ samples/ segment/
      │              styles/ tree/ trie/ visualization/
      └─ sorting/    94 files: algorithms/ animation/ app/ comparison/ components/ engine/
                     input/ styles/ types/ visualization/
```

| Folder | What it holds | Evidence |
| --- | --- | --- |
| `src/site` | `App.tsx` (router, theme owner), `modules.ts` (30 cards), `ModulePage.tsx`, `HostedModule.tsx`, `ModuleBar.tsx`, `SettingsMenu.tsx`, `HomePage.tsx`, `useTheme.ts` | VERIFIED |
| `src/shared/components/layout` | The groups shell: `groupsModel.ts` (1,441 lines), `dropTargets.ts`, `useGroups.ts`, `useGroupDrag.ts`, `GroupsLayout.tsx` (639), `GroupView.tsx`, `TabMenu.tsx`, `Splitter.tsx` | VERIFIED |
| `src/shared/components/canvas` | `CanvasLegend.tsx`, `VisualizationLegend.tsx`, `compactLegend.ts`, `FloatingText.tsx`, `StepNoteLayer.tsx` | VERIFIED |
| `src/shared/visualization` | `playbackCountdown.ts`, `useStepArrival.ts`, `stepNotes.ts`, `stepNotePlacement.ts`, `floatingText.ts`, `floatingTextTiming.ts`, `legend.ts`, `headline.ts` | VERIFIED |
| `src/shared/app` | `storage.ts` (localStorage that never throws), `themes.ts`, `useTheme.ts` (reader), `usePausedMotion.ts`, `useLayoutFit.ts`, `usePointerActivation.ts` | VERIFIED |
| `src/shared/styles` | 15 sheets (and 2 tests), among them `groups.css`, `editor.css`, `controls.css`, `panels.css`, `footer-bar.css`, `step-notes.css`, `canvas-legend.css` | VERIFIED |
| `src/<viz>/app` | The page: composition, page UI state, keyboard, host-bar parts, layout glue | VERIFIED |
| `src/<viz>/algorithms` | Engines (they build the sequence), presenters, pace, headline, pseudocode, step notes | VERIFIED |
| `src/<viz>/visualization` | Session model: reducer, hook, pace (graph, tree). Sorting: Canvas 2D drawing | VERIFIED |
| `src/<viz>/components` | Footer, panels, inspectors, canvas components | VERIFIED |

## 3. Diagram A · from a URL to the panels and the canvas

VERIFIED: every box below is a component or hook I read.

```text
URL  /  |  /:slug  |  /:slug/:algorithm
 │  src/main.tsx  → @ds/styles.css, @xyflow/react/dist/style.css, index.css
 ▼
site/App.tsx ── ThemeContext (site/useTheme.ts: the ONLY writer of html[data-theme])
 └─ BrowserRouter
    ├─ "/"        → HomePage (cards from modules.ts; DS LessonCard, TextInput, BottomBar)
    ├─ "/:slug[/:algorithm]" → ModuleRoute: unknown or 'soon' card → "/";
    │                          former id → current id; unknown algorithm → "/:slug"
    │   └─ ModulePage (switch module.visualizer, key = slug)
    │       └─ HostedModule ── HostChromeContext { renderTopBar(parts) → ModuleBar }
    │           └─ GraphApp | TreeApp | SortingApp  (initialAlgorithm, initialAction)
    └─ "*"        → "/"

A visualizer page  (graph: App composes it all; tree, sorting: App → … → VizPage)
 ├─ top bar  = renderTopBar(parts) → site ModuleBar: HOME, the card's algorithms,
 │             [1|2|4 panes for sorting], Full screen, Shortcuts,
 │             Settings (themes + "Animate paused steps" + layout items)
 ├─ GroupsLayout (src/shared/components/layout)
 │    ├─ left column ─┐
 │    ├─ right column ├─ GroupView per group: tab strip + every tab's panel mounted,
 │    ├─ bottom row  ─┘    the front one shown; renderPanel(id) → Action | e-Lecture
 │    │                    | Pseudocode | Status | extra:ancestor-table (tree, LCA)
 │    └─ .groups__drawing → the canvas element, passed in once
 ├─ FooterBar  (the visualizer's own: scrubber, speed, transport;
 │             "the footer is the only transport", AGENTS.md)
 └─ ShortcutsDialog
```

## 4. The site layer (`src/site`)

| Claim | Evidence |
| --- | --- |
| Routes are `/`, `/:slug`, `/:slug/:algorithm` and `*` → `/`. `BrowserRouter` uses `import.meta.env.BASE_URL` as its basename (`site/App.tsx:62-70`). | VERIFIED |
| `ModuleRoute` sends a slug that is unknown or not playable back to `/`. It redirects a former algorithm id (`formerIds`) to the current id, and drops an algorithm segment the card does not have (`site/App.tsx:20-55`). | VERIFIED |
| `modules.ts` has 30 cards: 8 `full`, 4 `partial`, 18 `soon` (made by the `soon()` helper; they do not open). `algorithms` lists what visualgo.net offers; `have` lists what is implemented. | VERIFIED |
| `initialAlgorithmFor` opens a card on the algorithm in the URL. Otherwise it opens on the card's first algorithm, unless the card `ownsVisualizer`. Only `graph-editor` and `sorting` own one. | VERIFIED |
| `ModulePage` imports all three Apps statically: there is no code splitting at the route level. Editor cards (`kind: 'editor'`) pass `initialAction = 'draw'`. Each module is keyed by slug (`site/ModulePage.tsx`). | VERIFIED |
| `HostedModule` gives each App a `HostChromeContext` whose `renderTopBar` draws the site's `ModuleBar`. Full screen and Shortcuts sit beside Settings, and the visualizer's `motionMenu` and `layoutMenu` go inside Settings (`site/HostedModule.tsx:60-117`). | VERIFIED |
| Theme: 9 themes. `light` is written as no attribute. The site writes `html[data-theme]` and saves the theme under `visualgo-web:sorting-visualizer-groups:theme`. The prefix is imported from `sorting/app/usePageLayout.ts` (`site/useTheme.ts:3,45,61-77`). | VERIFIED |
| The visualizers only read the theme. `shared/app/useTheme.ts` takes no arguments and follows the attribute with a `MutationObserver`. The graph does not read the theme in JavaScript at all (it uses CSS tokens only). The tree passes React Flow's `colorMode`. Sorting's `useSortPalette` watches the attribute itself so it can repaint the canvas. | VERIFIED |
| The site uses the design system's React components (`TopBar`, `BottomBar`, `LessonCard`, `TextInput`, `Overlay`). No visualizer imports a `@ds` component. | VERIFIED |
| The theme list is written twice: `site/useTheme.ts` `THEMES` and `shared/app/themes.ts` `THEMES` (same 9 ids). I found no test that ties the two lists together. | VERIFIED (lists); INFERENCE (no tie test) |

## 5. The shared layer (`src/shared`)

### 5.1 The groups shell (wireframe V10, "Panel groups")

| Piece | What it does | Evidence |
| --- | --- | --- |
| `groupsModel.ts` | A pure model. `LayoutState = { v: 1, nextGroupId, left, right, bottom }`; a region is `{ size, groups[], collapsed? }`; a group is `{ id, tabs[], active, size, collapsed? }`. Operations: `moveTab`, `pressTab`, `revealTab`, `setGroupCollapsed`, `offerExtraPanel`, `presentLayout`, `resizeRegionFromSplitter`, `resizeGroupFromSplitter`, `resetLayout`, `serializeLayout`, `parseLayout`. `resolveLayout` turns stored sizes into pixels; `dropTransition` and `canDrop` judge a drop. | VERIFIED (exports) |
| Defaults | `DEFAULT_LAYOUT`: Action + e-Lecture in one group on the left; Pseudocode above Status on the right; the bottom row empty. `DEFAULT_MIN_DRAWING` is 360 × 320; groups are at least 240 px wide; the strip is 31 px high; a splitter is 7 px. | VERIFIED |
| `panelRegistry.ts` | `PANEL_IDS = ['action','electure','pseudocode','status']`, their titles, and extra panels typed `` `extra:${string}` `` | VERIFIED |
| `useGroups.ts` | `useGroups(storageKey, reveal?, extraPanelIds?, fallback?)` holds the state. It loads with `parseLayout(readStorage(key))`, saves with `writeStorage(key, serializeLayout(state))`, and exposes move, press, collapse, resize, reset, offer and reveal. A host's reveal and an offered extra panel are not saved on their own; a real change by the visitor is. | VERIFIED (load/save calls); DOCUMENTED (save policy, from its comment and DD-34/DD-55) |
| `useGroupDrag.ts` | The tab drag. It starts after 6 px (`DRAG_THRESHOLD_PX`), listens on window pointer events, Escape cancels, and a release over a target calls `onDrop`. | VERIFIED |
| `dropTargets.ts` | The geometry of the targets, measured on the page: strip slots, group bands, edge bands | VERIFIED (file); DOCUMENTED (exact rules) |
| `GroupsLayout.tsx` | Measures its box with a `ResizeObserver`. It calls `presentLayout` then `resolveLayout` on every render, and draws the regions, the splitters, the drag preview, the `TabMenu`, and the canvas once inside `.groups__drawing`. | VERIFIED |
| `GroupView.tsx` | One group: a `role="tablist"` strip, then a body that mounts **every** tab's panel in its own `.group__scroll` (`data-panel-body`) and hides all but the active one. A panel therefore keeps its scroll and inputs behind another tab. | VERIFIED |
| `Splitter.tsx` | `role="separator"`, resized by pointer or arrow keys. The keys it handles stop there (`stopPropagation`). | VERIFIED |
| Users | All three visualizers import `GroupsLayout` and `useGroups` from here (`graph/app/App.tsx:31-33`, `tree/app/PageLayout.tsx:3`, `tree/app/usePageLayout.ts:1`, `sorting/app/PageLayout.tsx:3`, `sorting/app/usePageLayout.ts:15`). | VERIFIED |
| Origin | `groupsModel.ts` and `dropTargets.ts` first came in `72450e1`, and `GroupsLayout`, the tab menu and the drag overlay in `a876206`. Both are by BJoozz on 2026-10-17 and carry `Co-Authored-By: Claude Fable 5.1`. Kerk's `0394b64` (2026-10-18, `Co-Authored-By: Claude Opus 5.5`) moved them into `src/shared` (the file is a 100% rename). | VERIFIED (log, rename status) |

### 5.2 Other shared pieces

| Piece | Used by | What it is | Evidence |
| --- | --- | --- | --- |
| `visualization/playbackCountdown.ts` `continuePlaybackCountdown` | graph and tree `useVisualizationSession` | The time left of a step's delay, counted from when the session reached the step, so changing Speed mid-step keeps the time already spent. Added in `9baa117` (BJoozz, 2026-10-30, `Co-Authored-By: Claude Fable 5.1`). | VERIFIED |
| `visualization/useStepArrival.ts` | graph `App`, 15 tree run hooks (`src/tree/editor/use*Visualization.ts`, `useHeapRunView.ts`) | `{ forward, playing, effectiveIntervalMs }`. `forward` is true only when the step is one past the last in the same sequence. It updates its state during render. | VERIFIED |
| `visualization/stepNotes.ts` | graph (Dijkstra), tree (LCA, BST, AVL, heap) | The step-note writer: `writeStepNotes`, `createStepNoteWriter`, `NO_STEP_NOTES`; `StepNotes = { nodeNotes, canvasNotes }` | VERIFIED |
| `visualization/stepNotePlacement.ts` `placeStepNotes` | graph and tree note layers | Pure placement on screen. Options `keepToOwnNode` and `clearAtPop` (the graph asks for both); 20 px rise; 1.04 pop scale | VERIFIED |
| `components/canvas/StepNoteLayer.tsx` | `GraphCanvas`, tree `StepNoteLayer` wrapper | Generic over the drawn node type; mounted inside `<ReactFlow>` | VERIFIED |
| `FloatingText.tsx`, `floatingText.ts`, `floatingTextTiming.ts` | tree value popups and every note | Tones `gain`/`loss` draw a number; `accept`/`reject`/`note` draw text. 800 ms for a number, 1,600 ms for a note, never under 200 ms. | VERIFIED |
| `CanvasLegend.tsx`, `VisualizationLegend.tsx`, `legend.ts`, `compactLegend.ts` | graph (`App.tsx:528`, definition from `algorithmLegend.ts`), tree (LCA only) | The legend that floats on the canvas. It turns compact when the canvas is under 700 px wide or 221 px tall. | VERIFIED |
| `app/usePausedMotion.ts` + `chrome/PausedMotionMenuItem.tsx` | graph, tree | "Animate paused steps", saved as `visualgo.pausedMotion`. Until the visitor chooses, it follows `prefers-reduced-motion`. | VERIFIED |
| `chrome/Dialog.tsx`, `chrome/TransportIcon.tsx` | all three | The dialog and the transport glyphs | VERIFIED |
| `components/workspace/RunHeader.tsx`, `visualization/headline.ts` | graph and tree Status panels | The run header above an inspector. Both files are byte-identical to graph-visualizer-v2@`c8b14e6`. | VERIFIED (blob hash) |
| `components/panels/EditorSummary.tsx`, `styles/editor.css` | graph `GraphEditorControls` and `GraphTextEditor`; 5 tree editors | One editor layout in every module, the graph's. Added in `c59c155` (Kerk, 2026-10-18, `Co-Authored-By: Claude Opus 5.5`) and not changed since. | VERIFIED |
| `app/storage.ts` | `useGroups`, `usePausedMotion`, sorting experiment | `readStorage`, `writeStorage` and `removeStorage`, which swallow storage errors | VERIFIED |

## 6. Graph visualizer (`src/graph`)

**Composition.** VERIFIED: `graph/app/App.tsx` (623 lines) builds the whole page itself, with no `VizPage`. It calls `usePageUi`, `useHostChrome`, `usePausedMotion`, `useGroups('graph-visualizer-groups.layout', reveal)`, `useVisualizationSession(getAlgorithmStepPlaybackPace)`, `useGraphEditor`, `useGraphTextEditor`, `useResizeRefit`, `useLayoutFit`, `useAlgorithmConfiguration` and `useStepArrival`. It renders `renderTopBar?.(parts)`, then `GroupsLayout` (`minDrawing` 360 × 320) with `PagePanel` as `renderPanel`, then `FooterBar` and `ShortcutsDialog`. With no host there is no top bar (`App.tsx:570-596`). Paths in the table below are relative to `src/graph`.

| Layer | How it works | Evidence |
| --- | --- | --- |
| Session model | `visualization/sessionReducer.ts`: the session is `idle`, or `{ status: paused/playing/finished, sessionId, sourceTopologyRevision, sequence, stepIndex }`. Actions: `run`, `previous`, `next`, `seek`, `play`, `pause`, `reset`, `tick` (ignored unless it carries the same `sessionId`), `invalidate`, `topology-changed` (goes idle only when the revision differs), `set-interval`. The base interval is 50 to 1,000 ms, 500 by default. This file is byte-identical to graph-visualizer-v2@`c8b14e6`. | VERIFIED |
| Hook and timer | `useVisualizationSession.run(revision, factory)` builds the sequence, checks `runId === sessionId` and that it has at least one step, then dispatches `run`; an error becomes `runError`. One `setTimeout` per (session, `effectiveIntervalMs`) dispatches `tick` after `continuePlaybackCountdown(...).remainingMs`. | VERIFIED |
| Paces | `playbackTiming.ts`: 7 paces with multipliers very-fast 0.4, fast 0.7, normal 1, slow 1.5, emphasis 2, long 3, very-long 5. `effectiveIntervalMs = clamp(round(base × multiplier), 50, 5000)`. Each algorithm's `playbackTiming.ts` maps a step's phase to a pace; for BFS, `inspect-edge` is very-fast and `visit` is slow. | VERIFIED |
| Speed | `components/chrome/playbackSpeed.ts`: the slider is the inverted base interval, in 50 ms steps | VERIFIED |
| Engines | **Eager.** `createAlgorithmVisualizationSequence(request, runId)` switches over 11 ids (`bfs`, `dfs-recursive`, `dfs-stack`, `topological-sort`, `bipartite-check`, `cut-vertex-bridge`, `dijkstra`, `bellman-ford`, `maximum-flow`, `kruskal`, `prim`). Each returns `{ kind, runId, steps[] }` with every step built at once. There are no generators in `src/graph`. Prim is a "lazy edge-PQ Prim": "lazy" there names the algorithm variant, not lazy step generation. | VERIFIED |
| Step shape | `VisualizationStep = { id, description, metadata }`. The metadata is a union keyed by `phase` and carries the whole state of the step (for BFS: queue, visited, depths, parent edges, `activeCodeLine`). | VERIFIED |
| Per-algorithm folder | `create*Sequence.ts` (engine), `*Presentation.ts`, `playbackTiming.ts`, `headline.ts`, `pseudocode.ts`, `types.ts`. `algorithmIntegration.ts` dispatches each of them by `sequence.kind`. | VERIFIED |
| Run request | `resolveAlgorithmRunRequest` (`algorithmIntegration.ts:302`) builds it from the selected algorithm, `graphView` and the configuration (start/End node, Method). `graphInterpretation.ts` gives some algorithms an undirected view. | VERIFIED (symbols); DOCUMENTED (rules, DD-30/39/45/60) |
| Projection | `createAlgorithmGraphPresentation(sequence, stepIndex, { maximumFlowNetworkView, shortestPathTargetNodeId, withinStepMotion: { animationKey: runId:stepId, effectiveIntervalMs } })` returns a `GraphPresentation` (`nodes`, `edges`, `canonicalEdgeDefaults`, `showCanonicalEdges`, `virtualEdges`). `toReactFlowElements(graphView, layout, presentation, selection)` turns it into React Flow nodes and edges (`App.tsx:260-300`). | VERIFIED |
| Step notes | `createAlgorithmStepNotes(sequence, stepIndex, stepArrival)`: only Dijkstra writes notes; the other ten return `NO_STEP_NOTES`. | VERIFIED |
| Canvas | `components/graph/GraphCanvas.tsx`: `<ReactFlow>` with `nodeTypes = { graphNode: CsaGraphNode }` and `edgeTypes = { graphEdge: CenteredGraphEdge }`, an overlay `<Panel position="top-right">` for the legend, `StepNoteLayer`, and `PausedStepContext`. A fit is asked for by bumping the `fitViewRequest` counter. The layout uses `d3-force` (`graph/layout/forceLayout.ts`). | VERIFIED |
| Editor | `editor/useGraphEditor.ts` owns `GraphDocument` (with `topologyRevision`), `GraphLayout` and the selection. A topology change calls `visualization.handleTopologyChange(revision)`. Text editing is `useGraphTextEditor` over `graph/text/*`. | VERIFIED |
| Panels | `app/PagePanel.tsx` switches on the panel id: `ActionPanel` (`AlgorithmRunForm`, the picker, Draw graph), `ELecturePanel` (`electureSlides.ts`, static data), `PseudocodePanel` (`algorithmPseudocode.ts`), `StatusPanel` (`AlgorithmVisualizationInspector` with `RunHeader` and a typed inspector per algorithm). | VERIFIED (files and switch) |
| Saved | Only `graph-visualizer-groups.layout`. The graph itself is not saved; its working copies last for the visit (`graphWorkingCopies.ts`). | VERIFIED (no storage calls in `src/graph`); DOCUMENTED (DD-41) |

## 7. Tree visualizer (`src/tree`)

**Composition.** VERIFIED: `tree/app/App.tsx` (105 lines) holds `selection = { algorithmId, visited: WorkspaceMode[] }`. It maps the 7 algorithm ids (`lca-binary-lifting`, `bst`, `avl`, `binary-heap`, `trie`, `segment-tree`, `segment-tree-lazy`) to 5 modes (`tree`, `heap`, `trie`, `segment`, `segment-lazy-propagation`) in `workspaceModes.ts`. Each mode is a dynamic `import()`. App renders one `LazyWorkspace` per mode visited so far: `React.lazy` with `Suspense`, an error boundary and a Retry button. A mode that is not active keeps its hooks (and so its state) and renders `null` (for example `HeapMode.tsx:229`). App provides `PageChromeContext` (`theme`, `colorMode`, `pausedMotion`, `layout`, `ui`, `hostBar`) and draws the host's bar once, above every frame, from a `hostBar` store that the active `VizPage` fills in a layout effect. Paths in the table below are relative to `src/tree`.

```text
App ─ PageChromeContext, HostBar(store)
 └─ LazyWorkspace × visited mode
     └─ TreeMode | HeapMode | TrieMode | SegmentMode | SegmentTreeLazyMode
         owns: editor hook, one session hook per operation, the selected operation
         └─ ModePage (builds the four panels from props)
             └─ VizPage (frame: PageLayout → GroupsLayout, FooterBar, shortcuts, bar parts)
```

| Layer | How it works | Evidence |
| --- | --- | --- |
| Session model | `visualization/sessionReducer.ts`: the same lifecycle as the graph's, but generic over the sequence type, with `sourceContextKey` and a `context-changed` action in place of the topology revision. It is byte-identical to tree-visualizer@`46ce0a7`. `playbackTiming.ts` is identical to upstream and has the same 7 paces and multipliers as the graph's (only a doc comment differs). | VERIFIED |
| Hooks | `visualization/useVisualizationSession.ts` uses the shared countdown. `editor/useContextualVisualizationSession.ts` binds a run to a context key, such as `createBstInsertSourceContextKey(document, rootId, value)`. Each operation has its own hook (`useBstInsertVisualization`, `useAvlDeleteVisualization`, `useHeapRunView`, `useSegmentVisualization`, `useBinaryLiftingVisualization`, ...). BST Insert's hook, for example, returns `sequence`, `stepIndex`, `overlay`, `stepNotes`, `viewProjection`, `committableProjection`, `run`, the transport functions and `runError`. | VERIFIED (BST Insert hook read at `useBstInsertVisualization.ts:1-20, 105-190`; the others by grep) |
| Engines | **Eager.** `algorithms/algorithmIntegration.ts` `createTreeAlgorithmSequence(request, runId)`, with one overload per operation. The heap, segment and trie have their own integration files. There are no generators in `src/tree`. | VERIFIED |
| Step shape | `{ id, description, metadata, viewProjection? }`. The metadata has `phase`, `activeCodeLine`, ids of visited nodes and edges, the comparison and the result. A structural step can carry the tree as drawn (`TreeViewProjection`). The sequence also carries context, such as BST Insert's `resultProjection`. | VERIFIED (`bst/bstInsertTypes.ts:32-70`) |
| Projection | `createTreeAlgorithmOverlay(sequence, stepIndex)` returns a `TreeAlgorithmOverlay` (node and edge overlays, emphasis, popups, notes). `getTreeViewProjection` is pushed into the editor's view in a layout effect (`visualization/useViewProjectionSync.ts`). After an Insert or Delete, `getCommittableTreeViewProjection` lets `editor.commitViewProjection` keep the result. `TreeMode` calls `toReactFlowElements(viewDocument, viewRootId, treeLayout, presentation, selection, toggleCollapsed, overlay)` (`TreeMode.tsx:348-365`). The layout is `d3-hierarchy` (`tree/layout/createTreeLayout.ts`). | VERIFIED |
| Canvas | `components/tree/TreeCanvas.tsx`: `<ReactFlow>` with `treeNode: CsaTreeNode` and `treeEdge: StraightTreeEdge`, `colorMode` from the theme, an overlay `<Panel>` (the LCA legend), and `StepNoteLayer`. Array views sit beside it: `HeapDualView`/`HeapArrayView`, `SegmentArrayView`, and `TreeArrayView` with the LCA step strip or the traversal strip. | VERIFIED |
| Panels | `ModePage.tsx` builds `ActionPanel` (`RunForm`, `SampleList`, the edit body), `ELecturePanel` (`electureSlides.ts`, 806 lines of static data), `PseudocodePanel` and `StatusPanel` (an inspector with `RunHeader`). The extra panel `extra:ancestor-table` (`BinaryLiftingTable`) is passed by `TreeMode` only while LCA is selected (`TreeMode.tsx:591-592`), and `PageLayout.tsx` offers it beside Status. `LAYOUT_HOSTS_EXTRA_PANELS` is the constant `true`. | VERIFIED |
| Drawing floor | `drawingFloor.ts`: 320 × 200 for the tree and trie modes; 320 × 240 for heap and both segment trees | VERIFIED |
| Saved | Only `tree-visualizer-groups.layout`. Documents are not saved. | VERIFIED |
| State ownership | The editor hook owns documents, drafts, selection, collapse and projections. The session hooks own runs and parameters. The mode component owns the selected operation and the picker. App's `usePageUi` owns full screen, the open action, dialogs and the slide. Panels hold no state. | DOCUMENTED (tree ARCHITECTURE "State ownership"); VERIFIED for the parts read above |

## 8. Sorting visualizer (`src/sorting`)

**Composition.** VERIFIED: `sorting/app/App.tsx` calls `useSortingExperiment(initialAlgorithm)`, which owns the dataset draft and the committed dataset, `paneCount` (1, 2 or 4), the algorithms of the panes, `hasRun`, `runSerial`, `speed` and `startBlocker`. App mounts **either** `IdleFrame` (no player at all) **or** `RunFrame`, with `key={experiment.runKey}`. `runKey = "${hasRun ? 'run' : 'idle'}:${runSerial}:${paneCount}:${algorithms…}"`, so a start or a restart **remounts** the run frame (`App.tsx:355-360`, `useSortingExperiment.ts:285-295`). `RunFrame` calls `useComparisonPlayer(experiment.input, experiment.runs)` and plays on mount when `playOnStart` is set. Next with no run starts a frame that stays on operation 0. Both frames render `SortingFrame` → `VizPage` → `PageLayout` → `GroupsLayout`. Paths in the table below are relative to `src/sorting`.

| Layer | How it works | Evidence |
| --- | --- | --- |
| Engines | **Lazy.** One generator (`function*`) per algorithm in `algorithms/comparisonSorts.ts` and `nonComparisonSorts.ts`; 8 ids (`bubble`, `selection`, `insertion`, `merge`, `quick`, `randomQuick`, `counting`, `radix`). The type is `SortOperationProducer = Generator<SortOperation, number[], void>`. `createSortOperationProducerFactory(algorithm, input, seed)` returns a fresh producer each time it is called. | VERIFIED |
| Step shape | One `SortOperation` per step: `compare`, `swap`, `write`, `pivot`, `markSorted`, `auxWrite`, `bucketPush`, `bucketCollect` or `phase`. Each has an optional `line` and carried effects (`phaseChange`, `pivotChange`, `auxWrites`; a merge write also carries the `compare` that chose it). `PlaybackState` holds `array`, `operationIndex`, compared/changed/sorted indices, the pivot, auxiliary arrays, radix items and buckets, `phase`, `line`, `metrics` and `status`. | VERIFIED (`types/sort.ts`, `engine/operations.ts:16-31`) |
| Apply and undo | `applySortOperations` (one copy-on-write pass per batch), `revertSortOperation`, `replayOperations` | VERIFIED (exports); DOCUMENTED (copy-on-write) |
| Buffer | `comparison/operationBuffer.ts`. A `BufferedOperationRun` has `future` (look-ahead of 2,048, refilled at 512) and `history`, which is never trimmed. `readBufferedOperations(run, tick, count)` slices history and pulls from the generator only past its end. The buffers hang off the `runs` array in a module-level `WeakMap`, so that array's identity matters. | VERIFIED |
| Eager gate | `EAGER_OPERATION_CAP = 60_000`. `primeEagerOperationRuns` runs in the player's `useState` initialiser. It pulls the panes round robin, one chunk of 2,048 at a time, until every producer has finished or the total held reaches 60,000. If it reaches the cap it keeps what it pulled. When the whole run fits, the scrubber spans the real run from the first frame. | VERIFIED (`operationBuffer.ts:246-330`) |
| Model | `comparison/comparisonPlayback.ts`: `ComparisonPlaybackModel = { tick, status, panes[{ id, state, transition, generationError }] }`, with `advanceComparisonBatch`, `retreatComparison`, `seekComparison`, `playComparison`, `pauseComparison` and `resetComparison` | VERIFIED |
| Clock | `useComparisonPlayer`: a `requestAnimationFrame` scheduler (`createPlaybackFrameScheduler`). Speed is operations per second on 15 rungs (1 to 6,400; default 12). `resolvePlaybackBatchPolicy(speed, n, activePaneCount)` decides how many ticks a frame advances. It returns `seekableRange = replayableOperationRange(runs)` and `rangeIsFinal`. | VERIFIED |
| Canvas | `visualization/SortCanvas.tsx`: Canvas 2D (`getContext("2d")`, device pixel ratio capped at 2). It draws `drawBars`, `drawCountingScene` or `drawRadixScene`; transitions use `d3-interpolate` and `d3-ease`. `SortPaneGrid` shows 1, 2 or 4 panes; `SortSetupStrip` appears only in Compare. | VERIFIED |
| Panels | Study (1 pane): `SortActionPanel`, `ELecturePanel` (`sortingElectureSlides.ts`), `PseudocodePanel` (`hasRun` prop), `SortStatusPanel`. Compare (2 or 4 panes, `isCompareMode`): `AVAILABLE_PANELS.compare = ['status']`, and that tab holds `SortCompareStatus` because `COMPARE_METRICS = 'header'`. The algorithm nav in the bar is empty in Compare (`VizPage.tsx:259`). | VERIFIED |
| Layout | `usePageLayout(mode)` runs two `useGroups`: `sorting-visualizer-groups.layout.study` and `.layout.compare` (`COMPARE_LAYOUT`). `showPanels` shows only the mode's panels. | VERIFIED |
| Saved | `sorting-visualizer-groups.experiment` = `{ draft: committed, paneCount, algorithms }` (`useSortingExperiment.ts:153, 252-256`), plus the two layout keys | VERIFIED |
| Dead code | `engine/useSortPlayer.ts` is byte-identical to upstream and imported by nothing | VERIFIED |
| Own copy | `app/useLayoutFit.ts` differs from `shared/app/useLayoutFit.ts` only in a comment, and sorting imports its own copy | VERIFIED |

## 9. Diagram B · a run's data flow, from Play to the canvas (graph and tree)

VERIFIED: each arrow is a call or a prop I read (`graph/app/App.tsx:255-432`, `tree/app/VizPage.tsx:140-160`, both `useVisualizationSession.ts`, `tree/editor/useBstInsertVisualization.ts`).

```text
FooterBar  Autoplay ─► togglePlayback()          graph: App.tsx    tree: VizPage.tsx
              │ no session?            yes ─► pause() / play()
              ▼
   graph: runVisualization(play)   tree: startRun(play) → start.run() of the active operation
              │ visualization.run(revision | contextKey, runId => create…Sequence(request, runId))
              ▼
   useVisualizationSession.run      builds ALL steps now (eager); checks runId and ≥ 1 step
              │ dispatch {type:'run'} → { status:'paused', stepIndex: 0, sequence }
              │ then play() in the same batch   (Next with no run: stays paused on step 0)
              ▼
   session ◄── setTimeout(remainingMs) → dispatch {type:'tick', sessionId}
              │   remainingMs = continuePlaybackCountdown(prev, session, effectiveIntervalMs, now)
              │   effectiveIntervalMs = resolvePlaybackDelayMs(intervalMs, pace(sequence, stepIndex))
              ▼
   graph: createAlgorithmGraphPresentation(seq, i, opts) ─► GraphPresentation
          toReactFlowElements(graphView, layout, presentation, selection) ─► nodes, edges
   tree : createTreeAlgorithmOverlay(seq, i) + the step's viewProjection ─► editor view
          toReactFlowElements(viewDocument, root, layout, presentation, …, overlay)
              ▼
   GraphCanvas / TreeCanvas  (<ReactFlow>, overlay <Panel> with CanvasLegend, StepNoteLayer)
   useStepArrival(seq, i, playing, effectiveIntervalMs) ─► notes only on a step one forward
   The same session feeds Pseudocode (activeCodeLine via sequence.kind) and Status (RunHeader + inspector)
```

INFERENCE: a run is an immutable value. The session is the single source of "where are we", and the presentation is a pure function of (sequence, stepIndex, options). The canvas does not drive the session directly. An edit changes the document instead: in the graph a topology change ends the run (`topology-changed`); in the tree a context change does (`context-changed`). Graph DD-24 and the AGENTS.md rule "sequences are created only by the footer's start actions" say the same (DOCUMENTED).

## 10. Diagram C · the sorting Compare clock

VERIFIED (`useComparisonPlayer.ts`, `operationBuffer.ts`, `comparisonPlayback.ts`, `playbackBatching.ts`).

```text
useSortingExperiment ─ runs[] (its identity keys the WeakMap of buffers)
        │                                    RunFrame key=runKey  (a restart remounts it)
        ▼                                         │
 per pane: createSortOperationProducerFactory(algo, input, seed) → function* generator
           BufferedOperationRun  future ≤ 2,048 (refill at 512) ─► history (never trimmed)
 at mount: primeEagerOperationRuns: round robin, chunks of 2,048, until done or Σ = 60,000
        ▼
 clock:    requestAnimationFrame ─► resolvePlaybackBatchPolicy(speed ops/s, n, activePanes)
           ─► advanceComparisonBatch(model, k): model.tick += k   (ONE tick for every pane)
 per pane: state.operationIndex = min(tick, that pane's total)  → a finished pane sits still
 scrubber: 0 … replayableOperationRange(runs)
           = shortest history among panes that can still produce,
             or the longest history once none can   → a seek never runs a generator
 seek:     back → replayOperations(input, history[0..target]) per pane (exact past);
           forward → a silent advanceComparisonBatch   (comparisonPlayback.ts:326-376)
 Last:     fillOperationRuns(all) → seek(longest history)
```

The test `seekComparison.test.ts:68` "seeking equals repeated stepping" exists and passed in my run, as did `eagerPriming.test.ts`, which checks `replayableOperationRange`. VERIFIED.

## 11. Diagram D · the shared layer's boundaries

VERIFIED: I counted the direct importers of every file in `src/shared` (tests left out) with grep.

```text
 ┌───────────────────────────────── src/site ─────────────────────────────────┐
 │ router · modules.ts · ModuleBar · SettingsMenu · the theme WRITER          │
 │ @ds React components (TopBar, LessonCard, BottomBar, TextInput, Overlay)   │
 └───────┬───── static imports ────────┬─────────────────────────────┬────────┘
         │ renderTopBar(parts)         │                             │
 ┌───────▼────────┐            ┌───────▼────────┐            ┌───────▼────────┐
 │ src/graph      │            │ src/tree       │            │ src/sorting    │
 │ App composes   │            │ App→Lazy→Mode  │            │ App→Idle|Run   │
 │ session DD-17  │            │ →ModePage→Viz  │            │ →Frame→VizPage │
 │ eager engines  │            │ eager engines  │            │ lazy generators│
 │ React Flow     │            │ React Flow     │            │ Canvas 2D      │
 └───────┬────────┘            └───────┬────────┘            └───────┬────────┘
         │ imports                     │                             │
 ┌───────▼─────────────────────────────▼───── src/shared ────────────▼────────┐
 │ all three   : layout/ (GroupsLayout, useGroups, groupsModel),              │
 │               panels/panelRegistry, chrome/Dialog, TransportIcon,          │
 │               app/storage (through useGroups), styles controls | panels |  │
 │               footer-bar | pseudocode-panel | menu.css                     │
 │ graph + tree: playbackCountdown, useStepArrival, stepNotes, placement,     │
 │               StepNoteLayer (FloatingText inside it), CanvasLegend,        │
 │               compactLegend, usePausedMotion + menu item, useLayoutFit     │
 │               (sorting keeps a copy), RunHeader, headline, EditorSummary,  │
 │               styles/editor.css                                            │
 │ tree+sorting: app/useTheme (the reader), app/themes, usePointerActivation  │
 │ tree only   : FloatingText as value popups, workspace-loading.css,         │
 │               operation-selector.css, legend-swatches.css                  │
 │ graph only  : visualization-legend.css (direct import)                     │
 └────────────────────────────────────────────────────────────────────────────┘
```

### 11.1 What is shared and what each visualizer keeps

| Concern | Shared (one copy) | Per visualizer | Evidence |
| --- | --- | --- | --- |
| Page shell | Groups model, layout, drag, tab menu, splitters, `groups.css` | Composition (graph `App`; tree and sorting `VizPage` + `PageLayout` + `usePageLayout`), floor sizes, storage prefix | VERIFIED |
| Top bar | Drawn by the site (`ModuleBar`) | The parts each page hands over (`hostChrome.ts` per visualizer) | VERIFIED |
| Theme | The site writes it; `shared/app/useTheme.ts` reads it | How each canvas uses it (graph: tokens only; tree: `colorMode`; sorting: `useSortPalette`) | VERIFIED |
| Session and timer | `continuePlaybackCountdown` (graph and tree only) | Reducer and hook: graph (topology revision) and tree (generic, context key); sorting `useComparisonPlayer` (animation frames) | VERIFIED |
| Engines, presenters, pseudocode, e-Lecture text, inspectors | none | all per visualizer | VERIFIED |
| Canvas overlays | Legend, step-note layer and placement, floating text | Anchors and obstacles (graph `stepNoteAnchor.ts`, tree `components/tree/stepNotePlacement.ts`) | VERIFIED (files); DOCUMENTED (rules) |
| Footer | `footer-bar.css`, `TransportIcon` | `FooterBar.tsx` per visualizer: graph's and tree's are byte-identical; sorting's counts operations | VERIFIED |

### 11.2 Byte-identical copies outside `src/shared`

VERIFIED by `git hash-object` over every file in `src/{graph,tree,sorting,shared,site}`:

| Same bytes | Files |
| --- | --- |
| graph = tree | `components/chrome/FooterBar.tsx`, `components/chrome/playbackSpeed.ts` |
| graph = tree = sorting | `components/chrome/ShortcutsDialog.tsx`, `components/panels/pseudocodeHighlight.ts` |
| tree = sorting | `app/usePageShortcuts.ts`, `app/keyboardShortcuts.test.ts` |
| differ only in comments | `graph/visualization/playbackTiming.ts` vs `tree/…`; `shared/app/useLayoutFit.ts` vs `sorting/app/useLayoutFit.ts` |

`prototypes/AGENTS.md` says: "A file in a visualizer's folder is that visualizer's own; before copying one into another visualizer, move it to `src/shared` instead." (DOCUMENTED). INFERENCE: the copies above are older than that rule or were left on purpose. QUESTION for Bao: should the report call them known duplication (the sorting doc lists the footer back-port as item 1 of its backlog), or are they meant to stay?

## 12. Persistence keys (all `localStorage`; nothing goes to a server)

VERIFIED: I grepped every `readStorage`, `writeStorage` and `localStorage` call in `src`, tests left out.

| Key | Written by | Holds |
| --- | --- | --- |
| `visualgo-web:sorting-visualizer-groups:theme` | `site/useTheme.ts:45,72` | The theme id. The prefix is sorting's `STORAGE_PREFIX`, a name kept from the separate builds (see §15). |
| `visualgo.pausedMotion` | `shared/app/usePausedMotion.ts:11,128` | "Animate paused steps", shared by graph and tree |
| `graph-visualizer-groups.layout` | `useGroups` from `graph/app/App.tsx:74,158` | The graph's group arrangement (`v: 1`) |
| `tree-visualizer-groups.layout` | `useGroups` from `tree/app/usePageLayout.ts:13,22` | The tree's arrangement, keeping the place of `extra:ancestor-table` |
| `sorting-visualizer-groups.layout.study` and `.layout.compare` | `sorting/app/usePageLayout.ts:144-145` | One arrangement per sorting mode |
| `sorting-visualizer-groups.experiment` | `sorting/app/useSortingExperiment.ts:153,252` | The committed dataset draft, the pane count and the pane algorithms |

Not saved (VERIFIED, no other storage calls): graph documents; tree, heap, trie and segment documents; runs, step indices and Speed in all three visualizers (the sorting experiment key holds no speed). Graph and tree samples and working copies last for the visit only (DOCUMENTED: graph DD-41, tree TP-16).

## 13. Inherited from the standalone repositories versus built here

Upstream clones checked (read-only): graph-visualizer-v2 at `c8b14e6` and tree-visualizer at `46ce0a7` (the commits the docs name as the copy points), and sorting-algorithm-visualizer at `9236a65` (one squashed commit, 2026-08-19, BJoozz). VERIFIED with `git log -1` in each clone.

### 13.1 File-level comparison by path (VERIFIED by blob hash)

| Visualizer | Upstream `src` files | Same bytes now | Changed | Gone (or moved) | Files in `prototypes/src/<viz>` now |
| --- | --- | --- | --- | --- | --- |
| graph ← graph-visualizer-v2 | 173 | 53 | 82 | 38 | 313 |
| tree ← tree-visualizer | 289 | 88 | 163 | 38 | 523 |
| sorting ← sorting-algorithm-visualizer | 45 | 17 | 19 | 9 | 94 |

Limits (INFERENCE): this matches by path only, so moves count as "gone" (`dfs/` → `dfsStack/`; `CanvasLegend`, `RunHeader` and `headline` → `src/shared`). "Changed" says nothing about who changed a file or how much. The upstream files that are gone are mostly the old page shells: graph's `GraphWorkspace`, `PlayerDock`, `WorkspaceToolbar`; tree's `TreeWorkspace`, `VisualizationPlayer`, `ModeToolbar`; sorting's `App.tsx`, `PlaybackControls`, `Metrics`. The groups shell replaced them.

### 13.2 What came from where

| Part | Inherited | Built or changed in this repository | Evidence |
| --- | --- | --- | --- |
| Graph session reducer | `visualization/sessionReducer.ts` is byte-identical to graph-visualizer-v2 | `useVisualizationSession.ts` changed: it uses the shared countdown since `9baa117` (2026-10-30) | VERIFIED |
| Tree session reducer and paces | `sessionReducer.ts` and `playbackTiming.ts` are byte-identical to tree-visualizer | `useVisualizationSession.ts` changed; the operation hooks were added | VERIFIED |
| Graph algorithms | Upstream ids: `bfs`, `dfs`, `dijkstra`, `maximum-flow`, `kruskal` | Now 11. `dfs` became `dfs-stack`; added `dfs-recursive` (`4ab075c`, 2026-09-29), `bellman-ford` (`aef5d0b`, 2026-10-03), `prim` (`5428ed3`, 2026-10-04), `topological-sort` (`b88952d`, 2026-10-21), `bipartite-check` (`84c5917`) and `cut-vertex-bridge` (`0fc105c`, both 2026-10-22). All by BJoozz <123baoek31@gmail.com>. | VERIFIED (first-add commits) |
| Tree operations | Upstream: BST Insert, Delete and Search; AVL Insert and inspection; heap Insert and Extract-min; LCA by binary lifting; eager segment tree; trie | Added: AVL Delete (`9a2f04b`) and BST/AVL traversals (`e7f2fec`), both 2026-10-10; Binary Heap Extract K and Heap sort (`3409565`) and Update key and Delete (`1804565`), both 2026-10-20; the lazy segment tree (`fc4172d`, 2026-10-09). All by BJoozz. | VERIFIED (first-add commits) |
| Sorting | Generators, `operations.ts`, the comparison player and buffer, `SortCanvas`, the scene renderers (all from upstream, most changed since). `engine/useSortPlayer.ts` is unchanged and now unused. | The eager gate (`5ccef45`) and `replayableOperationRange` with round-robin priming (`fed2420`), both 2026-09-25, BJoozz, in the earlier sorting prototypes; `useSortingExperiment`, the Idle/Run frames and the Study/Compare layouts | VERIFIED (`git log -S`, `git show --stat`); upstream `operationBuffer.ts` has no such symbols |
| Groups shell | none; the upstream repositories have no tab groups | `72450e1` (model and drop targets) and `a876206` (layout, tab menu, drag overlay, sandbox), BJoozz, 2026-10-17, `Co-Authored-By: Claude Fable 5.1`. Moved to `src/shared` in `0394b64` (Kerk Tai Heng, 2026-10-18). | VERIFIED |
| Site | none | `87db4a3` (V2 site) and `8aeb543` (V7 site), BJoozz, 2026-09-28; `d445364` (groups site), BJoozz, 2026-10-17. Of the 39 commits that touched those site folders, 37 are by BJoozz and 2 by Kerk (`ae63a62`, `0394b64`). | VERIFIED (log) |
| One app | n/a | `0394b64` by Kerk Tai Heng, 2026-10-18 ("Keep V10 only: one app in prototypes/, run from the repository root", `Co-Authored-By: Claude Opus 5.5`): 924 renames, 2,575 deletions, 7 additions, 4 modifications. It deleted the V2/V7 copies, the two other sites and the submodules, put the 40 byte-identical shell files once in `src/shared`, and set up the root npm workspaces. | VERIFIED (`git show --name-status`; message DOCUMENTED) |
| Kerk's later changes to the app | n/a | `c59c155` (2026-10-18): removed the visualizers' own top bars, settings menus and theme writers, so the site draws the only bar and owns the theme. It turned `shared/app/useTheme.ts` from `useTheme(storageKey, owns = true)` into the reader `useTheme(): ThemeId`, deleted the shared `SettingsMenu`, and added `editor.css`, `controls.css` and `EditorSummary.tsx`. `5235fcf` (2026-10-18): the visualizers' Settings items styled as the site's own. `3c79d36` (2026-10-19): no Save image; Full screen and Shortcuts by Settings. `40a63bd` (2026-10-20): tips removed from the landing page. `a074f50` (2026-10-21): Next with no run starts a run paused on its first frame. `01a1a4a` (2026-10-22): Autoplay and Stop as green and red chips. Each carries `Co-Authored-By: Claude Opus 5.5`. | VERIFIED (log, stats); details DOCUMENTED by the messages |
| Floating text, step notes, countdown | none | `ff77eca` (2026-10-13, value popups, `Co-Authored-By: Claude Opus 5.5`); `d82aa18` (2026-10-23; `FloatingText`, `useStepArrival` and timing put into `src/shared`); `08590ef` (2026-10-25; `StepNoteLayer`, placement and writer into `src/shared`); `9baa117` (2026-10-30; `playbackCountdown.ts`). All by BJoozz; the last three carry `Co-Authored-By: Claude Fable 5.1`. | VERIFIED |

Commit tally on `prototypes/src` after the restructure (`0394b64..662e7b3`, merges left out): BJoozz 32 commits (+26,369 / −3,453 lines), Kerk Tai Heng 6 commits (+1,457 / −3,661). VERIFIED as counts. These are counts only, not ownership: line counts include moves and deletions. For the commits named in this section I read the message, the file list, and the part of the diff cited; I did not read every line of them.

AI assistance (VERIFIED as fact, not judged): most commits named here carry a `Co-Authored-By: Claude …` trailer (Opus 5, Opus 5.5 or Fable 5.1). `aef5d0b` (Bellman-Ford) and `5428ed3` (Prim) carry none.

## 14. Main symbols and where they live

| Symbol | File | Role |
| --- | --- | --- |
| `App`, `ModuleRoute` | `src/site/App.tsx` | Router and theme owner |
| `MODULES`, `findModule`, `findAlgorithm`, `findFormerAlgorithm`, `initialAlgorithmFor`, `isPlayable` | `src/site/modules.ts` | The card catalogue and URL rules |
| `ModulePage`, `HostedModule`, `ModuleBar`, `SettingsMenu` | `src/site/*.tsx` | Mount a visualizer and draw its bar |
| `useTheme` (writer), `ThemeContext`, `useSiteTheme` | `src/site/useTheme.ts` | The one theme writer |
| `useTheme` (reader), `THEMES`, `parseTheme` | `src/shared/app/useTheme.ts`, `themes.ts` | Visualizers follow `html[data-theme]` |
| `LayoutState`, `DEFAULT_LAYOUT`, `moveTab`, `resolveLayout`, `dropTransition`, `canDrop`, `parseLayout`, `serializeLayout` | `src/shared/components/layout/groupsModel.ts` | The pure arrangement model |
| `useGroups`, `useGroupDrag`, `GroupsLayout`, `GroupView`, `TabMenu`, `Splitter` | `src/shared/components/layout/` | The shell's state, drag and views |
| `PANEL_IDS`, `PanelId`, `ExtraPanelId`, `TabId` | `src/shared/components/panels/panelRegistry.ts` | Panel ids |
| `continuePlaybackCountdown` | `src/shared/visualization/playbackCountdown.ts` | Step timer that survives a Speed change |
| `useStepArrival`, `writeStepNotes`, `NO_STEP_NOTES`, `placeStepNotes` | `src/shared/visualization/` | How a step arrived; notes and their placement |
| `StepNoteLayer`, `FloatingText`, `CanvasLegend`, `isCompactLegendCanvas` | `src/shared/components/canvas/` | Canvas overlays |
| `usePausedMotion`, `readStorage`, `writeStorage` | `src/shared/app/` | Paused-step motion; safe storage |
| `visualizationSessionReducer`, `useVisualizationSession`, `resolvePlaybackDelayMs` | `src/graph/visualization/`, `src/tree/visualization/` | Session lifecycle and timing (two separate copies) |
| `createAlgorithmVisualizationSequence`, `createAlgorithmGraphPresentation`, `createAlgorithmStepNotes`, `getAlgorithmStepPlaybackPace`, `resolveAlgorithmRunRequest` | `src/graph/algorithms/algorithmIntegration.ts` | Graph dispatch by algorithm |
| `toReactFlowElements` | `src/graph/graph/adapters/`, `src/tree/tree/adapters/` | Presentation to React Flow |
| `GraphCanvas`, `TreeCanvas` | `src/graph/components/graph/`, `src/tree/components/tree/` | React Flow canvases |
| `createTreeAlgorithmSequence`, `createTreeAlgorithmOverlay`, `getTreeViewProjection`, `getCommittableTreeViewProjection` | `src/tree/algorithms/algorithmIntegration.ts` | Tree dispatch |
| `LazyWorkspace`, `getWorkspaceMode`, `VizPage`, `ModePage`, `PageLayout`, `usePageLayout` | `src/tree/app/` | Tree page frame |
| `useSortingExperiment`, `IdleFrame`, `RunFrame`, `runKey` | `src/sorting/app/` | Sorting page state and the mount boundary |
| `createSortOperationProducerFactory`, `*SortOperations` generators | `src/sorting/algorithms/` | Lazy sorting engines |
| `useComparisonPlayer`, `seekComparison`, `advanceComparisonBatch`, `replayableOperationRange`, `primeEagerOperationRuns`, `EAGER_OPERATION_CAP` | `src/sorting/comparison/` | Compare clock and buffers |
| `SortCanvas`, `drawBars`, `drawCountingScene`, `drawRadixScene` | `src/sorting/visualization/` | Canvas 2D drawing |

## 15. Docs versus code: what I found

| # | The docs say | The code at `662e7b3` | Label |
| --- | --- | --- | --- |
| 1 | All three ARCHITECTURE "Hosting" sections: a host owns `html[data-theme]` "and the page follows the attribute instead of writing it (`useTheme` with `owns` false)". Graph's state table: "Theme · `useTheme` · persisted". | `shared/app/useTheme.ts` takes no arguments and never writes. Since `c59c155` the site is the only writer, and the graph does not call any `useTheme`. The docs describe the code before `c59c155`. | VERIFIED (stale doc) |
| 2 | Tree ARCHITECTURE "Where the ancestor table goes" describes two paths, split rails (false) and panel groups (true). | `LAYOUT_HOSTS_EXTRA_PANELS = true` is a constant, and only the groups layout exists. The split-rails path is history. | VERIFIED |
| 3 | Sorting diagram: `SortStatusPanel` "(Study only)"; the text says "Compare shows Status alone". | Both hold: in Compare the Status tab shows `SortCompareStatus` (`COMPARE_METRICS = 'header'`), not `SortStatusPanel`. | VERIFIED |
| 4 | `site/useTheme.ts` comment: the key differs per "build" (split rails, docks, groups). | Only one build is left; the key is `visualgo-web:sorting-visualizer-groups:theme`. It works, but the name is historic. | VERIFIED |
| 5 | Sorting doc: "`seekComparison equals repeated stepping` asserts it". | The test is `describe("seeking equals repeated stepping")` (`seekComparison.test.ts:68`). It passed in my run. | VERIFIED |
| 6 | Tree "Lazy boundaries": the heap, trie and segment engines stay outside the first import, each workspace being a dynamic import; no test guards this. | The 5 dynamic `import()`s exist (`tree/app/App.tsx:17-21`). `site/ModulePage.tsx` imports the graph, tree and sorting Apps statically. I did not build, so chunk sizes are not checked. | VERIFIED (imports); DOCUMENTED (chunks) |
| 7 | `prototypes/AGENTS.md` "One fix, one place". | Six sets of byte-identical files remain in visualizer folders (§11.2). | VERIFIED |

## 16. Questions for Bao

1. QUESTION: both `BJoozz <123baoek31@gmail.com>` and `BJoozz <83776047+BJoozz@users.noreply.github.com>` are treated as you. Please confirm. On `main` the gmail address has 216 commits and the noreply address 30. All 30 noreply commits are "Merge pull request #…" commits made on GitHub, and every BJoozz commit cited in this note used the gmail address. Kerk has 17 commits as `taihengkerk@gmail.com`, plus 4 pull-request merges (#17, #18, #20, #21) as `42596694+kerktaiheng@users.noreply.github.com` (VERIFIED, `git log --format=%ae`). Merges are not evidence of authorship.
2. QUESTION: "the owner" in Kerk's commits of 2026-10-18 to 2026-10-22. Whose choices are these: "The owner's decision of 2026-10-18: V10 wins" (`0394b64`), "the owner's V10 choices 27 to 32" (`ae63a62`), "choices 33 to 41" (`c59c155`, including the shared `editor.css` and `controls.css` look), "choices 42 to 45, 2026-10-19" (`3c79d36`, including Full screen and Shortcuts beside Settings, and no Save image), "The owner's request, 2026-10-20" (`40a63bd`), and "the owner's choice 46" (Next with no run starts a paused run; first written in `a074f50` and touched again in `01a1a4a`; it now appears in `tree/app/VizPage.tsx` and `sorting/app/App.tsx` comments)? Yours, Kerk's, or a joint decision?
3. QUESTION: the report should say how the work was split. Should it describe the one-app restructure (`0394b64`), the bar and theme centralisation (`c59c155`) and the footer layout (`a074f50`, `01a1a4a`) as Kerk's, and the shell, site, sessions, engines and overlays as yours? My evidence for that split is the diffs named in §13, not commit counts.
4. QUESTION: are the stale theme and hosting sentences in the three ARCHITECTURE docs (§15, row 1) known? Your rule is that docs change only after you have been asked, and this audit is read-only, so I changed nothing.
5. QUESTION: should the byte-identical copies (§11.2) and the unused `sorting/engine/useSortPlayer.ts` be reported as known technical debt?
6. QUESTION: `bj/fix-traversal-ci` (`3a6443b`) is already an ancestor of `main` (merged as PR #7), so its code is part of what this note describes. `bj/engine-package-spike` (`053064f`, 2026-09-17, "M4a packaging spike for @visualgo/kerk-bfs-runtime") is 5 commits ahead of `main` and not in the app, so I left it out (VERIFIED, `git merge-base --is-ancestor`, `git rev-list --count`). Should the report mention the spike as part of the architecture work?
