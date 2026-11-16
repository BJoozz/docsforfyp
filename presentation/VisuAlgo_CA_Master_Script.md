# VisuAlgo+ CA Presentation: master script and structure

Working rehearsal draft • 16 November 2026 • 33 minutes plus 12 minutes for Q&A and buffer.

## How to use this version

The talk uses two PowerPoint files. `VisuAlgo_CA_Presentation.pptx` contains 22 timed slides and the Q&A slide (23). `VisuAlgo_CA_QA_Backup.pptx` contains four backup slides, B1 to B4; the recursive DFS recap comes first because it is the fallback for the live demo. Slides 14–18, B1 and B2 embed real-app clips; see [the media map](CA_PRESENTATION_MEDIA_USAGE.md). English speaking text, demo cues and source links are also embedded in speaker notes. Timing includes transitions and demonstrations; it is a rehearsal budget, not measured delivery time. Slides 7–12 are an evidence-based draft for Kerk to confirm and replace with his current details where necessary. No fabricated benchmarks or completed engine integration are claimed.

Owner confirmations: editing, playback and comparison were early goals discussed with Prof. Halim; LCA is the main Tree example; Bao recalls frequent Status reading among newer learners, especially for LCA, as motivation for floating text. The intended benefit has not been measured.

Order and test case, 16 November, at Bao's request: Sorting (slide 16) now comes before LCA (slide 17), because it stands apart from the two explanation slides. The LCA slide uses the Balanced · 10 nodes preset. Its clip first moves the root from 10 to 16 on camera, which also shows the re-root operation, then runs the query LCA(8, 20). The slide stresses what floating text is for.

Finalised on 16 November, at Bao's request: the captions under captures say only "Real app capture"; dates, commits and play instructions stay in the speaker notes and the media map. The two dated captions that remain, on slide 21 and backup B3, mark a snapshot of 1 November. Slide 20 says only "Live demo"; the text and cue in section 20 below are a working plan to settle in rehearsal. The backup slides moved to their own file.

Added on 16 November, on Bao's account: Prof. Halim also encouraged widening the range of algorithms VisuAlgo+ supports. There is no written record of this, and no specific topic is attributed to him. LCA with Binary Lifting and Trie were built in the standalone Tree prototype in September 2026 and are in the current app. Heavy-Light Decomposition and Centroid Decomposition are possible later extensions; they are not implemented and are not Semester 2 commitments.

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
| Q&A and buffer | Both | 12:00 | 23, then the backup file (B1–B4) |

## Slide-by-slide script

### 01. VisuAlgo+

**Bao · Introduction · 00:00–00:30**

**On slide**

- VisuAlgo+
- Rebuilding interactive algorithm visualization
- Truong Van Quoc Bao and Kerk Tai Heng · Supervisor: A/P Steven Halim
- NUS School of Computing · CP4101 Continuous Assessment · 16 November 2026

**Visual:** The current app's home page beside the title (app 346e84b): the VisuAlgo logo, the credit line, the Editors row and the top of the catalogue. Bao chose it on 16 November in place of a Dijkstra step, which slide 2 also shows.

**English script**

Good afternoon. We are Bao and Kerk, and our project is VisuAlgo+. We are rebuilding the platform while preserving its purpose: helping people learn and explore data structures and algorithms. Today we will explain the design process, our technical contributions, and what we learned from the working prototype.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/main.tex

### 02. Motivation

**Bao · Introduction · 00:30–01:40**

**On slide**

- More convenient graph editing: draw and change the graph you are studying, with parallel and curved edges handled clearly
- Richer interaction on the canvas: inspect a step, move things and see why a decision happens
- Sorting comparison on the same input: several algorithms on one dataset, side by side
- A wider range of algorithms: more topics, such as LCA with Binary Lifting and Trie, on foundations that make later ones easier to add

**Visual:** Four cards, each with a crop of today's prototype; the fourth shows the current Trie page (Insert "care", frame 5/7). Footer: directions proposed by Prof. Halim in early weekly meetings.

**English script**

