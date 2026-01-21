# Executive Study Plan: L1 - Data Trust
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~20 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L1 (DATA TRUST) QUESTIONS

**Even when "data trust" isn't mentioned, look for these keywords/phrases:**

### Explicit Data Trust Keywords:
- "data quality", "data trust", "data validation", "data verification"
- "debug metric", "metric off", "data issue", "data problem"
- "data scarcity", "data drift", "anomaly detection", "data bias"

### Implicit L1 Indicators:
- **Data quality questions:** "How do you ensure data quality?", "How do you validate data?", "How do you debug a metric?"
- **Data issues:** "Metric is off by X%", "Data looks wrong", "How do you handle poor-quality data?"
- **Data bias questions:** "How do you detect bias?", "Who is over/under-represented?", "Data scarcity"
- **Anomaly detection:** "How do you detect anomalies?", "Data drift", "Unexpected patterns"

### L1 vs P1 Distinction:
- **L1 (Data Trust):** "Debug a metric that was off by X%" → Focus: Is the data trustworthy? (Source, Freshness, Completeness, Bias, Sanity)
- **P1 (Metric Drop):** "Orders down 25%" → Focus: WHERE is drop coming from? (Segment to find hot spot)

### L1 vs P12 Distinction:
- **L1 (Data Trust):** "How do you validate data?" → Focus: Data quality framework
- **P12 (Operational Excellence):** "How do you ensure system reliability?" → Focus: Operational process

### Red Flags (NOT L1):
- "Orders down 25%" → P1 (Metric Drop)
- "How do you monitor a system?" → L5 (Observability)
- "How do you scale a system?" → L2 (Scale & Capacity)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Data Trust Framework** (HIGHEST PRIORITY)
2. ⚠️ **Data Quality Issues** (MEDIUM)

**For Data Engineer:**
1. ✅ **Data Trust Framework** (HIGHEST) - Core framework
2. ✅ **Data Quality Issues** (HIGH) - Practical application

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Data Trust Framework
**Questions:** ~15 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Debug a metric that was off" or "How do you ensure data quality?" - core data trust framework
- **Framework:** Source → Freshness → Completeness → Bias → Sanity Checks
- **Source:** Identify origin (Primary: product logs, first-party events | Secondary: internal pipelines, transformations | External: vendors, partners, APIs), Validate ownership (Who maintains it? Who is on-call? Is there documentation/lineage?)
- **Freshness:** Expected latency (Real-time, Hourly, Daily/Batch), Check gaps (Last updated timestamp, Delays vs SLA, Silent failures)
- **Completeness:** Coverage checks (Missing rows/days, Null/default-heavy fields, Partial segments dropped), Join loss (Inner joins removing data, Key mismatches, Upstream schema changes)
- **Bias:** Sampling bias (Logged-in only, Power users, Specific regions/platforms), Measurement bias (Proxy ≠ true behavior, Instrumentation gaps, Incentives to game metrics)
- **Sanity Checks:** Trend checks (Sharp jumps/drops), Ratio checks (Conversion > 100%?), Cross-metric consistency, Compare to historical baselines

**Concrete Examples:**
- "Debug metric: Source (Where did it come from? Who owns it?), Freshness (Is it up to date? Any delays?), Completeness (Anything missing? Join loss?), Bias (Who is over/under-represented?), Sanity (Does it pass smell test?)"
- "Data quality: Check source, freshness, completeness, bias, sanity - if trust is low, slow down, qualify, or re-measure"

