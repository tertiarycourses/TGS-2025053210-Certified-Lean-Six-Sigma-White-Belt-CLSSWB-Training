#!/usr/bin/env python3
"""Lean Six Sigma teaching content — the concept slides, in DMAIC order.

Each function renders the concept slides for one part of the course. Every key
concept is explained VISUALLY (diagram, chart, matrix, timeline) rather than as a
wall of bullets, per the house design standard. Content is grounded in the CSSC
"Six Sigma: A Complete Step-by-Step Guide" and the original v20 trainer deck.
"""
from pptx.util import Inches, Pt
from components import (BLUE, TEAL, AMBER, RED, VIOLET, INK, GREY, LIGHT, WHITE,
                        LINE, DMAIC_COLORS)


# ============================================================ FOUNDATIONS
def foundations(d):
    C = d.C
    d.section("FOUNDATIONS", "Six Sigma Foundations", "00",
              "Quality · Lean · Six Sigma · Lean Six Sigma · Belt roles · The DMAIC roadmap")

    # ---- What is Quality
    d.big_statement("What is Quality?",
                    "Before we can improve quality, we have to agree what the word actually means.",
                    "FOUNDATIONS · QUALITY", color=BLUE)
    d.compare_panels("Three Common Answers — and Why Only One Holds Up", [
        ("Defect-free output", "\"Quality means zero defects\"",
         ["Necessary, but not sufficient.",
          "A product can be flawless and still not sell.",
          "Defect-free against WHOSE standard?"]),
        ("Meeting set standards", "\"Quality means meeting the spec\"",
         ["Better — it is measurable.",
          "But a spec can be set at the wrong level.",
          "Meeting a spec nobody wants is waste."]),
        ("Meeting customer expectations", "\"Quality means the customer is satisfied\"",
         ["This is the Six Sigma definition.",
          "The customer sets the standard.",
          "Everything else follows from this."]),
    ], kicker="WHAT IS QUALITY?", accent=BLUE)

    # ---- What is Lean
    d.big_statement("What is Lean?",
                    "Lean maximises customer value by systematically removing everything the customer would not pay for.",
                    "FOUNDATIONS · LEAN", color=TEAL)
    d.tile_grid("Lean — The Core Idea", [
        ("Origin", "The Toyota Production System — refined in Japanese manufacturing from the 1950s."),
        ("Focus", "Speed and flow: shorten the time from customer request to delivery."),
        ("Enemy", "Waste (muda) — any effort that consumes resources but creates no customer value."),
        ("Method", "See the process, find the waste, remove it, then standardise the improvement."),
        ("Applies to", "Manufacturing AND service — hospitals, banks, IT service desks, government."),
        ("White Belt use", "Recognising waste, understanding process maps and supporting 5S in your own area."),
    ], kicker="WHAT IS LEAN?", cols=2, size=14, accent=TEAL)
    d.flow_h("The Five Lean Principles", [
        "Specify VALUE from the customer's point of view",
        "Map the VALUE STREAM and expose the waste in it",
        "Create FLOW so work moves without interruption",
        "Let the customer PULL work rather than pushing it",
        "Pursue PERFECTION through continuous improvement",
    ], kicker="LEAN · FIVE PRINCIPLES", color=TEAL)

    # ---- What is Six Sigma
    d.big_statement("What is Six Sigma?",
                    "A disciplined, data-driven method to reduce variation and defects — so the process delivers the same result every time.",
                    "FOUNDATIONS · SIX SIGMA", color=VIOLET)
    d.tile_grid("Six Sigma — The Core Idea", [
        ("Origin", "Motorola, 1986 — later made famous by General Electric under Jack Welch."),
        ("Focus", "Consistency: reduce the variation that creates defects."),
        ("Enemy", "Variation — the spread that turns a good average into an unreliable experience."),
        ("Method", "DMAIC, driven by data and statistics rather than opinion."),
        ("The target", "No more than 3.4 defects per million opportunities (DPMO)."),
        ("White Belt use", "Helping collect data and taking part in root cause discussions."),
    ], kicker="WHAT IS SIX SIGMA?", cols=2, size=14, accent=VIOLET)

    # ---- Lean + Six Sigma
    d.vs_diagram("Lean vs Six Sigma vs Lean Six Sigma",
                 ("Lean", ["Removes waste", "Improves speed and flow",
                           "Question: is this step worth doing?", "Tools: VSM, 5S, Kaizen, poka-yoke"]),
                 ("Six Sigma", ["Reduces variation", "Improves consistency and accuracy",
                                "Question: why does the result vary?", "Tools: DMAIC, Pareto, SPC, root cause"]),
                 ("Lean Six Sigma",
                  "Faster AND more consistent — remove the waste, then control the variation that remains."),
                 kicker="THE COMBINED METHOD")

    # ---- Belt roles
    d.ladder("The Lean Six Sigma Belt Pathway", [
        ("White Belt", "Awareness of Six Sigma; supports local problem solving"),
        ("Yellow Belt", "Knows the basic tools; supports projects and runs small improvements"),
        ("Green Belt", "Leads smaller projects; assists Black Belts with analysis"),
        ("Black Belt", "Leads complex projects full time; coaches Green and Yellow Belts"),
        ("Master Black Belt", "Trains and mentors Belts; owns deployment strategy"),
    ], kicker="WHO DOES WHAT", accent=BLUE,
        note="This course certifies you at White Belt — awareness of Lean Six Sigma and support for local problem solving.")

    # ---- DMAIC roadmap
    d.dmaic_wheel("The DMAIC Roadmap", [
        ("D", "Define", ["Define the problem", "Capture VOC and CTQ", "Charter and scope", "Map with SIPOC"]),
        ("M", "Measure", ["Plan data collection", "Measure the baseline", "Calculate yield/DPMO", "Find the waste"]),
        ("A", "Analyze", ["Analyse the data", "Pareto analysis", "5 Whys and Fishbone", "Find the root cause"]),
        ("I", "Improve", ["Generate solutions", "Select and pilot", "5S and poka-yoke", "Standardise the work"]),
        ("C", "Control", ["Build the control plan", "Visual management", "Hand over to the owner", "Sustain the gain"]),
    ], kicker="THE COURSE ROADMAP · WE FOLLOW THIS ORDER")


