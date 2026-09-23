"""
Activity 4 — IMPROVE phase. Continues the BrewBean Cafe running scenario.

Awareness depth: the learner brainstorms and screens ideas on a simple
impact/effort grid. No weighted solution-selection matrix, no FMEA, no DOE —
those belong at Yellow Belt and above.
"""

DOMAIN4 = [
    dict(
        num=4, topic=4,
        title="Improve — Choose and Pilot a Countermeasure",
        objective="Describe improvement actions that address the identified cause (A5, K2).",
        desc="A cause is only worth finding if something changes because of it. Take the root "
             "causes you shortlisted in Activity 3, generate countermeasures against them, and pick "
             "one that is small enough to try next week. The discipline here is to solve the "
             "CAUSE you proved, not the symptom you started with.",
        build="A brainstormed countermeasure list, an impact/effort grid, one selected countermeasure and a simple pilot plan.",
        services="Brainstorming, impact/effort screening, 5S, mistake proofing (Poka-Yoke), standard work, piloting",
        steps=[
            ("Write your top root cause from Activity 3 at the top of templates/countermeasure-brainstorm-template.csv — every idea must address THIS cause.", ""),
            ("Brainstorm at least six countermeasures without judging any of them yet, then compare your list with data/countermeasure-options.csv, which holds the twelve the team generated.", ""),
            ("Check whether 5S would help: is anything at the counter hard to find, out of place or untidy?", ""),
            ("Check whether mistake proofing would help: could the wrong order be made impossible rather than merely discouraged?", ""),
            ("Using the Impact and Effort scores in data/countermeasure-options.csv, plot every idea on templates/impact-effort-grid-template.csv and pick ONE from the high-impact, low-effort corner.", ""),
            ("In templates/standard-work-and-pilot-template.csv, write the improved method as standard work — short numbered steps with an unambiguous done/not-done check.", ""),
            ("Complete the pilot plan rows of the same template: what changes, who runs it, what you will measure, the baseline to beat, and how you will know it worked. THEN open data/pilot-week-results.csv and compare what actually happened — pay close attention to Thursday.", ""),
        ],
        duration='30 minutes',
        case_scenario=[
            'The team has proved its root cause and has a week to try something. The owner has agreed to a pilot but has made clear there is no budget for equipment this quarter.',
            'Twelve countermeasures were generated at the last team meeting, ranging from adding the counter milk restock to the opening checklist through to installing a mobile pre-order app. They vary enormously in cost, effort and risk, and the team has limited time and no capital.',
            'A cause is only worth finding if something changes because of it. Your job is to choose one countermeasure small enough to try next week, write the new method down so anyone on shift could follow it, and plan how you will know whether it worked.',
        ],
        discussion_prompts=[
            'Which countermeasures address the proven root cause, and which quietly address the symptom instead?',
            'What does the impact/effort grid tell you that a simple list of ideas does not?',
            'Why pilot only ONE countermeasure rather than several at once?',
            'Looking at the pilot week results — what happened on Thursday, and what does it reveal?',
        ],
        reflection_points=[
            'Was your instinct to pick the most impressive solution or the most effective one?',
            'Would your standard work be followable by someone on their first day, with no explanation?',
            'The pilot worked on four days of five. Is that a success or a failure, and why?',
        ],
        debrief_check='Every group can show a countermeasure that addresses the Activity 3 root cause, a completed impact/effort grid with one selection, numbered standard work with a done/not-done check, and a pilot plan naming a measure, an owner and a review date.',
        test="Your selected countermeasure clearly addresses the root cause from Activity 3 (not the symptom), and your pilot plan names a measure, an owner and a review date.",
    ),
]
