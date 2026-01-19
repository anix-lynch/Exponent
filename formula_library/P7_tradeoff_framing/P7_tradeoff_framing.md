# P7 - Tradeoff Framing

**Formula:** `Define Options → Winners / Losers → Guardrails → Decide + Communicate`

---

## 🧠 Mental Model (ASCII Tree)

```
START
│
├─ 1) DEFINE OPTIONS
│   ├─ Option A
│   ├─ Option B
│   └─ (Option C if needed)
│
├─ 2) WINNERS / LOSERS (by option)
│   ├─ Users
│   ├─ Business
│   ├─ Engineering / Ops
│   └─ Long-term Strategy
│
├─ 3) GUARDRAILS (non-negotiables)
│   ├─ Must not break X
│   ├─ Must stay within Y
│   └─ Must protect Z
│
└─ 4) DECIDE + COMMUNICATE
    ├─ Pick option
    ├─ Why this option
    ├─ What we're giving up
    └─ How we'll monitor risk
```

---

## 📌 Canonical Question Types

* "Should we do **A or B**?"
* "Is it worth trading **X for Y**?"
* "What are we giving up if we choose this?"
* "Why not the other option?"

---

## 📌 Sample: Google Flights Ads Decision

**Question:**
"Should Google Flights introduce ads?"

```
START
│
├─ DEFINE OPTIONS
│   ├─ Option A: No Ads
│   └─ Option B: Introduce Ads
│
├─ WINNERS / LOSERS
│
│   Option A: No Ads
│   ├─ Users: Clean UX, high trust
│   ├─ Business: Missed revenue
│   ├─ Brand: Strong long-term trust
│   └─ Risk: Slower monetization
│
│   Option B: Ads
│   ├─ Users: Worse experience, bias risk
│   ├─ Business: New revenue stream
│   ├─ Advertisers: New channel
│   └─ Risk: Trust erosion
│
├─ GUARDRAILS
│   ├─ Must not bias flight rankings
│   ├─ Must clearly label ads
│   ├─ Must cap ad density
│   └─ Must monitor user trust metrics
│
└─ DECIDE + COMMUNICATE
    ├─ Decision: Introduce limited ads
    ├─ Rationale: Revenue > UX cost if constrained
    ├─ Tradeoff Accepted: Slight UX degradation
    └─ Monitoring: CTR, conversion, trust surveys
```

---

## 🎯 One-Line Answer Template (Interview-Ready)

> "I'd frame this as a tradeoff between **X and Y**. Option A benefits ___ but costs ___. Option B unlocks ___ but risks ___. With guardrails around ___, I'd choose ___ and monitor ___."

---

## 🚨 Common Failure Modes (Avoid These)

* ❌ Listing pros/cons without **choosing**
* ❌ Ignoring who **loses**
* ❌ No guardrails → sounds reckless
* ❌ No monitoring plan

---

If you want, next we can do **P8 – Experiment Design** or stack **P7 + P10 (Exec Comms)** to answer like a staff-level PM.
