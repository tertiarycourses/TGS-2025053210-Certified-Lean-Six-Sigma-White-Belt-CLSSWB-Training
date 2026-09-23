"""Detailed step-by-step facilitation data for the five in-class DMAIC activities.

Each entry is keyed by activity number (1..5) and provides:
  timing     -- (minutes, phase) pairs that sum to the activity duration (30 min)
  artefact   -- what the group physically produces
  steps      -- ordered (heading, instruction) pairs; the actual "do this next"
  checklist  -- self-check items learners tick before the debrief
  tips       -- facilitator notes: what to watch for, common wrong turns

The instruction text is the authoritative long-form of the step; the short form
in data_domainN.py drives the slides and the labs README. Both run on the same
continuous BrewBean Cafe scenario, and every activity works from the mock data
in the activity's own data/ folder (see lab_data.py).
"""

STEPS = {

# ================================================================= DEFINE
1: dict(
    timing=[(4, "Read the scenario and the 30 pieces of customer feedback"),
            (9, "Extract VOC statements and convert each to a measurable CTQ"),
            (8, "Draft the problem statement and test it against SMART"),
            (5, "Agree what is in and out of scope"),
            (4, "Prepare the debrief line")],
    artefact="A VOC-to-CTQ table with five measurable requirements, a written problem "
             "statement containing no solution, a SMART goal, and an in/out scope table.",
    steps=[
        ("Read the scenario and the raw feedback",
         "Open data/voc-raw-customer-feedback.csv (or the Excel workbook) and read all 30 "
         "pieces of customer feedback — online reviews, comment cards and counter remarks. "
         "Underline every complaint you can find. Read before you write: the most common "
         "reason improvement projects fail is that the team decided what the problem was "
         "before looking at the evidence."),
        ("Capture five VOC statements in the customer's own words",
         "Using templates/voc-to-ctq-template.csv, write down five Voice of the Customer "
         "statements quoted from the Verbatim Comment column. Keep the customer's own "
         "words — 'I'm late for work because the queue is too slow', not 'customers desire "
         "improved service efficiency'. The translation happens in the next step, not here."),
        ("Turn each VOC into a measurable CTQ",
         "For each VOC statement, write what the customer actually needs, then a Critical "
         "to Quality requirement that carries BOTH a number AND a unit — 'served within 5 "
         "minutes', not 'served faster'. If you cannot put a number on it, you cannot tell "
         "later whether you fixed it."),
        ("Write the problem statement",
         "In templates/problem-statement-and-scope-template.csv, fill the four components: "
         "what is wrong, where and when it happens, since when, and how big it is — then "
         "the impact on the business. Write NO solution. 'Because we need to open a second "
         "till' is a solution and invalidates the statement."),
        ("Test the goal against SMART",
         "Rewrite your goal so it is Specific, Measurable, Achievable, Relevant and "
         "Time-bound. A complete goal names a metric, a baseline, a target and a date. "
         "Note the difference from the problem statement: the problem is what is wrong "
         "TODAY; the goal is what will be true at the END."),
        ("Agree the scope",
         "Fill the in-scope / out-of-scope rows so the team knows where the project stops. "
         "Test each item with: could a White Belt team finish that in six weeks? Anything "
         "needing capital spend or a supplier renegotiation goes out of scope."),
        ("Prepare the debrief line",
         "Agree one sentence: \"Our problem statement passes because it says ____, and it "
         "contains no solution.\" Nominate a spokesperson to read it out."),
    ],
    checklist=[
        "Five VOC statements are recorded in the customer's own words, quoted from the data.",
        "Every CTQ carries both a number and a unit.",
        "The problem statement names what, where/when, since when, how big and the impact.",
        "The problem statement contains NO solution.",
        "The SMART goal has a metric, a baseline, a target and a date.",
        "The scope table has entries in BOTH the in-scope and out-of-scope columns.",
    ],
    tips=[
        "Watch for learners paraphrasing the VOC into business language — stop them. VOC "
        "stays in the customer's own words; the translation belongs in the CTQ column.",
        "Push back on any CTQ written without a unit ('serve faster'). Ask: how would you "
        "know next month whether this improved?",
        "A problem statement that smuggles in a solution is the single most common White "
        "Belt error, and Case Study Q1 tests it directly. Read a few aloud and let the room "
        "spot the hidden solutions.",
        "If a table puts everything in scope, ask whether they could finish it in six weeks.",
    ]),

# ================================================================= MEASURE
2: dict(
    timing=[(5, "Agree the process boundaries and complete the SIPOC"),
            (9, "Build the process map and judge each step value-adding or not"),
            (4, "Classify the data as discrete or continuous"),
            (8, "Complete the DOWNTIME waste tally from the evidence"),
            (4, "Write down the baseline figures")],
    artefact="A completed SIPOC, a 15-step process map with each step judged VA or NVA, a "
             "completed DOWNTIME waste tally, and the written baseline figures.",
    steps=[
        ("Agree the start and stop points",
         "Fix the boundaries before anything else: start when the customer joins the queue, "
         "stop when the customer receives the drink. A process with no agreed boundaries "
         "produces a map nobody can compare against anything."),
        ("Complete the SIPOC",
         "Fill templates/sipoc-template.csv: Suppliers, Inputs, Process, Outputs, "
         "Customers. Hold the Process column to 5-7 high-level steps — the detail belongs "
         "in the process map, not here. A SIPOC is the one-page view a manager can read in "
         "thirty seconds."),
        ("Build the process map with real timings",
         "Open data/process-step-timings.csv — the 15 observed steps with their average "
         "times. Copy them into templates/process-map-template.csv. Note the 'Times Step "
         "Was Skipped' column: step 10 (fetching milk) happened for 18 of 60 customers and "
         "step 15 (remaking a drink) for 7 of 60."),
        ("Judge every step value-adding or not",
         "Mark each step VA or NVA and write one line saying why. The test is applied per "
         "STEP: would the customer pay extra for THIS step? Not 'does the customer want "
         "coffee'. Expect to find that the great majority of the elapsed time is "
         "non-value-adding — that is the normal and useful finding."),
        ("Classify the data you have",
         "Look at the columns in data/morning-rush-observation-log.csv. Which figures are "
         "discrete (counted — remakes, tallies) and which are continuous (measured on a "
         "scale — wait time in minutes)? Note that 'Drink Ordered' and 'Delay Reason' are "
         "neither: they are categorical labels."),
        ("Complete the DOWNTIME waste tally",
         "Open data/downtime-waste-tally.csv — three rows are completed as worked examples. "
         "Using the observation log and the step timings as your EVIDENCE, complete the "
         "remaining five rows in templates/downtime-tally-template.csv. Some waste types "
         "may legitimately be zero here; recording zero with evidence is a correct answer."),
        ("Write down the baseline",
         "Record the average wait, the longest wait, the percentage of customers over the "
         "5-minute promise, and the number of drinks remade. Identify which single waste "
         "type you tallied most often and at which step. Lab 5 measures the improvement "
         "against these numbers, and the Case Study expects a baseline to be quoted rather "
         "than invented."),
    ],
    checklist=[
        "The SIPOC has all five columns filled and the Process column holds 5-7 steps only.",
        "Every process step on the map carries an observed time.",
        "Every step is marked VA or NVA with a one-line justification.",
        "Each data column is correctly classified as discrete, continuous or categorical.",
        "All eight DOWNTIME rows are complete, each tagged to a process step and a count.",
        "The baseline figures are written down: average wait, longest wait, % over promise, remakes.",
    ],
    tips=[
        "Hold the line at 5-7 steps in the SIPOC Process column. Tables will want to list "
        "all fifteen; that is the process map's job.",
        "Watch for learners marking the whole process value-adding because 'the customer "
        "wants coffee'. Re-apply the test to each individual step.",
        "'Drink Ordered' is categorical, not continuous. Steer them to the two types the "
        "course teaches and note that a label is neither.",
        "Some tables tally waste from memory. Point them back to the data — the tally must "
        "be evidence, not impression.",
        "Park any 'hire more staff' suggestions. Solutions are Lab 4; this phase is facts.",
    ]),

# ================================================================= ANALYZE
3: dict(
    timing=[(9, "Build the 5 Whys chain down to an actionable cause"),
            (8, "Spread the causes across the Fishbone categories"),
            (5, "Read the Pareto and name the vital few"),
            (4, "Separate common cause from special cause"),
            (4, "Shortlist the causes backed by evidence")],
    artefact="A completed 5 Whys chain ending in an actionable cause, a Fishbone diagram "
             "with causes sorted into the five categories, and a shortlist of two or three "
             "root causes each backed by evidence.",
    steps=[
        ("State the symptom",
         "Write the symptom from your Lab 2 baseline at the top of "
         "templates/5-whys-template.csv — for example 'customers wait an average of 8.9 "
         "minutes against a 5-minute promise'. Start from the measured symptom, not from a "
         "theory about the cause."),
        ("Drill down with 5 Whys",
         "Ask 'why does that happen?' down the template, each answer becoming the next "
         "question. Stop when you reach a PROCESS the team can act on. Two rules: never "
         "stop at a person ('the barista is slow' is not a root cause — ask why), and do "
         "not stop early just because an answer sounds plausible."),
        ("Set up the Fishbone",
         "Open templates/fishbone-template.csv and write the problem in the head of the "
         "fish. The 5 Whys drills DOWN one chain; the Fishbone spreads WIDE so no whole "
         "area of cause is missed. Used together they are stronger than either alone."),
        ("Populate the five bones",
         "Brainstorm possible causes onto Manpower, Method, Machine, Material and "
         "Measurement. Then check them against data/cause-evidence-sheet.csv to see which "
         "ones the data actually supports — some entries there are pure opinion, and "
         "telling them apart is the point."),
        ("Read the Pareto",
         "Open data/delay-reason-pareto-data.csv — the delay reasons from your Lab 2 log, "
         "counted and ranked. Read the Cumulative % column and state which few causes "
         "account for most of the problem. Remember the Pareto ranks FREQUENCY, which is "
         "usually but not always the same as importance."),
        ("Separate common from special cause",
         "Using the last column of the cause-evidence sheet, decide for each cause whether "
         "it is common cause (built into the process, happens every day) or special cause "
         "(a specific one-off event). Common causes are fixed by changing the process; a "
         "team that chases special causes is always firefighting."),
        ("Shortlist on evidence",
         "In templates/root-cause-shortlist-template.csv, shortlist the two or three causes "
         "best supported by evidence — not by opinion, and not by who argued loudest. For "
         "each, record the evidence and where it came from. Three is the maximum a White "
         "Belt team should carry into Improve."),
    ],
    checklist=[
        "The 5 Whys chain ends in something the team can actually act on.",
        "The chain blames a process, not a named person.",
        "Every Fishbone cause sits under one of the five categories.",
        "The vital few are named, with the cumulative percentage quoted from the Pareto.",
        "Each cause is labelled common cause or special cause.",
        "Every shortlisted cause is backed by a stated observation, not an opinion.",
    ],
    tips=[
        "Watch for chains that stop at 'the barista is slow'. That blames a person. Ask "
        "'why is the barista slow?' and keep going.",
        "Some tables stop after two whys. The test is not exactly five levels — it is "
        "reaching something the team can act on.",
        "If a cause appears on the fishbone with no evidence anywhere, point at the "
        "cause-evidence sheet. Opinion is fine in brainstorming, not in the shortlist.",
        "Most rooms label everything 'common cause'. Use the grinder breakdown on the "
        "evidence sheet as the anchor example of a special cause.",
        "Compare two tables' 5 Whys chains side by side at the debrief. They usually reach "
        "different root causes from the same symptom — which is exactly why the evidence "
        "column decides. Flag that Case Study Q2 asks for this chain.",
    ]),

# ================================================================= IMPROVE
4: dict(
    timing=[(4, "Restate the root cause and brainstorm against it"),
            (9, "Score and plot every idea on the impact/effort grid"),
            (6, "Write the chosen method as standard work"),
            (7, "Write the pilot plan, then compare with the real results"),
            (4, "Debrief the Thursday dip")],
    artefact="A brainstormed countermeasure list, a completed impact/effort grid with one "
             "countermeasure selected, standard work for the new method, and a one-week "
             "pilot plan naming a measure, an owner and a review date.",
    steps=[
        ("Restate the root cause",
         "Write your top root cause from Lab 3 at the top of "
         "templates/countermeasure-brainstorm-template.csv. Every idea from here on must "
         "address THIS cause. The discipline of Improve is solving the cause you proved, "
         "not the symptom you started with."),
        ("Brainstorm without judging",
         "Generate at least six countermeasures without evaluating any of them yet. Then "
         "compare your list with data/countermeasure-options.csv, which holds the twelve "
         "the team generated, with impact, effort, cost and risk already scored."),
        ("Check the Lean tools",
         "Two quick tests. 5S: is anything at the counter hard to find, out of place or "
         "untidy? Mistake proofing (Poka-Yoke): could the wrong order be made impossible "
         "rather than merely discouraged? Both often produce cheaper fixes than adding "
         "people."),
        ("Plot the impact/effort grid",
         "Using the Impact and Effort scores in the data, plot every idea on "
         "templates/impact-effort-grid-template.csv and pick ONE from the high-impact, "
         "low-effort corner. Force a spread when scoring — if everything is high impact, "
         "the grid tells you nothing."),
        ("Write the standard work",
         "In templates/standard-work-and-pilot-template.csv, write the improved method as "
         "short numbered steps anyone on shift could follow, ending in an unambiguous "
         "done/not-done check. If you write 'make sure there is enough milk', ask how the "
         "next person would know."),
        ("Write the pilot plan",
         "Complete the pilot rows: what changes, who runs it, the start and end dates, what "
         "you will measure, the baseline to beat, how you will know it worked, and the "
         "review date. Pilot ONE countermeasure — change two and you will not know which "
         "one worked."),
        ("Compare against what actually happened",
         "Now open data/pilot-week-results.csv and read the week day by day against your "
         "plan. Pay close attention to Thursday. Ask yourselves what Thursday tells you "
         "about the countermeasure — and about what is still missing."),
    ],
    checklist=[
        "At least six countermeasures were generated before any was judged.",
        "Every countermeasure addresses the root cause from Lab 3, not the symptom.",
        "All options are plotted on the grid and exactly ONE is selected.",
        "The selection sits in the high-impact, low-effort corner, or is justified if not.",
        "The standard work is short numbered steps with a done/not-done check.",
        "The pilot plan names a measure, a baseline, an owner and a review date.",
        "The group can say what the Thursday result reveals.",
    ],
    tips=[
        "Keep data/pilot-week-results.csv HIDDEN until the pilot plans are written — "
        "revealing it early removes the thinking.",
        "Watch for tables choosing the exciting option (the pre-order app) over the "
        "effective one. Ask which proved root cause it addresses.",
        "Send back any countermeasure aimed at the symptom ('hire more staff so the queue "
        "is shorter') to the Lab 3 shortlist.",
        "Standard work written as a paragraph of prose is not standard work. Numbered steps.",
        "Thursday is the teaching point of the whole lab: the restock was missed and every "
        "measure snapped back. Let the room find it, then ask what would have prevented it "
        "— every answer they give is a CONTROL, and that is the agenda for Lab 5.",
    ]),

# ================================================================= CONTROL
5: dict(
    timing=[(4, "Choose the one measure that shows the gain is holding"),
            (9, "Complete the control plan and the reaction plan"),
            (5, "Design the visual board and write the SOP"),
            (5, "Plan the daily huddle"),
            (7, "Write the one-page summary and name the handover")],
    artefact="A completed control plan with a reaction plan, a visual board sketch, a short "
             "SOP, a daily huddle plan, and a one-page summary of the whole DMAIC story "
             "naming the process owner.",
    steps=[
        ("Choose the control measure",
         "Open data/post-improvement-monitoring.csv — four weeks of daily figures after the "
         "pilot was made permanent. Choose the ONE measure that tells you the improvement "
         "is still working. One or two measures watched properly beat five that nobody "
         "looks at."),
        ("Complete the control plan",
         "Look at data/control-plan-example.csv for the worked first row, then complete "
         "templates/control-plan-template.csv: what is measured, the target, how often it "
         "is checked, where it is recorded, and who owns it. Name one role as owner — a "
         "control plan owned by 'the team' is owned by nobody."),
        ("Write the reaction plan",
         "Write the exact steps to take when the measure misses target. 'Investigate' and "
         "'escalate' are not reaction plans — say what the supervisor physically does "
         "tomorrow morning. Then find week 3 in the monitoring data and state which day "
         "your plan would have triggered on."),
        ("Design the visual board",
         "Sketch a simple board that would have made the week-3 drift visible to the whole "
         "shift on day one. A run of the daily figure beats a single number, because drift "
         "shows up as a trend long before anyone calls it a problem."),
        ("Write the SOP",
         "In templates/sop-and-huddle-template.csv, turn your Lab 4 standard work into a "
         "short SOP the cafe could actually pin up — and state how anyone would know the "
         "step was done."),
        ("Plan the daily huddle",
         "Complete the huddle rows: who attends, what time, how long, what is reviewed and "
         "who runs it. Five minutes at the board is enough. The rule that makes huddles "
         "work: problems are named, not blamed."),
        ("Summarise and hand over",
         "Using templates/one-page-summary-template.csv, summarise the whole project — "
         "problem, cause, countermeasure, result and control — then name who you hand it "
         "over to and when. A White Belt project that stays with the improvement team has "
         "not finished."),
    ],
    checklist=[
        "One control measure is chosen and the reason for choosing it is stated.",
        "The control plan names a measure, a target, a frequency, a place and ONE owner.",
        "The reaction plan says what to DO, not 'investigate' or 'escalate'.",
        "The group can name the day in week 3 their plan would have triggered on.",
        "The visual board shows a run of the measure, not just today's number.",
        "The SOP is numbered steps with a done/not-done check.",
        "The one-page summary tells the complete DMAIC story and names the process owner.",
    ],
    tips=[
        "Project the week-3 rows and let the room find the drift before you name it.",
        "Challenge every reaction plan that says 'investigate'. Ask what the supervisor "
        "physically does tomorrow morning.",
        "Draw out the leading-indicator point: the restock check goes wrong on Monday, but "
        "the wait time only breaches on Tuesday. A control plan built on the leading "
        "indicator buys the team a full day.",
        "Watch for control plans with no owner, or 'the team' as the owner. One named role.",
        "Close the course with the week-3 story: five days, roughly 300 affected customers "
        "and a public complaint — prevented by one tick on a checklist and one glance at a "
        "board. Then have each learner read out the RESULT line from their summary.",
    ]),
}