VisuAlgo already lets students explore their own inputs and follow algorithms step by step. We want to preserve those strengths. In our early discussions, Prof. Halim proposed several directions for improving the platform. These included more convenient graph editing, clearer handling of parallel and curved edges, smoother and richer interaction with the canvas, and multiple sorting panes for comparison. He also encouraged us to widen the range of algorithms that VisuAlgo+ can visualize, so we wanted foundations that make new topics easier to add. These were goals from the beginning, and the prototypes helped us investigate how to reach them. The examples on the fourth card, LCA with Binary Lifting and Trie, are topics I added in the Tree prototype. My background in competitive programming and teaching also shaped my focus. When explaining an algorithm, I want the learner to understand why a decision happens, rather than only see the final answer. That means supporting examples that learners can change, inspect and discuss.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PREP.md

### 03. Why rebuild the foundation?

**Bao · Introduction · 01:40–02:50**

**On slide**

- Shared components already exist: for example, a graph widget used by several topics
- Module-specific logic complicates common changes: input handling and visual-state building live inside each topic
- New interactions need clearer state boundaries: comparison panes need their own state but shared controls

**Visual:** Simplified diagram: three original graph topics, each with its own input handling and state building, over one shared graph widget; consequence: one editing change means coordinated changes and checks across several topics.

**English script**

The original platform has grown through contributions over many years. It already has shared components, including a graph widget. However, substantial logic remains specific to individual modules. For example, graph topics contain their own input handling and visualization-state construction. A common editing change can therefore require coordinated changes and checks across topics. Sorting comparison raises another issue. Each pane needs its own execution state, while the controls must coordinate all panes. Dividing the screen alone does not solve this. These requirements gave us a reason to reorganize the foundation. We chose technologies and boundaries that support the interactions we want, while retaining useful tools such as D3 where they fit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PREP.md

### 04. Objectives and current scope

**Bao · Introduction · 02:50–04:00**

**On slide**

- A reusable visualization and interaction layer · now: Graph, Tree and Sorting share one shell; LCA and Trie already run on it · next: stabilize the shown workflows; add topics on the same foundations
- A renewed website and execution foundation · now: site with catalogue and routes; separate C++/WebAssembly engine foundation · next: connect them to the visualizers
- A working prototype with further integration ahead · now: students tried the prototype in Week 10 · next: validate, then an initial release around March 2027 (target)
- Current boundary: the visualizers run TypeScript algorithms in the browser; the engine is separate and connecting it is Semester 2 work

**Visual:** Three objective cards with NOW and NEXT chips, and a boundary band.

**English script**

Our objectives are to improve interaction across topics, build clearer boundaries so that new algorithms are easier to add, and validate the resulting functionality. We already have a working prototype that students have tried. Graph, Tree and Sorting currently run TypeScript implementations in the browser. Kerk has also developed a separate engine foundation. Connecting that engine and the wider website infrastructure to the visualizers remains part of the next stage. We are targeting an initial public release around March 2027, subject to integration and validation. The intended transition keeps the original VisuAlgo available and links to completed topics in VisuAlgo+. We will begin with how the early prototypes helped us make the interaction requirements concrete.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PREP.md

### 05. Early visualizer prototypes

**Bao · Early Design · 04:00–05:30**

**On slide**

- Graph: editing and playback on one canvas
- Tree: structural operations and ancestor information
- Sorting: independent runs with shared controls

**Visual:** Real stills of the standalone builds, rebuilt at their last documented commits (5fc06a0, c8b14e6, 46ce0a7, 9236a65) and captured on 16 Nov 2026: Graph prototype 1 run view, the Graph rewrite with one canvas, the Tree prototype's Binary Lifting table, and Sorting Room with two panes. Not the current app. The Tree card reads: LCA: ancestor table under the tree; Trie: insert and search along a prefix; Changes previewed before Apply. The prototype's Trie workspace (Insert and Search) is not pictured.

**English script**

The early prototypes were experiments in how to achieve the goals we had discussed with Prof. Halim. The first Graph prototype used separate editing and running views. In the standalone Graph rewrite, I kept one canvas and separated input, positions and playback. That let a learner move a vertex while continuing to inspect the same algorithm step. The Tree prototype also widened the range of topics: it included LCA with Binary Lifting, and Trie. Different algorithms brought different visualization needs: an ancestor table under the tree for LCA queries, and insert and search along a prefix for Trie. For operations that change the structure, I explored how to inspect a proposed result before applying it. Sorting explored a different interaction: several algorithms receive the same array, maintain their own states and advance through shared controls. Each prototype therefore tested a different requirement. The standalone Graph rewrite is distinct from the later layout named V2. I will use those names separately throughout the presentation.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

