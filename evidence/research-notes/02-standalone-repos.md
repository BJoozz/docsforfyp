# 02 - The four standalone repositories (before VisuAlgo+)

Audit of 2026-11-01. I read the four read-only clones in
`C:/Users/123ba/AppData/Local/Temp/fyp-repos/` and the VisuAlgo+ main repository at
`662e7b3`. All five working trees were still clean when I finished. Every claim has a label:

- **VERIFIED**: I saw it in code, a diff, a log, `gh` output or a test run.
- **DOCUMENTED**: a doc, commit message or PR body says it. I did not check it against code.
- **INFERENCE**: my reading of the evidence.
- **QUESTION**: Bao has to answer it.

Dates are commit dates in the author's local time (+0700 or +0800). GitHub's `mergedAt`
is in UTC, so it can be one day earlier.

## 1. Overview

| Repo | Dates | Commits (all refs / on main) | PRs | HEAD | VisuAlgo+ copied it at |
|---|---|---|---|---|---|
| graph-algorithm-visualizer ("V1") | 2026-07-28 to 08-19 | 55 / 24 | 8 | `5fc06a0` | never copied (see section 6) |
| sorting-algorithm-visualizer | 2026-08-19 (one commit) | 1 / 1 | 0 | `9236a65` | `9236a65` |
| graph-visualizer-v2 | 2026-08-20 to 09-11 | 53 / 52 | 14 | `c8b14e6` | `c8b14e6` |
| tree-visualizer | 2026-09-03 to 09-17 | 50 / 50 | 8 | `46ce0a7` | `46ce0a7` (the submodule pin was the older `1477cda`) |

All of the overview table is VERIFIED from `git log --all` and `gh pr list -R BJoozz/<repo>`. Every
copied commit is the HEAD of its repository's `main`.

### Authorship and AI assistance

| Repo | Commit authors | PR author (GitHub) | Commits with a `Co-Authored-By: Claude` trailer | PR bodies with "Generated with Claude Code" |
|---|---|---|---|---|
| V1 | BJoozz (47 local, 8 GitHub web merges) | BJoozz (8/8) | 0 of 50 non-merge commits | 0 of 8 |
| sorting | BJoozz (1) | none | 0 of 1 | none |
| v2 | BJoozz (39 local, 14 web) | BJoozz (14/14) | 20 of 38 non-merge commits, all from 2026-09-07 (Fable 5.1: 16, Opus 5: 4) | 14 of 14 |
| tree | BJoozz (42 local, 8 web) | BJoozz (8/8) | 34 of 41 non-merge commits, all from 2026-09-12 (Fable 5.1: 21, Opus 5: 13) | 1 of 8 (PR #1) |

- VERIFIED: every commit in the four repos is authored by "BJoozz", either
  `123baoek31@gmail.com` (local commits) or `83776047+BJoozz@users.noreply.github.com`
  (merges and squashes made on GitHub). QUESTION: Bao should confirm that both identities are his.
- VERIFIED: three commits have no trailer but still carry agent-related evidence. V1's PR #8 came
  from a branch named `agent/edit-tools-sidebar`. v2 had an `AGENTS.md` "for coding agents" from
  its second commit (`fc62e5a`, 2026-08-20), and its PRs #1 to #14 all used `agent/*` branches.
  sorting ships an 814-line `AGENTS.md`.
- INFERENCE: a missing trailer does not prove the work had no AI help. QUESTION: which tools
  helped with the commits that have no trailer (all of V1, v2 up to 2026-09-03, tree's first six
  commits, sorting)?

## 2. Test runs I did myself

I ran these on 2026-11-01 between 22:34 and 22:36 (Windows 11, Node v24.17.0, npm 11.13.0).
Each repo's HEAD went through `git archive` into
`C:/Users/123ba/AppData/Local/Temp/fyp-t02/<repo>`, and then I ran
`npm ci --prefer-offline --ignore-scripts`, which took 3 to 10 s per repo. I did not touch the
clones. I ran unit tests only. I did not run lint, the build or the Playwright suites.

| Repo @ commit | Command | Result (VERIFIED) |
|---|---|---|
| V1 @ `5fc06a0` | `npx vitest run --maxWorkers=4` | 24 files, **162/162 passed** |
| v2 @ `c8b14e6` | `npm test` (`node --experimental-strip-types --test`) | **276/276 passed**. A first try before `npm ci` failed 3 files with "Cannot find package 'react'", which was the environment, not the code. |
| tree @ `46ce0a7` | `npx vitest run --maxWorkers=4` | 90 files, **664/664 passed** (33 s) |
| sorting @ `9236a65` | `npx vitest run --maxWorkers=4` | 18 files, **334/335 passed, 1 failed** |

The sorting failure comes from the locale, not from a sorting algorithm. VERIFIED:
`src/components/Metrics.test.tsx` expects `"Done · 1,234 ops"`, but `Metrics.tsx` calls
`toLocaleString()` without a locale, and this PC's ICU locale is `vi-VN`, so the output is
`"1.234"`. Setting `LANG`/`LC_ALL` did not change Node's locale on Windows. INFERENCE: the test
would pass under an en-US locale (not checked).

The GitHub Actions record, which I read with `gh run list` and did not run myself, is VERIFIED:
V1's "Quality checks" run on the push of `5fc06a0` succeeded (lint, unit, build, Playwright), and
v2's "CI" run on the push of `c8b14e6` succeeded (lint, two `tsc`, unit, build, `git diff --check`,
and a Playwright job). tree and sorting have no `.github` folder, so they have no CI.