# ============================================================ DEFINE
def define_phase(d):
    d.big_statement("Define — What problem are we solving, and for whom?",
                    "The Define phase converts a vague complaint into a scoped, measurable problem statement everyone agrees on.",
                    "DMAIC · D — DEFINE", color=DMAIC_COLORS[0])
    d.flow_h("Steps in the Define Phase", [
        "Capture the Voice of the Customer",
        "Translate VOC into CTQ requirements",
        "Write the problem and goal statements",
        "Charter and scope the project",
        "Map the process with SIPOC",
    ], kicker="DEFINE · ROADMAP", color=DMAIC_COLORS[0])

    # VOC
    d.big_statement("Voice of the Customer (VOC)",
                    "The needs and expectations of the customer, expressed in the customer's own language.",
                    "DEFINE · VOC", color=BLUE)
    d.tile_grid("Where VOC Comes From", [
        ("Surveys", "Structured and at scale, but limited to the questions you thought to ask."),
        ("Interviews", "Rich and open-ended; best for understanding the 'why' behind a complaint."),
        ("Complaints & reviews", "Already coming in unprompted — the cheapest and most honest VOC source."),
        ("Direct observation", "Go and watch the work happen; customers cannot always articulate the problem."),
    ], kicker="SOURCES OF VOC", cols=2, size=15)
    d.two_col("VOC → Need → CTQ: The Translation",
              [("The customer says (VOC)", 0),
               ("\"I don't want to wait too long\"", 1),
               ("\"I don't want cold pizza\"", 1),
               ("\"I never know how long the wait will be\"", 1),
               ("Vague, emotional, unmeasurable", 1)],
              [("The measurable requirement (CTQ)", 0),
               ("Delivery in 30 minutes or less", 1),
               ("Pizza at 32°C minimum on arrival", 1),
               ("Wait time displayed, 5 minutes or less", 1),
               ("Specific, numeric, testable", 1)],
              kicker="THE CTQ TRANSLATION", lhead="Voice of the Customer", rhead="Critical to Quality",
              lcolor=AMBER, rcolor=TEAL)
    d.tile_grid("What Makes a Good CTQ?", [
        ("Specific", "Names exactly one characteristic of the output."),
        ("Measurable", "Has a number and a unit you can actually record."),
        ("Linked to VOC", "Traces back to something a customer genuinely said."),
        ("Has a target and limit", "States the target value and the acceptable range around it."),
    ], kicker="CTQ QUALITY CHECK", cols=2, size=15, accent=TEAL)

    # Charter
    d.tile_grid("The Project Charter", [
        ("Business case", "Why this project matters and what it is worth."),
        ("Problem statement", "What is wrong, quantified, over a stated time period."),
        ("Goal statement", "Metric, baseline, target and date."),
        ("Scope", "What is in, and explicitly what is out."),
        ("Team and roles", "Sponsor, project leader, White and Yellow Belt support, and subject matter experts."),
        ("Milestones", "The dates each DMAIC phase is expected to complete."),
    ], kicker="DEFINE · THE PROJECT'S CONTRACT", cols=2, size=14)
    d.two_col("Problem Statements — Good vs Bad",
              [("Weak problem statement", 0),
               ("\"The morning queue is too slow.\"", 1),
               ("No process named", 1),
               ("No time period", 1),
               ("No measure or baseline", 1),
               ("No customer impact stated", 1),
               ("Hints at a solution (\"we need more staff\")", 1)],
              [("Strong problem statement", 0),
               ("\"Between 1 and 31 March, customers served between 7:30am and 9:00am waited an average of 11.5 minutes against a 5-minute target, affecting 38% of morning customers and generating 24 online complaints.\"", 1),
               ("Process, period, measure, baseline and impact — and no solution.", 1)],
              kicker="WRITING THE PROBLEM STATEMENT", lhead="Avoid this", rhead="Aim for this",
              lcolor=RED, rcolor=TEAL)

    # SIPOC + process mapping
    d.big_statement("SIPOC — the macro 'as-is' map",
                    "One page that shows who supplies the process, what goes in, what happens, what comes out, and who receives it.",
                    "DEFINE · SIPOC", color=TEAL)
    d.sipoc_diagram("SIPOC — BrewBean Cafe Morning Rush", [
        ["Coffee bean supplier", "Dairy supplier", "Cup and lid supplier", "Barista team"],
        ["Order details", "Coffee beans", "Milk", "Cups and lids", "Payment"],
        ["1. Customer joins queue", "2. Order taken", "3. Payment made", "4. Drink prepared", "5. Drink handed over"],
        ["Prepared drink", "Receipt", "Order called out"],
        ["Walk-in customer", "Regular customer", "Office group orders"],
    ], kicker="DEFINE · WORKED EXAMPLE")


