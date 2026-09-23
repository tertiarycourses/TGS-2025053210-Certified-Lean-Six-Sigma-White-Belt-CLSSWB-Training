#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WSQ assessment set — Certified Lean Six Sigma White Belt (CLSSWB) Training
(TGS-2025053210). Produces FOUR DOCX in assessment/:

    WA (SAQ) - <title> - v2.docx                  question paper
    Answer to WA (SAQ) - <title> - v2.docx        answer key
    Case Study (CS) - <title> - v2.docx           question paper
    Answer to Case Study (CS) - <title> - v2.docx answer key

MIRRORS THE ORIGINAL PAPER pulled from the TMS (v1), exactly:
  * Instrument types      : WA (SAQ) + Case Study (CS)   — a CS stays a CS
  * WA  : 2 questions, 30 minutes — Q1 (K1, K2), Q2 (K3, K4, K5)
  * CS  : 4 questions, 30 minutes — Q1 (A1, A2), Q2 (A3), Q3 (A4), Q4 (A5)
  * Same K/A codes and the same mapping.

WHAT CHANGED vs the original: only the CONTENT. The original WA asked about
X-bar/R control charts and the Cp capability index — practitioner statistics that
a one-day White Belt AWARENESS course does not teach. WSQ requires that nothing be
assessed which is not covered in class, so every question here is answerable from
this course's own slides and labs, while the question count, codes and timings are
untouched.

