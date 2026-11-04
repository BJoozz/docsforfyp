# VisuAlgo+ CA Report — complete LaTeX draft

**Source update — 4 November 2026:** The LaTeX sources now include the Week 10 V10 user trial and the post-trial rationale for floating text. **The three checked-in PDFs predate this update and have not been rebuilt.** Compile the sources below before reviewing or submitting the revised report. Page count and layout require a fresh build.

Prepared for Truong Van Quoc Bao on 3 November 2026.

Updated in place on 3 November: added personal motivation based on competitive programming and teaching; clarified that Bao, Kerk and the supervisor agreed on V10 after the survey and V2/V7 implementations, retaining selected strengths of both. These clarifications come directly from Bao and supplement the pinned evidence snapshot.

## Compile

The maintained report lives in `report/` in `BJoozz/docsforfyp`. Edit `main.tex` and `references.bib` here, compile from this directory, and update `VisuAlgo_CA_Report_Draft.pdf` in the same commit. The report folder includes its own figure copies so it can also be uploaded to Overleaf independently. Generated LaTeX auxiliary files are ignored.

Upload the contents of this folder to Overleaf and choose `main.tex` as the main document, using pdfLaTeX. Alternatively:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The source uses standard TeX Live packages. The seven screenshots are included in `figures/`; the two diagrams are drawn with TikZ. References are in `references.bib`.

## Vietnamese reading versions

Added on 4 November 2026, translated from the English report at commit `675fc73`:

- [Full Vietnamese translation](vi/VisuAlgo_CA_Report_VI.pdf) — source: [vi/full.tex](vi/full.tex).
- [Vietnamese summary](vi/VisuAlgo_CA_Summary_VI.pdf) — source: [vi/summary.tex](vi/summary.tex).

These are reading aids, not replacements for the English submission. They include the personal motivation and the joint decision with Kerk and the supervisor to adopt V10. Build instructions are in [vi/README.md](vi/README.md); use XeLaTeX for Vietnamese.

## Review before submission

- Check the registered project title/subtitle and whether the main evaluator's name must appear on the cover. The descriptive subtitle is a working subtitle, not a verified registration title.
- Confirm name, matric number and any required departmental cover-page format.
- Review first-person statements on responsibilities, review/acceptance of AI-assisted work, and the supervisor discussion. They follow the updated evidence pack and your account.
- Confirm the proposed November–April plan with your supervisor and Kerk. The study size, measurements and integration milestone are proposals, not agreed commitments or completed work.
- Check the applicable AI-use declaration requirements and adapt the existing workflow disclosure if needed.
- Evidence-pack GitHub links may require access. Keep the evidence pack available to reviewers if needed.
- Remove “Draft for review” and the draft header only after completing the review.

## Evidence boundaries

Application snapshot: `662e7b3` in `kerktaiheng/visualgo-plus-design`.
Evidence snapshot: `67ce56c11ec109de22e10c11f9a9847ad2fd02e5` in `BJoozz/docsforfyp`.
Validation numbers are recorded results from 1 November 2026; application tests were not rerun to produce this report. The revised sources describe a formative Week 10 V10 user trial, based on Bao's account on 4 November and a screenshot of the shared footage folder. Detailed participant counts, test questions, scores and coded observations are not supplied. They do not claim learning improvement, measured attention-switching reduction, comparative usability, performance improvement, complete VisuAlgo parity or current WASM integration. See [the Week 10 addendum](week10_user_trial_addendum.md).

The original screenshots are preserved. The source package is self-contained for compilation; it does not include the application repository or modify its contents.
