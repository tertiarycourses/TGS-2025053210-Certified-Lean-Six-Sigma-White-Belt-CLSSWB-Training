# Activity 3 — Model Answer

**Analyze — Find the Root Cause**

*Certified Lean Six Sigma White Belt (CLSSWB) Training · TGS-2025053210 · Version v7*

> **Use this AFTER you have attempted the activity.** There is rarely one right answer in Lean Six Sigma — what matters is whether your reasoning is supported by the data. Compare your thinking with the model, not just your wording.

## 5 Whys (model)

```
PROBLEM: Customers wait an average of 8.9 minutes (up to 15.0) during
         the morning rush against a 5-minute promise.
WHY 1?   Drinks are not completed fast enough to clear the queue.
WHY 2?   The barista keeps stopping part-way through making an order.
WHY 3?   The milk at the counter runs out during the rush.
WHY 4?   It is not restocked before the rush starts.
WHY 5?   Restocking the counter milk is not part of anyone's opening routine.
ROOT CAUSE: No one owns restocking counter milk before 7:30am — it was never written
         into the opening checklist.
CHECK:   If restocking is assigned and done before 7:30am, the 18 mid-order trips
         stop, and roughly 29 minutes a morning of barista time comes back.

This is the SAME chain the Case Study answer key uses, so a learner who works this
lab properly has already rehearsed Case Study Q2.

Accept any chain that (a) ends in a PROCESS the team can change and (b) does not end
by blaming a named person. 'The barista is too slow' is not a root cause — ask why.
```

## Fishbone (model)

```
HEAD OF THE FISH: 'Morning queue is too slow (avg 8.9 min vs 5 min promise)'

MANPOWER:    one till open at peak though two are installed; no cover for breaks;
             no one assigned to restock.
METHOD:      no opening restock routine; order written on the cup then re-keyed;
             no check before handover so wrong drinks reach the customer.
MACHINE:     single grinder; card machine slow to connect.
MATERIAL:    milk stored in the back store, not at the counter; cups and lids kept
             apart.
MEASUREMENT: wait time never recorded; the 5-minute promise never tracked; complaints
             not logged anywhere the team can see.

Every one of these appears in the cause-evidence sheet, so learners can check their
fishbone against the data rather than against the trainer's opinion.
```

## Reading the Pareto (model)

```
The ranked delay reasons are:
  1. Waiting for milk restock: 18 (31.6%, cumulative 31.6%)
  2. Single till queue: 14 (24.6%, cumulative 56.1%)
  3. Order re-keyed into till: 9 (15.8%, cumulative 71.9%)
  4. Drink remade (wrong order): 7 (12.3%, cumulative 84.2%)
  5. Card payment slow: 5 (8.8%, cumulative 93.0%)
  6. Cups/lids not at hand: 4 (7.0%, cumulative 100.0%)

THE VITAL FEW: Waiting for milk restock and Single till queue together account for
56.1% of all observed delays. Fixing those two addresses most of the
problem; the remaining reasons are the 'useful many' and can wait.

This is the 80/20 point of the Pareto principle — and it is why the team works on
milk restocking and till cover rather than on the slow card machine.
```

## Common vs special cause (model)

```
COMMON CAUSE (built into the process, happens every day): milk not restocked; one
  till open; the re-keying step; no measurement of wait time; no agreed target.
  These are fixed by CHANGING THE PROCESS.
SPECIAL CAUSE (a specific one-off event): the grinder breaking on 12 June; the tour
  group on 15 June; a new barista still training.
  These are fixed by dealing with THAT EVENT — and you do not redesign a process
  around a one-off.

The White Belt point: a team that chases special causes is always firefighting. The
improvement comes from the common causes.
```

## Shortlist (model)

```
1. Counter milk not restocked before the rush — Method — COMMON.
   Evidence: 18 of 60 customers delayed by it; 96 sec average per trip; ~29 min of
   barista time lost per morning. Highest-count single reason on the Pareto.
2. Only one till open at peak — Manpower — COMMON.
   Evidence: 14 of 60 customers delayed; a second till is already installed, so the
   fix costs nothing in capital.
3. Order written on the cup then re-keyed into the till — Method — COMMON.
   Evidence: steps 4 and 5 capture the same information twice, ~19 sec per customer.

Note what is NOT shortlisted: 'the barista was new' and 'a tour group arrived' — both
special causes with no supporting evidence in the observed morning.
```

---

*Certified Lean Six Sigma White Belt (CLSSWB) Training · TGS-2025053210 · Version v7 · © 2026 Tertiary Infotech Academy Pte Ltd*
