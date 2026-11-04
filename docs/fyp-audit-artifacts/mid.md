## 3. Status at the pause

| Phase | Agents | Status |
|---|---|---|
| Find | 15 | **All completed.** 142 findings: 4 Critical, 67 Important, 71 Minor (finder severities). 15 notes blocks, kept verbatim in section 9. |
| Verify | 15 | **All completed.** Each of the 142 findings got a verdict, and 34 more findings were added. |
| Synthesize | 1 | **FAILED** (usage limit). There is no deduplicated review, no top 5, no claim-check table and no readiness verdict from the panel. |

After verification (severities as the verifiers corrected them):

{{STATS}}

**What "confirmed" means here.** A second Opus agent reproduced the evidence and agreed the finding is fair. It does **not** mean Bao agreed. The "added by a verifier" items were not themselves checked by a third agent. Re-check them before acting on one.

**Duplicates.** Many confirmed findings repeat each other across slices; for example, five slices flag the private evidence-pack references. Section 4 groups them by hand. The deduplication the synthesis agent should have done is still to do.

---

## 4. Consolidated picture (hand-grouped from the confirmed findings; preliminary, not a verified synthesis)

I grouped the findings by their IDs and first sentences and did no new checking. The full text of each finding, with its evidence, is in Appendix A.

### 4.1 Critical

1. **The PDF still says "draft" in four places.**
   - "DRAFT FOR REVIEW" on the cover.
   - The running header "CP4101 CA Report | Draft" on pp. 2–16.
   - The PDF title metadata "VisuAlgo+ — CA Report Draft".
   - The file name `VisuAlgo_CA_Report_Draft.pdf`.
   - Sources: `main.tex` lines 13, 27 and 48. Findings: `official-OFF-1`, `crit-report-QR-1`.

### 4.2 Factual inaccuracies: the report states something the code, git or the cited source contradicts

