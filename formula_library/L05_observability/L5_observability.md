# L5 - Observability

**Formula:** `Key Metrics → Alerts → Dashboards → Escalation`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "How do we know this system is healthy?"
│
├─ 1) Key Metrics (WHAT do we measure?)
│   │
│   ├─ Golden signals
│   │   ├─ Latency (p50 / p95 / p99)
│   │   ├─ Error rate
│   │   ├─ Throughput / volume
│   │   └─ Saturation (CPU, memory, queues)
│   │
│   ├─ Business metrics
│   │   ├─ Conversions / success rate
│   │   ├─ Drops / failures
│   │   └─ Revenue-impacting events
│   │
│   └─ Data quality (if data system)
│       ├─ Freshness
│       ├─ Completeness
│       └─ Anomalies
│
├─ 2) Alerts (WHEN do we wake someone?)
│   │
│   ├─ Symptom-based (preferred)
│   │   ├─ User-visible errors
│   │   ├─ SLO burn rate
│   │   └─ Missed business outcomes
│   │
│   ├─ Thresholds
│   │   ├─ Static (known limits)
│   │   └─ Dynamic (baseline deviation)
│   │
│   └─ Alert hygiene
│       ├─ Actionable
│       ├─ Low noise
│       └─ Clear owner
│
├─ 3) Dashboards (HOW do we debug fast?)
│   │
│   ├─ Overview
│   │   ├─ Health at a glance
│   │   └─ Red / yellow / green
│   │
│   ├─ Drill-down
│   │   ├─ By service
│   │   ├─ By region / segment
│   │   └─ By time
│   │
│   └─ Correlation
│       ├─ Deploys
│       ├─ Traffic spikes
│       └─ Feature flags
│
└─ 4) Escalation (WHAT happens next?)
    │
    ├─ Ownership
    │   ├─ On-call rotation
    │   └─ Clear runbooks
    │
    ├─ Response
    │   ├─ Mitigate first
    │   └─ Roll back / degrade
    │
    └─ Learning
        ├─ Postmortem
        ├─ Fix root cause
        └─ Improve signals
```

---

## 🔑 Golden Rule

If you can't answer **"Are users hurting right now?"** in 10 seconds,
your observability is broken.

---

## 📌 Sample: Payments API Monitoring

**Question:**
"How would you monitor a payments API?"

```
Metrics
├─ Success rate
├─ p95 latency
├─ Charge failures by reason
│
Alerts
├─ Success rate < 99% for 5 min
├─ Latency burn-rate alert
│
Dashboards
├─ Payments health overview
├─ Errors by issuer / region
│
Escalation
└─ Page payments on-call → rollback → postmortem
```

---

## 📊 Observability Sanity Checks

```
Check                | Question
-------------------------------------------
User impact          | Would users notice?
Actionability        | Do we know what to do?
Noise                | Would this page often?
Coverage             | Do we see failures early?
Correlation          | Can we link cause → effect?
```

---

## 💬 Language That Wins Interviews

* "I alert on symptoms, not CPU."
* "Dashboards are for debugging, alerts are for action."
* "If everything pages, nothing pages."
* "Metrics without ownership are just charts."

---

## 🔑 5-Second Recall

```
What do we measure?
→ When do we alert?
→ How do we debug?
→ Who responds and learns?
```

If you want, next we can do **L6 – Ops Tradeoffs**, or I can compress **L5** into a **30-second spoken answer** you can memorize, B chan.
