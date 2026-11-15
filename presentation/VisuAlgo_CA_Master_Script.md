# VisuAlgo+ CA Presentation: master script and structure

Working rehearsal draft • 16 November 2026 • 33 minutes plus 12 minutes for Q&A and buffer.

## How to use this version

The PowerPoint contains 22 timed slides, one Q&A slide and four backup slides (slide 27, a DFS recap clip, was added on 16 November as a fallback for the live demo). Slides 14–18, 24 and 27 embed real-app clips; see [the media map](CA_PRESENTATION_MEDIA_USAGE.md). English speaking text, demo cues and source links are also embedded in speaker notes. Timing includes transitions and demonstrations; it is a rehearsal budget, not measured delivery time. Slides 7–12 are an evidence-based draft for Kerk to confirm and replace with his current details where necessary. No fabricated benchmarks or completed engine integration are claimed.

Owner confirmations: editing, playback and comparison were early goals discussed with Prof. Halim; LCA is the main Tree example; Bao recalls frequent Status reading among newer learners, especially for LCA, as motivation for floating text. The intended benefit has not been measured.

## Run of show

| Section | Speaker | Time | Slides |
|---|---|---:|---|
| Introduction | Bao | 4:00 | 1–4 |
| Early Design | Bao | 3:00 | 5–6 |
| UI/UX Evolution | Kerk | 3:00 | 7–8 |
| Engine & Website | Kerk | 8:00 | 9–12 |
| Algorithm Visualizers | Bao | 8:00 | 13–19 |
| Demo & Evaluation | Both | 5:00 | 20–21 |
| Future Work | Both | 2:00 | 22 |
| Q&A and buffer | Both | 12:00 | 23 and backups |

## Slide-by-slide script

### 01. VisuAlgo+

**Bao · Introduction · 00:00–00:30**

**On slide**

- VisuAlgo+
- Rebuilding interactive algorithm visualization
- Truong Van Quoc Bao and Kerk Tai Heng · Supervisor: A/P Steven Halim
- NUS School of Computing · CP4101 Continuous Assessment · 16 November 2026

**Visual:** Current app screenshot beside the title: a Dijkstra step with its floating note (app 346e84b).

**English script**

Good afternoon. We are Bao and Kerk, and our project is VisuAlgo+. We are rebuilding the platform while preserving its purpose: helping people learn and explore data structures and algorithms. Today we will explain the design process, our technical contributions, and what we learned from the working prototype.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/main.tex

### 02. Motivation

**Bao · Introduction · 00:30–01:40**

**On slide**

- More convenient graph editing: draw and change the graph you are studying, with parallel and curved edges handled clearly
- Richer interaction on the canvas: inspect a step, move things and see why a decision happens
- Sorting comparison on the same input: several algorithms on one dataset, side by side

**Visual:** Three cards, each with a crop of today's prototype; footer: directions proposed by Prof. Halim in early weekly meetings.

**English script**

VisuAlgo already lets students explore their own inputs and follow algorithms step by step. We want to preserve those strengths. In our early discussions, Prof. Halim proposed several directions for improving the platform. These included more convenient graph editing, clearer handling of parallel and curved edges, and multiple sorting panes for comparison. Editing, playback and comparison were goals from the beginning. The prototypes helped us investigate how to implement them. My background in competitive programming and teaching also shaped my focus. When explaining an algorithm, I want the learner to understand why a decision happens, rather than only see the final answer. That means supporting examples that learners can change, inspect and discuss.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PREP.md

### 03. Why rebuild the foundation?

**Bao · Introduction · 01:40–02:50**

**On slide**

- Shared components already exist: for example, a graph widget used by several topics
- Module-specific logic complicates common changes: input handling and visual-state building live inside each topic
- New interactions need clearer state boundaries: comparison panes need their own state but shared controls

**Visual:** Simplified diagram: three original graph topics, each with its own input handling and state building, over one shared graph widget; consequence: one editing change means coordinated changes and checks across every topic.

**English script**

The original platform has grown through contributions over many years. It already has shared components, including a graph widget. However, substantial logic remains specific to individual modules. For example, graph topics contain their own input handling and visualization-state construction. A common editing change can therefore require coordinated changes and checks across topics. Sorting comparison raises another issue. Each pane needs its own execution state, while the controls must coordinate all panes. Dividing the screen alone does not solve this. These requirements gave us a reason to reorganize the foundation. We chose technologies and boundaries that support the interactions we want, while retaining useful tools such as D3 where they fit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PREP.md

### 04. Objectives and current scope

**Bao · Introduction · 02:50–04:00**

**On slide**