# ============================================================ MEASURE
def measure_phase(d):
    d.big_statement("Measure — How big is the problem, really?",
                    "The Measure phase replaces opinion with a trustworthy baseline you can improve against.",
                    "DMAIC · M — MEASURE", color=DMAIC_COLORS[1])
    d.flow_h("Steps in the Measure Phase", [
        "Identify the waste in the current process",
        "Decide what to measure and define it precisely",
        "Build the data collection plan and check sheet",
        "Collect the baseline data",
        "Calculate yield, DPMO and sigma level",
    ], kicker="MEASURE · ROADMAP", color=DMAIC_COLORS[1])

    # Waste
    d.big_statement("What is Waste?",
                    "Anything beyond the minimum information, equipment, material and effort absolutely required to add value for the customer.",
                    "MEASURE · WASTE (MUDA)", color=RED)
    d.waste_wheel("The Eight Wastes of Lean — DOWNTIME", [
        ("D", "Defects"), ("O", "Overproduction"), ("W", "Waiting"), ("N", "Non-utilised talent"),
        ("T", "Transport"), ("I", "Inventory"), ("M", "Motion"), ("E", "Extra-processing"),
    ], kicker="MEASURE · THE 8 WASTES")
    d.tile_grid("The Eight Wastes in a Service Process", [
        ("D — Defects", "A drink made wrong and remade; the wrong order handed over."),
        ("O — Overproduction", "Brewing more coffee at 8am than customers actually order, then pouring it away."),
        ("W — Waiting", "Customers standing in the queue; a drink waiting on the counter to be called out."),
        ("N — Non-utilised talent", "An experienced barista tied to the till instead of making drinks at peak."),
        ("T — Transport", "Carrying milk from the back store to the counter several times each morning."),
        ("I — Inventory", "A growing line of unmade orders on the rail during the rush."),
        ("M — Motion", "The barista walking back and forth because cups and lids are stored apart."),
        ("E — Extra-processing", "Writing the order on a cup and then re-keying it into the till."),
    ], kicker="DOWNTIME IN PRACTICE", cols=2, size=13, accent=RED)
    d.compare_panels("Value-Added vs Non-Value-Added", [
        ("Value-added (VA)", "The customer would pay for it",
         ["Changes the product or service.",
          "Done right the first time.",
          "The customer cares that it happened.",
          "Example: actually making the coffee."]),
        ("Business-value-added (BVA)", "Required, but not by the customer",
         ["Needed for legal or regulatory reasons.",
          "Required to run the business.",
          "Minimise it — you cannot remove it.",
          "Example: recording the sale for tax purposes."]),
        ("Non-value-added (NVA)", "Pure waste — remove it",
         ["Consumes time and resource for nothing.",
          "The customer would never pay for it.",
          "Attack this first.",
          "Example: a customer waiting in the queue."]),
    ], kicker="MEASURE · VALUE ANALYSIS", accent=TEAL)

    # Data types
    d.compare_panels("Types of Data — and Why It Matters", [
        ("Continuous data", "Measured on a scale",
         ["Any value within a range.",
          "Time, cost, temperature, length.",
          "More information per data point.",
          "Needs a smaller sample size."]),
        ("Discrete / attribute data", "Counted in whole units",
         ["Counts and categories only.",
          "Number of defects, pass/fail.",
          "Less information per data point.",
          "Needs a much larger sample."]),
    ], kicker="MEASURE · DATA TYPES", accent=BLUE)

    # Data collection
    d.tile_grid("The Data Collection Plan", [
        ("What", "Which metric, and what exactly counts as one observation."),
        ("Why", "Which CTQ or problem statement this metric supports."),
        ("How", "Automated report preferred; manual capture only when unavoidable."),
        ("Who", "Someone who knows the process and is available to do it consistently."),
        ("When", "The frequency and the exact period the data covers."),
        ("How many", "The sample size — enough to be representative, not so many it is unaffordable."),
    ], kicker="MEASURE · PLANNING THE DATA", cols=2, size=14, accent=TEAL)
    d.tile_grid("Check Sheets — the Simplest Reliable Tool", [
        ("One row per observation", "Never summarise as you collect — record the raw event."),
        ("Pre-printed categories", "Tick a box rather than writing free text; free text cannot be counted."),
        ("Mutually exclusive", "Every observation must fall into exactly one category."),
        ("Include the context", "Date, time, shift and who recorded it — you will need this later."),
    ], kicker="MEASURE · CHECK SHEETS", cols=2, size=15, accent=TEAL)

    # Process metrics


