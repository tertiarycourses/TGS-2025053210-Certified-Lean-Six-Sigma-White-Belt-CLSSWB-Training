#!/usr/bin/env python3
"""Generate the per-lab DATA PACK — the mock datasets (CSV + XLSX), the blank
worksheet templates, the worked model answer and the facilitator notes that sit
inside each labs/lab-NN-*/ folder.

Driven entirely by lab_data.py + course_data.py + data_domainN.py, so the pack
can never drift out of alignment with the slides, LG, LP or assessment.

Called by build_labs.py (which owns the folder layout and writes the lab README
into the same folder), so a single `build_labs.py` run produces the whole pack.

Layout produced per lab:

    labs/lab-01-define.../
        README.md                  the lab worksheet (written by build_labs.py)
        data/                      mock datasets - one .csv per dataset
        data/<lab>-workbook.xlsx   ALL datasets + blank templates, one per tab
        templates/                 blank worksheets - one .csv per template
        model-answer.md            the worked model answer
        facilitator-notes.md       trainer-facing notes
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from lab_data import LAB_DATA

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    HAVE_XLSX = True
except ImportError:                                    # pragma: no cover
    HAVE_XLSX = False

# ------------------------------------------------------------------ house style
BRAND = "1F4E79"          # header fill - matches the LP/LG table header
BRAND_LIGHT = "DCE6F1"    # template header fill
GREY = "808080"

HDR_FONT = Font(bold=True, color="FFFFFF", size=10, name="Arial")
TPL_FONT = Font(bold=True, color="1F4E79", size=10, name="Arial")
BODY_FONT = Font(size=10, name="Arial")
TITLE_FONT = Font(bold=True, size=13, color="1F4E79", name="Arial")
NOTE_FONT = Font(italic=True, size=9, color="808080", name="Arial")

THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def write_csv(path, headers, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for r in rows:
            w.writerow(r)


def _autosize(ws, headers, rows, start_row):
    """Column widths from the actual content, capped so a wide comment column
    does not push the sheet off the screen."""
    for ci, h in enumerate(headers, 1):
        widest = len(str(h))
        for r in rows:
            if ci - 1 < len(r):
                widest = max(widest, len(str(r[ci - 1])))
        ws.column_dimensions[get_column_letter(ci)].width = min(max(widest + 3, 10), 46)


def add_sheet(wb, name, title, desc, headers, rows, notes="", template=False):
    """One tab: title, description, a formatted header row and the data."""
    ws = wb.create_sheet(title=name[:31])
    ws["A1"] = title
    ws["A1"].font = TITLE_FONT
    ws["A2"] = desc
    ws["A2"].font = NOTE_FONT
    ws["A2"].alignment = Alignment(wrap_text=False, vertical="top")

    hr = 4
    fill = PatternFill("solid", fgColor=BRAND_LIGHT if template else BRAND)
    font = TPL_FONT if template else HDR_FONT
    for ci, h in enumerate(headers, 1):
        c = ws.cell(row=hr, column=ci, value=h)
        c.font = font
        c.fill = fill
        c.border = BORDER
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    ws.row_dimensions[hr].height = 30

    for ri, row in enumerate(rows, hr + 1):
        for ci, v in enumerate(row, 1):
            c = ws.cell(row=ri, column=ci, value=v)
            c.font = BODY_FONT
            c.border = BORDER
            c.alignment = Alignment(vertical="top", wrap_text=isinstance(v, str) and len(str(v)) > 45)

    if notes:
        nr = hr + len(rows) + 2
        ws.cell(row=nr, column=1, value="Note: " + notes).font = NOTE_FONT

    _autosize(ws, headers, rows, hr)
    ws.freeze_panes = ws.cell(row=hr + 1, column=1)
    return ws


def build_workbook(lab_num, lab_title, pack, out_path):
    """One .xlsx per lab holding every dataset and every blank template as tabs,
    behind a cover tab that says what each tab is for."""
    if not HAVE_XLSX:
        return False
    wb = Workbook()
    wb.remove(wb.active)

    cover = wb.create_sheet("About this workbook")
    cover["A1"] = f"Activity {lab_num} — {lab_title}"
    cover["A1"].font = Font(bold=True, size=15, color="1F4E79", name="Arial")
    cover["A2"] = f"{C.TITLE}  ·  {C.COURSE_CODE}  ·  Version {C.VERSION}"
    cover["A2"].font = NOTE_FONT
    cover["A4"] = ("Scenario: BrewBean Cafe morning rush. Every activity in this course uses the same "
                   "scenario, so your outputs build into one improvement package.")
    cover["A4"].font = BODY_FONT

    r = 6
    cover.cell(row=r, column=1, value="Tab").font = HDR_FONT
    cover.cell(row=r, column=2, value="Type").font = HDR_FONT
    cover.cell(row=r, column=3, value="What it is for").font = HDR_FONT
    for ci in (1, 2, 3):
        cover.cell(row=r, column=ci).fill = PatternFill("solid", fgColor=BRAND)
        cover.cell(row=r, column=ci).border = BORDER
    r += 1

    for d in pack.get("datasets", []):
        add_sheet(wb, d["name"], d["title"], d["desc"], d["headers"], d["rows"],
                  d.get("notes", ""), template=False)
        cover.cell(row=r, column=1, value=d["name"][:31]).font = BODY_FONT
        cover.cell(row=r, column=2, value="Data (read it)").font = BODY_FONT
        cover.cell(row=r, column=3, value=d["title"]).font = BODY_FONT
        r += 1
    for t in pack.get("templates", []):
        add_sheet(wb, t["name"], t["title"], t["desc"], t["headers"], t["rows"],
                  "", template=True)
        cover.cell(row=r, column=1, value=t["name"][:31]).font = BODY_FONT
        cover.cell(row=r, column=2, value="Template (fill it in)").font = BODY_FONT
        cover.cell(row=r, column=3, value=t["title"]).font = BODY_FONT
        r += 1

    cover.column_dimensions["A"].width = 34
    cover.column_dimensions["B"].width = 22
    cover.column_dimensions["C"].width = 60
    wb.save(out_path)
    return True


def data_readme(lab_num, lab_title, pack):
    """The data dictionary — what each file is, what each column means."""
    o = []
    o.append(f"# Activity {lab_num} — Data Pack")
    o.append("")
    o.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION}*")
    o.append("")
    o.append("All figures below are **mock data** created for training. They describe the "
             "BrewBean Cafe morning rush scenario used by every activity in this course, and they "
             "are internally consistent across the five activities — the Activity 2 observation "
             "log is the evidence base for the Activity 3 Pareto, and the Activity 5 monitoring "
             "data follows on from the Activity 4 pilot.")
    o.append("")
    o.append("## Files in this folder")
    o.append("")
    o.append("| File | Format | What it is |")
    o.append("|------|--------|------------|")
    for d in pack.get("datasets", []):
        o.append(f"| `{d['name']}.csv` | CSV | {d['title']} |")
    o.append(f"| `A{lab_num:02d}-Data-Workbook.xlsx` | Excel | Every dataset **and** every blank "
             f"template above, one per tab |")
    o.append("")
    o.append("> Open the `.xlsx` if you want everything in one place with the templates ready to "
             "type into. Open the `.csv` files if you prefer Google Sheets, LibreOffice or a "
             "plain text editor.")
    o.append("")
    for d in pack.get("datasets", []):
        o.append(f"## {d['title']}")
        o.append("")
        o.append(f"**File:** `{d['name']}.csv`  |  **Rows:** {len(d['rows'])}")
        o.append("")
        o.append(d["desc"])
        o.append("")
        o.append("| Column | Description |")
        o.append("|--------|-------------|")
        for h in d["headers"]:
            o.append(f"| `{h}` | |")
        o.append("")
        if d.get("notes"):
            o.append(f"**Note:** {d['notes']}")
            o.append("")
    o.append("---")
    o.append("")
    o.append(f"*© 2026 {C.ORG}*")
    o.append("")
    return "\n".join(o)


def model_md(lab_num, lab_title, pack):
    o = []
    o.append(f"# Activity {lab_num} — Model Answer")
    o.append("")
    o.append(f"**{lab_title}**")
    o.append("")
    o.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION}*")
    o.append("")
    o.append("> **Use this AFTER you have attempted the activity.** There is rarely one right answer "
             "in Lean Six Sigma — what matters is whether your reasoning is supported by the "
             "data. Compare your thinking with the model, not just your wording.")
    o.append("")
    for heading, lines in pack.get("model", []):
        o.append(f"## {heading}")
        o.append("")
        o.append("```")
        for ln in lines:
            o.append(ln)
        o.append("```")
        o.append("")
    o.append("---")
    o.append("")
    o.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*")
    o.append("")
    return "\n".join(o)


def facilitator_md(lab_num, lab_title, pack):
    f = pack.get("facilitator", {})
    o = []
    o.append(f"# Activity {lab_num} — Facilitator Notes")
    o.append("")
    o.append(f"**{lab_title}**")
    o.append("")
    o.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · TRAINER COPY*")
    o.append("")
    o.append("## Timing")
    o.append("")
    o.append(f.get("timing", ""))
    o.append("")
    o.append("## Setup")
    o.append("")
    o.append(f.get("setup", ""))
    o.append("")
    o.append("## What to watch for while they work")
    o.append("")
    for w in f.get("watch", []):
        o.append(f"- {w}")
    o.append("")
    o.append("## Common mistakes")
    o.append("")
    for m in f.get("mistakes", []):
        o.append(f"- {m}")
    o.append("")
    o.append("## Debrief")
    o.append("")
    o.append(f.get("debrief", ""))
    o.append("")
    o.append("---")
    o.append("")
    o.append(f"*© 2026 {C.ORG}*")
    o.append("")
    return "\n".join(o)


def build_pack(lab_num, lab_title, folder):
    """Write the data/, templates/, model answer and facilitator notes for one
    lab into an existing lab folder. Returns a summary dict for the caller."""
    pack = LAB_DATA.get(lab_num)
    if not pack:
        return None

    data_dir = os.path.join(folder, "data")
    tpl_dir = os.path.join(folder, "templates")
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(tpl_dir, exist_ok=True)

    for d in pack.get("datasets", []):
        write_csv(os.path.join(data_dir, d["name"] + ".csv"), d["headers"], d["rows"])
    for t in pack.get("templates", []):
        write_csv(os.path.join(tpl_dir, t["name"] + ".csv"), t["headers"], t["rows"])

    xlsx_name = f"A{lab_num:02d}-Data-Workbook.xlsx"
    build_workbook(lab_num, lab_title, pack, os.path.join(data_dir, xlsx_name))

    with open(os.path.join(data_dir, "README.md"), "w") as f:
        f.write(data_readme(lab_num, lab_title, pack))
    with open(os.path.join(folder, "model-answer.md"), "w") as f:
        f.write(model_md(lab_num, lab_title, pack))
    # NOTE: the facilitator-facing notes are published as the house
    # ANN-Facilitator-Guide-*.docx/.pdf by build_activities.py, so no separate
    # facilitator-notes.md is written here (it would duplicate that sheet).

    return dict(
        datasets=[d["name"] for d in pack.get("datasets", [])],
        templates=[t["name"] for t in pack.get("templates", [])],
        xlsx=xlsx_name,
        rows=sum(len(d["rows"]) for d in pack.get("datasets", [])),
    )


if __name__ == "__main__":
    if not HAVE_XLSX:
        print("WARNING: openpyxl not installed — .xlsx workbooks will be skipped.")
    print("build_lab_pack is called by build_labs.py; run that instead.")
