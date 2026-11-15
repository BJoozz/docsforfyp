# Interactive demo and editor positioning

Updated 15 November 2026. Owner-requested additions to the [contribution map](CA_PRESENTATION_CONTRIBUTION_MAP.md) and [preparation notes](CA_PRESENTATION_PREP.md).

## 1. Confirmed presentation direction

The owner wants to explicitly introduce and demonstrate:
- Floating text tied to algorithm decisions.
- Dynamic visual emphasis while playback is paused.
- Interactions and visual feedback on the final frame, including Dijkstra and DFS.
- Graph Editor and Tree Editor as distinct entry points, alongside algorithm-topic cards.
- A broader intended audience: experienced VisuAlgo users and regular competitive programmers who may use the editors to brainstorm, construct examples, inspect ideas and work through a problem.

The “experienced CP users will like/use this” statement is a product hypothesis, not an established user-study result. Present it as “we aim”, “we hope” or “we designed this to support”. The owner's intention is recorded here; no further user evidence is claimed.

## 2. Main message

**From watching algorithms to exploring your own ideas.**

Two complementary workflows:
- **Topic-first:** choose an algorithm/topic, learn its operation and inspect steps.
- **Input-first:** build a graph or tree, arrange it and explore compatible algorithms on that input.

Keep both entry points. The original VisuAlgo already allows custom inputs; the new contribution is the explicit editor entry point and workflow, not the invention of input editing.

Suggested CP use case: construct a small example or counterexample, run an algorithm, inspect a decision, change the example and compare the outcome. This supports thinking about a problem; it is not a general proof assistant or an automatic solver.

## 3. Behaviour checked in source

Source inspection on 15 November 2026; no browser rehearsal or test execution in this preparation.

| Feature | Checked behaviour | Demo boundary |
|---|---|---|
| Graph Editor | Dedicated editor card; opens Draw graph; all supported graph choices accessible within the visualizer; authored input remains while changing algorithms | Interpretations/domains can differ; explain relevant weighted/unweighted or directed/undirected treatment |
| Tree Editor | Dedicated editor card; shared input for Binary Lifting, BST and AVL | Does not expose every tree workspace: Heap, Trie and Segment Tree are separate. An arbitrary tree need not satisfy BST/AVL constraints |
| Floating text | Notes arrive with a forward step and explain a verdict near the relevant element | Select the step by advancing normally; do not assume a large seek or Previous replays the transient note |
| Paused motion | Emphasis may continue while the algorithm frame is frozen; controlled by Animate paused steps and reduced-motion behaviour | A moving edge does not mean the algorithm is still executing; ensure setting permits motion before demo |
| Dijkstra final frame | Hover chooses a temporary path target; leaving restores the configured End node; dragging does not trigger the hover preview | This path inspection is documented for BFS, Dijkstra and Bellman-Ford, not DFS |
| Recursive DFS final frame | DFS tree edges illuminate towards entered vertices in call order; vertex emphasis accompanies the spread | Demonstrate a final traversal recap, not a Dijkstra-style hover path feature |
| Stack DFS final frame | Nodes receive emphasis in visited order | Distinguish from recursive DFS tree-edge recap |
| Binary Lifting while paused/finished | Hover inspects root path and available power-of-two ancestors; canvas, ancestor table and Status share the result | Use as a Tree example if time permits; hover does not advance the session |

## 4. Proposed integrated demo — approximately 4–5 minutes

This replaces a disconnected list of feature demonstrations. Timing is a proposal and needs rehearsal.

| Stage | Action | What to say | Approx. time |
|---|---|---|---:|
| Start from input | On homepage, point out the two editors and open Graph Editor; enter a prepared small weighted graph and arrange one vertex | “We also provide an input-first workflow: start with the example you want to explore.” | 40 s |
| Explain a decision | Run Dijkstra with Next; advance to a relaxation with floating text | “The note explains why the value changes—or why it stays the same—at the place where the decision happens.” | 45 s |
| Pause and inspect | Stay paused on an active step; point to its emphasis and unchanged frame counter | “The algorithm is paused. The motion only keeps the current relationship visible.” | 25 s |
| Explore the result | Go to final Dijkstra frame; hover two vertices, then leave; optionally change End node | “The completed result remains interactive: I can inspect different paths without rerunning the algorithm.” | 40 s |
| Reuse the example | Switch within Graph Editor to recursive DFS on the same authored graph; show final recap | “I can explore another algorithm on the same example. Here the final view recaps the DFS traversal.” | 35 s |
| Tree Editor | Return home and open Tree Editor with a valid prepared tree; demonstrate an LCA query and paused/final ancestor hover | “The same input-first idea also supports tree exploration.” | 55 s |
| Connect to users | Briefly describe making a small example/counterexample during CP practice | “Our aim is to make this useful both for learning and for working through an idea.” | 20 s |

Keep sorting comparison and the V10 layout demonstration in their own technical slots, or replace a stage if the combined demo exceeds the allocated time. Do not silently add this on top of an already full 45-minute schedule.

Rehearsal checklist:
- Prepare exact input and target Dijkstra steps.
- Make sure the notes appear at the selected speed and fit the shared-screen size.
- Verify Animate paused steps, reduced-motion setting and final-frame behaviour.
- Keep a stable frame-counter reference when explaining paused motion.
- Check graph interpretation notices after switching algorithms.
- Use a valid LCA tree; demonstrate BST/AVL only with valid input for those operations.
- Capture a backup recording after a successful rehearsal.

## 5. English script — editor positioning

Alongside the algorithm pages, we added dedicated Graph Editor and Tree Editor entry points.

The idea is to let users begin with their own example. Instead of first choosing a topic, they can build a graph or tree, arrange it, and explore the algorithms supported by that editor.

We hope this will also be useful for experienced users, especially people who regularly practise competitive programming. When working on a problem, they often draw a small example, test an idea, or look for a counterexample. We want the editors to support that process by making those examples easy to construct, inspect and revise.

During execution, floating text explains decisions directly on the drawing. When playback is paused, visual emphasis can keep the current node or edge clear without advancing the algorithm. Some completed results also remain interactive—for example, hovering over a vertex after Dijkstra shows its path from the source.

Our aim is for VisuAlgo+ to support both learning an algorithm and thinking through a problem using an example of your own.

## 6. Technical explanation to connect to the demo

- Floating text: semantic verdict → per-algorithm note writer → shared placement/timing layer.
- Paused motion: algorithm progression and visual emphasis have different lifecycles.
- Final-frame inspection: query recorded results and derive a temporary presentation without rerunning or editing the graph.
- Editors: reusable visualizer and shared input, with routing/navigation that does not force a new topic page for each algorithm.
- Tree hover: the same inspection result feeds canvas, ancestor table and Status consistently.

These features belong in the technical contribution discussion, not only as visual polish. Their intended usefulness still needs user evaluation.

## 7. Sources

- [Module definitions and editor scope](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/src/site/modules.ts)
- [Graph App: hover target, editor entry and session composition](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/src/graph/app/App.tsx)
- [Final-frame plans: recursive DFS, stack DFS and Dijkstra](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/src/graph/algorithms/finalSpread.ts)
- [Tree architecture: state ownership and Binary Lifting hover](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/docs/tree/ARCHITECTURE.md)
- [Contribution evidence: C5, C10 and C11](../02_contribution_evidence.md)

Status: owner intent captured; source behaviours checked; script/demo proposed; live rehearsal pending.
