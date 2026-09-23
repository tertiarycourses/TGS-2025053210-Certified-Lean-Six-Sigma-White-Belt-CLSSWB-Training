"""
SINGLE SOURCE for the LAB DATA PACK — Certified Lean Six Sigma White Belt.

Every activity folder's mock dataset, blank template, worked model answer and
facilitator notes is defined here, so the lab pack can never drift out of
alignment with course_data.py / data_domainN.py (which define the lab steps)
or with the assessment (which uses the same BrewBean Cafe scenario).

DESIGN RULES (White Belt = AWARENESS depth):
  * The data is small enough to be read by eye and tallied by hand in a
    30-minute lab slot — no pivot tables, no formulas required.
  * Every figure is consistent with the assessment scenario: 7:30-9:00am rush,
    up to 15-minute waits against a 5-minute promise, one till open of two,
    milk fetched from the back store, orders re-keyed, drinks remade.
  * The numbers are internally consistent ACROSS labs: the Activity 2 observation
    log is the evidence base for the Activity 3 Pareto, and the Activity 5 post-pilot
    figures follow from the Activity 4 countermeasure.
  * Data is generated deterministically (fixed seed) so every rebuild produces
    byte-identical files and the model answers stay true.

Each entry in LAB_DATA is keyed by lab number and carries:
    datasets  : list of dict(name, title, desc, headers, rows, notes)
    templates : list of dict(name, title, desc, headers, rows)  - blank to fill
    model     : list of (heading, [lines])   - the worked model answer
    facilitator: dict(timing, setup, watch, mistakes, debrief)
"""

# ------------------------------------------------------------------ Activity 2 raw observation log
# 60 observed customers across the 7:30-9:00am rush on one weekday morning.
# Built deterministically so the Pareto in Activity 3 and the baseline in Activity 5
# always reconcile to the same totals.

_TIME_BANDS = [
    # (band label, n customers, wait low, wait high)  - the 8:00-8:30 peak is worst
    ("07:30-08:00", 12, 4.0, 8.5),
    ("08:00-08:30", 20, 9.0, 15.0),
    ("08:30-09:00", 18, 6.0, 12.5),
    ("09:00-09:15", 10, 2.5, 5.5),
]

_DRINKS = ["Latte", "Flat White", "Cappuccino", "Americano", "Espresso", "Mocha"]

# Delay reason -> how often it occurs. These frequencies ARE the Activity 3 Pareto:
# milk restocking is the vital few, matching the assessment's model 5 Whys chain.
_DELAY_REASONS = [
    ("Waiting for milk restock", 18),
    ("Single till queue", 14),
    ("Order re-keyed into till", 9),
    ("Drink remade (wrong order)", 7),
    ("Card payment slow", 5),
    ("Cups/lids not at hand", 4),
    ("No delay observed", 3),
]


def _build_observation_log():
    """Deterministic 60-row observation log. No randomness: a fixed deal so the
    file is byte-identical on every rebuild and the tallies are exact.

    The deal is weighted, not clustered: the heavy causes (milk restock, single
    till) fall mostly in the 08:00-08:30 peak, but every band carries a mix, so
    the log reads like a real observation sheet rather than a sorted table."""
    reasons = []
    for label, count in _DELAY_REASONS:
        reasons.extend([label] * count)
    assert len(reasons) == 60, len(reasons)

    # each row's band, in clock order
    order = []
    for band, n, lo, hi in _TIME_BANDS:
        order.extend([(band, lo, hi)] * n)
    assert len(order) == 60

    # Deal reasons round-robin with a stride coprime to 60, so the same multiset
    # is spread evenly across the morning instead of blocked by band.
    assigned = [None] * 60
    for slot in range(60):
        assigned[(slot * 7) % 60] = reasons[slot]

    # The quiet 09:00-09:15 band should not carry heavy causes: swap any
    # milk/till reason there with a light reason from the peak.
    heavy = {"Waiting for milk restock", "Single till queue"}
    quiet = [i for i in range(60) if order[i][0] == "09:00-09:15"]
    peak = [i for i in range(60) if order[i][0] == "08:00-08:30"]
    for qi in quiet:
        if assigned[qi] in heavy:
            for pi in peak:
                if assigned[pi] not in heavy:
                    assigned[qi], assigned[pi] = assigned[pi], assigned[qi]
                    break

    rows = []
    for i, (band, lo, hi) in enumerate(order):
        reason = assigned[i]
        span = hi - lo
        frac = ((i * 7) % 11) / 10.0          # 0.0 .. 1.0, repeatable
        wait = round(lo + span * frac, 1)
        # keep the data self-consistent with the reason recorded
        if reason == "Drink remade (wrong order)":
            wait = round(min(wait + 2.5, 18.0), 1)   # a remake always costs more
        elif reason == "No delay observed":
            wait = round(min(wait, 4.5), 1)          # by definition inside promise
        elif reason in heavy:
            wait = round(max(wait, 6.0), 1)          # a real delay exceeds the promise
        drink = _DRINKS[(i * 5) % len(_DRINKS)]
        remade = "Yes" if reason == "Drink remade (wrong order)" else "No"
        # clock time inside the band, evenly spaced
        h, m = band.split("-")[0].split(":")
        base = int(h) * 60 + int(m)
        same_band = [j for j in range(60) if order[j][0] == band]
        pos = same_band.index(i)
        width = 30 if band != "09:00-09:15" else 15
        t = base + int(pos * (width / max(len(same_band), 1)))
        clock = f"{t // 60:02d}:{t % 60:02d}"
        rows.append([
            f"C{i + 1:03d}", clock, band, drink, wait, remade, reason,
        ])
    return rows


OBSERVATION_ROWS = _build_observation_log()

# ---- derived figures the model answers quote (computed, never hand-typed) ----
_waits = [r[4] for r in OBSERVATION_ROWS]
AVG_WAIT = round(sum(_waits) / len(_waits), 1)
MAX_WAIT = max(_waits)
N_OBS = len(OBSERVATION_ROWS)
N_REMAKE = sum(1 for r in OBSERVATION_ROWS if r[5] == "Yes")
_peak = [r[4] for r in OBSERVATION_ROWS if r[2] == "08:00-08:30"]
PEAK_AVG = round(sum(_peak) / len(_peak), 1)
OVER_PROMISE = sum(1 for w in _waits if w > 5.0)
PCT_OVER = round(OVER_PROMISE / N_OBS * 100)

# Pareto table (Activity 3) derived straight from the Activity 2 log
_counts = {}
for r in OBSERVATION_ROWS:
    if r[6] != "No delay observed":
        _counts[r[6]] = _counts.get(r[6], 0) + 1
_total_delays = sum(_counts.values())
PARETO_ROWS = []
_cum = 0
for reason, n in sorted(_counts.items(), key=lambda kv: -kv[1]):
    _cum += n
    PARETO_ROWS.append([
        reason, n,
        round(n / _total_delays * 100, 1),
        round(_cum / _total_delays * 100, 1),
    ])
VITAL_FEW = [p[0] for p in PARETO_ROWS[:2]]
VITAL_FEW_PCT = PARETO_ROWS[1][3]

