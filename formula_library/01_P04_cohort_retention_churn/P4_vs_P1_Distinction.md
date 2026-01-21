# P4 vs P1: When is a "Drop" a Retention Question?

## The Key Distinction

**P1 (Metric Drop Diagnosis):**
- Generic metric decline (revenue, DAU, engagement, conversion rate, etc.)
- **Approach:** Segment by platform/geo/channel → Hypothesize → Data Check → Action
- **Focus:** WHERE is the drop coming from? (geography, platform, surface, channel)

**P4 (Cohort/Retention/Churn):**
- Specifically about **retention or churn** metrics
- **Approach:** Define Cohorts → Measure Retention → Identify Churn Drivers → Hypothesize → Fix
- **Focus:** WHEN do users leave? Which cohorts are worse? (cohort-based analysis required)

---

## Why "Retention Drop" Belongs in P4

### 1. Retention is inherently cohort-based

You **cannot measure retention** without cohorts:

```
❌ Wrong: "Overall retention is 40%"
✅ Right: "January cohort: 40% D30 retention"
         "February cohort: 35% D30 retention"
```

Retention requires:
- A starting point (cohort definition)
- A time window (D1, D7, D30, M3)
- A comparison (this cohort vs that cohort)

### 2. The solving framework is different

**P1 approach for "Revenue dropped 20%":**
```
Segment by:
├─ Platform (iOS vs Android vs Web)
├─ Geography (US vs EU vs APAC)
├─ Channel (ads vs organic)
└─ Surface (homepage vs search vs product page)

Find hot spot → Hypothesize → Fix
```

**P4 approach for "Retention dropped 35%":**
```
Define Cohorts:
├─ January signups vs February signups
├─ Ads cohort vs Organic cohort
└─ Activated users vs Not activated

Measure Retention:
├─ D1 retention: same or different?
├─ D7 retention: same or different?
└─ D30 retention: which cohort dropped?

Identify Churn Drivers:
├─ WHEN: Day 0-1? Week 1? Month 1+?
├─ WHO: Which cohort churns more?
└─ WHAT: What changed before churn?

Fix: Improve onboarding, targeting, or habit formation
```

### 3. The mental model is different

**P1 mental model:**
> "Something broke. Where is it broken? (platform/geo/channel)"

**P4 mental model:**
> "Users are leaving. When do they leave? Which cohort is worse? (cohort comparison)"

---

## Examples

### ✅ P1 (Generic Metric Drop)

**Q:** "Revenue dropped 20% last month"
- Metric: Revenue (not retention)
- Approach: Segment by platform/geo/channel
- Answer: "iOS revenue dropped 30%, Android stable → investigate iOS"

### ✅ P4 (Retention Drop)

**Q:** "Retention dropped 35% on Salesforce"
- Metric: Retention (cohort-based)
- Approach: Compare cohorts, measure retention curves
- Answer: "January cohort: 40% D30 retention. February cohort: 25% D30 retention. February users churn early (Day 0-1) → activation problem"

### ✅ P4 (Churn Increase)

**Q:** "40% increase in first month churn on HelloFresh"
- Metric: Churn (cohort-based)
- Approach: Compare cohorts, identify churn timing
- Answer: "Recent cohorts churn at Day 0-1 → onboarding/activation gap"

---

## Decision Tree

```
Is the metric "retention" or "churn"?
│
├─ YES → P4 (Cohort/Retention/Churn)
│   └─ Requires cohort analysis
│   └─ Framework: Define Cohorts → Measure Retention → Identify Churn Drivers
│
└─ NO → P1 (Metric Drop Diagnosis)
    └─ Segment by platform/geo/channel
    └─ Framework: Clarify Metric → Segment → Hypothesize → Data Check → Action
```

---

## Why This Matters

**"Diagnose a 35% drop in retention"** is correctly in P4 because:

1. ✅ **Retention is the metric** → requires cohort analysis
2. ✅ **Framework matches** → Define Cohorts → Measure Retention → Identify Churn Drivers
3. ✅ **Mental model fits** → "Which cohort is worse? When do they leave?"

If you tried to solve it with P1:
- ❌ You'd segment by platform/geo (not cohorts)
- ❌ You'd miss the cohort comparison (the core of retention analysis)
- ❌ You'd use the wrong framework

---

## One-Sentence Rule

> **If the metric IS retention/churn → P4. If the metric is something else (revenue, DAU, engagement) → P1.**

---

## Edge Cases

### "Retention dropped, but I want to segment by platform"

**Answer:** Still P4, but you can segment cohorts BY platform:
```
Cohort: January signups
├─ iOS cohort: 45% D30 retention
├─ Android cohort: 35% D30 retention
└─ Web cohort: 40% D30 retention

→ Android cohort is worse → investigate Android onboarding
```

This is still cohort analysis (cohorts defined by platform), not P1 segmentation.

### "Revenue dropped, and I suspect it's a retention problem"

**Answer:** Start with P1 to find WHERE revenue dropped. If you discover it's a retention issue, then use P4 framework:
```
P1: Revenue dropped 20%
├─ Segment: iOS revenue stable, Android revenue dropped 30%
└─ Hypothesis: Android retention problem

P4: Investigate Android retention
├─ Define cohorts: January Android users vs February Android users
├─ Measure retention: February cohort has lower D30 retention
└─ Identify churn drivers: Early churn (Day 0-1) → activation problem
```

---

## Summary

**P4 is correct for "retention drop" questions** because:
- Retention is inherently cohort-based
- The framework requires cohort analysis
- The mental model is "which cohort is worse?" not "where is the drop?"

**P1 is for generic metric drops** where you segment by platform/geo/channel, not cohorts.
