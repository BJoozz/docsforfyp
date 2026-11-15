# CA presentation: selected visual evidence

Prepared 15 November 2026. This is an asset-selection note, not a revised presentation outline or a new evaluation result.

The documentation repository was fast-forwarded from `f399626` to `99990d0`. The latest contribution map and interactive-demo plan take precedence over the earlier narrow three-case shortlist. In particular, the assets must give Tree, the shared shell and editor entry points visible space alongside Graph and Sorting. The report's attribution update is retained: Kerk suggested paused-step motion; Bao implemented it.

## Selection

Use screenshots by default. Produce at most **two short MP4s and no GIFs**. Reuse one small Dijkstra graph, one BST insertion and one two-pane sorting comparison. The purpose is to make the improvements visible, rather than demonstrate difficult algorithms.

| Claim | Evidence to show | Talk slot | Selected asset | Verification state |
| --- | --- | --- | --- | --- |
| Input-first editor entry points complement topic cards | Homepage has a separate Editors region | Engine & Website hand-off / start of joint demo | Editor entry-point screenshot | Captured; see manifest and workflow checks |
| A step explains its decision near the affected object | Dijkstra improves A from 4 to 2 through B; local note agrees with Status | Algorithm Visualizers: explainable steps | Dijkstra decision screenshot | Captured; see manifest and workflow checks |
| Presentation motion is independent of algorithm execution | Paused emphasis changes while the frame number stays fixed; dragging does not advance the run | Algorithm Visualizers / joint demo | One short graph MP4 | Captured; see manifest and workflow checks |
| The finished result remains explorable | Hover A and T at the same final frame; paths/costs differ | Joint demo or graph case | Main final-path screenshot + one backup endpoint | Captured; see manifest and workflow checks |
| Tree mutations distinguish a preview from the committed input | BST Insert(5), final preview, then Apply | Algorithm Visualizers: Tree operations | Preview screenshot + applied backup | Captured; see manifest and workflow checks |
| Sorting panes share input and a playback clock | Bubble and Selection on the same 12 numbers | Algorithm Visualizers: Sorting execution | Two-pane screenshot + one short MP4 | Captured; see manifest and workflow checks |
| Shared layout supports different workflows | Move Status into the bottom region without losing the graph/run | Algorithm Visualizers: shared V10 shell | Rearranged-layout screenshot | Captured; see manifest and workflow checks |

## Boundaries

- This pack does not replace the contribution overview: the contribution map still represents the wider algorithm, tree-workspace and testing work.
- Do not repeat all the examples in both the technical section and the 4–5 minute shared demo. Choose a placement for each during rehearsal.
- Do not present a current screenshot as an early prototype. The old report figures retain their own revision/date; they are not recaptured or relabelled here.
- The original VisuAlgo already supports custom input. The editor screenshots illustrate this prototype's workflow, not an invention of custom input.
- A sorting operation count is not CPU time, and this comparison is not a performance benchmark.
- A paused streak does not imply another algorithm step. A final hover queries the existing result; it does not rerun Dijkstra.
- Browser capture checks demonstrate the selected workflows only. They are not a fresh complete test-suite run or evidence of learning gains.
- Keep participant footage and the unmerged engine-integration experiment out of this pack.

## Rehearsal and selection

The output folder separates `01_main_slides`, `02_short_clips`, `03_backup` and `04_reproduce`. Its README recommends what to use first; its manifest records the app revision, UI settings, exact inputs, actions, observed checks and media metadata. Prefer the two clips as a fallback for a live demo, rather than adding them as extra speaking time.

Still outside this capture task: Early Design script, final 8–9 minute visualizer script, evaluation interpretation, future-work priorities, speaker hand-offs and full timed rehearsal. The current docs provide drafts and source evidence, not a completed rehearsal.

## Capture completed — 16 November 2026

Ready-to-use files are in [the presentation pack](../presentation/ca-2026-11-16/README.md), with a [visual chooser](../presentation/ca-2026-11-16/START_HERE.html). The final pack contains 6 main PNGs, 2 backup PNGs and exactly 2 MP4s (7.8s and 10.4s); no GIFs. Bubble + Selection was selected for the simple, readable side-by-side example. Raw attempts and codec tooling are not included.

Fresh browser observations at app `346e84b`: frame 11 stayed unchanged while paused animation time advanced; frame 12's local note agreed with Status; dragging B did not advance it; final hover paths to T/A had costs 4/2 at frame 21; the Tree editor text changed only at Apply; moving Status to bottom retained frame 21. Both sorting panes were at operation 48 in the selected still. These are workflow capture checks, not a rerun of the full unit/browser suite.

The source docs are sufficient for this asset subset. Historical prototype captures, full presentation timing, evaluation interpretation and the WASM-integration status still need their own evidence/context; no new claims or assets were invented to fill those gaps.
