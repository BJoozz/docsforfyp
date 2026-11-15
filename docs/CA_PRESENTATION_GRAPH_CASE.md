# Technical case 1 — Graph editing and reproducible playback

Prepared 15 November 2026. Working presentation draft, following [Part 1](CA_PRESENTATION_PREP.md).
Evidence: report, current main source, existing tests and selected commit history. No tests or live browser demo were executed during this preparation; demo steps below require rehearsal. Commit history is supporting engineering evidence, not proof of exclusive individual authorship.

## Main message

Moving a vertex changes the drawing. Changing an edge or weight changes the algorithm's input. Keeping those changes separate allows editing and execution to share one canvas without showing an old run as if it belonged to a new graph.

## Slide draft

**One canvas, consistent editing and playback**

- **Problem:** keep the edited graph and the displayed execution consistent.
- **Design:** separate graph data, layout, run session and presentation.
- **Behaviour:** moving a vertex keeps the run; changing the input invalidates it.
- **Playback:** select recorded steps for forward/backward inspection; reject stale timer events.

Visual suggestion: two screenshots of the same paused graph before/after moving one vertex, followed by an input edit that clears the run. Use actual screenshots after rehearsal, not simulated evidence.

| Owner | Holds | Why it matters |
|---|---|---|
| Graph document | Nodes, edges, weights, identities, topology revision | Identifies which input a run belongs to |
| Layout | Positions and pinning | Moving a node does not change the algorithm input |
| Session | Sequence, index, run identity, status | Controls which recorded step is displayed |
| Presentation | Derived highlights and badges | Playback decoration does not overwrite the authored graph |

## Problem, alternatives and decision

**Problem:** Separate editing and animation representations can drift apart. Sharing a canvas still requires clear ownership: positions, input and algorithm highlights must not accidentally overwrite one another.

**Alternatives for explaining the trade-off (not a claim that every option was experimentally evaluated):**

1. Separate editing and animation canvases: introduces another representation to synchronise.
2. Put input, layout and highlights in one mutable state: fewer initial boundaries, but input changes and presentation changes become harder to distinguish.
3. Selected design: a canonical document with separate layout, session and derived presentation, rendered on one persistent canvas.

The contribution is the integration and enforcement of these boundaries for algorithm visualization; React Flow itself is an existing library.

## English speaking script — approximately 2–3 minutes

One technical challenge was keeping graph editing and algorithm playback consistent.

A student should be able to arrange a graph, start an algorithm, and inspect its execution without losing the graph they were working with. But two actions that look similar on the screen can have very different meanings. Moving a vertex changes only the drawing. Changing an edge weight changes the input to the algorithm.

My visualization work addresses this by separating four kinds of state.

The graph document stores the vertices, edges and weights. The layout stores their positions. The run session stores the recorded steps and the current playback position. Finally, the presentation determines which vertices and edges are highlighted at that step. These parts are combined on the same canvas.

This separation gives us a clear rule for editing. Dragging a vertex updates the layout, so the existing run can remain valid. A semantic change to the graph updates its revision. If that revision differs from the one used to start the run, the old session is discarded. This prevents the interface from presenting a result calculated for a different input.

For playback, the current graph implementation builds the step sequence when a run starts. Moving forward or backward selects a step from that sequence and derives its presentation. This makes inspection straightforward, although generating and storing the full sequence has a startup and memory cost for long runs.

There is also an asynchronous issue. A timer from an earlier run must not advance a new run. Each run therefore has its own identity, and the session ignores timer events that do not match it.

The repository contains tests for revision-based invalidation, previous and next steps, seeking, and stale timer events. I will demonstrate the visible behaviour by pausing a run, moving a vertex, and then changing the graph input. The distinction is simple for the user, but it depends on keeping the underlying responsibilities separate.

## Proposed demo — 60–90 seconds

Use a small weighted graph with non-negative weights and Dijkstra. Keep Live force layout off for a predictable drawing. Rehearse the exact editor controls before presenting.

