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

---

## 📚 Detailed Example: Notion Cohort Analysis

**Notion is a perfect cohort example** because it has clear activation, habit, and expansion paths.

---

### Step 0: What "cohort" means (1 sentence)

> **A cohort = users who started at the same time (or same way), tracked forward together.**

---

### Step 1: Define the cohort (Notion example)

Let's pick **one clean cohort**:

```
Cohort: Users who signed up in January
Product: Notion
Plan: Free at signup
```

Assume:

* 1,000 users signed up in January

---

### Step 2: Choose the retention event (critical)

You must define **what "still active" means**.

For Notion, a good retention event is:

```
"User edits a page"
```

Not:

* login
* open app

Editing = real value.

---

### Step 3: Measure retention over time

Now track **that same 1,000 users** over time.

```
January cohort (1,000 users)

Day 1   → 600 edited a page   → 60% D1 retention
Day 7   → 420 edited a page   → 42% D7 retention
Day 30  → 300 edited a page   → 30% D30 retention
Month 3 → 220 edited a page   → 22% M3 retention
```

ASCII table:

```
Notion – January Cohort

Time      Active Users   Retention
D1        600             60%
D7        420             42%
D30       300             30%
M3        220             22%
```

This **curve shape** matters more than raw numbers.

---

### Step 4: Compare cohorts (this is the power move)

Now compare with **February cohort**.

```
February Cohort (1,000 users)

D1  → 650 (65%)
D7  → 500 (50%)
D30 → 420 (42%)
M3  → 390 (39%)
```

Side-by-side:

```
Month      Jan Cohort   Feb Cohort
D1           60%          65%
D7           42%          50%
D30          30%          42%
M3           22%          39%
```

📌 February is **strictly better**.

---

### Step 5: Ask the right PM question

Not:

> "Why did retention improve?"

But:

> **"What changed for February users?"**

Possible answers:

* New onboarding flow
* Better templates
* Team invite prompt earlier
* Faster time-to-first-doc

---

### Step 6: Segment the cohort (advanced but important)

Split January cohort:

```
January cohort
├─ Used a template at signup
│   └─ D30 retention = 45%
│
└─ Started with blank page
    └─ D30 retention = 18%
```

📌 Now you found a **retention driver**.

---

### Step 7: How this connects to revenue later

Retention → Expansion → Revenue

```
Users retained at M3
→ more likely to invite teammates
→ upgrade to Team plan
→ expansion revenue
```

Bad cohorts never expand.

---

### One-sentence interview answer (Notion version)

> "In Notion, we'd cohort users by signup month and track retention based on meaningful actions like page edits to understand whether onboarding and early value delivery are improving over time."

---

### Ultra-short memory hook

```
Cohort = start together
Retention = do value again
Compare cohorts = find what worked
```

---

If you want, next we can do **P5 Segmentation** or loop back and tighten P3 + P4 together (they pair really well).