# ============================================================ ANALYZE
def analyze_phase(d):
    d.big_statement("Analyze — Why is this happening?",
                    "The Analyze phase moves the team from a measured symptom to a proven, actionable root cause.",
                    "DMAIC · A — ANALYZE", color=DMAIC_COLORS[2])
    d.flow_h("Steps in the Analyze Phase", [
        "Study the data and the process map",
        "Generate a list of potential causes (Xs)",
        "Organise the causes with a Fishbone diagram",
        "Drill down with the 5 Whys",
        "Test each candidate cause against the evidence",
    ], kicker="ANALYZE · ROADMAP", color=DMAIC_COLORS[2])

    # Variation
    d.compare_panels("Two Kinds of Variation — and Two Different Responses", [
        ("Common cause", "Built into the process",
         ["Always present, random, predictable range.",
          "The process is stable but imperfect.",
          "Response: change the PROCESS.",
          "Reacting to individual points makes it worse."]),
        ("Special cause", "An external, assignable signal",
         ["Unusual, traceable to a specific event.",
          "Something changed that should not have.",
          "Response: investigate THAT event.",
          "Fix the cause, then remove it for good."]),
    ], kicker="ANALYZE · UNDERSTANDING VARIATION", accent=AMBER)

    # Pareto
    d.big_statement("The Pareto Principle — the 80/20 rule",
                    "Roughly 80% of the effects come from 20% of the causes. Find that 20% and you get most of the improvement for a fraction of the effort.",
                    "ANALYZE · PARETO", color=AMBER)
    d.pareto_chart("Pareto Chart — Causes of Delay at the BrewBean Cafe", [
        ("One till at\npeak hour", 210),
        ("Milk fetched\nfrom back store", 155),
        ("Order re-keyed\ninto till", 95),
        ("Card machine\nslow", 48),
        ("Drink remade\n(wrong order)", 30),
        ("Other", 12),
    ], kicker="ANALYZE · WORKED EXAMPLE",
        note="Two causes — a single till at peak hour and milk fetched from the back store — account for about 66% of all delay. Start there.")


    # Root cause
    d.big_statement("What is a root cause?",
                    "The deepest cause in the chain that you can actually act on — remove it, and the problem does not come back.",
                    "ANALYZE · ROOT CAUSE", color=VIOLET)
    d.tile_grid("The 5 Whys Technique", [
        ("Start with the problem", "State the effect precisely, using the data you measured."),
        ("Ask why — and answer with evidence", "Each answer must be something you can point to, not a guess."),
        ("Repeat about five times", "Five is a guide, not a rule — stop when you reach an actionable cause."),
        ("Watch for blame", "If an answer names a person rather than a process, ask why again."),
        ("Stop at actionable", "The root cause must be something within the team's power to change."),
        ("Verify with data", "Test the final cause against the evidence before acting on it."),
    ], kicker="ANALYZE · 5 WHYS", cols=2, size=14, accent=VIOLET)
    d.flow_h("5 Whys — Worked Example: The BrewBean Morning Queue", [
        "PROBLEM: Customers wait 11.5 minutes at 8am vs a 5-minute target",
        "WHY? Drinks are not made fast enough to clear the queue",
        "WHY? The barista keeps stopping mid-order",
        "WHY? Milk runs out at the counter and must be fetched from the back store",
        "ROOT CAUSE: No one restocks counter milk before the 7:30am rush begins",
    ], kicker="ANALYZE · 5 WHYS IN ACTION", color=VIOLET)
    d.fishbone("Fishbone (Ishikawa) — The Morning Queue Is Too Slow",
               "Morning\nqueue is\ntoo slow", [
                   ("Manpower", ["One till at peak", "No cover for breaks", "New staff untrained"]),
                   ("Method", ["No restocking routine", "Order re-keyed into till", "No queue policy"]),
                   ("Machine", ["Card machine slow", "One grinder only", "Till screen confusing"]),
                   ("Material", ["Milk stored at the back", "Cups and lids kept apart", "Beans not pre-ground"]),
                   ("Measurement", ["Wait time not tracked", "No target agreed", "Complaints not logged"]),
               ], kicker="ANALYZE · CAUSE AND EFFECT · THE 5Ms")