- A reusable visualization and interaction layer · now: Graph, Tree and Sorting share one V10 shell · next: stabilize the shown workflows
- A renewed website and execution foundation · now: site with catalogue and routes; separate C++/WebAssembly engine foundation · next: connect them to the visualizers
- A working prototype with further integration ahead · now: students tried V10 in Week 10 · next: validate, then an initial release around March 2027 (target)
- Current boundary: the visualizers run TypeScript algorithms in the browser; the engine is separate and connecting it is Semester 2 work

**Visual:** Three objective cards with NOW and NEXT chips, and a boundary band.

**English script**

Our objectives are to improve interaction across topics, build clearer boundaries for future development, and validate the resulting functionality. We already have a working prototype that students have tried. Graph, Tree and Sorting currently run TypeScript implementations in the browser. Kerk has also developed a separate engine foundation. Connecting that engine and the wider website infrastructure to the visualizers remains part of the next stage. We are targeting an initial public release around March 2027, subject to integration and validation. The intended transition keeps the original VisuAlgo available and links to completed topics in VisuAlgo+. We will begin with how the early prototypes helped us make the interaction requirements concrete.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PREP.md

### 05. Early visualizer prototypes

**Bao · Early Design · 04:00–05:30**

**On slide**

- Graph: editing and playback on one canvas
- Tree: structural operations and ancestor information
- Sorting: independent runs with shared controls

**Visual:** Real stills of the standalone builds, rebuilt at their last documented commits (5fc06a0, c8b14e6, 46ce0a7, 9236a65) and captured on 16 Nov 2026: Graph prototype 1 run view, the Graph rewrite with one canvas, the Tree prototype's Binary Lifting table, and Sorting Room with two panes. Not the current app.

**English script**

The early prototypes were experiments in how to achieve the goals we had discussed with Prof. Halim. The first Graph prototype used separate editing and running views. In the standalone Graph rewrite, I kept one canvas and separated input, positions and playback. That let a learner move a vertex while continuing to inspect the same algorithm step. For Tree, I explored operations that change the structure, and how to inspect a proposed result before applying it. Binary Lifting also required a tree and an ancestor table to explain one query together. Sorting explored a different interaction: several algorithms receive the same array, maintain their own states and advance through shared controls. Each prototype therefore tested a different requirement. The standalone Graph rewrite is distinct from the later layout named V2. I will use those names separately throughout the presentation.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

### 06. A common direction

**Bao · Early Design · 05:30–07:00**

**On slide**

- Bao: visualizers, algorithm execution, the V10 shell core and site integration
- Kerk: design system, engine foundation and infrastructure; organised user feedback; consolidated the application
- Joint design decisions with supervisor feedback: V10 decided together; Bao implemented its core model, Kerk refined and consolidated it
- Requirements carried forward: keep the drawing available · familiar playback across topics · topic-specific information alongside

**Visual:** Two contributor cards, a joint band and three requirement chips.

**English script**

We divided the work around our strengths, while discussing the interface together. My competitive programming and teaching experience helped me focus on algorithm behavior, intermediate states and explanations. I built the visualizer foundations and later the core shared shell and site integration. Kerk focused on the design system, engine foundation and infrastructure, and organized user feedback. The responsibilities overlap. In particular, we made the V10 design decisions together, I implemented its core model, and Kerk made later refinements and consolidated the application. Our early prototypes gave us concrete requirements: keep the drawing available, make playback familiar across topics, and allow topic-specific information alongside it. We used those requirements with Kerk's design system to explore the shared interface. Kerk will now explain how the layout evolved.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

### 07. Layout exploration

**Kerk · UI/UX Evolution · 07:00–08:30**

**On slide**

- Nine candidate layouts
- V2 split rails and V7 docks
- Comparable functionality across both builds

**Visual:** Schematic flow (drawings, not screenshots): nine wireframes → V2 rails and V7 docks → V10 (Week 9).

**English script**

The design process explored nine candidate visualization-page layouts. After an early user survey, Bao and I selected V2, with split rails, and V7, with draggable docks, for functional prototypes. Bao implemented Graph, Tree and Sorting in both layouts using the design system. Keeping comparable functionality helped us discuss the interface rather than compare unrelated features. Split rails provided a familiar arrangement for supporting information. Docks allowed users to move panels around the drawing. We used the working builds and discussions to decide which properties to retain. This early layout survey was separate from the Week 10 user trial. The purpose of the functional prototypes was to explore these choices in use.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

### 08. The V10 panel layout

**Kerk · UI/UX Evolution · 08:30–10:00**

**On slide**

- A persistent central canvas: stays mounted while panels move
- Tab groups around the drawing: left, right and bottom; move, split, resize
- One application after consolidation: Graph, Tree and Sorting share this shell