# ------------------------------------------------------------------ Activity 1
LAB1 = dict(
    datasets=[
        dict(
            name="voc-raw-customer-feedback",
            title="Raw Voice of the Customer feedback",
            desc="Thirty pieces of unedited customer feedback collected by the BrewBean Cafe "
                 "improvement team over two weeks — online reviews, comment cards and remarks "
                 "made at the counter. This is the raw material for Step 2 and Step 3: the "
                 "learner reads it, extracts VOC statements and turns them into measurable CTQs.",
            headers=["Feedback ID", "Date", "Source", "Customer Type", "Verbatim Comment", "Rating (1-5)"],
            rows=[
                ["F01", "2026-06-01", "Online review", "Regular", "Waited 14 minutes for one flat white. I'm late for work now.", 1],
                ["F02", "2026-06-01", "Counter remark", "Regular", "Why is only one till ever open in the morning?", 2],
                ["F03", "2026-06-02", "Online review", "Occasional", "Coffee is great but the queue is out the door by 8am.", 3],
                ["F04", "2026-06-02", "Comment card", "Regular", "Asked for oat milk, got dairy. Had to queue again to get it fixed.", 1],
                ["F05", "2026-06-03", "Online review", "Regular", "I need to be in and out in 5 minutes. It's more like 15.", 2],
                ["F06", "2026-06-03", "Counter remark", "New", "Is there a faster way to order? I'd pre-order if I could.", 3],
                ["F07", "2026-06-04", "Online review", "Regular", "Third time this month my order was wrong. Going elsewhere.", 1],
                ["F08", "2026-06-04", "Comment card", "Occasional", "Staff are lovely but clearly rushed off their feet.", 4],
                ["F09", "2026-06-05", "Online review", "Regular", "They ran out of milk at the counter AGAIN mid-order.", 2],
                ["F10", "2026-06-05", "Counter remark", "Regular", "The barista keeps disappearing to the back. What's going on?", 2],
                ["F11", "2026-06-08", "Online review", "Occasional", "Great coffee, terrible wait. I only go on weekends now.", 3],
                ["F12", "2026-06-08", "Comment card", "Regular", "Please open the second till between 8 and 9.", 2],
                ["F13", "2026-06-09", "Online review", "New", "Queued 12 minutes then gave up and left.", 1],
                ["F14", "2026-06-09", "Counter remark", "Regular", "I want to know how long the wait is before I join the queue.", 3],
                ["F15", "2026-06-10", "Online review", "Regular", "Order written on the cup then typed in again. Seems slow.", 3],
                ["F16", "2026-06-10", "Comment card", "Regular", "My usual order should not need explaining every single day.", 3],
                ["F17", "2026-06-11", "Online review", "Occasional", "Wrong drink twice in a row. Please check before handing over.", 1],
                ["F18", "2026-06-11", "Counter remark", "Regular", "Card machine took ages. Cash would have been quicker.", 3],
                ["F19", "2026-06-12", "Online review", "Regular", "Consistently good coffee when they get the order right.", 4],
                ["F20", "2026-06-12", "Comment card", "New", "No sign of how long the wait is. I had no idea what I was in for.", 2],
                ["F21", "2026-06-15", "Online review", "Regular", "Waited 15 minutes. That is my whole coffee break gone.", 1],
                ["F22", "2026-06-15", "Counter remark", "Regular", "Can you not make the regulars' orders ahead?", 3],
                ["F23", "2026-06-16", "Online review", "Occasional", "Lovely staff, chaotic mornings.", 3],
                ["F24", "2026-06-16", "Comment card", "Regular", "Decaf came as regular. I can't drink that.", 1],
                ["F25", "2026-06-17", "Online review", "Regular", "5 minute promise on the wall is a joke at 8:15am.", 1],
                ["F26", "2026-06-17", "Counter remark", "New", "Do you do mobile ordering? Everywhere else does.", 3],
                ["F27", "2026-06-18", "Online review", "Regular", "Cups and lids seem to be kept miles apart. Odd to watch.", 3],
                ["F28", "2026-06-18", "Comment card", "Regular", "I want the same drink, same way, every morning. That's all.", 4],
                ["F29", "2026-06-19", "Online review", "Occasional", "Second till sat empty while 11 of us queued.", 1],
                ["F30", "2026-06-19", "Counter remark", "Regular", "If it's going to be 15 minutes just tell me and I'll come back.", 2],
            ],
            notes="Ratings are the customer's own 1-5 star score where one was given. "
                  "Use the verbatim column for Step 2 — VOC must stay in the customer's words.",
        ),
    ],
    templates=[
        dict(name="voc-to-ctq-template", title="VOC-to-CTQ table (blank)",
             desc="Step 2 and Step 3. One row per VOC statement.",
             headers=["#", "VOC statement (customer's own words)", "What the customer really needs",
                      "CTQ requirement (measurable)", "Measure", "Target + unit"],
             rows=[[i, "", "", "", "", ""] for i in range(1, 6)]),
        dict(name="problem-statement-and-scope-template", title="Problem statement, SMART goal and scope (blank)",
             desc="Steps 4, 5 and 6.",
             headers=["Element", "Your entry"],
             rows=[["What is wrong", ""], ["Where / when it happens", ""], ["Since when", ""],
                   ["How big (the measure)", ""], ["Impact on the business", ""],
                   ["FULL PROBLEM STATEMENT (no solution)", ""],
                   ["SMART goal - Specific", ""], ["SMART goal - Measurable", ""],
                   ["SMART goal - Achievable", ""], ["SMART goal - Relevant", ""],
                   ["SMART goal - Time-bound", ""], ["FULL SMART GOAL", ""],
                   ["IN scope", ""], ["OUT of scope", ""]]),
    ],
    model=[
        ("VOC-to-CTQ table (model)", [
            "1. VOC: 'I need to be in and out in 5 minutes. It's more like 15.' (F05)",
            "   Need: to be served quickly enough to still get to work on time.",
            "   CTQ: Customer served within 5 minutes.  Measure: wait time, minutes.  Target: <= 5 min.",
            "2. VOC: 'Asked for oat milk, got dairy. Had to queue again.' (F04)",
            "   Need: the drink I ordered, first time.",
            "   CTQ: Order correct on first presentation.  Measure: drinks remade, count.  Target: 0 per morning.",
            "3. VOC: 'Why is only one till ever open in the morning?' (F02)",
            "   Need: enough serving capacity at peak.",
            "   CTQ: Two tills open during the rush.  Measure: tills open at 08:00.  Target: 2.",
            "4. VOC: 'They ran out of milk at the counter AGAIN mid-order.' (F09)",
            "   Need: the order made without interruption.",
            "   CTQ: Counter stocked for the full rush.  Measure: mid-order restock trips.  Target: 0.",
            "5. VOC: 'I want to know how long the wait is before I join the queue.' (F14)",
            "   Need: to decide whether to queue.",
            "   CTQ: Expected wait displayed.  Measure: wait time shown, yes/no.  Target: displayed from 07:30.",
            "",
            "MARK AS CORRECT only if every CTQ carries BOTH a number AND a unit. 'Faster service'",
            "is not a CTQ; 'served within 5 minutes' is.",
        ]),
        ("Problem statement (model)", [
            "\"Between 7:30am and 9:00am over the past two months, customers at BrewBean Cafe have",
            "waited up to 15 minutes to be served against the cafe's own 5-minute service promise,",
            "generating a rising number of online complaints and the loss of several regular",
            "customers.\"",
            "",
            "It passes because it states WHAT is wrong (wait exceeds promise), WHERE/WHEN (BrewBean,",
            "7:30-9:00am), SINCE WHEN (two months), HOW BIG (15 min vs 5 min) and the IMPACT",
            "(complaints, lost regulars) — and it names NO solution.",
            "",
            "REJECT anything containing a solution, e.g. '...because we need to open a second till'.",
        ]),
        ("SMART goal (model)", [
            "\"Reduce the average customer wait time during the 7:30-9:00am rush at BrewBean Cafe",
            "from 15 minutes to 5 minutes or less by 31 December 2026, without increasing staffing",
            "cost.\"",
            "",
            "Specific: wait time at BrewBean during the morning rush.",
            "Measurable: from 15 minutes to <= 5 minutes.",
            "Achievable: no extra headcount required; the second till already exists.",
            "Relevant: it is the CTQ customers complain about and it is losing the cafe regulars.",
            "Time-bound: by 31 December 2026.",
        ]),
        ("Scope (model)", [
            "IN SCOPE:  the 7:30-9:00am weekday morning rush; from the customer joining the queue",
            "           to the drink being handed over; the counter, till and barista station.",
            "OUT OF SCOPE: weekend trade; the food/pastry counter; supplier contracts and bean",
            "           sourcing; the cafe's fit-out and any building works; afternoon trade.",
            "",
            "The point of the scope table is that a White Belt project stays SMALL. Anything that",
            "would need capital spend or a supplier renegotiation belongs outside it.",
        ]),
    ],
    facilitator=dict(
        timing="30 minutes. 5 min reading the feedback, 10 min VOC-to-CTQ, 10 min problem "
               "statement and SMART goal, 5 min scope and debrief.",
        setup="Hand out (or open) voc-raw-customer-feedback.csv/.xlsx. Learners can work in "
              "pairs. No software beyond a spreadsheet or a printout is needed.",
        watch=[
            "Learners paraphrasing the VOC into business language — stop them. VOC must stay in "
            "the customer's own words; the translation happens in the CTQ column, not before.",
            "CTQs written without a unit ('serve faster'). Push for a number AND a unit.",
            "A problem statement that smuggles in a solution — this is the single most common "
            "White Belt error and it is explicitly tested in Case Study Q1.",
        ],
        mistakes=[
            "Writing the problem statement first and the VOC afterwards to fit it.",
            "Confusing the SMART goal with the problem statement — the problem is what is wrong "
            "TODAY, the goal is what will be true at the END.",
            "Putting everything in scope. Ask: 'could a White Belt team finish that in six weeks?'",
        ],
        debrief="Ask two pairs to read out their problem statement and have the room vote on "
                "whether it contains a hidden solution. Then confirm the four components it must "
                "carry — what, where/when, how big, impact — and note that Case Study Q1 asks for "
                "exactly this.",
    ),
)

