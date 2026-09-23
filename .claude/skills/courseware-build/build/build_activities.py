#!/usr/bin/env python3
"""Generate the activities/ folder — ONE FOLDER PER ACTIVITY, each holding the
house artefact set as DOCX **and** PDF, matching the Tertiary Infotech reference
activity packs (reference/Activities/NN - Title/A NN-*.docx|pdf):

    activities/
      README.md
      tools.md
      01 - Stakeholder Influence Mapping/
        A01-Facilitator-Guide-Stakeholder-Influence-Mapping.docx | .pdf
        A01-Learner-Worksheet-Stakeholder-Influence-Mapping.docx | .pdf
        A01-Checklist-Stakeholder-Influence-Mapping.docx         | .pdf
      ...

House format taken from the reference pack:
  * blue banner table (org name + course title · course code)
  * a 4-chip meta row: TYPE / DURATION / MAPS TO / TOPIC
  * Name+Date table on learner-facing sheets
  * Heading 2 sections, Arial 11pt body
  * Facilitator Guide carries the numbered run-sheet as a 3-column table
    (# | Instruction to learners | Facilitator note)
  * Checklist carries a criteria table (# | Criterion | Evidences | ✓)

Content is driven by course_data.py + data_domain1..4.py + data_activity_steps.py
so the packs stay aligned with the slide deck, Lesson Plan and Learner Guide.

HOUSE RULE: the detailed step-by-step lives HERE and in the Learner Guide —
never on the slides.
"""
import os, re, sys, glob, shutil, subprocess, tempfile

from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
from data_activity_steps import STEPS
from build_lab_pack import build_pack
from lab_data import LAB_DATA
ACT=sorted(DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5,key=lambda a:a["num"])
N_ACT=len(ACT)


def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and \
           (os.path.isdir(os.path.join(d,"activities")) or os.path.isdir(os.path.join(d,"labs"))):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO=_find_repo(HERE)
ACTIVITIES=os.path.join(REPO,"activities")

BRAND="1F6FEB"; INK="111827"; GREEN="10B981"; LIGHT="F5F8FC"; LINE="E2E8F0"
BRAND_RGB=RGBColor(0x1F,0x6F,0xEB); INK_RGB=RGBColor(0x11,0x18,0x27)
GREY_RGB=RGBColor(0x55,0x5B,0x66)
RULE="_"*95

def slug(t): return re.sub(r"[^a-z0-9]+","-",t.lower()).strip("-")
def title_slug(t): return re.sub(r"[^A-Za-z0-9]+","-",t).strip("-")

TOPIC_BY_NUM={t["num"]:t for t in C.TOPICS}
TYPE_LABEL={"role_play":"Role Play","case_study":"Case Study"}
DEFAULT_TYPE="Hands-on Lab"

def short_title(a):
    """Activity title without the leading "Phase — " prefix; the phase is already
    carried by the folder order and the MAPS TO chip."""
    return a["title"].split(" — ",1)[1] if " — " in a["title"] else a["title"]


def folder_for(a): return f"{a['num']:02d} - {short_title(a)}"

# ------------------------------------------------------------------ docx bits
def shade(cell,hexfill):
    tcPr=cell._tc.get_or_add_tcPr()
    shd=OxmlElement("w:shd"); shd.set(qn("w:val"),"clear")
    shd.set(qn("w:color"),"auto"); shd.set(qn("w:fill"),hexfill)
    tcPr.append(shd)

def no_borders(table):
    tbl=table._tbl; tblPr=tbl.tblPr
    borders=OxmlElement("w:tblBorders")
    for edge in ("top","left","bottom","right","insideH","insideV"):
        el=OxmlElement(f"w:{edge}"); el.set(qn("w:val"),"none"); el.set(qn("w:sz"),"0")
        borders.append(el)
    tblPr.append(borders)

def new_doc():
    doc=Document()
    n=doc.styles["Normal"]; n.font.name="Arial"; n.font.size=Pt(11)
    for st,sz,col in (("Heading 1",16,BRAND),("Heading 2",13,INK)):
        s=doc.styles[st]; s.font.name="Arial"; s.font.size=Pt(sz); s.font.bold=True
        s.font.color.rgb=RGBColor.from_string(col)
    for s in doc.sections:
        s.left_margin=s.right_margin=Cm(2.26)
        s.top_margin=s.bottom_margin=Cm(2.0)
    return doc

