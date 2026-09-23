# Lab 2 — Data Pack

*Certified Lean Six Sigma White Belt (CLSSWB) Training · TGS-2025053210 · Version v3*

All figures below are **mock data** created for training. They describe the BrewBean Cafe morning rush scenario used by every lab in this course, and they are internally consistent across the five labs — the Lab 2 observation log is the evidence base for the Lab 3 Pareto, and the Lab 5 monitoring data follows on from the Lab 4 pilot.

## Files in this folder

| File | Format | What it is |
|------|--------|------------|
| `morning-rush-observation-log.csv` | CSV | Morning rush observation log |
| `process-step-timings.csv` | CSV | Process step timings |
| `downtime-waste-tally.csv` | CSV | DOWNTIME waste tally (partially completed) |
| `lab-02-workbook.xlsx` | Excel | Every dataset **and** every blank template above, one per tab |

> Open the `.xlsx` if you want everything in one place with the templates ready to type into. Open the `.csv` files if you prefer Google Sheets, LibreOffice or a plain text editor.

## Morning rush observation log

**File:** `morning-rush-observation-log.csv`  |  **Rows:** 60

60 customers observed end to end during one weekday morning rush at BrewBean Cafe. Wait time is measured from the customer joining the queue to the drink being handed over. This is THE baseline dataset for the course — Lab 3's Pareto is derived from the Delay Reason column and Lab 5's control chart compares back to it.

| Column | Description |
|--------|-------------|
| `Customer ID` | |
| `Time Joined Queue` | |
| `Time Band` | |
| `Drink Ordered` | |
| `Wait Time (min)` | |
| `Drink Remade` | |
| `Delay Reason Observed` | |

**Note:** Observed by the improvement team with a stopwatch and a check sheet. Average wait 8.9 min; longest 15.0 min; 49 of 60 customers (82%) exceeded the 5-minute promise; 7 drinks were remade.

## Process step timings

**File:** `process-step-timings.csv`  |  **Rows:** 15

The average observed time for each step of the morning-rush process, with the team's value-add judgement left blank in the template. Use it for Step 3 and Step 4 of the lab.

| Column | Description |
|--------|-------------|
| `Step No` | |
| `Process Step` | |
| `Who Does It` | |
| `Avg Time (sec)` | |
| `Observed Range (sec)` | |
| `Times Step Was Skipped` | |

**Note:** 'Times Step Was Skipped' counts how many of the 60 observed customers did NOT experience that step — so step 10 happened for 18 of 60 customers and step 15 for 7 of 60. Steps 2, 8 and 10 are where the time actually goes.

## DOWNTIME waste tally (partially completed)

**File:** `downtime-waste-tally.csv`  |  **Rows:** 8

The team's waste walk, half done. Three rows are filled in as worked examples; the learner completes the rest in Step 6 from the observation log and the process timings.

| Column | Description |
|--------|-------------|
| `Waste Type (DOWNTIME)` | |
| `What It Looks Like Here` | |
| `Process Step` | |
| `Tally Count` | |
| `Est. Time Lost per Morning (min)` | |

**Note:** The three completed rows are worked examples. The learner fills the remaining five from what the data actually shows — some may legitimately be zero, and saying so with evidence is a correct answer.

---

*© 2026 Tertiary Infotech Academy Pte Ltd*
