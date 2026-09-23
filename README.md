# TGS-2025053210 - Certified Lean Six Sigma White Belt (CLSSWB) Training

> **Course:** WSQ - Certified Lean Six Sigma White Belt (CLSSWB) Training  
> **Course Code:** TGS-2025053210  
> **Register here:** https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-white-belt-clsswb-training.html

These are the hands-on activity packs for the WSQ Certified Lean Six Sigma White Belt (CLSSWB) Training course delivered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/).

This repository contains **5 guided Lean Six Sigma White Belt activities** — exactly one per phase of the **DMAIC roadmap** — grounded in the Council for Six Sigma Certification (CSSC) White Belt body of knowledge. Every activity runs on one continuous scenario, the BrewBean Cafe morning rush, and ships with its own mock data.

---

## Courseware

| Artifact | File |
|----------|------|
| **Slide deck** | `courseware/Certified Lean Six Sigma White Belt (CLSSWB) Training-v5.pptx` (and `.pdf`) |
| **Learner Guide (Markdown)** | [LG-Certified Lean Six Sigma White Belt (CLSSWB) Training.md](LG-Certified%20Lean%20Six%20Sigma%20White%20Belt%20%28CLSSWB%29%20Training.md) |
| **Learner Guide (DOCX/PDF)** | `courseware/LG-Certified Lean Six Sigma White Belt (CLSSWB) Training.docx` (and `.pdf`) |
| **Lesson Plan (DOCX/PDF)** | `courseware/LP-Certified Lean Six Sigma White Belt (CLSSWB) Training.docx` (and `.pdf`) |
| **Activity Index** | [activities/README.md](activities/README.md) |
| **Tools and Frameworks** | [activities/tools.md](activities/tools.md) |

> **Note:** assessment papers, answer keys and trainer-only materials are intentionally not published in this repository.

---

## Activities

Each activity folder carries the full house pack:

| File | What it is |
|------|------------|
| `ANN-Facilitator-Guide-*.docx` / `.pdf` | Trainer run-sheet: purpose, set-up, scenario, numbered steps with facilitator notes, timing, debrief |
| `ANN-Learner-Worksheet-*.docx` / `.pdf` | The learner's sheet: scenario, steps and a working space |
| `ANN-Checklist-*.docx` / `.pdf` | Criteria to tick before the debrief |
| `data/` | Mock datasets (`.csv`) + `ANN-Data-Workbook.xlsx` + data dictionary |
| `templates/` | Blank worksheets to fill in (`.csv`) |
| `model-answer.md` | Worked model answer |

**1. Customer Requirements and the Problem Statement** — DMAIC · DEFINE · 30 minutes  
[Folder](activities/01%20-%20Customer%20Requirements%20and%20the%20Problem%20Statement/) · [Data](activities/01%20-%20Customer%20Requirements%20and%20the%20Problem%20Statement/data/) · [Model answer](activities/01%20-%20Customer%20Requirements%20and%20the%20Problem%20Statement/model-answer.md)

**2. Map the Process and Spot the Waste** — DMAIC · MEASURE · 30 minutes  
[Folder](activities/02%20-%20Map%20the%20Process%20and%20Spot%20the%20Waste/) · [Data](activities/02%20-%20Map%20the%20Process%20and%20Spot%20the%20Waste/data/) · [Model answer](activities/02%20-%20Map%20the%20Process%20and%20Spot%20the%20Waste/model-answer.md)

**3. Find the Root Cause** — DMAIC · ANALYZE · 30 minutes  
[Folder](activities/03%20-%20Find%20the%20Root%20Cause/) · [Data](activities/03%20-%20Find%20the%20Root%20Cause/data/) · [Model answer](activities/03%20-%20Find%20the%20Root%20Cause/model-answer.md)

**4. Choose and Pilot a Countermeasure** — DMAIC · IMPROVE · 30 minutes  
[Folder](activities/04%20-%20Choose%20and%20Pilot%20a%20Countermeasure/) · [Data](activities/04%20-%20Choose%20and%20Pilot%20a%20Countermeasure/data/) · [Model answer](activities/04%20-%20Choose%20and%20Pilot%20a%20Countermeasure/model-answer.md)

**5. Hold the Gain and Hand Over** — DMAIC · CONTROL · 30 minutes  
[Folder](activities/05%20-%20Hold%20the%20Gain%20and%20Hand%20Over/) · [Data](activities/05%20-%20Hold%20the%20Gain%20and%20Hand%20Over/data/) · [Model answer](activities/05%20-%20Hold%20the%20Gain%20and%20Hand%20Over/model-answer.md)

---

## How to use

1. Read the Learner Guide first — it follows the same DMAIC order as the course.
2. Work the 5 activities in order; each one's output feeds the next.
3. Open the activity's `data/` folder — the CSVs or the Excel workbook — and work from the real figures, not from memory.
4. Fill the blank templates as you go, then tick the Checklist before the debrief.
5. Compare against `model-answer.md` only after you have attempted the activity.

---

## Repository structure

```
courseware/          slide deck (PPTX + PDF), Learner Guide, Lesson Plan
  assets/            diagrams and images used by the deck
activities/          5 activity folders + index + toolkit
  NN - <name>/       one folder per activity:
    ANN-Facilitator-Guide-*.docx|pdf
    ANN-Learner-Worksheet-*.docx|pdf
    ANN-Checklist-*.docx|pdf
    data/            mock datasets + Excel workbook + data dictionary
    templates/       blank worksheets
    model-answer.md
LG-Certified Lean Six Sigma White Belt (CLSSWB) Training.md
                     Learner Guide (Markdown mirror of the DOCX)
.claude/skills/courseware-build/build/
                     single-source generators: one content module
                     drives the deck, LP, LG and activities
```

All artifacts are generated from `course_data.py` + `data_domainN.py` + `lab_data.py`, so the deck, Lesson Plan, Learner Guide and activities stay 100% aligned. The datasets are internally consistent across activities, so the BrewBean Cafe story reconciles from Define through to Control.

## Interactive tools

- [5 Whys](https://alfredang.github.io/5whys/) — root-cause chain builder
- [Fishbone Diagram](https://alfredang.github.io/fishbone/) — Ishikawa cause-and-effect builder
- [Pareto Chart](https://alfredang.github.io/paretochart/) — collaborative brainstorm, vote and live chart
- [NovaSPC](https://alfredang.github.io/novaspc/) — run charts, SPC charts and process capability

## Reference

- [Council for Six Sigma Certification - Lean Six Sigma White Belt Certification](https://www.sixsigmacouncil.org/lean-six-sigma-white-belt-certification/)
- [Course registration page](https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-white-belt-clsswb-training.html)
- [activities/tools.md](activities/tools.md) - frameworks, formulas and free tools

---

*Version v5 · 23 September 2026 · © 2026 Tertiary Infotech Academy Pte Ltd*
