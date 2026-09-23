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
        duration='30 minutes',
        case_scenario=[
            'The pilot worked. The countermeasure was made permanent and the improvement team was stood down. Four weeks later the team has been asked to review how it is holding up.',
            'The daily figures have been collected throughout. Weeks 1 and 2 look good. In week 3 something goes wrong: a new opening staff member was never shown the restock step, the measure degrades for five consecutive days, and nobody notices until a customer complains publicly on the Friday. Week 4 recovers once the SOP is pinned up and the handover is done properly.',
            'Most improvements work for a fortnight and then quietly disappear. Your job is to close the BrewBean Cafe story by deciding what will be measured from now on, who owns it, what happens when it slips, and how the improved process is handed back to the people who run it every day.',
        ],
        discussion_prompts=[
            'Looking at the monitoring data, which day would a good control plan have triggered on — and how many customers were affected before anyone noticed?',
            'Which of your measures is a leading indicator and which is lagging? Why does the difference matter here?',
            'What makes a reaction plan actionable rather than just a statement of intent?',
            'Who should own this process now that the improvement team has disbanded, and why that person?',
        ],
        reflection_points=[
            'The countermeasure was correct and the improvement still decayed. What does that tell you about the Control phase?',
            'What would week 3 have looked like if the visual board had already been in place?',
            'Which improvement in your own workplace has quietly drifted back, and what control was missing?',
        ],
        debrief_check='Every group can show a control plan naming a measure, target, frequency and a single named owner; a reaction plan that says what to DO; and a one-page summary telling the complete DMAIC story from problem to named handover.',
        test="Your control plan names a measure, a target, a frequency and an owner; your reaction plan says what to DO when it slips; and your one-page summary tells the complete DMAIC story from problem to handover.",
    ),
]
