# Executive Study Plan: L5 - Observability
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~20 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L5 (OBSERVABILITY) QUESTIONS

**Even when "observability" isn't mentioned, look for these keywords/phrases:**

### Explicit Observability Keywords:
- "observability", "monitoring", "dashboard", "metrics", "alerts", "logging"
- "system health", "track performance", "monitor X", "how do you know if X is healthy"
- "SLO", "SLI", "error rate", "latency", "throughput", "saturation"

### Implicit L5 Indicators:
- **Monitoring questions:** "How do you monitor X?", "What dashboard would you build?", "How do you track system health?"
- **Metrics questions:** "What metrics would you track?", "How do you measure X?", "Key metrics for X"
- **Alert questions:** "When do you alert?", "How do you set up alerts?", "Alert strategy"
- **System design monitoring:** "Design monitoring system", "Design metrics service", "Design logging service"

### L5 vs L2 Distinction:
- **L5 (Observability):** "How do you monitor a system?" → Focus: Metrics, alerts, dashboards, escalation
- **L2 (Scale & Capacity):** "What breaks if traffic grows 10x?" → Focus: Identify bottlenecks, design for scale

### L5 vs P12 Distinction:
- **L5 (Observability):** "How do you monitor a system?" → Focus: Technical monitoring framework
- **P12 (Operational Excellence):** "How do you ensure system reliability?" → Focus: Operational process

### Red Flags (NOT L5):
- "What breaks if traffic grows 10x?" → L2 (Scale & Capacity)
- "How do you ensure system reliability?" → P12 (Operational Excellence)
- "How do you debug a metric?" → L1 (Data Trust)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Observability Framework** (HIGHEST PRIORITY)
2. ⚠️ **Dashboard Design** (MEDIUM)

**For Data Engineer:**
1. ✅ **Observability Framework** (HIGHEST) - Core framework
2. ✅ **Dashboard Design** (HIGH) - Practical application

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Observability Framework
**Questions:** ~15 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "How do you monitor X?" or "What dashboard would you build?" - core observability framework
- **Framework:** Key Metrics → Alerts → Dashboards → Escalation
- **Key Metrics:** Golden signals (Latency: p50/p95/p99, Error rate, Throughput/volume, Saturation: CPU, memory, queues), Business metrics (Conversions/success rate, Drops/failures, Revenue-impacting events), Data quality (if data system: Freshness, Completeness, Anomalies)
- **Alerts:** Symptom-based (preferred: User-visible errors, SLO burn rate, Missed business outcomes), Thresholds (Static: known limits, Dynamic: baseline deviation), Alert hygiene (Actionable, Low noise, Clear owner)
- **Dashboards:** Overview (Health at a glance: red/yellow/green, Key metrics visible immediately), Drill-down (By service, By region/segment, By time), Correlation (Deploys, Traffic spikes, Feature flags)
- **Escalation:** Ownership (On-call rotation, Clear runbooks), Response (Mitigate first, Roll back/degrade), Learning (Postmortem, Fix root cause, Improve signals)

**Concrete Examples:**
- "Monitor payments API: Metrics (Success rate, p95 latency, charge failures), Alerts (Success rate < 99% for 5 min, latency burn-rate), Dashboards (Payments health overview, errors by issuer/region), Escalation (Page payments on-call → rollback → postmortem)"
- "Observability: Define metrics, set up alerts, build dashboards, define escalation"