def banner(doc):
    """Blue org/course banner across the top."""
    t=doc.add_table(rows=1,cols=1); t.alignment=WD_TABLE_ALIGNMENT.CENTER
    c=t.rows[0].cells[0]; shade(c,BRAND); no_borders(t)
    p=c.paragraphs[0]; p.space_after=Pt(0)
    r=p.add_run(C.ORG); r.bold=True; r.font.size=Pt(10); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
    p2=c.add_paragraph(); p2.space_before=Pt(0)
    r2=p2.add_run(f"{C.TITLE}  ·  {C.COURSE_CODE}")
    r2.font.size=Pt(8.5); r2.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
    return t

def meta_chips(doc,a):
    """TYPE / DURATION / MAPS TO / TOPIC chip row."""
    t=TOPIC_BY_NUM[a["topic"]]
    chips=[("TYPE",TYPE_LABEL.get(a.get("case_type"),DEFAULT_TYPE)),
           ("DURATION",a["duration"]),
           ("MAPS TO",t["phase"]),
           ("TOPIC",t["title"])]
    tbl=doc.add_table(rows=1,cols=4); no_borders(tbl)
    for cell,(k,v) in zip(tbl.rows[0].cells,chips):
        shade(cell,LIGHT)
        p=cell.paragraphs[0]; p.space_after=Pt(0)
        r=p.add_run(k); r.bold=True; r.font.size=Pt(7.5); r.font.color.rgb=BRAND_RGB
        p2=cell.add_paragraph(); p2.space_before=Pt(0)
        r2=p2.add_run(v); r2.font.size=Pt(9); r2.font.color.rgb=INK_RGB
    doc.add_paragraph()
    return tbl

def name_date(doc):
    t=doc.add_table(rows=2,cols=2); t.style="Table Grid"
    for i,label in enumerate(("Name","Date")):
        c=t.rows[i].cells[0]; c.text=""
        r=c.paragraphs[0].add_run(label); r.bold=True; r.font.size=Pt(9.5)
        shade(c,LIGHT)
        t.rows[i].cells[1].text=""
    doc.add_paragraph()

def head(doc,a,kind):
    p=doc.add_paragraph(); p.space_after=Pt(2)
    r=p.add_run(f"ACTIVITY {a['num']} — {kind}")
    r.bold=True; r.font.size=Pt(12); r.font.color.rgb=BRAND_RGB
    p2=doc.add_paragraph(); p2.space_after=Pt(8)
    r2=p2.add_run(a["title"]); r2.bold=True; r2.font.size=Pt(15); r2.font.color.rgb=INK_RGB

def blanks(doc,n=1):
    for _ in range(n):
        p=doc.add_paragraph(); p.space_after=Pt(2)
        r=p.add_run(RULE); r.font.size=Pt(10); r.font.color.rgb=RGBColor(0xAA,0xB2,0xBF)

def footer_note(doc):
    p=doc.add_paragraph(); p.space_before=Pt(14)
    r=p.add_run(f"{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · "
                f"© 2026 {C.ORG}")
    r.font.size=Pt(8); r.font.color.rgb=GREY_RGB; r.italic=True