### 06. Two parallel foundations

**Bao · Early Design · 05:30–07:00**

**On slide**

- Bao · standalone visualizers, Jul–Sep 2026: TypeScript algorithms, editors and playback, reused later; Separate apps, each with its own bars and controls; Showed what each topic needs from a shared page
- Kerk · design system and UI kit, Aug–Sep 2026: Restyled visualgo.net: purple and gold, Inter, nine themes; 26 components, from the top bar to lesson cards; UI kit recreating visualgo.net's home and visualisation pages
- Requirements we carried forward: Keep the drawing available · Familiar playback across topics · Topic-specific information alongside

**Visual:** Left card: a still of Bao's standalone Graph rewrite (slide 5 showed all three prototypes). Right card: the home and visualisation screens of Kerk's design-system UI kit, which recreate visualgo.net's pages in the new style, rendered from commit 634b5be (3 Sep 2026). Both captured on 16 Nov 2026.

**English script**

From late August, Kerk and I worked in parallel. I was building the standalone Graph rewrite and the Tree prototype, while Kerk designed the look of VisuAlgo+. My visualizers already worked, and their algorithms, editors and playback became the base of the later builds. But each was a separate app with its own bars and controls, so they needed one page and one look. Kerk restyled visualgo.net into a design system with nine themes and twenty-six components. His UI kit recreates visualgo.net's home and visualisation pages, and the site I built later follows his home page. Around the same time, Kerk also committed the first version of his C++ and WebAssembly engine foundation, which he will present later. The prototypes gave us three requirements: keep the drawing available, keep playback familiar across topics, and show topic-specific information beside the drawing. Kerk will now show how he laid out the new visualisation page.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/design-history/README.md

### 07. From nine wireframes to two working layouts

**Kerk · UI/UX Evolution · 07:00–08:30**

**On slide**

- Kerk's wireframes, V1–V9: One top bar and footer; seven panel layouts and two drag states of V7
- V2 and V7 chosen together: By Kerk and Bao, after an early layout survey of students that Kerk organised
- Bao's six working builds: Graph, Tree and Sorting in both layouts: his prototypes on Kerk's tokens and themes
- Same features in both builds, so our discussions compared the layouts on real runs, not just as drawings

**Visual:** Left: the "At a glance" grid of Kerk's wireframe page (commit 69aa8e4, 4 Sep 2026), nine frames V1–V9 with V2 and V7 outlined on the slide. Middle: the V2 and V7 wireframes. Right: Bao's working Graph builds in V2 (split rails) and V7 (docks). He made them on 20–27 September; the stills show them as they stood on 17 October, at commit ae63a62, the last one that still had them.

**English script**

Alongside the design system, I drew low-fidelity wireframes of the visualisation page, with an AVL tree as the example. I gave every version the same top bar and footer. e-Lecture is a panel, and the footer holds a scrubber, zoom and shortcuts. The versions differ only in where the panels live and how they open. There are nine versions: seven layouts, and two that show V7 during a drag and after the drop. I then organised an early layout survey with students. It was formative input, separate from the Week 10 trial. After that, Bao and I chose two layouts together: V2 with split rails, and V7 with draggable docks. Bao built Graph, Tree and Sorting in both layouts, reusing his standalone prototypes and my design tokens and themes. The two layouts had the same features, so when we discussed them, we were comparing the layouts themselves, on real runs rather than drawings.

**Team review:** Kerk to confirm this slide: the wireframes, the student feedback he organised (no numbers are on record) and how the choice is described. The script was rewritten on 16 November from the records and Bao's account.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/design-history/README.md

### 08. From V2 and V7 to V10

**Kerk · UI/UX Evolution · 08:30–10:00**

**On slide**

- From V2 · split rails: Panels stacked and visible together; Its panel positions as V10's default
- From V7 · draggable docks: Panels moved by dragging their tabs; A bottom area and splitters to resize
- V10 · panel groups: The canvas stays central and uncovered; Tab groups around the drawing; One playback bar for every topic
- Discussed together: Kerk and Bao, with Prof. Halim's feedback
- Bao: built V10's panel-group model and shell (16–18 Oct)
- Kerk: refined V10's dragging, controls and fonts; made its site and visualizers one app (18–22 Oct)

