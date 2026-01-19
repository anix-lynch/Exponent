# L4 - Constraints

**Formula:** `Legal → Technical → Organizational → Timeline → Prioritize`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "What limits us?"
│
├─ 1) Legal / Regulatory (WHAT are we not allowed to do?)
│   │
│   ├─ Compliance
│   │   ├─ GDPR / CCPA / HIPAA
│   │   ├─ Data residency
│   │   └─ Consent requirements
│   │
│   ├─ Contracts
│   │   ├─ Vendor terms
│   │   ├─ Partner SLAs
│   │   └─ Licensing limits
│   │
│   └─ Risk exposure
│       ├─ Fines / penalties
│       ├─ Lawsuits
│       └─ Regulatory scrutiny
│
├─ 2) Technical (WHAT can't the system do today?)
│   │
│   ├─ Architecture
│   │   ├─ Legacy systems
│   │   ├─ Tight coupling
│   │   └─ Data quality gaps
│   │
│   ├─ Scale limits
│   │   ├─ Latency
│   │   ├─ Throughput
│   │   └─ Reliability
│   │
│   └─ Dependencies
│       ├─ External APIs
│       ├─ Data availability
│       └─ Infra readiness
│
├─ 3) Organizational (WHO blocks or enables this?)
│   │
│   ├─ People
│   │   ├─ Hiring gaps
│   │   ├─ Specialized expertise
│   │   └─ On-call ownership
│   │
│   ├─ Incentives
│   │   ├─ Team OKRs misaligned
│   │   ├─ Competing priorities
│   │   └─ Political resistance
│   │
│   └─ Process
│       ├─ Review cycles
│       ├─ Approval chains
│       └─ Cross-team coordination
│
├─ 4) Timeline (WHEN does this break?)
│   │
│   ├─ Fixed deadlines
│   │   ├─ Launch dates
│   │   ├─ Regulatory deadlines
│   │   └─ Contract renewals
│   │
│   ├─ Sequencing
│   │   ├─ Must-do-first work
│   │   ├─ Long-lead items
│   │   └─ Critical path
│   │
│   └─ Opportunity cost
│       ├─ What slips if this ships?
│       └─ What breaks if it's late?
│
└─ 5) Prioritize (WHAT do we do about it?)
    │
    ├─ Hard constraints (NON-NEGOTIABLE)
    │   ├─ Legal / safety
    │   └─ External deadlines
    │
    ├─ Soft constraints (NEGOTIABLE)
    │   ├─ Scope
    │   ├─ UX polish
    │   └─ Internal tooling
    │
    └─ Strategy
        ├─ Redesign to avoid constraint
        ├─ Phase rollout
        └─ Explicitly accept risk
```

---

## 🔑 Golden Rule

Constraints are not excuses.
They are **design inputs**.

Good answers say **what you'll trade**, not just **what you can't do**.

---

## 📌 Sample: Global Feature Launch

**Question:**
"Why can't we launch this feature globally?"

```
Legal
├─ GDPR requires explicit consent
│
Technical
├─ EU data not isolated yet
│
Org
├─ Legal review takes 4–6 weeks
│
Timeline
├─ Marketing launch in 2 weeks
│
Decision
└─ Launch US-only → EU in Phase 2
```

---

## 📊 Constraint Sanity Checks

```
Check                | Question
--------------------------------------------
Hard vs soft         | Is this truly non-negotiable?
Avoid vs mitigate    | Can we design around it?
Temporary vs permanent| Does this expire?
Owner                | Who must say "yes"?
Cost of waiting       | What breaks if we delay?
```

---

## 💬 Language That Wins Interviews

* "The binding constraint here is ___, not engineering effort."
* "Legally this is non-negotiable, so we adjust scope instead."
* "We can unblock this by sequencing ___ first."
* "This is a soft constraint we're choosing to accept."

---

## 🔑 5-Second Recall

```
What are we legally blocked from?
→ What can't the system do?
→ Who slows this down?
→ What deadlines force tradeoffs?
→ What do we change, phase, or accept?
```

If you want, next we can do **L5 – Observability** in the same deep-tree format, or I can compress **L4** into a **20-second spoken answer** for interviews.
