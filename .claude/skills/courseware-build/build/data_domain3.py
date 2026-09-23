"""
Lab 3 — ANALYZE phase. Continues the BrewBean Cafe running scenario.

Awareness depth: the learner uses 5 Whys and a Fishbone and reads a Pareto chart
that is supplied. They are not asked to run hypothesis tests or regression.
"""
from lab_data import AVG_WAIT

DOMAIN3 = [
    dict(
        num=3, topic=3,
        title="Analyze — Find the Root Cause",
        objective="Identify likely causes using 5 Whys and Fishbone analysis (A3, K2).",
        desc="You now know WHERE the delay happens. This lab asks WHY it happens. Most teams "
             "jump straight from a symptom to a solution and end up fixing the wrong thing — "
             "the queue is long, so hire more staff — when the real cause was something else "
             "entirely. Here you drill past the symptom to a cause you can actually act on.",
        build="A completed 5 Whys chain, a Fishbone diagram with causes sorted by category, and a shortlist of likely root causes.",
        services="Symptom vs cause, 5 Whys, Fishbone (5M) diagram, Pareto chart, common vs special cause variation",
        steps=[
            (f"Write the symptom from your Lab 2 baseline at the top of templates/5-whys-template.csv (e.g. 'customers wait an average of {AVG_WAIT} minutes against a 5-minute promise').", ""),
            ("Ask 'why does that happen?' down the template, each answer becoming the next question. Stop when you reach a PROCESS the team can act on — never at a person.", ""),
            ("Open templates/fishbone-template.csv and write the problem in the head of the fish.", ""),
            ("Brainstorm possible causes onto the five bones — Manpower, Method, Machine, Material, Measurement — then check them against data/cause-evidence-sheet.csv to see which ones the data actually supports.", ""),
            ("Open data/delay-reason-pareto-data.csv — the delay reasons from the Lab 2 log, counted and ranked. Read the Cumulative % column and state which few causes account for most of the problem.", ""),
            ("Using the last column of data/cause-evidence-sheet.csv, decide for each cause whether it is common cause (built into the process) or special cause (a one-off event).", ""),
            ("In templates/root-cause-shortlist-template.csv, shortlist the two or three causes best supported by evidence — not by opinion.", ""),
        ],
        test="Your 5 Whys chain ends in something the team can actually act on, every Fishbone cause sits under one of the five categories, and each shortlisted cause is backed by an observation, not an opinion.",
    ),
]