**Visual:** Left: Bao's working Tree builds in V2 (split rails) and V7 (docks), as of 17 October, with what V10 keeps from each. Right: the current app (Tree Editor, app 346e84b) with coloured outlines for the tab groups, the canvas and the shared playback bar.

**English script**

Comparing the two builds showed a trade-off. V2 keeps every panel in a fixed place and lets several be open at once. V7 lets you move panels, but shows only one tab per dock. Bao and I discussed this, with feedback from Prof. Halim. In Week 9, we arrived at V10, which keeps both strengths. Panels stay stacked and visible together, as in V2, and you drag tabs between areas, as in V7. Each area can now hold several tab groups, and the canvas stays in the centre, never covered. Bao built the panel-group model and shell. I then implemented refinements we agreed on, such as drag sensitivity, controls and fonts. On 18 October, I merged the site and the visualizers into one application, so we now fix the shell in one place. Bao will show the shell in detail later. Next, I will turn to the website and execution architecture.

**Team review:** Kerk to confirm this slide: his refinements, the consolidation and how the discussion with Prof. Halim is described. The script was rewritten on 16 November from the records and Bao's account.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/design-history/README.md

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

**Visual:** 2×2 cards with a short detail and a small current-app thumbnail each. Card 02 reads: implemented: LCA (Binary Lifting), Trie, recursive DFS, Bellman-Ford, Prim, bridges, AVL, heap, lazy segment tree; each with its own steps, pseudocode and inspector. Its thumbnail is the current Trie page.

**English script**

My contribution covers the visualizer foundations, the V10 shell and integration into the site. It also covers the algorithms themselves: I added topics such as LCA with Binary Lifting and Trie, and each algorithm needs its own step model, pseudocode and inspector. I also worked on how individual steps communicate their meaning and how the behavior is tested. I will show selected decisions. The examples connect the underlying state model to something a user can directly observe.

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
- Add a parallel edge: a separate edge (its own identity and weight: 5 and 2)
- Who owns which state: Document (nodes, edges, weights) · Layout (positions) · Session (run and selected step) · Presentation (derived highlights)

**Visual:** State-ownership diagram and three outcome cards beside clip `03b_graph_drag_edit_parallel.mp4` (16.2 s): B dragged at frame 12/21; B → A changed from 1 to 5 in Draw graph → Edges, giving NO RUN; a second B → A edge drawn on the canvas and given weight 2. The first take, `03_graph_drag_then_edit.mp4`, is kept as an alternative.

**English script**

Moving a vertex changes the drawing. Changing an edge weight changes the problem the algorithm is solving. So I keep the graph document, layout, playback session and presentation separate, as listed on the slide. [Press → to play the clip.] I drag B: the counter stays at 12. Changing B to A from 1 to 5 edits the document and invalidates the run. Then I draw a second edge from B to A and give it weight 2 in the text. The two parallel edges are separate edges, each with its own identity and weight, for the editor, the drawing and the algorithms. The aim is consistent interaction backed by clear state ownership.

**Delivery cue:** Clip, 16.2 s.
- 0–1.0 s: paused at 12/21, relaxing B → A.
- 1.0–3.5 s: B dragged; still 12/21.
- 3.5–7.2 s: Draw graph → Edges, "B A 1" becomes "B A 5": label 5, NO RUN, NO ACTIVE RUN.
- 7.2–9.2 s: a new edge is dragged on the canvas from B's handle to A's handle.
- 9.2–10.8 s: two B → A edges, curved apart; the new one has no weight yet, the Edges text gains "B A", and the app notes that it counts as 1.
- 10.8–12.2 s: typing " 2" on that line gives the second edge its label 2; the notice goes away.
- 12.2–16.2 s: both edges carry their own weights, 5 and 2; still NO RUN.

Live layout was off. The app has no on-canvas weight edit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_GRAPH_CASE.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/03b_graph_drag_edit_parallel.mp4

### 16. Sorting comparison

**Bao · Algorithm Visualizers · 20:55–21:55**

**On slide**

- The same dataset in every pane: 12 values, Bubble and Selection
- One clock, independent operation streams: both panes pause at operation 48
- Retained history supports seeking: the clip ends with Last, a seek to the final operation
- Operation counts are not CPU time

**Visual:** Codex clip `02_sorting_shared_clock.mp4` (10.4 s), poster at operation 48.

**English script**

