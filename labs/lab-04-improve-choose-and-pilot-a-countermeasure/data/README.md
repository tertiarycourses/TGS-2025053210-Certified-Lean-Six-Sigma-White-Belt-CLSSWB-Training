# Lab 4 — Data Pack

*Certified Lean Six Sigma White Belt (CLSSWB) Training · TGS-2025053210 · Version v3*

All figures below are **mock data** created for training. They describe the BrewBean Cafe morning rush scenario used by every lab in this course, and they are internally consistent across the five labs — the Lab 2 observation log is the evidence base for the Lab 3 Pareto, and the Lab 5 monitoring data follows on from the Lab 4 pilot.

## Files in this folder

| File | Format | What it is |
|------|--------|------------|
| `countermeasure-options.csv` | CSV | Countermeasure options with impact, effort and cost |
| `pilot-week-results.csv` | CSV | Pilot week results |
| `lab-04-workbook.xlsx` | Excel | Every dataset **and** every blank template above, one per tab |

> Open the `.xlsx` if you want everything in one place with the templates ready to type into. Open the `.csv` files if you prefer Google Sheets, LibreOffice or a plain text editor.

## Countermeasure options with impact, effort and cost

**File:** `countermeasure-options.csv`  |  **Rows:** 12

Twelve candidate countermeasures the team generated against the shortlisted root causes, scored for impact and effort. Used in Step 5 to plot the impact/effort grid and choose one.

| Column | Description |
|--------|-------------|
| `Option` | |
| `Countermeasure` | |
| `Addresses Which Root Cause` | |
| `Impact (1-5)` | |
| `Effort (1-5)` | |
| `Est. Cost (SGD)` | |
| `Risk` | |

**Note:** Impact 5 = would remove most of the delay; Effort 5 = weeks of work or significant spend. The high-impact / low-effort corner is impact >= 4 and effort <= 2.

## Pilot week results

**File:** `pilot-week-results.csv`  |  **Rows:** 6

What actually happened when the chosen countermeasure was piloted for one week. The same 60-customer observation was repeated each day. Used in Step 7 to judge whether the pilot worked, and carried into Lab 5 as the new baseline.

| Column | Description |
|--------|-------------|
| `Day` | |
| `Date` | |
| `Customers Observed` | |
| `Avg Wait (min)` | |
| `Longest Wait (min)` | |
| `Drinks Remade` | |
| `Mid-order Milk Trips` | |
| `Restock Done Before 07:30?` | |

**Note:** Thursday is deliberately bad — the opening staff member was on leave and the restock was missed. That single row is the most important teaching point in the lab: the countermeasure works, but nothing yet HOLDS it in place. That is exactly what Lab 5 (Control) exists to fix.

---

*© 2026 Tertiary Infotech Academy Pte Ltd*