**Visual:** Current app screenshot (Tree Editor, app 346e84b, 16 Nov 2026) with coloured outlines for the tab groups, the canvas and the shared playback bar.

**English script**

In Week 9, we discussed combining selected strengths of V2 and V7 into V10. The central drawing stays available, while the supporting information lives in panel groups. Users can move tabs, split groups and resize the surrounding space. Bao implemented the core model and shell. We then discussed refinements to the interaction, and I implemented several of them. I also consolidated the separate visualizer copies into one application and moved common code into a shared layer. That reduced the need to make the same shared fix in multiple copies. The Week 10 trial used V10 after this decision. Bao will explain the implementation constraints behind the shell later. I will now turn to the website and execution architecture.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

### 09. Application boundaries

**Kerk · Engine & Website · 10:00–12:00**

**On slide**

- Site host: routes, top bar and theme
- Visualizers: input, execution and playback (TypeScript in the page)
- Shared layer: layout and presentation utilities
- Separate engine foundation awaiting integration

**Visual:** Layered diagram: site host over three visualizer boxes (Graph and Tree: React Flow with D3 layout; Sorting: Canvas 2D) over the shared layer; the engine is a dashed box to the side.

**English script**

The prototype is one React and TypeScript application built with Vite. The site host owns routing, the top bar and the theme. It mounts Graph, Tree or Sorting, and each visualizer owns its domain input and playback. The shared layer supplies the panel layout and reusable presentation utilities. This separation matters because the shell should know where a Status panel sits, while the algorithm decides what that panel means. Graph and Tree use React Flow for the drawing. D3 supplies selected layout calculations. Sorting uses Canvas 2D for arrays and algorithm-specific representations. There is an important boundary in the current build: these visualizers execute TypeScript algorithms in the page. The WebAssembly engine is a separate project. This separation lets us develop interaction and execution independently while we work toward integration.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

### 10. Engine foundation

**Kerk · Engine & Website · 12:00–14:30**

**On slide**

- C++20 compiled to WebAssembly
- Execution inside a worker
- Protocol messages connect the page and engine
- Python tracing explored through Pyodide

**Visual:** Flow diagram: page ⇄ protocol messages ⇄ worker (WebAssembly engine, Pyodide); band with the design question about exposing state without depending on page layout.

**English script**

The engine foundation explores running C++ algorithms compiled to WebAssembly inside a worker. The page and engine communicate through protocol messages instead of direct calls into the visualization components. A worker gives execution a separate context, while the page remains responsible for interaction and drawing. The documented engine uses protobuf messages with graph and array representations. It also includes a Python execution path through Pyodide for tracing sorting algorithms. The architectural question is how to expose enough state for visualization without making the engine depend on the page layout. The engine should describe algorithm state and changes. The visualizer still needs to interpret those changes for a learner. For example, an engine update to a distance does not by itself decide where an explanatory note should appear or which pseudocode line to emphasize. That interpretation belongs at the integration boundary. [Engine demonstration: use the separate engine build to show one forward step and inspect its state output. Keep this demonstration within 45 seconds.]

**Delivery cue:** Kerk: confirm against your current engine build. Optional 45-second separate-engine demonstration is included in this time slot.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

### 11. Reversible execution and integration

**Kerk · Engine & Website · 14:30–16:30**

**On slide**

- Engine history: reversible records per step
- Current visualizers: sequences or operation history
- Integration must preserve identity and step meaning

**Visual:** Two cards marked ≠, over a band with three chips: node and edge identity, the same run across edits and restarts, state/pseudocode/notes agree on a step.

**English script**

The engine and visualizers currently use different history models. The documented engine keeps a reversible journal of records for each step, and can move backward through those records. The current Graph and Tree visualizers build their step sequences when a run starts. Sorting pulls operations from generators and retains history for seeking. Connecting these systems requires an explicit translation, rather than only replacing an algorithm function. Node and edge identities must stay consistent, particularly for parallel edges. The same run must remain identifiable when the user changes input or starts again. The displayed state, pseudocode and explanatory text must also agree on what a step means. Bao carried out an earlier integration experiment, including stable edge identities and a browser client. That experiment remains separate from the delivered visualizers. Our proposed next step is one complete Graph integration, checked against the current TypeScript behavior before expanding coverage.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

### 12. Website integration

**Kerk · Engine & Website · 16:30–18:00**

**On slide**

- One site controls navigation and theme
- Visualizers supply topic-specific controls
- Shared infrastructure supports further integration