Sorting comparison gives every pane the same input while keeping its execution state independent. A shared clock advances the active panes by logical operations. They can show different actions and finish at different times. Generators produce the operations. Upcoming operations use bounded buffering, while retained history supports backward seeking. Keeping that history has a memory cost on long runs. [Press → to play the clip.] The counters describe the visualization's operations. They are not CPU runtime measurements, and equal operation indices do not guarantee equal computational cost. This makes the comparison useful for examining behavior, while keeping the interpretation honest.

**Delivery cue:** Codex clip, 10.4 s: Bubble and Selection on 8, 3, 10, 1, 6, 4, 12, 2, 9, 5, 11, 7 at 12 operations/s; both pause at operation 48 (Bubble 27 compares, 19 swaps; Selection 40 compares, 4 swaps); Last ends at 92 and 86 operations. Live alternative: step back once with Prev, only if time allows.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16/02_short_clips/02_sorting_shared_clock.mp4

### 17. LCA: explaining a decision to stay

**Bao · Algorithm Visualizers · 21:55–23:50**

**On slide**

- Floating text puts the reason beside the node: 9 of this query's 12 steps carry a note; no node moves during the query
- Query: LCA(8, 20) = 16 (Balanced · 10 nodes; root moved 10 → 16)
- Depth gap 2: lift u from 8 to 4
- Same ancestor 16: keep u and v
- Ancestors 10 and 18 differ: lift both

**Visual:** Clip `01d_lca_reroot_on_camera_8_20.mp4` (27.9 s, app 346e84b): the root is moved from 10 to 16 on camera, then the query runs. The left column shows three of the run's notes, cropped from stills of frames 4, 8 and 9: "gap 2 ≥ 2 · lift u", "same ancestor · keep u, v" and "differ · lift both". Earlier clips, kept as alternatives: `01c_lca_reroot_8_20.mp4` (the same query without the re-root on camera), `01b_lca_keep_then_jump.mp4` (LCA(6, 10) = 8) and `01_lca_equal_ancestors.mp4` (LCA(6, 2) = 4), both on the default tree.

**English script**

Binary Lifting is one of the topics I added. A query has several stages and reads an ancestor table. [Press → to play the clip.] I move the root from 10 to 16 with one control. Then I ask for the LCA of 8 and 20. First 8 must catch up: the gap is 2, so it stays at k = 3 and 2, and at k = 1 it lifts two levels, to 4. At k = 3, 2 and 1 both ancestors are 16, so u and v stay. At k = 0 they are 10 and 18, so both lift, and their shared parent, 16, is the answer. The cursors stay while the ancestors are equal, because they look for the highest ancestors that differ. During the query no node moves, and five of the twelve steps only decide to stay. Without a note, those steps look the same. With floating text, the reason sits beside the node, so the learner can read it without leaving the tree. Status keeps the full sentence, and the pseudocode and the table reads agree with it. My recollection from the Week 10 trial is that newer learners had to read Status frequently, especially for algorithms with several stages such as LCA. Floating text is my design response. We still need to evaluate whether it reduces attention switching. The same rooted tree and ancestor queries are also groundwork for more advanced tree topics later.

**Delivery cue:** Clip, 27.9 s; keep talking over it. Set up before recording: preset Balanced · 10 nodes (root 10), u = 8, v = 20. The re-root is in the clip.
- 0.0–1.5 s: the preset with root 10. Root under Structure reads 10 and Depth reads 3.
- 2.4–3.3 s: typing 16 in the Root control moves the root. The ROOT badge moves to 16, the tree is laid out again and the view re-fits. Depth reads 4; u and v are kept.
- Frame 1/12 (5.0 s): depths 4 and 2.
- Frames 2–3 (6.2 s, 8.2 s): k = 3 and k = 2, the gap 2 is smaller than 8 and 4, so u stays ("gap 2 < 8 · keep u", "gap 2 < 4 · keep u").
- Frame 4 (10.2 s): k = 1, "gap 2 ≥ 2 · lift u". Frame 5 (12.2 s): u moves from 8 to 4, "↑ 2 levels".
- Frames 6–8 (14.3 s, 16.3 s, 18.3 s): k = 3, 2, 1, both ancestors are 16, "same ancestor · keep u, v".
- Frame 9 (20.3 s): k = 0, ancestors 10 and 18 differ, "differ · lift both". Frame 10 (22.3 s): u = 10, v = 18.
- Frame 11 (24.2 s): same parent, 16. Frame 12 (25.4 s): LCA(8, 20) = 16.