## 3. graph-algorithm-visualizer (V1)

**What it is (DOCUMENTED, README.md, 117 lines).** It is "a React + TypeScript + Vite mini project
for building weighted graphs and visualizing BFS, DFS, Dijkstra, Maximum Flow, and Kruskal's
algorithm". It uses React Flow for rendering and d3-force for Auto Layout and Live Layout, and the
visuals are described as "CSAcademy-inspired". Its docs are `docs/ARCHITECTURE.md` (338 lines,
"Architecture and Invariants", invariants 1 to 9) and `docs/DEVELOPER_GUIDE.md` (541 lines). It
has no DESIGN_DECISIONS and no AGENTS.md (VERIFIED). VERIFIED: the package name in
`package.json` is `js-ts-learning`.

**Stack (VERIFIED, package.json).** React 19.2, TypeScript ~6.0, Vite 8, `@xyflow/react` 12.11
and `d3-force` 3. It uses ESLint 10, Vitest 4.1 and Playwright 1.62. At HEAD it has 70 non-test
TS/TSX files (8,350 lines), 3,121 test lines and 2,006 CSS lines (counted with `wc -l`, which
includes blank lines).

**Architecture (DOCUMENTED, ARCHITECTURE.md; file names VERIFIED).** `App.tsx` owns the graph
across two modes, Edit and Run. In Edit Mode, `EditableGraph` runs editing and the d3-force live
layout. In Run Mode, a separate read-only `GraphView` shows the algorithm. Both render through
one `GraphCanvas` (React Flow), using the custom `CsaGraphNode` and `CenteredGraphEdge`. The
algorithms (`bfs`, `dfs`, `dijkstra`, `edmondsKarp`, `kruskal`, with pure engines for flow and
Union-Find) generate typed `VisualizationStep[]` snapshots. `App` wraps them in a typed
`VisualizationSequence` (`kind`, `runId`, `steps`). The algorithm-agnostic
`VisualizationPlayer` "controls time", and each algorithm has its own `*RunView` that draws its
panels.

**Features (DOCUMENTED, README).** It offers text or canvas editing, directed or undirected
graphs and non-negative weights, where an omitted weight is a hidden zero. It has Auto and Live
layout, pinned nodes, three samples per algorithm and a one-step undo. Playback has a scrubber, a
speed of 0.05 to 1 s per step and keyboard shortcuts. Edmonds-Karp shows a residual view and a
final minimum-cut proof. Kruskal handles both a spanning tree and a spanning forest. There is
also a fullscreen Run Mode.