**Representative Questions (Do 5 only):**
- Q183: Debug a metric that was off by x percentage. (metric debugging angle)
- Q790: Explain data drifting. (data drift angle)
- Q803: Explain how you handle data scarcity. (data scarcity angle)
- Q915: Given a feature data record (FDR), how would you detect anomalies in it? (anomaly detection angle)
- Q1006: Have you ever had to work with poor-quality data or suggest new tracking? (data quality angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When assessing data trust, I use Source → Freshness → Completeness → Bias → Sanity Checks. First, I check Source: Identify origin (Primary: product logs, first-party events, direct user actions | Secondary: internal pipelines, transformations, aggregated data | External: vendors, partners, scraped data, third-party APIs), Validate ownership (Who maintains it? Who is on-call when it breaks? Is there documentation/lineage? Can we trace the data flow?). Second, I check Freshness: Expected latency (Real-time: should update immediately | Hourly: should update within the hour | Daily/Batch: should update on schedule), Check gaps (Last updated timestamp: when was it last refreshed? Delays vs SLA: is it meeting expected update frequency? Silent failures: no alerts but stale data). Third, I check Completeness: Coverage checks (Missing rows/days: are there gaps in the time series? Null or default-heavy fields: are key fields populated? Partial segments dropped: are all user segments/platforms included?), Join loss (Inner joins removing data: are we losing records in joins? Key mismatches: do join keys align correctly? Upstream schema changes: did schema changes break data collection?). Fourth, I check Bias: Sampling bias (Logged-in only: are we missing anonymous users? Power users: are we over-representing heavy users? Specific regions/platforms: are all geos and devices included?), Measurement bias (Proxy ≠ true behavior: is our metric a good proxy for what we care about? Instrumentation gaps: are we tracking all relevant events? Incentives to game metrics: could users or teams be gaming the measurement?). Finally, I do Sanity Checks: Trend checks (Sharp jumps/drops that don't align with known changes), Ratio checks (Conversion > 100%? Negative values where impossible?), Cross-metric consistency (Do related metrics move together logically?), Compare to historical baselines (Is this within expected range?). The key principle: No decision is better than a confident decision on bad data. If trust is low → slow down, qualify, or re-measure."

**How to Adapt This Narrative for Each Question:**

- **Q183 (Debug metric off by X%):** Focus on debugging → "To debug a metric that's off by X%, I'd: Source (Identify origin: Where did this metric come from? Primary data (product logs, events) or secondary (pipelines, transformations) or external (vendors, APIs)? Validate ownership: Who maintains this? Who is on-call? Is there documentation/lineage?), Freshness (Check if data is up to date: Expected latency - should this be real-time, hourly, or daily? Check gaps - Last updated timestamp, delays vs SLA, silent failures), Completeness (Verify nothing is missing: Coverage checks - missing rows/days, null fields, partial segments dropped, Join loss - inner joins removing data, key mismatches, upstream schema changes), Bias (Check who is over/under-represented: Sampling bias - logged-in only, power users, specific regions/platforms, Measurement bias - proxy ≠ true behavior, instrumentation gaps, incentives to game), Sanity Checks (Verify numbers pass smell test: Trend checks - sharp jumps/drops, Ratio checks - conversion > 100%?, Cross-metric consistency, Compare to historical baselines). I'd systematically go through each dimension to identify where the trust breaks down."

- **Q790 (Explain data drifting):** Emphasize data drift → "Data drift occurs when the distribution of input data changes over time, causing model performance to degrade. To detect it, I'd: Source (Identify origin: Where is the data coming from? Has the source changed?), Freshness (Check if data is up to date: Are there delays or stale data?), Completeness (Verify nothing is missing: Are all segments still included? Any join loss?), Bias (Check who is over/under-represented: Has the user population changed? Sampling bias? Measurement bias?), Sanity Checks (Verify numbers pass smell test: Compare current distribution to historical baseline, detect shifts in feature distributions, check for outliers). I'd monitor feature distributions over time and alert when they deviate significantly from training data."

---

### BUCKET 2: Data Quality Issues
**Questions:** ~5 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "How do you handle poor-quality data?" or "Data quality issues" - same framework, with focus on practical issues
- **Approach:** Same data trust framework, with focus on common data quality problems
- **Common Issues:** Missing data, Stale data, Biased data, Inconsistent data, Schema changes
- **Solutions:** Data validation, Monitoring, Alerts, Documentation, Lineage tracking

**Concrete Examples:**
- "Poor-quality data: Check source (documentation, ownership), freshness (monitoring, alerts), completeness (validation, checks), bias (sampling, measurement), sanity (validation rules)"
- "Data quality: Implement validation, monitoring, alerts, documentation, lineage"

**Representative Questions (Do 5 only):**
- Q1006: Have you ever had to work with poor-quality data or suggest new tracking? (data quality angle)
- Q248: Describe your experience with statistics. (statistics/data quality angle)
- Q183: Debug a metric that was off by x percentage. (data quality debugging angle)
- Q790: Explain data drifting. (data quality monitoring angle)
- Q803: Explain how you handle data scarcity. (data quality/data scarcity angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When handling data quality issues, I use the same data trust framework but focus on practical solutions. I identify the issue using Source → Freshness → Completeness → Bias → Sanity Checks. Then I implement solutions: Data validation (Rules, checks, automated tests), Monitoring (Track freshness, completeness, anomalies), Alerts (Notify when data quality degrades), Documentation (Data dictionary, lineage, ownership), Lineage tracking (Trace data flow, dependencies). I prioritize based on impact: High-impact metrics get more rigorous checks, Low-impact metrics get basic validation. The key is preventing bad data from reaching decision-makers."

**How to Adapt This Narrative for Each Question:**

- **Q1006 (Poor-quality data or new tracking):** Focus on practical solutions → "When working with poor-quality data, I'd: Assess using data trust framework (Source: Identify origin, validate ownership, Freshness: Check if up to date, Completeness: Verify nothing missing, Bias: Check representation, Sanity: Verify numbers), Implement solutions (Data validation: Rules, checks, automated tests, Monitoring: Track freshness, completeness, anomalies, Alerts: Notify when quality degrades, Documentation: Data dictionary, lineage, ownership, Lineage tracking: Trace data flow), Prioritize (High-impact metrics: More rigorous checks, Low-impact: Basic validation). For new tracking, I'd: Design tracking (Clear events, consistent schema, documentation), Validate (Test in staging, monitor in production, sanity checks), Monitor (Track quality metrics, alert on issues). I'd focus on preventing bad data from reaching decision-makers."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Data Trust Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Data Quality Issues** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through data trust framework in 2 minutes (Source → Freshness → Completeness → Bias → Sanity Checks)
- [ ] Identify data quality issues (Source, freshness, completeness, bias, sanity)
- [ ] Apply framework to debug metrics (Systematic approach)
- [ ] Explain when to slow down (If trust is low, qualify or re-measure)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the data trust framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Source → Freshness → Completeness → Bias → Sanity Checks framework**, not memorizing answers

**Remember:** L1 is about data trust. The framework: Source → Freshness → Completeness → Bias → Sanity Checks. Key principle: No decision is better than a confident decision on bad data. If trust is low → slow down, qualify, or re-measure.
