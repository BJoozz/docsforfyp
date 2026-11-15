# English captions and short speaking cues

Use one claim per image. These lines explain the interface improvements; they are not algorithm lectures or measured learning outcomes.

| Asset | Slide caption | Short speaking cue |
| --- | --- | --- |
| 01 Editors | **Start with your own input.** | “The editor is another way into the same visualizers. I can build a small example, then explore algorithms on it.” |
| 02 Dijkstra decision | **Explain the decision where it happens.** | “Here, the route through B improves A from four to two. The local note, pseudocode and Status describe the same step.” |
| Graph MP4 | **The frame is paused; the emphasis is still moving.** | “The counter stays at eleven. This motion highlights the current step; it does not execute another step. I can also move a vertex without changing the run.” |
| 03 Dijkstra final | **A finished run is still explorable.** | “Hovering over T shows a path of length four. Hovering over A shows a path of length two, using the same completed result.” |
| 04 BST preview | **Explore a change before applying it.** | “The new node is visible in a preview. The underlying tree changes only when I choose Apply.” |
| 05 Sorting | **Same input. One playback clock. Different operations.** | “These simple sorts receive the same twelve numbers. At the same operation index, their arrays show different progress. These counts are operations, not CPU time.” |
| Sorting MP4 | **Compare the steps side by side.** | “Both panes pause and resume together. The final jump uses Last, so the clip is a workflow example, not a speed benchmark.” |
| 06 V10 layout | **Arrange the workspace around the task.** | “I moved Status below the drawing. The graph and the completed run remain available.” |
| Backup: A | **A different target, without another run.** | “The frame is still twenty-one. Only the target I am inspecting has changed.” |
| Backup: applied tree | **Apply commits the preview.** | “Five is now part of the input tree. The previous preview has ended.” |

## Attribution and claim limits

- Bao implemented the visualizer work described in the contribution map, including paused motion. Kerk suggested paused motion, built the design system and contributed engine/infrastructure, consolidation and CI. V10 design choices were joint under the supervisor's guidance. A speaker's section is not a claim of sole authorship.
- Original VisuAlgo already has custom input. Say this is a revised editor workflow; do not claim custom input itself is new.
- Dijkstra hover-path inspection is different from the final DFS recap. No DFS clip is included in this small pack.
- Tree Editor contains LCA/BST/AVL. It does not imply all heap/trie/segment workspaces share this tree.
- These assets show current prototype behavior, not shipped WASM integration, a complete replacement of VisuAlgo, a CPU benchmark or measured learning gains.