# ============================================================ IMPROVE
def improve_phase(d):
    d.big_statement("Improve — What change will actually fix it?",
                    "The Improve phase generates, selects and pilots solutions that address the proven root cause.",
                    "DMAIC · I — IMPROVE", color=DMAIC_COLORS[3])
    d.flow_h("Steps in the Improve Phase", [
        "Generate candidate solutions against the root cause",
        "Select using weighted criteria",
        "Pilot the change at small scale",
        "Measure whether the metric actually moved",
        "Standardise the new method",
    ], kicker="IMPROVE · ROADMAP", color=DMAIC_COLORS[3])
    d.tile_grid("Generating Solutions", [
        ("Brainstorming", "Free generation against the specific root cause — not the general problem."),
        ("Brainwriting", "Written idea generation; avoids the loudest voice dominating the room."),
        ("Benchmarking", "Find who already does this well, internally or externally, and learn from them."),
        ("Anti-brainstorming", "Ask how to make the problem worse, then invert every answer."),
    ], kicker="IMPROVE · IDEA GENERATION", cols=2, size=15)
    d.matrix2x2("Prioritising Countermeasures — Impact vs Effort",
                "EFFORT REQUIRED  →", "IMPACT  →", [
                    ("Quick wins", "High impact, low effort. Do these first — they build momentum and credibility."),
                    ("Major projects", "High impact, high effort. Worth doing, but plan and resource them properly."),
                    ("Fill-ins", "Low impact, low effort. Do them if there is spare capacity."),
                    ("Thankless tasks", "Low impact, high effort. Avoid these entirely."),
                ], kicker="IMPROVE · PRIORITISATION", accent=TEAL)
    d.flow_h("5S — Organising the Workplace", [
        "SORT — remove what is not needed",
        "SET IN ORDER — a place for everything",
        "SHINE — clean and inspect regularly",
        "STANDARDISE — make the first 3S the norm",
        "SUSTAIN — audit and keep the discipline",
    ], kicker="IMPROVE · 5S", color=TEAL)
    d.big_statement("Poka-Yoke — mistake proofing",
                    "Design the process so the error is difficult or impossible to make — rather than relying on people to be careful.",
                    "IMPROVE · POKA-YOKE", color=VIOLET)
    d.tile_grid("Standard Work", [
        ("What it is", "The documented, current best-known way to perform the task."),
        ("Why it matters", "You cannot improve a process that everyone performs differently."),
        ("What it contains", "The sequence, the time each step takes and the quality checks."),
        ("Who writes it", "The people who do the work — not a manager writing in isolation."),
        ("Keep it living", "Update it every time a better method is proven."),
        ("The Lean insight", "Standard work is the baseline for the NEXT improvement, not a straitjacket."),
    ], kicker="IMPROVE · STANDARD WORK", cols=2, size=14)
    d.tile_grid("Piloting Before Full Rollout", [
        ("Why pilot", "Exposes practical issues cheaply, before they affect every customer."),
        ("Keep it small", "One shift, one counter or one drink type is usually enough."),
        ("Measure the same way", "Use the identical operational definition as your baseline, or you cannot compare."),
        ("Run it long enough", "Cover a full business cycle so you see normal variation."),
        ("Decide honestly", "Adopt, adapt or abandon — a failed pilot that saves a bad rollout is a success."),
        ("Then standardise", "Only after the pilot proves the gain do you write it into standard work."),
    ], kicker="IMPROVE · PILOTING", cols=2, size=14, accent=BLUE)


