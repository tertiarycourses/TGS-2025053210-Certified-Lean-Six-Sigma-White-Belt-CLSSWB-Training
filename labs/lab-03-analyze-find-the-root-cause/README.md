# Lab 3 — Analyze — Find the Root Cause

**DMAIC phase:** ANALYZE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma White Belt (CLSSWB) Training (TGS-2025053210)

## Objective

Identify likely causes using 5 Whys and Fishbone analysis (A3, K2).

## Scenario

BrewBean Cafe is a busy coffee shop serving mainly office workers on their way to work. During the 7:30am-9:00am morning rush customers queue for up to 15 minutes against a 5-minute service promise, some drinks are made wrong and have to be remade, and online complaints have been rising. Management has formed a small improvement team and you have joined it as the White Belt member, supporting the team rather than leading the project.

## What you will build

A completed 5 Whys chain, a Fishbone diagram with causes sorted by category, and a shortlist of likely root causes.

**Tools and techniques:** Symptom vs cause, 5 Whys, Fishbone (5M) diagram, Pareto chart, common vs special cause variation

## Your data pack

Everything you need is in this folder. The data is mock data built for the BrewBean Cafe scenario — it is realistic and internally consistent across all five labs, so what you find here carries into the next lab.

### Data to work from — `data/`

| File | What it is |
|------|------------|
| [`delay-reason-pareto-data.csv`](data/delay-reason-pareto-data.csv) | Delay reason Pareto data (6 rows) |
| [`cause-evidence-sheet.csv`](data/cause-evidence-sheet.csv) | Candidate causes and their evidence (12 rows) |
| [`lab-03-workbook.xlsx`](data/lab-03-workbook.xlsx) | **Excel workbook** — every dataset *and* every blank template below, one per tab |

### Blank worksheets to fill in — `templates/`

| File | What you fill in |
|------|------------------|
| [`5-whys-template.csv`](templates/5-whys-template.csv) | 5 Whys chain (blank) — Steps 1 and 2. Stop when you reach something the team can act on. |
| [`fishbone-template.csv`](templates/fishbone-template.csv) | Fishbone (5M) diagram (blank) — Steps 3 and 4. Problem goes in the head of the fish. |
| [`root-cause-shortlist-template.csv`](templates/root-cause-shortlist-template.csv) | Root cause shortlist (blank) — Steps 6 and 7. |

> **Tip:** open the Excel workbook if you want everything in one window with the templates ready to type into. Use the CSVs if you prefer Google Sheets, LibreOffice or a plain text editor.

See [`data/README.md`](data/README.md) for the data dictionary — what every column means and how the figures were collected.

## Steps

### Step 1

Write the symptom from your Lab 2 baseline at the top of templates/5-whys-template.csv (e.g. 'customers wait an average of 8.9 minutes against a 5-minute promise').

### Step 2

Ask 'why does that happen?' down the template, each answer becoming the next question. Stop when you reach a PROCESS the team can act on — never at a person.

### Step 3

Open templates/fishbone-template.csv and write the problem in the head of the fish.

### Step 4

Brainstorm possible causes onto the five bones — Manpower, Method, Machine, Material, Measurement — then check them against data/cause-evidence-sheet.csv to see which ones the data actually supports.

### Step 5

Open data/delay-reason-pareto-data.csv — the delay reasons from the Lab 2 log, counted and ranked. Read the Cumulative % column and state which few causes account for most of the problem.

### Step 6

Using the last column of data/cause-evidence-sheet.csv, decide for each cause whether it is common cause (built into the process) or special cause (a one-off event).

### Step 7

In templates/root-cause-shortlist-template.csv, shortlist the two or three causes best supported by evidence — not by opinion.

## Check your work

Your 5 Whys chain ends in something the team can actually act on, every Fishbone cause sits under one of the five categories, and each shortlisted cause is backed by an observation, not an opinion.

## Deliverable

Save your output — it forms part of your BrewBean Cafe improvement package and is your revision material for the assessment.

## Compare your answer

Once you have attempted the lab, compare your thinking against [`model-answer.md`](model-answer.md). There is rarely one right answer in Lean Six Sigma — what matters is whether your reasoning is supported by the data in front of you.

---

*Certified Lean Six Sigma White Belt (CLSSWB) Training · TGS-2025053210 · Version v3 · © 2026 Tertiary Infotech Academy Pte Ltd*
