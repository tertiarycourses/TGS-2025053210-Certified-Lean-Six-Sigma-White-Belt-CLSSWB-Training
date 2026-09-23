# Lab 2 — Model Answer

**Measure — Map the Process and Spot the Waste**

*Certified Lean Six Sigma White Belt (CLSSWB) Training · TGS-2025053210 · Version v3*

> **Use this AFTER you have attempted the lab.** There is rarely one right answer in Lean Six Sigma — what matters is whether your reasoning is supported by the data. Compare your thinking with the model, not just your wording.

## SIPOC (model)

```
SUPPLIERS: coffee bean roaster; dairy/oat milk supplier; cup and lid supplier;
           till and card-machine provider; the cafe's own back store.
INPUTS:    beans, milk, cups, lids, sleeves; the customer's order; barista and
           cashier time; the espresso machine and grinder; the till system.
PROCESS:   1. Customer joins queue  2. Order taken at till  3. Payment  4. Cup to
           barista  5. Drink made  6. Drink handed over.
OUTPUTS:   the finished drink; the receipt; the customer's experience of the wait.
CUSTOMERS: office workers in the morning rush (the primary customer); walk-in and
           occasional customers.

Mark down a SIPOC whose Process column has 12 steps — the discipline is the 5-7 step
high-level view. The detail belongs in the process map, not the SIPOC.
```

## Process map and value-add judgement (model)

```
VALUE-ADDING (the customer would pay for it): steps 3 (stating the order),
  9 (grinding and extracting), 11 (steaming and pouring).  Total ~97 sec.
NON-VALUE-ADDING: steps 2, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15.  Total ~671 sec.

So roughly 97 of 768 seconds - about 13% - of the process is value-adding. The
single largest non-value-adding block is step 2 (queueing, 265 sec) followed by
step 8 (cup waiting at the barista station, 143 sec) and step 10 (fetching milk,
96 sec average).

Accept step 6 (payment) being argued either way, as long as the learner justifies it:
the customer must pay, but they would not pay EXTRA for the paying. Business-value-
adding is the usual verdict. Step 5 (re-keying) is never value-adding — the order was
already captured in step 4.
```

## Data type classification (model)

```
CONTINUOUS (measured on a scale): Wait Time (min); every Avg Time (sec) in the
  process timings; time lost per morning.
DISCRETE (counted): Customer ID count; Drink Remade yes/no count; tally counts in the
  DOWNTIME sheet; number of tills open; complaint counts.

'Drink Ordered' and 'Delay Reason' are neither — they are CATEGORICAL (attribute)
data. At White Belt it is enough that the learner does not call them continuous.
```

## DOWNTIME tally (model — the five rows left blank)

```
O - Overproduction: preparing drinks speculatively before an order is placed.
  Tally 0 at BrewBean today. 'Zero, with evidence' is a correct answer.
N - Non-utilised talent: a trained barista spending ~29 min a morning walking to the
  back store for milk, and the second till standing idle while a trained cashier
  serves elsewhere. Tally 18 (the restock trips). ~29 min.
T - Transport: the cup travelling from till to barista station (step 7) - small but
  real. Tally 60, ~8 min.
I - Inventory: cups queued at the barista station waiting to be made (step 8) - work
  in progress sitting in a queue. Tally 60, ~143 min of accumulated cup-waiting.
E - Extra-processing: writing the order on the cup and then re-keying it into the
  till (steps 4 + 5) - the same information captured twice. Tally 60, ~19 min.

LARGEST WASTE BY COUNT AND BY TIME: W - Waiting, at step 2 and step 8.
The most ACTIONABLE waste is M - Motion / N - Non-utilised talent at step 10, because
it has a single obvious cause the team can remove. That is the thread Lab 3 pulls.
```

## Baseline figures (model)

```
Customers observed:        60
Average wait:              8.9 min   (promise: 5.0 min)
Longest wait:              15.0 min
Average wait at 08:00-08:30 peak: 12.4 min
Customers over the 5-min promise: 49 of 60  (82%)
Drinks remade:             7

These are the numbers Lab 5 measures the improvement against. Learners should write
them down — the Case Study expects a baseline to be quoted, not invented.
```

---

*Certified Lean Six Sigma White Belt (CLSSWB) Training · TGS-2025053210 · Version v3 · © 2026 Tertiary Infotech Academy Pte Ltd*
