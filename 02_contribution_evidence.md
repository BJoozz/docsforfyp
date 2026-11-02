# 02 · Contribution evidence for VisuAlgo+ (C1 to C14)

Audit date: 2026-11-01/02\
Repository: `kerktaiheng/visualgo-plus-design`, `main` at `662e7b3`\
Evidence labels: VERIFIED / DOCUMENTED / INFERENCE / QUESTION\
The owner's answers of 2026-11-01 and 2026-11-03 are applied (doc 01, the table at its top); anything they leave open stays a QUESTION.

## How to read this document

- **Ids and labels.** C1 to C14 and Q1 to Q17 are the ids of research note 09 (`evidence/research-notes/09-candidate-contributions.md`). VERIFIED: seen in code, a diff, a log or a test run. DOCUMENTED: a doc, commit message or PR body says it. INFERENCE: my reading. QUESTION: Bao must answer.
- **Names.** "Bao" means the git identities `BJoozz <123baoek31@gmail.com>` (his own commits) and `BJoozz <83776047+BJoozz@users.noreply.github.com>` (30 GitHub merge commits). Both are Bao's (confirmed 2026-11-03). "Kerk" means `Kerk Tai Heng <taihengkerk@gmail.com>` and `kerktaiheng`.
- **AI assistance.** Most of Bao's commits were made with Claude Code, and Bellman-Ford and Prim with Codex (doc 01 §1.4). Per Bao (2026-11-03), every AI-assisted change was made under his requests, choices and confirmation, and he read the diffs, ran the app and ran the tests or watched CI before accepting it. This document treats that work as his and does not repeat the point; blame still shows only who last changed a line.
- **Tests.** The full check set passed on 2026-11-01 (research note 07 §2): typecheck; lint 0 errors, 2 warnings; 654 `node:test` + 2,619 vitest = 3,273 unit cases; the build; 151 of 151 browser cases. On 2026-11-02 at 13:58 +08:00 I also ran seven graph test files (`node --experimental-strip-types --test`, Node v24.17.0, on a `git archive` copy of `main` outside the repository): C7's five property and oracle files, 45 of 45 passed; C10's two graph step-note files, 22 of 22 passed. Every cited hash was checked with `git show -s`, every ownership number with `git blame -w` at `HEAD`. The working tree stayed clean.
- **Scope (Q1).** The FYP is NUS AY2026/27 Semester 1. Bao counts the work from the first standalone commit (2026-07-28) through the summer as "week 0", and all the standalone work is inside the report's scope; the FYP proper began in Week 1 of the semester, about 2026-08-10 (exact date to confirm), so V1's work to PR #5 (08-09) is week 0 and the rest FYP proper. The tables give dates, not phases.

## 1. Overview of the major contributions

Facts are VERIFIED (git log, blame, test logs of 2026-11-01/02) unless marked. The last two columns are INFERENCE: my ranking, after note 09 §3.

