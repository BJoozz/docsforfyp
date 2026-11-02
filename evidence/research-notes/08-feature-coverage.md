# 08 - Feature and algorithm coverage on main, and when each arrived

Evidence audit for Bao's FYP report. Repository `kerktaiheng/visualgo-plus-design`, `main` at `662e7b3` (2026-10-31). Written 2026-11-01. Read-only: nothing in the repository, the four clones or the two worktrees was changed (`git status` stayed empty in the repository and the four clones; the two worktrees were already empty on disk, see section 2).

Labels: **VERIFIED** (I saw it in code, a diff, a log or a test run), **DOCUMENTED** (a doc, commit message, PR body or code comment says it; I did not check it against code), **INFERENCE** (my reading), **QUESTION** (needs Bao, listed in section 11).

## Summary

- What a visitor gets on main: one site (`prototypes/src/site`) with 12 cards that open and 18 "soon" cards. Behind them are three visualizers: graph (11 algorithm ids), tree (7 workspaces: LCA Binary Lifting, BST, AVL, Binary Heap, Trie, Segment Tree, Segment Tree (lazy)) and sorting (8 algorithms, in Study and Compare modes). VERIFIED.
- **Inherited** from Bao's standalone repositories. Each was copied unchanged in its first commit here (for sorting, all but three drawing files) and has been changed here since. Graph: BFS, stack DFS, Dijkstra, Edmonds-Karp and Kruskal. Tree: LCA Binary Lifting; BST Search, Insert and Delete; AVL Inspection and Insert; Min-Heap Insert and Extract Min; the eager Segment Tree (Build, Range Sum, Point Update, Range Update); Trie Insert and Search. Sorting: the eight algorithms, with 1, 2 or 4 panes and fullscreen. VERIFIED.
- **Built in this repository**:
  - Graph: recursive DFS, Bellman-Ford, Prim, Topological Sort, Bipartite Graph Check and Cut Vertex & Bridge.
  - Tree: Find Min/Max, Predecessor/Successor, Lower Bound, Select, the three traversals and AVL Delete; the Binary Heap's Min/Max order and its seven new operations; the lazy Segment Tree; LCA as two runs, with hover.
  - Sorting: Study and Compare modes, Pseudocode and the scrubber.
  - Shared: every e-Lecture deck, the Settings menu, the theme switch, the Shortcuts dialog, and the UI capabilities in section 9.
  - Exceptions in section 9, inherited in whole or in part: the graph's canvas legend, Live force layout, the tree's badges, the sample presets, the tree's playback shortcuts and sorting's fullscreen. The theme tokens come from Kerk's design system.
  - Evidence: VERIFIED. I grepped each clone at the copied commit and found none of these features there.
- Authors: of the 78 feature commits traced here, 72 are by `BJoozz <123baoek31@gmail.com>` and 6 by `Kerk Tai Heng <taihengkerk@gmail.com>`. 76 of the 78 carry a `Co-Authored-By: Claude ...` trailer. VERIFIED.
- Tests I ran myself on a copy of `662e7b3` (2026-11-01): graph node suite 654/654 pass; vitest 2619/2619 pass in 235 files. I did not run the browser (Playwright) suite. VERIFIED.

## 1. Method

- **Current features.** I read the registries on main:
  - `src/site/modules.ts` (cards) and `src/site/App.tsx` (routes);
  - `src/graph/algorithms/algorithmIntegration.ts` and `algorithmMethods.ts`;
  - `src/tree/algorithms/catalog.ts`, `src/tree/app/workspaceModes.ts`, and the heap, segment, lazy and trie `catalog.ts` files;
  - `src/sorting/app/sortingCatalog.ts`;
  - the three e-Lecture slide files and the three keyboard-shortcut lists.
- **Arrival.** For each feature I found the first commit that added its main file or identifier:
  - `git log --reverse --diff-filter=A` on the file, or `git log --reverse -S <identifier> -- prototypes`;
  - then how that commit reached main. I mapped each first-parent merge's `p1..p2` commits. A commit that sits on main's first-parent line came with no merge commit.
