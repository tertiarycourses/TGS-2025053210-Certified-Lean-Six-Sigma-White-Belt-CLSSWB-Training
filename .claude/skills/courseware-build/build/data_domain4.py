"""
Lab 4 — IMPROVE phase. Continues the BrewBean Cafe running scenario.

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
             "causes you shortlisted in Lab 3, generate countermeasures against them, and pick "
             "one that is small enough to try next week. The discipline here is to solve the "
             "CAUSE you proved, not the symptom you started with.",
        build="A brainstormed countermeasure list, an impact/effort grid, one selected countermeasure and a simple pilot plan.",
        services="Brainstorming, impact/effort screening, 5S, mistake proofing (Poka-Yoke), standard work, piloting",
        steps=[
            ("Write your top root cause from Lab 3 at the top of the sheet — every idea must address THIS cause.", ""),
            ("Brainstorm at least six countermeasures without judging any of them yet.", ""),
            ("Check whether 5S would help: is anything at the counter hard to find, out of place or untidy?", ""),
            ("Check whether mistake proofing would help: could the wrong order be made impossible rather than merely discouraged?", ""),
            ("Plot every idea on the impact/effort grid and pick one from the high-impact, low-effort corner.", ""),
            ("Write the improved method as standard work — short numbered steps anyone on shift could follow.", ""),
            ("Write a one-week pilot plan: what changes, who runs it, what you will measure, and how you will know it worked.", ""),
        ],
        test="Your selected countermeasure clearly addresses the root cause from Lab 3 (not the symptom), and your pilot plan names a measure, an owner and a review date.",
    ),
]
