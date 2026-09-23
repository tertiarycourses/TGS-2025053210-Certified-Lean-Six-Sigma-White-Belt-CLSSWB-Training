"""
Lab 5 — CONTROL phase. Closes the BrewBean Cafe running scenario.

Awareness depth: the learner completes a control plan template and a one-page
summary. No SPC control charts with calculated limits, no capability indices —
those belong at Yellow Belt and above.
"""

DOMAIN5 = [
    dict(
        num=5, topic=5,
        title="Control — Hold the Gain and Hand Over",
        objective="Describe the control actions that sustain an improvement (A5, K2).",
        desc="Most improvements work for a fortnight and then quietly disappear. Control is what "
             "stops that happening. Close the BrewBean Cafe story by deciding what will be "
             "measured from now on, who owns it, what happens when it slips, and how the "
             "improved process is handed back to the people who run it every day.",
        build="A completed control plan, a visual management board sketch, and a one-page summary of the whole DMAIC story.",
        services="Control plan, visual management, SOPs, team huddles, handover, one-page summary",
        steps=[
            ("Open data/post-improvement-monitoring.csv — four weeks of daily figures after the pilot was made permanent. Choose the ONE measure that tells you the improvement is still working.", ""),
            ("Look at data/control-plan-example.csv for the worked first row, then complete templates/control-plan-template.csv: measure, target, how often it is checked, where it is recorded and who owns it.", ""),
            ("Write the reaction plan — the exact steps to take when the measure misses target. Then find week 3 in the monitoring data and state which day your plan would have triggered on.", ""),
            ("Sketch a simple visual board that would have made the week-3 drift visible to the whole shift on day one.", ""),
            ("In templates/sop-and-huddle-template.csv, turn your Lab 4 standard work into a short SOP the cafe could actually pin up.", ""),
            ("Complete the huddle rows of the same template: who attends, what is reviewed, who runs it and how long it lasts.", ""),
            ("Using templates/one-page-summary-template.csv, summarise the whole project — problem, cause, countermeasure, result and control — and name who you hand it over to and when.", ""),
        ],
        test="Your control plan names a measure, a target, a frequency and an owner; your reaction plan says what to DO when it slips; and your one-page summary tells the complete DMAIC story from problem to handover.",
    ),
]
