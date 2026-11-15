# CA presentation — prototype evidence and remaining drafts

Updated 16 November 2026. Presentation drafts for Bao and Kerk. The working timing is 33 minutes of presentation in a 45-minute slot. Bao has 3 minutes for Early Design and 8 minutes for Algorithm Visualizers. The joint Demo & Evaluation has 5 minutes, and Future Work has 2 minutes. Timing and selection of examples are rehearsal proposals.

## 1. What the standalone prototypes established

| Prototype and recorded milestone | Interaction explored | What carried forward |
| --- | --- | --- |
| **Graph prototype 1, late July–August.** It began with graph editing, force layout and BFS/DFS with pseudocode and queue/stack views. The July 29–30 refactor moved traversal playback to a generic player. Dijkstra, parallel-edge rendering, flow/min-cut and Kruskal followed. | Users could provide a graph and follow multiple algorithms with reusable controls. Editing and running used separate canvas instances built around common rendering components. Keeping their viewport and rendering behaviour aligned became a recurring design concern. | The interaction and visualization lessons informed the second Graph prototype. [Initial commit](https://github.com/BJoozz/graph-algorithm-visualizer/commit/f3a0db8) · [Generic player](https://github.com/BJoozz/graph-algorithm-visualizer/commit/4b91c13) · [V1 architecture](https://github.com/BJoozz/graph-algorithm-visualizer/blob/5fc06a0/docs/ARCHITECTURE.md#invariant-1-one-rendering-pipeline) |
| **Standalone Graph Visualizer V2, August–September.** The unified workspace was committed August 20, followed by the playback session and live, bidirectional text editing. | Users could move between editing and playback on a persistent canvas. The graph document, layout, session and step presentation had distinct owners, so positions could change independently of the input used for a run. | This standalone repo became the Graph foundation in both September layout builds and eventually in V10. [Unified workspace](https://github.com/BJoozz/graph-visualizer-v2/commit/f6149f1) · [Live editor](https://github.com/BJoozz/graph-visualizer-v2/commit/37c00d9) · [Design decisions DD-01–DD-06](https://github.com/BJoozz/graph-visualizer-v2/blob/c8b14e6/docs/DESIGN_DECISIONS.md#dd-01-v1-is-reference-material-not-a-codebase-to-continue) |
| **Sorting Room, first published commit August 19.** One, two or four panes, eight algorithms and a canvas renderer. The single squashed commit already contains the operation-stream implementation. | All panes received the same input and advanced one logical operation per shared tick, with independent state. Typed operations exposed comparisons, swaps and writes, as well as auxiliary activity in Counting and Radix Sort. A bounded future buffer and retained history enabled lazy generation and exact reverse stepping. | The execution and rendering foundation was imported. The shared application added Study/Compare and revised seeking and run preparation. [Standalone snapshot](https://github.com/BJoozz/sorting-algorithm-visualizer/commit/9236a65) · [Performance milestone](https://github.com/BJoozz/sorting-algorithm-visualizer/blob/9236a65/docs/performance-milestone.md) · [Study/Compare import](https://github.com/BJoozz/visualgo-plus-design/commit/ee4bb72) |
| **Tree Visualizer, September.** The first snapshot supported rooted-tree editing, LCA and BST search. Later commits added state-changing operations, Binary Lifting, Heap, Trie and Segment Tree. Binary Lifting built its ancestor table column by column with worked examples. | The user can choose a root for the same edge list and follow the new layout. A tree mutation introduces temporary structures, so playback can preview an insertion or deletion and commit the result on Apply at the end. Binary Lifting showed a different need, namely to align the tree with a preprocessing table and a query. | The tree modules, operations and session architecture formed the Tree foundation. [Initial Tree commit](https://github.com/BJoozz/tree-visualizer/commit/e687099) · [Tree operations](https://github.com/BJoozz/tree-visualizer/commit/015469e) · [Binary Lifting columns](https://github.com/BJoozz/tree-visualizer/commit/540308b) · [Standalone workspace behaviour](https://github.com/BJoozz/tree-visualizer/blob/46ce0a7/README.md) |

**Naming on slides.** Use *standalone Graph rewrite* for Bao's Graph Visualizer V2. Use *split rails (V2)* and *docks (V7)* for the team layouts. Bao built Graph, Tree and Sorting in both layouts using Kerk's design system. The preliminary layout survey informed the choice of V2 and V7. The later Week 10 trial used V10 after its adoption. [Graph import](https://github.com/BJoozz/visualgo-plus-design/commit/0073875) · [Tree import](https://github.com/BJoozz/visualgo-plus-design/commit/7b16bf3) · [Sorting import](https://github.com/BJoozz/visualgo-plus-design/commit/ee4bb72) · [CA report §3](../report/main.tex#L112) · [Week 10 addendum](../report/week10_user_trial_addendum.md)

## 2. Early Design Phase — Bao, 3 minutes

| Slide | On-slide copy | Visual and delivery |
| --- | --- | --- |
| **Exploring three visualizers** | **Graph** · edit an input and follow a run. **Tree** · inspect changes before applying them. **Sorting** · compare algorithms on the same data. | Three labelled crops from the actual standalone builds. Point to the canvas and playback in Graph, an operation or ancestor table in Tree, and the shared transport in Sorting. About 1:40. |
| **From prototypes to a common direction** | One continuous workspace · Familiar playback across topics · Room for topic-specific explanations | Show the standalone Graph editor and run views alongside the Graph rewrite, or use an annotated still if the original builds are unavailable. End with the handoff to Kerk's UI/UX evolution. About 1:20. |

### English speaker notes

I started by building standalone visualizers for Graph, Tree and Sorting. These let me make the interactions work on real examples while Kerk explored the design of the wider site.

The first Graph prototype let me draw or type in a graph and then step through BFS or DFS. I added a reusable player so other algorithms could use the same controls. The editor and the run view still used separate canvas instances, and keeping the two views consistent took work. In the next Graph prototype, I kept one canvas throughout. I could move a vertex and continue looking at the same step. This gave me a concrete model of what it should feel like to edit and run an algorithm in one workspace.

Sorting posed a different question. I wanted to give several algorithms the same array, advance them together and see what each algorithm was doing. Each pane ran independently, while one set of controls moved the comparison forward or backward. That made it possible to study differences on a shared input.

With Tree, I explored both how to show a rooted structure and how to visualize operations that change it. For example, the user could step through a BST insertion, look at the proposed result and decide whether to apply it. Binary Lifting also gave us a reason to show a table alongside the tree.

Together, these prototypes gave us practical requirements for the shared interface. The drawing needed to stay available, playback needed to feel familiar across topics, and the surrounding panels needed to support different kinds of explanations. Kerk and I used the working prototypes and his design system to try how those pieces could fit together. Kerk will now explain the layout options, what we learned from user feedback and how we arrived at V10.

## 3. Algorithm Visualizers — Bao, 8 minutes

These six speaking beats include the motion clips and short live interactions. They can fit into four slides. Keep the longer Graph walkthrough, detailed memory policy and oracle details in [Q&A backup](CA_PRESENTATION_GRAPH_CASE.md) and the [contribution map](CA_PRESENTATION_CONTRIBUTION_MAP.md).

| Slide | Main point | Beats and timing |
| --- | --- | --- |
| **My work across the visualizers** | Standalone foundations, new algorithms and operations, editor and site integration, shared V10 shell, explanation and testing. | Contribution overview, 0:45. |
| **One workspace, different state** | The layout system can move panels around the canvas. The graph workspace distinguishes input from position and playback. | V10 panel groups, 1:10. Graph state and one-canvas clip, 1:15. |
| **Different ways to represent a run** | Tree previews structural changes. Sorting compares independent operation streams on a shared input. | Heap preview and Apply, 1:10. Sorting Compare, 1:15. |
| **Explain, pause and inspect** | Floating text explains a decision, paused motion keeps focus, and the completed graph stays explorable. | Dijkstra demo and handoff, 2:25 including switching and a few seconds of observation. |

### English speaker notes

**Overview.** My work focused on what happens when a learner opens a visualizer, changes an example and steps through the algorithm. I built the standalone Graph, Tree and Sorting foundations, extended their algorithms and operations, and integrated them into the site using Kerk's design system. I implemented the core V10 shell and worked on explanatory features such as floating text. I will show how those pieces work together.

**V10 shared shell.** Kerk has shown how we reached the V10 design. Here is what the implementation needs to support. I can move the Status panel next to Pseudocode or split it into a group of its own. The canvas stays mounted in the middle, so the learner can rearrange supporting information even during a run. The shared layout model handles groups, sizing and valid places to drop a tab. The same geometry helps render the layout and decide where a panel can fit. The model also loads saved layouts and can recover from an invalid saved configuration. Graph, Tree and Sorting can use that shell while each supplies its own panels. *Show one tab move on a running or paused example, then reset the layout before the next clip or tab.*

**Graph.** Moving a vertex changes its position. Editing the weight of an edge changes what the algorithm is solving. I store the graph input, positions, playback session and step presentation separately. Here I move a vertex and keep the current step. When I change the weight, the session is cleared and I can start a new run on the updated graph. The same graph representation also tracks exact edge identity, which matters for parallel edges and algorithms such as bridge detection. *Show drag versus edit in a short clip. Reserve the oracle for Evaluation.*

**Tree.** Heap insertion shows why a step sometimes needs to display a structure the user has yet to save. Here, inserting 1 puts it below 7, and the same items are highlighted in the tree and the array. As I step forward, I can see where the new item moves. As I step backward, I can inspect the earlier structure. The editor changes when I explicitly apply the completed result. *Use the Heap capture or a short preview/back/Apply clip. Keep Binary Lifting hover for the joint workflow.*

**Sorting.** Each pane receives the same dataset. The shared clock advances each active pane by one logical operation per tick, while the panes maintain independent states and can finish at different times. The operations expose comparisons, writes and, where relevant, steps involving buckets. Generators let us pull operations as needed, with bounded buffering for upcoming operations. We keep the history for seeking, which costs memory on long runs. The shared counter tells us how far we have advanced through the operations. CPU runtime would require a separate measurement. *Use two panes on a shared screen for readability. The existing four-pane screenshot shows the full comparison option.*

**Explain, pause and inspect.** On this Dijkstra step, the drawing can stay almost the same even though the algorithm has made a decision. I press Next and a short note tells me why the new distance is accepted or rejected. The detail stays in Status, and the note appears beside the part of the graph being discussed. Now the counter is fixed because I have paused the run. The motion you can still see highlights the current relationship. At the end, I can hover a vertex to inspect its shortest path using the result we already computed. These features also make more sense when you start with your own example. In the joint demo we will begin with the editors and show how that workflow carries across algorithms.

## 4. Joint Demo & Evaluation — 5 minutes

### Workflow — 3 minutes

| Time | Action and message |
| --- | --- |
| 0:00–1:20 | Show the Graph and Tree Editor cards. Open Graph Editor, load a prepared example and run Dijkstra. Switch to recursive DFS on the same graph and show the final traversal recap. Explain that the editor starts from the learner's example, which can be used to test an observation or look for a counterexample during competitive-programming practice. Point out that different algorithms interpret the same input differently. |
| 1:20–3:00 | Open Tree Editor with a valid prepared tree. Run the Binary Lifting query and inspect ancestors on hover after pausing or finishing. Say how the interaction connects the tree with its ancestor information. The editor currently offers Binary Lifting, BST and AVL. The Heap example in the technical section is a separate workspace. |
 
Dijkstra floating text, paused emphasis and final-path hover have their own short slot in Algorithm Visualizers. In the joint demo, show the same Graph Editor input continuing into DFS quickly. DFS's final animation recaps visit order and the traversal tree. [Editor and final-frame behaviour](CA_PRESENTATION_INTERACTIVE_DEMO.md)

### Evaluation slide and speaker notes — 2 minutes

**On slide.** Software correctness · independent oracles and browser checks. Week 10 usability · 15–20 minutes of independent use, a short post-use test and feedback. Design response · floating text, legend and Status changes.

We checked both algorithm results and interaction behaviour. For example, to test cut vertices and bridges, we used an independent method that removes a vertex or edge and counts the connected components again. It gives us a way to check cases such as parallel edges. On the snapshot used for the report, we recorded 3,273 passing unit tests and 151 passing Chromium browser cases. These checks tell us what the software did on the cases we tested.

For usability, in Week 10 we asked NUS students with different levels of algorithm experience and prior VisuAlgo use to try V10 independently for 15 to 20 minutes. The sessions were recorded, and participants completed a short post-use test and gave feedback. We went on to add floating text to keep short explanations near the graph or tree, and adjusted the legend and Status panel. The trial guided those changes. A follow-up with defined tasks would let us see how users work with the revised interface and where they still need help.

**Evidence boundaries.** Label the recorded test totals **1 November, app commit `662e7b3`, Chromium for browser cases**. The post-use test and feedback support formative findings. The available record leaves learning gains, comparative usability and the effect of floating text unmeasured. There is room for one concrete observation if Bao or Kerk can locate it in the session records. Add the action observed, what changed and what was measured, if anything. Omit any participant count or quotation until a source is available. [Validation evidence](../04_figures_and_validation.md#21-the-check-run-of-2026-11-01) · [Report evaluation](../report/main.tex#L293) · [Trial addendum](../report/week10_user_trial_addendum.md)

## 5. Future Work — both, 2 minutes

| Order | What is complete enough to show progress |
| --- | --- |
| **Stabilize the current prototype and consolidate trial observations.** | A reproducible build and a short set of anonymized observations tied to design decisions. |
| **Integrate one Graph algorithm end to end with the shared engine and website infrastructure.** | Graph input, stable node and edge identities, typed step conversion, rendering, forward/backward playback and cancellation all agree with the TypeScript baseline for the chosen example and tests. |
| **Validate and prepare the first release.** | Defined user tasks, desktop/browser checks and measurements for startup, seeking and memory. Release completed topics progressively, targeting an initial public release around March 2027. |

### English speaker notes

**Bao.** Our current prototype gives us working Graph, Tree and Sorting visualizers. Next, we want to organize the Week 10 feedback into specific observations, stabilize the main workflows and test the revised interface on a few defined tasks. For example, we can ask a learner to explain a Dijkstra relaxation and see how they use the canvas, pseudocode and Status.

**Kerk.** For the engine, the proposed first step is to connect one Graph algorithm across the full application, from the user's input to execution in the engine and playback in the visualizer. We can compare the result and the step behaviour with the current TypeScript implementation before extending the integration.

**Both.** We are targeting an initial public release around March 2027, subject to the progress of integration and validation. Our current transition plan keeps the original VisuAlgo available and links to completed topics in VisuAlgo+. Over time we aim to cover the algorithms that the original platform offers.

Speaker assignment within this closing and the first integration algorithm are workshop proposals. The report records a single-Graph-algorithm integration slice and a preliminary February–April window. The later preparation note records March as the target for an initial release. [Report plan](../report/main.tex#L326) · [Release direction](CA_PRESENTATION_PREP.md#q3-what-is-the-current-state-and-intended-release)

## 6. Capture list and rehearsal

| Priority | Capture or action | Asset or reproduction source |
| --- | --- | --- |
| 1 | Three stills for Early Design, from the standalone Graph, Tree and Sorting builds. Use a common viewport and legible crops. On the second slide, use the Graph rewrite as the continuation of the standalone Graph story. | Suggested refs `5fc06a0`, `46ce0a7`, `9236a65`, `c8b14e6`. These refer to the last documented standalone snapshots. |
| 2 | Two motion clips, about 10–15 seconds each. First, move a V10 panel while playback is paused. Second, advance into a Dijkstra relaxation note, let paused motion show briefly with the frame counter visible, then hover two final-frame targets. Split this second clip into two if the text is too quick at presentation size. | [F3 panel-drag still](../figures/F3-tab-drag-preview.png) · [F4 Dijkstra note still](../figures/F4-sssp-dijkstra-frame24-note.png) · [Reproduction notes](../figures/README.md) |
| 3 | One short Graph state clip, then Heap and Sorting stills or clips. Show vertex drag at a fixed frame followed by a weight change and reset. For Heap, show the preview or Apply boundary. For Sorting, keep the shared dataset, operation count and both panes visible. | [Graph case](CA_PRESENTATION_GRAPH_CASE.md#proposed-demo--6090-seconds) · [F6 Heap still](../figures/F6-heap-insert-climb-note.png) · [F7 Sorting still](../figures/F7-sorting-compare-4-panes.png) |
| 4 | Backup clips for the joint workflow. Record a Graph Editor algorithm switch using the same graph and recursive DFS final recap, and a Tree Editor Binary Lifting hover. | [F1 editor cards](../figures/F1-home-catalogue.png) · [F5 LCA still](../figures/F5-lca-query-6-2-frame2-note.png) · [Editor demo script](CA_PRESENTATION_INTERACTIVE_DEMO.md) |

**Candidate Graph Editor input for rehearsal.** Directed, start at A. Paste the edges below. The graph has a rejected relaxation into D from C (`2 + 7 > 6`) and a later accepted update into D from B (`3 + 2 < 6`). The final shortest path from A to D is A → C → B → D, distance 5. Changing the weight of B → D from 2 to 8 should clear the existing session. After a fresh run, the direct A → D path has distance 6. These are calculated expectations for this input. Confirm the note wording, steps and controls in the chosen presentation build.

```text
A B 4
A C 2
A D 6
C B 1
C D 7
B D 2
```

**Candidate Tree input for rehearsal.** Use the already documented tree with root 8 and edges `8 4`, `8 12`, `4 2`, `4 6`, `12 10`, `12 14`. Query `u=6, v=2`. The LCA is 4. [F5 capture notes](../figures/README.md#f5-lca-query-6-2-frame2-notepng)

Pin the demo build, clear any saved layout in the demo profile, check the Animate paused steps setting, keep Live layout off for the vertex-drag clip, and advance with Next to trigger floating text. Leave the current frame counter visible in motion clips. The existing F-series images are documented historical captures from `662e7b3`. Behaviour and frame numbers in the rehearsal build should be checked before replacing them. Review for this draft used source, selected patches and existing report evidence. It included no fresh build, browser rehearsal, recordings or test runs.
