# Lab 2 — Measure — Map the Process and Spot the Waste

**DMAIC phase:** MEASURE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma White Belt (CLSSWB) Training (TGS-2025053210)

## Objective

Describe how the process runs and identify the eight wastes in it (A4, K2).

## Scenario

BrewBean Cafe is a busy coffee shop serving mainly office workers on their way to work. During the 7:30am-9:00am morning rush customers queue for up to 15 minutes against a 5-minute service promise, some drinks are made wrong and have to be remade, and online complaints have been rising. Management has formed a small improvement team and you have joined it as the White Belt member, supporting the team rather than leading the project.

## What you will build

A SIPOC overview, a step-by-step process map with timings, and a completed waste tally sheet.

**Tools and techniques:** SIPOC, process mapping, types of data, check sheets, the eight wastes (DOWNTIME)

## Your data pack

Everything you need is in this folder. The data is mock data built for the BrewBean Cafe scenario — it is realistic and internally consistent across all five labs, so what you find here carries into the next lab.

### Data to work from — `data/`

| File | What it is |
|------|------------|
| [`morning-rush-observation-log.csv`](data/morning-rush-observation-log.csv) | Morning rush observation log (60 rows) |
| [`process-step-timings.csv`](data/process-step-timings.csv) | Process step timings (15 rows) |
| [`downtime-waste-tally.csv`](data/downtime-waste-tally.csv) | DOWNTIME waste tally (partially completed) (8 rows) |
| [`lab-02-workbook.xlsx`](data/lab-02-workbook.xlsx) | **Excel workbook** — every dataset *and* every blank template below, one per tab |

### Blank worksheets to fill in — `templates/`

| File | What you fill in |
|------|------------------|
| [`sipoc-template.csv`](templates/sipoc-template.csv) | SIPOC (blank) — Step 2. Keep Process to 5-7 steps only. |
| [`process-map-template.csv`](templates/process-map-template.csv) | Process map with value-add judgement (blank) — Steps 3 and 4. |
| [`downtime-tally-template.csv`](templates/downtime-tally-template.csv) | DOWNTIME tally sheet (blank) — Step 6. |

> **Tip:** open the Excel workbook if you want everything in one window with the templates ready to type into. Use the CSVs if you prefer Google Sheets, LibreOffice or a plain text editor.

See [`data/README.md`](data/README.md) for the data dictionary — what every column means and how the figures were collected.

## Steps

### Step 1

Agree the start and stop points of the process — start: customer joins the queue; stop: customer receives the drink.

### Step 2

Complete templates/sipoc-template.csv: Suppliers, Inputs, Process (5-7 steps only), Outputs, Customers.

### Step 3

Open data/process-step-timings.csv. Copy the 15 steps into templates/process-map-template.csv with their observed times.

### Step 4

Mark each step VA or NVA in the template — the test is whether the customer would pay extra for THAT step — and write one line saying why.

### Step 5

Look at the columns in data/morning-rush-observation-log.csv and classify each: which figures are discrete (counted) and which are continuous (measured)?

### Step 6

Open data/downtime-waste-tally.csv — three rows are completed as worked examples. Using the observation log and the step timings as your evidence, complete the remaining five rows in templates/downtime-tally-template.csv.

### Step 7

Identify which single waste type you tallied most often and at which process step, then write down the baseline figures (average wait, longest wait, % over the 5-minute promise, drinks remade) — Lab 5 measures the improvement against them.

## Check your work

Your SIPOC has all five columns filled, every process step has a time, and every waste on your tally sheet is tagged to one of the eight DOWNTIME types.

## Deliverable

Save your output — it forms part of your BrewBean Cafe improvement package and is your revision material for the assessment.

## Compare your answer

Once you have attempted the lab, compare your thinking against [`model-answer.md`](model-answer.md). There is rarely one right answer in Lean Six Sigma — what matters is whether your reasoning is supported by the data in front of you.

---

*Certified Lean Six Sigma White Belt (CLSSWB) Training · TGS-2025053210 · Version v3 · © 2026 Tertiary Infotech Academy Pte Ltd*
