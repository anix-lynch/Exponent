# P12 - Operational Excellence

**Formula:** `Assess Current State → Identify Risks → Prioritize Fixes → Communicate Plan → Monitor`

---

## 🧠 Mental Model (ASCII Tree)

```
START: System / project is live (or about to ship) and must stay healthy
│
├─ 1) Assess Current State (WHAT is actually happening)
│   │
│   ├─ Define scope
│   │   ├─ Product / system boundaries
│   │   ├─ Owners (who's on-call / accountable)
│   │   └─ SLAs / expectations
│   │
│   └─ Baseline health
│       ├─ Availability (uptime, error rates)
│       ├─ Performance (latency, throughput)
│       ├─ Quality (bugs, data correctness)
│       └─ Operations (on-call load, manual work)
│
├─ 2) Identify Risks (WHAT could break)
│   │
│   ├─ Enumerate failure modes
│   │   ├─ Technical (scaling, dependencies)
│   │   ├─ Data (freshness, correctness)
│   │   ├─ Process (handoffs, approvals)
│   │   └─ People (bus factor, burnout)
│   │
│   └─ For each risk
│       ├─ Likelihood
│       ├─ Impact (blast radius)
│       └─ Detection difficulty
│
├─ 3) Prioritize Fixes (WHAT to fix first)
│   │
│   ├─ Rank risks by
│   │   ├─ Impact × Likelihood
│   │   └─ Time-to-detect × Time-to-recover
│   │
│   └─ Choose actions
│       ├─ Prevent (design changes)
│       ├─ Detect (metrics, alerts)
│       └─ Respond (runbooks, ownership)
│
├─ 4) Communicate Plan (ALIGN execution)
│   │
│   ├─ What we're fixing now vs later
│   ├─ Owners and timelines
│   ├─ Tradeoffs accepted
│   └─ Escalation paths
│
└─ 5) Monitor (KEEP it healthy)
    │
    ├─ Track leading indicators
    ├─ Review incidents + near-misses
    ├─ Update runbooks
    └─ Revisit risks regularly
```

---

## 🔑 Golden Rule

Operational excellence ≠ zero failures.
Operational excellence = **fail small, detect fast, recover predictably**.

---

## 📌 Sample: New Feature Launch Reliability

**Question:**
"How would you ensure a newly launched feature stays reliable at scale?"

```
START: Feature just launched
│
├─ 1) Assess Current State
│   ├─ SLA: 99.9% availability
│   ├─ Latency p95 < 300ms
│   └─ On-call owner defined
│
├─ 2) Identify Risks
│   ├─ Traffic spikes during peak hours
│   ├─ Downstream API dependency
│   ├─ Manual rollback process
│   └─ No alert on silent data failures
│
├─ 3) Prioritize Fixes
│   ├─ Add latency + error alerts (detect)
│   ├─ Circuit breaker for dependency (contain)
│   ├─ Automate rollback (respond)
│   └─ Load test before next release (prevent)
│
├─ 4) Communicate Plan
│   ├─ Week 1: alerts + dashboards
│   ├─ Week 2: rollback automation
│   └─ Known risk: peak-hour throttling
│
└─ 5) Monitor
    ├─ Weekly health review
    ├─ Postmortem on incidents
    └─ Update runbooks quarterly
```

---

## 📊 Risk Register (Quick Fill)

```
Risk | Likelihood | Impact | Detection | Mitigation
----------------------------------------------------
Traffic spike | High | High | Medium | Autoscaling
Dependency fail | Medium | High | Fast | Circuit breaker
Data lag | Low | High | Slow | Freshness alert
On-call fatigue | Medium | Medium | Fast | Rotation + tooling
```

---

## 💬 Language That Works

* "What's the blast radius if this fails?"
* "How would we know this is broken at 3am?"
* "What's our fastest safe rollback?"
* "What risk are we explicitly accepting?"

---

## 🔑 5-Second Recall

```
What can break?
→ How bad is it?
→ How fast do we notice?
→ How fast can we recover?
```

If you want, next we can compress **P9–P12 into a single ops + leadership cheat sheet**, or I can generate **mock interview answers** using this exact structure.
