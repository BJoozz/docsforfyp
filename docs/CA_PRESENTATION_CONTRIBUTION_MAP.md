# Technical contribution map — broader presentation review

Updated 15 November 2026. Code snapshot: [main at 346e84b](https://github.com/BJoozz/visualgo-plus-design/commit/346e84b838e87ae8affacdc54f0e0eb75eab1529).

## Review conclusion

The earlier three suggested cases (one-canvas graph playback, sorting comparison, floating text) were a presentation shortlist, not an inventory of the work. They omitted substantial contributions, especially the V10 panel-group shell, site integration, tree operation semantics, algorithm correctness and validation.

Use a **breadth overview followed by selected depth**. The [graph case](CA_PRESENTATION_GRAPH_CASE.md) remains useful as a backup/deep-dive draft; its 2–3 minute allocation is no longer assumed to be the final main-deck structure.

## Evidence scope and attribution

- Historical attribution and project-wide inventory: [C1–C14 contribution evidence](../02_contribution_evidence.md), [architecture](../03_architecture_and_decisions.md), [timeline](../01_scope_and_timeline.md). These describe the earlier audit snapshot, not today's test counts or coverage.
- Current review: main source tree; 70 recent commit entries; detailed messages and selected patches of decimal arithmetic, Prim batching, recursive DFS notes and graph navigation commits; selected shared-layout, sorting, tree-session and note-dispatch code.
- This is a broad evidence review, not a line-by-line audit of every repository or a fresh test execution. Historical attribution not re-established from every original commit is identified through the existing evidence record.
- Code inherited from Bao's own standalone graph, tree and sorting repositories remains part of his contribution. “Inherited into this repo” does not mean “implemented by someone else.”
- Credit Kerk's design system/wireframes, engine foundation, one-app consolidation and CI, and distinguish joint design decisions from who implemented them. Do not reduce the role split to “Bao: frontend; Kerk: backend”: Bao also built TypeScript algorithm execution and substantial site/shell integration.
- Do not claim that every line was written manually; the existing evidence record documents AI-assisted work under the owner's direction.
- The engine integration experiment is historical, unmerged work, not a delivered WASM integration.

## 1. Contribution inventory, grouped for presentation

| Group | Work and technical substance | Evidence and attribution | Presentation role |
|---|---|---|---|
| **A. Visualization foundations** | Graph V1 → V2 redesign; canonical graph data, independent layout, reproducible sessions and derived presentation; live editor/canvas interaction; tree and sorting foundations. | C1+C2. Graph case checked against current editor, reducer and App. Standalone origins belong to Bao. | Breadth slide; one concise architecture example |
| **B. Reusable V10 layout system** | Tab groups in left/right/bottom regions; join/split/move/resize/collapse; keep canvas mounted; preserve panel inputs; common size resolver, drop acceptance and preview; validated saved layouts. This is a stateful layout system, not just arranging CSS panels. | C4+C6. Historical commits 72450e1, a876206 and integration into three visualizers. Current groupsModel and its 4,000-operation invariant test inspected. Kerk supplied original wireframes and later refinements; some decisions joint. | **Main technical story** |
| **C. Website and visualizer integration** | Functional site and catalogue, routes/deep links, host-chrome adapters, integration of actual visualizers with shared UI, later algorithm navigation/search. | C5; site implementation built on Kerk's design system. Single app consolidation/current CI mostly Kerk (C14). Recent 5c1aea9 inspected. | Shared architecture and breadth slide |
| **D. Algorithm execution and correctness** | Browser TypeScript algorithm implementations, typed phases, algorithm-specific state, pseudocode and inspectors; recursive DFS, Bellman-Ford, Prim, topological methods, bipartite methods and cut vertices/bridges; stable edge IDs for multigraph behaviour. | C7 plus C1 foundations; historical independent-oracle tests in C7. More than drawing an existing engine's output. | Breadth plus one deep example/backup |
| **E. Tree operation semantics** | BST/AVL searches and mutations, rotations; min/max heap operations; LCA preprocessing/query and ancestor inspection; lazy segment-tree propagation; previews and final Apply for mutating operations; operation-context invalidation. | C2+C8. Current sequence files exist; useContextualVisualizationSession inspected. Detailed historical operation and property-test evidence in C8. | Give Tree explicit visibility; select one demo |
| **F. Sorting execution and comparison** | Eight generator-based algorithms; 1/2/4 panes; same input and shared clock with separate pane state; Study/Compare; future buffering, eager priming cap, retained history and exact seeking. | C2+C9. Current operationBuffer and comparisonPlayback inspected. Future buffer 2,048 per run; aggregate eager cap 60,000; history not globally bounded. | Main story or focused demo |
| **G. Explainable algorithm steps** | Floating text, verdicts for unchanged states, pseudocode linkage, meaningful step grouping, edge motion, paused focus, final recap and reduced-motion behaviour; placement aware of nodes/badges/labels. | C10+C11, plus recent note and Prim changes. Latest dispatch has notes for Dijkstra, Bellman-Ford, Prim, BFS, stack DFS and recursive DFS; this does not mean every frame has a note. | **Main technical story**, linking algorithm knowledge to learning design |
| **H. Reliability and validation** | State-machine checks, seeded properties/independent oracles, layout invariants, regression tests, numerical semantics, producer failure handling, keyboard/viewport fixes and review-driven corrections. | C13 and recent commit evidence. Historical test passes stay dated; no fresh pass claim from this review. | Weave into each story and evaluation slide |
| **I. Exploration and teaching-content adaptation** | Six V2/V7 implementations, movement to V10, engine integration spike; adaptation of original examples and lecture content, formative trial. | C3+C4+C12. Attribute original teaching material; separate parked experiments from shipped work. | Methodology, timeline and backup |

These nine groups reorganise C1–C14 for communication; they are not nine independent inventions and should not be added up as a novelty score.

## 2. Important omitted technical depth

### V10: a reusable layout engine

The previous shortlist missed the strongest shared-system case.

- Pure operations maintain panel/group invariants.
- Geometry resolution is reused by display and allowable drops.
- Layout changes must preserve the central canvas and panel state.
- Stored layouts need validation and recovery.
- Current tests contain a seeded 4,000-step operation sequence checking invariants.

Sources: [prototypes/src/shared/components/layout/groupsModel.ts](https://github.com/BJoozz/visualgo-plus-design/blob/346e84b838e87ae8affacdc54f0e0eb75eab1529/prototypes/src/shared/components/layout/groupsModel.ts); [prototypes/src/shared/components/layout/groupsModel.test.ts](https://github.com/BJoozz/visualgo-plus-design/blob/346e84b838e87ae8affacdc54f0e0eb75eab1529/prototypes/src/shared/components/layout/groupsModel.test.ts). Historical ownership and alternatives: C6.

### Tree: state-changing operations, not another graph drawing

A tree mutation has intermediate states that must be inspectable without committing each animation frame to the input. Context keys prevent a run being reused for a different operation/input context. Heap, AVL and lazy segment tree each add semantic requirements; LCA combines preprocessing and query views.

Source inspected: [prototypes/src/tree/editor/useContextualVisualizationSession.ts](https://github.com/BJoozz/visualgo-plus-design/blob/346e84b838e87ae8affacdc54f0e0eb75eab1529/prototypes/src/tree/editor/useContextualVisualizationSession.ts). Operation implementations and historical evidence: C8. A dedicated tree deep-dive is still needed before choosing its final demo.

### Sorting: comparison semantics and memory trade-offs

Current source explicitly retains history, caps future buffering, and primes producers round-robin under an aggregate budget so pane histories do not become unnecessarily unbalanced. Seeking backwards reconstructs the selected state from retained operations. Failed panes must not be shown as completed or ranked as successful.

Sources: [prototypes/src/sorting/comparison/operationBuffer.ts](https://github.com/BJoozz/visualgo-plus-design/blob/346e84b838e87ae8affacdc54f0e0eb75eab1529/prototypes/src/sorting/comparison/operationBuffer.ts); [prototypes/src/sorting/comparison/comparisonPlayback.ts](https://github.com/BJoozz/visualgo-plus-design/blob/346e84b838e87ae8affacdc54f0e0eb75eab1529/prototypes/src/sorting/comparison/comparisonPlayback.ts); commit a677b5b (message inspected).

Do not call this constant-memory execution, or treat equal operation indices as equal CPU time.

### Algorithm correctness and educational representation

Examples worth developing:
- Cut-vertex/bridge traversal must distinguish parallel edges by identity.
- A topological failure should communicate why no ordering exists.
- Lazy propagation must distinguish stored values, pending tags and effective results.
- Floating-point arithmetic can change decisions, not only formatting.
- A logical algorithm action may be better explained by grouped frames than one frame per low-level event.

The existing C7/C8 evidence supports the first three; current arithmetic and Prim patches support the latter two. Do not claim invention of the standard algorithms.

## 3. Changes after the submitted report / earlier audit

Keep these distinct from what the report already described.

| Change | Evidence reviewed | Meaning for presentation |
|---|---|---|
| Broader graph step-note coverage | Current algorithmIntegration.ts; ffdedc3 actual patch; 56a2b5a/db76996 in recent history | The old audit's “only Dijkstra among graph algorithms” statement is stale. Current dispatcher covers six graph sequence kinds. |
| Prim settle split into inspection and atomic enqueue frames | 4d8c5c1 message and selected patch | Explicit design of teaching granularity while retaining separate extract/accept/discard behaviour. |
| Decimal addition in Dijkstra, Bellman-Ford and Kruskal totals | 457ff8b patch and current addAsWritten.ts, clarified by later 7e327e8 | Prevents familiar decimal examples from producing misleading ties/updates. Has documented numerical limits; not arbitrary-precision arithmetic. |
| Graph Editor shortcuts plus grouped searchable algorithm menu | 5c1aea9 message and patch | Navigation design, keyboard behaviour and host integration; DFS shortcut means recursive DFS. |
| Tree pan/zoom cancels queued and active fit requests | 7e8891c, cdb4d9c, a3067a6 messages/history | User interaction takes precedence over automatic layout fitting. Not freshly browser-tested here. |
| Shared controls/keyboard and robust failure states | b85c1e9, 7aa2db5, a677b5b messages/history | Reuse and reliability work beyond adding algorithms. |

Current note dispatch: [prototypes/src/graph/algorithms/algorithmIntegration.ts](https://github.com/BJoozz/visualgo-plus-design/blob/346e84b838e87ae8affacdc54f0e0eb75eab1529/prototypes/src/graph/algorithms/algorithmIntegration.ts). Current numerical policy: [prototypes/src/graph/algorithms/addAsWritten.ts](https://github.com/BJoozz/visualgo-plus-design/blob/346e84b838e87ae8affacdc54f0e0eb75eab1529/prototypes/src/graph/algorithms/addAsWritten.ts).

Detailed commits:
- [Prim frames](https://github.com/BJoozz/visualgo-plus-design/commit/4d8c5c18860c15973fbfd0e208be2bffa08856d9)
- [Recursive DFS notes](https://github.com/BJoozz/visualgo-plus-design/commit/ffdedc3a5389be7e55ead3fce8bea0acd28751e7)
- [Decimal arithmetic](https://github.com/BJoozz/visualgo-plus-design/commit/457ff8b66d6a508227c96942ebdbf50f70bb9150)
- [Graph navigation](https://github.com/BJoozz/visualgo-plus-design/commit/5c1aea95e9fd6355a505c69feaa7febc60cd279e)

## 4. Revised presentation recommendation

Working proposal, not a final agreed allocation.

**First show breadth, then select depth.** Use a single overview slide showing three layers:

1. Shared platform: V10 shell, site integration and reusable controls.
2. Visualization and execution: Graph, Tree and Sorting with distinct state/operation needs.
3. Explanation and quality: meaningful steps, contextual feedback and validation.

For the approximately nine-minute personal technical section:

| Time | Content |
|---|---|
| 1 minute | Contribution overview; identify Graph, Tree, Sorting and shared shell/site work |
| 2 minutes | V10 shared layout: problem, invariant/geometry design, one visible interaction |
| 2 minutes | Visualization execution: short graph state example and one Tree mutation example |
| 2 minutes | Sorting comparison and its execution/seek trade-off |
| 2 minutes | Meaningful algorithm steps with one example, plus correctness/validation evidence |

This timing is a draft to rehearse. Demo/evaluation in the shared section can carry more examples; do not repeat full demonstrations in every slot.

Backup candidates:
- Full graph state/playback script already written.
- Heap/AVL/lazy-tree operation semantics.
- Independent oracle testing and numerical edge cases.
- Detailed shell constraints and layout persistence.
- WASM integration experiment (explicitly not shipped integration).

Do not expand the talk by explaining every feature. The point is to let the assessor see the scope first and then judge selected technical decisions.

## 5. Next preparation step

Before drafting more isolated scripts:
1. Review this map and choose the final main stories.
2. Prepare the contribution-overview slide.
3. Develop the V10 shell case with exact alternatives and invariant evidence.
4. Give Tree an explicit example rather than leaving it implicit under Graph.
5. Retain the graph case as reusable material; shorten it if used in the main deck.

No source code was changed by this review.