**Representative Questions (Do 5 only):**
- Q117: As the PM for Lyft, what dashboard would you build to track the health of the app? (health monitoring angle)
- Q361: Design a metrics and logging service. (metrics service design angle)
- Q362: Design a metrics service. (metrics service design angle)
- Q367: Design a monitoring system for 1000 web servers. (monitoring system design angle)
- Q368: Design a monitoring system for TikTok. (monitoring system design angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When designing observability, I use Key Metrics → Alerts → Dashboards → Escalation. First, I define Key Metrics: Golden signals (Latency: p50/p95/p99 response times, Error rate: percentage of failed requests, errors per second, Throughput/volume: requests per second, transactions per minute, Saturation: CPU, memory, queue depth, resource utilization), Business metrics (Conversions/success rate: business outcome metrics, Drops/failures: user-facing failures, drop-off rates, Revenue-impacting events: payment failures, checkout issues), Data quality (if data system: Freshness - data update frequency, latency, Completeness - missing records, coverage, Anomalies - unexpected patterns, outliers). Second, I set up Alerts: Symptom-based (preferred: User-visible errors - alerts on issues users experience, SLO burn rate - alert when SLO error budget is being consumed, Missed business outcomes - conversion drops, revenue impact), Thresholds (Static: known limits - e.g., error rate > 1%, Dynamic: baseline deviation - e.g., 3-sigma from normal), Alert hygiene (Actionable: alert tells us what to do, Low noise: only alerts on real issues, not false positives, Clear owner: who responds to this alert). Third, I build Dashboards: Overview (Health at a glance: red/yellow/green status, Key metrics visible immediately), Drill-down (By service: isolate which service has issues, By region/segment: geographic or user segment breakdown, By time: historical trends, time-series analysis), Correlation (Deploys: link metrics to deployment events, Traffic spikes: correlate with traffic patterns, Feature flags: see impact of feature toggles). Remember: Dashboards are for debugging, alerts are for action. Finally, I define Escalation: Ownership (On-call rotation: clear ownership, rotation schedule, Clear runbooks: documented response procedures), Response (Mitigate first: stop the bleeding, restore service, Roll back/degrade: revert changes or disable features), Learning (Postmortem: document what happened, why, and how to prevent, Fix root cause: address underlying issue, not just symptoms, Improve signals: update metrics, alerts, dashboards based on learnings). The key principle: If you can't answer 'Are users hurting right now?' in 10 seconds, your observability is broken."

**How to Adapt This Narrative for Each Question:**

- **Q117 (Lyft app health dashboard):** Focus on app health → "To build a dashboard for Lyft app health, I'd: Key Metrics (Golden signals: Latency - ride request response time, match time, Error rate - failed requests, API errors, Throughput - requests per second, rides per minute, Saturation - server CPU, memory, queue depth, Business metrics: Ride success rate - rides completed vs requested, Driver availability, Rider wait time, Revenue-impacting: Payment failures, booking failures), Alerts (Symptom-based: User-visible errors - ride requests failing, SLO burn rate - if latency SLO being consumed, Missed business outcomes - ride success rate drops, Thresholds: Static - error rate > 1%, Dynamic - 3-sigma deviation, Alert hygiene: Actionable - tells us which service, Low noise - only real issues, Clear owner - on-call rotation), Dashboards (Overview: Health at a glance - red/yellow/green, Key metrics - ride success rate, latency, error rate, Drill-down: By service - ride matching, payments, driver app, By region - city breakdown, By time - trends, Correlation: Deploys - link to deployments, Traffic spikes - peak hours, Feature flags - new features), Escalation (Ownership: On-call rotation, runbooks, Response: Mitigate first - rollback if needed, Learning: Postmortem, fix root cause). I'd prioritize: Ride success rate (business metric), Latency (user experience), Error rate (reliability)."

- **Q361 (Metrics and logging service):** Emphasize system design → "To design a metrics and logging service, I'd: Key Metrics (Golden signals: Latency - p50/p95/p99, Error rate, Throughput, Saturation, Business metrics: Application-specific, Data quality: Freshness, completeness, anomalies), Alerts (Symptom-based: User-visible errors, SLO burn rate, Thresholds: Static and dynamic, Alert hygiene: Actionable, low noise, clear owner), Dashboards (Overview: Health at a glance, Drill-down: By service, region, time, Correlation: Deploys, traffic, features), Escalation (Ownership: On-call, runbooks, Response: Mitigate, rollback, Learning: Postmortem, improve). System design: Metrics collection (Agents on servers, push/pull model), Storage (Time-series DB, retention policies), Query (API for dashboards, alerts), Scalability (Handle high volume, low latency). I'd design: Collection layer (Agents, SDKs), Storage layer (Time-series DB, log storage), Query layer (API, dashboards), Alert layer (Alerting engine, notification)."

---

### BUCKET 2: Dashboard Design
**Questions:** ~5 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Design a dashboard for X" or "What dashboard would you build?" - same framework, with focus on dashboard design
- **Approach:** Same observability framework, with focus on dashboard structure
- **Dashboard Structure:** Overview (Health at a glance), Drill-down (By dimension), Correlation (With events)
- **Design Principles:** User-focused (Who uses it? What do they need?), Actionable (Can they act on it?), Clear (Easy to understand)

**Concrete Examples:**
- "Sales dashboard: Overview (Revenue, deals, pipeline), Drill-down (By rep, by product, by region), Correlation (With campaigns, launches)"
- "Dashboard design: Overview for health, drill-down for debugging, correlation for context"

**Representative Questions (Do 5 only):**
- Q117: As the PM for Lyft, what dashboard would you build to track the health of the app? (dashboard design angle)
- Q181: Create geographic and demographic dashboards for weekly, monthly, and yearly analytics using order data (100M daily records for 5 years) and customer data (1B customers). (analytics dashboard angle)
- Q285: Design a dashboard that helps sales leaders monitor their product's performance. (sales dashboard angle)
- Q361: Design a metrics and logging service. (metrics service with dashboards angle)
- Q362: Design a metrics service. (metrics service with dashboards angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When designing dashboards, I use the same observability framework but focus on dashboard structure. I design Overview: Health at a glance (Red/yellow/green status, Key metrics visible immediately, User-focused - who uses this? What do they need?), Drill-down: By dimension (By service: isolate which service has issues, By region/segment: geographic or user segment breakdown, By time: historical trends, Actionable - can they act on it?), Correlation: With events (Deploys: link metrics to deployment events, Traffic spikes: correlate with traffic patterns, Feature flags: see impact of feature toggles, Clear - easy to understand). I prioritize based on user needs: Executives need high-level health, Engineers need drill-down, Operations need alerts. The key is making dashboards actionable and clear."

**How to Adapt This Narrative for Each Question:**

- **Q285 (Sales dashboard):** Focus on sales context → "To design a sales dashboard, I'd: Key Metrics (Business metrics: Revenue, deals closed, pipeline value, Conversion rate, Sales cycle length, ARPU, Golden signals: If technical - latency, error rate, Throughput: Deals per day, Data quality: Data freshness, completeness), Alerts (Symptom-based: Revenue drops, Pipeline issues, Missed business outcomes, Thresholds: Static - revenue targets, Dynamic - deviation from baseline, Alert hygiene: Actionable - tells sales team what to do, Low noise, Clear owner), Dashboards (Overview: Health at a glance - revenue vs target, deals closed, pipeline, Drill-down: By rep - individual performance, By product - product performance, By region - geographic breakdown, By time - trends, Correlation: With campaigns - marketing impact, With launches - product impact, With seasonality - time-based patterns), Escalation (Ownership: Sales ops, Response: Adjust strategy, Learning: Postmortem, improve). I'd prioritize: Revenue (primary metric), Pipeline (leading indicator), Conversion rate (efficiency)."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Observability Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Dashboard Design** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through observability framework in 2 minutes (Key Metrics → Alerts → Dashboards → Escalation)
- [ ] Define key metrics (Golden signals, business metrics, data quality)
- [ ] Set up alerts (Symptom-based, thresholds, alert hygiene)
- [ ] Design dashboards (Overview, drill-down, correlation)
- [ ] Define escalation (Ownership, response, learning)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the observability framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Key Metrics → Alerts → Dashboards → Escalation framework**, not memorizing answers

**Remember:** L5 is about observability. The framework: Key Metrics → Alerts → Dashboards → Escalation. Key principle: If you can't answer "Are users hurting right now?" in 10 seconds, your observability is broken.