**Visual:** Site frame with three visualizer slots and an infrastructure card; attribution line: Bao built the functional catalogue, routes and host adapters; Kerk consolidated and refined.

**English script**

The website needs to host the visualizers without duplicating their controls. The prototype gives the site ownership of the top bar and theme. Each visualizer supplies the topic-specific parts, such as algorithm choices or sorting pane controls. The host then presents these within one site. Bao built the functional catalogue, routes and host adapters on the design system. My consolidation and refinements helped make this a single application. This is an integration boundary where our contributions meet. The broader website infrastructure and engine still need to come together with the visualization layer. Keeping these responsibilities explicit helps us avoid a second set of playback controls or conflicting theme state. Bao will now explain how the visualization layer uses these boundaries to support editing, comparison and explanations.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

### 13. My visualization contributions

**Bao · Algorithm Visualizers · 18:00–18:40**

**On slide**

- Graph, Tree and Sorting foundations
- Algorithm and operation extensions
- V10 shell and site integration
- Step explanations and validation

**Visual:** 2×2 cards with a one-line detail and a small current-app thumbnail each.

**English script**

My contribution covers the visualizer foundations, algorithm execution and operation extensions, the V10 shell, and integration into the site. I also worked on how individual steps communicate their meaning and how the behavior is tested. I will show selected decisions across these areas. The examples connect the underlying state model to something a user can directly observe.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

### 14. A shared shell with clear constraints

**Bao · Algorithm Visualizers · 18:40–19:50**

**On slide**

- The canvas stays mounted: moving Status does not reload the drawing or the run
- One model governs sizes and valid drops: split, join or dock: the preview uses the same geometry as the result
- Saved layouts recover safely: versioned and checked, repaired or reset

**Visual:** Clip `02b_v10_split_left_bottom.mp4` (16.3 s, app 346e84b), paused at frame 12/21 throughout. The Status tab, set up beside Pseudocode, is dragged down to split the right column in two, then into the left group, then to the bottom row under the drawing. The first take, `02_v10_move_panel.mp4`, is kept as an alternative.

**English script**

The V10 shell is a stateful layout system. Moving a panel must preserve the canvas and the panel's input state. The layout model keeps groups in the left, right and bottom regions and enforces size constraints. One resolver handles the geometry used for both the displayed layout and drop previews. This helps the preview match what the user will get after releasing the tab. Saved layouts are versioned and checked when loaded, with repair or a default when needed. Each visualizer supplies its own panels and minimum drawing space. [Press → to play the clip: the Status tab splits the right group in two, joins the left group, then docks under the drawing, while the run stays at frame 12.] The implementation trades the freedom of a completely general split layout for a stable drawing area and predictable interactions.

**Delivery cue:** Clip, 16.3 s, frame 12/21 throughout.
- 1.5–4.4 s: Status is dragged down its own group (the preview moves from the upper to the lower half).
- 4.4 s: the right column splits into two equal groups.
- 6.3–9.2 s: Status is dragged to the left group.
- 11.1–14.0 s: Status is dragged to the bottom row.
- 14.0 s: Status docks under the drawing; the drawing re-fits and the left group shows E-Lecture.

Live alternative only if time allows.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/02b_v10_split_left_bottom.mp4

### 15. Input, layout and playback

**Bao · Algorithm Visualizers · 19:50–20:55**

**On slide**

- Move a vertex: preserve the run (changes Layout only)
- Change an edge weight: invalidate the run (changes the Document)
- Who owns which state: Document (nodes, edges, weights) · Layout (positions) · Session (run and selected step) · Presentation (highlights derived from the step)

**Visual:** State-ownership diagram beside clip `03_graph_drag_then_edit.mp4` (8.0 s): B dragged at frame 12/21, then B → A changed from 1 to 5 in Draw graph → Edges, giving NO RUN.

**English script**

Moving a vertex changes the drawing. Changing an edge weight changes the problem the algorithm is solving. I separate the graph document, layout, playback session and presentation. The document contains nodes, edges and weights. Layout contains positions. A session records the run and selected step. Presentation derives the visible highlights and badges from that step. [Press → to play the clip.] Dragging B preserves the current step: the counter stays at 12. Changing the weight of B to A from 1 to 5 edits the document, so the old run is invalidated and the footer says No run. We cannot keep showing a result for the wrong input. Stable edge identity also lets us distinguish parallel edges. The aim is consistent interaction backed by clear state ownership.

**Delivery cue:** Clip, 8.0 s: 0–0.8 s paused at 12/21 relaxing B → A; 0.8–1.8 s B dragged, still 12/21; 3.0–4.5 s Draw graph → Edges, "B A 1" selected; 4.5–8.0 s typing 5: label 5, NO RUN, NO ACTIVE RUN. Live layout was off. The app has no on-canvas weight edit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_GRAPH_CASE.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/03_graph_drag_then_edit.mp4

