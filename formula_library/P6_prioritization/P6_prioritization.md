# P6 - Prioritization

**Formula:** `Impact × Confidence × Ease → RICE Score → Decide + Communicate`

---

## 🧠 Mental Model (ASCII Tree)

```
Start
│
├─ 1) List Candidates
│     ├─ Feature A
│     ├─ Feature B
│     └─ Feature C
│
├─ 2) Score Each Candidate
│     │
│     ├─ Impact (How big is the upside?)
│     │     ├─ 3 = massive user/business impact
│     │     ├─ 2 = meaningful but local
│     │     └─ 1 = minor improvement
│     │
│     ├─ Confidence (How sure are we?)
│     │     ├─ 1.0 = strong data / past proof
│     │     ├─ 0.7 = some data / informed guess
│     │     └─ 0.4 = mostly hypothesis
│     │
│     └─ Ease (How hard is it?)
│           ├─ 3 = very easy / quick win
│           ├─ 2 = medium effort
│           └─ 1 = hard / long-term
│
├─ 3) Compute RICE
│     └─ RICE = Impact × Confidence × Ease
│
├─ 4) Rank by RICE Score
│
└─ 5) Decide + Communicate
      ├─ What we do first
      ├─ What we delay
      └─ Why (tradeoffs)
```

---

## 📌 Sample: Feature Prioritization

**Question:**
"We have 3 features to build next quarter. What should we prioritize?"

```
Candidates
│
├─ Feature A: Improve onboarding tutorial
├─ Feature B: New advanced analytics dashboard
└─ Feature C: Refactor backend for performance
```

```
Scoring
│
├─ Feature A
│     Impact    = 3   (affects all new users)
│     Confidence= 0.9 (data shows onboarding drop-off)
│     Ease      = 3   (mostly UI + copy)
│     RICE      = 3 × 0.9 × 3 = 8.1
│
├─ Feature B
│     Impact    = 2   (power users only)
│     Confidence= 0.6 (customer requests, no hard data)
│     Ease      = 1   (complex build)
│     RICE      = 2 × 0.6 × 1 = 1.2
│
└─ Feature C
      Impact    = 2   (indirect user benefit)
      Confidence= 0.7 (known latency issues)
      Ease      = 2   (moderate effort)
      RICE      = 2 × 0.7 × 2 = 2.8
```

```
Ranking
│
├─ #1 Feature A (8.1)
├─ #2 Feature C (2.8)
└─ #3 Feature B (1.2)
```

```
Decision
│
├─ Build Feature A first → biggest impact, high confidence, easy
├─ Schedule Feature C next → solid ROI, technical health
└─ Defer Feature B → low ROI right now
```

---

## 🔑 One-Line Interview Closer

```
"I prioritize using a simple RICE-style framework: maximize impact,
discount uncertainty, factor effort, then communicate why some things wait."
```

If you want, next we can do **P7 Tradeoff Framing** in the same ASCII + sample style.
