#!/usr/bin/env python3
"""Generate the labs/ tree from the same single source (course_data +
data_domainN + lab_data) that drives the PPT, LP and LG, so the labs can never
drift out of alignment with the rest of the courseware.

EACH LAB IS ITS OWN FOLDER:

    labs/README.md                    index
    labs/tools.md                     toolkit, formulas, DOWNTIME reference
    labs/lab-01-<slug>/
        README.md                     the lab worksheet
        data/                         mock datasets (.csv) + data dictionary
        data/lab-01-workbook.xlsx     every dataset + template, one per tab
        templates/                    blank worksheets (.csv)
        model-answer.md               worked model answer
        facilitator-notes.md          trainer-facing notes

The datasets, templates, model answers and facilitator notes all come from
lab_data.py and are written by build_lab_pack.py.
"""
import os
import re
import sys
import glob
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
from build_lab_pack import build_pack
from lab_data import LAB_DATA

ACT = sorted(DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5, key=lambda a: a["num"])
TOPICS = {t["num"]: t for t in C.TOPICS}


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
LABS = os.path.join(REPO, "labs")

TOOLS = {
    "5whys": ("5 Whys", "https://alfredang.github.io/5whys/"),
    "fishbone": ("Fishbone Diagram", "https://alfredang.github.io/fishbone/"),
    "pareto": ("Pareto Chart (collaborative)", "https://alfredang.github.io/paretochart/"),
    "novaspc": ("NovaSPC", "https://alfredang.github.io/novaspc/"),
}

SCENARIO = (
    "BrewBean Cafe is a busy coffee shop serving mainly office workers on their way to work. During the "
    "7:30am-9:00am morning rush customers queue for up to 15 minutes against a 5-minute service promise, "
    "some drinks are made wrong and have to be remade, and online complaints have been rising. "
    "Management has formed a small improvement team and you have joined it as the White Belt member, "
    "supporting the team rather than leading the project."
)


def slug(title):
    t = title.replace("Elective — ", "")
    t = re.sub(r"[^a-zA-Z0-9 ]", "", t).lower()
    return "-".join(t.split())[:60]


def folder_name(a):
    """The per-lab folder, e.g. lab-01-define-customer-requirements-..."""
    return f"lab-{a['num']:02d}-{slug(a['title'])}"


