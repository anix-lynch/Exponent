# P1 - Metric Drop Diagnosis

**Formula:** `Clarify Metric → Segment → Hypothesize → Data Check → Action`

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