# ------------------------------------------------------------------ documents
def facilitator_guide(a):
    sp=STEPS[a["num"]]; t=TOPIC_BY_NUM[a["topic"]]
    doc=new_doc(); banner(doc); head(doc,a,"FACILITATOR GUIDE"); meta_chips(doc,a)

    doc.add_heading("Purpose of this activity",level=2)
    doc.add_paragraph(f"By the end of this activity learners will be able to "
                      f"{a['objective'][0].lower()}{a['objective'][1:]}")

    doc.add_heading("What learners produce",level=2)
    doc.add_paragraph(sp["artefact"])

    doc.add_heading("Materials required",level=2)
    for m in ["Learner Worksheet (one per learner)","Checklist (one per group)",
              "Flipchart or A3 sheet and markers","The course slides for the scenario and framework",
              "Internet access where the activity calls for live research"]:
        doc.add_paragraph(m,style="List Bullet")

    doc.add_heading("Set-up",level=2)
    grouping=("Groups of exactly 3 so every role is played."
              if a.get("roles") else "Groups of 3–5.")
    doc.add_paragraph(f"{grouping} Distribute one worksheet per learner and one checklist per group, "
                      f"and make sure every group can open this activity's data/ folder. All "
                      f"{N_ACT} activities run on the same continuous BrewBean Cafe scenario and "
                      f"follow DMAIC in order, so remind learners where this activity sits in that "
                      f"story — and that its output feeds the next one.")

    doc.add_heading("Scenario / briefing material",level=2)
    for para in a["case_scenario"]:
        doc.add_paragraph(para)

    if a.get("roles"):
        doc.add_heading("Roles",level=2)
        doc.add_paragraph("Assign one role per participant:")
        for name,goal,brief in a["roles"]:
            p=doc.add_paragraph(style="List Bullet")
            r=p.add_run(f"{name} — "); r.bold=True
            r2=p.add_run(f"Goal: {goal}. "); r2.italic=True
            p.add_run(brief)

    doc.add_heading("How to run it — step by step",level=2)
    tbl=doc.add_table(rows=1,cols=3); tbl.style="Table Grid"
    hdr=tbl.rows[0].cells
    for i,h in enumerate(["#","Instruction to learners","Facilitator note"]):
        hdr[i].text=""; r=hdr[i].paragraphs[0].add_run(h)
        r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
        shade(hdr[i],BRAND)
    tips=sp.get("tips",[])
    for i,(heading,instruction) in enumerate(sp["steps"],1):
        cells=tbl.add_row().cells
        cells[0].text=""; cells[0].paragraphs[0].add_run(str(i)).font.size=Pt(9.5)
        cells[1].text=""
        p=cells[1].paragraphs[0]
        r=p.add_run(f"{heading}. "); r.bold=True; r.font.size=Pt(9.5)
        r2=p.add_run(instruction); r2.font.size=Pt(9.5)
        cells[2].text=""
        note=tips[i-1] if i-1 < len(tips) else ""
        cells[2].paragraphs[0].add_run(note).font.size=Pt(9)
        if i%2==0:
            for c in cells: shade(c,LIGHT)

    doc.add_heading("Suggested timing",level=2)
    tt=doc.add_table(rows=1,cols=2); tt.style="Table Grid"
    h=tt.rows[0].cells
    for i,x in enumerate(["Minutes","Phase"]):
        h[i].text=""; r=h[i].paragraphs[0].add_run(x)
        r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
        shade(h[i],BRAND)
    for mins,phase in sp["timing"]:
        c=tt.add_row().cells
        c[0].text=""; c[0].paragraphs[0].add_run(f"{mins} min").font.size=Pt(9.5)
        c[1].text=""; c[1].paragraphs[0].add_run(phase).font.size=Pt(9.5)
    p=doc.add_paragraph()
    r=p.add_run(f"Total: {sum(m for m,_ in sp['timing'])} minutes"); r.bold=True; r.font.size=Pt(9.5)

    doc.add_heading("Discussion & decision prompts",level=2)
    for prompt in a["discussion_prompts"]:
        doc.add_paragraph(prompt,style="List Number")

    doc.add_heading("Debrief",level=2)
    doc.add_paragraph("Bring the class back together and draw out the learning:")
    for b in ["Ask two or three groups to show what they produced, not just what they concluded.",
              "Ask what surprised them — the gap between what they assumed and what they found.",
              f"Link the activity explicitly back to DMAIC · {t['phase']} — {t['title']}.",
              "Remind learners this activity rehearses what the Case Study assessment will require."]:
        doc.add_paragraph(b,style="List Bullet")
    doc.add_paragraph("Reflection questions:")
    for point in a["reflection_points"]:
        doc.add_paragraph(point,style="List Bullet")

    if sp.get("tips"):
        doc.add_heading("Facilitator notes — what to watch for",level=2)
        for tip in sp["tips"]:
            doc.add_paragraph(tip,style="List Bullet")

    doc.add_heading("Success criterion",level=2)
    doc.add_paragraph(a["debrief_check"])

    doc.add_heading("Assessment link",level=2)
    doc.add_paragraph(
        f"This activity builds {t['phase']} — {t['title']}. All {N_ACT} activities are in-class "
        f"activities assessed indirectly through the open-book Case Study (CS) component, which "
        f"reuses the same techniques on the same continuous BrewBean Cafe scenario. Knowledge "
        f"is assessed in the Written Assessment (WA-SAQ). Nothing is assessed that is not "
        f"practised here or taught in the slides.")
    footer_note(doc)
    return doc