**Tests (VERIFIED).** It has 24 unit test files (`src/**/*.test.ts[x]`) and 1 Playwright file
(`e2e/app.e2e.ts`, with 4 `test(` calls). Vitest was added in `788af81` (2026-07-31), and
Playwright and CI (`.github/workflows/quality.yml`) were added in `b0bb316` (2026-08-12). The
large graph inputs are in `test-data/`.

**First commit (VERIFIED, `f3a0db8`, 2026-07-28, 32 files, +6,040, of which 3,043 are `package-lock.json`).** It contains the leftovers
of the Vite React template (`src/assets/hero.png`, `react.svg`, `vite.svg`, `public/icons.svg`,
`favicon.svg`, all still present at HEAD). It also already contains Bao's own working app:
`App.tsx` (387 lines), `EditableGraph.tsx` (447), `graph.ts` (291, with
`createBfsStepsWithEdges` and `createDfsStepsWithEdges`) and `layout/forceLayout.ts` (109), plus
README and docs. INFERENCE: the app was built on a create-vite scaffold before the first commit.
QUESTION: is there any history before 2026-07-28? The name "js-ts-learning" suggests the project
began as a learning folder.

### V1 milestones

| # | Milestone (branch / PR) | Dates | Hashes | What it added |
|---|---|---|---|---|
| 1 | First version, BFS/DFS (direct to main) | 07-28 to 07-29 | `f3a0db8`, `3b7f552`, `32cd572`, `2c4feaa` | Editor, force layout, BFS/DFS playback with pseudocode and queue/stack ("Complete BFS and DFS visualizer") |
| 2 | Generic visualization framework (`feature/visualization-framework`, PR #1) | 07-29 to 07-31 | `b597ffc` to `f7179a6`, merged `ab3676a` | Generic step model and reusable `VisualizationPlayer`; BFS and DFS migrated; old traversal steps removed |
| 3 | Weighted Dijkstra (`feature/dijkstra-visualization`, PR #2) | 07-31 to 08-03 | 16 commits `652c8bb` to `3bb28c6`, squashed `265d6a7` | Weighted edges and labels, Dijkstra steps and UI, first unit tests, fixed nodes, hidden omitted weights |
| 4 | Parallel edges (`fix/parallel-edges`, PR #3) | 08-05 | `6870064`, squashed `3103aff` | Parallel edges drawn separately |
| 5 | Maximum Flow (`feature/maximum-flow`, PR #4) | 08-05 to 08-08 | 14 commits `1b3fffb` to `198baf5`, squashed `447abc0` | Edmonds-Karp engine and steps, residual network view, flow edge table, speed control |
| 6 | Minimum cut and samples (`feature/minimum-cut`, PR #5) | 08-09 | `244264f`, merged `87566f9` | Minimum-cut step and graph samples |
| 7 | UI polish and fullscreen (`feature/ui-polish`, PR #6) | 08-11 | `25e070a`, merged `4315111` | Fullscreen Run Mode and UI polish |
| 8 | Kruskal and browser tests (`feature/kruskal-visualization`, PR #7) | 08-12 to 08-19 | `b0bb316`, `dd848bc`, merged `2a94a7e` | Kruskal/Union-Find engine and panels, Playwright smoke tests, GitHub Actions workflow, typed run architecture |
| 9 | Editor tools beside the graph (`agent/edit-tools-sidebar`, PR #8) | 08-19 | `11e5a04`, `61e095e`, merged `5fc06a0` (HEAD) | Editor sidebar layout. The PR body is empty. |

VERIFIED: PRs #2, #3 and #4 were squash-merged, and each squash commit's tree is identical to
its branch head (`git diff` is empty). That is why `git log --all` shows 55 commits but `main`
has 24. The other PRs were merge commits.

## 4. sorting-algorithm-visualizer ("Sorting Room")

**What it is (DOCUMENTED, README.md, 87 lines; AGENTS.md, 814 lines).** It is "a one-, two-, or
four-pane, operation-based sorting algorithm visualizer". Its AGENTS.md calls it "a standalone
Sorting Algorithm Visualizer and Comparator ... part of a larger algorithm visualization project,
but ... independent from the graph algorithm visualizer". AGENTS.md also fixes the scope at
exactly eight algorithms and gives a "Current Development Order". The only other doc is
`docs/performance-milestone.md` (156 lines), which covers lazy operation streams and a
repeatable profiler, and says its sample measurements were "captured on 2026-08-13 with Node
v24.17.0". I did not re-run them and do not report them. There is no ARCHITECTURE or developer
guide (VERIFIED).

**Stack (VERIFIED, package.json).** React 19.2, TypeScript 6.0, Vite 8.2, HTML Canvas,
`d3-ease` and `d3-interpolate`. It has no React Flow. It uses ESLint 10 and Vitest 4.1, and has
a `profile` script (`scripts/profile-sorting.mjs`). Size: 26 non-test TS/TSX files (5,983 lines),
4,094 test lines and 1,294 CSS lines.

**Architecture (DOCUMENTED, README).** The algorithms work on private input copies and record
typed delta operations (`compare`, `swap`, `write`, `pivot`, `markSorted`, `auxWrite`, `phase`,
radix bucket moves). They do not know about React, timing or Canvas. A playback engine applies
those operations and reverses them. A comparison controller keeps one global tick and a
playback state for each pane. A presentation-only transition resolver turns the before/after
states into eased frames, and a Canvas renderer draws those frames in a cancellable
`requestAnimationFrame` loop. Fast batches use copy-on-write working state.

**Algorithms (DOCUMENTED, README; module files VERIFIED).** Bubble, Selection, Insertion, Merge,
Quick (Lomuto, last element), Randomized Quick (seeded), Counting (integer range up to 512) and
LSD Radix (base 10). There are 1, 2 or 4 panes on the same input, backward playback, a
fullscreen mode and metrics (compares, swaps, writes).

**Tests (VERIFIED).** It has 18 Vitest files, no e2e and no CI. My run gave 334/335 (section 2).

**History (VERIFIED).** It has one commit: `9236a65`, "Initial sorting algorithm visualizer",
2026-08-19 19:23 +0800, 58 files, +16,083 lines (3,109 of them `package-lock.json`). It contains no template assets, so it is Bao's
own code. DOCUMENTED (prototypes/docs/sorting/AGENTS.md): "history is squashed to a single root
commit - earlier versions are not recoverable". INFERENCE: development started before 08-19,
since the performance doc is dated 08-13. QUESTION: when did the sorting work start, does the
original history still exist anywhere, and why was it squashed?

| # | Milestone | Date | Hash | What it added |
|---|---|---|---|---|
| 1 | Single squashed import | 2026-08-19 | `9236a65` | The whole app: 8 algorithms, comparison panes, Canvas renderer, lazy operation streams, profiler, AGENTS.md, performance notes |

## 5. graph-visualizer-v2

**What it is (DOCUMENTED).** README.md (319 lines): "a React, TypeScript, Vite, React Flow, and
d3-force workspace for editing a graph and playing algorithm visualizations on the same
persistent canvas". The other docs are `AGENTS.md` (415 lines, "mandatory safety and
implementation rules for coding agents"), `docs/ARCHITECTURE.md` (493), `docs/DESIGN_DECISIONS.md`
(577, DD-01 to DD-22), `docs/DEVELOPER_GUIDE.md` (536) and `docs/IMPROVEMENT_BACKLOG.md` (102). The
backlog records a review on 2026-09-03 with "237 tests passing". That is DOCUMENTED only; my own
run at `c8b14e6` gave 276.

**Stack (VERIFIED, package.json).** React 19.2, TypeScript ~6.0, Vite 8.2, `@xyflow/react` 12.11
and `d3-force` 3. It uses oxlint 1.75. Unit tests run on Node's own test runner
(`node --experimental-strip-types --test`), so there is no Vitest, and Playwright is 1.63.
README says Node 22.12 or newer. Size: 112 non-test TS/TSX files (14,487 lines), 8,772 test lines
and 2,936 CSS lines.

**Architecture (DOCUMENTED, README "Architecture" and DD-02/03/10/12).** The state is split
into separate owners:

- `GraphDocument`: semantic nodes, exact edge IDs, directedness and a topology revision.
- `GraphLayout`: positions and pins.
- `VisualizationSession`: one sequence, playback, speed, and the revision captured at Run.
- `GraphPresentation`: a transient overlay derived from the current step.

There is one `GraphCanvas` (React Flow), and it stays mounted through both editing and
playback. Sequences are generated only when Run is pressed. Each algorithm keeps its own
metadata type behind a discriminated union. The residual arcs of Maximum Flow are virtual
presentation edges and never enter the document. d3-force is used only as a synchronous
coordinate calculator (DD-08).

**Algorithms and features (DOCUMENTED, README).** BFS, DFS, Dijkstra, Edmonds-Karp maximum flow
with minimum cut, and Kruskal MST/MSF. The graph text editor is live and two-way, with no Apply
button. There are 31 typed samples, including a 40-node stress test. The virtual board scales
with the node count. The Player Dock has Base time and semantic pacing for each operation, and
a step scrubber. Other features are a collapsible legend on the canvas, a sticky run header,
Flow/Residual views and an edge table with a "Relevant" filter. Out of scope on purpose: V1's
Edit/Run pages, the second canvas, the fixed board tiers, Undo and fullscreen ("Current scope
versus V1 ideas", DESIGN_DECISIONS.md).

**Tests (VERIFIED).** It has 42 unit test files (41 under `src/` and 1 in `tests/`) and 13
Playwright specs in `e2e/` plus `helpers.ts` (27 `test(` lines). The first tests came in
`2a9858a` (08-20), Playwright in `2ece0c6` (PR #2, 09-07) and CI (`.github/workflows/ci.yml`) in
`86762de` (PR #7, 09-08).

**First commits (VERIFIED).** `92fa193` (2026-08-20 13:04, 19 files) is the plain create-vite
React template: `App.tsx` is the counter demo with the hero image and Vite logo. Bao's own work
begins with `fc62e5a` (AGENTS.md, 255 lines, the V2 rules), then `41e1461` (dependencies),
`f6149f1` (the single workspace and canvas, 27 files) and `2a9858a` (the editor and stable force
layout, with the first tests).

### v2 milestones

| # | Milestone | Dates | Hashes | What it added |
|---|---|---|---|---|
| 1 | Scaffold and rules (direct to main) | 08-20 | `92fa193`, `fc62e5a`, `41e1461` | Vite template, AGENTS.md rules, React Flow and d3-force |
| 2 | One workspace, editor, layout | 08-20 | `f6149f1`, `2a9858a` | Toolbar, inspector and Player Dock around one canvas; document commands; drag and force layout; first unit tests |
| 3 | The five algorithms | 08-27 to 08-30 | `f864de7` BFS and session, `37c00d9` live text editor, `ff01dce` DFS and Dijkstra, `df6132b`, `bb3140f` Kruskal, `c5dfb43` Edmonds-Karp | The full algorithm set and its playback |
| 4 | Docs, samples, large graphs | 08-30 to 09-03 | `0f5b49a` docs, `b1c3004` samples, `cd50d47` scrubber, `a8c3e00` large graphs, `e8a73be` backlog | ARCHITECTURE, DESIGN_DECISIONS, DEVELOPER_GUIDE; sample catalog; step scrubber |
| 5 | Review fixes, tests, CI (PRs #1 to #7, `agent/*`) | 09-07 to 09-08 | `e1d59e0` #1 legend and sample caption, `ce0cb7b` #2 test globs and Playwright, `4b12bb4` #3 typed IDs, `0609aea` #4 idle dock, `061f8c2` #5 run-scoped editor, `9110a6f` #6 review fixes, `d9abac1` #7 CI | Tests by glob, browser smoke suite, CI, inspector UX |
| 6 | Inspector and canvas UX (PRs #8 to #14) | 09-10 to 09-11 | `2406a59` #8 resize refit, `db92357` #9 persistence notes (docs), `b0c3d2b` #10 refit fixes, `65161ea` #11 sticky run header, `f2440dc` #12 edges named by endpoints, `2518980` #13 canvas legend, `acc3062` #14 shared pseudocode panel | Today's inspector and legend layout |
| 7 | Last commit (direct to main) | 09-11 | `c8b14e6` | "fix: align inspector edge identity and flow filters". This is the commit VisuAlgo+ copied. |

VERIFIED: PR #5's follow-up fix exists twice. `6a6a13e` (left on `agent/run-scoped-editor-disclosure`)
and `4aff2b3` (PR #6) make the same change. `71be848` is a local sync merge of main into PR #11's
branch.

## 6. Relation: graph-algorithm-visualizer (V1) to graph-visualizer-v2

**Verdict: a rewrite (a redesign in a new repository), not a continuation.** A few V1 pieces were
carried over and adapted.

| Evidence | Label |
|---|---|
| v2 is a separate repository with its own root (`92fa193`, a fresh Vite template, 2026-08-20). It shares no commits with V1. It started the day after V1's last commit (`5fc06a0`, 2026-08-19). | VERIFIED |
| v2 AGENTS.md: "This project is a redesign of the existing Graph Visualizer located in the sibling folder `../js-ts-learning`. The old project is Graph Visualizer V1. V1 is behavior/history reference only", and "Do NOT modify any files under `../js-ts-learning`". | DOCUMENTED |
| V1's `package.json` name is `js-ts-learning`, the folder that v2 names. | VERIFIED |
| DD-01 "V1 is reference material, not a codebase to continue": "Port behavior only after expressing it through V2 ownership boundaries." AGENTS.md lists the "V1 architecture that should NOT be copied": the giant App, the `mode` switch between "edit" and "run", separate edit and run canvases, `GraphView`, the large `EditableGraph`, topology snapshots per step, duplicated ownership, one global CSS file, and eager timeline regeneration. | DOCUMENTED |
| Some files have the same name and part of the same code. After normalising quotes and semicolons, these counts are lines of more than 20 characters that appear in both files: `CenteredGraphEdge.tsx` 41 (V1 has 200 lines), `parallelEdges.ts` 36 (126), `CsaGraphNode.tsx` 7 (49, same structure, renamed CSS classes), `kruskalEngine.ts` 38 (277, the Union-Find code with the same identifiers). The force layout (4 of 135) and the Edmonds-Karp engine (10 of 522) were rewritten. I compared V1 `5fc06a0` against v2 `f6149f1` for the components and against v2 `c8b14e6` for the engines. | VERIFIED (counts); INFERENCE (ported and adapted) |
| Same algorithm set (BFS, DFS, Dijkstra, Edmonds-Karp with min cut, Kruskal) and the same stack family. v2 swapped ESLint for oxlint and Vitest for `node:test`. | VERIFIED |
| VisuAlgo+ `main` (`662e7b3`) never names `graph-algorithm-visualizer` or `js-ts-learning` (`git grep`, 0 hits). V1 reaches VisuAlgo+ only through v2. | VERIFIED (0 hits); INFERENCE (only through v2) |

## 7. tree-visualizer

**What it is (DOCUMENTED, README.md, 190 lines).** It is "a standalone rooted-tree workspace built
with React, TypeScript, Vite, React Flow, and `d3-hierarchy`". It has six workspaces: LCA ·
Binary Lifting, BST, AVL, Min Heap, Trie and Segment Tree. Its docs are `docs/ARCHITECTURE.md`
(588), `docs/DEVELOPER_GUIDE.md` (559), `docs/BACKLOG.md` (875, TV-nn items, created 2026-09-12
with a "496 passing in 66 files" baseline) and `docs/UX_AUDIT.md` (103, dated 2026-09-10). It has
no AGENTS.md and no DESIGN_DECISIONS (VERIFIED).

**Stack (VERIFIED, package.json).** React 19.2, TypeScript ~6.0, Vite 8.2, `@xyflow/react` 12.11
and `d3-hierarchy` 3. It uses oxlint, Vitest 4 with happy-dom 20, and an `analyze` bundle-report
script. Size: 173 non-test TS/TSX files (15,968 lines), 9,468 test lines and 3,597 CSS lines.

**Architecture (DOCUMENTED, ARCHITECTURE.md).** There is one persistent workspace and one
controlled React Flow canvas. The layout pipeline goes in this order:

1. `TreeDocument` (undirected topology) plus the selected root.
2. `orientTreeFromRoot`.
3. Collapse state and the layout orientation.
4. The d3-hierarchy tidy layout.
5. Interpolated layout snapshots.
6. React Flow.

Algorithm playback is a parallel pipeline. A pure typed sequence feeds the generic
`VisualizationPlayer`. From there a presenter gives the `TreeAlgorithmOverlay`, and an optional
`TreeViewProjection` gives temporary topology for insert/delete previews. A preview is committed
only by an explicit **Apply**. The heap uses an ordered-array `HeapDocument` shown both as array
slots and as a complete tree. The segment tree is a derived interval tree.

**Operations (DOCUMENTED, README).** Binary Lifting LCA (with an ancestor table; the simple LCA
engine is kept only as a test oracle), BST Search/Insert/Delete, AVL Inspection/Insert, Min Heap
Insert/Extract Min, Trie Insert/Search, and Segment Tree Build/Range Sum/Point Update/Range
Update. Other features: rerooting, Top-to-Bottom and Left-to-Right layouts, subtree
collapse/expand, animated transitions, sample cases, a collapsible data editor and keyboard
playback shortcuts.

**Tests (VERIFIED).** It has 90 Vitest files (including App integration tests on happy-dom), no
e2e and no CI. My run gave 664/664.

**First commit (VERIFIED, `e687099`, 2026-09-03, 89 files, +10,605, of which 2,000 are `package-lock.json`).** It is Bao's own code with
no template assets: LCA plus BST search, the editor, tidy layout, the player, 15 test files, and
README/ARCHITECTURE/DEVELOPER_GUIDE. Its folder layout mirrors v2 (`editor/`, `visualization/`,
`components/workspace`, `tree/{model,layout,text,adapters,presentation}`), and its playback
modules share code with v2 `a8c3e00` (09-02). Counted as above, `sessionReducer.ts` shares 72
lines (v2 file 191 lines), `useVisualizationSession.ts` 42 (138) and `playbackTiming.ts` 14 (44).
INFERENCE: tree-visualizer was started from v2's architecture and session code. No tree doc
says so. QUESTION: is that right?

### tree milestones

| # | Milestone (branch / PR) | Dates | Hashes | What it added |
|---|---|---|---|---|
| 1 | First version (direct to main) | 09-03 | `e687099` | Tree editor, tidy layout, generic player, simple LCA, BST Search |
| 2 | Five more structures | 09-08 | `015469e` (163 files, +15,149) | BST Insert/Delete, AVL, Min Heap, Trie, Segment Tree |
| 3 | Binary Lifting and unification | 09-10 to 09-12 | `f10d6d1`, `2b9ed00`, `1477cda`, `1e7b076` | Binary Lifting LCA, segment range updates, level-by-level start-up animation (`1477cda`, later the submodule pin), one workspace model |
| 4 | Review fixes (`fix/bst-label-narration`, PR #1) | 09-12 to 09-14 | 14 commits `35aa55b` to `cdacbd0`, merged `a4b6d08` | BST narration by value, dark palette, readable badges, 11.5px text floor, legend swatches, simple LCA kept as test oracle, insert into an empty tree, 31-node readability, `docs/BACKLOG.md` |
| 5 | Editor and polish (PRs #2 and #3) | 09-14 | `b2f3763` #2 collapsible data editor, `b8b0dab` #3 desktop polish | Collapsible editor; workspace labels, timing, legends |
| 6 | Binary Lifting columns (PR #4) | 09-14 | `540308b`, merged `d4ebca9` | Table built column by column with worked examples |
| 7 | Coverage and accessibility (PRs #5 and #6) | 09-15 | `1080fba` #5, `fb041b9` #6 | BST inspector coverage, error classification; selection ring, radio group, a11y gaps |
| 8 | Playback shortcuts (`feat/playback-shortcuts`, merged locally, no PR) | 09-15 | `1f41ed4` to `8cb871a`, merged `3bf142c` | Space, arrows, Home/End, R; focus rules |
| 9 | Samples and ancestor table (PRs #7 and #8) | 09-17 | `f8ed923` #7, `1ead852` merged `46ce0a7` #8 (HEAD) | Ten-node chain samples; collapsible ancestor table. VisuAlgo+ copied this commit. |

## 8. Where VisuAlgo+ copied each repository

| Source | Copied at | Evidence |
|---|---|---|
| graph-visualizer-v2 | `c8b14e6` (its HEAD) | DOCUMENTED: `prototypes/docs/graph/AGENTS.md` lines 20-22 ("this copy was taken at commit `c8b14e6`"). VERIFIED: the main repo's submodule `prototypes/graph-visualizer-v2` was pinned at `c8b14e6` in `986deba` (2026-09-13, BJoozz). The first copy `0073875` (2026-09-20, BJoozz, Fable 5.1 trailer, "built on a copy of the graph-visualizer-v2 submodule") has `describeEdge.ts` and `maximumFlowEdgeRows.ts`/`.test.ts`, the files changed only by `c8b14e6`, byte-identical to `c8b14e6` and not to `acc3062`. Overall 143 of 173 `src` files are identical against `c8b14e6`, compared with 140 against `acc3062`. |
| tree-visualizer | `46ce0a7` (its HEAD) | DOCUMENTED: `prototypes/docs/tree/AGENTS.md` lines 21-26, and the message of `7b16bf3` ("taken at BJoozz/tree-visualizer 46ce0a7; the submodule pointer stays at 1477cda"). VERIFIED: the submodule was pinned at `1477cda` (`986deba`). The first copy `7b16bf3` (2026-09-22, BJoozz, Fable 5.1 trailer) contains `BinaryLiftingTable.toggle.test.tsx`, which exists only from PR #8, identical to `46ce0a7`. The number of identical `src` files rises with every earlier candidate and peaks at `46ce0a7` (225 of 289; `1477cda` gives 138). |
| sorting-algorithm-visualizer | `9236a65` (its only commit) | DOCUMENTED: `prototypes/docs/sorting/AGENTS.md` lines 30-34. VERIFIED: the submodule was pinned at `9236a65` in `e7a44f9` (2026-09-23, BJoozz). The first copy `ee4bb72` (2026-09-25, BJoozz, Opus 5 trailer) has 33 of 45 `src` files identical. |

The rest of the copy history is VERIFIED. The three submodules were removed in `0394b64`
(2026-10-18, author "Kerk Tai Heng", Claude Opus 5.5 trailer, "Keep V10 only: one app in
prototypes/"). Today, in `main` at `662e7b3`, the share of each source that is still
byte-identical, with paths mapped `src/` to `prototypes/src/<module>/`, is graph 53 of 173, tree
88 of 289 and sorting 17 of 45. I also checked a few files with `git diff --no-index`: sorting
`input/generateInput.ts` and graph `graph/layout/forceLayout.ts` are identical, while tree
`algorithms/trie/createTrieSequence.ts` differs by 7 lines. DOCUMENTED: the prototype docs record
these changes as deliberate departures, and I did not audit them here. QUESTION: who decided on
and carried out the submodule removal in `0394b64`? The author field says Kerk.

## 9. Questions for Bao

1. Are both BJoozz identities (`123baoek31@gmail.com` and `83776047+BJoozz@users.noreply.github.com`) yours?
2. V1 is named `js-ts-learning` and its first commit already holds about 3,000 lines besides the lockfile, including
   BFS and DFS. Was there earlier history, and what is the scaffold's origin?
3. Sorting was squashed into `9236a65` on 2026-08-19, but its doc is dated 2026-08-13. When did
   that work start, and does the original history exist?
4. Which AI tools or agents helped on the commits without trailers (V1, v2 before 09-07, tree's
   first six commits, sorting)? Who wrote the AGENTS.md files?
5. Did tree-visualizer start from v2's code (the shared session/reducer lines in section 7)?
6. Why was the tree submodule pinned at `1477cda` while the prototypes copied `46ce0a7`?
7. The sorting test `Metrics.test.tsx` fails under a vi-VN locale. Is this known? (VERIFIED: VisuAlgo+
   `main` does not contain that assertion; `git grep "1,234 ops"` finds nothing under `prototypes/`.)
8. Who decided on the submodule removal (`0394b64`, authored by Kerk)?
