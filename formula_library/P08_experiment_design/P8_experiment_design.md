# P8 - Experiment Design

**Formula:** `Hypothesis → Metric → Design → Run → Validate → Decide`

---

## 🧠 Mental Model (ASCII Tree)

```
P8: EXPERIMENT DESIGN
|
+-- 0) Frame (30 sec)
|     - What decision are we making?
|     - What constraint matters? (time, risk, traffic, legal, UX)
|
+-- 1) HYPOTHESIS
|     - "If we change X for users Y, then outcome Z will change because R."
|     - X = treatment (what changes)
|     - Y = target population
|     - Z = expected direction + size (if possible)
|     - R = mechanism (why it should work)
|
+-- 2) METRIC (success + safety)
|     +-- Primary metric (the "one number" for decision)
|     |     - Must map to goal (revenue, retention, activation, etc.)
|     |
|     +-- Guardrails (prevent self-own)
|     |     - Quality / user harm / churn / latency / errors / complaints
|     |
|     +-- Diagnostics (helps explain *why*)
|           - Step metrics, funnel steps, latency breakdown, CTR vs CVR, etc.
|
+-- 3) DESIGN (make it valid)
|     +-- Unit of randomization
|     |     - user vs session vs account vs geo vs device
|     |     - avoid spillover (users affecting each other)
|     |
|     +-- Population / eligibility
|     |     - new users? returning? specific segment?
|     |
|     +-- Variants
|     |     - Control vs Treatment (or A/B/C)
|     |     - keep everything else constant
|     |
|     +-- Duration & sample sizing (conceptual)
|     |     - run full cycles (weekday/weekend)
|     |     - ensure enough power for expected effect size
|     |
|     +-- Instrumentation
|           - event tracking, logging, exposure definition
|           - "who saw treatment?" must be unambiguous
|
+-- 4) RUN (execution plan)
|     - Ramp: 1% → 10% → 50% → 100% (if safe)
|     - Monitor guardrails daily
|     - Freeze conflicting changes
|
+-- 5) VALIDATE (trust the result?)
|     +-- A/A or sanity checks (if available)
|     +-- SRM check (sample ratio mismatch)
|     +-- Balance check (are groups comparable?)
|     +-- Correct attribution (exposure vs outcome window)
|     +-- Novelty / seasonality / logging changes
|     +-- Multiple testing / peeking risk
|
+-- 6) DECIDE
      - Ship / iterate / rollback
      - Rollout plan + follow-up monitoring
      - Learnings: mechanism confirmed? which segment moved?
```

---

## 📌 Sample: Checkout Redesign Experiment

**Prompt:**
"We want to redesign checkout to increase purchases. Design an experiment."

```
SAMPLE: Checkout redesign
|
+-- 1) Hypothesis
|     If we simplify checkout (fewer fields, clearer shipping costs),
|     then purchase conversion will increase because less friction.
|
+-- 2) Metrics
|     Primary: Purchase conversion rate (session→purchase)
|     Guardrails: Refund rate, support tickets, payment failure rate, latency
|     Diagnostics: Step drop-offs (cart→shipping→payment→confirm),
|                  field error rate, time-to-complete checkout
|
+-- 3) Design
|     Randomization unit: user (avoid cross-session confusion)
|     Population: all users entering checkout (exclude employees/bots)
|     Variants: A = current checkout, B = redesigned checkout
|     Duration: cover at least 1–2 full weekly cycles
|     Instrumentation: "exposed_to_new_checkout" event + step events
|
+-- 4) Run
|     Ramp 1% → 10% → 50% while watching guardrails daily
|     Freeze other checkout changes during test window
|
+-- 5) Validate
|     Check SRM (traffic split correct?)
|     Confirm exposure definition (users counted only if saw checkout)
|     Ensure no logging break (events firing in both variants)
|     Segment read: new vs returning, device type, geo
|
+-- 6) Decide
      If primary metric up and guardrails stable → ship with gradual rollout
      If mixed → iterate (e.g., shipping cost clarity) and re-test
      If guardrails worsen → rollback + root-cause (payment failures? confusion?)
```

---

If you want, I can do **P9 next** in the same style, or we can add a **"cheat mini-template"** (5 lines) you can paste into notes during interviews.