# ------------------------------------------------------------------ Activity 2
LAB2 = dict(
    datasets=[
        dict(
            name="morning-rush-observation-log",
            title="Morning rush observation log",
            desc=f"{N_OBS} customers observed end to end during one weekday morning rush at "
                 "BrewBean Cafe. Wait time is measured from the customer joining the queue to "
                 "the drink being handed over. This is THE baseline dataset for the course — "
                 "Activity 3's Pareto is derived from the Delay Reason column and Activity 5's control "
                 "chart compares back to it.",
            headers=["Customer ID", "Time Joined Queue", "Time Band", "Drink Ordered",
                     "Wait Time (min)", "Drink Remade", "Delay Reason Observed"],
            rows=OBSERVATION_ROWS,
            notes=f"Observed by the improvement team with a stopwatch and a check sheet. "
                  f"Average wait {AVG_WAIT} min; longest {MAX_WAIT} min; "
                  f"{OVER_PROMISE} of {N_OBS} customers ({PCT_OVER}%) exceeded the 5-minute "
                  f"promise; {N_REMAKE} drinks were remade.",
        ),
        dict(
            name="process-step-timings",
            title="Process step timings",
            desc="The average observed time for each step of the morning-rush process, with the "
                 "team's value-add judgement left blank in the template. Use it for Step 3 and "
                 "Step 4 of the lab.",
            headers=["Step No", "Process Step", "Who Does It", "Avg Time (sec)",
                     "Observed Range (sec)", "Times Step Was Skipped"],
            rows=[
                [1, "Customer joins the queue", "Customer", 0, "0", 0],
                [2, "Customer waits to reach the till", "Customer", 265, "60-540", 0],
                [3, "Customer states the order", "Customer + Cashier", 22, "12-40", 0],
                [4, "Cashier writes the order on the cup", "Cashier", 11, "7-18", 0],
                [5, "Cashier re-keys the order into the till", "Cashier", 19, "12-35", 0],
                [6, "Customer pays by card", "Customer + Cashier", 27, "15-70", 0],
                [7, "Cup passed to the barista station", "Cashier", 8, "4-15", 0],
                [8, "Cup waits in the barista queue", "-", 143, "20-420", 0],
                [9, "Barista grinds and extracts the shot", "Barista", 34, "28-45", 0],
                [10, "Barista fetches milk from the back store", "Barista", 96, "0-180", 42],
                [11, "Barista steams the milk and pours", "Barista", 41, "33-58", 0],
                [12, "Barista finds a lid and sleeve", "Barista", 14, "6-30", 0],
                [13, "Barista calls the order out", "Barista", 6, "3-12", 0],
                [14, "Customer collects the drink", "Customer", 9, "4-25", 0],
                [15, "Drink remade after an error", "Barista", 78, "0-140", 53],
            ],
            notes="'Times Step Was Skipped' counts how many of the 60 observed customers did NOT "
                  "experience that step — so step 10 happened for 18 of 60 customers and step 15 "
                  "for 7 of 60. Steps 2, 8 and 10 are where the time actually goes.",
        ),
        dict(
            name="downtime-waste-tally",
            title="DOWNTIME waste tally (partially completed)",
            desc="The team's waste walk, half done. Three rows are filled in as worked examples; "
                 "the learner completes the rest in Step 6 from the observation log and the "
                 "process timings.",
            headers=["Waste Type (DOWNTIME)", "What It Looks Like Here",
                     "Process Step", "Tally Count", "Est. Time Lost per Morning (min)"],
            rows=[
                ["D - Defects", "Drinks made wrong and remade", "15", 7, 9],
                ["O - Overproduction", "", "", "", ""],
                ["W - Waiting", "Customers queueing; cups waiting at the barista station", "2, 8", 60, 408],
                ["N - Non-utilised talent", "", "", "", ""],
                ["T - Transport", "", "", "", ""],
                ["I - Inventory", "", "", "", ""],
                ["M - Motion", "Barista walking to the back store for milk", "10", 18, 29],
                ["E - Extra-processing", "", "", "", ""],
            ],
            notes="The three completed rows are worked examples. The learner fills the remaining "
                  "five from what the data actually shows — some may legitimately be zero, and "
                  "saying so with evidence is a correct answer.",
        ),
    ],
    templates=[
        dict(name="sipoc-template", title="SIPOC (blank)",
             desc="Step 2. Keep Process to 5-7 steps only.",
             headers=["Suppliers", "Inputs", "Process (5-7 steps)", "Outputs", "Customers"],
             rows=[["", "", "", "", ""] for _ in range(7)]),
        dict(name="process-map-template", title="Process map with value-add judgement (blank)",
             desc="Steps 3 and 4.",
             headers=["Step No", "Process Step", "Time (sec)", "Value-Adding? (VA/NVA)",
                      "Why you judged it that way"],
             rows=[[i, "", "", "", ""] for i in range(1, 16)]),
        dict(name="downtime-tally-template", title="DOWNTIME tally sheet (blank)",
             desc="Step 6.",
             headers=["Waste Type", "What It Looks Like Here", "Process Step", "Tally Count",
                      "Est. Time Lost per Morning (min)"],
             rows=[[w, "", "", "", ""] for w in
                   ["D - Defects", "O - Overproduction", "W - Waiting", "N - Non-utilised talent",
                    "T - Transport", "I - Inventory", "M - Motion", "E - Extra-processing"]]),
    ],
    model=[
        ("SIPOC (model)", [
            "SUPPLIERS: coffee bean roaster; dairy/oat milk supplier; cup and lid supplier;",
            "           till and card-machine provider; the cafe's own back store.",
            "INPUTS:    beans, milk, cups, lids, sleeves; the customer's order; barista and",
            "           cashier time; the espresso machine and grinder; the till system.",
            "PROCESS:   1. Customer joins queue  2. Order taken at till  3. Payment  4. Cup to",
            "           barista  5. Drink made  6. Drink handed over.",
            "OUTPUTS:   the finished drink; the receipt; the customer's experience of the wait.",
            "CUSTOMERS: office workers in the morning rush (the primary customer); walk-in and",
            "           occasional customers.",
            "",
            "Mark down a SIPOC whose Process column has 12 steps — the discipline is the 5-7 step",
            "high-level view. The detail belongs in the process map, not the SIPOC.",
        ]),
        ("Process map and value-add judgement (model)", [
            "VALUE-ADDING (the customer would pay for it): steps 3 (stating the order),",
            "  9 (grinding and extracting), 11 (steaming and pouring).  Total ~97 sec.",
            "NON-VALUE-ADDING: steps 2, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15.  Total ~671 sec.",
            "",
            f"So roughly 97 of 768 seconds - about 13% - of the process is value-adding. The",
            "single largest non-value-adding block is step 2 (queueing, 265 sec) followed by",
            "step 8 (cup waiting at the barista station, 143 sec) and step 10 (fetching milk,",
            "96 sec average).",
            "",
            "Accept step 6 (payment) being argued either way, as long as the learner justifies it:",
            "the customer must pay, but they would not pay EXTRA for the paying. Business-value-",
            "adding is the usual verdict. Step 5 (re-keying) is never value-adding — the order was",
            "already captured in step 4.",
        ]),
        ("Data type classification (model)", [
            "CONTINUOUS (measured on a scale): Wait Time (min); every Avg Time (sec) in the",
            "  process timings; time lost per morning.",
            "DISCRETE (counted): Customer ID count; Drink Remade yes/no count; tally counts in the",
            "  DOWNTIME sheet; number of tills open; complaint counts.",
            "",
            "'Drink Ordered' and 'Delay Reason' are neither — they are CATEGORICAL (attribute)",
            "data. At White Belt it is enough that the learner does not call them continuous.",
        ]),
        ("DOWNTIME tally (model — the five rows left blank)", [
            "O - Overproduction: preparing drinks speculatively before an order is placed.",
            "  Tally 0 at BrewBean today. 'Zero, with evidence' is a correct answer.",
            "N - Non-utilised talent: a trained barista spending ~29 min a morning walking to the",
            "  back store for milk, and the second till standing idle while a trained cashier",
            "  serves elsewhere. Tally 18 (the restock trips). ~29 min.",
            "T - Transport: the cup travelling from till to barista station (step 7) - small but",
            "  real. Tally 60, ~8 min.",
            "I - Inventory: cups queued at the barista station waiting to be made (step 8) - work",
            "  in progress sitting in a queue. Tally 60, ~143 min of accumulated cup-waiting.",
            "E - Extra-processing: writing the order on the cup and then re-keying it into the",
            "  till (steps 4 + 5) - the same information captured twice. Tally 60, ~19 min.",
            "",
            f"LARGEST WASTE BY COUNT AND BY TIME: W - Waiting, at step 2 and step 8.",
            "The most ACTIONABLE waste is M - Motion / N - Non-utilised talent at step 10, because",
            "it has a single obvious cause the team can remove. That is the thread Activity 3 pulls.",
        ]),
        ("Baseline figures (model)", [
            f"Customers observed:        {N_OBS}",
            f"Average wait:              {AVG_WAIT} min   (promise: 5.0 min)",
            f"Longest wait:              {MAX_WAIT} min",
            f"Average wait at 08:00-08:30 peak: {PEAK_AVG} min",
            f"Customers over the 5-min promise: {OVER_PROMISE} of {N_OBS}  ({PCT_OVER}%)",
            f"Drinks remade:             {N_REMAKE}",
            "",
            "These are the numbers Activity 5 measures the improvement against. Learners should write",
            "them down — the Case Study expects a baseline to be quoted, not invented.",
        ]),
    ],
    facilitator=dict(
        timing="30 minutes. 5 min SIPOC, 10 min process map and value-add, 5 min data types, "
               "10 min waste tally and debrief.",
        setup="Open morning-rush-observation-log and process-step-timings. If the room has a "
              "whiteboard, draw the SIPOC on it together before learners fill their own.",
        watch=[
            "SIPOC Process columns running to 15 steps. Hold the line at 5-7.",
            "Learners marking the whole process value-adding because 'the customer wants coffee'. "
            "The test is per STEP: would the customer pay extra for THIS step?",
            "Learners calling 'Drink Ordered' continuous data. It is categorical — steer them to "
            "the two types the course teaches and note that a label is neither.",
        ],
        mistakes=[
            "Tallying waste from memory instead of from the data. Point them back at the log.",
            "Recording zero for a waste type and treating that as a failure. Zero with evidence "
            "is a legitimate, well-supported answer.",
            "Jumping to 'hire more staff' during the waste walk. Park it — solutions are Activity 4.",
        ],
        debrief="Put the baseline figures on the board and ask: which single step would you "
                f"attack first? Most rooms say the queue (step 2). Push back — the queue is the "
                "SYMPTOM. Step 10 (fetching milk) is a cause you can act on, and that hands "
                "straight over to Activity 3.",
    ),
)