### 16. LCA: explaining a decision to stay

**Bao · Algorithm Visualizers · 20:55–22:35**

**On slide**

- Query: LCA(6, 10) = 8 (same depth, so no depth lift)
- k = 1: both ancestors are 8 (keep u and v: nothing moves, the note says why)
- k = 0: ancestors 4 and 12 differ (lift both one level; their parent 8 is the answer)

**Visual:** Clip `01b_lca_keep_then_jump.mp4` (10.3 s): notes "same ancestor · keep u, v" and "differ · lift both". Alternative clip `01_lca_equal_ancestors.mp4` shows LCA(6, 2) = 4.

**English script**

Binary Lifting is a useful example because a query has several stages and connects a tree with an ancestor table. On this small tree we query 6 and 10. They have the same depth, so there is no depth-lifting phase. [Press → to play the clip.] At k = 1 both candidate ancestors are 8, so the algorithm keeps u and v where they are. Nothing moves on the drawing, but a meaningful decision has happened, and the short note above 8 says so. At k = 0 the candidates are 4 and 12. They differ, so both cursors lift one level; now they share the parent 8, which is the answer. The tree, the table reads in the strip under the drawing, the pseudocode and Status all describe the same selected step. During the Week 10 trial, I observed that less experienced users still depended heavily on Status, especially for algorithms with several stages such as LCA. Floating text is my design response: bring a short explanation closer to the object being discussed. Status remains available for the full explanation. We still need to evaluate whether this reduces attention switching.

**Delivery cue:** Clip, 10.3 s: frame 2/7 (k = 2, both 8); 0.9 s frame 3, k = 1, note "same ancestor · keep u, v" above 8; 2.8 s frame 4, k = 0, 4 and 12 differ, "differ · lift both"; 4.9 s frame 5, u = 4, v = 12, "↑ 1 level"; 6.7 s same parent 8; 8.0 s LCA(6, 10) = 8. Tree: root 8; edges 8-4, 8-12, 4-2, 4-6, 12-10, 12-14. Do not describe a depth-balancing move.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/week10_user_trial_addendum.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/01b_lca_keep_then_jump.mp4 (alternative: 01_lca_equal_ancestors.mp4, LCA(6, 2) = 4)

### 17. Sorting comparison

**Bao · Algorithm Visualizers · 22:35–23:50**

**On slide**

- The same dataset in every pane: 12 values, Bubble and Selection
- One clock, independent operation streams: both panes pause at operation 48
- Retained history supports seeking: the clip ends with Last, a seek to the final operation
- Operation counts are not CPU time

**Visual:** Codex clip `02_sorting_shared_clock.mp4` (10.4 s), poster at operation 48.

**English script**

Sorting comparison gives every pane the same input while keeping its execution state independent. A shared clock advances the active panes by logical operations. They can show different actions and finish at different times. Generators produce operations as needed. Upcoming operations use bounded buffering, while retained history supports backward seeking. Keeping that history has a memory cost on long runs. [Press → to play the clip: both panes pause together at operation 48, resume, then Last seeks to the end.] The counters describe the visualization's operations. They are not CPU runtime measurements, and equal operation indices do not guarantee equal computational cost. This makes the comparison useful for examining behavior, while keeping the interpretation honest.

**Delivery cue:** Codex clip, 10.4 s: Bubble and Selection on 8, 3, 10, 1, 6, 4, 12, 2, 9, 5, 11, 7 at 12 operations/s; both pause at operation 48 (Bubble 27 compares, 19 swaps; Selection 40 compares, 4 swaps); Last ends at 92 and 86 operations. Live alternative: step back once with Prev, only if time allows.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16/02_short_clips/02_sorting_shared_clock.mp4

### 18. Pause and inspect the result

**Bao · Algorithm Visualizers · 23:50–25:10**

**On slide**

- Paused motion keeps the current relationship visible: the counter stays at frame 17 while edge 2 → 3 is emphasised
- A short note explains the step on arrival: frame 18, 12 + 14 < 33 · update
- Final Dijkstra hover reveals a computed path: 8: 0 → 2 → 3 → 8, distance 42 · 4: distance 46

