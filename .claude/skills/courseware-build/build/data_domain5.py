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
            ("Choose the ONE measure that tells you the improvement is still working (e.g. average wait time at 8:00am).", ""),
            ("Complete the control plan template: measure, target, how often it is checked, and who owns it.", ""),
            ("Write the reaction plan — the exact steps to take when the measure misses target.", ""),
            ("Sketch a simple visual board that would make this measure visible to the whole shift.", ""),
            ("Turn your Lab 4 standard work into a short SOP the cafe could actually pin up.", ""),
            ("Plan a five-minute daily huddle: who attends, what is reviewed and how long it lasts.", ""),
            ("Summarise the whole project on one page — problem, cause, countermeasure, result and control — and name who you hand it over to.", ""),
        ],
        test="Your control plan names a measure, a target, a frequency and an owner; your reaction plan says what to DO when it slips; and your one-page summary tells the complete DMAIC story from problem to handover.",
    ),
]
