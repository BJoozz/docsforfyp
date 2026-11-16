# VisuAlgo+ CA talk: cheat sheet

One glance per slide: the message, the points to hit and the line that leads to the next slide. Clip and demo slides also list their cues. The full wording is in [the master script](VisuAlgo_CA_Master_Script.md) and in the speaker notes. Both come from `ca-2026-11-16-deck-media/deck-build/speaking_script.json`.

33 minutes of talk, then 12 minutes of questions. Slides 7 to 12 are Kerk's; 20 to 23 are shared.

## 01 · VisuAlgo+

*Bao · Introduction · 00:00–00:30*

**Message:** We are rebuilding VisuAlgo, and we keep what it is for: learning and exploring algorithms.

- We are Bao and Kerk; the project is VisuAlgo+
- Rebuild the platform, keep its purpose
- Three parts today: how the design evolved, what each of us built, what the prototype taught us

**Next:** Let me start with why we are doing this.

## 02 · Motivation

*Bao · Introduction · 00:30–01:40*

**Message:** We keep VisuAlgo's strengths, and we follow Prof. Halim's directions: better interaction and a wider range of algorithms.

- VisuAlgo already has custom input and step-by-step runs; we keep them
- Prof. Halim's directions: easier graph editing, clearer parallel and curved edges, richer canvas interaction, side-by-side sorting
- He also encouraged a wider range of algorithms; LCA and Trie are topics I added
- My own focus, from competitive programming and teaching: explain why a step happens

**Next:** So why not just add these features to the existing site?

## 03 · Why rebuild the foundation?

*Bao · Introduction · 01:40–02:50*

**Message:** In the original code, one common change touches several topics, so we reorganised the foundation.

- The platform grew over many years; some parts are shared, such as the graph widget
- But each topic has its own input handling and state building
- So one editing change means changes and checks in several topics
- Sorting comparison: each pane needs its own state, with shared controls
- Decision: reorganise the foundation, and keep tools that fit, such as D3

**Next:** With that reason in mind, here is what we aim to deliver.

## 04 · Objectives and current scope

*Bao · Introduction · 02:50–04:00*

**Message:** We have three objectives and a working prototype; connecting the engine and a first release come next.

- Three objectives, one per card: a reusable visualization and interaction layer; a renewed website and execution foundation; a working prototype to validate
- Now: Graph, Tree and Sorting share one shell; students tried the prototype in Week 10
- Boundary: the visualizers run TypeScript in the browser; Kerk's C++ and WebAssembly engine is separate; connecting them is Semester 2 work
- Target: a first public release around March 2027; the original VisuAlgo stays online

**Next:** Let me go back to where it started: the early prototypes.

## 05 · Early visualizer prototypes

*Bao · Early Design · 04:00–05:30*

**Message:** Each early prototype tested one requirement that the final design had to meet.

- The prototypes were experiments toward the goals we discussed with Prof. Halim
- Graph: first separate edit and run views, then one canvas; input, positions and playback are separate, so moving a vertex keeps the same step
- Tree: new topics (LCA with Binary Lifting, Trie); an ancestor table under the tree; preview before Apply
- Sorting: the same array in every pane; each pane has its own state; one playback bar
- Naming: the standalone Graph rewrite is not the layout called V2

**Next:** While I was building the Graph rewrite and the Tree prototype, Kerk was designing the look of the new site.

## 06 · Two parallel foundations

*Bao · Early Design · 05:30–07:00*

**Message:** Two foundations grew side by side: my working visualizers and Kerk's design system.

- From late August, Kerk and I worked in parallel
- Mine: working algorithms, editors and playback, but separate apps with their own controls
- Kerk's: a design system from restyling visualgo.net (nine themes, twenty-six components) and a UI kit; also the first version of his engine
- Three requirements carried forward: keep the drawing available; keep playback familiar; show topic information beside the drawing

**Next:** Kerk will now show how he laid out the new visualisation page.

## 07 · From nine wireframes to two working layouts

*Kerk · UI/UX Evolution · 07:00–08:30*

**Message:** We narrowed nine wireframes to two layouts, and Bao built both, so we could compare real runs.

- Low-fidelity wireframes of the visualisation page, with an AVL tree as the example
- Same top bar and footer everywhere; the versions differ in where panels live and how they open
- Nine versions: seven layouts and two drag states of V7
- An early layout survey with students: formative, separate from the Week 10 trial
- Bao and I chose V2 (split rails) and V7 (draggable docks); Bao built Graph, Tree and Sorting in both

**Next:** So what did the comparison show?

## 08 · From V2 and V7 to V10

*Kerk · UI/UX Evolution · 08:30–10:00*