Say that floating text is a design response to a formative observation; its effect is not measured.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/week10_user_trial_addendum.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/01d_lca_reroot_on_camera_8_20.mp4 (stills in https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/stills/)

### 18. Pause and inspect the result

**Bao · Algorithm Visualizers · 23:50–25:10**

**On slide**

- Paused motion keeps the current relationship visible: the counter stays at frame 17 while edge 2 → 3 is emphasised
- A short note explains the step on arrival: frame 18, 12 + 14 < 33 · update
- Final Dijkstra hover reveals a computed path: 8: 0 → 2 → 3 → 8, distance 42 · 4: distance 46

**Visual:** Clip `04b_dijkstra_big_note_pause_hover.mp4` (14.0 s): Dijkstra from 0 on the nine-vertex Big preset (visualgo.net's TESSELLATION). The first take, on the four-vertex S, A, B, T graph, `04_dijkstra_note_pause_hover.mp4`, is kept as an alternative.

**English script**

I also separate visual emphasis from algorithm progress. This is Dijkstra from vertex 0 on visualgo.net's nine-vertex "Big" example. [Press → to play the clip, and say each cue as it happens.] Paused at frame 17: the edge from 2 to 3 keeps moving. Next: a note arrives. Last. Hover 8. Hover 4. [The clip stops on the hover over 4.] While the run was paused at frame 17, the edge streak and the glow kept moving, but the counter stayed at 17. That emphasizes the current relationship without advancing the computation, which helps the learner inspect it for longer. Kerk suggested this paused motion; I implemented it. Next brought a short note beside 3: 12 plus 14 is less than 33, so update; the badge on 3 changed from 33 to 26. Floating text handles the arrival of a step; paused motion handles waiting on it. At the final frame, hovering 8 showed its computed shortest path, 0 to 2 to 3 to 8, distance 42; hovering 4 showed 0 to 2 to 3 to 4, distance 46. The application derives the highlight from the stored result; it does not rerun. Motion can be turned off, and reduced-motion behavior matters for accessibility.

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
- Try compatible algorithms
- Build small tests and investigate conjectures

**Visual:** Current Editors section of the home page (app 346e84b) above a three-step flow; limits line: custom input already exists in VisuAlgo, this is a more explicit entry point; adoption not measured.

**English script**

The Graph and Tree Editor entry points support a workflow that begins with an example. The user may already have a graph in mind and want to investigate it. This can support competitive programming practice: construct a small test, check an observation, or search for a counterexample. The original VisuAlgo already supports custom inputs. Our addition is a more explicit entry point and workflow centered on that input. Tree Editor currently focuses on Binary Lifting, BST and AVL, with input conditions still applying. This is an intended use case, and we have not measured long-term adoption. We will now show a short continuous workflow.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

### 20. Live demo

**Both · Demo & Evaluation · 26:00–29:00**

**On slide**

- Live demo
- A short demo of VisuAlgo+

**Visual:** A navy divider slide with only those two lines. At Bao's request (16 November), what the demo shows is settled here in the script, not on the slide. The text and cue below are a working plan to settle in rehearsal.

**English script**

Bao: I will start with a prepared graph so that we can focus on exploration. First, Dijkstra answers a shortest-path question. We can inspect the result, then switch to recursive DFS on the same compatible graph and ask about traversal instead. The final DFS motion recaps the traversal tree. The input is the starting point for different questions.

Kerk: The site gives these activities a common interface. The user can return to the editors and choose a different structure without learning a completely separate navigation system.

Bao: In Tree Editor, I will use the small tree from the LCA example. We can inspect ancestor information and the query result. If we change the relevant input or query, the old run must no longer represent the new question. These interactions are intended to support someone thinking through an example, as well as someone studying a named algorithm.

[Run the sequence below. Narrate only the action currently on screen. Allow the audience to observe. If a live action fails, return to the prepared slide and explain the expected state rather than debug during the talk.]

**Delivery cue:** 0:00–0:20 Graph Editor and input; 0:20–1:00 Dijkstra result; 1:00–1:40 recursive DFS and final recap; 1:40–2:40 Tree Editor and LCA ancestor inspection; 2:40–3:00 return to slides. Avoid repeating the full floating-text explanation. Fallback: if a live step fails, use the clips on slides 15, 17 and 18, or the recursive DFS recap, the first slide of the backup file; do not debug during the talk.

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

**Visual:** Four-step roadmap, each with a one-line detail. Limits lines: March 2027 is a target; possible later extensions, not Semester 2 commitments: advanced tree topics such as Heavy-Light Decomposition and Centroid Decomposition.

**English script**

Kerk: Our next integration milestone is one Graph algorithm working across the full application. The input, engine execution and visualizer playback should agree on node and edge identity, step meaning and cancellation. We can check the result against the current TypeScript implementation before expanding the integration.

Bao: In parallel, I want to stabilize the workflows we have shown and evaluate the revised explanations. A task could ask a learner to explain why an LCA step keeps both nodes in place. We can observe how they use the canvas, ancestor table and Status, rather than assume that additional animation helps. We also need measurements for startup, seeking and memory on longer runs.

Both: We are targeting an initial public release around March 2027, depending on integration and validation. The current transition plan keeps the original platform available and links to completed topics. Our broader ambition is to cover the original algorithm range and, later, to add advanced topics. For example, the rooted-tree and ancestor-query work behind LCA could support Heavy-Light Decomposition or Centroid Decomposition. Those are possibilities, not Semester 2 commitments; integration, validation and stability come first. The current work provides the visualizer foundations and a working prototype on which to build that release.

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

**Backup file:** open `VisuAlgo_CA_QA_Backup.pptx` before the talk. It holds four slides for Q&A: B1 recursive DFS recap (also the fallback for the live demo), B2 preview before Apply (BST), B3 correctness and limitations, B4 evidence and ownership.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/main.tex

## Backup file

`VisuAlgo_CA_QA_Backup.pptx` holds the four backup slides, pages B1 to B4. They are outside the timed talk. The recursive DFS recap is first because it is the fallback for the live demo.

### B1. Backup: recursive DFS recap (demo fallback)

**Backup / demo fallback, outside timed talk**

**On slide**

- Same graph, another question: recursive DFS from S on the S, A, B, T graph of slides 14–15
- The final frame replays the DFS tree: glow and streak in visit order, S → A → T, then S → B
- Different from Dijkstra's hover: a recap of the traversal, not a path query

**Visual:** Clip `06_dfs_recursive_recap.mp4` (8.5 s): Last to 21/21, visited S, A, T, B; the final frame replays the DFS tree about every 3 s.

**English script**

Use this slide only if the live Graph Editor part of the demo on slide 20 fails. Recursive DFS runs on the same S, A, B, T graph as the Dijkstra clips on slides 14 and 15. On its final frame, the drawing replays the DFS tree in visit order every few seconds: S to A to T, then S to B. This is a different final behaviour from Dijkstra's hover path.

**Delivery cue:** Press → to play the clip.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/06_dfs_recursive_recap.mp4

### B2. Backup: preview before Apply

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

### B3. Backup: correctness and limitations

**Backup / Q&A, outside timed talk**

**On slide**

- Independent oracle for cut vertices and bridges
- Stable edge identity for parallel edges
- Long sorting histories still cost memory

**Visual:** Historical still (app 662e7b3, 1 Nov 2026), now larger.

**English script**

For cut vertices and bridges, an independent oracle removes each candidate and compares connected-component counts. Exact edge identity matters because removing one of two parallel edges is different from removing the connection altogether. Other limits include unbounded retained sorting history and upfront sequence construction in Graph and Tree. Passing tests cover the tested cases and do not establish complete correctness, performance or learning benefit. AI tools assisted implementation and review under my requirements. I remained responsible for the design choices, acceptance and validation.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

### B4. Backup: evidence and ownership

**Backup / Q&A, outside timed talk**

**On slide**

- CA report and architecture records
- Contribution map and prototype history
- Week 10 trial addendum
- Source links in each slide’s notes

**Visual:** Four evidence cards with repository paths.

**English script**

Primary evidence lives in BJoozz/docsforfyp: report/main.tex, 03_architecture_and_decisions.md, docs/CA_PRESENTATION_CONTRIBUTION_MAP.md, docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md and report/week10_user_trial_addendum.md. Prototype history: BJoozz/graph-algorithm-visualizer, graph-visualizer-v2, tree-visualizer and sorting-algorithm-visualizer. Application: kerktaiheng/visualgo-plus-design (fork BJoozz/visualgo-plus-design), main 346e84b. In the main deck, slides 1, 2, 8 and 13–19 use real captures of app 346e84b from 15–16 November, and so do the first two slides of the backup file; the correctness slide of the backup file is a historical capture of 662e7b3 (figures/README.md); slide 5, and the left card of slide 6, show the standalone prototypes rebuilt at their documented commits; slides 6 to 8 use design-history artifacts rendered from their own commits: Kerk's UI kit (634b5be) and wireframes (69aa8e4), and Bao's working V2 and V7 builds (ae63a62). The 15–16 November clarifications record early supervisor direction, the LCA selection and Bao's recollection about Status reading. They also record Bao's account that Prof. Halim encouraged widening the range of algorithms in general (no written record; no specific topic is attributed to him). LCA with Binary Lifting and Trie were built in the standalone Tree prototype in September 2026 and are in the current app. Heavy-Light Decomposition and Centroid Decomposition are possible later extensions and are not implemented. Kerk should review slides 7–12 against his current engine and website work before the joint presentation.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

## Demo preparation and remaining work

Slides 14–18 now play real-app clips embedded in the deck (app `346e84b`, recorded 15–16 November), so no window switching is needed during the technical section. The live demo stays on slide 20. Each clip has a poster frame on the slide as its static fallback; press → or click to play. Details: [media map](CA_PRESENTATION_MEDIA_USAGE.md) · [changelog](CA_DECK_CHANGELOG.md).

| Clip or live action | Slide | Length | Fallback |
|---|---:|---:|---|
| V10: split, join and dock Status while paused | 14 | 16.3 s clip | Poster: Status docked under the drawing at 12/21 |
| Vertex drag, weight edit and a parallel edge | 15 | 16.2 s clip | Poster: both B → A edges, labelled 5 and 2 |
| Sorting shared input and clock | 16 | 10.4 s clip (Codex) | Poster: both panes at operation 48 |
| Root moved from 10 to 16, then LCA(8, 20) | 17 | 27.9 s clip | Poster: frame 9/12, "differ · lift both" |
| Dijkstra on the nine-vertex Big graph: paused motion, note and final hover | 18 | 14.0 s clip | Poster: frame 18/53 with the 2 → 3 update note |
| Joint editor workflow | 20 | 3 min live | Clips on slides 15–18; backup B1 for the DFS recap |

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

Choose the preset Balanced · 10 nodes (root 10), then set Root to 16 under Edit tree → Structure; the slide-17 clip shows this step. The clip then queries 8 and 20: 8 first lifts two levels to 4; at k = 3, 2 and 1 both ancestors are 16, so the cursors stay; at k = 0 the ancestors are 10 and 18, so both lift; LCA(8, 20) = 16. The earlier clips use the default tree (root 8): LCA(6, 10) = 8 and LCA(6, 2) = 4.

```text
10 4
4 2
4 6
6 8
10 16
16 12
12 14
16 18
18 20
```

### Rehearsal checks

- Use English locale, a readable viewport and a known saved layout.
- Disable Live layout for the graph drag comparison.
- Check Animate paused steps and reduced-motion preferences.
- Use Next to trigger floating text; verify the note remains legible long enough.
- The clips come from main 346e84b; if the demo build differs, check the slide-20 steps on it.
- Click through slides 14–18 of the main deck and B1–B2 of the backup file once in slideshow mode; each clip should play on →.
- Open both files before the talk and share the whole screen on Zoom, not one window, so the audience also sees the backup file when you switch to it.
- Kerk confirms slides 7–12 and the first integration algorithm.
- Keep March 2027 as a target, not a guaranteed release date.
- If running late, shorten slide 20 to Graph only; the LCA clip was already shown on slide 17.

## Source notes

Deck media: https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/README.md
Historical screenshots: https://github.com/BJoozz/docsforfyp/blob/main/figures/README.md
Test evidence: https://github.com/BJoozz/docsforfyp/blob/main/04_figures_and_validation.md
Trial record: https://github.com/BJoozz/docsforfyp/blob/main/report/week10_user_trial_addendum.md
Architecture: https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

This master supersedes earlier suggested timings and Heap-first technical sequencing. Older drafts remain useful for evidence and Q&A.