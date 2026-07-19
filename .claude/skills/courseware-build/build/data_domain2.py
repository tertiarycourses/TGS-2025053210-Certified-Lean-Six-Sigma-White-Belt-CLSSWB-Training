"""
Lab 2 — MEASURE phase. Continues the BrewBean Cafe running scenario.

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
            ("Complete the SIPOC template: Suppliers, Inputs, Process (5-7 steps only), Outputs, Customers.", ""),
            ("List the process steps in order and write the observed time next to each one.", ""),
            ("Mark each step as value-adding (the customer would pay for it) or not value-adding.", ""),
            ("Classify the data you collected: which figures are discrete (counted) and which are continuous (measured)?", ""),
            ("Walk the process again with the DOWNTIME check sheet and tally every waste you observe against its type.", ""),
            ("Identify which single waste type you tallied most often, and which process step it happens at.", ""),
        ],
        test="Your SIPOC has all five columns filled, every process step has a time, and every waste on your tally sheet is tagged to one of the eight DOWNTIME types.",
    ),
]
