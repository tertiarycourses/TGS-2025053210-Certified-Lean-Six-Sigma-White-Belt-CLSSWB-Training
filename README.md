# TGS-2025053210 - Certified Lean Six Sigma White Belt (CLSSWB) Training

> **Course:** WSQ - Certified Lean Six Sigma White Belt (CLSSWB) Training  
> **Course Code:** TGS-2025053210  
> **Register here:** https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-white-belt-clsswb-training.html

These are the hands-on lab exercises for the WSQ Certified Lean Six Sigma White Belt (CLSSWB) Training course delivered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/).

This repository contains **5 guided Lean Six Sigma White Belt labs** (5 core and 0 elective), structured around the **DMAIC roadmap** and grounded in the Council for Six Sigma Certification (CSSC) White Belt body of knowledge.

---

## Courseware

| Artifact | File |
|----------|------|
| **Slide deck** | `courseware/Certified Lean Six Sigma White Belt (CLSSWB) Training-v3.pptx` (and `.pdf`) |
| **Learner Guide (Markdown)** | [LG-Certified Lean Six Sigma White Belt (CLSSWB) Training.md](LG-Certified%20Lean%20Six%20Sigma%20White%20Belt%20%28CLSSWB%29%20Training.md) |
| **Learner Guide (DOCX/PDF)** | `courseware/LG-Certified Lean Six Sigma White Belt (CLSSWB) Training.docx` (and `.pdf`) |
| **Lesson Plan (DOCX/PDF)** | `courseware/LP-Certified Lean Six Sigma White Belt (CLSSWB) Training.docx` (and `.pdf`) |
| **Lab Index** | [labs/README.md](labs/README.md) |
| **Tools and Templates** | [labs/tools.md](labs/tools.md) |

> **Note:** assessment papers, answer keys and trainer-only materials are intentionally not published in this repository.

---

## How to use

1. Read the Learner Guide first — it follows the same DMAIC order as the course.
2. Complete the five labs in order using the BrewBean Cafe scenario.
3. Complete the elective labs if time allows, or as post-course practice.
4. Keep every worksheet — the final lab combines them into one improvement package.
5. Review the 'Check your work' step at the end of each lab before moving on.

---

## Lab catalogue

### Define — Understand the Problem

- [Lab 1 - Define — Customer Requirements and the Problem Statement](labs/lab-01-define-customer-requirements-and-the-problem-statement/README.md) — [data](labs/lab-01-define-customer-requirements-and-the-problem-statement/data/), [model answer](labs/lab-01-define-customer-requirements-and-the-problem-statement/model-answer.md)

### Measure — See What Is Really Happening

- [Lab 2 - Measure — Map the Process and Spot the Waste](labs/lab-02-measure-map-the-process-and-spot-the-waste/README.md) — [data](labs/lab-02-measure-map-the-process-and-spot-the-waste/data/), [model answer](labs/lab-02-measure-map-the-process-and-spot-the-waste/model-answer.md)

### Analyze — Find the Cause

- [Lab 3 - Analyze — Find the Root Cause](labs/lab-03-analyze-find-the-root-cause/README.md) — [data](labs/lab-03-analyze-find-the-root-cause/data/), [model answer](labs/lab-03-analyze-find-the-root-cause/model-answer.md)

### Improve — Fix the Cause

- [Lab 4 - Improve — Choose and Pilot a Countermeasure](labs/lab-04-improve-choose-and-pilot-a-countermeasure/README.md) — [data](labs/lab-04-improve-choose-and-pilot-a-countermeasure/data/), [model answer](labs/lab-04-improve-choose-and-pilot-a-countermeasure/model-answer.md)

### Control — Hold the Gain

- [Lab 5 - Control — Hold the Gain and Hand Over](labs/lab-05-control-hold-the-gain-and-hand-over/README.md) — [data](labs/lab-05-control-hold-the-gain-and-hand-over/data/), [model answer](labs/lab-05-control-hold-the-gain-and-hand-over/model-answer.md)

---

## Repository structure

```
courseware/          slide deck (PPTX + PDF), Learner Guide, Lesson Plan
  archive/           superseded deck versions
  assets/            diagrams and images used by the deck
labs/                5 lab folders + index + toolkit
  lab-NN-<name>/     one folder per lab:
    README.md          the lab worksheet
    data/              mock datasets (.csv) + .xlsx workbook + data dictionary
    templates/         blank worksheets to fill in (.csv)
    model-answer.md    worked model answer
    facilitator-notes.md   trainer notes
LG-Certified Lean Six Sigma White Belt (CLSSWB) Training.md
                     Learner Guide (Markdown mirror of the DOCX)
.claude/skills/courseware-build/build/
                     single-source generators: one content module
                     drives the deck, LP, LG and labs
```

All artifacts are generated from `course_data.py` + `data_domainN.py`, so the deck, Lesson Plan, Learner Guide and labs stay 100% aligned.

## Interactive tools

- [5 Whys](https://alfredang.github.io/5whys/) — root-cause chain builder
- [Fishbone Diagram](https://alfredang.github.io/fishbone/) — Ishikawa cause-and-effect builder
- [Pareto Chart](https://alfredang.github.io/paretochart/) — collaborative team brainstorm, vote and live chart
- [NovaSPC](https://alfredang.github.io/novaspc/) — run charts, SPC charts and process capability

## Reference

- [Council for Six Sigma Certification - Lean Six Sigma White Belt Certification](https://www.sixsigmacouncil.org/lean-six-sigma-white-belt-certification/)
- [Course registration page](https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-white-belt-clsswb-training.html)
- [labs/tools.md](labs/tools.md) - templates, formulas and free tools used in the labs

## Free tools used

- Microsoft Excel, LibreOffice Calc, or Google Sheets
- Draw.io / diagrams.net for SIPOC, process maps and fishbone diagrams
- The interactive tools listed above
- Whiteboard or sticky notes for facilitation activities

---

*Version v3 · 23 September 2026 · © 2026 Tertiary Infotech Academy Pte Ltd*