**Visual:** Clip `04b_dijkstra_big_note_pause_hover.mp4` (14.0 s): Dijkstra from 0 on the nine-vertex Big preset (visualgo.net's TESSELLATION). The first take, on the four-vertex S, A, B, T graph, `04_dijkstra_note_pause_hover.mp4`, is kept as an alternative.

**English script**

I also separate visual emphasis from algorithm progress. When playback pauses, the frame counter stays fixed. Optional motion can continue to emphasize the current node or edge without advancing the computation. This helps the learner inspect a relationship for longer. Floating text handles the arrival of a step and explains a short verdict. These are different mechanisms. At Dijkstra's final frame, the user can hover a vertex to inspect its computed shortest path. The application derives that highlight from the stored result. DFS has a different final behavior: a moving recap of the visit order and traversal tree. [Press → to play the clip: frame 17 stays fixed while edge 2 → 3 is emphasised; Next shows the note at frame 18, and 3's distance drops from 33 to 26; Last, then hover 8 and 4.] Motion can be turned off, and reduced-motion behavior matters for accessibility.

**Delivery cue:** Clip, 14.0 s.
- 0–3.0 s: paused at 17/53 (inspect 2 → 3, weight 14); the streak and glow move.
- 3.0 s: Next to 18/53; "12 + 14 < 33 · update" beside 3, whose badge reads 33→26.
- 6.0 s: Last, 53/53, 9 nodes settled.
- 7.6 s: hover 8: 0 → 2 → 3 → 8, distance 42.
- 10.6 s: hover 4: 0 → 2 → 3 → 4, distance 46.

Point at the 2 → 3 edge while the counter reads 17. Edge weights are small at slide size.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/04b_dijkstra_big_note_pause_hover.mp4

### 19. Editors for exploring an example

**Bao · Algorithm Visualizers · 25:10–26:00**

**On slide**

- Begin with a graph or tree
- Try compatible algorithms on the example
- Build small tests and investigate conjectures

**Visual:** Current Editors section of the home page (app 346e84b) above a three-step flow; limits line: custom input already exists in VisuAlgo, this is a clearer entry point; adoption not measured.

**English script**

The Graph and Tree Editor entry points support a workflow that begins with an example. The user may already have a graph in mind and want to investigate it. This can support competitive programming practice: construct a small test, check an observation, or search for a counterexample. The original VisuAlgo already supports custom inputs. Our addition is a more explicit entry point and workflow centered on that input. Tree Editor currently focuses on Binary Lifting, BST and AVL, with input conditions still applying. This is an intended use case, and we have not measured long-term adoption. We will now show a short continuous workflow.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

### 20. Demo: one example, several questions

**Both · Demo & Evaluation · 26:00–29:00**

**On slide**

- Graph Editor: Dijkstra and recursive DFS
- Tree Editor: a prepared LCA query
- Change an example and inspect the result

**Visual:** Timeline of the four demo steps with their time ranges, and a fallback card: if a live step fails, return to the clips on slides 15–18.

**English script**

Bao: I will start with a prepared graph so that we can focus on exploration. First, Dijkstra answers a shortest-path question. We can inspect the result, then switch to recursive DFS on the same compatible graph and ask about traversal instead. The final DFS motion recaps the traversal tree. The input is the starting point for different questions.

Kerk: The site gives these activities a common interface. The user can return to the editors and choose a different structure without learning a completely separate navigation system.

Bao: In Tree Editor, I will use the small tree from the LCA example. We can inspect ancestor information and the query result. If we change the relevant input or query, the old run must no longer represent the new question. These interactions are intended to support someone thinking through an example, as well as someone studying a named algorithm.

[Run the sequence below. Narrate only the action currently on screen. Allow the audience to observe. If a live action fails, return to the prepared slide and explain the expected state rather than debug during the talk.]

**Delivery cue:** 0:00–0:20 Graph Editor and input; 0:20–1:00 Dijkstra result; 1:00–1:40 recursive DFS and final recap; 1:40–2:40 Tree Editor and LCA ancestor inspection; 2:40–3:00 return to slides. Avoid repeating the full floating-text explanation.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

### 21. Evaluation and design response

**Both · Demo & Evaluation · 29:00–31:00**

**On slide**

- 1 Nov 2026: 3,273 unit tests and 151 Chromium cases (snapshot, app 662e7b3; not a rerun today)
- Week 10: independent use, post-use test and feedback
- Frequent Status reading motivated floating text
- Learning impact remains unmeasured

**Visual:** Two stat callouts, a Week 10 card, a design-response band and an amber limits band.

**English script**

Bao: We evaluated software behavior and collected formative feedback. The report snapshot records 3,273 passing unit tests and 151 passing Chromium browser cases on 1 November. For example, cut-vertex and bridge tests use an independent approach that removes a vertex or edge and recounts connected components. This checks results through a different method.

Kerk: In Week 10, NUS students with different levels of algorithm experience used V10 independently for 15 to 20 minutes. We recorded the sessions, then collected a short post-use test and feedback. This was separate from the earlier layout survey.