# ============================================================ CONTROL
def control_phase(d):
    d.big_statement("Control — How do we make the gain stick?",
                    "Without the Control phase, processes drift back to the old way within months and the whole project is wasted.",
                    "DMAIC · C — CONTROL", color=DMAIC_COLORS[4])
    d.flow_h("Steps in the Control Phase", [
        "Build the control plan",
        "Set up monitoring and visual management",
        "Document the SOP and standard work",
        "Hand over to the process owner",
        "Close the project and share the learning",
    ], kicker="CONTROL · ROADMAP", color=DMAIC_COLORS[4])
    d.tile_grid("The Control Plan — Six Required Columns", [
        ("Metric", "What is being monitored — the same operational definition as the baseline."),
        ("Target", "The agreed acceptable value or range."),
        ("Method", "How the measurement is taken — report, dashboard, sample or audit."),
        ("Frequency", "How often it is checked: per shift, daily, weekly."),
        ("Owner", "The named person accountable — a role, never 'the team'."),
        ("Reaction plan", "Exactly what happens when the metric falls outside target."),
    ], kicker="CONTROL · THE CONTROL PLAN", cols=2, size=14, accent=BLUE)
    d.tile_grid("Visual Management", [
        ("Visual boards", "Display the metric, the target and the current status where the team works."),
        ("Make it obvious", "Anyone should see whether performance is on target within a few seconds."),
        ("Team huddles", "A short daily stand-up at the board — 15 minutes maximum."),
        ("Drives ownership", "When performance is visible, the team owns it rather than the manager."),
        ("Surfaces issues early", "Problems are raised while they are still small and cheap to fix."),
        ("Keep it current", "An out-of-date board is worse than no board — it teaches people to ignore it."),
    ], kicker="CONTROL · MAKING IT VISIBLE", cols=2, size=14, accent=TEAL)
    d.tile_grid("Standard Operating Procedures (SOPs)", [
        ("Written instructions", "Describe how to perform the task to achieve the required result."),
        ("Include the measures", "State the benchmarks and quality checks, not only the steps."),
        ("Centrally accessible", "Held in one agreed place everyone can reach and search."),
        ("Version controlled", "It must be obvious which version is current."),
    ], kicker="CONTROL · SOPs", cols=2, size=15)
    d.flow_h("Project Handover and Closure", [
        "Confirm the improvement held for a full cycle",
        "Hand the control plan to the named process owner",
        "Train everyone on the new standard work",
        "Document the financial or service benefit",
        "Share the learning so others can reuse it",
    ], kicker="CONTROL · CLOSING THE PROJECT", color=DMAIC_COLORS[4])
