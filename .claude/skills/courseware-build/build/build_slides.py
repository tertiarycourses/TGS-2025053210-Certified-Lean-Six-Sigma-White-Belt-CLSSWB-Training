#!/usr/bin/env python3
"""Build the CLSSYB slide deck — all-white Tertiary house style, DMAIC order.

Structure:
  Cover → Admin (TRAQOM, trainers x2, ground rules, LMS, lesson plan, TSC,
  outcomes, course outline, briefing, assessment, assessment flow)
  → Foundations → D → M → A → I → C  (each phase: concept slides then its labs)
  → Wrap-up → TRAQOM → Certificate → Assessment → Assessment Flow → Digital Attendance → Thank You

Content comes entirely from course_data.py + data_domainN.py + concepts.py so the
PPT, LP, LG and labs stay 100% aligned.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
from lab_data import LAB_DATA
from components import (Deck, BLUE, TEAL, AMBER, RED, VIOLET, INK, GREY, LIGHT,
                        WHITE, LINE, DMAIC_COLORS)
import concepts

ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and \
           (os.path.isdir(os.path.join(d, "activities")) or os.path.isdir(os.path.join(d, "labs"))):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
ASSETS = os.path.join(REPO, "courseware", "assets")


def asset(name):
    p = os.path.join(ASSETS, name)
    return p if os.path.exists(p) else None


d = Deck(C)

# ============================================================ COVER
d.cover(logo=asset("tertiary-logo.png"))

# ============================================================ ADMIN
d.section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")

d.flow_h("Digital Attendance (Mandatory)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR code with your phone camera",
    "Key in your NRIC/FIN and submit",
    "Repeat for AM, PM and the assessment",
    "Keep 75% attendance to stay eligible for funding",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=BLUE)

# --- two trainer profile cards (house hard rule) ---
d.trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
                "General Trainer template —\nto be completed by the trainer",
                [("Name", ""), ("Title / Designation", ""), ("Qualifications", ""),
                 ("Areas of expertise", ""), ("Training & industry experience", ""), ("Contact", "")],
                initials="?", accent=GREY, photo=asset("trainer_template.png"))
d.trainer_slide("YOUR TRAINER", C.TRAINER,
                "Principal Trainer\nTertiary Infotech Academy Pte. Ltd.",
                [("Role", "Principal Trainer, Tertiary Infotech Academy Pte. Ltd."),
                 ("Qualifications", "PhD; Certified Lean Six Sigma practitioner and trainer."),
                 ("Delivers", "WSQ courses on Lean Six Sigma, quality management and data analytics."),
                 ("Experience", "Process improvement across manufacturing, service and technology sectors."),
                 ("Founder", "Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
                initials="AA", accent=BLUE, photo=asset("trainer_profile.png"))

d.content("Let's Know Each Other", [
    "Your name, organisation and role.",
    "Your experience with process improvement or quality work (if any).",
    "One process at work that frustrates you — we may use it as your course scenario.",
], kicker="ICE-BREAKER")

d.tile_grid("Ground Rules", [
    "Set your mobile phone to silent mode.",
    "Participate actively — no question is too small.",
    "Mutual respect: agree to disagree.",
    "One conversation at a time.",
    "Be punctual; return from breaks on time.",
    "75% attendance is required for certification.",
], kicker="HOUSEKEEPING", cols=2, size=15)

# --- Download course material (visual step flow, not a bullet wall) ---
lms = asset("lms_download.png")
if lms:
    d.image_slide("Download Your Course Material", lms,
                  kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com",
                  caption="Log in to lms-tms.tertiaryinfotech.com to download the slides, Learner Guide and activity files.")
else:
    d.flow_h("Download Your Course Material", [
        "Go to lms-tms.tertiaryinfotech.com",
        "Sign in with the account details given in class",
        "Open this course from your dashboard",
        "Download the slides, Learner Guide and activity files",
        "Keep them open — the assessment is open book",
    ], kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com", color=TEAL)

# --- Lesson plan ---
d.two_col("Lesson Plan — 1 Day, 8 Hours",
          [("Morning — Foundations and Define", 0),
           ("Digital attendance (AM) · Introductions", 1),
           ("Foundations: Quality, Lean, Six Sigma, Lean Six Sigma", 1),
           ("Belt roles and the DMAIC roadmap", 1),
           ("DEFINE: VOC, CTQ, problem statement, SMART goal", 1),
           ("Activity 1 — Define: requirements and problem statement", 1),
           ("MEASURE: process mapping, SIPOC, data, the 8 wastes", 1),
           ("Activity 2 — Measure: map the process, spot the waste", 1)],
          [("Afternoon — Analyze, Improve, Control", 0),
           ("Digital attendance (PM)", 1),
           ("ANALYZE: root cause, 5 Whys, Fishbone, Pareto", 1),
           ("Activity 3 — Analyze: find the root cause", 1),
           ("IMPROVE: solutions, 5S, mistake proofing, piloting", 1),
           ("Activity 4 — Improve: choose and pilot a countermeasure", 1),
           ("CONTROL: control plan, visual management, handover", 1),
           ("Activity 5 — Control: hold the gain · Revision", 1),
           ("Briefing · Final Assessment (WA + CS)", 1)],
          kicker="SCHEDULE · 9:30am-6:30pm with a 1-hour lunch",
          lhead="Morning", rhead="Afternoon")

# --- WSQ TSC alignment ---
d.content(f"Skills Framework — TSC: {C.TSC_TITLE}", [
    f"TSC Code: {C.TSC_CODE}",
] + C.TSC_ABILITIES + C.TSC_KNOWLEDGE, kicker="WSQ SKILLS FRAMEWORK", size=16)

d.tile_grid("Learning Outcomes", [
    ("LO1 — Core concepts", "Describe quality, Lean, Six Sigma and the belt roles in an improvement team."),
    ("LO2 — The DMAIC roadmap", "Explain the five phases of DMAIC and what happens in each."),
    ("LO3 — Define", "Identify customer requirements and a clear problem statement."),
    ("LO4 — Measure", "Describe how a process is mapped and measured, and identify the 8 wastes."),
    ("LO5 — Analyze", "Identify likely causes using 5 Whys and Fishbone analysis."),
    ("LO6 — Improve & Control", "Describe actions that fix a cause and hold the gain."),
], kicker="WHAT YOU'LL ACHIEVE", cols=2, size=14)

d.dmaic_wheel("Course Outline — We Follow DMAIC End to End", [
    ("D", "Define", ["VOC and CTQ", "Problem statement", "SMART goal, charter", "Activity 1"]),
    ("M", "Measure", ["Process mapping, SIPOC", "Types of data", "The 8 wastes", "Activity 2"]),
    ("A", "Analyze", ["Root cause", "5 Whys, Fishbone", "Pareto, variation", "Activity 3"]),
    ("I", "Improve", ["Generating solutions", "5S, mistake proofing", "Standard work, pilot", "Activity 4"]),
    ("C", "Control", ["Control plan", "Visual management", "SOPs and handover", "Activity 5"]),
], kicker="COURSE ROADMAP")

# --- Briefing BEFORE assessment (house hard rule) ---
d.tile_grid("Briefing for Assessment", [
    ("Phones away", "Place phones and other materials under the table or on the floor."),
    ("No recording", "No photos or recording of assessment scripts."),
    ("Work alone", "No discussion of any kind during the assessment."),
    ("Black or blue pen", "Use a black or blue pen for hard-copy assessments."),
    ("No correction fluid", "No liquid paper or correction tape on your script."),
    ("Pens down on time", "Scripts are collected as soon as time is up."),
], kicker="BEFORE YOU SIT THE ASSESSMENT", cols=2, size=14, accent=VIOLET)

d.tile_grid("Assessment", [
    ("Written Assessment (WA)", C.ASSESSMENT["written"]),
    ("Case Study (CS)", C.ASSESSMENT["practical"]),
    ("Open book", "Slides, Learner Guide, your activity outputs and approved materials only."),
    ("Attendance", C.ASSESSMENT["note"]),
    ("Result", "Graded Competent (C) or Not Yet Competent (NYC) by the assessor."),
    ("Appeals", "An appeal process is available if you wish to contest a result."),
], kicker="FINAL ASSESSMENT", cols=2, size=14, accent=VIOLET)

d.flow_h("Assessment Flow", [
    "TRAQOM survey — scan the QR code on the LMS",
    "Assessment digital attendance — scan the SSG QR",
    "Sit the WA (SAQ), then the Case Study — open book",
    "Submit your answers on the LMS",
    "Sign the Assessment Summary Record",
], kicker="ON ASSESSMENT DAY", color=VIOLET)

# NOTE: no Practice Exam slide — there is no CLSSYB practice exam available.
# (The bundled courseware/assets/practice_exam.png belongs to a DIFFERENT course
# — CompTIA CySA+, TGS-2024049211 — and must never be used in this deck.)

# ============================================================ FOUNDATIONS
concepts.foundations(d)

# ============================================================ DMAIC PHASES + LABS
PHASE_FN = {
    1: concepts.define_phase,
    2: concepts.measure_phase,
    3: concepts.analyze_phase,
    4: concepts.improve_phase,
    5: concepts.control_phase,
}
TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"] == t["num"]] for t in C.TOPICS}


def render_labs(acts, phase_label):
    for a in acts:
        opt = a.get("elective", False)
        tag = f"ACTIVITY {a['num']}"
        d.activity_overview(tag, a["title"], a["desc"], a["build"], a["services"],
                            kicker=f"{phase_label} · HANDS-ON", elective=opt)
        # what the learner has been given to work from, before the steps begin
        pack = LAB_DATA.get(a["num"])
        if pack:
            tiles = [(d_["title"], f"{len(d_['rows'])} rows — {d_['name']}.csv")
                     for d_ in pack.get("datasets", [])]
            ntp = len(pack.get("templates", []))
            if ntp:
                tiles.append((f"{ntp} blank templates",
                              "Worksheets to fill in — one per step group"))
            tiles.append((f"A{a['num']:02d}-Data-Workbook.xlsx",
                          "Every dataset and template, one per tab"))
            d.tile_grid(f"Your Data Pack — Activity {a['num']}", tiles,
                        kicker=f"ACTIVITY {a['num']} · WHAT YOU HAVE BEEN GIVEN",
                        cols=2, size=13)
        steps = a["steps"]
        total = len(steps)
        # Eyebrow: the DMAIC phase, not a character-truncated title — the full
        # title already sits in the H1 directly beneath it.
        short = phase_label.replace("DMAIC · ", "")
        # Awareness-level course: two steps per slide keeps the one-day deck tight
        # while every step stays on screen for the learner.
        numbered = [(i, instr) for i, (instr, _cmd) in enumerate(steps, 1)]
        for j in range(0, len(numbered), 2):
            d.step_pair_slide(f"ACTIVITY {a['num']} · {short}", a["title"],
                              numbered[j:j + 2], total)
        d.test_slide(a["title"], a["test"], kicker=f"ACTIVITY {a['num']} · VERIFY")


# Foundations labs (topic 0) come right after the foundations concepts
render_labs(TOPIC_ACTS.get(0, []), "FOUNDATIONS")

for t in C.TOPICS:
    if t["num"] == 0:
        continue
    idx = t["num"] - 1
    col = DMAIC_COLORS[idx % len(DMAIC_COLORS)]
    d.section(f"DMAIC · {t['phase']}", t["title"], t["code"], t["subtitle"])
    d.tile_grid(f"Key Concepts — {t['phase'].title()}", t["concepts"],
                kicker=f"{t['phase']} · {t['weighting']} OF THE COURSE", cols=2, size=14, accent=col)
    # teaching content for this phase
    PHASE_FN[t["num"]](d)
    # labs that belong to this phase
    acts = TOPIC_ACTS.get(t["num"], [])
    if acts:
        core = [a for a in acts if not a.get("elective")]
        opts = [a for a in acts if a.get("elective")]
        rows = []
        for a in core:
            rows.append((f"Activity {a['num']} — {a['title'][:46]}", a["build"][:70]))
        for a in opts:
            rows.append((f"Activity {a['num']} (elective) — {a['title'].replace('Elective — ', '')[:40]}",
                         a["build"][:70]))
        d.tile_grid(f"Hands-On Activities — {t['phase'].title()}", rows,
                    kicker="WHAT YOU'LL DO", cols=1, size=14, accent=col)
        render_labs(acts, f"DMAIC · {t['phase']}")
    # phase recap
    d.content(f"Recap — {t['phase'].title()}",
              [c[0] + " — " + c[1] for c in t["concepts"]],
              kicker="PHASE RECAP", size=15)

# ============================================================ WRAP-UP
d.section("WRAP-UP", "Course Summary & Next Steps", "")
d.dmaic_wheel("What You Achieved — The Full DMAIC Journey", [
    ("D", "Define", ["Captured VOC and CTQ", "Wrote the problem statement", "Set a SMART goal", "Agreed the scope"]),
    ("M", "Measure", ["Built the SIPOC", "Mapped the process", "Classified the data", "Tallied the 8 wastes"]),
    ("A", "Analyze", ["Ran the 5 Whys", "Built the Fishbone", "Read the Pareto chart", "Shortlisted the causes"]),
    ("I", "Improve", ["Generated countermeasures", "Screened on impact/effort", "Wrote standard work", "Planned the pilot"]),
    ("C", "Control", ["Built the control plan", "Set visual management", "Wrote the SOP", "Handed over"]),
], kicker="YOUR IMPROVEMENT PACKAGE")

d.tile_grid("Your Integrated Improvement Package", [
    ("VOC and CTQ table", "Customer requirements translated into measurable CTQs."),
    ("Problem statement and goal", "A clear problem statement, a SMART goal and an agreed scope."),
    ("SIPOC and process map", "The BrewBean Cafe process as it really runs, with times against each step."),
    ("Waste tally sheet", "Every observed waste tagged to one of the eight DOWNTIME types."),
    ("5 Whys and Fishbone", "A cause chain and a categorised cause diagram for your problem."),
    ("Countermeasure and pilot plan", "One selected countermeasure with standard work and a one-week pilot."),
    ("Control plan and SOP", "Measure, target, frequency, owner, reaction plan and handover."),
    ("One-page summary", "The complete DMAIC story from problem to handover."),
], kicker="WHAT YOU BUILT", cols=2, size=13)

d.tile_grid("Final Readiness Checklist", [
    "Can you define quality, Lean, Six Sigma and Lean Six Sigma in your own words?",
    "Can you name the five DMAIC phases and say what each one delivers?",
    "Can you describe the belt roles and where the White Belt contributes?",
    "Can you trace a VOC statement through to a measurable CTQ?",
    "Can you write a problem statement that contains no solution?",
    "Can you name the eight wastes and give a workplace example of each?",
    "Can you explain the difference between a symptom and a root cause?",
    "Can you run a 5 Whys chain and sort causes on a Fishbone diagram?",
    "Can you describe what a control plan needs to hold a gain?",
], kicker="BEFORE THE ASSESSMENT", cols=1, size=14, accent=TEAL)

d.tile_grid("Continuing Your Lean Six Sigma Journey", [
    ("Apply it at work", "Spot and log the eight wastes in your own area within 30 days."),
    ("Yellow Belt", "The next step — supports DMAIC projects and the data analysis behind them."),
    ("Keep the templates", "Your activity outputs are reusable templates for real improvement work."),
    ("Join the conversation", "Raise improvement ideas in your team; small changes spread by example."),
], kicker="NEXT STEPS", cols=2, size=15, accent=AMBER)

# ============================================================ CLOSE (house order)
# TRAQOM → Certificate → Assessment → Assessment Flow → Digital Attendance → Thank You
d.flow_h("TRAQOM Survey", [
    "Open the TRAQOM survey link on the LMS",
    "Key in the last four characters of your NRIC/FIN",
    "Key in the six-digit course run ID",
    "Complete and submit — your feedback shapes this course",
], kicker="YOUR FEEDBACK", color=TEAL)

d.content("Certificate & Support", [
    "Two e-certificates are awarded on demonstrating competency and achieving at least 75% attendance.",
    "A SkillsFuture Statement of Attainment (SOA) is issued for the WSQ assessment.",
    "Email: enquiry@tertiaryinfotech.com",
    "Tel / WhatsApp: +65 6100 0613",
], kicker="AFTER THE COURSE")

d.big_statement("Final Assessment",
                "Written Assessment (SAQ, 30 minutes) followed by the Case Study (30 minutes). Both are open book.",
                "ASSESSMENT", color=VIOLET)

d.flow_h("Assessment Flow", [
    "TRAQOM survey — scan the QR code on the LMS",
    "Assessment digital attendance — scan the SSG QR",
    "Sit the WA (SAQ), then the Case Study — open book",
    "Submit your answers on the LMS",
    "Sign the Assessment Summary Record",
], kicker="ON ASSESSMENT DAY", color=VIOLET)

d.flow_h("Digital Attendance (Assessment)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR code with your phone camera",
    "Key in your NRIC/FIN and submit",
    "Attendance must be recorded before you begin the papers",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=BLUE)

d.big_statement("Thank You!",
                "Go and spot one waste in your own process this month — that is where every improvement starts.",
                "END OF COURSE", color=BLUE)

# ============================================================ TRANSITIONS + SAVE
d.apply_transitions(kind="fade", dur_ms=700)

out = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
d.prs.save(out)
print(f"✅ {out}")
print(f"   {len(d.prs.slides._sldIdLst)} slides")