Bao: My recollection is that newer learners still had to read Status frequently, especially with multi-stage algorithms such as LCA. I added floating text to put short explanations near the relevant canvas objects, alongside changes to the legend and Status. These are design responses to formative observations. We have not measured whether floating text improves learning or reduces attention switching. A follow-up study needs defined tasks and observations of the revised interface.

**Delivery cue:** Historical test snapshot: app commit 662e7b3, 1 November 2026. LCA-specific observation is Bao’s recollection clarified on 16 November, not a coded analysis of reviewed footage.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/week10_user_trial_addendum.md

### 22. Semester 2 priorities

**Both · Future Work · 31:00–33:00**

**On slide**

- Integrate one Graph algorithm end to end
- Validate interaction, correctness and resource use
- Evaluate revised explanations with defined tasks
- Target an initial release around March 2027

**Visual:** Four-step roadmap, each with a one-line detail; limits line: March 2027 is a target.

**English script**

Kerk: Our next integration milestone is one Graph algorithm working across the full application. The input, engine execution and visualizer playback should agree on node and edge identity, step meaning and cancellation. We can check the result against the current TypeScript implementation before expanding the integration.

Bao: In parallel, I want to stabilize the workflows we have shown and evaluate the revised explanations. A task could ask a learner to explain why an LCA step keeps both nodes in place. We can observe how they use the canvas, ancestor table and Status, rather than assume that additional animation helps. We also need measurements for startup, seeking and memory on longer runs.

Both: We are targeting an initial public release around March 2027, depending on integration and validation. The current transition plan keeps the original platform available and links to completed topics. Our broader ambition is to cover the original algorithm range. The current work provides the visualizer foundations and a working prototype on which to build that release.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

### 23. Questions

**Backup / Q&A, outside timed talk**

**On slide**

- Questions
- Interactive visualization foundations
- A working prototype and a defined integration path
- Evidence and media: github.com/BJoozz/docsforfyp

**English script**

Thank you. We are happy to discuss the design decisions, implementation trade-offs or evaluation plan.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/main.tex

### 24. Backup: preview before Apply

**Backup / Q&A, outside timed talk**

**On slide**

- Inspect intermediate structures: BST Insert(5), the new node is a preview
- Step backward through the preview: the committed tree is unchanged
- Apply the completed result to the input: the tree text gains the edge 6 5

**Visual:** Clip `05_bst_preview_apply.mp4` (8.6 s).

**English script**

A mutating operation needs a different contract from a read-only query such as LCA. BST Insert(5) runs as a preview: the search path and the new node are visible, and I can step backward through the preview, but the tree document and its text input stay unchanged. Only Apply commits the completed result; the tree text then gains the edge 6 5 and the run ends. Switching to another operation discards the preview. Heap insertion follows the same contract, with an array view alongside the tree.

**Delivery cue:** Clip, 8.6 s: preview complete at 8/8 (text still 6 lines); Previous to 7/8 and 6/8; Next back to 8/8; 5.2 s Apply insertion, NO RUN; 6.2 s Edit tree shows "6 5" (8 nodes, 7 edges).

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/05_bst_preview_apply.mp4

### 25. Backup: correctness and limitations

**Backup / Q&A, outside timed talk**

**On slide**

- Independent oracle for cut vertices and bridges
- Stable edge identity for parallel edges
- Long sorting histories still cost memory

**Visual:** Historical still (app 662e7b3, 1 Nov 2026), now larger.

**English script**

For cut vertices and bridges, an independent oracle removes each candidate and compares connected-component counts. Exact edge identity matters because removing one of two parallel edges is different from removing the connection altogether. Other limits include unbounded retained sorting history and upfront sequence construction in Graph and Tree. Passing tests cover the tested cases and do not establish complete correctness, performance or learning benefit. AI tools assisted implementation and review under my requirements. I remained responsible for the design choices, acceptance and validation.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

### 26. Backup: evidence and ownership

**Backup / Q&A, outside timed talk**

**On slide**

- CA report and architecture records
- Contribution map and prototype history
- Week 10 trial addendum
- Source links in each slide’s notes

**Visual:** Four evidence cards with repository paths.

**English script**