def lab_md(a):
    kind = "Elective" if a.get("elective") else "Core"
    title = a["title"].replace("Elective — ", "")
    tp = TOPICS[a["topic"]]
    phase = tp["phase"]
    out = []
    out.append(f"# Lab {a['num']} — {title}")
    out.append("")
    out.append(f"**DMAIC phase:** {phase}  |  **Lab type:** {kind}  |  "
               f"**Course:** {C.TITLE} ({C.COURSE_CODE})")
    out.append("")
    if a.get("elective"):
        out.append("> **Elective lab.** Complete this lab if time allows during class, or afterwards as "
                   "additional practice. It extends the same BrewBean Cafe scenario used by the "
                   "core labs.")
        out.append("")
    out.append("## Objective")
    out.append("")
    out.append(a["objective"])
    out.append("")
    out.append("## Scenario")
    out.append("")
    out.append(SCENARIO)
    out.append("")
    out.append("## What you will build")
    out.append("")
    out.append(a["build"])
    out.append("")
    out.append(f"**Tools and techniques:** {a['services']}")
    out.append("")

    # ---- the data pack that ships in this lab folder ----
    pack = LAB_DATA.get(a["num"])
    if pack:
        out.append("## Your data pack")
        out.append("")
        out.append("Everything you need is in this folder. The data is mock data built for the "
                   "BrewBean Cafe scenario — it is realistic and internally consistent across all "
                   "five labs, so what you find here carries into the next lab.")
        out.append("")
        out.append("### Data to work from — `data/`")
        out.append("")
        out.append("| File | What it is |")
        out.append("|------|------------|")
        for d in pack.get("datasets", []):
            out.append(f"| [`{d['name']}.csv`](data/{d['name']}.csv) | {d['title']} "
                       f"({len(d['rows'])} rows) |")
        xl = f"lab-{a['num']:02d}-workbook.xlsx"
        out.append(f"| [`{xl}`](data/{xl}) | **Excel workbook** — every dataset *and* every blank "
                   f"template below, one per tab |")
        out.append("")
        if pack.get("templates"):
            out.append("### Blank worksheets to fill in — `templates/`")
            out.append("")
            out.append("| File | What you fill in |")
            out.append("|------|------------------|")
            for t in pack["templates"]:
                out.append(f"| [`{t['name']}.csv`](templates/{t['name']}.csv) | {t['title']} — "
                           f"{t['desc']} |")
            out.append("")
        out.append("> **Tip:** open the Excel workbook if you want everything in one window with "
                   "the templates ready to type into. Use the CSVs if you prefer Google Sheets, "
                   "LibreOffice or a plain text editor.")
        out.append("")
        out.append("See [`data/README.md`](data/README.md) for the data dictionary — what every "
                   "column means and how the figures were collected.")
        out.append("")
    # any tool URLs used by this lab
    used = []
    for _, cmd in a["steps"]:
        if cmd.startswith("http"):
            for key, (name, url) in TOOLS.items():
                if url == cmd and name not in [u[0] for u in used]:
                    used.append((name, url))
    if used:
        out.append("### Online tools used in this lab")
        out.append("")
        for name, url in used:
            out.append(f"- **{name}** — {url}")
        out.append("")
    out.append("## Steps")
    out.append("")
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        out.append(f"### Step {i}")
        out.append("")
        out.append(instr)
        if cmd:
            out.append("")
            if cmd.startswith("http"):
                out.append(f"Open the tool: <{cmd}>")
            else:
                out.append("```")
                out.append(cmd)
                out.append("```")
        out.append("")
    out.append("## Check your work")
    out.append("")
    out.append(a["test"])
    out.append("")
    out.append("## Deliverable")
    out.append("")
    out.append(f"Save your output — it forms part of your BrewBean Cafe improvement package and is your "
               f"revision material for the assessment.")
    out.append("")
    if pack and pack.get("model"):
        out.append("## Compare your answer")
        out.append("")
        out.append("Once you have attempted the lab, compare your thinking against "
                   "[`model-answer.md`](model-answer.md). There is rarely one right answer in "
                   "Lean Six Sigma — what matters is whether your reasoning is supported by the "
                   "data in front of you.")
        out.append("")
    out.append("---")
    out.append("")
    out.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · "
               f"© 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out)


def readme_md():
    out = []
    out.append(f"# Labs — {C.TITLE}")
    out.append("")
    out.append(f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**")
    out.append("")
    out.append("These labs follow the DMAIC roadmap end to end. Every lab builds on the same BrewBean Cafe "
               "morning rush scenario, so your outputs accumulate into one complete improvement package.")
    out.append("")
    out.append("## Lab types")
    out.append("")
    out.append("- **Core** — completed by everyone; maps directly to the assessment.")
    out.append("- **Elective** — additional practice with further Lean Six Sigma tools; run when time "
               "allows or after the course.")
    out.append("")
    out.append("## Lab index")
    out.append("")
    out.append("Each lab is a self-contained folder: the worksheet, its mock data (CSV + Excel), "
               "blank templates to fill in, a worked model answer and trainer notes.")
    out.append("")
    out.append("| # | Lab | DMAIC phase | Type | Data pack |")
    out.append("|---|-----|-------------|------|-----------|")
    files = {}
    for a in ACT:
        fd = folder_name(a)
        files[a["num"]] = fd
        kind = "Elective" if a.get("elective") else "Core"
        title = a["title"].replace("Elective — ", "")
        pack = LAB_DATA.get(a["num"], {})
        nds = len(pack.get("datasets", []))
        ntp = len(pack.get("templates", []))
        blurb = f"{nds} dataset{'s' if nds != 1 else ''} + {ntp} template{'s' if ntp != 1 else ''}" \
            if pack else "—"
        out.append(f"| {a['num']} | [{title}]({fd}/README.md) | {TOPICS[a['topic']]['phase']} | "
                   f"{kind} | [{blurb}]({fd}/data/) |")
    out.append("")
    out.append("## What is in each lab folder")
    out.append("")
    out.append("| Item | What it is |")
    out.append("|------|------------|")
    out.append("| `README.md` | The lab worksheet — objective, scenario, steps and the check |")
    out.append("| `data/` | The mock datasets as `.csv`, plus one `.xlsx` workbook holding every "
               "dataset and template on its own tab |")
    out.append("| `data/README.md` | Data dictionary — what each column means |")
    out.append("| `templates/` | Blank worksheets to fill in, as `.csv` |")
    out.append("| `model-answer.md` | The worked model answer — read it *after* you attempt the lab |")
    out.append("| `facilitator-notes.md` | Trainer copy: timing, what to watch for, common "
               "mistakes, debrief |")
    out.append("")
    out.append("## About the data")
    out.append("")
    out.append("Every figure is **mock data** built for training. It is internally consistent "
               "across all five labs:")
    out.append("")
    out.append("- The Lab 2 observation log is the evidence base for the Lab 3 Pareto.")
    out.append("- The Lab 3 root cause is what the Lab 4 countermeasure addresses.")
    out.append("- The Lab 4 pilot results carry into the Lab 5 monitoring data.")
    out.append("")
    out.append("So the numbers you quote in one lab still hold in the next, and the whole story "
               "reconciles at the end.")
    out.append("")
    out.append("## The interactive toolkit")
    out.append("")
    out.append("See [tools.md](tools.md) for the browser-based problem-solving tools used in the labs.")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*© 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out), files


