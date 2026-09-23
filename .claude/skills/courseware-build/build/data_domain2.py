"""
Activity 2 — MEASURE phase. Continues the BrewBean Cafe running scenario.

Awareness depth: the learner maps a process and tallies waste using supplied
templates. No sigma level, no DPMO, no MSA — those are Yellow Belt and above.
"""

DOMAIN2 = [
    dict(
        num=2, topic=2,
        title="Measure — Map the Process and Spot the Waste",
        objective="Describe how the process runs and identify the eight wastes in it (A4, K2).",
        desc="You cannot improve what you cannot see. Walk the BrewBean Cafe morning rush from "
             "the customer joining the queue to the drink being handed over, draw it as it "
             "really happens, and tally where time and effort are being lost. This is the "
             "phase that turns opinions about the problem into facts about the problem.",
        build="A SIPOC overview, a step-by-step process map with timings, and a completed waste tally sheet.",
        services="SIPOC, process mapping, types of data, check sheets, the eight wastes (DOWNTIME)",
        steps=[
            ("Agree the start and stop points of the process — start: customer joins the queue; stop: customer receives the drink.", ""),
            ("Complete templates/sipoc-template.csv: Suppliers, Inputs, Process (5-7 steps only), Outputs, Customers.", ""),
            ("Open data/process-step-timings.csv. Copy the 15 steps into templates/process-map-template.csv with their observed times.", ""),
            ("Mark each step VA or NVA in the template — the test is whether the customer would pay extra for THAT step — and write one line saying why.", ""),
            ("Look at the columns in data/morning-rush-observation-log.csv and classify each: which figures are discrete (counted) and which are continuous (measured)?", ""),
            ("Open data/downtime-waste-tally.csv — three rows are completed as worked examples. Using the observation log and the step timings as your evidence, complete the remaining five rows in templates/downtime-tally-template.csv.", ""),
            ("Identify which single waste type you tallied most often and at which process step, then write down the baseline figures (average wait, longest wait, % over the 5-minute promise, drinks remade) — Activity 5 measures the improvement against them.", ""),
        ],
        duration='30 minutes',
        case_scenario=[
            'The team now has an agreed problem statement, but still only opinions about where the time goes. Management wants to act immediately; the team has persuaded them to spend one morning measuring first.',
            'The improvement team spent one weekday morning observing the 7:30am-9:00am rush with a stopwatch and a check sheet. They timed 60 customers end to end, recorded what each one ordered, how long they waited, whether the drink had to be remade, and what was visibly holding things up. They also timed every step of the process itself.',
            'Your job is to turn that raw observation into a picture of the process as it really runs — not as the staff handbook describes it — and to find where the time and effort are actually being lost.',
        ],
        discussion_prompts=[
            'Looking at your process map, what proportion of the total time is genuinely value-adding — and does that surprise you?',
            'Which single step would you attack first, and is that step a symptom or a cause?',
            'Which waste types came out at zero, and what evidence lets you say so with confidence?',
            'Why does the team need to agree what is recorded, who records it and when, BEFORE collection starts?',
        ],
        reflection_points=[
            'Was the step you assumed was the bottleneck actually the one the data pointed to?',
            'How would the map differ if you had asked staff to describe the process instead of observing it?',
            'Which of these wastes do you recognise in your own workplace?',
        ],
        debrief_check='Every group can show a SIPOC with all five columns filled, a process map with every step timed and judged VA or NVA, a complete DOWNTIME tally tied to evidence, and the written baseline figures.',
        test="Your SIPOC has all five columns filled, every process step has a time, and every waste on your tally sheet is tagged to one of the eight DOWNTIME types.",
    ),
]