- **Unification commit.** `0394b64` (Kerk, PR #20, 2026-10-18) shows as the commit that "added" every `prototypes/src/...` path. Its diff is 924 renames, 2575 deletions and 7 new files (VERIFIED). So I traced each feature back through the old folders: `prototypes/graph-visualizer-split-rails`, `-docks` and `-groups`, the tree and sorting equivalents, and `visualgo-web-*`.
- **Inherited or built here.** I compared the files of the first copy here with the clone at the copied commit (blob hashes). I also grepped the clone at that commit for each feature.
- **Dates.** Dates are git author dates, in the author's own time zone (+07:00 or +08:00 here). PR dates in `prs.txt` are GitHub's and can fall one day earlier.
- **Line counts.** Before 2026-10-18 every change was made in two or three copies of each visualizer, plus docs. So diff sizes from that time are inflated and are not a measure of effort. INFERENCE from the file lists.

## 2. Tests I ran (2026-11-01, Node v24.17.0)

I ran these on a `git archive 662e7b3` copy under `%TEMP%\fyp08\extract`, outside the repository. A junction pointed the copy at the repository's installed `node_modules`, and a vitest config put the cache inside the copy.

| Suite | Command (in the copy's `prototypes/`) | Result |
|---|---|---|
| Graph algorithms | `node --experimental-strip-types --test "src/graph/algorithms/**/*.test.ts"` | 396 tests, 396 pass |
| Whole graph node suite | `node --experimental-strip-types --test "src/graph/**/*.test.ts"` | 654 pass, 0 fail. The first try, without packages, gave 626/630; all 4 failures were `Cannot find package 'react'` |
| Tree and sorting algorithms, site cards | `vitest run src/tree/algorithms src/sorting/algorithms src/site/modules.test.ts` | 90 files, 1115 tests, all pass |
| Whole vitest suite | `vitest run --maxWorkers=4` | 235 files, 2619 tests, all pass |
| Browser (Playwright e2e) | not run | - |

- The counts 654 and 2619 match PR #37's body ("`npm test` 654 + 2619").
- After the runs, `git status` in the repository was still empty and the repository's `node_modules/.vite` still did not exist. VERIFIED.
- These unit tests check the engines, presentations and catalogs. They do not show that motion, popups or layout look right on screen; that is the job of the e2e suite, which I did not run.
- The two worktrees (`visualgo-engine-v2-experiment`, `visualgo-traversal-ci`) hold no files on disk, only their `.git` pointer file; their folders date from 2026-10-08 and 2026-10-23. `git status` there lists every tracked file as deleted (314 and 2544). I did not cause this: I ran nothing inside them and read their branches through git refs only (`053064f`, `3a6443b`). VERIFIED (state); the cause, perhaps a temp-folder clean-up, is INFERENCE.

## 3. Where the code came from

| Visualizer | Standalone repository (read-only clone) | Copied commit | First copy here | Copy check |
|---|---|---|---|---|
| Graph | graph-visualizer-v2 | `c8b14e6`, also the old submodule pin | `0073875`, 2026-09-20, PR #1 (V2 split rails and V7 docks) | The five engines I checked are byte-identical to the clone. The copy's `src` has 193 files against upstream's 173, the extra ones being the page shell. VERIFIED |
| Tree | tree-visualizer | `46ce0a7` (2026-09-17). The submodule pin `1477cda` is an older ancestor | `7b16bf3`, 2026-09-22, PR #2 | All 106 files under `src/algorithms` are byte-identical to `46ce0a7`. VERIFIED |
| Sorting | sorting-algorithm-visualizer | `9236a65` (2026-08-19), the repository's only commit | `ee4bb72`, 2026-09-25, PR #3 | 32 domain files are byte-identical (`algorithms`, `comparison`, `engine`, `animation`, `input`, and `visualization` except 3 drawing files). VERIFIED |

- **Docs agree.** `prototypes/docs/{graph,tree,sorting}` name the same copied commits. DOCUMENTED.
- **Older graph repository.** graph-algorithm-visualizer (2026-07-28 to 2026-08-19) already had BFS, DFS, Dijkstra, Edmonds-Karp and Kruskal files (VERIFIED from its file list). graph-visualizer-v2 first added those folders between 2026-08-27 and 2026-08-30 (VERIFIED). Whether v2 is a rewrite is a QUESTION (Q6).
- **Inherited engines changed here.** Since the copy, the inherited graph engines were changed by 5 to 28 lines each: BFS 27, stack DFS 23, Dijkstra 28, Kruskal 5, Edmonds-Karp 5 (`diff` line counts against the clone). VERIFIED.
- **Kerk's design system.** `design/design-system` was added by Kerk in `634b5be` (2026-09-03) and already defines the theme names. VERIFIED.
- **Kerk's wireframe.** Added in `69aa8e4` (2026-09-04). VERIFIED.
  - The file `design/wireframes/wireframe 2 viz desktop.html` names e-Lecture (33 times), Pseudocode (33), full screen (3), shortcuts (6), settings (2), theme (2), Save image (4) and legend (3).
  - So these page parts were specified by Kerk and built by Bao. INFERENCE (Q8).

### How commits reached main

| Range on main's first-parent line | Branch | PR |
|---|---|---|
| merges `6a621df`, `495fa73`, `ca56cef`, `9cc009f` | graph, tree and sorting wireframe branches; the site | PRs #1 to #4, with merge commits |
| `9cc009f..ae2f31f`: 33 commits, 2026-09-29 to 2026-10-08 | bj/visualgo-web-editors | PR #6, fast-forward, empty body |
| `ae2f31f..a521c13`: 4 commits, 2026-10-09 | bj/segment-tree-lazy | none |
| `a521c13..c620145`: 7 commits, 2026-10-09/10 | bj/bst-avl-operations | none |
| `c620145..c3f6508`: 44 commits, 2026-10-10 to 2026-10-15 | bj/uiux-pass-1 | none |
| `c3f6508..f510477`: 2 commits, 2026-10-15 | bj/dock-drop-zones | none |
| merges from `fb0b6a9` on | PRs #7 to #37 | merge commits. PR #19 came in through #20; #23 merged into #22's branch; #30 merged into #29's branch and reached main through #31 |
| `3c79d36`, `40a63bd`, `a074f50`, `01a1a4a` | Kerk, pushed straight to main | none |

VERIFIED: each branch head equals its range end, from the first-parent list and `prs.txt`. "None" means `prs.txt` lists no PR for it.

### Authors and AI assistance (facts only)

- Of the 78 feature commits this note cites, 72 are by BJoozz <123baoek31@gmail.com>. Six are by Kerk Tai Heng: `ae63a62`, `0394b64`, `c59c155`, `3c79d36`, `a074f50` and `01a1a4a`. VERIFIED.
- 76 of the 78 carry a `Co-Authored-By: Claude` trailer: Claude Fable 5.1 on 37, Claude Opus 5.5 on 34, Claude Opus 5 (1M context) on 5. The two without one are `aef5d0b` (the Bellman-Ford engine) and `4bd0879` (Prim's contracts). VERIFIED.
- Upstream:
  - graph-visualizer-v2 has 20 Claude trailer lines and tree-visualizer 34.
  - graph-algorithm-visualizer has none.
  - sorting-algorithm-visualizer has none, but it is a single squashed commit, so there is no history to read.
  - In main's commit messages, 10 lines mention Codex (reviews).
  - VERIFIED (counts).

## 4. The site: routes and cards (`src/site`)

- **Routes.** `/`, `/:slug` and `/:slug/:algorithm`; anything else goes to `/` (`src/site/App.tsx`). A card's `formerIds` keep old links working: `dfs` goes to `dfs-stack`, `min-heap` to `binary-heap`. VERIFIED.
- **Where the cards come from.** The header comment of `modules.ts` says three things (DOCUMENTED; I did not check visualgo.net):
  - the 26 visualgo.net cards and their tags are "transcribed from visualgo.net's own homepage table, by way of `design/design-system/ui_kits/visualgo-web/data.js`";
  - `algorithms` is "what the REAL module offers, surveyed from visualgo.net", and `have` is what is implemented;
  - Trie, LCA, Graph Editor and Tree Editor are extra cards.
- **What "full" means.** A card's status counts algorithm *names*, not operations.
- The site was built in the V2 build `87db4a3` and the V7 build `8aeb543` (PR #4, 2026-09-28). The groups build `d445364` (PR #15) later replaced them. Kerk's `0394b64` moved it to `src/site`. VERIFIED.

| Feature (card, route) | Visualizer | Inherited / built here | Commit / PR | Date | Record | Status now (visualgo.net's algorithms per `modules.ts`; ours) | Label |
|---|---|---|---|---|---|---|---|
| Graph Editor `/graph-editor` | graph | built here (our own card) | `cc38942`, PR #6 | 2026-10-01 | site proposal, stage 6 | full, New: all 11 graph ids on one input | VERIFIED |
| Tree Editor `/tree-editor` | tree | built here (our own card) | `cc38942`, PR #6 | 2026-10-01 | site proposal, stage 6 | full, New: LCA, BST, AVL on one tree | VERIFIED |
| Sorting `/sorting` | sorting | card built here | `87db4a3`, PR #4 | 2026-09-28 | - | full: 8 of 8 | VERIFIED |
| Binary Search Tree, AVL Tree `/bst` | tree | card built here | `87db4a3`, PR #4 | 2026-09-28 | TP-15 | full (BST, AVL). It was already "full" on 2026-09-28, when BST had only 3 operations and AVL 2 | VERIFIED |
| Binary Heap `/heap` | tree | card built here | `87db4a3`; full in `ae59183`, `908f8a3` (PR #25) | 2026-09-28; 2026-10-21 | TP-33 | full. It was partial ("Binary Min Heap") until 2026-10-21 | VERIFIED |
| Segment Tree `/segmenttree` | tree | card built here | `87db4a3`, PR #4 | 2026-09-28 | TP-13 | partial: Range Sum (eager and lazy); no Range Min, no Range Max | VERIFIED |
| Graph Traversal `/dfsbfs` | graph | card built here | `87db4a3`, PR #4 | 2026-09-28 | DD-33, DD-60 | partial: BFS, DFS (2 variants), Topological Sort, Bipartite, CVB; no SCC, no 2-SAT | VERIFIED; the plan for SCC and 2-SAT is DOCUMENTED (graph backlog item 19) |
| Single-Source Shortest Paths `/sssp` | graph | card built here | `87db4a3`, PR #4 | 2026-09-28 | DD-38, DD-45 | partial: Dijkstra, Bellman-Ford; "BFS on unweighted" not counted (Q7) | VERIFIED |
| Min Spanning Tree `/mst` | graph | card built here | `87db4a3`; full in `65634cf` (PR #6) | 2026-09-28; 2026-10-05 | DD-39 | full: Kruskal, Prim. It was partial until Prim arrived | VERIFIED |
| Max Flow `/maxflow` | graph | card built here | `87db4a3`, PR #4 | 2026-09-28 | - | partial: Edmonds-Karp only; no Ford-Fulkerson, Dinic or Min Cut entry (the last frame does show a minimum cut, DOCUMENTED in DD-47) | VERIFIED |
| Trie `/trie`, Lowest Common Ancestor `/lca` | tree | cards built here | `87db4a3`, PR #4 | 2026-09-28 | - | full. These are pages visualgo.net has but does not list (DOCUMENTED) | VERIFIED |
| 18 "soon" cards | - | cards built here | `87db4a3`, PR #4 | 2026-09-28 | - | do not open: Array, Bitmask, Linked List and others, Hash Table, Graph DS, UFDS, Fenwick Tree, Recursion Tree, Cycle Finding, Suffix Array, Suffix Tree, Convex Hull, Polygon, Matching, MVC, Steiner Tree, TSP, Reductions | VERIFIED |
| Homepage section for the two editors | site | built here | `5e745b2` (no PR) | 2026-10-12 | - | on main | VERIFIED (commit) |
| Homepage line "experimental version of Prof Halim's visualgo.net, by Kerk and Bao" | site | built here | `ae2f31f`, PR #6 | 2026-10-08 | - | on main | VERIFIED (commit) |

### What the docs say about visualgo.net

All DOCUMENTED. I did not open visualgo.net or the private fork BJoozz/visualgo.

- **BST and AVL.** "The BST and AVL workspaces offer the operations of visualgo.net's BST page" (TP-15).
- **Heap.** "visualgo.net's page is a max heap only; the order switch is this prototype's" (TP-33). TP-33 gives its source as "visualgo.net's heap page (`resources/views/viz/heap.blade.php` in BJoozz/visualgo) and its 50 lecture slides".
- **Lectures.** visualgo.net's lectures fit "a max heap; Remove with frequencies; a segment tree with neither range addition nor lazy propagation, and it has none for Trie or LCA" (TP-14). "Slides that drive the visualization, quizzes and reading progress are not built" (TP-14).
- **Graph samples.** These are "visualgo.net's example graphs, copied from its source: `getExampleGraph` in `public/js/graph_library/helperObjects.js`, and the Max Flow page's own examples in `resources/views/viz/maxflow.blade.php` (the private repo BJoozz/visualgo)" (header of `src/graph/algorithms/visualgoExamples.ts`; DD-48). (Q4)
- **Graph Traversal** (DD-60, Q4):
  - Topological Sort and Bipartite Graph Check get a Method "where visualgo.net runs one in two ways".
  - Topological Sort on a cycle "stops at the evidence ... where visualgo.net discards the run and prints an error".
  - The decks use visualgo.net's "own text where it has one".
- **Training and Login.** Training was never built (site proposal §8). The Login button was later removed by choice 39 (`c59c155`).

## 5. Graph visualizer (`src/graph`)

- **Registry.** `IMPLEMENTED_ALGORITHM_DEFINITIONS` in `src/graph/algorithms/algorithmIntegration.ts`, in toolbar order. VERIFIED.
- **Upstream.** At `c8b14e6` the clone has only the folders `bfs`, `dfs`, `dijkstra`, `kruskal` and `maximumFlow`. So every other algorithm was built here (VERIFIED by its absence there).

| Feature | Visualizer | Inherited / built here | Commit / PR | Date | Record | Status | Label |
|---|---|---|---|---|---|---|---|
| Breadth-first search (Start node, End node) | graph | inherited: v2 `f864de7` (2026-08-27) | `0073875`, PR #1 | 2026-09-20 | upstream DD-19; DD-37, DD-44, DD-45, DD-47 | on main; engine changed here | VERIFIED |
| Depth-first search (stack), id `dfs-stack` | graph | inherited as `dfs` (`ff01dce`, 2026-08-28); renamed here | `0073875`, PR #1; renamed in `4ab075c`, PR #6 | 2026-09-20; 2026-09-29 | DD-33 | on main; old `dfs` links redirect (`65766cc`) | VERIFIED |
| Depth-first search (recursive) | graph | built here | `4ab075c`, PR #6 | 2026-09-29 | DD-33 | on main | VERIFIED |
| Topological Sort, Method DFS or Kahn | graph | built here | `b88952d`, PR #28 | 2026-10-21 | DD-60 | on main | VERIFIED |
| Bipartite Graph Check, Method DFS or BFS | graph | built here | `84c5917`, PR #28 | 2026-10-22 | DD-60 | on main | VERIFIED |
| Cut Vertex & Bridge (DFS num/low; no Method) | graph | built here | `0fc105c`, PR #28 | 2026-10-22 | DD-60 | on main | VERIFIED |
| Dijkstra | graph | inherited (`ff01dce`, 2026-08-28) | `0073875`, PR #1; distances on the nodes `6fc6150` (PR #6) | 2026-09-20; 2026-09-29 | upstream DD-18; DD-32, DD-45, DD-61 | on main; engine changed here | VERIFIED |
| Bellman-Ford (signed weights, negative-cycle witness) | graph | built here ("this prototype's own") | `aef5d0b`, `0aac567`, `6417767`, `eac9fbd`, `e6ce1ac`; PR #6 | 2026-10-03/04 | DD-38; `docs/graph/BELLMAN_FORD_ACCEPTANCE.md` | on main | VERIFIED |
| Maximum flow (Edmonds-Karp) | graph | inherited (`c5dfb43`, 2026-08-30) | `0073875`, PR #1 | 2026-09-20 | upstream DD-13, DD-14; DD-37, DD-47 | on main | VERIFIED |
| Kruskal's minimum spanning forest | graph | inherited (`bb3140f`, 2026-08-28) | `0073875`, PR #1 | 2026-09-20 | DD-37 | on main | VERIFIED |
| Prim's minimum spanning forest (lazy, a queue of edges) | graph | built here ("this prototype's own") | `4bd0879`, `5428ed3`, `686c06b`, `65634cf`, `490e1d1`, `6b1791a`; PR #6 | 2026-10-04/05 | DD-39; `docs/graph/PRIM_ACCEPTANCE.md`; `design/proposals/prim-v2-v7` | on main | VERIFIED |
| Graph editing: Nodes/Edges text, drawing, Directed, Auto layout, pins | graph | inherited (upstream `src/editor`) | `0073875`; became Action's Draw graph (DD-23); made a disclosure in `ae63a62` (Kerk) | 2026-09-20; 2026-10-18 | DD-06, DD-08, DD-23, DD-58 | on main | VERIFIED |
| An omitted weight reads as 1 (replaces upstream DD-07) | graph | built here | `0919126`, PR #6 | 2026-10-01 | DD-36 | on main | VERIFIED (commit); rule DOCUMENTED |
| Layout board 1.3 times upstream's | graph | built here | `867b428`, PR #16 | 2026-10-17 | DD-48 | on main | VERIFIED (commit) |

The record texts are DOCUMENTED. Presence, first commit and landing are VERIFIED.

## 6. Tree visualizer (`src/tree`)

- **Workspaces** (`src/tree/app/workspaceModes.ts`): LCA · Binary Lifting, BST, AVL, Binary Heap, Trie, Segment Tree, and Segment Tree (lazy).
- **Operations.** `src/tree/algorithms/catalog.ts` has 18 ids for LCA, BST and AVL. The heap, segment, lazy-segment and trie catalogs add 9, 4, 4 and 2. VERIFIED.
- **Upstream at `46ce0a7`** had (VERIFIED from the catalogs in the clone):
  - `lca-binary-lifting`;
  - `bst-search`, `bst-insert`, `bst-delete`;
  - `avl-inspection`, `avl-insert`;
  - `heap-insert` ("Min-Heap Insert") and `heap-extract-min`;
  - Segment Tree Build, Range Sum, Point Update and Range Update;
  - Trie Insert and Trie Search.

| Feature | Visualizer | Inherited / built here | Commit / PR | Date | Record | Status | Label |
|---|---|---|---|---|---|---|---|
| LCA Binary Lifting: ancestor table built level by level, then Query | tree | inherited (`f10d6d1`, 2026-09-10) | `7b16bf3`, PR #2 | 2026-09-22 | - | on main | VERIFIED |
| Ancestor table as a step strip under the tree; its own panel, later an "Ancestor table" tab | tree | built here. Upstream's table already existed and could be folded away (`1ead852`) | `00ed4c2`, `303e50b`, `75d0bae`, `b0d099b`; PR #6 | 2026-10-07/08 | TP-04, TP-22 | on main | VERIFIED |
| LCA as two runs, Preprocessing and Query, picked in Action | tree | built here | `e55de1c`; PR #23 into #22's branch, on main through PR #22 (`15c0cc7`) | 2026-10-19 | TP-31 | on main | VERIFIED |
| LCA hover: the path to the root and the 2^k-th ancestors | tree | built here | `60ccc44`, PR #24 | 2026-10-20 | TP-32 | on main | VERIFIED |
| BST Search, Insert, Delete | tree | inherited (`e687099`, 2026-09-03) | `7b16bf3`, PR #2 | 2026-09-22 | TP-15 | on main | VERIFIED |
| AVL Balance Inspection, AVL Insert | tree | inherited (`015469e`, 2026-09-08) | `7b16bf3`, PR #2 | 2026-09-22 | TP-15 | on main | VERIFIED |
| Find Min, Find Max, in grouped operation radios | tree | built here | `c364204` (no PR) | 2026-10-09 | TP-15 | on main | VERIFIED |
| Predecessor, Successor, Lower Bound | tree | built here | `a6c9965` (no PR) | 2026-10-09 | TP-15 | on main | VERIFIED |
| Select(k), with ranks and sizes | tree | built here | `c56eb7b` (no PR) | 2026-10-10 | TP-15 | on main | VERIFIED |
| Inorder, Preorder, Postorder, with a traversal strip | tree | built here | `e7f2fec` (no PR) | 2026-10-10 | TP-15 | on main | VERIFIED |
| AVL Delete, rebalancing up to the root | tree | built here | `9a2f04b`, `c620145` (no PR) | 2026-10-10 | TP-15 | on main | VERIFIED |
| Heap Insert and Heap Extract | tree | inherited as Min-Heap Insert and Extract Minimum (`015469e`) | `7b16bf3`, PR #2; generalised in `7d39c38` (PR #25), renamed in `3fec43c` (PR #26) | 2026-09-22; 2026-10-20/21 | TP-33 | on main | VERIFIED |
| Binary Heap: Min or Max order, 1-based indices, operation groups | tree | built here (visualgo.net is max only, DOCUMENTED) | `7d39c38`, PR #25 | 2026-10-20 | TP-33 | on main | VERIFIED |
| Heap Create in O(N log N) and in O(N) | tree | built here | `0a86739`, PR #25 | 2026-10-20 | TP-33 | on main | VERIFIED |
| Heap Update key(i, v), Heap Delete(i) | tree | built here | `1804565`, PR #25 | 2026-10-20 | TP-33 | on main | VERIFIED |
| Heap Extract K times; Heap sort and Heap sort in-place; output rail; at most 31 items | tree | built here | `3409565`, PR #25 | 2026-10-20 | TP-33 | on main | VERIFIED |
| Heap values follow the Segment Trees' decimal rule | tree | built here | `ea37326`, PR #27 | 2026-10-21 | TP-33 | on main | VERIFIED |
| Segment Tree (sums): Build, Range Sum, Point Update, Range Update | tree | inherited (`015469e`) | `7b16bf3`, PR #2; exact decimal sums in `fc4172d`; typed numbers read as written in `a521c13` | 2026-09-22; 2026-10-09 | TP-13 | on main; sums only | VERIFIED |
| Segment Tree with lazy propagation: the same four operations, plus a push wave | tree | built here | `fc4172d`, `a521c13` (no PR) | 2026-10-09 | TP-13 | on main | VERIFIED |
| Trie Insert, Trie Search | tree | inherited (`015469e`) | `7b16bf3`, PR #2 | 2026-09-22 | - | on main; same scope as upstream | VERIFIED |
| Edges run centre to centre, rim to rim | tree | built here | `499cb42`, PR #22 | 2026-10-19 | TP-30 | on main | VERIFIED |

The TP record texts are DOCUMENTED. TP-15 itself lists upstream's five operations and calls the rest "this prototype's own", which matches the catalog comparison above.

## 7. Sorting visualizer (`src/sorting`)

| Feature | Visualizer | Inherited / built here | Commit / PR | Date | Record | Status | Label |
|---|---|---|---|---|---|---|---|
| Eight algorithms: Bubble, Selection, Insertion, Merge, Quick (last-element Lomuto pivot), Randomized Quick, Counting, LSD Radix | sorting | inherited (`9236a65`, 2026-08-19) | `ee4bb72`, PR #3 | 2026-09-25 | SP-07, SP-11 | on main | VERIFIED |
| 1, 2 or 4 panes on one input with one shared tick; the Counting and Radix scenes | sorting | inherited (upstream README; `type PaneCount` in `App.tsx`) | `ee4bb72`, PR #3 | 2026-09-25 | - | on main: 1 pane is Study, 2 or 4 is Compare (`PANE_COUNTS = [1, 2, 4]`) | VERIFIED |
| Study mode: one pane inside the page shell, with Pseudocode and e-Lecture | sorting | built here | `ee4bb72`, `786b278`; PR #3 | 2026-09-25 | SP-03, SP-12, SP-17 | on main | VERIFIED |
| Compare mode: pane grid, setup strip and per-pane algorithm select; no Pseudocode or e-Lecture; Status table in a collapsed bottom row | sorting | built here on upstream's panes | `eeba29d`, `661a2b2`, `0a915b6` (PR #3); groups version `0e3857f` (PR #15) | 2026-09-25; 2026-10-17 | SP-03, SP-04, SP-09, SP-15 | on main | VERIFIED |
| Pseudocode, with the current line lit for every algorithm | sorting | built here (upstream has no pseudocode) | `ee4bb72`, `3e62f2c`, `c3a9da4`; PR #3 | 2026-09-25/26 | SP-07, SP-10, SP-11 | on main | VERIFIED |
| Scrubber (seeking) and Last | sorting | built here (no seek or scrub upstream at `9236a65`) | `42d1597`, `5ccef45`, `fed2420`; PR #3 | 2026-09-25 | SP-05, SP-06 | on main | VERIFIED |
| Warning when the bars get too thin | sorting | built here | `3c61e81`, PR #3 | 2026-09-27 | proposal U7, U9 | on main | VERIFIED (commit) |
| Fullscreen | sorting | inherited (upstream's Fullscreen API mode, with Escape to leave) | the page shell in `ee4bb72` | 2026-09-25 | - | on main, from the site bar | VERIFIED |
| Paused-step motion, step notes, value popups | sorting | not built for sorting | - | - | - | absent: no `usePausedMotion` and no step notes in `src/sorting` | VERIFIED |

The sorting proposal says the wireframe "contains no multi-pane, comparison or sorting variant ... Compare mode is therefore new design" (`design/proposals/sorting-v2-v7/README.md`, §12). DOCUMENTED.

## 8. e-Lecture decks

- **Upstream had none.** None of the three standalone repositories has an e-Lecture: grepping "lecture" at the copied commits finds 0 files. VERIFIED.
- **The panel** comes from Kerk's wireframe (VERIFIED by the term count in section 3).
- **Slide counts** are the quoted `title:` entries in each slide file (VERIFIED as counts). That one entry is one slide is INFERENCE.

| Feature | Visualizer | Inherited / built here | Commit / PR | Date | Record | Status | Label |
|---|---|---|---|---|---|---|---|
| 11 decks, one per algorithm id, 3 to 5 slides each: 40 slides now | graph | built here | `0073875` (15 slides), PR #1; one deck added with each new algorithm: `4ab075c`, `0aac567`, `686c06b`, `b88952d`, `84c5917`, `0fc105c` | 2026-09-20 to 2026-10-22 | DD-60 item 4: "short" decks, the full decks "a later round" | on main | VERIFIED; plan DOCUMENTED |
| 7 decks, 111 slides now: LCA 10, BST 23, AVL 15, Binary Heap 36, Segment Tree 10, lazy 11, Trie 6 | tree | built here; written "after visualgo.net's" lectures | `7b16bf3` (24 placeholder slides), PR #2; `3a429ad`, `7cfc537` (2026-10-09, no PR); `5e9f0ef`, `c620145` (2026-10-10, no PR); `88e8396` (2026-10-21, PR #25) | 2026-09-22 to 2026-10-21 | TP-14, TP-15, TP-33 | on main | VERIFIED; style DOCUMENTED |
| 1 deck, 9 slides: one shared slide and one per algorithm | sorting | built here | `ee4bb72`, PR #3; tests in `3e62f2c` | 2026-09-25/26 | proposal §6 | on main, Study only | VERIFIED |

On 2026-09-28 the site proposal still called the e-Lecture "placeholder slides" (§8). DOCUMENTED.

## 9. UI capabilities

| Feature | Visualizer | Inherited / built here | Commit / PR | Date | Record | Status | Label |
|---|---|---|---|---|---|---|---|
| Step notes: a step writes its verdict as floating text on the canvas | tree: LCA, every BST and AVL operation, Binary Heap. graph: Dijkstra's relax step | built here | `d82aa18`, `116588e` (PR #29); `7180d81`, `277405c`, `94ec5db` (PR #30 into #29's branch, on main through PR #31); `08590ef` (the shared layer), `157d9a9`, `6b1a4fc` (PR #32) | 2026-10-23 to 2026-10-25 | TP-34, TP-36, DD-61 | on main. None in the Segment Trees, Trie, sorting or the other graph algorithms (grep) | VERIFIED |
| Paused-step motion, switched by "Animate paused steps" in Settings | graph, tree | built here | `7e92baf` (graph), `a8c191c` (tree), `62558bb` (site menu), `0b9e063`, `467d1f7`: all on bj/uiux-pass-1, no PR | 2026-10-12/13 | DD-42, TP-17 | on main; sorting has none | VERIFIED |
| Final-frame motion: a finished run keeps its last frame moving | graph | built here: the last frame keeps moving, for every algorithm. Upstream had final recap waves for BFS, Dijkstra and Max Flow (`bfsFinalWave.ts`, `dijkstraFinalWave.ts`, `maximumFlowBfsWave.ts` at `c8b14e6`) | `be570eb`, `fced77a`; PR #12 | 2026-10-16 | DD-47 | on main. `finalSpread.ts` covers 9 ids; BFS and Max Flow have their own | VERIFIED; "upstream kept its waves to the final recaps" DOCUMENTED (DD-37) |
| Edge waves: the step that examines an edge shows which way it crosses it | graph | built here | `bcbed32`, `c4e597d`; PR #6 | 2026-10-02 | DD-37 | on main for every algorithm; each new algorithm added its own. Kahn's method has no inspection step | VERIFIED (commits, `edgeWaveTravel.ts`); scope DOCUMENTED |
| Value popups (`+7`, `-3`) float off a changed number | tree: both Segment Trees, Binary Heap | built here | `ff77eca` (no PR); `1804565` (PR #25); `ea37326` (PR #27) | 2026-10-13; 2026-10-20/21 | TP-20, TP-33 | on main | VERIFIED |
| End badges: a run ends on a badge that says how it ended (MISS, DONE, NONE) | tree | the badges NOW, MISS, INSERTED and DONE are inherited (grep at `46ce0a7`); the end rule and NONE are built here | `28e08f8` (no PR); `277405c` (PR #31) | 2026-10-13; 2026-10-24 | TP-19, TP-36 | on main | VERIFIED |
| Canvas legend | graph: inherited. tree: Binary Lifting only, built here. sorting: legend stays in the Status panel | graph: upstream DD-13 ("the contextual legend sits on the canvas"; `CanvasLegend` exists upstream). Built here: the see-through legend, the tree's canvas legend, and the shared 12px legend | `f1d9e40`, `c3f6508` (no PR); `1f763dc` (PR #29); `19aaef3` (PR #33) | 2026-10-14/15; 2026-10-23; 2026-10-26 | DD-13 notes, TP-35 | on main | VERIFIED |
| Samples are visualgo.net's example graphs, drawn where visualgo draws them | graph | built here. The sample catalog itself is inherited (upstream DD-15: five to ten typed samples per algorithm); the data was copied from visualgo's source (Q4) | `bc46260`, `174b417`, `32de95c`; PR #13 | 2026-10-16 | DD-48 | on main | VERIFIED (commits, file); source DOCUMENTED |
| Node label fits its node | graph | built here. The tree's own `labelSize.ts` is inherited | `e360df1`, `96f85e2`; PR #14 | 2026-10-16 | DD-49 | on main | VERIFIED |
| SSSP End node: only the run's last frame shows the path | graph: BFS, Dijkstra, Bellman-Ford | built here | `9e6e7bd` (PR #8); `2511937`, `8a5f607` (PR #9) | 2026-10-15 | DD-45 | on main (`ShortestPathAlgorithmId`) | VERIFIED |
| Live force layout | graph | inherited. Upstream starts it on (`useState(true)` at `c8b14e6`) and runs the whole simulation on every frame of a drag | built here: a drag with Live off follows the pointer, `74a4958` (no PR, 2026-10-12); Live starts off, `6b953d5` (PR #10, 2026-10-15); a drag pushes only the nodes it nears, `ae63a62` (Kerk, PR #19 through #20, 2026-10-18) | see commits | DD-43, DD-46, DD-57 | on main: off at start (`useState(false)`, with a DD-46 comment) | VERIFIED; DD-57's "owner" is a QUESTION (Q2) |
| Method control in the run form | graph: Topological Sort (DFS, Kahn), Bipartite Graph Check (DFS, BFS) | built here | `b88952d`, PR #28 | 2026-10-21 | DD-60 | on main (`ALGORITHM_METHODS`) | VERIFIED |
| Action-panel presets: a picker at the top of Action ("Select preset"); the custom data kept for the visit | graph, tree | presets inherited (graph DD-15 samples; tree examples, made buttons in TP-09 at `7b16bf3`). Built here: the picker and the working copies. The "Select preset" label came in Kerk's commit | `5d03867`, `57d0144` (graph) and `04e8836`, `95bf326` (tree), no PR, 2026-10-11; `ae63a62` (Kerk, 2026-10-18) | 2026-10-11; 2026-10-18 | DD-41, TP-16, TP-09, DD-58 item 3, TP-28 | on main | VERIFIED; label's "owner" is a QUESTION (Q2) |
| Settings menu | all, in the site bar | built here; none upstream (grep). Each visualizer first had its own (`0073875`, `7b16bf3`, `ee4bb72`). The site's menu came in `87db4a3` (PR #4). Kerk removed the visualizers' own menus in `c59c155` (PR #21) | see commits | 2026-09-20 to 2026-10-18 | site proposal §6, §9 | on main: Theme (9 themes), Animate paused steps (graph, tree), Reset panel layout | VERIFIED |
| Keyboard shortcuts and the Shortcuts dialog (`?`) | all | tree upstream had playback shortcuts (`usePlaybackShortcuts.ts`); graph upstream had none; sorting upstream had only Escape for its fullscreen overlay. The lists and the dialog were built here | `0073875`, `7b16bf3`, `ee4bb72`; dialog made modal in `65eee09` (PR #2) | 2026-09-20 to 2026-09-25 | TP-05 | on main: Space, Left/Right, Home/End, - and +, F, Shift+F, PageUp/PageDown, ?, Esc; sorting adds Alt+1/2/4 | VERIFIED |
| Themes: Light, Tide, Forest, Clay, Midnight, Abyss, Pine, Ember, Classic | all | the theme tokens come from Kerk's design system (`634b5be`); the switch was built here; graph and tree upstream followed the OS colour scheme (`prefers-color-scheme`) | `0073875`, `37075b1` (PR #1); site `87db4a3` (PR #4); the site owns the theme since `c59c155` (Kerk, PR #21) | 2026-09-20 | DD-28 | on main | VERIFIED |
| Full screen (Shift+F) | all | sorting upstream had it; built here for graph and tree | `0073875` (a footer button); moved beside Settings in `3c79d36` (Kerk, no PR) | 2026-09-20; 2026-10-19 | V10 choice 44 | on main | VERIFIED |
| Panel-groups layout (V10) around a fixed canvas | all | built here by Bao; Kerk deleted the V2 and V7 layouts | `72450e1`, `a876206`, `950ab6f`, `d82a24c`, `0e3857f`, `d445364`; PR #15 | 2026-10-17 | DD-50 to DD-56, TP-21 to TP-27, SP-12 to SP-18 | the only layout since PR #20 | VERIFIED |
| Footer transport: Previous/Next lead, Autoplay and Stop chips, Next starts a run | all | built here. Bao centred the transport (`d6ce97b`, PR #11). Kerk added Autoplay and the chips (`a074f50`, `01a1a4a`, straight to main) | see commits | 2026-10-16; 2026-10-21/22 | DD-24, brought up to date in `9baa117` (PR #37) | on main | VERIFIED |

Presence, commits and landing are VERIFIED. Record texts are DOCUMENTED. I did not check how anything looks on screen.

## 10. Removed, or not on main

| Feature | Visualizer | Inherited / built here | Commit / PR | Date | Record | Status | Label |
|---|---|---|---|---|---|---|---|
| Go (and sorting's Run) button | all | built here | removed in `117975a`, `d431074`, `66c12b8` (no PR); the footer's Play started runs, and Autoplay or Next do now | 2026-10-10 | DD-24 | removed | VERIFIED |
| Save image | all | built here at `0073875` (it is in Kerk's wireframe) | removed, with `html-to-image`, in `3c79d36` (Kerk) | 2026-10-19 | V10 choice 43 | removed | VERIFIED |
| Login button; About · Team · Terms; the homepage's tag-filter toggle | site | from the design-system kit | removed in `c59c155` (Kerk, PR #21) | 2026-10-18 | V10 choices 39 to 41 | removed | DOCUMENTED (PR #21 body, commit message) |
| Homepage tips | site | built here | removed in `40a63bd` (Kerk) | 2026-10-20 | - | removed | VERIFIED (commit subject) |
| V2 split-rails and V7 docks layouts, the standalone pages, the three submodules | all | built here | deleted in `0394b64` (Kerk, PR #20) | 2026-10-18 | - | removed | VERIFIED |
| "Kerk BFS runtime" engine integration | graph | built by Bao on a branch | `478174f` to `ffb9274` on origin/bj/engine-v2-experiment, plus `053064f` on the local bj/engine-package-spike | 2026-09-17 | - | not on main (`git cherry` marks all 4 `+`) | VERIFIED |
| Training, quizzes, slides that drive the visualization | site, all | never built | - | - | site proposal §8, TP-14 | absent | DOCUMENTED |
| SCC and 2-SAT; Range Min and Range Max; Ford-Fulkerson and Dinic | graph, tree | not built | - | - | graph backlog item 19 (SCC and 2-SAT "a later round") | absent from the registries | VERIFIED; plan DOCUMENTED |

## 11. Questions for Bao

1. **Q1 Identity.** Are both `BJoozz <123baoek31@gmail.com>` and `BJoozz <83776047+BJoozz@users.noreply.github.com>` yours? The four standalone repositories use both; every one of your feature commits here uses the first.
2. **Q2 "The owner" in Kerk's commits.** Who made these choices, you or Kerk? Each commit attributes them to "the owner":
   - `ae63a62`: V10 choices 27 to 32. Thin split bands, vector transport, Select preset, Draw graph as a disclosure, push-only Live layout (DD-57), no small text (DD-58, TP-28, SP-19).
   - `c59c155`: choices 33 to 41, DD-59, TP-29, SP-20. One font and one control look; Login and About/Team/Terms removed.
   - `3c79d36`: choices 42 to 45. No Save image; Full screen and Shortcuts beside Settings; a longer speed slider.
   - `40a63bd`: "The owner's request, 2026-10-20".
   - `0394b64`: "The owner's decision of 2026-10-18: V10 wins".
   - A pattern, not evidence (INFERENCE): choices 27 to 45 are quoted in English, while choices 1 to 26 carry Vietnamese quotes with translations.
3. **Q3 "Owner" in your own PR.** PR #37 says "The owner's commit `a074f50` (2026-10-21)", and that commit is Kerk's. Does "owner" mean Kerk there? This audit assumes "owner" means you in your own branches.
4. **Q4 visualgo.net material.** What permission covers the following, and how will the report credit Prof Halim's visualgo.net?
   - The example graphs (DD-48) are "copied from its source" in the private fork BJoozz/visualgo.
   - TP-33 draws on the heap page and its 50 lecture slides.
   - The DD-60 decks use visualgo.net's "own text where it has one".
5. **Q5 Sorting history.** sorting-algorithm-visualizer is a single commit (`9236a65`, 2026-08-19). Do you have its original history, or other dated evidence?
6. **Q6 Graph v2.** Was graph-visualizer-v2 (BFS first added on 2026-08-27) a rewrite of graph-algorithm-visualizer? That repository ran from 2026-07-28 to 2026-08-19 and had the same five algorithms.
7. **Q7 Card status.** Card status counts visualgo.net's algorithm names, not operations: `/bst` was already "full" on 2026-09-28 with three BST and two AVL operations. How should the report state coverage? Is it also intended that the SSSP card does not count BFS, when BFS takes the End node?
8. **Q8 Wireframe.** Kerk's wireframe (`69aa8e4`) already names e-Lecture, Pseudocode, full screen, shortcuts, settings, theme, Save image and a legend. Which page features are your design, and which are your build of Kerk's design?
9. **Q9 No PR.** Four branches reached main with no PR: bj/segment-tree-lazy, bj/bst-avl-operations, bj/uiux-pass-1 and bj/dock-drop-zones, 57 commits in all. PR #6 has an empty body. Is there another review record for this work? The docs mention Codex reviews, for example in TP-14 and TP-15.
10. **Q10 Browser suite.** I did not run the browser suite. PR #37's body reports a "full browser suite 150/150" (DOCUMENTED). Is there a CI run link you can cite?

## Appendix: the read-only commands behind this note (shortened)

```sh
git log main --reverse --diff-filter=A --format='%h %ad %an' --date=short -- "prototypes/*/algorithms/<name>/*"
git log main --reverse --format='%h %ad %an' --date=short -S "<identifier or '## DD-nn: ...'>" -- prototypes
git log --first-parent --merges --format='%h %P' main      # then: git rev-list p1..p2 per merge -> commit-to-PR map
git rev-parse <here>:<path>  vs  git -C <clone> rev-parse <copied>:<path>   # byte-identity of copies
git -C <clone> grep -l -i "<feature term>" <copied commit> -- src          # absence upstream
git show --stat / --shortstat <commit>;  git show <commit>:<path> | grep ...
git cherry -v main <branch>                                               # off-main work
git archive 662e7b3 prototypes/src ... | tar -x   (into %TEMP%; tests run there, never in the repository)
```
