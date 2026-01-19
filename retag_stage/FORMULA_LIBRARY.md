# 📚 FORMULA LIBRARY - 26 Canonical Patterns

**Purpose:** Anti-hallucination. Copy formulas from here, don't generate.

---

## 📑 TABLE OF CONTENTS

### 🟢 NORTHSTAR FORMULAS (12)
- [P1 - Metric Drop Diagnosis](#p1---metric-drop-diagnosis)
- [P2 - NSM + KPI Ladder](#p2---nsm--kpi-ladder)
- [P3 - Funnel Analysis](#p3---funnel-analysis)
- [P4 - Cohort / Retention / Churn](#p4---cohort--retention--churn)
- [P5 - Segmentation](#p5---segmentation)
- [P6 - Prioritization](#p6---prioritization)
- [P7 - Tradeoff Framing](#p7---tradeoff-framing)
- [P8 - Experiment Design](#p8---experiment-design)
- [P9 - Decision Under Uncertainty](#p9---decision-under-uncertainty)
- [P10 - Executive Communication](#p10---executive-communication)
- [P11 - Stakeholder Alignment](#p11---stakeholder-alignment)
- [P12 - Operational Excellence](#p12---operational-excellence)

### 🟡 LHF FORMULAS (14)
- [L1 - Data Trust](#l1---data-trust)
- [L2 - Scale & Capacity](#l2---scale--capacity)
- [L3 - Cost / ROI](#l3---cost--roi)
- [L4 - Constraints](#l4---constraints)
- [L5 - Observability](#l5---observability)
- [L6 - Ops Tradeoffs](#l6---ops-tradeoffs)
- [L7 - Data Modeling](#l7---data-modeling)
- [L8 - Market Analysis](#l8---market-analysis)
- [L9 - Financial Sensitivity](#l9---financial-sensitivity)
- [L10 - Process Optimization](#l10---process-optimization)
- [L11 - Risk Mitigation](#l11---risk-mitigation)
- [L12 - Metrics Interpretation](#l12---metrics-interpretation)
- [L13 - SQL Reasoning](#l13---sql-reasoning)
- [L14 - System Design (Conceptual)](#l14---system-design-conceptual)

### 🔴 IGNORE
- [IGNORE](#ignore)

---

## 🟢 NORTHSTAR FORMULAS (12)

### P1 - Metric Drop Diagnosis
**Formula:** `Clarify Metric → Segment → Hypothesize → Data Check → Action`

[📖 **View Detailed Guide**](../../formula_library/P1_metric_drop/README.md)

---

## P1 ASCII TREE (copy/paste mental model)

```text
P1: METRIC DROP DIAGNOSIS
Goal: explain "X is down" and decide what to do next

0) START
   |
   v
1) CLARIFY METRIC  (What exactly dropped?)
   |
   +-- 1.1 Define numerator/denominator (is it a RATE or COUNT?)
   |       - ex: conversion = orders / sessions
   |
   +-- 1.2 Define scope (WHERE/WHEN/WHO)
   |       - region, platform, surface, segment, time window
   |
   +-- 1.3 Define baseline + delta
   |       - from A to B, magnitude, when started
   |
   v
2) DATA CHECK (Is the drop real?)
   |
   +-- 2.1 Instrumentation change?
   |       - tracking code, event name, schema, logging, pipeline
   |
   +-- 2.2 Timing/latency/backfill?
   |       - delayed events, ETL lag, late-arriving data
   |
   +-- 2.3 Denominator weird?
   |       - sessions up, bot traffic, sampling, filtering
   |
   +-- IF "DATA BUG" -> ACTION: fix measurement, re-read metrics
   |   ELSE continue
   |
   v
3) SEGMENT (Where is it coming from?)
   |
   +-- 3.1 Slice by: platform (iOS/Android/Web)
   +-- 3.2 Slice by: geography / language / cohort (new vs returning)
   +-- 3.3 Slice by: funnel step / surface / entry point
   +-- 3.4 Slice by: acquisition channel (ads, organic, email)
   |
   +-- Identify "HOT SPOT" segment(s) = biggest contribution to drop
   |
   v
4) HYPOTHESIZE (Why did it happen?)
   |
   +-- 4.1 Product change?
   |       - UI, ranking, pricing, policy, feature launch
   |
   +-- 4.2 External change?
   |       - seasonality, competitor, outage, market event
   |
   +-- 4.3 Supply-side change? (if marketplace)
   |       - inventory, quality, seller behavior
   |
   +-- 4.4 Performance change?
   |       - latency, crash, error rates
   |
   +-- Make 3-5 hypotheses, ranked by likelihood x impact
   |
   v
5) VALIDATE (fast checks to confirm/kill hypotheses)
   |
   +-- 5.1 Correlation in time (did it start exactly at release?)
   +-- 5.2 Counter-metrics (crashes up? latency up? add-to-cart down?)
   +-- 5.3 Funnel step localization (where exactly is friction?)
   +-- 5.4 Compare control segments (platform A vs B, region A vs B)
   |
   v
6) ACTION (What do we do now?)
   |
   +-- 6.1 If severe + clear culprit -> rollback / hotfix / disable
   +-- 6.2 If unclear -> run targeted experiment / logging / sampling
   +-- 6.3 If segment-specific -> fix that surface/channel/bug
   +-- 6.4 Communicate plan: what we know, what we're testing, ETA
```

---

## SAMPLE 1 (classic)

**Prompt:** "Orders down 25% since yesterday. What do you do?"

```text
1) Clarify
- Orders = completed checkouts? paid orders?
- Scope: all countries? web only? last 24h vs same weekday last week?
- Delta: -25% overall; when exactly started?

2) Data Check
- Any tracking/pipeline change yesterday?
- Payment event missing? order-completed event renamed?
- ETL lag: are late events missing?

3) Segment
- Slice by platform: iOS -40%, web flat
- Slice by geo: US only
=> Hot spot = iOS + US

4) Hypotheses
- iOS app update caused checkout crash
- Payment provider degraded in US iOS path
- New promo banner blocked CTA on iOS

5) Validate
- Check crash rate, latency, payment error codes by platform
- Funnel: add-to-cart ok, checkout-start ok, payment-success down
=> culprit likely payment errors / crash

6) Action
- If confirmed: rollback iOS release / switch payment fallback
- Add alerting; exec update with culprit + mitigation + monitoring
```

---

## SAMPLE 2 (rate vs denominator trap)

**Prompt:** "Conversion rate dropped from 10% to 7%."

```text
1) Clarify
- Conversion = orders / sessions (rate)
- Is orders down, or sessions up (bad traffic), or both?

2) Data Check
- Did session tracking change? bots? new channel sending low-intent traffic?

3) Segment
- By channel: new paid campaign added; converts at 1%
- By landing page: new landing page converts poorly
=> Hot spot = new campaign + landing page

4) Hypotheses
- Campaign targeting wrong audience
- Landing page broken / slow
- Pricing mismatch vs ad promise

5) Validate
- Compare bounce, time-to-interact, funnel step drop on that landing page
- Ad group breakdown

6) Action
- Pause campaign or fix landing page
- Add guardrails: quality metrics per channel (bounce, add-to-cart)
```

---

## SAMPLE 3 (data bug)

**Prompt:** "DAU dropped 15% today."

```text
1) Clarify
- DAU definition: unique users with 'app_open' event?
- Timezone cutoff? rolling 24h?

2) Data Check
- 'app_open' event missing from Android build?
- Pipeline delay today?
- Sampling changed?
=> If yes: measurement issue

6) Action
- Fix instrumentation/pipeline
- Recompute DAU using backup signal (sessions, server auth hits)
- Postmortem + add monitors for event volume anomalies
```

---

## MICRO-CHEAT SHEET (memorize this)

```text
Clarify: what metric? what definition? what scope?
Data check: is it real?
Segment: where is it from?
Hypothesize: top 3 causes
Validate: quickest kill tests
Action: rollback / fix / experiment / communicate
```

If you paste **one real question from your batches** (a P1 one like "X down Y%"), I'll run it through this tree and produce a **tight 6-line "short_answer"** you can reuse across many similar questions.

---

### P2 - NSM + KPI Ladder
**Formula:** `Define NSM → Input KPIs → Leading Indicators → Guardrails → Dashboard`

### P3 - Funnel Analysis
**Formula:** `Define Funnel Steps → Measure Drop-off → Identify Friction → Hypothesize Fix → Test`

### P4 - Cohort / Retention / Churn
**Formula:** `Define Cohorts → Measure Retention → Identify Churn Drivers → Hypothesize → Fix`

### P5 - Segmentation
**Formula:** `(Persona × Behavior × Value) → Rank → Focus Top Segments`

### P6 - Prioritization
**Formula:** `Impact × Confidence × Ease → RICE Score → Decide + Communicate`

### P7 - Tradeoff Framing
**Formula:** `Define Options → Winners/Losers → Guardrails → Decide + Communicate`

### P8 - Experiment Design
**Formula:** `Hypothesis → Metric → Design → Run → Validate → Decide`

### P9 - Decision Under Uncertainty
**Formula:** `Clarify Assumptions → Identify Risks → Validation Plan → Decide`

### P10 - Executive Communication
**Formula:** `Context → Insight → Recommendation → Next Steps`

### P11 - Stakeholder Alignment
**Formula:** `Understand Incentives → Address Concerns → Build Coalition → Decide`

### P12 - Operational Excellence
**Formula:** `Assess Current State → Identify Risks → Prioritize Fixes → Communicate Plan → Monitor`

---

## 🟡 LHF FORMULAS (14)

### L1 - Data Trust
**Formula:** `Source → Freshness → Completeness → Bias → Sanity Checks`

### L2 - Scale & Capacity
**Formula:** `Current Load → 10× Projection → Bottlenecks → Mitigation`

### L3 - Cost / ROI
**Formula:** `Cost Drivers → Benefits → Breakeven → Decide`

### L4 - Constraints
**Formula:** `Legal → Technical → Organizational → Timeline → Prioritize`

### L5 - Observability
**Formula:** `Key Metrics → Alerts → Dashboards → Escalation`

### L6 - Ops Tradeoffs
**Formula:** `Speed vs Quality vs Reliability → SLAs → Error Budget → Decide`

### L7 - Data Modeling
**Formula:** `Entities → Relationships → Metrics → Grain → Validate`

### L8 - Market Analysis
**Formula:** `Competitors → Differentiation → Market Conditions → Strategy`

### L9 - Financial Sensitivity
**Formula:** `Levers (Price, Volume, Churn) → Impact → Prioritize`

### L10 - Process Optimization
**Formula:** `Map Workflow → Identify Bottlenecks → Optimize → Measure`

### L11 - Risk Mitigation
**Formula:** `Enumerate Risks → Blast Radius → Mitigations → Monitor`

### L12 - Metrics Interpretation
**Formula:** `Metric Moved → Proxy Validity → Gaming Risk → Decide`

### L13 - SQL Reasoning
**Formula:** `Conceptual Join → Aggregation Logic → Filter Logic → Output`

### L14 - System Design (Conceptual)
**Formula:** `Components → Data Flow → Boundaries → Scale Considerations`

---

## 🔴 IGNORE (No Formula Needed)
**Formula:** `N/A`
**Notes:** Coding, ML theory, brain teasers, low ROI