**Message:** V10 keeps the strengths of both: visible stacked panels from V2 and draggable tabs from V7, around a canvas that is never covered.

- Trade-off: V2 has fixed places with several panels open; V7 has movable panels but one tab per dock
- Bao and I discussed it, with Prof. Halim's feedback; we arrived at V10 in Week 9
- V10: panels stacked and visible together, tabs dragged between areas, several tab groups per area, the canvas in the centre
- Bao built the panel-group model and the shell
- Kerk implemented the agreed refinements and, on 18 October, merged the site and the visualizers into one application

**Next:** Bao will show the shell in detail later. Next, I will turn to the website and the execution architecture.

## 09 · Application boundaries

*Kerk · Engine & Website · 10:00–12:00*

**Message:** The prototype is one application with clear owners, and today the engine is still separate from it.

- One React and TypeScript application, built with Vite
- The site host owns routing, the top bar and the theme; it mounts Graph, Tree or Sorting
- Each visualizer owns its input and playback; a shared layer supplies the panel layout and presentation utilities
- Drawing: React Flow for Graph and Tree, D3 for some layout calculations, Canvas 2D for Sorting
- Boundary: the visualizers run TypeScript in the page; the WebAssembly engine is a separate project

**Next:** Let me now describe that engine.

## 10 · Engine foundation

*Kerk · Engine & Website · 12:00–14:30*

**Message:** The engine runs algorithms in a worker; the plan is that it describes their state and the visualizer explains it to the learner.

- C++ algorithms compiled to WebAssembly, running inside a worker
- The page and the engine talk through protocol messages, not direct calls
- Protobuf messages with graph and array representations; a Python path through Pyodide for tracing sorting algorithms
- Design question: expose enough state without tying the engine to the page layout
- Plan: the engine describes state and changes; the visualizer decides the note and the pseudocode line

**Next:** The harder part is connecting the engine to the visualizers.

## 11 · Reversible execution and integration

*Kerk · Engine & Website · 14:30–16:30*

**Message:** The engine and the visualizers keep history differently, so connecting them needs an explicit translation, one Graph algorithm first.

- Engine: a reversible journal, one record per step, and it can move backward
- Visualizers: Graph and Tree build all steps when a run starts; Sorting pulls from generators and keeps history
- Three things must stay consistent: node and edge identity, run identity, and the meaning of a step
- Bao's earlier integration experiment stays separate from the delivered visualizers
- Next step: one complete Graph integration, checked against the TypeScript behaviour

**Next:** Finally, the website that hosts all of this.

## 12 · Website integration

*Kerk · Engine & Website · 16:30–18:00*

**Message:** The site hosts the visualizers without duplicating their controls, and this boundary is where our contributions meet.

- The site owns the top bar and the theme; each visualizer supplies its topic-specific parts
- Bao built the working catalogue, the routes and the host adapters on the design system
- Kerk's consolidation and refinements made it a single application
- The wider website infrastructure and the engine still have to join the visualization layer
- Clear responsibilities avoid a second set of playback controls and conflicting theme state

**Next:** Bao will now explain how the visualization layer uses these boundaries for editing, comparison and explanations.

## 13 · My visualization contributions

*Bao · Algorithm Visualizers · 18:00–18:40*

**Message:** I built the visualizer foundations, the algorithms, the shell and the step explanations; I will show a few decisions you can see on screen.

- Foundations for Graph, Tree and Sorting
- Algorithms: each needs its own steps, pseudocode and inspector, for example LCA with Binary Lifting, and Trie
- The V10 shell and the integration into the site
- How each step explains itself, and how the behaviour is tested
- Next: a few selected decisions

**Next:** The first one is the shell.

## 14 · A shared shell with clear constraints

*Bao · Algorithm Visualizers · 18:40–19:50*

**Message:** You can move panels around without losing the drawing or the run.

- The layout has state: moving a panel must keep the canvas and the panel's input
- One model keeps the groups (left, right, bottom) and enforces size limits
- One resolver computes both the real layout and the drop preview, so the preview matches the result
- Saved layouts are versioned and checked; a broken one is repaired or reset
- Trade-off: less freedom than a fully general split layout, for a stable drawing and predictable drops

**Cues**

- Press → after the first two sentences. The clip is 16 seconds and plays once.
- Name each move as it lands: the split (4 s), the left group (9 s), under the drawing (14 s).
- The footer counter stays at 12 of 21. It is small on Zoom, so say the number.

**Next:** The same care for the run applies when the user edits the graph.

## 15 · Input, layout and playback

*Bao · Algorithm Visualizers · 19:50–20:55*

**Message:** Moving a vertex changes the drawing; changing a weight changes the problem. So they are stored separately.

