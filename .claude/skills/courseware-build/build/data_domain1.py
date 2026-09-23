"""
Lab 1 — DEFINE phase.

The White Belt has exactly FIVE labs, one per DMAIC phase. All five follow ONE
running scenario — the BrewBean Cafe morning rush — so the learner carries a
single improvement story from Define through to Control across the day.

Awareness depth: the learner DESCRIBES and IDENTIFIES using supplied templates.
They are not asked to lead a project, build a charter from nothing, or compute
sigma levels (all of which belong at Yellow Belt and above).
"""

SCENARIO = (
    "BrewBean Cafe — morning rush. Customers queue up to 15 minutes between "
    "7:30am and 9:00am, orders are sometimes made wrong, and regulars have begun "
    "complaining online. The cafe manager has asked a small improvement team to "
    "look into it. You are the White Belt team member supporting that team."
)

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Define — Customer Requirements and the Problem Statement",
        objective="Identify customer requirements and write a clear problem statement (A1, A2).",
        desc="Start the BrewBean Cafe improvement the way every real project starts: find out "
             "what the customer actually wants, turn that into something measurable, and state "
             "the problem clearly enough that everyone agrees on it. The most common reason "
             "improvement projects fail is that the team never agreed what the problem was.",
        build="A VOC-to-CTQ table, a written problem statement, a SMART goal and a simple scope table.",
        services="Voice of the Customer, CTQ, problem statement, SMART goal, project scope",
        steps=[
            ("Read the BrewBean Cafe scenario, then open data/voc-raw-customer-feedback.csv (or the workbook) and read all 30 pieces of customer feedback. Underline every complaint you can find.", ""),
            ("Using templates/voc-to-ctq-template.csv, write down five Voice of the Customer statements in the customer's OWN words, quoted from the Verbatim Comment column — do not paraphrase them yet.", ""),
            ("Turn each VOC statement into a measurable CTQ requirement in the same template — every CTQ must carry a number AND a unit (e.g. 'served within 5 minutes').", ""),
            ("In templates/problem-statement-and-scope-template.csv, write the problem statement: what is wrong, where, since when, and how big. Do NOT write a solution.", ""),
            ("Check your problem statement against the SMART test and rewrite the goal so it is Specific, Measurable, Achievable, Relevant and Time-bound.", ""),
            ("Fill the in-scope / out-of-scope rows at the bottom of the same template so the team knows where the project stops.", ""),
        ],
        test="Every CTQ has a number and a unit, your problem statement contains no solution, and your goal has a metric, a baseline, a target and a date.",
    ),
]
