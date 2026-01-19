# L3 - Cost / ROI

**Formula:** `Cost Drivers → Benefits → Breakeven → Decide`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "Is this worth building?"
│
├─ 1) Cost Drivers (WHAT do we pay?)
│   │
│   ├─ Build cost
│   │   ├─ Eng time (people × weeks)
│   │   ├─ Opportunity cost (what we don't build)
│   │   └─ One-time infra setup
│   │
│   ├─ Run cost
│   │   ├─ Compute / storage / bandwidth
│   │   ├─ Third-party APIs
│   │   └─ Support & ops
│   │
│   └─ Risk cost
│       ├─ Reliability risk
│       ├─ Compliance / legal
│       └─ Brand damage
│
├─ 2) Benefits (WHAT do we gain?)
│   │
│   ├─ Revenue
│   │   ├─ New users
│   │   ├─ Higher conversion
│   │   └─ ARPU / LTV lift
│   │
│   ├─ Cost savings
│   │   ├─ Automation
│   │   ├─ Infra reduction
│   │   └─ Support deflection
│   │
│   └─ Strategic
│       ├─ Learning
│       ├─ Moat / differentiation
│       └─ Risk reduction
│
├─ 3) Breakeven (WHEN does it pay back?)
│   │
│   ├─ Simple math
│   │   ├─ Monthly benefit
│   │   ├─ Monthly cost
│   │   └─ Payback period
│   │
│   └─ Sensitivity
│       ├─ Best case
│       ├─ Base case
│       └─ Worst case
│
└─ 4) Decide (WHAT do we do?)
    │
    ├─ Greenlight
    │   ├─ Short payback
    │   └─ Asymmetric upside
    │
    ├─ Scope down
    │   ├─ MVP first
    │   └─ Cheaper experiment
    │
    └─ Kill / Defer
        ├─ Long breakeven
        └─ High downside
```

---

## 🔑 Golden Rule

ROI is not "big upside."
It's **"good outcomes even if we're wrong."**

---

## 📌 Sample: Feature-Flag System Build Decision

**Question:**
"Should we build an internal feature-flag system?"

```
Costs
├─ Build: 3 eng × 1 month = ~$90k
├─ Run: $2k/month
│
Benefits
├─ Faster launches
├─ Fewer rollbacks
├─ Less on-call pain (~$8k/month saved)
│
Breakeven
├─ $90k / $8k ≈ 11 months
│
Decision
└─ Build MVP OR buy off-the-shelf
```

---

## 📊 Cost / ROI Sanity Checks

```
Check              | Question
-----------------------------------------
Unit economics     | Does usage scale cost?
Payback            | < 6–12 months?
Reversibility      | Can we undo this?
Fixed vs variable  | What grows with scale?
Alt options        | Buy vs build?
```

---

## 💬 Language That Wins Interviews

* "The biggest cost driver is ___, not infra."
* "Even in the downside case, we break even in ___ months."
* "This is only worth it if adoption exceeds ___."

---

## 🔑 5-Second Recall

```
What does it cost?
→ What does it return?
→ When do we break even?
→ Should we build, shrink, or kill?
```

If you want, next we can do **L4 – Constraints**, or I can compress **L3** into a **30-second interview answer** you can memorize.