- Four things stored separately: the graph document, the layout, the playback session, the presentation
- Drag a vertex: only the layout changes, so the run continues
- Change a weight: the document changes, so the old run is no longer valid
- A parallel edge is a separate edge, with its own identity and weight
- Result: consistent interaction, because each piece of state has one owner

**Cues**

- Press →. The clip is 16 seconds.
- Say each action as it happens: drag B (2 s), weight 1 to 5 and NO RUN (5 s), the second edge (8 s), its weight 2 (11 s).
- End on the final frame: two B → A edges, labelled 5 and 2.

**Next:** That was one run. Sorting comparison needs several runs side by side.

## 16 · Sorting comparison

*Bao · Algorithm Visualizers · 20:55–21:55*

**Message:** The panes share one input and one clock, but each keeps its own state; the counters are operations, not runtime.

- Every pane gets the same input and keeps its own state
- One shared clock moves all panes, one logical operation at a time; they can finish at different times
- Operations come from generators; history is kept for stepping back, which costs memory on long runs
- The counters count operations in the visualization, not CPU time

**Cues**

- Press →. The clip is 10 seconds.
- Say 'both at 48' when the panes pause.
- Last is a jump to the end, not a speed result.

**Next:** The next two slides are about a different question: how one step explains itself.

## 17 · LCA: explaining a decision to stay

*Bao · Algorithm Visualizers · 21:55–23:50*

**Message:** Floating text puts the reason beside the node, so a step with no movement still explains itself.

- Binary Lifting is a topic I added; a query has several stages and reads an ancestor table
- Clip: the root moves from 10 to 16, then LCA(8, 20): 8 lifts to 4; both stay at ancestor 16; both lift at k = 0; the answer is 16
- During the query no node moves, and 5 of the 12 steps only decide to stay
- With floating text the reason sits beside the node; Status keeps the full sentence
- Why: as I remember the Week 10 trial, newer learners often had to read Status; the benefit is not measured yet

**Cues**

- Press → after the first two sentences. The clip is 28 seconds; keep pace with it.
- Clip: the root moves to 16 (3 s), the query starts (5 s), 8 lifts to 4 (10 s), both stay at 16 (14 to 20 s), both lift (20 s), the answer 16 (25 s).
- After the clip, point at the three note crops on the left.
- Say clearly that the benefit is not measured yet.
- If you are late, skip the last sentence, on advanced tree topics.

**Next:** LCA shows a note when a step arrives. The next slide adds two more tools: motion while paused, and hover on the result.

## 18 · Pause and inspect the result

*Bao · Algorithm Visualizers · 23:50–25:10*

**Message:** Emphasis and progress are separate: motion while paused, a note when a step arrives, and hover on the result never advance or rerun the algorithm.

