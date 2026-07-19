"""
Lab 3 — ANALYZE phase. Continues the BrewBean Cafe running scenario.

Awareness depth: the learner uses 5 Whys and a Fishbone and reads a Pareto chart
that is supplied. They are not asked to run hypothesis tests or regression.
"""

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
            ("Write the symptom from your Lab 2 findings at the top of the 5 Whys template (e.g. 'customers wait 15 minutes').", ""),
            ("Ask 'why does that happen?' five times, each answer becoming the next question. Stop when you reach something you can act on.", ""),
            ("Draw the Fishbone diagram and write the problem in the head of the fish.", ""),
            ("Brainstorm possible causes onto the five bones: Manpower, Method, Machine, Material and Measurement.", ""),
            ("Read the supplied Pareto chart of BrewBean complaint types and state which few causes account for most of the problem.", ""),
            ("Decide for each shortlisted cause whether it is common cause (happens every day) or special cause (a one-off event).", ""),
            ("Shortlist the two or three causes best supported by the data you collected in Lab 2.", ""),
        ],
        test="Your 5 Whys chain ends in something the team can actually act on, every Fishbone cause sits under one of the five categories, and each shortlisted cause is backed by an observation, not an opinion.",
    ),
]
