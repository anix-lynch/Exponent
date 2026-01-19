# P4 - Cohort / Retention / Churn

**Formula:** `Define Cohorts → Measure Retention → Identify Churn Drivers → Hypothesize → Fix`

---

## 🧠 Mental Model (ASCII Tree)

```
START
│
├─ 1) DEFINE COHORTS
│     ├─ By signup time?        (week / month)
│     ├─ By acquisition source? (ads / organic / referral)
│     ├─ By persona?            (power users / casual)
│     └─ By behavior?           (activated vs not)
│
├─ 2) MEASURE RETENTION
│     ├─ Retention curve (D1 / D7 / D30 / W4 / M3)
│     ├─ Compare cohorts side-by-side
│     ├─ Absolute level? (how low)
│     └─ Shape? (early cliff vs slow decay)
│
├─ 3) IDENTIFY CHURN DRIVERS
│     ├─ WHEN do users leave?
│     │     ├─ Day 0–1  → onboarding / activation
│     │     ├─ Week 1   → value not clear
│     │     └─ Month 1+ → habit / competition
│     │
│     ├─ WHO leaves more?
│     │     ├─ Specific segments?
│     │     └─ Specific channels?
│     │
│     └─ WHAT changes before churn?
│           ├─ Drop in key actions
│           ├─ Fewer sessions
│           └─ Feature not used
│
├─ 4) HYPOTHESIZE
│     ├─ If users churn early → activation gap
│     ├─ If one cohort worse  → acquisition mismatch
│     ├─ If usage drops first → value erosion
│     └─ If late churn        → lack of habit / reminders
│
└─ 5) FIX
      ├─ Improve onboarding / activation
      ├─ Tighten targeting
      ├─ Reinforce core value loop
      ├─ Add retention hooks (email, push, content)
      └─ Measure cohort again → did curve move?
```

---

## 📌 Sample: Monthly Retention Drop

**Question:**
"Monthly retention dropped from 40% to 25% for new users."

```
DEFINE COHORTS
├─ Cohort A: Users who signed up last month
├─ Cohort B: Users who signed up 2–3 months ago
└─ Split by channel: Ads vs Organic

MEASURE RETENTION
├─ D1 retention: same
├─ D7 retention: same
└─ M1 retention: ↓ only for Ads cohort

IDENTIFY CHURN DRIVERS
├─ Ads users:
│     ├─ Activate feature less
│     ├─ Fewer sessions after week 1
│     └─ Drop happens right after trial ends
│
└─ Organic users:
      └─ Stable retention

HYPOTHESIZE
├─ Ads are attracting low-intent users
├─ Trial-to-paid value not clear
└─ Core habit not formed in first week

FIX
├─ Change ad targeting → higher intent
├─ Redesign onboarding around "aha" action
├─ Add week-1 nudges to reinforce habit
└─ Re-check M1 retention for next cohort
```

---

## 🔑 Mental Shortcut

* **Early drop = activation problem**
* **One cohort worse = targeting problem**
* **Late decay = habit / value problem**

If you want, next we can do **P5 Segmentation** or loop back and tighten P3 + P4 together (they pair really well).