1. Load a small graph; show the input and arrangement.
2. Press **Next** from idle to create a paused run at its first frame, then advance a few frames. Alternatively Autoplay starts and plays a run.
3. Pause and drag a vertex. Expected: the position changes while the selected algorithm step remains.
4. Use Previous and Next. Explain that playback changes algorithm presentation, not the authored topology.
5. Change an edge weight through the editor. Expected: the old run clears because the input revision changed.
6. Start again. Explain that the new sequence is based on the edited input.

Do not promise a different shortest-path result unless the chosen weight actually changes it. Rewinding a run does not undo the user's layout changes. Input invalidation is not incremental recomputation.

## Q&A backup

**Why is one canvas not enough on its own?**  
The same drawing surface can still mix unrelated state. The important part is who owns input, positions and execution state, and which changes invalidate a run.

**Why not recalculate automatically after every edit?**  
The implemented workflow discards an obsolete run and starts a new sequence on user action. It avoids implying that the old frame remains meaningful after an input change. This is not a claim that incremental execution is impossible.

**Why store the full sequence?**  
It makes previous/next and seeking straightforward. The cost is generating and retaining the sequence up front; this preparation does not establish a performance bound or benchmark.

**What happens to an old timer?**  
A tick includes its session ID. The reducer ignores it unless the current session is playing and its ID matches. Timer cleanup is also performed by the hook.

**What is yours versus React Flow?**  
React Flow supplies the canvas interaction/rendering foundation. The project-specific work includes semantic graph state, layout separation, algorithm step production, presentation mapping, invalidation and playback lifecycle. Confirm final individual wording against team contribution records.

**Is this already the WASM engine?**  
The report describes browser TypeScript algorithm sequences and a separate WASM engine foundation. This case concerns the visualizer/session layer; it does not assert completed WASM integration.

**What evidence supports reliability?**  
Existing reducer tests cover revision invalidation, stepping, seeking and stale timer rejection. This review inspected those tests, not a fresh execution result. Live behaviour still needs rehearsal.

## Commit-based engineering example — backup, not another main-slide topic

[9baa117](https://github.com/BJoozz/visualgo-plus-design/commit/9baa117fc6d97ecf377f4f32f1406dba0e338549): inspected the message and actual patch.

- Before: changing Speed restarted the full timeout. Repeated slider movement could postpone the next step repeatedly.
- After: graph and tree share a countdown helper retaining the elapsed time for the current session state.
- Example from the added test: after 300 ms of a step, changing its delay to 1,000 ms leaves 700 ms, not a fresh 1,000 ms.
- The patch adds countdown regression tests; it preserves the existing stale-session protection.
- Useful Q&A point: correctness includes interaction timing, not only the final algorithm result.

The file history also contains [0394b64](https://github.com/BJoozz/visualgo-plus-design/commit/0394b6472b104cf516477750d387cb63c7833f02), whose message describes V10 consolidation into one app. That move is not evidence that the session architecture originated in that commit. The current architecture document explicitly traces the foundation to graph-visualizer-v2 at c8b14e6.

## Source map

- [Report: state ownership](../report/main.tex): section “State ownership and reproducible playback”.
- [Architecture](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/docs/graph/ARCHITECTURE.md): persistent canvas, inherited foundation, page ownership, actual Autoplay/Next controls.
- [Editor](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/src/graph/editor/useGraphEditor.ts): document commits notify topology changes; node dragging commits layout.
- [App composition](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/src/graph/app/App.tsx): connects editor topology changes to session invalidation and passes drag handlers into GraphCanvas.
- [Session reducer](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/src/graph/visualization/sessionReducer.ts): source revision, run ID, stepping, seeking and tick guards.
- [Session hook](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/src/graph/visualization/useVisualizationSession.ts): sequence creation, timer setup/cleanup and countdown.
- [Reducer tests](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/src/graph/visualization/sessionReducer.test.ts): inspected existing checks.
- [Countdown regression tests](https://github.com/BJoozz/visualgo-plus-design/blob/main/prototypes/src/graph/visualization/playbackCountdown.test.ts): inspected in commit patch.

## Remaining preparation

- Rehearse the proposed demo and capture real before/after screenshots.
- Confirm individual contribution wording with the existing evidence record.
- Do not claim measured learning gains or benchmarked performance from this architecture alone.
- Next technical cases remain sorting comparison and meaningful algorithm steps.