Primary evidence lives in BJoozz/docsforfyp: report/main.tex, 03_architecture_and_decisions.md, docs/CA_PRESENTATION_CONTRIBUTION_MAP.md, docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md and report/week10_user_trial_addendum.md. Prototype history: BJoozz/graph-algorithm-visualizer, graph-visualizer-v2, tree-visualizer and sorting-algorithm-visualizer. Application: kerktaiheng/visualgo-plus-design (fork BJoozz/visualgo-plus-design), main 346e84b. Slides 1, 2, 8, 13–19, 24 and 27 use real captures of app 346e84b from 15–16 November; slide 25 is a historical capture of 662e7b3 (figures/README.md); slide 5 shows the standalone prototypes rebuilt at their documented commits; slide 7 is schematic. The November 16 clarification records early supervisor direction, the LCA selection and Bao's recollection about Status reading. Kerk should review slides 7–12 against his current engine and website work before the joint presentation.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

### 27. Backup: recursive DFS recap (demo fallback)

**Backup / demo fallback, outside timed talk**

**On slide**

- Same graph, another question: recursive DFS from S on the Dijkstra example
- The final frame replays the DFS tree: glow and streak in visit order, S → A → T, then S → B
- Different from Dijkstra's hover: a recap of the traversal, not a path query

**Visual:** Clip `06_dfs_recursive_recap.mp4` (8.5 s): Last to 21/21, visited S, A, T, B; the final frame replays the DFS tree about every 3 s.

**English script**

Use this slide only if the live Graph Editor part of the demo on slide 20 fails. Recursive DFS runs on the same S, A, B, T graph as the Dijkstra clips. On its final frame, the drawing replays the DFS tree in visit order every few seconds: S to A to T, then S to B. This is a different final behaviour from Dijkstra's hover path.

**Delivery cue:** Press → to play the clip.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/06_dfs_recursive_recap.mp4

## Demo preparation and remaining work

Slides 14–18 now play real-app clips embedded in the deck (app `346e84b`, recorded 15–16 November), so no window switching is needed during the technical section. The live demo stays on slide 20. Each clip has a poster frame on the slide as its static fallback; press → or click to play. Details: [media map](CA_PRESENTATION_MEDIA_USAGE.md) · [changelog](CA_DECK_CHANGELOG.md).

| Clip or live action | Slide | Length | Fallback |
|---|---:|---:|---|
| V10: split, join and dock Status while paused | 14 | 16.3 s clip | Poster: Status docked under the drawing at 12/21 |
| Vertex drag versus weight edit | 15 | 8.0 s clip | Poster: after the edit, NO RUN |
| LCA(6, 10): keep, then lift | 16 | 10.3 s clip | Poster: frame 4/7, "differ · lift both" |
| Sorting shared input and clock | 17 | 10.4 s clip (Codex) | Poster: both panes at operation 48 |
| Dijkstra on the nine-vertex Big graph: paused motion, note and final hover | 18 | 14.0 s clip | Poster: frame 18/53 with the 2 → 3 update note |
| Joint editor workflow | 20 | 3 min live | Clips on slides 15–18; backup 27 for the DFS recap |

### Prepared Graph input

Directed; start A. Expected shortest A-to-D path is A–C–B–D with distance 5. Change B–D to 8 and rerun: the direct A–D path has distance 6. Confirm behavior in the presentation build.

```text
A B 4
A C 2
A D 6
C B 1
C D 7
B D 2
```

### Prepared LCA input

Root 8. The slide-16 clip queries 6 and 10: at k = 1 both ancestors are 8 (keep), at k = 0 they are 4 and 12 (lift both), so LCA(6, 10) = 8. The alternative query 6 and 2 keeps u and v at every step; LCA(6, 2) = 4. Both pairs have equal depth, so neither shows a depth-balancing phase.

```text
8 4
8 12
4 2
4 6
12 10
12 14
```

### Rehearsal checks

- Use English locale, a readable viewport and a known saved layout.
- Disable Live layout for the graph drag comparison.
- Check Animate paused steps and reduced-motion preferences.
- Use Next to trigger floating text; verify the note remains legible long enough.
- The clips come from main 346e84b; if the demo build differs, check the slide-20 steps on it.
- Click through slides 14–18, 24 and 27 once in slideshow mode; each clip should play on →.
- Kerk confirms slides 7–12 and the first integration algorithm.
- Keep March 2027 as a target, not a guaranteed release date.
- If running late, shorten slide 20 to Graph only; the LCA clip was already shown on slide 16.

## Source notes

Deck media: https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/README.md
Historical screenshots: https://github.com/BJoozz/docsforfyp/blob/main/figures/README.md
Test evidence: https://github.com/BJoozz/docsforfyp/blob/main/04_figures_and_validation.md
Trial record: https://github.com/BJoozz/docsforfyp/blob/main/report/week10_user_trial_addendum.md
Architecture: https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

This master supersedes earlier suggested timings and Heap-first technical sequencing. Older drafts remain useful for evidence and Q&A.