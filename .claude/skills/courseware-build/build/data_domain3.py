"""
Activity 3 — ANALYZE phase. Continues the BrewBean Cafe running scenario.

Awareness depth: the learner uses 5 Whys and a Fishbone and reads a Pareto chart
that is supplied. They are not asked to run hypothesis tests or regression.
"""
from lab_data import AVG_WAIT

DOMAIN3 = [
    dict(
        num=3, topic=3,
        title="Analyze — Find the Root Cause",
        objective="Identify likely causes using 5 Whys and Fishbone analysis (A3, K2).",
        desc="You now know WHERE the delay happens. This activity asks WHY it happens. Most teams "
             "jump straight from a symptom to a solution and end up fixing the wrong thing — "
             "the queue is long, so hire more staff — when the real cause was something else "
             "entirely. Here you drill past the symptom to a cause you can actually act on.",
        build="A completed 5 Whys chain, a Fishbone diagram with causes sorted by category, and a shortlist of likely root causes.",
        services="Symptom vs cause, 5 Whys, Fishbone (5M) diagram, Pareto chart, common vs special cause variation",
        steps=[
            (f"Write the symptom from your Activity 2 baseline at the top of templates/5-whys-template.csv (e.g. 'customers wait an average of {AVG_WAIT} minutes against a 5-minute promise').", ""),
            ("Ask 'why does that happen?' down the template, each answer becoming the next question. Stop when you reach a PROCESS the team can act on — never at a person.", ""),
            ("Open templates/fishbone-template.csv and write the problem in the head of the fish.", ""),
            ("Brainstorm possible causes onto the five bones — Manpower, Method, Machine, Material, Measurement — then check them against data/cause-evidence-sheet.csv to see which ones the data actually supports.", ""),
            ("Open data/delay-reason-pareto-data.csv — the delay reasons from the Activity 2 log, counted and ranked. Read the Cumulative % column and state which few causes account for most of the problem.", ""),
            ("Using the last column of data/cause-evidence-sheet.csv, decide for each cause whether it is common cause (built into the process) or special cause (a one-off event).", ""),
            ("In templates/root-cause-shortlist-template.csv, shortlist the two or three causes best supported by evidence — not by opinion.", ""),
        ],
        duration='30 minutes',
        case_scenario=[
            'The team now knows WHERE the delay happens. This activity asks WHY it happens.',
            'At the last team meeting two theories were argued loudly. The owner still wants to buy a second machine. The shift supervisor wants to add a staff member to the morning rota. Both are solutions to a symptom nobody has yet explained: the queue is long, so add capacity. Neither theory has been tested against the observation data.',
            'Most improvement teams jump straight from a symptom to a solution and end up fixing the wrong thing at considerable cost. Your job is to drill past the symptom to a cause the team can actually act on — and to be able to show the evidence for it.',
        ],
        discussion_prompts=[
            "Compare your 5 Whys chain with another group's. You started from the same symptom — did you reach the same root cause, and what does that tell you?",
            'Which causes on your Fishbone have real evidence behind them, and which are assumptions the team simply believes?',
            'The Pareto ranks causes by frequency. When might the most frequent cause NOT be the most important one?',
            'Why does it matter whether a cause is common cause or special cause?',
        ],
        reflection_points=[
            "Did your chain stop at a person at any point? What happened when you asked 'why' again?",
            "Which of the owner's or supervisor's two theories survives contact with the data?",
            'What would it have cost the cafe to act on the loudest opinion instead of the evidence?',
        ],
        debrief_check='Every group can show a 5 Whys chain ending in an actionable process cause, a Fishbone with causes sorted into the five categories, and two or three shortlisted causes each backed by a stated observation.',
        test="Your 5 Whys chain ends in something the team can actually act on, every Fishbone cause sits under one of the five categories, and each shortlisted cause is backed by an observation, not an opinion.",
    ),
]