def tools_md():
    out = []
    out.append("# Lean Six Sigma Toolkit")
    out.append("")
    out.append(f"*{C.TITLE} · {C.COURSE_CODE}*")
    out.append("")
    out.append("## Interactive online tools")
    out.append("")
    out.append("These browser-based tools are used during the labs. No installation or licence needed.")
    out.append("")
    out.append("| Tool | What it does | Used in |")
    out.append("|------|--------------|---------|")
    out.append("| [5 Whys](https://alfredang.github.io/5whys/) | Build and share a 5 Whys root-cause chain | Lab 8 |")
    out.append("| [Fishbone Diagram](https://alfredang.github.io/fishbone/) | Build an Ishikawa cause-and-effect diagram | Lab 8 |")
    out.append("| [Pareto Chart](https://alfredang.github.io/paretochart/) | Collaborative session: the team brainstorms and votes, and the Pareto chart builds itself live | Lab 7 |")
    out.append("| [NovaSPC](https://alfredang.github.io/novaspc/) | Run charts, SPC charts (c, u, np, p, X-mR, X̄-R, X̄-s) and process capability from your own CSV | Labs 7, 10 |")
    out.append("")
    out.append("### Using the collaborative Pareto tool")
    out.append("")
    out.append("1. One team member creates a session and shares the access code.")
    out.append("2. Everyone else joins the session using that code.")
    out.append("3. The team brainstorms candidate causes into the session.")
    out.append("4. Each member votes on the causes that matter most.")
    out.append("5. The live Pareto chart reveals the vital few to act on.")
    out.append("")
    out.append("## Templates you will produce")
    out.append("")
    for a in ACT:
        title = a["title"].replace("Elective — ", "")
        out.append(f"- **Lab {a['num']} — {title}:** {a['build']}")
    out.append("")
    out.append("## Formula quick reference")
    out.append("")
    out.append("| Metric | Formula |")
    out.append("|--------|---------|")
    out.append("| Yield | (Good units / Total units) × 100 |")
    out.append("| DPU | Defects / Units |")
    out.append("| DPO | Defects / (Units × Opportunities per unit) |")
    out.append("| DPMO | DPO × 1,000,000 |")
    out.append("| First Pass Yield (FPY) | Units passing with no rework / Units started |")
    out.append("| Rolled Throughput Yield (RTY) | FPY₁ × FPY₂ × … × FPYₙ |")
    out.append("| Process Cycle Efficiency | Value-added time / Total lead time |")
    out.append("| Takt time | Available working time / Customer demand |")
    out.append("")
    out.append("### Sigma level reference")
    out.append("")
    out.append("| Sigma | DPMO | Yield |")
    out.append("|-------|------|-------|")
    for s, d, y in [("1σ", "690,000", "31%"), ("2σ", "308,000", "69%"), ("3σ", "66,800", "93.3%"),
                    ("4σ", "6,210", "99.38%"), ("5σ", "233", "99.977%"), ("6σ", "3.4", "99.99966%")]:
        out.append(f"| {s} | {d} | {y} |")
    out.append("")
    out.append("## The eight wastes — DOWNTIME")
    out.append("")
    for letter, name, ex in [
        ("D", "Defects", "Wrong ticket category; work that must be redone"),
        ("O", "Overproduction", "Reports nobody reads"),
        ("W", "Waiting", "Tickets sitting in the triage queue"),
        ("N", "Non-utilised talent", "Skilled agents doing routine data entry"),
        ("T", "Transport", "Tickets bouncing between teams"),
        ("I", "Inventory", "A growing backlog of unassigned tickets"),
        ("M", "Motion", "Switching between four systems for one ticket"),
        ("E", "Extra-processing", "Approvals that add no customer value"),
    ]:
        out.append(f"- **{letter} — {name}:** {ex}")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*© 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- write
