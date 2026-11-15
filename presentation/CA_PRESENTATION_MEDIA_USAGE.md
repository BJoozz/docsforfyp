# Current-app media integration for VisuAlgo+ CA (16 November 2026)

Source evidence: [Codex's verified asset pack](ca-2026-11-16/README.md) at `a30b588`; app build `346e84b`. The [master speaking script](VisuAlgo_CA_Master_Script.md) is the initial 33-minute draft. No unverified new algorithm outcome or learning gain should be claimed.

| Existing slide | Primary asset or fallback | Short narration | Note |
| --- | --- | --- | --- |
| 14 – Shared shell | [V10 layout still](ca-2026-11-16/01_main_slides/06_v10_layout.png) | “I moved Status below the canvas; the run stayed at its completed frame.” | New capture from current app; keep 20-second drag demo optional. |
| 15 – Graph state ownership | [Graph paused-step MP4](ca-2026-11-16/02_short_clips/01_graph_paused_step.mp4) | “At frame 11 the run is paused while the highlight moves. After I click Next, the explanation appears at frame **12**; dragging B keeps the run at frame 12.” | Corrects the older single-frame cue. The paused glow is subtle over Zoom; point to the highlighted edge. |
| 16 – LCA (primary Tree example) | Existing historical LCA still in the deck | “Equal candidate ancestors mean both nodes stay; this is still a meaningful step.” | This pack has no new LCA image. Do **not** mislabel BST Insert as LCA. |
| 17 – Sorting comparison | [Two-pane still](ca-2026-11-16/01_main_slides/05_sorting_compare.png); [Sorting MP4](ca-2026-11-16/02_short_clips/02_sorting_shared_clock.mp4) | “Both panes use the same 12 numbers and share controls; at operation 48 the arrays differ.” | MP4 is fallback; Last jumps to the final frame, **not** a timing benchmark. |
| 18 – Dijkstra explanation + exploration | [Decision still](ca-2026-11-16/01_main_slides/02_dijkstra_decision.png); [Hover-T still](ca-2026-11-16/01_main_slides/03_dijkstra_final_path_t.png) | “The note near A explains the relaxation. At the last frame, hovering T shows a path of length 4 without rerunning.” | Current app screenshots; another hover example is in backups. |
| 19–20 – Editor workflow | [Editor-entry still](ca-2026-11-16/01_main_slides/01_editor_entry_points.png) | “We make entering through the user's own graph or tree a clear option.” | Original VisuAlgo already had custom inputs; this is a **workflow** refinement. |
| 24 – Tree mutation backup | [BST Insert preview](ca-2026-11-16/01_main_slides/04_tree_insert_preview.png); [Applied result](ca-2026-11-16/03_backup/02_tree_insert_applied.png) | “The operation can be inspected before Apply commits the new tree.” | Useful backup case; don't add a full new tree section. |

## Presentation decisions
- Prefer the newer current-app PNGs over old historical stills for Graph, Sorting and V10 when updating slide layout.
- Keep the dated historical still for the **LCA** slide; state it is historical if asked.
- The two MP4s total ~18 seconds. Use only once each, or as **backup** for live demonstrations, so the 33-minute talk does not expand.
- If the Graph clip's subtle pause animation is not visible over Zoom, point at the highlighted edge and explain the frozen frame number; don't claim dramatic motion.
- Do not claim WebAssembly integration is already live: current visualizers use TypeScript execution; the engine is a separate foundation.
- Slides 7–12 are an evidence-based draft of **Kerk's** contributions. Kerk must confirm technical claims, ownership and demonstrations before the joint talk.
- Keep the **3:00–3:45 PM SGT** meeting and **12-minute discussion buffer**. If short on time, shorten slide 20's live demo to Graph-only and keep LCA as an earlier technical still.
- This supplement indexes existing assets; it is not proof of a new test-suite run, an A/B study, measured learning impact or a Zoom rehearsal.

## Media quality summary
Codex generated 6 main PNGs, 2 backup PNGs, and 2 H.264 MP4s from app commit `346e84b`. Its [manifest](ca-2026-11-16/manifest.json) and [verification log](ca-2026-11-16/04_reproduce/media-verification.json) document resolutions, captured states and playback checks. The current media pack has no new LCA/DFS-recap/editor-from-scratch clip.