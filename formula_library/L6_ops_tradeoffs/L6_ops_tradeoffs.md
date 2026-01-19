# L6 - Ops Tradeoffs

**Formula:** `Speed vs Quality vs Reliability → SLAs → Error Budget → Decide`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "What do we optimize for when things conflict?"
│
├─ 1) Speed vs Quality vs Reliability (pick the tension)
│   │
│   ├─ Speed
│   │   ├─ Fast deploys
│   │   ├─ Rapid iteration
│   │   └─ Short time-to-market
│   │
│   ├─ Quality
│   │   ├─ Fewer bugs
│   │   ├─ Correctness
│   │   └─ User trust
│   │
│   └─ Reliability
│       ├─ Uptime
│       ├─ Consistency
│       └─ Predictability
│
│   ⚠ Rule: You can maximize **2**, never all 3
│
├─ 2) SLAs / SLOs (WHAT do we promise?)
│   │
│   ├─ SLI (signal)
│   │   ├─ Availability
│   │   ├─ Latency
│   │   └─ Success rate
│   │
│   ├─ SLO (target)
│   │   ├─ 99.9% uptime
│   │   ├─ p95 < 300ms
│   │   └─ <0.1% errors
│   │
│   └─ SLA (external promise)
│       └─ What customers can hold you to
│
├─ 3) Error Budget (HOW much can we break?)
│   │
│   ├─ Error Budget = 1 − SLO
│   │   ├─ 99.9% SLO → 0.1% budget
│   │   └─ Budget = permission to move fast
│   │
│   ├─ Budget healthy?
│   │   ├─ YES → Ship faster
│   │   └─ NO  → Freeze launches, fix reliability
│   │
│   └─ Shared contract
│       ├─ Product wants speed
│       └─ Ops wants stability
│
└─ 4) Decide + Communicate
    │
    ├─ Make tradeoff explicit
    ├─ Align stakeholders
    └─ Revisit when conditions change
```

---

## 🔑 Golden Rule

If tradeoffs are implicit,
someone is silently paying the cost (usually users or on-call).

---

## 📌 Sample: Fast Releases vs Uptime

**Question:**
"How do you balance fast releases with uptime?"

```
Tradeoff
├─ Default: Speed + Reliability
├─ Accept slightly lower quality via flags
│
SLO
├─ 99.9% availability
│
Error Budget
├─ Healthy → canary deploys OK
├─ Burned → freeze features
│
Decision
└─ Slow down launches until budget recovers
```

---

## 📊 When to Bias Each Side

```
Situation                    | Bias Toward
------------------------------------------------
Early startup                | Speed
Regulated / payments system  | Reliability
Core user-facing feature     | Quality
Incident ongoing             | Reliability
Innovation window open       | Speed
```

---

## 💬 Interview One-Liners

* "Error budgets turn reliability into a product decision."
* "Speed is allowed until the error budget is gone."
* "Reliability is a feature with a cost."
* "Tradeoffs should be explicit, not accidental."

---

## 🔑 5-Second Recall

```
What are we optimizing?
→ What do we promise?
→ How much can we fail?
→ When do we slow down?
```

Next options:
• **L7 – Data Modeling**
• **L8 – Market / Competitive**
• or compress **L6** into a **20-second spoken answer** you can recite cleanly.