def learner_worksheet(a):
    sp=STEPS[a["num"]]; t=TOPIC_BY_NUM[a["topic"]]
    doc=new_doc(); banner(doc); head(doc,a,"LEARNER WORKSHEET"); meta_chips(doc,a); name_date(doc)

    doc.add_heading("What you are doing",level=2)
    doc.add_paragraph(a["case_scenario"][0])
    p=doc.add_paragraph()
    r=p.add_run("What you will produce: "); r.bold=True
    p.add_run(sp["artefact"])

    doc.add_heading("The scenario",level=2)
    for para in a["case_scenario"][1:]:
        doc.add_paragraph(para)

    if a.get("roles"):
        doc.add_heading("Role assignment",level=2)
        rt=doc.add_table(rows=1,cols=3); rt.style="Table Grid"
        h=rt.rows[0].cells
        for i,x in enumerate(["Role","Played by","Goal"]):
            h[i].text=""; r=h[i].paragraphs[0].add_run(x)
            r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
            shade(h[i],BRAND)
        for name,goal,brief in a["roles"]:
            c=rt.add_row().cells
            c[0].text=""; c[0].paragraphs[0].add_run(name).font.size=Pt(9.5)
            c[1].text=""
            c[2].text=""; c[2].paragraphs[0].add_run(goal).font.size=Pt(9.5)
        doc.add_paragraph()

    doc.add_heading("Your steps",level=2)
    for heading,instruction in sp["steps"]:
        p=doc.add_paragraph(style="List Number")
        r=p.add_run(f"{heading} — "); r.bold=True
        p.add_run(instruction)

    doc.add_heading("Your working space",level=2)
    doc.add_paragraph("Complete every field. You may keep this worksheet and refer to it during "
                      "the open-book assessment.")
    for i,(heading,_) in enumerate(sp["steps"],1):
        p=doc.add_paragraph(); p.space_after=Pt(2); p.space_before=Pt(8)
        r=p.add_run(f"Step {i} — {heading}"); r.bold=True; r.font.size=Pt(10)
        r.font.color.rgb=BRAND_RGB
        blanks(doc,2)

    doc.add_heading("Answers to the discussion prompts",level=2)
    for i,prompt in enumerate(a["discussion_prompts"],1):
        p=doc.add_paragraph(); p.space_after=Pt(2); p.space_before=Pt(8)
        r=p.add_run(f"{i}. {prompt}"); r.bold=True; r.font.size=Pt(10)
        blanks(doc,2)

    doc.add_heading("Reflect & discuss",level=2)
    for point in a["reflection_points"]:
        p=doc.add_paragraph(); p.space_after=Pt(2); p.space_before=Pt(8)
        r=p.add_run(point); r.bold=True; r.font.size=Pt(10)
        blanks(doc,2)

    doc.add_heading("Check your work",level=2)
    doc.add_paragraph(a["debrief_check"])
    footer_note(doc)
    return doc

def checklist(a):
    sp=STEPS[a["num"]]; t=TOPIC_BY_NUM[a["topic"]]
    doc=new_doc(); banner(doc); head(doc,a,"CHECKLIST"); meta_chips(doc,a); name_date(doc)

    doc.add_heading(f"Self-check — {a['title']}",level=2)
    doc.add_paragraph("Tick each item you have completed. Any blank is a gap to close before "
                      "your group presents at the debrief.")
    tbl=doc.add_table(rows=1,cols=4); tbl.style="Table Grid"
    h=tbl.rows[0].cells
    for i,x in enumerate(["#","Criterion","Evidences","✓"]):
        h[i].text=""; r=h[i].paragraphs[0].add_run(x)
        r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
        shade(h[i],BRAND)
    for i,item in enumerate(sp["checklist"],1):
        c=tbl.add_row().cells
        c[0].text=""; c[0].paragraphs[0].add_run(str(i)).font.size=Pt(9.5)
        c[1].text=""; c[1].paragraphs[0].add_run(item).font.size=Pt(9.5)
        c[2].text=""; c[2].paragraphs[0].add_run(t["phase"]).font.size=Pt(9.5)
        c[3].text=""
        if i%2==0:
            for cc in c: shade(cc,LIGHT)
    doc.add_paragraph()

    doc.add_heading("Debrief check",level=2)
    p=doc.add_paragraph(); r=p.add_run(a["debrief_check"]); r.font.size=Pt(10.5)

    doc.add_heading("Feedback",level=2)
    for q in ["What did you find hardest in this activity?",
              "What is the ONE thing you will do differently at work?"]:
        p=doc.add_paragraph(); p.space_after=Pt(2); p.space_before=Pt(8)
        r=p.add_run(q); r.bold=True; r.font.size=Pt(10)
        blanks(doc,2)
    footer_note(doc)
    return doc

# ------------------------------------------------------------------ pdf
_SOFFICE=shutil.which("soffice") or shutil.which("libreoffice")

