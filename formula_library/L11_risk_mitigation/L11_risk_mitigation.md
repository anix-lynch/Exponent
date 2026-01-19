# L11 - Risk Mitigation

**Formula:** `Enumerate Risks → Blast Radius → Mitigations → Monitor`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "What could go wrong?"
│
├─ 1) Enumerate Risks (LIST before judging)
│   │
│   ├─ Technical (bugs, downtime, data loss)
│   ├─ Data (quality, drift, leakage, bias)
│   ├─ Operational (on-call load, handoffs)
│   ├─ Legal / Compliance (PII, regulations)
│   └─ Business (revenue, trust, reputation)
│
│   ⚠ Rule: If you can't name it, you can't manage it
│
├─ 2) Assess Blast Radius (HOW bad is it?)
│   │
│   ├─ Users affected (1% vs 100%)
│   ├─ Duration (minutes vs weeks)
│   ├─ Reversibility (easy rollback vs permanent)
│   └─ Visibility (internal vs public)
│
│   Output: Risk = Probability × Impact
│
├─ 3) Prioritize (NOT all risks deserve fixes)
│   │
│   ├─ High impact + high probability → ACT
│   ├─ High impact + low probability → PLAN
│   ├─ Low impact + high probability → AUTOMATE
│   └─ Low impact + low probability → ACCEPT
│
├─ 4) Mitigate (REDUCE impact or probability)
│   │
│   ├─ Prevent: guardrails, validation, limits
│   ├─ Detect: monitoring, alerts
│   ├─ Contain: rate limits, feature flags
│   └─ Recover: rollback, backups, runbooks
│
├─ 5) Monitor (ASSUME failure will happen)
│   │
│   ├─ Early warning metrics
│   ├─ Alert thresholds
│   └─ Clear owner + escalation path
│
└─ OUTPUT: "If X happens, we detect in Y mins and recover in Z."
```

---

## 📊 Risk Types → Typical Mitigations

```
| Risk Type     | Example                    | Mitigation                     |
|---------------|----------------------------|--------------------------------|
| Data          | Bad input                  | Validation + sanity checks     |
| Model         | Drift                      | Drift monitoring               |
| Infra         | Traffic spike              | Rate limits + autoscaling      |
| Product       | Bad launch                 | Feature flags + phased rollout |
| Legal         | PII exposure               | Access control + audits        |
```

---

## 🚨 Anti-Patterns (Red Flags)

```
✗ "Low probability" with huge impact ignored
✗ No owner for a risk
✗ Alerts without action plans
✗ One big mitigation instead of layers
✗ Learning only after an outage
```

---

## 📌 Interview Example: ML Model Launch

**Question:**
"What risks would you consider before launching a new ML model?"

```
Risks
├─ Prediction drift
├─ Biased outcomes
├─ Latency regression

Blast Radius
├─ Affects recommendations for all users

Mitigation
├─ Shadow deploy
├─ Canary rollout
├─ Drift + latency alerts

Monitor
└─ Auto-rollback on threshold breach
```

---

## 💬 One-Liners You Can Drop

* "Risk = probability × blast radius."
* "You don't eliminate risk — you bound it."
* "Detection speed matters more than perfection."
* "Assume failure, design recovery."

---

## 🔑 5-Second Recall

```
List → Size → Fix → Watch
```

Next: **L12 – Metrics Interpretation**, or want a **rapid L1–L11 drill** to lock everything in.