os.makedirs(LABS, exist_ok=True)

readme, files = readme_md()
written = 0
packs = {}
for a in ACT:
    folder = os.path.join(LABS, files[a["num"]])
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write(lab_md(a))
    title = a["title"].replace("Elective — ", "")
    packs[a["num"]] = build_pack(a["num"], title, folder)
    written += 1

with open(os.path.join(LABS, "README.md"), "w") as f:
    f.write(readme)
with open(os.path.join(LABS, "tools.md"), "w") as f:
    f.write(tools_md())

core = sum(1 for a in ACT if not a.get("elective"))

# Superseded flat lab files from the pre-folder layout. They are NOT deleted
# automatically — the build reports them and leaves the decision to a human.
STALE = sorted(glob.glob(os.path.join(LABS, "lab-*.md")))


# ---------------------------------------------------------------- repo README
def repo_readme(files):
    n = len(ACT)
    out = []
    out.append(f"# {C.COURSE_CODE} - {C.TITLE}")
    out.append("")
    out.append(f"> **Course:** WSQ - {C.TITLE}  ")
    out.append(f"> **Course Code:** {C.COURSE_CODE}  ")
    out.append("> **Register here:** https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-white-belt-clsswb-training.html")
    out.append("")
    out.append(f"These are the hands-on lab exercises for the WSQ {C.TITLE} course delivered by "
               "[Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/).")
    out.append("")
    out.append(f"This repository contains **{n} guided Lean Six Sigma White Belt labs** "
               f"({core} core and {n-core} elective), structured around the **DMAIC roadmap** and grounded in the "
               "Council for Six Sigma Certification (CSSC) White Belt body of knowledge.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Courseware")
    out.append("")
    out.append("| Artifact | File |")
    out.append("|----------|------|")
    # URL-encode spaces/parens so the Markdown links work on GitHub
    def enc(p):
        return p.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
    lg_md = f"LG-{C.SHORT_TITLE}.md"
    out.append(f"| **Slide deck** | `courseware/{C.SHORT_TITLE}-{C.VERSION}.pptx` (and `.pdf`) |")
    out.append(f"| **Learner Guide (Markdown)** | [{lg_md}]({enc(lg_md)}) |")
    out.append(f"| **Learner Guide (DOCX/PDF)** | `courseware/LG-{C.SHORT_TITLE}.docx` (and `.pdf`) |")
    out.append(f"| **Lesson Plan (DOCX/PDF)** | `courseware/LP-{C.SHORT_TITLE}.docx` (and `.pdf`) |")
    out.append("| **Lab Index** | [labs/README.md](labs/README.md) |")
    out.append("| **Tools and Templates** | [labs/tools.md](labs/tools.md) |")
    out.append("")
    out.append("> **Note:** assessment papers, answer keys and trainer-only materials are intentionally "
               "not published in this repository.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## How to use")
    out.append("")
    out.append("1. Read the Learner Guide first — it follows the same DMAIC order as the course.")
    out.append("2. Complete the five labs in order using the BrewBean Cafe scenario.")
    out.append("3. Complete the elective labs if time allows, or as post-course practice.")
    out.append("4. Keep every worksheet — the final lab combines them into one improvement package.")
    out.append("5. Review the 'Check your work' step at the end of each lab before moving on.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Lab catalogue")
    out.append("")
    for t in C.TOPICS:
        acts = [a for a in ACT if a["topic"] == t["num"]]
        if not acts:
            continue
        # t['title'] already leads with the phase name for the DMAIC topics, so
        # don't print it twice ("Define — Define — Scope the Problem").
        heading = t["title"] if t["title"].lower().startswith(t["phase"].lower()) \
            else f"{t['phase'].title()} — {t['title']}"
        out.append(f"### {heading}")
        out.append("")
        for a in acts:
            title = a["title"].replace("Elective — ", "")
            tag = " *(elective)*" if a.get("elective") else ""
            fd = files[a["num"]]
            pk = LAB_DATA.get(a["num"], {})
            extra = ""
            if pk:
                extra = (f" — [data]({enc('labs/'+fd+'/data/')}), "
                         f"[model answer]({enc('labs/'+fd+'/model-answer.md')})")
            out.append(f"- [Lab {a['num']} - {title}]({enc('labs/'+fd+'/README.md')}){tag}{extra}")
        out.append("")
    out.append("---")
    out.append("")
    out.append("## Repository structure")
    out.append("")
    out.append("```")
    out.append("courseware/          slide deck (PPTX + PDF), Learner Guide, Lesson Plan")
    out.append("  archive/           superseded deck versions")
    out.append("  assets/            diagrams and images used by the deck")
    out.append(f"labs/                {len(ACT)} lab folders + index + toolkit")
    out.append("  lab-NN-<name>/     one folder per lab:")
    out.append("    README.md          the lab worksheet")
    out.append("    data/              mock datasets (.csv) + .xlsx workbook + data dictionary")
    out.append("    templates/         blank worksheets to fill in (.csv)")
    out.append("    model-answer.md    worked model answer")
    out.append("    facilitator-notes.md   trainer notes")
    out.append(f"LG-{C.SHORT_TITLE}.md")
    out.append("                     Learner Guide (Markdown mirror of the DOCX)")
    out.append(".claude/skills/courseware-build/build/")
    out.append("                     single-source generators: one content module")
    out.append("                     drives the deck, LP, LG and labs")
    out.append("```")
    out.append("")
    out.append("All artifacts are generated from `course_data.py` + `data_domainN.py`, so the deck, "
               "Lesson Plan, Learner Guide and labs stay 100% aligned.")
    out.append("")
    out.append("## Interactive tools")
    out.append("")
    out.append("- [5 Whys](https://alfredang.github.io/5whys/) — root-cause chain builder")
    out.append("- [Fishbone Diagram](https://alfredang.github.io/fishbone/) — Ishikawa cause-and-effect builder")
    out.append("- [Pareto Chart](https://alfredang.github.io/paretochart/) — collaborative team brainstorm, vote and live chart")
    out.append("- [NovaSPC](https://alfredang.github.io/novaspc/) — run charts, SPC charts and process capability")
    out.append("")
    out.append("## Reference")
    out.append("")
    out.append("- [Council for Six Sigma Certification - Lean Six Sigma White Belt Certification](https://www.sixsigmacouncil.org/lean-six-sigma-white-belt-certification/)")
    out.append("- [Course registration page](https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-white-belt-clsswb-training.html)")
    out.append("- [labs/tools.md](labs/tools.md) - templates, formulas and free tools used in the labs")
    out.append("")
    out.append("## Free tools used")
    out.append("")
    out.append("- Microsoft Excel, LibreOffice Calc, or Google Sheets")
    out.append("- Draw.io / diagrams.net for SIPOC, process maps and fishbone diagrams")
    out.append("- The interactive tools listed above")
    out.append("- Whiteboard or sticky notes for facilitation activities")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*Version {C.VERSION} · {C.VERSION_DATE} · © 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out)


with open(os.path.join(REPO, "README.md"), "w") as f:
    f.write(repo_readme(files))

print(f"Saved {written} lab FOLDERS to {LABS}  ({core} core, {written-core} elective)")
for n in sorted(packs):
    pk = packs[n]
    if pk:
        print(f"  lab {n:02d}: {len(pk['datasets'])} dataset(s) ({pk['rows']} rows), "
              f"{len(pk['templates'])} template(s), {pk['xlsx']}, model answer, facilitator notes")
print("Saved labs/README.md, labs/tools.md and README.md")
if STALE:
    print("\nNOTE: superseded flat lab files remain (not deleted automatically):")
    for f in STALE:
        print("  " + os.path.relpath(f, REPO))
    print("  Remove them once you are satisfied with the new folder layout.")