# ------------------------------------------------------------------ Activity 3
LAB3 = dict(
    datasets=[
        dict(
            name="delay-reason-pareto-data",
            title="Delay reason Pareto data",
            desc="The Delay Reason column from the Activity 2 observation log, counted and ranked. "
                 "This is the 'supplied Pareto chart' the lab's Step 5 refers to — the learner "
                 "reads it rather than building it from scratch.",
            headers=["Delay Reason", "Count", "% of Delays", "Cumulative %"],
            rows=PARETO_ROWS,
            notes=f"Derived from the {N_OBS}-customer observation log ({_total_delays} customers "
                  f"experienced a delay). The top two reasons — {VITAL_FEW[0]} and {VITAL_FEW[1]} "
                  f"— account for {VITAL_FEW_PCT}% of all delays. That is the 'vital few'.",
        ),
        dict(
            name="cause-evidence-sheet",
            title="Candidate causes and their evidence",
            desc="Every cause the team brainstormed, with whether any evidence actually supports "
                 "it. Used in Step 7 to shortlist causes on evidence rather than opinion, and in "
                 "Step 6 to judge common vs special cause.",
            headers=["Candidate Cause", "Fishbone Category", "Evidence in the Data?",
                     "Where the Evidence Is", "Common or Special Cause?"],
            rows=[
                ["Counter milk not restocked before the rush", "Method", "Yes",
                 "18 restock trips; step 10 avg 96 sec", "Common"],
                ["Only one till open at peak", "Manpower", "Yes",
                 "14 single-till delays; 2 tills installed", "Common"],
                ["Order written on cup then re-keyed", "Method", "Yes",
                 "Steps 4+5 duplicate; 9 delays", "Common"],
                ["Wrong drinks made and remade", "Method", "Yes",
                 f"{N_REMAKE} remakes; step 15 avg 78 sec", "Common"],
                ["Card machine slow to connect", "Machine", "Yes",
                 "5 delays; step 6 range up to 70 sec", "Common"],
                ["Cups and lids stored apart", "Material", "Yes",
                 "4 delays; step 12 range up to 30 sec", "Common"],
                ["Barista was new and still training", "Manpower", "No",
                 "Not recorded; opinion only", "Special"],
                ["Grinder broke down on 12 June", "Machine", "No",
                 "One-off, outside the observed period", "Special"],
                ["Wait time is not measured at all", "Measurement", "Yes",
                 "No wait-time record existed before this log", "Common"],
                ["Customers order complicated drinks", "Material", "No",
                 "No link in the data between drink type and wait", "Common"],
                ["A tour group arrived on 15 June", "Manpower", "No",
                 "Single event; not in the observed morning", "Special"],
                ["No agreed target for service time", "Measurement", "Yes",
                 "5-min promise on the wall, never tracked", "Common"],
            ],
            notes="Deliberately mixed: some causes are evidence-backed and some are pure opinion. "
                  "The learning point of Step 7 is telling them apart.",
        ),
    ],
    templates=[
        dict(name="5-whys-template", title="5 Whys chain (blank)",
             desc="Steps 1 and 2. Stop when you reach something the team can act on.",
             headers=["Level", "Question", "Answer"],
             rows=[["Problem (symptom)", "What is going wrong?", ""],
                   ["Why 1", "Why does that happen?", ""],
                   ["Why 2", "Why does THAT happen?", ""],
                   ["Why 3", "Why does THAT happen?", ""],
                   ["Why 4", "Why does THAT happen?", ""],
                   ["Why 5", "Why does THAT happen?", ""],
                   ["ROOT CAUSE", "What can the team actually act on?", ""],
                   ["Check", "If we remove this, does the problem stop recurring?", ""]]),
        dict(name="fishbone-template", title="Fishbone (5M) diagram (blank)",
             desc="Steps 3 and 4. Problem goes in the head of the fish.",
             headers=["Category", "Cause 1", "Cause 2", "Cause 3", "Cause 4"],
             rows=[[c, "", "", "", ""] for c in
                   ["Manpower", "Method", "Machine", "Material", "Measurement"]]),
        dict(name="root-cause-shortlist-template", title="Root cause shortlist (blank)",
             desc="Steps 6 and 7.",
             headers=["Shortlisted Cause", "Evidence that supports it",
                      "Common or Special Cause?", "Why it made the shortlist"],
             rows=[["", "", "", ""] for _ in range(3)]),
    ],
    model=[
        ("5 Whys (model)", [
            f"PROBLEM: Customers wait an average of {AVG_WAIT} minutes (up to {MAX_WAIT}) during",
            "         the morning rush against a 5-minute promise.",
            "WHY 1?   Drinks are not completed fast enough to clear the queue.",
            "WHY 2?   The barista keeps stopping part-way through making an order.",
            "WHY 3?   The milk at the counter runs out during the rush.",
            "WHY 4?   It is not restocked before the rush starts.",
            "WHY 5?   Restocking the counter milk is not part of anyone's opening routine.",
            "ROOT CAUSE: No one owns restocking counter milk before 7:30am — it was never written",
            "         into the opening checklist.",
            "CHECK:   If restocking is assigned and done before 7:30am, the 18 mid-order trips",
            "         stop, and roughly 29 minutes a morning of barista time comes back.",
            "",
            "This is the SAME chain the Case Study answer key uses, so a learner who works this",
            "lab properly has already rehearsed Case Study Q2.",
            "",
            "Accept any chain that (a) ends in a PROCESS the team can change and (b) does not end",
            "by blaming a named person. 'The barista is too slow' is not a root cause — ask why.",
        ]),
        ("Fishbone (model)", [
            "HEAD OF THE FISH: 'Morning queue is too slow (avg "
            f"{AVG_WAIT} min vs 5 min promise)'",
            "",
            "MANPOWER:    one till open at peak though two are installed; no cover for breaks;",
            "             no one assigned to restock.",
            "METHOD:      no opening restock routine; order written on the cup then re-keyed;",
            "             no check before handover so wrong drinks reach the customer.",
            "MACHINE:     single grinder; card machine slow to connect.",
            "MATERIAL:    milk stored in the back store, not at the counter; cups and lids kept",
            "             apart.",
            "MEASUREMENT: wait time never recorded; the 5-minute promise never tracked; complaints",
            "             not logged anywhere the team can see.",
            "",
            "Every one of these appears in the cause-evidence sheet, so learners can check their",
            "fishbone against the data rather than against the trainer's opinion.",
        ]),
        ("Reading the Pareto (model)", [
            "The ranked delay reasons are:",
        ] + [f"  {i+1}. {r[0]}: {r[1]} ({r[2]}%, cumulative {r[3]}%)"
             for i, r in enumerate(PARETO_ROWS)] + [
            "",
            f"THE VITAL FEW: {VITAL_FEW[0]} and {VITAL_FEW[1]} together account for",
            f"{VITAL_FEW_PCT}% of all observed delays. Fixing those two addresses most of the",
            "problem; the remaining reasons are the 'useful many' and can wait.",
            "",
            "This is the 80/20 point of the Pareto principle — and it is why the team works on",
            "milk restocking and till cover rather than on the slow card machine.",
        ]),
        ("Common vs special cause (model)", [
            "COMMON CAUSE (built into the process, happens every day): milk not restocked; one",
            "  till open; the re-keying step; no measurement of wait time; no agreed target.",
            "  These are fixed by CHANGING THE PROCESS.",
            "SPECIAL CAUSE (a specific one-off event): the grinder breaking on 12 June; the tour",
            "  group on 15 June; a new barista still training.",
            "  These are fixed by dealing with THAT EVENT — and you do not redesign a process",
            "  around a one-off.",
            "",
            "The White Belt point: a team that chases special causes is always firefighting. The",
            "improvement comes from the common causes.",
        ]),
        ("Shortlist (model)", [
            "1. Counter milk not restocked before the rush — Method — COMMON.",
            "   Evidence: 18 of 60 customers delayed by it; 96 sec average per trip; ~29 min of",
            "   barista time lost per morning. Highest-count single reason on the Pareto.",
            "2. Only one till open at peak — Manpower — COMMON.",
            "   Evidence: 14 of 60 customers delayed; a second till is already installed, so the",
            "   fix costs nothing in capital.",
            "3. Order written on the cup then re-keyed into the till — Method — COMMON.",
            "   Evidence: steps 4 and 5 capture the same information twice, ~19 sec per customer.",
            "",
            "Note what is NOT shortlisted: 'the barista was new' and 'a tour group arrived' — both",
            "special causes with no supporting evidence in the observed morning.",
        ]),
    ],
    facilitator=dict(
        timing="30 minutes. 10 min 5 Whys, 10 min Fishbone, 5 min reading the Pareto, 5 min "
               "shortlist and debrief.",
        setup="Open delay-reason-pareto-data and cause-evidence-sheet. The online 5 Whys and "
              "Fishbone tools (links in the lab README) work well projected — build one chain "
              "together as a room before learners work in pairs.",
        watch=[
            "5 Whys chains that stop at 'the barista is slow'. That blames a person, not a "
            "process. Ask 'why is the barista slow?' and keep going.",
            "Chains that stop after two whys because the answer sounds plausible. The test is not "
            "five levels exactly — it is reaching something the team can ACT on.",
            "Causes appearing on the fishbone that have no evidence anywhere. Point at the "
            "cause-evidence sheet: opinion is allowed in brainstorming, not in the shortlist.",
        ],
        mistakes=[
            "Treating the Pareto as a ranking of importance rather than of frequency. It shows "
            "what happens MOST, which is usually but not always what matters most.",
            "Confusing common and special cause — most rooms label everything 'common'. Use the "
            "grinder breakdown as the anchor example of a special cause.",
            "Shortlisting five or six causes. Three is the maximum a White Belt team can carry "
            "into Improve.",
        ],
        debrief="Compare two pairs' 5 Whys chains side by side. They will usually reach different "
                "root causes from the same symptom — that is the point, and it is why the "
                "evidence column decides which one the team acts on. Flag that Case Study Q2 asks "
                "for exactly this chain.",
    ),
)

