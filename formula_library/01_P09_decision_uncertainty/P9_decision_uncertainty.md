# P9 - Decision Under Uncertainty

**Formula:** `Clarify Assumptions → Identify Risks → Validation Plan → Decide`

---

## 🧠 Mental Model (ASCII Tree)

```
START: We must decide, but information is incomplete
│
├─ 1) Clarify Assumptions
│   │
│   ├─ What do we believe is true?
│   │   ├─ User behavior assumptions
│   │   ├─ Market / demand assumptions
│   │   ├─ Technical feasibility assumptions
│   │   └─ Timing / dependency assumptions
│   │
│   └─ Classify assumptions
│       ├─ Critical (decision breaks if wrong)
│       └─ Non-critical (nice to know)
│
├─ 2) Identify Risks
│   │
│   ├─ If assumption is wrong, what happens?
│   │   ├─ Revenue risk
│   │   ├─ User trust / UX risk
│   │   ├─ Technical / scalability risk
│   │   ├─ Legal / compliance risk
│   │   └─ Opportunity cost
│   │
│   └─ Rank risks
│       ├─ High impact × high likelihood → MUST address
│       └─ Low impact or low likelihood → monitor
│
├─ 3) Validation Plan
│   │
│   ├─ What is the cheapest signal to reduce uncertainty?
│   │   ├─ Qualitative: user interviews, expert review
│   │   ├─ Quantitative: logs, metrics, small experiments
│   │   ├─ Proxies: analogous products, historical data
│   │   └─ Time-boxed spike / prototype
│   │
│   └─ Decide upfront
│       ├─ What result would change the decision?
│       └─ What result is "good enough" to proceed?
│
└─ 4) Decide
    │
    ├─ Option A: Proceed now
    │   └─ If upside >> downside and risks are bounded
    │
    ├─ Option B: Delay and validate
    │   └─ If one critical unknown dominates
    │
    └─ Option C: Kill / pivot
        └─ If downside is irreversible or catastrophic
```

---

## 📌 Sample: AI Auto-Reply Feature Launch

**Question:**
"Should we launch a new AI-powered auto-reply feature for customer support?"

```
START: Launch AI auto-reply?
│
├─ 1) Clarify Assumptions
│   ├─ Users trust AI-generated replies
│   ├─ AI replies reduce support workload
│   └─ Errors will be rare and acceptable
│
├─ 2) Identify Risks
│   ├─ Wrong reply → user trust damage (HIGH)
│   ├─ Legal/compliance issues (MEDIUM)
│   ├─ Minimal efficiency gain (LOW)
│
├─ 3) Validation Plan
│   ├─ Shadow mode: AI drafts, humans approve
│   ├─ Measure: % usable replies, correction rate
│   ├─ Interview top support agents
│   └─ 2-week time box
│
└─ 4) Decide
    ├─ If ≥70% replies usable → limited beta
    ├─ If <70% but improving → iterate + delay
    └─ If trust issues severe → kill feature
```

---

## 🔑 Mental Shortcut (5-second recall)

```
What must be true?
→ What breaks if it's false?
→ What's the cheapest proof?
→ Decide with guardrails
```

If you want, next we can continue with **P10 – Executive Communication** in the same ASCII + sample format, or convert all P1–P9 into a single printable cheat sheet.
