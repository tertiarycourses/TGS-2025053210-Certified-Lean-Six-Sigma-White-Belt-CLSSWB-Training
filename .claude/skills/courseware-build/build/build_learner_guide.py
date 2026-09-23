#!/usr/bin/env python3
"""Generate the CLSSYB Learner Guide as BOTH a Markdown mirror (LG-*.md at repo
root) and a DOCX (courseware/LG-*.docx) from one source, so they never diverge.

House format: cover page, Document Version Control Record, auto TOC, Arial 11pt
body, one section per DMAIC phase, one sub-section per lab (Objective · Goal ·
What you'll build · Step-by-step · Check your work), plus quick-reference
formulas, assessment preparation and a glossary. All content is driven by
course_data + the domain data files, keeping the LG 100% aligned with the slide
deck, Lesson Plan and labs.
"""
import os, sys
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
from lab_data import LAB_DATA
ACT=DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5
import prodoc
def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and os.path.isdir(os.path.join(d,"labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO=_find_repo(HERE); ASSETS=os.path.join(os.path.dirname(HERE),"assets")

# ---------------- block DSL (single content stream → MD + DOCX) ----------------
B=[]
def h1(t): B.append(("h1",t))
def h2(t): B.append(("h2",t))
def h3(t): B.append(("h3",t))
def p(t):  B.append(("p",t))
def bullets(xs): B.append(("bullets",xs))
def steps(xs): B.append(("steps",xs))
def code(t): B.append(("code",t))
def note(t): B.append(("note",t))
def rule(): B.append(("rule",))

# ---------------- content ----------------
h1("Introduction")
p(f"This Learner Guide accompanies the WSQ course {C.TITLE} ({C.COURSE_CODE}), conducted by {C.ORG}. "
  "This is a one-day Lean Six Sigma awareness course. It follows the DMAIC roadmap end to end — "
  "Define, Measure, Analyze, Improve, Control — with one hands-on lab in each of the five phases, "
  "and provides step-by-step instructions for every lab.")
p("The course content is grounded in the body of knowledge published by The Council for Six Sigma "
  "Certification (CSSC) in 'Six Sigma: A Complete Step-by-Step Guide', so what you learn here matches "
  "the recognised White Belt standard.")
p("As a White Belt you are being prepared to CONTRIBUTE to an improvement team — to understand the "
  "language, recognise waste, and support the tools your team uses. You are not expected to lead a "
  "project or perform the statistical analysis; those belong to the Yellow, Green and Black Belt levels.")
p("Every lab uses one continuous scenario — the BrewBean Cafe morning rush, where customers queue up "
  "to 15 minutes and orders are sometimes made wrong. By the end of the day your five lab outputs form "
  "a complete improvement story: customer requirements and problem statement, process map and waste "
  "tally, root cause analysis, a selected countermeasure with a pilot plan, and a control plan.")

h1("Course Learning Outcomes")
bullets(C.LEARNING_OUTCOMES)

h1("Skills Framework Alignment")
p(f"This course is aligned to the WSQ Technical Skills and Competencies (TSC) {C.TSC_TITLE} ({C.TSC_CODE}).")
h3("Abilities")
bullets(C.TSC_ABILITIES)
h3("Knowledge")
bullets(C.TSC_KNOWLEDGE)

h1("Before You Start")
h3("What you need")
bullets([
 "A laptop with a spreadsheet application (Microsoft Excel, Google Sheets or LibreOffice Calc), or simply pen and paper.",
 "A browser, for the interactive problem-solving tools used in the Analyze lab.",
 "The course slides and this Learner Guide, downloaded from https://lms-tms.tertiaryinfotech.com.",
 "A work process of your own to think about — the tools apply far better when the example is real.",
])
h3("The interactive problem-solving toolkit")
p("Two browser-based tools are used during the labs. No installation or licence is required.")
bullets([
 "5 Whys — build and share a 5 Whys chain: https://alfredang.github.io/5whys/",
 "Fishbone Diagram — build an Ishikawa cause-and-effect diagram: https://alfredang.github.io/fishbone/",
])
h3("How the five labs fit together")
bullets([
 "There are five labs — exactly one for each phase of DMAIC: Define, Measure, Analyze, Improve and Control.",
 "All five labs build on the same BrewBean Cafe scenario, so each lab's output becomes the next lab's input.",
 "Every lab is completed by everyone, and all five map directly to the assessment.",
])
h3("Conventions used in every lab")
bullets([
 "Each lab states its objective, the deliverable you produce, the steps, and a check to confirm you are done.",
 "Tables shown in the steps can be built in a spreadsheet or on the worksheet provided.",
 "Where a lab uses an online tool, the tool URL is shown with the step.",
 "Keep every lab output — they combine into your final improvement package and are your revision material.",
])

# ---------------- per-topic, per-lab ----------------
for t in C.TOPICS:
    label = t["phase"].title() if t["num"] else "Foundations"
    h1(f"{t['phase']} — {t['title']}  ({t['weighting']})")
    p(t["subtitle"])
    h3("Key concepts")
    bullets([f"{name} — {desc}" for name, desc in t["concepts"]])
    for a in [x for x in ACT if x["topic"]==t["num"]]:
        kind = "Elective" if a.get("elective") else "Core"
        title = a["title"].replace("Elective — ","")
        h2(f"Lab {a['num']} — {title}  [{kind}]")
        p(f"Objective: {a['objective']}")
        p(f"Goal: {a['desc']}")
        h3("What you'll build")
        p(a["build"]+f"   (Tools and techniques: {a['services']}.)")
        pack = LAB_DATA.get(a["num"])
        if pack:
            h3("Your data pack")
            p("This lab ships with its own mock data for the BrewBean Cafe scenario. Everything "
              "below is in the lab folder, as CSV files and as one Excel workbook with a tab per "
              "sheet.")
            bullets(
                [f"DATA — {d['title']} ({len(d['rows'])} rows): {d['desc']}"
                 for d in pack.get("datasets", [])] +
                [f"TEMPLATE — {t['title']}: {t['desc']}"
                 for t in pack.get("templates", [])] +
                [f"Excel workbook: lab-{a['num']:02d}-workbook.xlsx — every dataset and template "
                 f"above, one per tab.",
                 "Model answer: model-answer.md — read it AFTER you attempt the lab."])
        h3("Step-by-step")
        steps([(instr,cmd) for instr,cmd in a["steps"]])
        h3("Check your work")
        p(a["test"])
        note(f"The full worksheet, the data, the blank templates and the model answer for this "
             f"lab are in the labs/lab-{a['num']:02d}-*/ folder.")
        rule()

h1("Quick Reference — The DMAIC Roadmap")
h3("What each phase asks, and what it delivers")
bullets([
 "Define — 'What problem are we solving, and for whom?' Delivers the Voice of the Customer, the CTQ requirements, a problem statement, a SMART goal and an agreed scope.",
 "Measure — 'How big is the problem, really?' Delivers a SIPOC, a process map, a data collection plan and a baseline of how the process performs today.",
 "Analyze — 'Why is this happening?' Delivers the shortlisted root causes, supported by 5 Whys, a Fishbone diagram and the data collected in Measure.",
 "Improve — 'What change will actually fix it?' Delivers a selected countermeasure, standard work for the new method, and a pilot plan.",
 "Control — 'How do we make the gain stick?' Delivers a control plan, visual management, an SOP and a handover to the process owner.",
])
h3("A note on Six Sigma measurement")
p("You will hear practitioners refer to a process's 'sigma level' and to DPMO (Defects Per Million "
  "Opportunities) — the measure Six Sigma uses to describe how often a process produces a defect. "
  "The well-known Six Sigma target is 3.4 defects per million opportunities, which is why the method "
  "carries that name.")
p("As a White Belt you are expected to RECOGNISE these terms and understand what they describe. "
  "Calculating DPMO and converting it to a sigma level is done at Yellow Belt and above, and is not "
  "assessed on this course.")

h1("Quick Reference — The Eight Wastes (DOWNTIME)")
bullets([
 "D — Defects: output that fails the requirement and must be corrected or redone.",
 "O — Overproduction: producing more, or earlier, than the customer needs.",
 "W — Waiting: work or people idle, waiting for the next step, an approval or information.",
 "N — Non-utilised talent: skills and ideas of people not being used.",
 "T — Transport: unnecessary movement of materials, work items or information between places.",
 "I — Inventory: work in progress, backlogs and queues sitting between steps.",
 "M — Motion: unnecessary movement of people, or switching between systems and screens.",
 "E — Extra-processing: doing more work to the output than the customer requires or values.",
])

h1("Preparing for the Assessment")
bullets([
 C.ASSESSMENT["written"],
 C.ASSESSMENT["practical"],
 "Both papers are open book — you may use these slides, this Learner Guide and your lab outputs.",
 "Revise by re-reading your own lab outputs; they follow exactly the same scenario as the assessment.",
 "Be ready to define quality, Lean, Six Sigma and Lean Six Sigma, and explain how they differ.",
 "Be ready to describe the belt roles and say where a White Belt contributes to an improvement team.",
 "Be ready to name the eight wastes (DOWNTIME) and give a workplace example of each.",
 "Be ready to explain each DMAIC phase, what it delivers and which tools belong to it.",
 "Be ready to translate a VOC statement into a measurable CTQ requirement.",
 "Be ready to write a problem statement that describes the problem without naming a solution.",
 "Be ready to explain how the Fishbone diagram and 5 Whys are used together to find a root cause.",
 "Be ready to describe what a control plan must contain to hold an improvement in place.",
 "Re-work the labs from memory — being able to produce the tools unaided is the best preparation.",
 C.ASSESSMENT["note"],
])

h1("Glossary")
gl=[
 ("Lean","A method to maximise customer value by systematically identifying and removing waste."),
 ("Six Sigma","A data-driven method to reduce variation and defects; the target is 3.4 defects per million opportunities."),
 ("Lean Six Sigma","The combined method — Lean improves speed and flow, Six Sigma improves consistency and accuracy."),
 ("DMAIC","Define, Measure, Analyze, Improve, Control — the Six Sigma improvement roadmap."),
 ("PDCA","Plan, Do, Check, Act — a lighter improvement cycle used for small, fast improvements."),
 ("VOC","Voice of the Customer — customer needs and expectations expressed in the customer's own words."),
 ("CTQ","Critical to Quality — a specific, measurable requirement translated from a VOC statement."),
 ("SIPOC","Suppliers, Inputs, Process, Outputs, Customers — the macro 'as-is' process map."),
 ("Muda","The Japanese term for waste — any activity that consumes resource but creates no customer value."),
 ("DOWNTIME","Mnemonic for the eight wastes: Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra-processing."),
 ("Value-added (VA)","An activity the customer would be willing to pay for because it changes the product or service."),
 ("Non-value-added (NVA)","An activity that consumes resource but adds nothing the customer values — pure waste."),
 ("Defect","An output that fails to meet the CTQ requirement."),
 ("Common cause variation","Natural, always-present variation built into the process; addressed by changing the process."),
 ("Special cause variation","Unusual variation traceable to a specific assignable event; addressed by investigating that event."),
 ("Pareto principle","The 80/20 rule — roughly 80% of effects come from 20% of causes."),
 ("5 Whys","Repeatedly asking 'why' to drill from a symptom down to an actionable root cause."),
 ("Fishbone (Ishikawa) diagram","A cause-and-effect diagram organising candidate causes into categories such as the 5Ms."),
 ("5M categories","Manpower, Method, Machine, Material, Measurement — standard Fishbone categories."),
 ("DPMO","Defects Per Million Opportunities — the defect-rate measure Six Sigma uses. Recognise the term; calculating it is a Yellow Belt skill."),
 ("Yield","The percentage of output produced without defects."),
 ("Sigma level","A yardstick for process performance derived from DPMO; the Six Sigma target is 3.4 DPMO."),
 ("Discrete data","Data you obtain by counting, such as the number of orders made wrong."),
 ("Continuous data","Data you obtain by measuring on a scale, such as waiting time in minutes."),
 ("Check sheet","A simple structured tally form used to collect process data consistently."),
 ("5S","Sort, Set in order, Shine, Standardise, Sustain — a Lean method for organising the workplace."),
 ("Poka-Yoke","Mistake proofing — designing the process so an error is difficult or impossible to make."),
 ("Standard work","The documented current best-known method for performing a task."),
 ("Pilot","A small-scale trial of a change, run before full rollout so mistakes stay cheap."),
 ("Control plan","The document naming the metric, target, monitoring method, frequency, owner and reaction plan."),
 ("Reaction plan","The agreed steps to take when a controlled measure misses its target."),
 ("Visual management","Making process performance visible at a glance, so problems are noticed the same day."),
 ("SOP","Standard Operating Procedure — written instructions that lock in the improved method."),
]
B.append(("dl",gl))


# ---------------- render Markdown ----------------
def _anchor(txt):
    return "".join(ch.lower() if ch.isalnum() else ("-" if ch in " -" else "") for ch in txt)

def render_md():
    out=[f"# {C.TITLE} — Learner Guide",""]
    out.append(f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Conducted by:** {C.ORG} ({C.UEN.replace('UEN: ','UEN ')})  |  **Version {C.VERSION} · {C.VERSION_DATE}**")
    out.append("")
    # TOC (h1 + h2)
    out.append("## Contents"); out.append("")
    for kind,*rest in B:
        if kind=="h1": out.append(f"- [{rest[0]}](#{_anchor(rest[0])})")
        elif kind=="h2": out.append(f"  - [{rest[0]}](#{_anchor(rest[0])})")
    out.append("")
    for kind,*rest in B:
        if kind=="h1": out+=["",f"## {rest[0]}",""]
        elif kind=="h2": out+=["",f"### {rest[0]}",""]
        elif kind=="h3": out+=[f"**{rest[0]}**",""]
        elif kind=="p": out+=[rest[0],""]
        elif kind=="bullets": out+=[f"- {x}" for x in rest[0]]+[""]
        elif kind=="steps":
            for i,(instr,cmd) in enumerate(rest[0],1):
                out.append(f"{i}. {instr}")
                if cmd: out+=["",f"   ```bash",f"   {cmd}","   ```",""]
            out.append("")
        elif kind=="code": out+=["```bash",rest[0],"```",""]
        elif kind=="note": out+=[f"> **Note:** {rest[0]}",""]
        elif kind=="rule": out+=["---",""]
        elif kind=="dl":
            for term,defn in rest[0]: out.append(f"- **{term}** — {defn}")
            out.append("")
    return "\n".join(out)

MD_OUT=os.path.join(REPO,f"LG-{C.SHORT_TITLE}.md")
with open(MD_OUT,"w") as f: f.write(render_md())
print("Saved",MD_OUT)

# ---------------- render DOCX ----------------
BRAND=RGBColor(0x1F,0x6F,0xEB); DARK=RGBColor(0x11,0x18,0x27); GREY=RGBColor(0x55,0x5B,0x66)
INKCODE=RGBColor(0x0B,0x30,0x60)
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Arial"; normal.font.size=Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc,"LEARNER GUIDE",C.TITLE,C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS,"tertiary-infotech-logo.png"),
                      course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc,[
 ("1","1 July 2026","Initial release — CLSSWB Learner Guide for the one-day Lean Six Sigma awareness course.",C.TRAINER),
 ("2",C.VERSION_DATE,"Guide rebuilt from the single-source content module and restructured to follow the "
  "DMAIC roadmap end to end, with exactly one hands-on lab per DMAIC phase (5 labs). All labs unified "
  "under one continuous scenario (the BrewBean Cafe morning rush) so each lab output feeds the next. "
  "Content simplified to White Belt awareness depth: sigma-level and DPMO calculation, MSA, FMEA, value "
  "stream mapping, Kano analysis, weighted solution-selection matrices and SPC control limits removed "
  "and replaced with recognition-level explanations; quick-reference section changed from formulas to "
  "the DMAIC roadmap; glossary aligned to the tools actually taught.",C.TRAINER),
 ("3",C.VERSION_DATE,"Lab data pack added. Each of the five labs is now a self-contained folder "
  "carrying its mock dataset in CSV and Excel form, blank worksheet templates, a worked model answer "
  "and facilitator notes. The datasets are internally consistent across the five labs — the Lab 2 "
  "observation log is the evidence base for the Lab 3 Pareto, and the Lab 4 pilot results carry into "
  "the Lab 5 monitoring data — so the BrewBean Cafe story reconciles end to end. Lab steps rewritten "
  "to reference the specific data and template files the learner works from.",C.TRAINER),
])
prodoc.add_toc(doc)

def code_para(text):
    for line in text.split("\n"):
        para=doc.add_paragraph(); prodoc._shade_para(para) if hasattr(prodoc,"_shade_para") else None
        r=para.add_run(line); r.font.name="Consolas"; r.font.size=Pt(9.5); r.font.color.rgb=INKCODE

for kind,*rest in B:
    if kind=="h1": doc.add_heading(rest[0],level=1)
    elif kind=="h2": doc.add_heading(rest[0],level=2)
    elif kind=="h3":
        para=doc.add_paragraph(); r=para.add_run(rest[0]); r.bold=True; r.font.size=Pt(11); r.font.color.rgb=BRAND
    elif kind=="p": doc.add_paragraph(rest[0])
    elif kind=="bullets":
        for x in rest[0]: doc.add_paragraph(x,style="List Bullet")
    elif kind=="steps":
        for i,(instr,cmd) in enumerate(rest[0],1):
            para=doc.add_paragraph(style="List Number"); para.add_run(instr)
            if cmd: code_para(cmd)
    elif kind=="code": code_para(rest[0])
    elif kind=="note":
        para=doc.add_paragraph(); r=para.add_run("Note: "); r.bold=True; r.font.color.rgb=BRAND
        para.add_run(rest[0]).font.size=Pt(10)
    elif kind=="rule": doc.add_paragraph("")
    elif kind=="dl":
        for term,defn in rest[0]:
            para=doc.add_paragraph(style="List Bullet")
            r=para.add_run(term+" — "); r.bold=True; para.add_run(defn)

prodoc.add_page_numbers(doc)
prodoc.enable_update_fields(doc)
DOCX_OUT=os.path.join(REPO,"courseware",f"LG-{C.SHORT_TITLE}.docx")
doc.save(DOCX_OUT)
print("Saved",DOCX_OUT)