# ------------------------------------------------------------------ Activity 4
LAB4 = dict(
    datasets=[
        dict(
            name="countermeasure-options",
            title="Countermeasure options with impact, effort and cost",
            desc="Twelve candidate countermeasures the team generated against the shortlisted "
                 "root causes, scored for impact and effort. Used in Step 5 to plot the "
                 "impact/effort grid and choose one.",
            headers=["Option", "Countermeasure", "Addresses Which Root Cause",
                     "Impact (1-5)", "Effort (1-5)", "Est. Cost (SGD)", "Risk"],
            rows=[
                ["A", "Add counter milk restock to the 7:00am opening checklist",
                 "Milk not restocked", 5, 1, 0, "Low"],
                ["B", "Move a milk fridge to the barista station",
                 "Milk not restocked", 5, 3, 900, "Low"],
                ["C", "Open the second till from 07:45 to 09:00",
                 "One till open", 4, 2, 0, "Low"],
                ["D", "Hire an extra barista for the morning shift",
                 "One till open", 4, 5, 2400, "Medium"],
                ["E", "Take the order straight into the till, drop the cup-writing step",
                 "Order re-keyed", 3, 2, 0, "Low"],
                ["F", "Install a mobile pre-order app",
                 "One till open", 5, 5, 12000, "High"],
                ["G", "Colour-coded cup stickers for milk type",
                 "Drinks remade", 4, 1, 40, "Low"],
                ["H", "Barista reads the order back before handing over",
                 "Drinks remade", 3, 1, 0, "Low"],
                ["I", "Move cups, lids and sleeves into one station caddy (5S)",
                 "Cups and lids apart", 3, 1, 60, "Low"],
                ["J", "Replace the card machine",
                 "Card machine slow", 2, 4, 700, "Medium"],
                ["K", "Display the expected wait on a board at the door",
                 "No measurement", 2, 1, 30, "Low"],
                ["L", "Buy a second espresso grinder",
                 "Single grinder", 3, 4, 3200, "Medium"],
            ],
            notes="Impact 5 = would remove most of the delay; Effort 5 = weeks of work or "
                  "significant spend. The high-impact / low-effort corner is impact >= 4 and "
                  "effort <= 2.",
        ),
        dict(
            name="pilot-week-results",
            title="Pilot week results",
            desc="What actually happened when the chosen countermeasure was piloted for one week. "
                 "The same 60-customer observation was repeated each day. Used in Step 7 to "
                 "judge whether the pilot worked, and carried into Activity 5 as the new baseline.",
            headers=["Day", "Date", "Customers Observed", "Avg Wait (min)", "Longest Wait (min)",
                     "Drinks Remade", "Mid-order Milk Trips", "Restock Done Before 07:30?"],
            rows=[
                ["Baseline", "2026-06-19", 60, AVG_WAIT, MAX_WAIT, N_REMAKE, 18, "No"],
                ["Mon", "2026-06-22", 58, 8.4, 13.5, 5, 4, "Yes"],
                ["Tue", "2026-06-23", 61, 7.1, 11.0, 4, 2, "Yes"],
                ["Wed", "2026-06-24", 59, 6.3, 9.5, 3, 1, "Yes"],
                ["Thu", "2026-06-25", 62, 9.8, 15.0, 6, 7, "No"],
                ["Fri", "2026-06-26", 60, 6.0, 9.0, 3, 0, "Yes"],
            ],
            notes="Thursday is deliberately bad — the opening staff member was on leave and the "
                  "restock was missed. That single row is the most important teaching point in "
                  "the lab: the countermeasure works, but nothing yet HOLDS it in place. That is "
                  "exactly what Activity 5 (Control) exists to fix.",
        ),
    ],
    templates=[
        dict(name="countermeasure-brainstorm-template", title="Countermeasure brainstorm (blank)",
             desc="Steps 1 and 2. At least six ideas, no judging yet.",
             headers=["#", "Countermeasure idea", "Which root cause does it address?"],
             rows=[[i, "", ""] for i in range(1, 9)]),
        dict(name="impact-effort-grid-template", title="Impact/effort grid (blank)",
             desc="Step 5. Score each idea, then place it in a quadrant.",
             headers=["Option", "Countermeasure", "Impact (1-5)", "Effort (1-5)",
                      "Quadrant", "Selected?"],
             rows=[["", "", "", "", "", ""] for _ in range(8)]),
        dict(name="standard-work-and-pilot-template", title="Standard work and pilot plan (blank)",
             desc="Steps 6 and 7.",
             headers=["Element", "Your entry"],
             rows=[["Selected countermeasure", ""], ["Root cause it addresses", ""],
                   ["Standard work step 1", ""], ["Standard work step 2", ""],
                   ["Standard work step 3", ""], ["Standard work step 4", ""],
                   ["Standard work step 5", ""],
                   ["Pilot: what changes", ""], ["Pilot: who runs it", ""],
                   ["Pilot: start and end date", ""], ["Pilot: what we will measure", ""],
                   ["Pilot: baseline to beat", ""], ["Pilot: how we will know it worked", ""],
                   ["Pilot: review date", ""]]),
    ],
    model=[
        ("Impact/effort grid (model)", [
            "HIGH IMPACT / LOW EFFORT — do these first (impact >= 4, effort <= 2):",
            "  A  Add counter milk restock to the opening checklist   (5 impact, 1 effort, $0)",
            "  C  Open the second till 07:45-09:00                    (4 impact, 2 effort, $0)",
            "  G  Colour-coded cup stickers for milk type             (4 impact, 1 effort, $40)",
            "HIGH IMPACT / HIGH EFFORT — plan these later:",
            "  B  Milk fridge at the barista station; D  Extra barista; F  Pre-order app",
            "LOW IMPACT / LOW EFFORT — easy wins, do if convenient:",
            "  E  Order straight into the till; H  Read the order back; I  5S caddy; K  Wait board",
            "LOW IMPACT / HIGH EFFORT — do not do these:",
            "  J  Replace the card machine; L  Second grinder",
            "",
            "SELECTED: Option A — add counter milk restock to the 7:00am opening checklist.",
            "Why: it is the highest impact on the grid, costs nothing, can start tomorrow, and it",
            "addresses the root cause proved in Activity 3 rather than the symptom. A White Belt",
            "countermeasure should be small enough to try next week — this one is.",
            "",
            "Reject an answer that selects F (the pre-order app): it may be a good idea, but it is",
            "$12,000, high risk, and it does not address the proven root cause. It solves the",
            "SYMPTOM (queue length).",
        ]),
        ("Standard work (model)", [
            "COUNTER MILK RESTOCK — opening routine, to be done by 07:15 every weekday:",
            "  1. On arrival, open the back store fridge.",
            "  2. Carry 6 litres of dairy and 3 litres of oat milk to the counter fridge.",
            "  3. Fill the counter fridge to the marked fill line.",
            "  4. Check the line is reached; if not, fetch one more litre.",
            "  5. Tick 'Counter milk restocked' on the opening checklist and initial it.",
            "",
            "Good standard work is short, numbered, written for the person doing the job, and has",
            "an unambiguous done/not-done check (the fill line and the tick). If a learner writes",
            "'make sure there is enough milk', ask them how the next person would know.",
        ]),
        ("Pilot plan (model)", [
            "WHAT CHANGES:   counter milk is restocked to the fill line before 07:15 each weekday.",
            "WHO RUNS IT:    the opening staff member; the shift supervisor owns the result.",
            "WHEN:           Monday 22 June to Friday 26 June 2026 (one week).",
            "WHAT WE MEASURE: average wait time 07:30-09:00; number of mid-order milk trips;",
            "                 drinks remade; and whether the restock was done before 07:30.",
            f"BASELINE TO BEAT: {AVG_WAIT} min average wait, 18 milk trips, {N_REMAKE} remakes.",
            "HOW WE KNOW IT WORKED: average wait falls below 8 minutes AND mid-order milk trips",
            "                 fall below 5 per morning.",
            "REVIEW DATE:    Monday 29 June 2026.",
        ]),
        ("Reading the pilot results (model)", [
            f"Baseline:  {AVG_WAIT} min average, 18 milk trips, {N_REMAKE} remakes.",
            "Mon 8.4 / Tue 7.1 / Wed 6.3 / Thu 9.8 / Fri 6.0 min.",
            "Average across the pilot week: 7.5 min — a fall of about 5.4 minutes, roughly 42%.",
            "Mid-order milk trips fell from 18 to 0-7 per morning; remakes fell from "
            f"{N_REMAKE} to 3-6.",
            "",
            "VERDICT: the pilot met its success criteria on four days of five. The countermeasure",
            "works. But the wait is not yet at the 5-minute CTQ, so the team should keep going —",
            "option C (second till) is the next item on the grid.",
            "",
            "THE THURSDAY POINT — this is the lesson of the lab:",
            "On Thursday the opening staff member was on leave, the restock was missed, and every",
            "measure snapped back towards baseline (9.8 min, 7 milk trips, 6 remakes). The",
            "improvement is real but FRAGILE: it depends on one person remembering. Nothing yet",
            "holds it in place when that person is away.",
            "",
            "Ask the room: what would stop Thursday happening again? Every answer they give — a",
            "checklist that is signed, a visual board, an SOP, a daily huddle, a named owner, a",
            "reaction plan — is a CONTROL. That is Activity 5.",
        ]),
    ],
    facilitator=dict(
        timing="30 minutes. 5 min brainstorm, 10 min grid and selection, 5 min standard work, "
               "10 min pilot plan, results and debrief.",
        setup="Open countermeasure-options. Keep pilot-week-results HIDDEN until learners have "
              "written their own pilot plan in Step 7 — revealing it early removes the thinking.",
        watch=[
            "Learners choosing the exciting option (the app) over the effective one. Ask which "
            "root cause it addresses — usually none that was proved.",
            "Countermeasures aimed at the symptom ('hire more staff so the queue is shorter'). "
            "Send them back to their Activity 3 shortlist.",
            "Standard work written as a paragraph of prose. It must be numbered steps with a "
            "check anyone could apply.",
        ],
        mistakes=[
            "Scoring everything 5 for impact. Force a spread — if everything is high impact, the "
            "grid tells you nothing.",
            "Picking two or three countermeasures at once. Pilot ONE, or you will not know which "
            "one worked.",
            "Reading the Thursday dip as 'the pilot failed'. It did not — it revealed that the "
            "improvement has no control on it yet.",
        ],
        debrief="Reveal pilot-week-results only after the pilot plans are written. Walk the week "
                "day by day and let the room spot Thursday themselves. Then ask what would have "
                "prevented it — and write their answers on the board as the agenda for Activity 5.",
    ),
)