| ID | Contribution | Period (2026) | Where | Bao's part | Collaborator or inherited part | Status now | Evidence | Report value |
|---|---|---|---|---|---|---|---|---|
| C1 | Graph visualizer V1, then the v2 redesign | 07-28 to 09-11 | `graph-algorithm-visualizer`, `graph-visualizer-v2` | all 55 V1 and 53 v2 commits (v2 built with Claude from 09-07) | create-vite template; a few V1 files ported into v2 | V1 superseded; v2 is the base of `prototypes/src/graph` | Strong: history; units 162/162, 276/276 | High (foundation, from week 0) |
| C2 | Tree and sorting visualizers | by 08-13 to 09-17 | `tree-visualizer`, `sorting-algorithm-visualizer` | all commits (tree built with Claude from 09-12) | tree probably began from v2's session code (INFERENCE, Q10) | base of `src/tree`, `src/sorting` | Medium-strong: tree 664/664; sorting 334/335, one squashed commit | Medium-high |
| C3 | Engine integration study (M0 to M4a) | 09-17 | `bj/engine-v2-experiment` + 2 local branches | 6 commits on Kerk's engine | Kerk's engine | never merged; unused | Weak-medium: tests not run, no CI | Low-medium |
| C4 | V2 (split rails) and V7 (docks) prototypes | 09-13 to 10-15 | PRs #1 to #3 | built all six copies | Kerk's wireframe (V1 to V9), themes | deleted 10-18; ideas kept in V10 | Medium: merges, blob comparisons | Medium (exploration) |
| C5 | The site and its host boundary | 09-28 to 10-20 | PRs #4, #6, #15; `prototypes/src/site` | site, routes, host-chrome boundary, static hosting | Kerk's design system and UI kit; his `c59c155` (one bar, one theme writer) | integrated; deployed | Strong: 1,898 of 1,954 lines; site specs pass | High, shared credit |
| C6 | V10 "Panel groups" shell | 10-16 to 10-18; fix 10-29 | PRs #15 to #17, #35 | design (choices 1 to 26), model, shell, tests | Kerk: drop-band tuning (41 lines), move to `src/shared` | the only layout | Strong: model 1,441/1,441 lines; 77 unit cases | Highest |
| C7 | Graph algorithms beyond upstream | 09-29 to 10-22 | PRs #6, #8, #9, #28 | recursive DFS, End node, Topological Sort, Bipartite Check, Cut Vertex & Bridge; Bellman-Ford and Prim (built with Codex, DD-38, DD-39) | 5 engines from v2 | integrated (11 ids) | Strong: property and oracle tests, re-run 2026-11-02 | High |
| C8 | Tree operations beyond upstream | 10-07 to 10-21 | PRs #6, #22 to #27; direct pushes | BST/AVL operations, lazy segment tree, Binary Heap round, LCA runs and hover | six workspaces from tree-visualizer | integrated | Strong tests; weak process (no PR for some) | Medium-high |
| C9 | Sorting: Study, Compare, exact seeking | 09-23 to 10-30 | PR #3, `0e3857f`, PR #37 | integration layer, seeking, eager cap | sorting core inherited; SP-19, SP-20 in Kerk's commits | integrated | Medium | Medium |
| C10 | Step notes and on-canvas explanation | 10-13 to 10-26 | PRs #29 to #33 | writers, shared layer, placement, timing | none found | integrated; partial coverage | Strong: blame 100%; unit and browser cases | High |
| C11 | Motion and playback semantics | 10-02 to 10-30 | PR #6, direct pushes, PRs #10 to #12, #37 | waves, paused motion, merged steps, final frame, countdown | Kerk's `a074f50`, `01a1a4a`; upstream pacing | integrated | Medium | Medium |
| C12 | visualgo.net samples, e-Lectures, catalogue | 09-28 to 10-22 | PR #13; decks; `modules.ts` | copied the examples, wrote the decks | visualgo.net source (used with Prof Halim's knowledge and agreement, owner 2026-11-03) | integrated | Medium-low: source DOCUMENTED | Medium-low; credit matters |
| C13 | Process and verification evidence | 09-20 to 10-30 | records, tests, CI, PRs #34 to #37 | 88 of 95 records and most test lines | Kerk: 7 records, `app.yml`, most of `prototypes/AGENTS.md` | in use | Strong run; no PR review | High (evaluation) |
| C14 | One app, CI and deployment | 09-03 to 10-30 | `.github/workflows`, `0394b64` | old CI, static hosting, review tooling | mostly Kerk | integrated; deployed | Strong (Kerk's) | Context only |

## 2. Detailed evidence records

### 2.1 C6 · V10 "Panel groups" shell

**Problem.** After V2 and V7 had been built for all three visualizers (C4), one layout had to merge their ideas: three regions (left, right, bottom), each a stack of collapsible tab groups, around a fixed canvas that is never a tab and never remounted, with VS Code-style drag feedback and every size limit in one place. [DOCUMENTED, PR #15, header of `groupsModel.ts`]

**Baseline.** Kerk's wireframe 2 (`69aa8e4`, frames V1 to V9) [VERIFIED]; Bao's V7 `docksModel.ts`, named in `groupsModel.ts` as the source of its region arithmetic (DD-26) [DOCUMENTED]. No upstream repository had tab groups [VERIFIED].

**Bao's part and others'.**

| Kind | Evidence | Label |
|---|---|---|
| Design | Frames V10 and V11 added to Kerk's wireframe file (`55f3387`); the proposal `design/proposals/viz-shell-v10/README.md` (7 of 13 commits); choices 1 to 26, quoted in Vietnamese in Bao's commits (choice 1: "Chồng nhóm theo vùng", stacks of groups by region) | VERIFIED |
| Original implementation | Blame: `groupsModel.ts` 1,441 of 1,441 lines; its test 1,355/1,355; `GroupsLayout.tsx` 637/639; `dropTargets.ts` 347/388; `GroupView`, `TabMenu`, `Splitter`, `useGroups` 658/658 | VERIFIED |
| Integration, maintenance | Graph page `950ab6f`, tree `d82a24c`, sorting `0e3857f`, site `d445364` (PR #15, 20 commits, 2026-10-17); choices 24 to 26 in `649f42e`, `b8f1c1a` (PR #17); front tab kept in view `fd9ff5c` (PR #35, review finding S2-01) | VERIFIED |
| Kerk (implementer) | 41 lines of `dropTargets.ts` (`ae63a62`, `c59c155`) for choices 27 and 33; the pure move into `src/shared` (`0394b64`) | VERIFIED; choices 27 to 48 were decided by Kerk and Bao together (owner, 2026-11-03) |

**Approach and components.** [VERIFIED in code]
- **State, defaults, minimums, drop targets and views:** as set out in doc 03 §1.3 (`LayoutState`, `DEFAULT_LAYOUT`, groups of at least 240 × 120 px, the graph's 360 × 320 drawing floor, the drop targets of DD-52 with `BAND_SHARE = 0.2`, every tab's panel kept mounted, one versioned key per visualizer).
- **Invariants,** "kept by every operation and by the parser" (DD-51): each of the four panels (`action`, `electure`, `pseudocode`, `status`) in exactly one group; each declared extra panel at most once; no empty group (a group whose last tab leaves is removed; a region left with none closes and keeps its size); `active` is one of the group's tabs; no nesting; `v: 1`. `parseLayout` falls back to the default for anything unparseable, not `v: 1` or missing a panel, and repairs a bad front tab, size or id.
- **One resolver.** `resolveLayout(state, dims, { minDrawing })` fits the open columns into the width less their splitters and the centre's minimum (`centreMinWidth`: the floor's width, or the bottom row's groups at 240px plus splitters when wider), in proportion to how far each is above its minimum, never under 240px; it caps the bottom row at the height less a splitter and the floor; below every minimum the columns keep 240px and the centre gives way. Stored sizes are preferences, refitted on every render. `maxRegionSize`, `maxGroupSize` and `canDrop` reuse this arithmetic, so splitter ranges and drop refusals match what is drawn.

**Alternatives and trade-offs.** [DOCUMENTED, proposal §0.1, DD-50 to DD-56, PR #36] Two built layouts were compared first (C4). Choice 1 rejects "a depth-2 grid" and "a free split tree"; choice 19 rejects V7's fixed 1:2:1 drop zones for VS Code-style edge bands; choices 24 to 26: fit only when the drawing's size changes, bottom groups keep 240px, hidden groups keep their space. The split band went from 30% to 15% capped at 32px (choice 27), then to a fifth (choice 33), in Kerk's commits (joint decisions). Tab drag and split checks stay manual ("guides only, no new shell e2e", PR #36, review S2-02).

**Resulting behaviour.** [VERIFIED; figure F3] By default Action and e-Lecture share one left group, Pseudocode sits above Status on the right, and there is no bottom row. Dragging Action over the middle of the Pseudocode group previews a join (F3); its lower fifth splits off a new group; the drawing's bottom edge band opens the bottom row. A drop with no room is refused: "No room for another group in the …" plus the region's name.

**Verification evidence.** `groupsModel.test.ts` (62 cases) runs a 4,000-step seeded random walk (mulberry32, seed 20261017) of moves, collapses, resizes and splitter presses; after every step it checks each invariant on the stored and the presented layout and that bottom groups keep 240px while the page holds every minimum; every 25 steps it round-trips `parseLayout(serializeLayout(state))`; it requires over 100 allowed and over 10 refused drops [VERIFIED, file read]. It and `dropTargets.test.ts` (15 cases) passed on 2026-11-01 [VERIFIED, notes 03 and 07]; so did `prototypes/e2e/graph.spec.ts:299` (DD-54).

**Status and limitations.** The only layout since `0394b64` (2026-10-18), used by all three visualizers [VERIFIED]. No browser case drags or splits a tab; one drives a column splitter (`prototypes/e2e/graph.spec.ts:299`, DD-54). `0394b64` deleted 62 of the kept groups layout's 74 spec files (the visualizers' own suites, 12 of them shell specs such as `layout-groups*.spec.ts`); the site's 12 stayed [VERIFIED]. Desktop and laptop windows only [DOCUMENTED]. The proposal's status line still reads "Stage 0 … design only" [VERIFIED, stale]. Commit dates support no productivity claim (unsafe claim 21).

**Key references.** `prototypes/src/shared/components/layout/`; DD-50 to DD-56, TP-21 to TP-27, SP-12 to SP-18; PRs #15 (`c899b69`), #16, #17 (`b9ec8fa`), #35.

**Suggested section and figure.** "One shell for three visualizers": F3; D2 (doc 04 §1.4) or doc 03's Diagram 2 (`LayoutState` → `presentLayout` → `resolveLayout` → `GroupsLayout`); a table of invariants and minimums.

### 2.2 C7 · Graph algorithms beyond upstream

**Problem.** graph-visualizer-v2 had five algorithms; visualgo.net's Graph Traversal, SSSP and MST pages list more. `createAlgorithmVisualizationSequence` now switches over 11 ids. [VERIFIED; aim DOCUMENTED]

**Baseline.** BFS, stack DFS, Dijkstra, Edmonds-Karp and Kruskal from v2 (`c8b14e6`, copied in `0073875`), changed here by 5 to 28 lines each [VERIFIED, note 08].

**Bao's part and others'.**

| Kind | Evidence | Label |
|---|---|---|
| Original implementation | Recursive DFS `4ab075c` (DD-33); End node for BFS, Dijkstra and Bellman-Ford `9e6e7bd`, `2511937`, `8a5f607` (DD-45, PRs #8, #9); PR #28 (DD-60): Topological Sort, DFS or Kahn, `b88952d` (+3,280/−127); Bipartite Graph Check, DFS or BFS, `84c5917` (+3,182/−95); Cut Vertex & Bridge `0fc105c` (+2,806/−119); the Method control `ALGORITHM_METHODS`. Claude trailers on all | VERIFIED |
| Decision | DD-60 quotes the owner's choices of 2026-10-21 in Vietnamese ("thực hiện trước 3 thuật đầu tiên", do the first three first); Codex's research note was "input only" (PR #28) | DOCUMENTED |
| Built with Codex | Bellman-Ford (`aef5d0b`, `0aac567`, `6417767`) and Prim (`4bd0879`, `5428ed3`, `686c06b`, `65634cf`, `490e1d1`), at Bao's request; DD-38 and DD-39 record the plans as Codex's, with Bao's dated choices of 2026-10-04 and 10-05. The review commits `eac9fbd` and `6b1791a` report independent checks agreeing on 4,000 random signed graphs | VERIFIED (commits); review content DOCUMENTED |
| Kerk | None in these engines | VERIFIED |

**Approach and components.** [VERIFIED in code unless marked] One folder per algorithm: an eager engine (`create*Sequence.ts`, all steps built at once), presentation, pacing, headline, pseudocode, types; `algorithmIntegration.ts` dispatches by `sequence.kind`; `graphInterpretation.ts` gives Bipartite Check and Cut Vertex & Bridge an undirected reading (DD-30). Topological Sort on a cycle ends on its evidence (the DFS witness cycle, or Kahn's stuck vertices), where visualgo.net discards the run [DOCUMENTED, DD-60]. Cut Vertex & Bridge skips the parent edge by id (`edge.id === parentEdge.get(u)`, `createCutVertexBridgeSequence.ts:170`), so a doubled edge is never a bridge; its comment says visualgo.net skips every edge to the parent vertex [DOCUMENTED, not checked on visualgo.net].

**Alternatives and trade-offs.** [DOCUMENTED, DD-33, DD-60] Two DFS entries named for what they hold; later traversals take one entry and a Method; SCC and 2-SAT left for a later round; short decks.

**Resulting behaviour.** [VERIFIED; figure F8] On visualgo.net's CP4 4.7 sample, the last frame of Cut Vertex & Bridge marks the cut vertices and bridges. Kahn on a cyclic graph ends by listing the stuck vertices, each with indegree above zero.

**Verification evidence.** Seeded property and oracle tests, hand-written (no property-testing library), under `prototypes/src/graph/algorithms/` [VERIFIED, files read]:

| File | Generator | Independent check | Random cases |
|---|---|---|---|
| `topologicalSort/topologicalSortProperty.test.ts` | directed graphs, 1 to 9 vertices, parallel copies; DAGs only add edges forward along a shuffled rank, others any edge incl. self-loops | three-colour cycle search; every vertex ordered once, every edge forward; on a cycle no order, the DFS witness is a closed walk of real edges through the call stack, Kahn's stuck set is exactly the unordered vertices | 300 DAGs + 400 mixed (over 100 cyclic), both methods |
| `bipartiteCheck/bipartiteCheckProperty.test.ts` | multigraphs, 1 to 10 vertices; bipartite ones join two hidden halves; parallel copies, self-loops | BFS 2-colouring; sides cover every vertex and split every edge; the odd-cycle witness has distinct vertices and ends on the conflict edge | 400 undirected (84 not bipartite) + 300 directed + 300 with parallel edges or a self-loop |
| `cutVertexBridge/cutVertexBridgeProperty.test.ts` | multigraphs, 1 to 10 vertices, parallel copies, self-loops; every other graph authored directed | brute force: remove each vertex and edge, count components; a root is a cut vertex iff it has two or more DFS children | 400 seeds (must give over 300 cut vertices, 500 bridges, 100 second edges to a parent) + 300 seeds |
| `bellmanFord/createBellmanFordSequence.test.ts` (Codex-built) | 140 signed multigraphs, 1 to 6 vertices, weights −4 to 5 | all-pairs Floyd–Warshall oracle incl. reachability through negative cycles, every source | at least 140 graph-source cases |
| `prim/primEngine.test.ts` (Codex-built) | 20 signed multigraphs, 1 to 5 vertices | exhaustive search over edge subsets for the minimum spanning forest; every start | 20 graphs × every start |

My 2026-11-02 run of these five files: 45 of 45 passed [VERIFIED]. On 2026-11-01 the graph suite passed 654/654, and so did `graph-traversal.spec.ts` (10 cases), `bellman-ford.spec.ts` (2), `prim.spec.ts` (5) and the Graph Editor case that runs all eleven algorithms [VERIFIED, note 07]. The Bellman-Ford and Prim acceptance records cannot be re-run: their scripts went with the standalone builds on 2026-10-18 [VERIFIED absence].

**Status and limitations.** Integrated. Not built: SCC and 2-SAT (graph backlog item 19), Ford-Fulkerson, Dinic [VERIFIED absent; plan DOCUMENTED]. Only Dijkstra writes step notes (C10).

**Key references.** Folders `topologicalSort`, `bipartiteCheck`, `cutVertexBridge`, `bellmanFord`, `prim`; `algorithmMethods.ts`, `graphInterpretation.ts`; DD-33, DD-38, DD-39, DD-45, DD-60; PR #28 (merge `4621b1f`).

**Suggested section and figure.** "Algorithms and how they are checked": lead with PR #28 and the End node; F8 and the table above. Say that Bellman-Ford and Prim were built with Codex (DD-38, DD-39).

### 2.3 C10 · Step notes and on-canvas explanation

**Problem.** A step that changes nothing on the drawing (a rejected comparison, a kept distance) showed its verdict only in Status. The owner asked on 2026-10-23 for floating text on the canvas, green to accept and red to reject (TP-34, quoted in Vietnamese), and on 2026-10-25 for Dijkstra too (DD-61, where "Codex's plan was input only"). [DOCUMENTED]

**Baseline.** The tree's inherited NOW, MISS, INSERTED and DONE badges; value popups (`ff77eca`, TP-20) and end badges (`28e08f8`, TP-19) built here on 2026-10-13. [VERIFIED]

**Bao's part and others'.** All commits are Bao's (`ff77eca`, `d82aa18`, `7180d81`, `277405c`, `94ec5db`, `08590ef`, `157d9a9`, `6b1a4fc`). Blame: `stepNotePlacement.ts` 247/247, `stepNotes.ts` 70/70, `floatingTextTiming.ts` 43/43, `StepNoteLayer.tsx` 94/94, `FloatingText.tsx` 45/45. `08590ef` moved the writer, placement and layer into `src/shared`: one layer for tree and graph. Kerk: none found. [VERIFIED]

**Approach and components.** [VERIFIED in code]
- **Writers.** `stepNotes.ts` (`createStepNoteWriter`, `writeStepNotes`, `NO_STEP_NOTES`) plus one writer per operation: 13 in the tree (LCA 1, BST 8, AVL 3, Binary Heap 1) and `dijkstraStepNotes.ts`. Tones `accept` (green), `reject` (red), `note` (ink).
- **Layer.** `StepNoteLayer.tsx` sits outside React Flow's pan and zoom transform: 14px text at any zoom, following pans, zooms and drags. A note shows only when its step is reached forward (`useStepArrival`). The layer is `aria-hidden`, so Status stays the full account [intent DOCUMENTED, DD-22's note].
- **Obstacle model** (`placeStepNotes`, `prototypes/src/shared/visualization/stepNotePlacement.ts`). Inputs: the canvas size; each drawn node as an anchor (`screen` box, `reach` of node and marks, `badges`); other `obstacles` (the graph's edge-weight labels; the tree's ROOT band, badges, index and popups via its wrapper). A note goes centred above its node, 4px above its reach, moved in from the sides (8px margin). If that leaves the canvas or lies on a badge or obstacle, it tries beside the node (right, then left), then below, taking the first place inside the canvas that covers nothing, else the one covering least; it lies on a badge only if every place does. A note without a node uses the top centre or a top corner; a note whose node is off the canvas is hidden; overlapping notes stack. A note rises up to 20px, less where the canvas top, a badge, an obstacle or a note above is nearer. The canvas legend is not an obstacle (the owner's answer of 2026-10-25, `157d9a9`). The graph sets `keepToOwnNode` (other nodes count as badges) and `clearAtPop` (check at the 1.04 pop scale); the tree sets neither.
- **Timing** (`floatingTextTiming.ts`). A number popup lives 800ms (`VALUE_POPUP_MS`), a note 1,600ms (`FLOATING_NOTE_MS`). Stepped by hand, a text lives its whole life; while a run plays it is cut to `0.9 × effectiveIntervalMs − delay`, and dropped when that is under 200ms (`FLOATING_TEXT_MIN_MS`).

**Alternatives and trade-offs.** [DOCUMENTED, PR #32, `157d9a9`] Keeping notes off the legend was dropped because the legend can be hidden. Left open: on crowded samples at fit zoom some graph notes still land on another vertex or a weight (34 and 95 of 444 notes), and 525 of 49,947 tree fuzz notes would move under `clearAtPop`.

**Resulting behaviour.** [VERIFIED; figure F4] Dijkstra on `/sssp`, frame 24 of 31: relaxing B→E writes "4 + 3 < 8 · update" in green over E while its badge reads 8→7; an equal or longer candidate writes "… · keep" in red, a settled target "already settled" (`dijkstraStepNotes.ts:33-43`). Tree examples: F5 (LCA query), F6 (heap insert).

**Verification evidence.** The six shared test files (`stepNotes`, `stepNotePlacement`, `StepNoteLayer`, `FloatingText`, `floatingTextTiming`, `floatingTextTones`), 17 tree note test files, `prototypes/e2e/dijkstra.spec.ts` (8 cases: text, colour, placement, 1366 × 768 with the legend open) and the note cases of `prototypes/e2e/tree.spec.ts` passed on 2026-11-01 [VERIFIED, note 07]. My 2026-11-02 run of `dijkstraStepNotes.test.ts` and `stepNoteAnchor.test.ts`: 22 of 22 passed [VERIFIED]. PR #32's "20,000-scenario fuzz, 0 mismatches" is DOCUMENTED only; no fuzz script is in the repository [VERIFIED absence].

**Status and limitations.** Partial coverage: LCA, BST, AVL, Binary Heap and Dijkstra; none for the segment trees, Trie, sorting or the other ten graph algorithms [VERIFIED]. No evidence of a learning benefit exists; describe the mechanism and its tests only (unsafe claim 1).

**Key references.** `prototypes/src/shared/visualization/` (`stepNotes.ts`, `stepNotePlacement.ts`, `floatingTextTiming.ts`, `useStepArrival.ts`), `prototypes/src/shared/components/canvas/StepNoteLayer.tsx`, `prototypes/src/graph/components/graph/stepNoteAnchor.ts`, `prototypes/src/tree/components/tree/stepNotePlacement.ts`; TP-19, TP-20, TP-34 to TP-36, DD-61; PRs #29 to #33.

**Suggested section and figure.** "Explaining a step on the canvas": F4 with F5 or F6; a sketch of the candidate places and the rise.

### 2.4 C1 + C2 · Standalone foundations (from week 0)

**Problem.** [DOCUMENTED, READMEs, `AGENTS.md`, v2's DD-01 to DD-12] Graph: an editable weighted graph that plays BFS, DFS, Dijkstra, Edmonds-Karp with minimum cut, and Kruskal. V1 grew one large `App`, separate edit and run canvases and snapshots per step; v2 rebuilt it with separate state owners (`GraphDocument`, `GraphLayout`, `VisualizationSession`, `GraphPresentation`) around one canvas that stays mounted, and typed step sequences built when a run starts. Tree: one persistent workspace for LCA, BST, AVL, Min Heap, Trie and Segment Tree, with previews committed only on Apply. Sorting: typed operations applied and reversed by a player, on 1, 2 or 4 panes with one tick, drawn on a Canvas.

**Baseline.** V1's first commit `f3a0db8` (2026-07-28) already holds a working app on a create-vite scaffold (package `js-ts-learning`); earlier history is Q10. v2 starts from the plain template `92fa193`. [VERIFIED]

**Bao's part.** Every commit in the four repositories is Bao's; Kerk has none [VERIFIED]. No third-party code was found in them beyond the create-vite template [INFERENCE]; where V1's first commit and the squashed sorting commit came from is Q10. Adaptation: v2 ported a few V1 pieces (`CenteredGraphEdge`, `parallelEdges`, `CsaGraphNode`, the Union-Find of `kruskalEngine`) [VERIFIED shared lines; INFERENCE ported]; tree's `sessionReducer.ts` shares 72 lines with v2's, so it probably began from v2 [INFERENCE, Q10].

| Repository | Dates (2026) | Commits, PRs, HEAD | Tooling (fact) [VERIFIED] |
|---|---|---|---|
| `graph-algorithm-visualizer` (V1) | 07-28 to 08-19 | 55 (24 on `main`), 8 PRs, `5fc06a0` | no trailer on 50 non-merge commits; PR #8 from `agent/edit-tools-sidebar` |
| `graph-visualizer-v2` | 08-20 to 09-11 | 53, 14 PRs, `c8b14e6` | trailers on 20 of 38, from 09-07; `AGENTS.md` "for coding agents" from `fc62e5a` |
| `tree-visualizer` | 09-03 to 09-17 | 50, 8 PRs, `46ce0a7` | trailers on 34 of 41, from 09-12 |
| `sorting-algorithm-visualizer` | `9236a65` (08-19, squashed; doc dated 08-13) | 1 | no trailer; an 814-line `AGENTS.md` |

**Approach and components.** [DOCUMENTED; names VERIFIED] React 19, TypeScript, Vite; React Flow with `d3-force` (graph) and `d3-hierarchy` (tree); a generic typed session (`sessionReducer.ts`: idle, or paused/playing/finished with a `sessionId`, so a stale tick is ignored); typed per-algorithm metadata; semantic pacing per step type (v2 DD-17). v2 recorded DD-01 to DD-22 (16 commits, all Bao's).

**Alternatives and trade-offs.** [DOCUMENTED] v2's DD-01: "V1 is reference material, not a codebase to continue"; its `AGENTS.md` lists the V1 architecture "that should NOT be copied". v2 dropped V1's Edit/Run pages, fullscreen and undo on purpose.

**Resulting behaviour.** [VERIFIED] The app still runs this design: `prototypes/src/graph/visualization/sessionReducer.ts` and `prototypes/src/tree/visualization/sessionReducer.ts` are byte-identical to `graph-visualizer-v2@c8b14e6` and `tree-visualizer@46ce0a7` (blob hashes, 2026-11-02). F2 shows the inherited BFS on `/dfsbfs`.

**Verification evidence.** Unit runs at each HEAD on 2026-11-01 (note 02): V1 162/162, v2 276/276, tree 664/664, sorting 334/335 (the failure is a locale-dependent assertion in `Metrics.test.tsx` on this PC's vi-VN locale). V1's and v2's last CI runs were green; tree and sorting have no CI. [VERIFIED]

**Status and limitations.** V1 is superseded and reaches the app only through v2. Copies: v2 `c8b14e6` → `0073875` (09-20), tree `46ce0a7` → `7b16bf3` (09-22), sorting `9236a65` → `ee4bb72` (09-25); still byte-identical: graph 53 of 173 source files, tree 88 of 289, sorting 17 of 45 [VERIFIED, note 02]. Sorting's process is not evidenced (Q10); its 2026-08-13 performance numbers describe the standalone engine only (unsafe claim 20).

**Key references.** V1 `2c4feaa`, `265d6a7`, `447abc0`, `b0bb316`; v2 `f6149f1`, `f864de7`, `ff01dce`, `c5dfb43`, `0f5b49a`, `2ece0c6`, `86762de`; tree `e687099`, `015469e`, `f10d6d1`; inherited DD-01 to DD-22.

**Suggested section and figure.** "Background and foundations (week 0 onwards)": a timeline of the four repositories and the three copy points; a diagram of v2's state owners around one canvas; F2.

### 2.5 C5 · The site and its host boundary

**Problem.** One site that mounts the real visualizers under one top bar: a homepage catalogue; routes `/`, `/:slug`, `/:slug/:algorithm`; one owner of the theme (`html[data-theme]`); static hosting under a subpath. [VERIFIED code; DOCUMENTED aim]

**Baseline.** Kerk's design system (`634b5be`: tokens, nine themes, 26 components, a UI kit with `HomeScreen.jsx`), itself "read from source code" of a visualgo fork [VERIFIED files; DOCUMENTED source]; each visualizer had its own bar, menus and theme writer.

**Bao's part and others'.**

| Kind | Evidence | Label |
|---|---|---|
| Original implementation | V2 and V7 sites `87db4a3`, `8aeb543` (2026-09-28, PR #4); host-chrome adapters `a8dd634` (+948/−162); `VA_BASE` and `prototypes/scripts/static-fallback.mjs` (29/29 lines); editor cards `cc38942`; credit line `ae2f31f`; groups site `d445364`; one design-system edit, `57912e8` (`TopBar` `onHomeClick`). Blame of every file in `prototypes/src/site`: 1,898 of 1,954 lines (Kerk 56) | VERIFIED |
| Kerk | The design system and kit the homepage follows (the site proposal: "Kerk's homepage", "Kerk's UI kit"); 56 lines of `src/site`; `c59c155` made the site the only bar and theme writer by deleting the visualizers' own; `3c79d36` (Full screen and Shortcuts beside Settings, no Save image); `40a63bd` (tips removed); `prototypes/vite.config.ts` 72/72 (kept `VA_BASE`) | VERIFIED; choices 33 to 45 were decided by Kerk and Bao together (owner, 2026-11-03) |
| Third party | Card table "transcribed from visualgo.net's own homepage table" via the kit's `data.js`; the VisuAlgo name; NUS Computing and Optiver logos | DOCUMENTED; used with Prof Halim's knowledge and agreement (owner, 2026-11-03) |

**Approach and components.** [VERIFIED] `App.tsx`: a `BrowserRouter` with `basename = import.meta.env.BASE_URL`; unknown paths return to `/`; former ids redirect (`dfs` → `dfs-stack`, `min-heap` → `binary-heap`). `modules.ts`: 30 cards, 8 full, 4 partial, 18 "soon". `HostedModule` provides `HostChromeContext`, whose `renderTopBar` draws the site's `ModuleBar`, so each visualizer hands its bar parts to the host. `useTheme.ts` is the only writer of `html[data-theme]`; the visualizers only read it. A static host serves deep links through the `404.html` and `_redirects` written after the build.

**Alternatives and trade-offs.** [DOCUMENTED, site proposal] The kit's `VizScreen` is a reference, not code; the design system's `MediaControls` and `SpeedControl` go unused in favour of the visualizers' footer ("a loss worth naming"); 12 of 30 cards open.

**Resulting behaviour.** [VERIFIED] `/sssp` opens the graph visualizer on Dijkstra under the site bar. On 2026-11-01 the Pages site answered 200 and the deep link `/bst/avl` was served by the `404.html` fallback (curl, not a browser; note 07). F1 shows the catalogue.

**Verification evidence.** `modules.test.ts` 24/24; the `home` (12), `journey` (8), `chrome` (4) and `themes` (5) browser cases passed on 2026-11-01; `themes.spec.ts` computes the WCAG contrast of sampled chrome text in all nine themes and requires 4.5:1. [VERIFIED]

**Status and limitations.** Deployed by GitHub Pages; the Vercel attempt (`c9e4598`, PR #5) was closed [VERIFIED]. The theme list is written twice (`prototypes/src/site/useTheme.ts`, `prototypes/src/shared/app/themes.ts`) with no test tying them; "full" counts visualgo.net's algorithm names, not operations (Q14) [VERIFIED].

**Key references.** `prototypes/src/site/` (`App.tsx`, `HostedModule.tsx`, `ModulePage.tsx`, `useTheme.ts`, `modules.ts`); `design/proposals/visualgo-web-site/README.md`; DD-28, DD-34, TP-10, TP-11; PRs #4 (`9cc009f`), #6, #15.

**Suggested section and figure.** "System integration: one site, three visualizers": F1 and a diagram site → `HostedModule` → visualizer → `GroupsLayout`; credit Kerk's design system, kit and `c59c155` in the same paragraph.

### 2.6 C8 · Tree operations beyond upstream (deep case: the Binary Heap round)

**Scope.** tree-visualizer offered BST Search/Insert/Delete, AVL Inspection/Insert, Min-Heap Insert/Extract Min, an eager sum segment tree, and Trie Insert/Search [VERIFIED at `46ce0a7`]. Added here, all first-add commits Bao's with Claude trailers [VERIFIED]:

| Area | Commits | Record | Route to `main` |
|---|---|---|---|
| BST/AVL: Min/Max, Predecessor/Successor, Lower Bound, Select(k), three traversals, AVL Delete | `c364204`, `a6c9965`, `c56eb7b`, `e7f2fec`, `9a2f04b`, `c620145` | TP-15 | pushed, no PR |
| Lazy segment tree; exact decimals in both trees | `fc4172d`, `a521c13` | TP-13 | pushed, no PR |
| LCA ancestor strip; two runs; hover ancestors | `00ed4c2`, `303e50b`; `e55de1c`; `60ccc44` | TP-04, TP-22, TP-31, TP-32 | PRs #6, #22 (with #23), #24 |
| Edges centre to centre | `499cb42` | TP-30 | PR #22 |
| Binary Heap round | below | TP-33 | PRs #25 to #27 |

Kerk: none in these operations; TP-28 and TP-29 (the "Select preset" label, the editor look) come from his commits, joint decisions [VERIFIED].

**Deep case: the Binary Heap round (2026-10-20/21).**
- **Problem.** The owner's request of 2026-10-20 (TP-33, Vietnamese quote): make "Binary Min Heap" a "Binary Heap" with a Min/Max switch, and learn the other operations from visualgo.net's source. [DOCUMENTED]
- **Baseline.** Inherited Min-Heap Insert and Extract Min (`015469e`, copied in `7b16bf3`). [VERIFIED]
- **Bao's part and others'.** PR #25: 8 commits, 108 files, +8,933/−587 (`7d39c38` order, 1-based indices, groups; `0a86739` Create; `1804565` Update key, Delete; `3409565` Extract K times, Heap sort, 31 items; `88e8396` deck and TP-33); then `3fec43c` (PR #26) and `ea37326` (PR #27) [VERIFIED]. PR #25 says "each step was built by one agent and reviewed by two" [DOCUMENTED].
- **Approach and components.** `HeapOrder = 'min' | 'max'` on the document; comparisons through `heapOutranks(a, b, order)`; `validateHeap` names the order; six groups: Create (O(N log N) or O(N)), Insert, Extract (once or K times, with an output rail), Update key(i, v), Delete(i) (root ∓ 1 trick), Heap sort (default or in-place, a query); 1-based indices; at most 31 items (`HEAP_MAX_ITEMS = 31`); changing runs preview until Apply. [VERIFIED symbols; details DOCUMENTED, TP-33]
- **Alternatives and trade-offs.** visualgo.net's page is max-heap only, so the switch is this prototype's; 31 items (visualgo.net's normal-scale limit) rather than 63, the implementer's pick after the question "31 or 63?" quoted in TP-33; some slips of the original not copied (e.g. Heap sort stopping at N−1). [DOCUMENTED, TP-33, PR #25]
- **A finding reproduced before its fix.** Codex's review of PRs #25/#26 found Update key's popup reading `+Infinity` for a min heap `[-1e308, 5]` with A[1] set to `1e308`; PR #27 says it was reproduced in both directions first. The owner then limited heap values to the segment trees' decimal rule (15 digits, 6 decimals), one rule in `prototypes/src/tree/heap/model/heapValue.ts`. [DOCUMENTED, PR #27; file VERIFIED]
- **Resulting behaviour.** A heap insert climbs with one note per comparison, in the style "13 > 7 · swap up" (TP-33 wording) [DOCUMENTED]; figure F6.
- **Verification evidence.** Seeded property tests in `prototypes/src/tree/algorithms/heap/`: each Create method under each order turns 200 random lists into a valid heap of the same values, committable only on its last frame; Delete and Update key 300 random runs per order; Heap sort 300 + 200 rounds [VERIFIED, files read]. The 1,881 tree vitest cases and 62 `tree.spec.ts` cases passed on 2026-11-01 [VERIFIED, note 07].

**Status and limitations.** Integrated. Not built: Range Min and Range Max; batch insert and remove [VERIFIED absent; plan DOCUMENTED]. The BST/AVL and lazy-tree work reached `main` with no PR and no recorded review [VERIFIED].

**Key references.** `prototypes/src/tree/algorithms/heap/`, `prototypes/src/tree/heap/model/`; TP-13, TP-15, TP-30 to TP-33; merges `e267352` (#25), `a436873` (#26), `7380025` (#27).

**Suggested section and figure.** One case study, not a list: "Rebuilding the heap after visualgo.net", with F6 and a table of the six operation groups.

### 2.7 C13 · Process and verification evidence

**Problem.** Keep a fast-changing, AI-assisted codebase coherent: record each decision with whose choice it is, list departures from upstream, add tests with each change, and reproduce review findings before fixing them. [DOCUMENTED]

**Baseline.** v2's DD-01 to DD-22 and its rule "update the owning document in the same change". [VERIFIED, note 04]

**Bao's part and others'.**

| Kind | Evidence | Label |
|---|---|---|
| Records | 95 local records: DD-23 to DD-61 (39), TP-01 to TP-36 (36), SP-01 to SP-20 (20); 88 first written in Bao's commits, 7 in Kerk's (`ae63a62`: DD-57, DD-58, TP-28, SP-19; `c59c155`: DD-59, TP-29, SP-20) | VERIFIED |
| Test code | Blame: 14 browser specs 4,887 of 4,952 lines; graph tests 17,479 lines to Kerk's 146, tree 25,955 to 136, sorting 6,615 to 12, shared 2,611 to 103; 159 of Bao's commits touch tests, 148 with a Claude trailer | VERIFIED (note 07; specs re-checked) |
| Rule and reviews | "Upstream is a reference only" (`38c726f`); review sessions of 2026-10-26, 10-27, 10-29, fixed in `a5bb08f` (PR #34), `fd9ff5c` (#35), `02c4e12` (#36, docs only), `9baa117` (#37); PRs #34, #35 and #37 say each finding was "reproduced before the fix" | commits VERIFIED; the findings were Codex reviews that Bao read first, each verified before its fix, the fixes his choices (owner, 2026-11-03) |
| Kerk | The 7 records; `app.yml` (94/94 lines), `pages.yml` (65/65), `ci.yml` (20/20); 62 of 70 lines of `prototypes/AGENTS.md`, including "one fix, one place" | VERIFIED |

**Approach.** Records name the decider ("the owner's decision", "the implementer's", "Codex's … not reviewed") [DOCUMENTED]; three backlogs (24, 20, 13 items); two acceptance records; the check list in `prototypes/AGENTS.md` [VERIFIED].

**Verification evidence.** The 2026-11-01 run (see "How to read"). CI: 266 runs (2026-09-04 to 10-30), 8 failed, each fixed by a later commit; `main` was red for three pushes (10-10 to 10-14, a font-sensitive test fixed by `3a6443b`, PR #7); the runs for `662e7b3` are green. [VERIFIED, note 07]

**Status and limitations (gaps).** [VERIFIED] No PR has a review or comment; 90 of Bao's commits reached `main` without a merge commit (09-29 to 10-15); the manual checklists (20, 10, 26 items) were run by hand and by agents but never recorded (owner, 2026-11-03); no coverage tool; Chromium only, desktop sizes; no automated accessibility audit; no user study and no benchmark (Kerk's early survey on the layouts has no record with Bao); browser specs went from 208 files to 12 on 2026-10-18 (14 now). Some docs are stale (Q13). "Docs describe the current state", "the owner decides rules" and "proportionate tests" are Bao's practice, not written rules.

**Key references.** `prototypes/docs/{graph,tree,sorting}/` (`DESIGN_DECISIONS.md`, `IMPROVEMENT_BACKLOG.md`); `prototypes/docs/graph/BELLMAN_FORD_ACCEPTANCE.md`, `PRIM_ACCEPTANCE.md`; `prototypes/AGENTS.md`; `.github/workflows/app.yml`; PRs #7, #34 to #37.

**Suggested section and figure.** "Evaluation and verification": a table of the 2026-11-01 results and the CI history; a plain list of what is not evaluated; the AI-assisted workflow in one paragraph (doc 05 §3).

### 2.8 Short records

**C9 · Sorting: Study, Compare and exact seeking.** Study is one pane with Pseudocode and e-Lecture; Compare is 2 or 4 panes with Status only (SP-03). The scrubber seeks exactly by replaying kept history (`seekComparison`, SP-05, `42d1597`); eager production stops at 60,000 operations across panes, round robin, then continues lazily (`EAGER_OPERATION_CAP`, SP-06, `5ccef45`); a restart remounts the run frame and always plays (SP-01, `9baa117`). Bao built it in PR #3 (`ee4bb72` to `613bca7`) and `0e3857f`; none of these symbols exists upstream. Inherited: the eight generators, the operation model, `operationBuffer.ts`, the Canvas renderer. Kerk: SP-19, SP-20 (joint decisions). Evidence: `seekComparison.test.ts` ("matches at every tick", forward and rewinding), `eagerPriming.test.ts`, 571 sorting cases and 11 `sorting.spec.ts` cases passed on 2026-11-01. Limits: no paused motion, no step notes. Figure F7. [VERIFIED unless marked]

**C11 · Motion and playback semantics.** Edge waves show which way an examined edge is crossed (DD-37, `bcbed32`); a paused step keeps its focus moving behind "Animate paused steps", which follows reduced motion until chosen (DD-42, TP-17; `7e92baf`, `a8c191c`); a drag with Live off follows the pointer (DD-43, `74a4958`); a step that only completes the one before is merged into it (DD-44, TP-18, SP-11); Live starts off (DD-46, `6b953d5`); the finished last frame keeps moving (DD-47, `be570eb`); a Speed change keeps a step's elapsed time via a shared countdown (`playbackCountdown.ts`, `9baa117`). All Bao's. Kerk: `a074f50` (Autoplay beside Stop; Next starts a paused run) and `01a1a4a` (coloured chips), pushed to `main`; DD-24 and SP-01 call `a074f50` "the owner's commit": a joint decision implemented by Kerk (owner, 2026-11-03). Inherited: typed pacing (upstream DD-17). Evidence: `playbackCountdown.test.ts`, `prototypes/e2e/graph.spec.ts:113`, `prototypes/e2e/sorting.spec.ts:107`, `prototypes/e2e/paused-motion.spec.ts` passed on 2026-11-01. [VERIFIED unless marked]

**C3 · Engine integration study (M0 to M4a).** On 2026-09-17 Bao explored connecting Kerk's C++/WASM engine to graph-visualizer-v2: stable edge ids (M1, `478174f`), a browser engine client (M2, `e348a6d`, `ee65bef`), a BFS runtime for string-id hosts (M3, `ffb9274`), a packaging spike (M4a, `053064f`, local only) and a paused draft (`53d2ef4`, local only); `4bd9ca9`..`053064f` (M1 to M4a) changes 65 files, +4,818/−183, and `53d2ef4` another 14 files, +509/−49, all in `wasm-arch/`; trailers on 4 of 6 [VERIFIED]. It defines 44, 59, 125 and 130 Node tests at M1 to M4a, loop-generated tests and Kerk's existing 25 included [VERIFIED counts]; that they pass is DOCUMENTED only (no CI, not re-run). Never merged; `prototypes/src` uses none of it [VERIFIED]. Bao's own idea, parked by his choice to focus on the visualizers; the two local-only commits stay local (owner, 2026-11-03).

**C4 · V2 (split rails) and V7 (docks) prototypes.** The three visualizers in two of Kerk's nine wireframe layouts: graph (`0073875`, PR #1), tree (`7b16bf3`, PR #2), sorting (`ee4bb72`, PR #3), plus V7 drop zones (`f510477`) [VERIFIED]. Kept alike by rule ("fix V2 first, then V7", `diff -rq`, `cmp`) [DOCUMENTED]; at `94cdaf3` the graph pair had 340 identical and 38 differing files [VERIFIED, note 03]. Bao built all six folders; Kerk drew the wireframe; Kerk and Bao chose V2 and V7 together after a survey of a group of users that Kerk organised (owner, 2026-11-03; no record with Bao). Deleted by Kerk's `0394b64`; V10 grew from the docks copies [VERIFIED]. PRs #3 and #4 say their final suites were "not independently rerun" [DOCUMENTED].

**C12 · visualgo.net content.** 37 of visualgo.net's example graphs with the same vertices, edges, weights and positions (`prototypes/src/graph/algorithms/visualgoExamples.ts`; PR #13, `bc46260`; DD-48); decks written after visualgo.net's lectures (graph 11 decks and 40 slides, tree 7 and 111, sorting 1 and 9); cards in visualgo.net's order [VERIFIED files and counts]. The file's header names visualgo.net's source, held in the private repository `BJoozz/visualgo`; PR #13 says every example was re-checked against it after two extraction errors [DOCUMENTED]. Prof Halim knows of and agrees to the use of the material, the name and the logos (owner, 2026-11-03; no written source).

**C14 · One app, CI and deployment (mostly Kerk's).** Kerk: `pages.yml`, `app.yml`, `ci.yml`; `c39b3cf` (app at `/`, engine demo at `/engine/`, PR #18); `0394b64` (PR #20: one app in `prototypes/` with npm workspaces, 3,510 files changed, the V2/V7 copies, two sites and the submodules deleted); `c59c155`, `5235fcf` (PR #21) [VERIFIED]. "The owner's decision of 2026-10-18: V10 wins" was Kerk's and Bao's together (owner, 2026-11-03). Bao: the old `prototypes.yml` (`37075b1`), static hosting (PR #4), review tooling (`a5bb08f`, PR #34), a closed Vercel attempt (`c9e4598`, PR #5) [VERIFIED]. 48 Pages runs, 43 successful; `662e7b3` green and deployed [VERIFIED]. The owner's description adds web, cache and cloud infrastructure to Kerk's part; that work lies outside the evidence read here.

## 3. Attribution summary

### 3.1 Clearly Bao's (on diffs and blame)

The four standalone repositories (C1, C2); the groups shell's model, layout, drag code, tests and design choices 1 to 26 (C6); the Graph Traversal round with its property tests, recursive DFS and the End node (C7); step notes (C10); the site's code and host boundary (C5); the tree operations (C8); the sorting integration layer (C9); the motion and playback work except Kerk's two footer commits (C11); the V2/V7 prototypes (C4); the engine study (C3); the review-session fixes (C13). The records and tests are his too: 88 of the 95 records and most test lines (Bellman-Ford's and Prim's were built with Codex). This matches the owner's working description: Bao built the graph, tree and sorting visualizers and their integration into the shared interface [code VERIFIED; description DOCUMENTED].

### 3.2 Kerk's

- The design system (`634b5be`), the wireframes (`69aa8e4`), the C++/WASM and Python engine in `wasm-arch/` (2026-09-03 to 09-14), and all current workflows [VERIFIED].
- The one-app consolidation `0394b64`; in `c59c155` the single bar and theme writer, `controls.css` (143 of 153 lines) and `editor.css` (122/122); `TransportIcon.tsx` (26/26: 16 lines from `ae63a62`, 10 from `01a1a4a`) and, in `ae63a62`, the Live push-apart `pushApart.ts` (177/177); the drop-band tuning; `3c79d36`, `40a63bd`, `a074f50`, `01a1a4a`; seven records; most of `prototypes/AGENTS.md` and the root `README.md` (15 of 17 lines) [VERIFIED].
- He implemented choices 27 to 48, which he and Bao decided together (owner, 2026-11-03). Kerk is a fellow FYP student on VisuAlgo+ under the same supervisor.

### 3.3 Inherited from Bao's own standalone repositories

"Inherited" here means "not built in this repository", not someone else's work. [VERIFIED]

| Source | Copied at → first copy | Still byte-identical | What it brought |
|---|---|---|---|
| `graph-visualizer-v2` | `c8b14e6` → `0073875` | 53 of 173 source files | five engines, session reducer, one-canvas architecture, DD-01 to DD-22 |
| `tree-visualizer` | `46ce0a7` → `7b16bf3` | 88 of 289 | six workspaces and engines, session reducer, badges |
| `sorting-algorithm-visualizer` | `9236a65` → `ee4bb72` | 17 of 45 | eight generators, operation model, buffer, Canvas renderer |

V1 reaches the app only through v2.

### 3.4 Inherited from third parties

- **visualgo.net (A/P Steven Halim's):** 37 example graphs, the lecture text the decks follow, the module catalogue, the VisuAlgo name; the NUS Computing and Optiver logos; Kerk's design system was "read from source code" of a visualgo fork [DOCUMENTED; used with Prof Halim's knowledge and agreement, owner 2026-11-03].
- **Libraries and assets:** React 19, React Router 7, React Flow (`@xyflow/react` 12), `d3-force`, `d3-hierarchy`, `d3-interpolate`, `d3-ease`; Vite 8, TypeScript 6, Vitest 4, happy-dom, Playwright, oxlint [VERIFIED, `prototypes/package.json`]; the Inter and JetBrains Mono fonts from Google Fonts, imported by the design system's `tokens/fonts.css:5` and `tokens/modern-skin.css:17` through its `styles.css`, which `prototypes/src/main.tsx:16` imports [VERIFIED]; the create-vite template [VERIFIED, V1's and v2's first commits].

### 3.5 AI assistance (facts only)

The counts are in doc 01 §1.4 and the report's paragraph in doc 05 §3. A `Co-Authored-By: Claude` trailer is on 199 of Bao's 213 own commits on `main`, 14 of Kerk's 17, 20 of 38 in v2, 34 of 41 in tree and 4 of 6 in the engine study, and on none in V1 or sorting; 30 of the 37 PR bodies say "Generated with [Claude Code]" [VERIFIED]. Bellman-Ford and Prim were built with Codex (DD-38, DD-39); later Codex plans and reviews were "input only" or reproduced before a fix (PRs #27 to #29) [DOCUMENTED]. `AGENTS.md` rules for coding agents exist in v2, sorting and the app [VERIFIED]. Of Bao's 14 untrailered commits, the 8 Bellman-Ford and Prim stage commits were made with Codex and the other 6 (`986deba`, `c458755`, `75d9760`, `1af2c72`, `e7a44f9`, `3a6443b`) by hand (owner, 2026-11-03). Per Bao, all of it was done under his requests, choices and confirmation, with his own reading of the diffs and runs of the app and of the tests or CI before acceptance.

### 3.6 What the owner's answers of 2026-11-03 settled

| Q | Answer applied | Affects |
|---|---|---|
| Q2 | Both identities are Bao's | every "Bao's" here is VERIFIED |
| Q3 | Choices 27 to 48, "V10 wins" (`0394b64`), `40a63bd` and `a074f50`: Kerk and Bao together, implemented by Kerk | C5, C6, C9, C11, C13, C14; DD-52, DD-57 to DD-59, TP-23, TP-28, TP-29, SP-14, SP-19, SP-20 |
| Q4 | AI-assisted work is Bao's: his requests, choices and confirmation; diffs read, app and tests run | C7 and every trailered change |
| Q5 | Records naming no person are implementer's defaults Bao accepted: his decisions | C13 and the design rationale |
| Q6 to Q9, Q11, Q12 | The review findings' source, Prof Halim's agreement, V2 and V7, the engine study, the checklists, the local commits: doc 01, the table at its top | C3, C4, C12, C13 |

Still open: Q1 (the exact date of Week 1), Q8 (Kerk's survey data), Q10 (the standalone history before the first commits).
