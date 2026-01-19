# P5 - Segmentation

**Formula:** `(Persona × Behavior × Value) → Rank → Focus Top Segments`

---

## 🧠 Mental Model (ASCII Tree)

```
START
│
├─► Define PERSONAS (WHO)
│    ├─ Demographics (age, role, company size)
│    ├─ Context (job-to-be-done, environment)
│    └─ Needs / constraints
│
├─► Define BEHAVIORS (HOW)
│    ├─ Frequency (daily / weekly / occasional)
│    ├─ Depth (light vs power usage)
│    └─ Lifecycle stage (new / active / mature)
│
├─► Define VALUE (WHY THEY MATTER)
│    ├─ Revenue (ARPU, LTV)
│    ├─ Strategic value (growth, network effects)
│    └─ Cost / risk (support, churn risk)
│
├─► Combine into SEGMENTS
│    ├─ Persona A × Behavior X × High Value
│    ├─ Persona B × Behavior Y × Medium Value
│    └─ Persona C × Behavior Z × Low Value
│
├─► RANK SEGMENTS
│    ├─ Impact on core metric
│    ├─ Size / growth potential
│    └─ Effort to serve
│
└─► FOCUS
     ├─ Primary segment (default design target)
     ├─ Secondary segment (nice-to-have)
     └─ Deprioritize / ignore the rest
```

---

## 📌 Sample: Productivity App User Focus

**Question:**
"Which users should we focus on for a productivity app?"

```
GOAL: Improve retention + revenue
│
├─► PERSONAS
│    ├─ Students
│    ├─ Individual professionals
│    └─ Team managers
│
├─► BEHAVIORS
│    ├─ Light users (task lists only)
│    ├─ Power users (projects, automations)
│    └─ Collaborative users (shared boards)
│
├─► VALUE
│    ├─ Low: Free users, low engagement
│    ├─ Medium: Individual paid users
│    └─ High: Teams (multiple seats, low churn)
│
├─► SEGMENTS (Persona × Behavior × Value)
│    ├─ Students × Light × Low
│    ├─ Professionals × Power × Medium
│    └─ Managers × Collaborative × High
│
├─► RANKING
│    ├─ Managers × Collaborative × High  → ⭐⭐⭐
│    ├─ Professionals × Power × Medium   → ⭐⭐
│    └─ Students × Light × Low            → ⭐
│
└─► DECISION
     ├─ PRIMARY FOCUS: Team managers
     ├─ DESIGN FOR: Collaboration, permissions, reporting
     └─ DEPRIORITIZE: Student-only features
```

---

## 🔑 When to Instantly Recognize P5 in Interviews

```
If the question asks:
- "Which users should we focus on?"
- "Who is the most valuable segment?"
- "Different users behave differently — what do we do?"
- "We can't serve everyone — who matters most?"

→ This is P5 Segmentation
```

---

If you want, next we can do **P6 Prioritization (RICE)** in the same ASCII + sample style, or compress P5 into a **1-glance cheat card** for interview recall.
