"""
SINGLE SOURCE OF TRUTH — Certified Lean Six Sigma White Belt (CLSSWB) Training.

This is a ONE-DAY Six Sigma AWARENESS course. It is deliberately simplified from
the two-day Yellow Belt (TGS-2025053922): the same DMAIC storyline and the same
house visual system, but every phase is taught at awareness depth — what the
tool is, why it matters, and how to read one — rather than at practitioner depth.

Simplification rules applied against the Yellow Belt:
  * 5 labs, exactly one per DMAIC phase (Yellow Belt has 14).
  * No sigma-level maths, no DPMO conversion tables, no MSA, no FMEA, no VSM,
    no Kano, no solution-selection matrices, no descriptive statistics.
  * Learners CONTRIBUTE to an improvement team; they do not lead a project.
  * Concepts are explained with plain-language definitions and one worked
    example each, using a single running scenario the whole day.

Content is grounded in:
  * "WSQ - Dr. Alfred Ang - Certified Lean Six Sigma White Belt (CLSSWB) - v3.pptx"
    (the 117-slide original trainer deck — see reference/)
  * "Six Sigma: A Complete Step-by-Step Guide" — The Council for Six Sigma
    Certification (CSSC), which defines the White Belt awareness standard.

Every artifact (PPT, LP, LG, LG.md, labs index) is generated from this module +
data_domainN.py so they stay 100% aligned.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Certified Lean Six Sigma White Belt (CLSSWB) Training"
SHORT_TITLE  = "Certified Lean Six Sigma White Belt (CLSSWB) Training"
COURSE_CODE  = "TGS-2025053210"
VERSION      = "v6"
VERSION_DATE = "23 September 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1

# ------------------------------------------------------------------ TSC alignment (WSQ)
TSC_TITLE = "Quality Process Control"
TSC_CODE  = "ELE-QUA-5006-1.1"
TSC_ABILITIES = [
    "A1: Support the definition of an improvement project to meet process performance.",
    "A2: Assist in establishing the scope of work based on organisational requirements.",
    "A3: Assist in analysing process performance data to identify causes of variation.",
    "A4: Support the measurement of process performance against defined quality standards.",
    "A5: Support improvement and control actions that sustain process performance.",
]
TSC_KNOWLEDGE = [
    "K1: Basic Lean and Six Sigma concepts — quality, value, waste and variation.",
    "K2: Basic quality tools used at each phase of the DMAIC roadmap.",
]

# ------------------------------------------------------------------ outcomes
# Awareness-level verbs (describe / identify / explain / contribute) — NOT the
# practitioner verbs used at Yellow Belt (define / analyse / recommend).
LEARNING_OUTCOMES = [
    "LO1: Describe the core concepts of quality, Lean, Six Sigma and Lean Six Sigma, and the belt roles in an improvement team.",
    "LO2: Explain the five phases of the DMAIC roadmap and what happens in each.",
    "LO3: Identify customer requirements and a clear problem statement in the Define phase.",
    "LO4: Describe how a process is mapped and measured, and identify the eight wastes in the Measure phase.",
    "LO5: Identify likely causes of a problem using 5 Whys and Fishbone analysis in the Analyze phase.",
    "LO6: Describe common improvement and control actions that fix a cause and hold the gain.",
]

# ------------------------------------------------------------------ topics
# One topic per DMAIC phase, plus Foundations. Exactly one activity per DMAIC phase.
TOPICS = [
    dict(num=0, code="00", phase="FOUNDATIONS",
         title="Lean Six Sigma Foundations",
         subtitle="Quality · Lean · Six Sigma · Lean Six Sigma · Belt roles · The DMAIC roadmap",
         weighting="20%",
         concepts=[
            ("What is Quality", "Quality is meeting the customer's requirements — not just being free of defects."),
            ("What is Lean", "Lean removes waste so work flows faster to the customer."),
            ("What is Six Sigma", "Six Sigma reduces variation so results become consistent and predictable."),
            ("Lean Six Sigma", "The two combined: faster flow AND fewer defects, decided by data not opinion."),
            ("Belt roles", "White, Yellow, Green, Black and Master Black Belt — who does what on a team."),
            ("The DMAIC roadmap", "Define, Measure, Analyze, Improve, Control — the five-step improvement path."),
         ]),
    dict(num=1, code="D", phase="DEFINE",
         title="Define — Understand the Problem",
         subtitle="Voice of the Customer · CTQ · Problem statement · SMART goal · Project charter",
         weighting="20%",
         concepts=[
            ("Voice of the Customer", "Ask customers what they need, and record it in their own words."),
            ("Critical to Quality", "Turn each customer need into something specific you can measure."),
            ("Problem statement", "What is wrong, where, since when, and how big — never the solution."),
            ("SMART goal", "Specific, Measurable, Achievable, Relevant and Time-bound."),
            ("Project charter", "A one-page summary of the problem, goal, scope and team."),
            ("Scope", "Agreeing what is in and out keeps a small project small."),
         ]),
    dict(num=2, code="M", phase="MEASURE",
         title="Measure — See What Is Really Happening",
         subtitle="Process mapping · SIPOC · Types of data · Data collection · The eight wastes",
         weighting="20%",
         concepts=[
            ("Process mapping", "Draw the steps as they really happen, not as the manual says."),
            ("SIPOC", "A one-page overview: Suppliers, Inputs, Process, Outputs, Customers."),
            ("Types of data", "Discrete data you count; continuous data you measure on a scale."),
            ("Data collection", "Agree what to record, who records it, and when — before you start."),
            ("Check sheets", "A simple tally form is the easiest reliable way to collect data."),
            ("The eight wastes", "DOWNTIME — Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra-processing."),
         ]),
    dict(num=3, code="A", phase="ANALYZE",
         title="Analyze — Find the Cause",
         subtitle="Root cause · 5 Whys · Fishbone diagram · Pareto chart · Variation",
         weighting="20%",
         concepts=[
            ("Symptom vs cause", "Treating the symptom makes the problem come back; treating the cause does not."),
            ("Root cause", "The cause that, once removed, stops the problem recurring."),
            ("5 Whys", "Keep asking 'why?' until you reach something you can actually act on."),
            ("Fishbone diagram", "Sort possible causes into Manpower, Method, Machine, Material and Measurement."),
            ("Pareto chart", "Roughly 80% of the problem usually comes from 20% of the causes."),
            ("Variation", "Some variation is normal in the process; some has a specific assignable cause."),
         ]),
    dict(num=4, code="I", phase="IMPROVE",
         title="Improve — Fix the Cause",
         subtitle="Generating solutions · 5S · Mistake proofing · Standard work · Piloting",
         weighting="10%",
         concepts=[
            ("Generating solutions", "Brainstorm against the proven cause — never against the symptom."),
            ("Choosing a solution", "Compare ideas on impact, effort and risk before committing."),
            ("5S", "Sort, Set in order, Shine, Standardise, Sustain — a tidy workplace for physical or digital work."),
            ("Mistake proofing", "Poka-Yoke makes the error hard or impossible to make."),
            ("Standard work", "Write the better method down so everyone does it the same way."),
            ("Piloting", "Try the change small first, so mistakes stay cheap."),
         ]),
    dict(num=5, code="C", phase="CONTROL",
         title="Control — Hold the Gain",
         subtitle="Control plan · Visual management · SOPs · Team huddles · Handover",
         weighting="10%",
         concepts=[
            ("Why Control matters", "Without Control, processes quietly drift back to the old way."),
            ("Control plan", "What we measure, the target, how often, who owns it, and what to do if it slips."),
            ("Visual management", "Make performance visible so problems are noticed the same day."),
            ("Standard operating procedures", "Written instructions that lock in the improved method."),
            ("Team huddles", "Short regular stand-ups catch problems while they are still small."),
            ("Handover", "Give the improved process back to the people who run it every day."),
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours)
DAY_THEMES = {
    1: "Lean Six Sigma foundations and the full DMAIC roadmap, with assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 30 minutes, open book.",
    practical="Case Study (CS) — applied Lean Six Sigma scenario tasks, 30 minutes, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