# ------------------------------------------------------------------ Activity 5
LAB5 = dict(
    datasets=[
        dict(
            name="post-improvement-monitoring",
            title="Post-improvement monitoring — four weeks",
            desc="Four weeks of daily average wait times after the pilot was made permanent. "
                 "The learner uses this in Steps 1-3 to choose the control measure, set the "
                 "target and write a reaction plan that would have caught the drift.",
            headers=["Week", "Day", "Date", "Avg Wait (min)", "Restock Done Before 07:30?",
                     "Drinks Remade", "Within 8-min Target?"],
            rows=[
                [1, "Mon", "2026-06-29", 6.2, "Yes", 3, "Yes"],
                [1, "Tue", "2026-06-30", 5.9, "Yes", 2, "Yes"],
                [1, "Wed", "2026-07-01", 6.4, "Yes", 3, "Yes"],
                [1, "Thu", "2026-07-02", 6.0, "Yes", 2, "Yes"],
                [1, "Fri", "2026-07-03", 5.7, "Yes", 2, "Yes"],
                [2, "Mon", "2026-07-06", 6.1, "Yes", 3, "Yes"],
                [2, "Tue", "2026-07-07", 6.6, "Yes", 3, "Yes"],
                [2, "Wed", "2026-07-08", 6.3, "Yes", 2, "Yes"],
                [2, "Thu", "2026-07-09", 6.8, "Yes", 4, "Yes"],
                [2, "Fri", "2026-07-10", 6.2, "Yes", 3, "Yes"],
                [3, "Mon", "2026-07-13", 7.4, "No", 5, "Yes"],
                [3, "Tue", "2026-07-14", 8.9, "No", 6, "No"],
                [3, "Wed", "2026-07-15", 9.6, "No", 6, "No"],
                [3, "Thu", "2026-07-16", 10.2, "No", 7, "No"],
                [3, "Fri", "2026-07-17", 11.1, "No", 8, "No"],
                [4, "Mon", "2026-07-20", 6.5, "Yes", 3, "Yes"],
                [4, "Tue", "2026-07-21", 6.1, "Yes", 2, "Yes"],
                [4, "Wed", "2026-07-22", 5.8, "Yes", 2, "Yes"],
                [4, "Thu", "2026-07-23", 6.0, "Yes", 3, "Yes"],
                [4, "Fri", "2026-07-24", 5.9, "Yes", 2, "Yes"],
            ],
            notes="Week 3 is the drift: a new opening staff member was not shown the restock step, "
                  "the measure degraded for five days, and nobody noticed until a customer "
                  "complained on the Friday. Week 4 recovers after the SOP was pinned up and the "
                  "handover was done properly. This is the whole argument for Control in one "
                  "dataset — the learner should be able to say exactly which day a reaction plan "
                  "would have triggered.",
        ),
        dict(
            name="control-plan-example",
            title="Control plan — worked example (one row completed)",
            desc="The control plan format with a single worked row, so the learner can see the "
                 "level of specificity expected before completing their own in Step 2.",
            headers=["What We Measure", "Target", "How Often", "Who Checks", "Where Recorded",
                     "Reaction if Off Target"],
            rows=[
                ["Average customer wait, 07:30-09:00", "<= 8 min (stretch: 5 min)", "Daily",
                 "Shift supervisor", "Board at the barista station",
                 "Same day: check the restock was done; if not, do it and tell the opening staff. "
                 "Two days off target: raise at the huddle and re-brief the whole shift."],
                ["Counter milk restocked before 07:15", "", "", "", "", ""],
                ["Drinks remade per morning", "", "", "", "", ""],
                ["", "", "", "", "", ""],
            ],
            notes="Row 1 is the worked example. The learner completes rows 2-4. Note that the "
                  "reaction column says what to DO, not 'investigate' — a reaction plan that says "
                  "'escalate' is not a reaction plan.",
        ),
    ],
    templates=[
        dict(name="control-plan-template", title="Control plan (blank)",
             desc="Steps 1, 2 and 3.",
             headers=["What We Measure", "Target", "How Often", "Who Checks", "Where Recorded",
                      "Reaction if Off Target"],
             rows=[["", "", "", "", "", ""] for _ in range(4)]),
        dict(name="sop-and-huddle-template", title="SOP and daily huddle plan (blank)",
             desc="Steps 5 and 6.",
             headers=["Element", "Your entry"],
             rows=[["SOP title", ""], ["SOP owner", ""], ["SOP step 1", ""], ["SOP step 2", ""],
                   ["SOP step 3", ""], ["SOP step 4", ""], ["SOP step 5", ""],
                   ["How we know the step was done", ""],
                   ["Huddle: who attends", ""], ["Huddle: what time", ""],
                   ["Huddle: how long", ""], ["Huddle: what is reviewed", ""],
                   ["Huddle: who runs it", ""]]),
        dict(name="one-page-summary-template", title="One-page DMAIC summary (blank)",
             desc="Step 7. The whole project on one page.",
             headers=["DMAIC Phase", "What we did", "What we found / produced"],
             rows=[["DEFINE", "", ""], ["MEASURE", "", ""], ["ANALYZE", "", ""],
                   ["IMPROVE", "", ""], ["CONTROL", "", ""],
                   ["Handed over to", "", ""], ["Date of handover", ""]]),
    ],
    model=[
        ("The control measure (model)", [
            "THE ONE MEASURE: average customer wait time, 07:30-09:00, measured daily.",
            "",
            "Why this one: it is the measure the CUSTOMER experiences, it maps directly to the",
            "5-minute CTQ from Activity 1, and it moves whenever the process slips — as week 3 proves.",
            "",
            "A good secondary measure is 'counter milk restocked before 07:15 - yes/no', because",
            "it is a LEADING indicator: it goes wrong BEFORE the wait time does. In week 3 the",
            "restock failed on Monday but the wait only breached target on Tuesday. A control",
            "plan built on the leading indicator catches the problem a day earlier.",
        ]),
        ("Control plan (model)", [
            "MEASURE: Average customer wait, 07:30-09:00",
            "  Target: <= 8 min (stretch 5 min) | Frequency: daily | Owner: shift supervisor",
            "  Recorded: whiteboard at the barista station",
            "  Reaction: same day - check whether the restock was done; if not, do it now and",
            "  re-brief the opening staff. Two consecutive days off target - raise at the huddle",
            "  and re-brief the whole shift. Five days off target - reopen the improvement.",
            "",
            "MEASURE: Counter milk restocked before 07:15 (yes/no)",
            "  Target: Yes, every day | Frequency: daily | Owner: opening staff member",
            "  Recorded: signed opening checklist",
            "  Reaction: if No - restock immediately and note why; if No twice in a week, the",
            "  supervisor retrains the opening staff and checks the following morning in person.",
            "",
            "MEASURE: Drinks remade per morning",
            "  Target: <= 3 | Frequency: daily | Owner: barista",
            "  Recorded: tally on the counter check sheet",
            "  Reaction: above 3 - check the cup stickers are in use; above 5 for two days -",
            "  re-brief on reading the order back before handover.",
            "",
            "Every reaction says what to DO and who does it. 'Escalate to management' is not a",
            "reaction plan.",
        ]),
        ("Reading the monitoring data (model)", [
            "Weeks 1 and 2: wait steady at 5.7-6.8 min, restock done daily, remakes 2-4. In",
            "  control and comfortably inside the 8-minute target.",
            "Week 3: the restock is missed from Monday. Wait climbs 7.4 - 8.9 - 9.6 - 10.2 - 11.1",
            "  and remakes climb with it. Nobody notices until a customer complains on Friday.",
            "Week 4: the SOP is pinned up and the new staff member is shown the step. Wait returns",
            "  to 5.8-6.5 within a day.",
            "",
            "WHEN WOULD THE CONTROL PLAN HAVE TRIGGERED?",
            "  Monday 13 July — the LEADING indicator ('restock done before 07:15') is No. A",
            "  control plan built on it catches the drift on day one, before a single customer is",
            "  affected.",
            "  Tuesday 14 July — the wait measure breaches 8 minutes. Even a plan built only on",
            "  the lagging measure catches it on day two.",
            "  Without either, it took until Friday 17 July and a customer complaint — five days",
            "  and roughly 300 affected customers later.",
            "",
            "THE POINT: the improvement did not fail because the countermeasure was wrong. It",
            "failed because nothing was watching. That is what Control is for.",
        ]),
        ("SOP, visual board and huddle (model)", [
            "SOP — 'Counter milk restock', owned by the shift supervisor:",
            "  1. On arrival, open the back store fridge.",
            "  2. Carry 6 L dairy and 3 L oat milk to the counter fridge.",
            "  3. Fill to the marked fill line.",
            "  4. Confirm the line is reached.",
            "  5. Tick and initial 'Counter milk restocked' on the opening checklist.",
            "  DONE CHECK: the checklist is signed AND the fridge is at the fill line by 07:15.",
            "",
            "VISUAL BOARD at the barista station — a simple whiteboard showing:",
            "  * today's average wait, written up at 09:05",
            "  * a 20-day run of the daily figure, so drift is visible as a trend not a number",
            "  * the 8-minute target line drawn across it",
            "  * a green/red tick for 'restock done before 07:15'",
            "  * the reaction plan pinned beside it",
            "In week 3, five red ticks in a row would have been visible to everyone on shift.",
            "",
            "DAILY HUDDLE — 5 minutes at 09:10, at the board, run by the shift supervisor:",
            "  who: everyone on the morning shift",
            "  what: yesterday's wait vs target; was the restock done; any remakes; anything in",
            "        the way today",
            "  rule: problems are named, not blamed; anything unresolved gets an owner and a date.",
        ]),
        ("One-page summary and handover (model)", [
            "DEFINE   — VOC from 30 customer comments; CTQ 'served within 5 minutes'; problem:",
            f"           waits up to {MAX_WAIT} min against a 5-min promise over two months.",
            f"MEASURE  — {N_OBS} customers observed; average wait {AVG_WAIT} min; {PCT_OVER}% over",
            "           the promise; largest wastes Waiting and Motion; 18 mid-order milk trips.",
            f"ANALYZE  — Pareto: {VITAL_FEW[0]} and {VITAL_FEW[1]} = {VITAL_FEW_PCT}% of delays.",
            "           5 Whys root cause: counter milk restocking was never in anyone's opening",
            "           routine.",
            "IMPROVE  — Added the restock to the 07:00 opening checklist ($0). One-week pilot:",
            "           average wait 7.5 min, a 42% reduction.",
            "CONTROL  — Daily wait measure and restock check on a visual board; signed opening",
            "           checklist; SOP pinned at the station; 5-minute daily huddle; reaction plan",
            "           owned by the shift supervisor.",
            "",
            f"RESULT   — Average morning wait reduced from {AVG_WAIT} min to about 6.0 min, a",
            "           reduction of roughly 60%, at no capital cost.",
            "HANDOVER — Handed to the shift supervisor as process owner on 24 July 2026, with the",
            "           SOP, the control plan and the board. The improvement team's role ends;",
            "           the people who run the process every day now own it.",
            "",
            "STILL OPEN — the 5-minute CTQ is not yet met. Option C (open the second till at peak)",
            "           is the next countermeasure and has been logged for the supervisor.",
            "",
            "A complete summary tells the whole story: problem, cause, countermeasure, result,",
            "control, owner. The Case Study expects the same arc.",
        ]),
    ],
    facilitator=dict(
        timing="30 minutes. 5 min choosing the measure, 10 min control plan and reaction plan, "
               "5 min board and SOP, 10 min one-page summary and course debrief.",
        setup="Open post-improvement-monitoring and control-plan-example. Project the week-3 rows "
              "and let the room find the drift before you name it.",
        watch=[
            "Reaction plans that say 'investigate' or 'escalate'. Ask: what does the supervisor "
            "physically DO tomorrow morning? A reaction plan is an instruction, not an intention.",
            "Control plans with no owner, or with 'the team' as the owner. One named role.",
            "Learners choosing five control measures. One or two, watched properly, beats five "
            "that nobody looks at.",
        ],
        mistakes=[
            "Treating Control as paperwork filed after the project. It is the only phase that "
            "makes the other four worth doing.",
            "Missing the leading-indicator point: the restock check moves before the wait time "
            "does, so it buys the team a day.",
            "Forgetting the handover. A White Belt project that stays with the improvement team "
            "has not finished — name the process owner and the date.",
        ],
        debrief="Close the course with the week-3 story. Ask what it cost — five days, roughly "
                "300 customers, and a public complaint — and what would have prevented it: one "
                "tick on a checklist and one glance at a board. Then have each learner read out "
                "the one-line RESULT from their summary. That summary is their revision sheet for "
                "the Case Study.",
    ),
)

LAB_DATA = {1: LAB1, 2: LAB2, 3: LAB3, 4: LAB4, 5: LAB5}