def to_pdf(docx_path):
    """Convert a DOCX to PDF beside it. Returns True on success."""
    if not _SOFFICE: return False
    outdir=os.path.dirname(docx_path)
    with tempfile.TemporaryDirectory() as tmp:
        profile=os.path.join(tmp,"lo")
        try:
            subprocess.run([_SOFFICE,"--headless",
                            f"-env:UserInstallation=file://{profile}",
                            "--convert-to","pdf","--outdir",outdir,docx_path],
                           check=True,capture_output=True,timeout=240)
        except Exception:
            return False
    return os.path.exists(os.path.splitext(docx_path)[0]+".pdf")

# ------------------------------------------------------------------ indexes
def readme_md():
    L=[f"# {C.TITLE} — Activities",""]
    L.append(f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**")
    L.append("")
    L.append(f"{N_ACT} hands-on activities — exactly one per phase of the **DMAIC roadmap**. Every "
             "activity runs on one continuous scenario, the **BrewBean Cafe morning rush**, and each "
             "activity's output becomes the next one's input, so by the end of the day your work "
             "forms a single complete improvement package.")
    L.append("")
    L.append("## What each activity folder contains")
    L.append("")
    L.append("| Artefact | What it is | Who uses it |")
    L.append("|---|---|---|")
    L.append("| `ANN-Facilitator-Guide-*.docx` / `.pdf` | Purpose, materials, set-up, scenario, the "
             "numbered run-sheet with facilitator notes, timing, debrief and success criterion | Trainer |")
    L.append("| `ANN-Learner-Worksheet-*.docx` / `.pdf` | The scenario, the steps, and a working space "
             "to capture the output and prompt answers | Learner |")
    L.append("| `ANN-Checklist-*.docx` / `.pdf` | Criteria table to tick before the debrief, plus feedback | Learner group |")
    L.append("| `data/` | The mock datasets as `.csv`, plus one `.xlsx` workbook holding every dataset "
             "and template on its own tab, and a data dictionary | Learner |")
    L.append("| `templates/` | Blank worksheets to fill in, as `.csv` | Learner |")
    L.append("| `model-answer.md` | The worked model answer — read it *after* attempting the activity | Learner |")
    L.append("")
    L.append("> The **detailed step-by-step instructions live here and in the Learner Guide — never "
             "on the slides.** The trainer facilitates the scenario and discussion from the deck "
             "while learners work from these sheets and the data.")
    L.append("")
    L.append("## Activities")
    L.append("")
    L.append("| # | DMAIC phase | Activity | Type | Duration | Data pack | Folder |")
    L.append("|---|---|---|---|---|---|---|")
    for a in ACT:
        t=TOPIC_BY_NUM[a["topic"]]; d=folder_for(a)
        pk=LAB_DATA.get(a["num"],{})
        nds=len(pk.get("datasets",[])); ntp=len(pk.get("templates",[]))
        blurb=f"{nds} dataset{'s' if nds!=1 else ''} + {ntp} template{'s' if ntp!=1 else ''}" if pk else "—"
        L.append(f"| {a['num']} | {t['phase']} | {a['title']} | "
                 f"{TYPE_LABEL.get(a.get('case_type'),DEFAULT_TYPE)} | {a['duration']} | {blurb} | `{d}/` |")
    L.append("")
    L.append("## About the data")
    L.append("")
    L.append("Every figure is **mock data** built for training. It is internally consistent across "
             "all five activities:")
    L.append("")
    L.append("- The Activity 2 observation log is the evidence base for the Activity 3 Pareto.")
    L.append("- The Activity 3 root cause is what the Activity 4 countermeasure addresses.")
    L.append("- The Activity 4 pilot results carry into the Activity 5 monitoring data.")
    L.append("")
    L.append("So the numbers you quote in one activity still hold in the next, and the whole "
             "BrewBean Cafe story reconciles from Define through to Control.")
    L.append("")
    L.append("See [tools.md](tools.md) for the frameworks and free tools used across the activities.")
    L.append("")
    L.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*")
    L.append("")
    return "\n".join(L)


def tools_md():
    L=["# Lean Six Sigma Toolkit","",f"*{C.TITLE} · {C.COURSE_CODE}*",""]
    L.append("## Frameworks used in the activities")
    L.append("")
    L.append("| Framework | What it does | Used in |")
    L.append("|---|---|---|")
    for r in [
        ("Voice of the Customer (VOC)","Captures what customers say in their own words, before any interpretation.","Activity 1"),
        ("Critical to Quality (CTQ)","Turns each customer need into something measurable with a number and a unit.","Activity 1"),
        ("Problem statement","States what is wrong, where, since when and how big — never the solution.","Activity 1"),
        ("SMART goal","Specific, Measurable, Achievable, Relevant, Time-bound.","Activity 1"),
        ("SIPOC","A one-page process overview: Suppliers, Inputs, Process, Outputs, Customers.","Activity 2"),
        ("Process mapping","Draws the steps as they really happen, with observed times and VA/NVA judgement.","Activity 2"),
        ("The eight wastes (DOWNTIME)","Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra-processing.","Activity 2"),
        ("Check sheets","A simple tally form — the easiest reliable way to collect data.","Activity 2"),
        ("5 Whys","Drills DOWN one cause-and-effect chain until it reaches something actionable.","Activity 3"),
        ("Fishbone (Ishikawa) diagram","Spreads WIDE across Manpower, Method, Machine, Material, Measurement.","Activity 3"),
        ("Pareto chart","Roughly 80% of the problem comes from 20% of the causes — the vital few.","Activity 3"),
        ("Common vs special cause","Separates variation built into the process from one-off events.","Activity 3"),
        ("Impact/effort grid","Screens countermeasures so the team picks high impact and low effort first.","Activity 4"),
        ("5S","Sort, Set in order, Shine, Standardise, Sustain.","Activity 4"),
        ("Mistake proofing (Poka-Yoke)","Makes the error hard or impossible to make.","Activity 4"),
        ("Standard work","Writes the better method down so everyone does it the same way.","Activity 4"),
        ("Control plan","Measure, target, frequency, owner, and the reaction when it slips.","Activity 5"),
        ("Visual management","Makes performance visible so drift is noticed the same day.","Activity 5"),
        ("Leading vs lagging indicators","Separates the early warning from the after-the-fact confirmation.","Activity 5"),
    ]:
        L.append(f"| {r[0]} | {r[1]} | {r[2]} |")
    L.append("")
    L.append("## Interactive online tools")
    L.append("")
    L.append("These browser-based tools are free and need no installation or licence.")
    L.append("")
    L.append("| Tool | What it does |")
    L.append("|---|---|")
    L.append("| [5 Whys](https://alfredang.github.io/5whys/) | Build and share a 5 Whys root-cause chain |")
    L.append("| [Fishbone Diagram](https://alfredang.github.io/fishbone/) | Build an Ishikawa cause-and-effect diagram |")
    L.append("| [Pareto Chart](https://alfredang.github.io/paretochart/) | Collaborative brainstorm, vote, and a live Pareto chart |")
    L.append("| [NovaSPC](https://alfredang.github.io/novaspc/) | Run charts, SPC charts and process capability from your own CSV |")
    L.append("")
    L.append("## The eight wastes — DOWNTIME")
    L.append("")
    L.append("| Letter | Waste | What it looks like at BrewBean Cafe |")
    L.append("|---|---|---|")
    for l,name,ex in [
        ("D","Defects","Drinks made wrong and remade"),
        ("O","Overproduction","Drinks prepared before an order is placed"),
        ("W","Waiting","Customers queueing; cups waiting at the barista station"),
        ("N","Non-utilised talent","A trained barista walking to the back store for milk"),
        ("T","Transport","The cup travelling from till to barista station"),
        ("I","Inventory","Cups queued at the barista station waiting to be made"),
        ("M","Motion","Walking to the back store mid-order"),
        ("E","Extra-processing","Writing the order on the cup, then re-keying it into the till"),
    ]:
        L.append(f"| **{l}** | {name} | {ex} |")
    L.append("")
    L.append("## The DMAIC roadmap")
    L.append("")
    L.append("| Phase | The question it asks | What it delivers |")
    L.append("|---|---|---|")
    for ph,q,d in [
        ("Define","What problem are we solving, and for whom?","VOC, CTQs, problem statement, SMART goal, scope"),
        ("Measure","How big is the problem, really?","SIPOC, process map, data collection, the baseline"),
        ("Analyze","Why is this happening?","Shortlisted root causes backed by evidence"),
        ("Improve","What change will actually fix it?","A selected countermeasure, standard work, a pilot plan"),
        ("Control","How do we hold the gain?","Control plan, visual management, SOP, huddle, handover"),
    ]:
        L.append(f"| **{ph}** | {q} | {d} |")
    L.append("")
    L.append(f"*{C.TITLE} · {C.COURSE_CODE} · © 2026 {C.ORG}*")
    L.append("")
    return "\n".join(L)


# ------------------------------------------------------------------ repo README
def repo_readme():
    def enc(p): return p.replace(" ","%20").replace("(","%28").replace(")","%29")
    L=[f"# {C.COURSE_CODE} - {C.TITLE}",""]
    L.append(f"> **Course:** WSQ - {C.TITLE}  ")
    L.append(f"> **Course Code:** {C.COURSE_CODE}  ")
    L.append("> **Register here:** https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-white-belt-clsswb-training.html")
    L.append("")
    L.append(f"These are the hands-on activity packs for the WSQ {C.TITLE} course delivered by "
             "[Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/).")
    L.append("")
    L.append(f"This repository contains **{N_ACT} guided Lean Six Sigma White Belt activities** — "
             "exactly one per phase of the **DMAIC roadmap** — grounded in the Council for Six Sigma "
             "Certification (CSSC) White Belt body of knowledge. Every activity runs on one "
             "continuous scenario, the BrewBean Cafe morning rush, and ships with its own mock data.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Courseware")
    L.append("")
    L.append("| Artifact | File |")
    L.append("|----------|------|")
    lg_md=f"LG-{C.SHORT_TITLE}.md"
    L.append(f"| **Slide deck** | `courseware/{C.SHORT_TITLE}-{C.VERSION}.pptx` (and `.pdf`) |")
    L.append(f"| **Learner Guide (Markdown)** | [{lg_md}]({enc(lg_md)}) |")
    L.append(f"| **Learner Guide (DOCX/PDF)** | `courseware/LG-{C.SHORT_TITLE}.docx` (and `.pdf`) |")
    L.append(f"| **Lesson Plan (DOCX/PDF)** | `courseware/LP-{C.SHORT_TITLE}.docx` (and `.pdf`) |")
    L.append("| **Activity Index** | [activities/README.md](activities/README.md) |")
    L.append("| **Tools and Frameworks** | [activities/tools.md](activities/tools.md) |")
    L.append("")
    L.append("> **Note:** assessment papers, answer keys and trainer-only materials are "
             "intentionally not published in this repository.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Activities")
    L.append("")
    L.append("Each activity folder carries the full house pack:")
    L.append("")
    L.append("| File | What it is |")
    L.append("|------|------------|")
    L.append("| `ANN-Facilitator-Guide-*.docx` / `.pdf` | Trainer run-sheet: purpose, set-up, "
             "scenario, numbered steps with facilitator notes, timing, debrief |")
    L.append("| `ANN-Learner-Worksheet-*.docx` / `.pdf` | The learner's sheet: scenario, steps and "
             "a working space |")
    L.append("| `ANN-Checklist-*.docx` / `.pdf` | Criteria to tick before the debrief |")
    L.append("| `data/` | Mock datasets (`.csv`) + `ANN-Data-Workbook.xlsx` + data dictionary |")
    L.append("| `templates/` | Blank worksheets to fill in (`.csv`) |")
    L.append("| `model-answer.md` | Worked model answer |")
    L.append("")
    for a in ACT:
        t=TOPIC_BY_NUM[a["topic"]]; d=folder_for(a)
        L.append(f"**{a['num']}. {short_title(a)}** — DMAIC · {t['phase']} · {a['duration']}  ")
        L.append(f"[Folder]({enc('activities/'+d+'/')}) · "
                 f"[Data]({enc('activities/'+d+'/data/')}) · "
                 f"[Model answer]({enc('activities/'+d+'/model-answer.md')})")
        L.append("")
    L.append("---")
    L.append("")
    L.append("## How to use")
    L.append("")
    L.append("1. Read the Learner Guide first — it follows the same DMAIC order as the course.")
    L.append(f"2. Work the {N_ACT} activities in order; each one's output feeds the next.")
    L.append("3. Open the activity's `data/` folder — the CSVs or the Excel workbook — and work "
             "from the real figures, not from memory.")
    L.append("4. Fill the blank templates as you go, then tick the Checklist before the debrief.")
    L.append("5. Compare against `model-answer.md` only after you have attempted the activity.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Repository structure")
    L.append("")
    L.append("```")
    L.append("courseware/          slide deck (PPTX + PDF), Learner Guide, Lesson Plan")
    L.append("  assets/            diagrams and images used by the deck")
    L.append(f"activities/          {N_ACT} activity folders + index + toolkit")
    L.append("  NN - <name>/       one folder per activity:")
    L.append("    ANN-Facilitator-Guide-*.docx|pdf")
    L.append("    ANN-Learner-Worksheet-*.docx|pdf")
    L.append("    ANN-Checklist-*.docx|pdf")
    L.append("    data/            mock datasets + Excel workbook + data dictionary")
    L.append("    templates/       blank worksheets")
    L.append("    model-answer.md")
    L.append(f"LG-{C.SHORT_TITLE}.md")
    L.append("                     Learner Guide (Markdown mirror of the DOCX)")
    L.append(".claude/skills/courseware-build/build/")
    L.append("                     single-source generators: one content module")
    L.append("                     drives the deck, LP, LG and activities")
    L.append("```")
    L.append("")
    L.append("All artifacts are generated from `course_data.py` + `data_domainN.py` + "
             "`lab_data.py`, so the deck, Lesson Plan, Learner Guide and activities stay 100% "
             "aligned. The datasets are internally consistent across activities, so the BrewBean "
             "Cafe story reconciles from Define through to Control.")
    L.append("")
    L.append("## Interactive tools")
    L.append("")
    L.append("- [5 Whys](https://alfredang.github.io/5whys/) — root-cause chain builder")
    L.append("- [Fishbone Diagram](https://alfredang.github.io/fishbone/) — Ishikawa cause-and-effect builder")
    L.append("- [Pareto Chart](https://alfredang.github.io/paretochart/) — collaborative brainstorm, vote and live chart")
    L.append("- [NovaSPC](https://alfredang.github.io/novaspc/) — run charts, SPC charts and process capability")
    L.append("")
    L.append("## Reference")
    L.append("")
    L.append("- [Council for Six Sigma Certification - Lean Six Sigma White Belt Certification](https://www.sixsigmacouncil.org/lean-six-sigma-white-belt-certification/)")
    L.append("- [Course registration page](https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-white-belt-clsswb-training.html)")
    L.append("- [activities/tools.md](activities/tools.md) - frameworks, formulas and free tools")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"*Version {C.VERSION} · {C.VERSION_DATE} · © 2026 {C.ORG}*")
    L.append("")
    return "\n".join(L)