- Dijkstra from vertex 0 on visualgo.net's nine-vertex 'Big' example
- Paused at frame 17: the light on edge 2 to 3 keeps moving, the counter does not (Kerk's suggestion, my implementation)
- Next: a note beside 3 says 12 + 14 < 33, so update; 33 becomes 26
- Final frame: hover 8 gives 0, 2, 3, 8 with distance 42; hover 4 gives distance 46; read from the stored result
- The motion can be turned off and respects the reduced-motion setting

**Cues**

- Press →. The clip is only 14 seconds: paused at 17 (0 s), Next (3 s), Last (6 s), hover 8 (8 s), hover 4 (11 s).
- During the clip, only name the steps. Explain after it stops.
- The paused motion is subtle on Zoom: say 'still 17' and point at the edge from 2 to 3.

**Next:** The editors bring these features together.

## 19 · Editors for exploring an example

*Bao · Algorithm Visualizers · 25:10–26:00*

**Message:** The editors start from the user's own example, and let them ask several questions about it.

- Two entry points on the home page: the Graph Editor and the Tree Editor
- Start from an example you already have in mind, then try compatible algorithms on it
- Fits competitive programming practice: a small test, an observation, a counterexample
- The original VisuAlgo already accepts custom input; ours is a more explicit entry point
- An intended use; adoption is not measured

**Next:** Let us look at this live.

## 20 · Live demo

*Both · Demo & Evaluation · 26:00–29:00*

**Message:** One example, several questions: the same input drives different algorithms, in one interface.

- This is the running app, not a recording
- Graph Editor: one small graph; eleven graph algorithms on the same input
- Question 1, Dijkstra from A: hover E gives A, B, E with distance 7; hover D gives A, C, D with distance 3
- Question 2, recursive DFS on the same graph: the last frame replays the DFS tree (A, B, D, F, E, C)
- Kerk: one interface for every structure
- Tree Editor: pause on a step and hover a node to see its path to the root, its ancestors and its table row

**Cues**

- A proposed plan, checked on app 346e84b on 16 November. Settle it in rehearsal.
- Before the talk: open the app, load both editors once, choose Settings → Reset panel layout, check that 'Animate paused steps' is on, and return to the home page.
- 0:00 Home page → click the Graph Editor card. It opens on Breadth-First Search with the default graph: vertices A to F, eight directed edges.
- 0:10 Click Algorithms ▾ to show the list (11 algorithms in 5 groups), then press Esc.
- 0:20 Click DIJ. Click Next (frame 1 of 31), then Last. Hover E: A → B → E · distance 7. Hover D: A → C → D · distance 3.
- 0:50 Click DFS. The graph stays and the footer says NO RUN. Click Autoplay (31 frames, about 15 seconds). Final frame: Visited A, B, D, F, E, C.
- 1:30 Kerk speaks. Bao clicks HOME, then the Tree Editor card.
- 1:45 It opens on Binary Lifting, Query, root 8, u = 6, v = 2. Click the Ancestor table tab. Click Next twice (frame 2 of 6, note 'same ancestor · keep u, v'). Hover 6, then 14.
- 2:40 Return to PowerPoint and press → for slide 21.
- If a step fails, do not debug: use the clips on slides 15, 17 and 18, or B1 in the backup file. If time is short, stop after the DFS recap.

**Next:** So how did we evaluate all this?

## 21 · Evaluation and design response

*Both · Demo & Evaluation · 29:00–31:00*

**Message:** We tested the software and ran a formative trial in Week 10; floating text is a design response, and its effect is not yet measured.

- Bao: tests, a snapshot of 1 November: 3,273 unit tests and 151 browser cases passing
- Bao: an example of an independent check: cut vertices and bridges
- Kerk: Week 10: NUS students used V10 on their own for 15 to 20 minutes; sessions recorded; a short post-use test and feedback
- Bao: as I remember it, newer learners often had to read Status, so I added floating text, with legend and Status changes
- Not measured yet; a follow-up study needs defined tasks

**Next:** That brings us to the plan for Semester 2.

## 22 · Semester 2 priorities

*Both · Future Work · 31:00–33:00*

**Message:** Next: one Graph algorithm through the engine end to end, a stable and evaluated prototype, and a first release around March 2027.

- Kerk: the integration milestone is one Graph algorithm across the full application, checked against the TypeScript version
- Bao: stabilise the workflows we showed; evaluate the explanations with defined tasks; measure startup, seeking and memory
- Kerk: target a first public release around March 2027; the original platform stays available
- Bao: the wider ambition is the original range, then advanced topics; Heavy-Light and Centroid Decomposition are possibilities, not commitments
- Today we have the foundation and a working prototype

**Next:** That is the end of our talk.

## 23 · Questions

*Backup*

**Message:** Thank the audience and open the floor.

- Thank you
- Questions on the design decisions, the implementation or the evaluation plan
- The backup slides are in the second file

## B1 · Backup: recursive DFS recap (demo fallback)

*Backup*

**Message:** If the live Graph demo fails, this clip shows the recursive DFS recap.

- The same S, A, B, T graph as the clips on slides 14 and 15
- The final frame replays the DFS tree in visit order: S, A, T, then S, B
- Different from Dijkstra's final frame, where you hover a vertex to see its path

**Cues**

- Use this slide only if the Graph Editor part of the live demo fails.
- Press → to play. The clip is 8.5 seconds.

## B2 · Backup: preview before Apply

*Backup*

**Message:** An operation that changes the tree runs as a preview first; only Apply commits it.

- A changing operation needs a different contract from a read-only query such as LCA
- BST Insert 5 runs as a preview: the search path and the new node are visible, and I can step backward
- The tree and its text do not change until Apply
- Apply commits the result: the text gains the edge 6 5 and the run ends
- Heap insertion follows the same contract

**Cues**

- Explain the preview first, on the poster. Then press →: the clip is 8.6 seconds: two steps back, forward again, then Apply.

## B3 · Backup: correctness and limitations

*Backup*

**Message:** We check results with an independent method, and we are open about the limits.

- Cut vertices and bridges: an independent check removes each candidate and counts the components again
- Exact edge identity matters: removing one of two parallel edges keeps the connection
- Limits: sorting history is not bounded; Graph and Tree build all their steps up front
- Passing tests do not prove full correctness, performance or learning benefit
- AI tools assisted under my requirements; the design choices, acceptance and validation are mine

## B4 · Backup: evidence and ownership

*Backup*

**Message:** The main evidence is in the public repository, and each slide's notes link to its sources.

- Repository: BJoozz/docsforfyp
- The CA report and the architecture records
- The contribution map and the prototype history
- The Week 10 trial addendum
- Each slide's notes link to its sources and media