| Claim in the report | What the panel found | IDs |
|---|---|---|
| p.11: notes "are suppressed for intervals below 200 milliseconds"; duration "limited by the step interval and configured delay" | Misstates the code. The 200 ms floor applies to the note's remaining life, which is 90% of the step interval minus the delay. | `floating-FT-4`, `counts-NUM-1`, `crit-accuracy-ACC-18` |
| p.10, Figure 6 caption: "the new value 1 moves above 7" | The captured frame (3 of 9) shows the comparison **before** the swap; 1 is still below 7. | `counts-NUM-4`, `algorithms-ALGFIG-3`, `floating-added-2` |
| p.12, Figure 9 caption: "presents the rebuilt modules alongside clearly marked future topics" | The 1440×900 viewport capture shows no "Coming soon" card. | `algorithms-ALGFIG-1`, `counts-NUM-5` |
| p.12: "Of the 30 catalogue cards, 12 open a module; eight are labelled full and four partial" | The counts are right, but they mix VisuAlgo+'s two editor cards with visualgo.net module cards. "Full" is undefined, and 4 of the 8 "full" cards are not visualgo.net modules. | `counts-added-2`, `crit-accuracy-ACC-6`, `qa-QA-6`, `crit-problem-added-2` |
| p.7: "the drawing has a target floor of 360 by 320 pixels" (presented as shared) | Graph only; tree and sorting pass their own floors. | `counts-NUM-3`, `architecture-ARCH-3` |
| p.5, Figure 1: rendering drawn as passing through the shared layer | The modules render directly. | `architecture-ARCH-1` |
| p.7, Figure 2: bottom region drawn full width under all three columns | The left and right columns run full height; the bottom sits under the canvas. | `architecture-ARCH-2` |
| p.6 and p.13: sorting history "remains unbounded" | Never trimmed, but bounded: input is capped at 240 values. | `architecture-ARCH-4` |
| p.9: "700 graph inputs for cut-vertex/bridge checks" right after the oracle sentence | Reads as 700 oracle comparisons; only seeds 1–400 are oracle-compared. | `counts-NUM-2`, `algorithms-ALGFIG-2` |
| p.9: "End node where applicable" | Only BFS, Dijkstra and Bellman–Ford take an End node. | `algorithms-ALGFIG-6`, `crit-accuracy-ACC-8` |
| p.4: "Later choices 27–48 and the subsequent 'V10 wins' changes were joint decisions" | "V10 wins" (18 Oct) came after choices 27–32 and before 33–48. It names the one-app consolidation, which the next sentence credits to Kerk. | `timeline-added-1`, `crit-accuracy-ACC-9`, `contributions-CONTRIB-4` |
| p.4: "Kerk conducted a user survey to inform the choice between the V2 split-rail and V7 dock-based layouts" | The owner's recorded answer: the survey came first, then Kerk and Bao together picked V2 and V7 from **nine** layouts in **Kerk's wireframe**. The wireframe is never credited. | `timeline-TL-3`, `contributions-CONTRIB-1`, `contributions-CONTRIB-2`, `crit-accuracy-ACC-4`, `qa-QA-3`, `crit-problem-added-1`, `crit-management-added-1` |
| p.4: "We also implemented both variants" | The V2 and V7 builds were Bao's, so the sentence undersells him. | `crit-technical-TA-4` |
| p.4: two different "V2"s side by side (Graph Visualizer V2, layout V2); "V10" never defined | Ambiguous to an outsider. | `contributions-added-2`, `qa-QA-7` |
| p.4, Table 1 periods | Some work sits in the wrong period (graph extensions started in late September), and pre-semester V1 work is merged into "Late July–August". | `timeline-TL-4`, `timeline-added-2` |
| p.11: "Following the Week 10 trial, I introduced floating text … [8, 6]" | The cited snapshot `67ce56c` says no user evaluation exists. The dated record (TP-34, PR #29) gives Bao's request of **23 Oct** with no trial. Week 10 is 19–23 Oct, so the claim holds only if every session came before that request. | `timeline-TL-1`, `timeline-TL-2`, `floating-FT-2`, `literature-LIT-6`, `crit-accuracy-ACC-2`, `crit-accuracy-ACC-14`; uncertain: `floating-FT-1`, `crit-accuracy-ACC-1` |
| p.11: notes "beside the relevant node or edge"; "the anchor follows the relevant node or edge" | Overstates the anchoring behaviour. | `floating-FT-5` |
| p.11: motivating example is a rejected relaxation; Figure 8 shows an accepted one | The text never says rejected relaxations get notes. | `floating-FT-7` |
| p.3: "Halim et al. [2] present VisuAlgo" | The 2012 paper presents the predecessor and never uses the name; Halim 2015 calls VisuAlgo its continuation. | `literature-LIT-4`, `crit-literature-LR-3` |
| p.15, reference [4] | The OpenDSA URL fails with a TLS certificate error. | `literature-LIT-5` |
| p.12: "266 CI runs" | Sits among the 1 November results, but the runs span 4 workflows and the whole history. | `crit-accuracy-ACC-11` |
| p.13: "Separate developer checks also lack a complete recorded protocol" | The protocol exists (checklists of 20, 10 and 26 items); only the **runs** were not recorded. | `crit-accuracy-ACC-17` |
| p.2, p.11 and p.16: supervisor statements | They rest only on Bao's later account (3 Nov), which only the p.16 small print discloses. | `crit-accuracy-ACC-5`; uncertain: `contributions-CONTRIB-3` |

### 4.3 Important themes (score-relevant, not factual errors)

- **Week 10 trial underspecified, and ethics not mentioned.**
  - It is the only user evidence, yet it has no dates, participant count, tested build, test content or observation.
  - Video was recorded, but there is no word on consent or storage. The planned 6–10-student study also has no ethics or consent step.
  - IDs: `crit-management-PM-2`, `qa-QA-1`, `crit-management-PM-6`, `qa-QA-2`, `official-added-1`; uncertain: `crit-accuracy-ACC-15`.
- **Evidence references [6]–[8] are private.**
  - They point to the private `BJoozz/docsforfyp`, so examiners get a 404.
  - They are the most-cited sources and look like publications.
  - A public build exists, which `official-added-3` names as the kerktaiheng GitHub Pages site.
  - IDs: `counts-added-1`, `floating-added-1`, `literature-LIT-1`, `crit-literature-LR-5`, `crit-report-QR-8`, `qa-QA-5`, `crit-accuracy-added-1`, `official-added-3`.
- **Page count is 16 against the official "10-15 pages".** Dropping the p.16 back matter alone gives 15 pages (variant v1). The prose cuts plus flexible floats give 14. IDs: `crit-report-QR-2`, `official-OFF-2`; cut list in the `crit-report` notes (section 9).
- **No explicit problem statement; objectives not measurable.**
  - Nothing traces back to the objectives, and objective 1 (technology selection) has no criteria or alternatives.
  - The official form's Technical Achievement section starts with "Formulation and problem statement".
  - IDs: `crit-problem-PU-1`, `crit-problem-PU-2`, `crit-problem-PU-3`, `official-OFF-7`, `contributions-CONTRIB-5`.
- **Literature review is thin, dated and descriptive.**
  - The newest peer-reviewed work is from 2012, and the review never positions the work against other systems.
  - The effectiveness literature is not used to justify the design.
  - VS Code is not credited as the precedent for V10.
  - visualgo.net itself is never cited.
  - It counts under Understanding (30%).
  - IDs: `literature-LIT-2`, `literature-LIT-3`, `literature-LIT-7`, `literature-LIT-8`, `literature-LIT-9`, `literature-added-1..4`, `crit-literature-LR-1..6`, `crit-problem-PU-8`, `official-OFF-5`.
- **Technical contribution not stated crisply.**
  - Decisions are given as WHAT with little WHY or rejected alternative, although the 95 decision records have them.
  - Validation is not tied back to the named risks, and the individual scale of the work is undersold.
  - IDs: `crit-technical-TA-1`, `crit-technical-TA-2`, `crit-technical-TA-3`, `crit-technical-TA-4`, `qa-QA-9` (why React Flow).
- **Project management.**
  - Table 5 ignores the official final-report deadline of 7 Apr 2027; it puts report writing in April.
  - Challenges are described as design properties, not as problems that actually occurred.
  - Process evidence (PRs, decision records) is invisible to the Main Evaluator.
  - IDs: `crit-management-PM-1`, `official-OFF-3`, `crit-management-PM-3`, `official-OFF-6`.
- **Presentation.**
  - Caveats are repeated 13 times (`crit-report-QR-3`).
  - Screenshot text prints at about 3–4 pt (`crit-report-QR-4`).
  - Figures 1–2 and 5–9 and Tables 3–5 are never referenced in the text (`crit-report-QR-5`, `algorithms-added-1`).
  - Abbreviations are left unexpanded (`crit-report-QR-6`).
  - Evidence-bookkeeping sentences sit in the body (`crit-report-QR-7`, `official-added-2`, `crit-accuracy-ACC-3`).
  - One feature goes by four names (`floating-FT-3`, `crit-accuracy-ACC-13`).

### 4.4 Candidate top 5 before submission (my preliminary ranking, for the next session to confirm or adjust)

1. **Remove every "draft" marker:** cover, header, PDF metadata and file name.
2. **Fix the Week 10 trial and floating-text passage.**
   - Date the trial and cite the addendum instead of [8, 6].
   - Make the chronology match the 23 Oct request.
   - Add a consent and ethics sentence.
   - This needs Bao's answers (section 5).
3. **Correct the factual inaccuracies in 4.2.** Above all: the note timing, the Figure 6 and Figure 9 captions, the survey, wireframe and "both variants" wording, the "V10 wins" order, and the End-node scope.
4. **Make the evidence reachable and get to 15 pages or fewer.**
   - Point to the public build, or give examiners access, or drop the per-sentence self-citations.
   - Remove the p.16 back matter, which alone gives 15 pages.
5. **Add a one-paragraph problem statement and measurable objectives** (p.2). Then cut the repeated caveats so the contribution is visible.

---

## 5. Questions only Bao can answer (blocking for some fixes)

1. **Week 10 session dates.** On which dates between Mon 19 and Fri 23 Oct 2026 were the sessions held? Were all of them before your floating-text request on 23 Oct (TP-34; PR #29 opened 13:36 SGT)? If not, p.11's "Following the Week 10 trial" and "post-trial" must soften to "during Week 10, alongside the trial". (`timeline-TL-1`, `floating-FT-1`)
2. **Tested build.** Was it the public Pages site, and on which day, or a local build at which commit? (`timeline-TL-1`)
3. **Trial details.** Can the report give a participant count and one or two concrete observations? Or must it stay "several users"? (`crit-management-PM-2`, `qa-QA-1`)
4. **Consent.** Did participants consent to video recording? Should the report say ethics review will be confirmed with the supervisor before the follow-up study? (`crit-accuracy-ACC-15`, `official-added-1`)
5. **Supervisor's part.** Was Prof Halim part of the V10 decision? So far this rests only on your clarification of 3 Nov. The same applies to his "canvas-focused goal" behind floating text (p.11). (`contributions-CONTRIB-3`, `crit-accuracy-ACC-5`)
6. **Evidence access.**
   - Will examiners be given access to `BJoozz/docsforfyp`?
   - Or should references [6]–[8] be replaced by the public app link and an appendix?
   - Or should the self-citations be dropped from sentences? (`literature-LIT-1`, `crit-report-QR-8`, `qa-QA-5`)
7. **Title.** Is "VisuAlgo+ / Rebuilding Interactive Algorithm Visualizations" the registered project title? The README calls it unverified. (`official-OFF-4`, `crit-report-QR-16`)
8. **Main Evaluator.** Who is it? The softcopy must go to them as well as to Prof Halim.
9. **The page-break macro.** Do you accept the uncommitted change from section 2.5? It is needed for the current page counts.
10. **Uncertain minor items.**
    - "V1 began on 28 July": the first commit already holds a working app (`timeline-TL-5`).
    - Should the parallel-edge note say VisuAlgo+ deliberately differs from VisuAlgo (`crit-technical-TA-7`)?
    - Should p.12 present any performance observation (`crit-technical-TA-9`)?

---

## 6. Remaining tasks, in priority order

1. **Get Bao's answers to section 5,** at least questions 1–6. Present them with the evidence links and options, in Vietnamese.
2. **Finish the synthesis the failed agent should have produced.**
   - Deduplicate `derived.confirmed` in the JSON.
   - Produce the deliverable in section 8.
   - Do not re-run the finders or verifiers.
3. **Re-check before acting.** Reproduce each finding you are about to act on, especially the 34 "added by a verifier" items (6 Important). Use the repositories, not the scratchpad paths.
4. **Agree the fix list with Bao.** Offer options per item. He decides wording that concerns his account, the trial, the supervisor, Kerk's credit and what to cut.
5. **Apply the approved edits.**
   - Edit `report/main.tex`, then mirror them in `report/vi/full.tex` and `report/vi/summary.tex`; the README says to keep them in sync.
   - Rebuild with the commands in section 2.4.
   - Check: at most 15 pages, no draft marker anywhere (grep the PDF text and metadata), no undefined references, and the figures readable.
   - Update `report/README.md` and `week10_user_trial_addendum.md`.
6. **Commit only when Bao asks, and only by explicit paths.** Do not push unless told.
7. **Before 17:00 SGT today: Bao submits** the softcopy to Prof Halim and the Main Evaluator. This is his action.
8. **Prepare the CA presentation** for Reading Week, 14–20 Nov 2026. Use the `qa` notes (section 9, slice 15): the likely questions, slide outline and demo script.

---

## 7. Instructions for the next Claude session

- **Start here.** Read sections 0–6, then load `fyp-audit-panel-results.json`. Its keys:
  - `finder.<slice>`: findings, positives and notes.
  - `verifier.<slice>`: results (verdicts) and missed (added findings).
  - `derived.confirmed`, `derived.uncertain`, `derived.refuted` and `derived.positives`: merged and sorted by severity.
- **Slices:** `timeline`, `counts`, `architecture`, `algorithms`, `floating`, `contributions`, `literature`, `official`, `crit-problem`, `crit-technical`, `crit-literature`, `crit-management`, `crit-report`, `crit-accuracy`, `qa`.
- **Do not change the report before Bao chooses.** This is a standing rule: verify review findings, explain the current state, offer fix options, and wait for his choice.
- **Do not invent trial data,** quotes, participant numbers or scores. The addendum is the only source.
- **Do not reopen settled facts** (section 2.6). Mention AI assistance once at most; it is Bao's work.
- **Treat Codex's notes and plans as input only.** Bao does not read them, so they are not his agreement.
- **Agents.** If you need any, use Opus at max effort (Bao's rule), and keep their number small.
- **Repositories.** Both are read-only for review purposes. Never commit, push, reset or check out without Bao's explicit request.
- **Regenerating this file.** `docs/fyp-audit-artifacts/gen-handoff.js` regenerates the generated sections from the workflow journal, which exists only on Bao's machine. In the cloud, work from the JSON.

---

## 8. Expected final deliverables

1. **A review for Bao, in Vietnamese** (English for technical terms and quoted report text), in this order:
   1. Overall readiness: 5–8 sentences, with a one-line judgement per criterion, using the **official** weights from section 2.7.
   2. Top 5 fixes before submission: page or section, what to change, and why.
   3. Findings by severity (Critical / Important / Minor), deduplicated, ordered by page, each as "[page, §] issue → fix (basis)".
   4. A claim-check table: claim | page | source | MATCH / MISMATCH (true value) / UNVERIFIABLE. Include the matches, so Bao sees what is safe.
   5. What to add and what to cut, with page references and approximate lines saved. Use the `crit-report` cut list and `fyp-audit-artifacts/cut-list/`.
   6. Questions for Bao, with options (section 5).
   7. CA presentation preparation: likely questions, slide outline and demo script (from the `qa` notes).
   8. Strengths to keep, at most 10 (from the positives).
2. **After Bao approves the fixes:** revised `main.tex` with the Vietnamese sources kept in sync, and rebuilt PDFs with no "draft" markers and at most 15 pages.
3. **Optionally,** a short note recording the trial answers in `report/week10_user_trial_addendum.md`.

---