# ------------------------------------------------------------------ main
if __name__=="__main__":
    os.makedirs(ACTIVITIES,exist_ok=True)

    for name,text in (("README.md",readme_md()),("tools.md",tools_md())):
        with open(os.path.join(ACTIVITIES,name),"w",encoding="utf-8") as f: f.write(text)
        print("Wrote activities/"+name)
    with open(os.path.join(REPO,"README.md"),"w",encoding="utf-8") as f: f.write(repo_readme())
    print("Wrote README.md")

    pdf_ok=pdf_skip=0
    for a in ACT:
        d=os.path.join(ACTIVITIES,folder_for(a)); os.makedirs(d,exist_ok=True)
        ts=title_slug(short_title(a)); n=f"A{a['num']:02d}"
        for kind,builder in (("Facilitator-Guide",facilitator_guide),
                             ("Learner-Worksheet",learner_worksheet),
                             ("Checklist",checklist)):
            path=os.path.join(d,f"{n}-{kind}-{ts}.docx")
            builder(a).save(path)
            if to_pdf(path): pdf_ok+=1
            else: pdf_skip+=1
        # the mock data pack (CSV + XLSX + templates + model answer) for this activity
        pk=build_pack(a["num"],a["title"],d)
        extra=""
        if pk:
            extra=(f", {len(pk['datasets'])} dataset(s) ({pk['rows']} rows), "
                   f"{len(pk['templates'])} template(s), {pk['xlsx']}, model answer")
        print(f"Wrote {folder_for(a)}/  (3 sheets{extra})")

    print(f"\nPDFs rendered: {pdf_ok}   failed/skipped: {pdf_skip}")
    if pdf_skip and not _SOFFICE:
        print("NOTE: soffice/libreoffice not found — PDFs were not rendered.")

    # superseded layouts are reported, never deleted automatically
    stale=[]
    old_labs=os.path.join(REPO,"labs")
    if os.path.isdir(old_labs):
        stale.append(os.path.relpath(old_labs,REPO)+"/")
    for old in sorted(glob.glob(os.path.join(ACTIVITIES,"lab-*"))):
        stale.append(os.path.relpath(old,REPO))
    if stale:
        print("\nNOTE: superseded lab layout still present (not deleted automatically):")
        for p in stale: print("  "+p)
        print("  Remove or archive once you are satisfied with activities/.")