Page layout (house standard): page 1 cover; page 2 Trainee Information +
Instructions + Grading block ONLY; scenario/questions start on page 3.
Assessments carry the cover page only — no Document Version Control Record.
"""
import os
import sys

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL, WD_BREAK

# ----------------------------------------------------------------- config
TITLE = "Certified Lean Six Sigma White Belt (CLSSWB) Training"
COURSE_CODE = "TGS-2025053210"
VERSION = "v7"
WA_MINUTES = "30 minutes"
CS_MINUTES = "30 minutes"


def _find_repo():
    env = os.environ.get("REPO")
    if env and os.path.isdir(env):
        return os.path.abspath(env)
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, ".git")) or \
           (os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs"))):
            return d
        d = os.path.dirname(d)
    return os.getcwd()


REPO = _find_repo()
OUT = os.path.join(REPO, "assessment")
os.makedirs(OUT, exist_ok=True)

# prodoc.py gives the WSQ house cover page (same as the LP / LG).
for _cand in (os.path.join(REPO, ".claude/skills/courseware-build/build"),
              os.path.join(REPO, ".claude/skills/tertiary-lesson-plan"),
              os.path.expanduser("~/.claude/skills/tertiary-lesson-plan")):
    if os.path.exists(os.path.join(_cand, "prodoc.py")):
        sys.path.insert(0, _cand)
        break
import prodoc  # noqa: E402

prodoc.TGS = f"TGS Ref No: {COURSE_CODE}"


def _logo(name):
    here = os.path.dirname(os.path.abspath(__file__))
    for p in (os.path.join(REPO, "courseware/assets", name), os.path.join(here, "assets", name)):
        if os.path.exists(p):
            return p
    return None


ORG_LOGO = _logo("tertiary-infotech-logo.png") or _logo("tertiary-logo.png")

DARK = RGBColor(0x16, 0x1B, 0x26)
BRAND = RGBColor(0x1F, 0x6F, 0xEB)
GREY = RGBColor(0x55, 0x5B, 0x66)

# ================================================================ WA — content
# Mirrors the original: TWO questions, Q1 -> (K1, K2), Q2 -> (K3, K4, K5).
# K1/K2 are the course's declared TSC knowledge codes; K3-K5 continue the
# original paper's numbering and are covered by the same taught material.
WRITTEN = [
    dict(
        num=1,
        codes="K1, K2",
        context=(
            "Lean and Six Sigma began as two separate improvement methods and are now most often "
            "used together as Lean Six Sigma. Understanding what each one attacks is the "
            "foundation for everything else in the DMAIC roadmap."
        ),
        question=(
            "Explain the difference between Lean and Six Sigma, and describe what Lean Six Sigma "
            "combines. In your answer, state what each method is mainly trying to remove or reduce, "
            "and explain what is meant by 'quality' in this context."
        ),
        lines=8,
        answer=[
            "Quality means meeting the customer's requirements — not merely being free of defects. "
            "A product or service can be defect-free against an internal spec and still fail the "
            "customer. (Slides: Foundations — What is Quality?)",
            "Lean is about SPEED and FLOW. It maximises customer value by systematically identifying "
            "and removing WASTE — any activity that consumes time or resource but that the customer "
            "would not pay for. (Slides: Foundations — What is Lean?)",
            "Six Sigma is about CONSISTENCY and ACCURACY. It is a data-driven method that reduces "
            "VARIATION and DEFECTS so the process produces a predictable result every time. "
            "(Slides: Foundations — What is Six Sigma?)",
            "Lean Six Sigma combines the two: faster flow AND fewer defects, with decisions made from "
            "data rather than opinion. Lean alone can make a bad process faster; Six Sigma alone can "
            "make a slow process consistent. Together they address both. "
            "(Slides: Foundations — The Combined Method)",
            "Accept any reasonable phrasing that separates Lean = waste/speed from "
            "Six Sigma = variation/defects, and that defines quality in terms of the customer.",
        ],
    ),
    dict(
        num=2,
        codes="K3, K4, K5",
        context=(
            "A cafe has asked an improvement team to look at its morning rush. Customers are queuing "
            "for up to 15 minutes between 7:30am and 9:00am, some drinks are made wrong and have to "
            "be remade, and the team has begun collecting data at the counter."
        ),
        question=(
            "Using this situation:\n"
            "a) Name the five phases of the DMAIC roadmap in the correct order, and state in one "
            "sentence what the team does in each phase.\n"
            "b) Identify THREE of the eight wastes (DOWNTIME) that are present in this situation, "
            "and give the evidence for each one.\n"
            "c) Propose two follow-up actions the team should take next, and justify each."
        ),
        lines=14,
        answer=[
            "a) The five DMAIC phases, in order (Slides: Foundations — The DMAIC Roadmap; each phase "
            "section opener):",
            "   • DEFINE — understand and state the problem: capture the Voice of the Customer, "
            "translate it into measurable CTQ requirements, and write a problem statement and a "
            "SMART goal without naming a solution.",
            "   • MEASURE — see what is really happening: map the process (SIPOC and a step-by-step "
            "map), decide what data to collect, and establish a baseline of current performance.",
            "   • ANALYZE — find the cause: use 5 Whys, a Fishbone diagram and a Pareto chart to get "
            "from the symptom to a root cause supported by the data.",
            "   • IMPROVE — fix the cause: generate countermeasures against the proven root cause, "
            "screen them, write standard work and pilot the change at small scale.",
            "   • CONTROL — hold the gain: put a control plan, visual management and an SOP in place "
            "and hand the improved process back to the people who run it.",
            "b) Any THREE of the eight wastes, each with evidence "
            "(Slides: Measure — The Eight Wastes of Lean / DOWNTIME in Practice):",
            "   • WAITING — customers standing in the queue for up to 15 minutes; drinks waiting on "
            "the counter to be called out.",
            "   • DEFECTS — drinks made wrong and remade; the wrong order handed over.",
            "   • MOTION — the barista walking back and forth because cups, lids and milk are stored "
            "apart from where the drinks are made.",
            "   • INVENTORY — a growing line of unmade orders building up on the rail during the rush.",
            "   • EXTRA-PROCESSING — writing the order on a cup and then re-keying it into the till.",
            "   • TRANSPORT — carrying milk from the back store to the counter repeatedly.",
            "   Accept any three correctly named wastes with plausible supporting evidence.",
            "c) Two reasonable follow-up actions, each justified. Accept any two of, or similar to:",
            "   • Finish the MEASURE phase before changing anything — record actual wait times and "
            "tally the wastes on a check sheet, so the team has a baseline to compare against and is "
            "acting on data rather than opinion.",
            "   • Move to ANALYZE and run a 5 Whys and a Fishbone on the biggest observed delay, so "
            "the team fixes the root cause rather than the symptom (e.g. hiring more staff when the "
            "real cause is that counter milk is never restocked before the rush).",
            "   • Build a Pareto chart of the delay causes to identify the vital few that account for "
            "most of the problem, so effort goes where it has the most effect.",
            "   Do NOT award a solution proposed with no supporting cause analysis "
            "(e.g. 'hire more staff') unless the candidate explicitly notes it is premature.",
        ],
    ),
]

# ================================================================ CS — content
# Mirrors the original: FOUR questions, Q1 -> (A1, A2), Q2 -> (A3), Q3 -> (A4), Q4 -> (A5).
SCENARIO_TITLE = "Scenario: The BrewBean Cafe Morning Rush"
SCENARIO = (
    "BrewBean Cafe is a busy coffee shop in the CBD serving mainly office workers on their way to "
    "work. Over the past two months the cafe has received a rising number of online complaints about "
    "slow service, and several regular customers have said they now buy their coffee elsewhere. "
    "Management has formed a small improvement team and you have joined it as the White Belt member, "
    "supporting the team rather than leading the project. Initial observations of the 7:30am-9:00am "
    "morning rush show:"
)
SCENARIO_POINTS = [
    "A sample of 60 customers was timed across one morning rush: the average wait was "
    f"8.9 minutes and the longest was 15.0 minutes, against the cafe's own "
    "5-minute service promise.",
    "Only one till is open at peak hour, even though two are installed.",
    "Milk runs out at the counter during the rush and has to be fetched from the back store.",
    "Orders are written on the cup and then re-keyed into the till.",
    "7 drinks were made wrong and had to be remade, delaying everyone behind in the queue.",
    "No one currently records how long customers actually wait.",
]
SCENARIO_TAIL = (
    "Answer all four questions below in relation to this scenario. Your answers should reflect the "
    "White Belt role — supporting and contributing to the improvement team."
)

CASE = [
    dict(
        num=1,
        codes="A1, A2",
        labs="Activity 1",
        question=(
            "Based on the information provided and using the DMAIC framework, outline THREE things the "
            "improvement team should establish in the DEFINE phase to scope this problem properly. "
            "Briefly explain the purpose of each, and write a suitable problem statement for BrewBean "
            "Cafe."
        ),
        lines=14,
        answer=[
            "Any THREE of the following, each with its purpose (Activity 1 — Define: Customer Requirements "
            "and the Problem Statement, worked against voc-raw-customer-feedback.csv; "
            "Slides: DMAIC · Define):",
            "• VOICE OF THE CUSTOMER (VOC) — capture what customers actually say, in their own words "
            "(e.g. 'I'm late for work because the queue is too slow'). Purpose: ground the project in "
            "real customer need rather than the team's assumptions.",
            "• CRITICAL TO QUALITY (CTQ) REQUIREMENTS — translate each VOC statement into something "
            "specific and measurable with a number and a unit (e.g. 'served within 5 minutes'). "
            "Purpose: give the team a testable target it can measure against.",
            "• PROBLEM STATEMENT — state what is wrong, where, since when and how big, without naming "
            "a solution. Purpose: get everyone agreeing on the same problem before any work starts.",
            "• SMART GOAL — Specific, Measurable, Achievable, Relevant, Time-bound. Purpose: make "
            "clear what success looks like and by when.",
            "• SCOPE (in / out) — agree explicitly what the project covers. Purpose: keep a small "
            "project small and prevent scope creep.",
            "• PROJECT CHARTER — one page carrying the problem, goal, scope and team. Purpose: the "
            "project's 'contract' so the sponsor and team are aligned.",
            "",
            "MODEL PROBLEM STATEMENT (accept any wording containing all four components — what, "
            "where/when, how much, and impact, with NO solution):",
            "\"Between 7:30am and 9:00am over the past two months, customers at BrewBean Cafe waited "
            "an average of up to 15 minutes to be served against a 5-minute service promise, "
            "generating a rising number of online complaints and the loss of several regular "
            "customers.\"",
            "",
            "DO NOT award a problem statement that contains a solution (e.g. '...because we need to "
            "open a second till'), or one with no measure, no time period or no stated impact.",
        ],
    ),
    dict(
        num=2,
        codes="A3",
        labs="Activity 3",
        question=(
            "The team needs to find out WHY the queue is slow rather than guessing. Recommend a "
            "root cause analysis approach the team should use, explain why it is suitable, and apply "
            "it to ONE of the problems observed in the scenario."
        ),
        lines=14,
        answer=[
            "Recommend 5 WHYS and/or a FISHBONE (Ishikawa) DIAGRAM, and explain the choice "
            "(Activity 3 — Analyze: Find the Root Cause, worked against delay-reason-pareto-data.csv "
            "and cause-evidence-sheet.csv; Slides: DMAIC · Analyze):",
            "• Why suitable: both are simple, quick, team-based tools that need no statistics, which "
            "suits a White Belt team acting on observations. They move the team from the SYMPTOM "
            "('the queue is slow') to a CAUSE it can actually act on. Fixing a symptom makes the "
            "problem come back; fixing the cause does not.",
            "• 5 Whys drills DOWN one chain of cause and effect; a Fishbone spreads WIDE across "
            "categories (Manpower, Method, Machine, Material, Measurement) to make sure no whole "
            "area of cause is missed. Used together they are stronger than either alone.",
            "",
            "WORKED 5 WHYS (accept any chain that ends in something the team can act on):",
            "  PROBLEM: Customers wait up to 15 minutes at 8:00am against a 5-minute promise.",
            "  WHY? Drinks are not made fast enough to clear the queue.",
            "  WHY? The barista keeps stopping part-way through making an order.",
            "  WHY? The milk at the counter runs out during the rush.",
            "  WHY? It is not restocked before the rush starts.",
            "  ROOT CAUSE: No one owns restocking counter milk before 7:30am — it was never made "
            "part of the opening routine.",
            "",
            "ALTERNATIVE (equally acceptable) — Fishbone categories for 'Morning queue is too slow':",
            "  Manpower — one till open at peak; no cover for breaks.",
            "  Method — no restocking routine; order re-keyed into the till.",
            "  Machine — only one grinder; card machine slow.",
            "  Material — milk stored at the back; cups and lids kept apart.",
            "  Measurement — wait time not tracked; no target agreed; complaints not logged.",
            "",
            "Credit the candidate for stopping at an ACTIONABLE cause and for not blaming a person "
            "(if an answer names an individual rather than a process, the chain should continue).",
        ],
    ),
    dict(
        num=3,
        codes="A4",
        labs="Activity 2",
        question=(
            "List TWO measures (KPIs) BrewBean Cafe should collect to understand how the process is "
            "really performing, explain why each is important, and state for each whether it is "
            "discrete or continuous data and how it would be collected."
        ),
        lines=14,
        answer=[
            "Any TWO sensible measures, each with purpose, data type and collection method "
            "(Activity 2 — Measure, worked against morning-rush-observation-log.csv and "
            "process-step-timings.csv; Slides: DMAIC · Measure):",
            "• CUSTOMER WAIT TIME (minutes, from joining the queue to receiving the drink). "
            "Why: it is the measure the customer actually experiences and it maps directly to the "
            "5-minute CTQ, so it tells the team whether the promise is being met. "
            "Data type: CONTINUOUS (measured on a scale). "
            "Collected by: timing a sample of customers with a stopwatch at set intervals during the "
            "rush, recorded on a check sheet.",
            "• NUMBER OF DRINKS REMADE (count per morning). "
            "Why: each remake is a defect that consumes barista time twice and pushes back everyone "
            "in the queue, so it links a quality problem directly to the delay. "
            "Data type: DISCRETE (counted). "
            "Collected by: a tally on a check sheet at the counter each time a drink is remade.",
            "",
            "Other acceptable measures: number of customers served per hour (discrete, counted from "
            "till records); queue length at fixed times (discrete, counted by observation); number of "
            "complaints per week (discrete, counted from the online reviews).",
            "",
            "A complete answer must, for EACH measure: name it, justify why it matters, correctly "
            "classify it as discrete (counted) or continuous (measured), and say how it would be "
            "recorded. The point about agreeing WHAT is recorded, WHO records it and WHEN — before "
            "collection starts — should be credited.",
        ],
    ),
    dict(
        num=4,
        codes="A5",
        labs="Activity 5",
        question=(
            "Suppose the team makes a change and the average wait time improves, but after one month "
            "it has drifted back towards 15 minutes. Recommend what the team should do to make the "
            "improvement stick, and describe what a control plan for BrewBean Cafe would contain."
        ),
        lines=14,
        answer=[
            "The drift back is exactly what the CONTROL phase exists to prevent — without it, "
            "processes quietly return to the old way (Activity 5 — Control, worked against "
            "post-improvement-monitoring.csv, whose week 3 shows precisely this drift; "
            "Slides: DMAIC · Control).",
            "",
            "A CONTROL PLAN for BrewBean Cafe should name:",
            "• THE MEASURE — the one number that shows the improvement is still working "
            "(e.g. average customer wait time at 8:00am).",
            "• THE TARGET — 5 minutes or less, taken from the CTQ agreed in Define.",
            "• THE FREQUENCY / MONITORING METHOD — how and how often it is checked "
            "(e.g. timed sample of five customers every morning, recorded on the check sheet).",
            "• THE OWNER — a named person accountable for it (e.g. the duty shift supervisor). "
            "A control plan with no named owner is only a wish.",
            "• THE REACTION PLAN — the exact steps to take when the measure misses target "
            "(e.g. open the second till immediately; escalate to the manager if missed three days "
            "running).",
            "",
            "Alongside the control plan, credit any of:",
            "• STANDARD WORK / SOP — write the improved method down as short numbered steps "
            "(e.g. 'restock counter milk before 7:30am') and pin it up, so everyone works the same way.",
            "• VISUAL MANAGEMENT — put the wait-time measure on a board where the whole shift can see "
            "it, so a problem is noticed the same day rather than at the end of the month.",
            "• TEAM HUDDLES — a short daily stand-up to review the measure and surface problems while "
            "they are still small.",
            "• HANDOVER — formally hand the improved process to the people who run it every day, so "
            "ownership does not disappear when the improvement team disbands.",
            "",
            "A strong answer recognises that the drift means the CONTROL phase was skipped or is not "
            "being followed — not that the original countermeasure was necessarily wrong.",
        ],
    ),
]

# ================================================================ coverage check
def check_coverage():
    """Fail the build if any declared K or A code is not assessed."""
    ks = {c.strip() for q in WRITTEN for c in q["codes"].split(",")}
    as_ = {c.strip() for q in CASE for c in q["codes"].split(",")}
    want_k = {"K1", "K2", "K3", "K4", "K5"}
    want_a = {"A1", "A2", "A3", "A4", "A5"}
    missing_k, missing_a = want_k - ks, want_a - as_
    print("\nCOVERAGE MAP")
    print("  WA (knowledge):")
    for q in WRITTEN:
        print(f"    Q{q['num']}  ({q['codes']})")
    print("  CS (ability):")
    for q in CASE:
        print(f"    Q{q['num']}  ({q['codes']})")
    if missing_k or missing_a:
        raise SystemExit(f"\n!! COVERAGE FAILURE — missing K: {sorted(missing_k)}  missing A: {sorted(missing_a)}")
    print(f"  OK — all K {sorted(want_k)} and all A {sorted(want_a)} covered.\n")


# ================================================================ doc helpers
def new_doc():
    d = Document()
    n = d.styles["Normal"]
    n.font.name = "Arial"
    n.font.size = Pt(11)
    return d


def line(d, text="", bold=False, size=11, color=DARK, after=6, align=None, italic=False):
    p = d.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    if align is not None:
        p.alignment = align
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.name = "Arial"
    return p


def bullet(d, text):
    p = d.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text)
    r.font.size = Pt(11)
    r.font.name = "Arial"
    r.font.color.rgb = DARK
    return p


def page_break(d):
    d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def cover(d, instrument, is_key):
    """WSQ house cover page — same as the LP / LG. Cover only, no version record."""
    label = f"{instrument} — Answer Key" if is_key else instrument
    prodoc.add_cover_page(d, label.upper(), TITLE, VERSION.lstrip("v"),
                          org_logo=ORG_LOGO, course_logo=None, course_code=COURSE_CODE)


def candidate_page(d, minutes, extra=None):
    """Page 2 — Trainee Information + Instructions + Grading block, and nothing else."""
    line(d, "A: Trainee Information", bold=True, size=12, after=6)
    line(d, "Trainee Name (as per NRIC): _________________________________________", after=6)
    line(d, "Last 3 digits and alphabet of NRIC / FIN: ___________________________", after=6)
    line(d, "Date: ______________________________", after=14)

    line(d, "B: Instructions to Candidate", bold=True, size=12, after=6)
    for t in [
        "1. This is an individual exercise.",
        "2. This is an open book assessment. You may refer to the course slides, the Learner Guide "
        "and your own activity outputs.",
        f"3. A total of {minutes} is given to complete this assessment.",
        "4. Answer ALL questions in the space provided on this document.",
        "5. Submit your completed answers on the LMS at https://lms-tms.tertiaryinfotech.com/",
    ] + (extra or []):
        line(d, t, after=4)
    line(d, "", after=10)

    line(d, "C: For Official Use Only", bold=True, size=12, after=6)
    line(d, "Grade: _________ (C / NYC)", after=6)
    line(d, "Assessor Name: ____________________________    Assessor NRIC: ____________________", after=6)
    line(d, "Date: _____________________________________    Signature: ________________________", after=6)


def answer_box(d, n_lines):
    """Ruled answer space.

    A run of underscores is used rather than paragraph borders: LibreOffice
    merges the borders of consecutive empty paragraphs into one rule. 68
    characters of Arial 11 fits inside the page margins without wrapping.
    """
    line(d, "Answer:", bold=True, color=GREY, after=4)
    for _ in range(n_lines):
        line(d, "_" * 68, color=GREY, after=8)


# ================================================================ builders
def build_wa(is_key):
    d = new_doc()
    cover(d, "Written Assessment (SAQ)", is_key)  # prodoc's cover ends with a page break

    if is_key:
        line(d, "Written Assessment (SAQ) — Model Answers / Marking Guide",
             bold=True, size=14, color=BRAND, after=4)
        line(d, "TRAINER COPY — not to be issued to candidates.",
             bold=True, size=11, color=RGBColor(0xB0, 0x1C, 0x2E), after=10)
        line(d, f"Duration: {WA_MINUTES}  ·  Open book  ·  All questions are open-ended (no multiple choice).",
             size=10, color=GREY, after=14)
    else:
        candidate_page(d, WA_MINUTES)
        page_break(d)
        line(d, "D: Short Answer Questions", bold=True, size=12, after=4)
        line(d, "Answer BOTH questions. Each question shows the knowledge codes it assesses.",
             size=10, color=GREY, after=12)

    for q in WRITTEN:
        line(d, f"Question {q['num']} ({q['codes']})", bold=True, size=12, color=BRAND, after=4)
        line(d, q["context"], size=10, color=GREY, italic=True, after=6)
        line(d, q["question"], after=8)
        if is_key:
            line(d, "Model answer — award for any reasonable equivalent wording:",
                 bold=True, size=10, color=GREY, after=4)
            for pt in q["answer"]:
                if pt == "":
                    line(d, "", after=2)
                else:
                    bullet(d, pt)
            line(d, "", after=12)
        else:
            answer_box(d, q["lines"])
            line(d, "", after=10)

    name = ("Answer to WA (SAQ)" if is_key else "WA (SAQ)") + f" - {TITLE} - {VERSION}.docx"
    out = os.path.join(OUT, name)
    d.save(out)
    print("  saved", os.path.basename(out))


def build_cs(is_key):
    d = new_doc()
    cover(d, "Case Study (CS)", is_key)  # prodoc's cover ends with a page break

    if is_key:
        line(d, "Case Study (CS) Assessment — Model Answers / Marking Guide",
             bold=True, size=14, color=BRAND, after=4)
        line(d, "TRAINER COPY — not to be issued to candidates.",
             bold=True, size=11, color=RGBColor(0xB0, 0x1C, 0x2E), after=10)
        line(d, f"Duration: {CS_MINUTES}  ·  Open book  ·  All questions are open-ended (no multiple choice).",
             size=10, color=GREY, after=14)
    else:
        candidate_page(d, CS_MINUTES)
        page_break(d)

    line(d, "D: Case Study", bold=True, size=12, after=6)
    line(d, SCENARIO_TITLE, bold=True, size=11, after=4)
    line(d, SCENARIO, after=6)
    for pt in SCENARIO_POINTS:
        bullet(d, pt)
    line(d, "", after=4)
    line(d, SCENARIO_TAIL, italic=True, size=10, color=GREY, after=12)

    for q in CASE:
        cite = f"  [{q['labs']}]" if q.get("labs") else ""
        line(d, f"Question {q['num']} ({q['codes']}){cite}", bold=True, size=12, color=BRAND,
             after=4)
        line(d, q["question"], after=8)
        if is_key:
            line(d, "Model answer — award for any reasonable equivalent wording:",
                 bold=True, size=10, color=GREY, after=4)
            for pt in q["answer"]:
                if pt == "":
                    line(d, "", after=2)
                else:
                    bullet(d, pt)
            line(d, "", after=12)
        else:
            answer_box(d, q["lines"])
            line(d, "", after=10)

    name = ("Answer to Case Study (CS)" if is_key else "Case Study (CS)") + f" - {TITLE} - {VERSION}.docx"
    out = os.path.join(OUT, name)
    d.save(out)
    print("  saved", os.path.basename(out))


if __name__ == "__main__":
    check_coverage()
    print(f"Building assessment set into {OUT}")
    build_wa(False)
    build_wa(True)
    build_cs(False)
    build_cs(True)
    print("\nDone — 4 DOCX. Mirrors the TMS original: WA 2 questions / 30 min, CS 4 questions / 30 min.")
