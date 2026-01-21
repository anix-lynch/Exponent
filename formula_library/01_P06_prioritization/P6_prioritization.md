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

---

## 📚 4 Representative P6 Sample Answers (RICE Framework)

### 1️⃣ YouTube PM: AI Tool for Creator Ideas & Scripts

**Question:**
"As a YouTube PM, how would you evaluate building an AI tool to auto-generate creator ideas & scripts?"

#### Step 1) List candidates

* **A. Idea generator only** (titles + outlines)
* **B. Full script generation**
* **C. Analytics-driven idea suggestions** (based on channel history)

#### Step 2) Score (RICE)

| Feature                   | Impact | Confidence | Ease | RICE    |
| ------------------------- | ------ | ---------- | ---- | ------- |
| A. Idea generator         | 2      | 0.7        | 3    | **4.2** |
| B. Full scripts           | 3      | 0.4        | 1    | **1.2** |
| C. Analytics-driven ideas | 3      | 0.7        | 2    | **4.2** |

#### Step 3–4) Rank

1. **A / C (tie)**
2. B

#### Step 5) Decide + Communicate

* **Do first:** Idea generator + analytics-based suggestions
* **Delay:** Full script generation
* **Why:** High creator value with fast delivery; full scripts are risky, opinionated, and costly

---

### 2️⃣ OpenTable PM: Worst Post-Reservation Experiences

**Question:**
"As an OpenTable PM, how would you prioritize improving the worst post-reservation experiences?"

#### Step 1) List candidates

* **A. Real-time reservation confirmation**
* **B. Easy modification / cancellation flow**
* **C. Post-booking reminder + directions**

#### Step 2) Score

| Feature            | Impact | Confidence | Ease | RICE    |
| ------------------ | ------ | ---------- | ---- | ------- |
| A. Confirmation    | 3      | 1.0        | 2    | **6.0** |
| B. Modify / cancel | 2      | 0.7        | 3    | **4.2** |
| C. Reminders       | 1      | 0.7        | 3    | **2.1** |

#### Step 3–4) Rank

1. **A**
2. B
3. C

#### Step 5) Decide + Communicate

* **Do first:** Real-time confirmation (reduces no-shows, anxiety)
* **Delay:** Reminders
* **Why:** Highest impact + strongest data signal

---

### 3️⃣ TPM: Timeline Cut in Half

**Question:**
"As a TPM, how do you handle unchanged deliverables but timeline cut in half?"

#### Step 1) List candidates

* **A. Cut non-critical scope**
* **B. Parallelize work streams**
* **C. Add temporary staffing**

#### Step 2) Score

| Option         | Impact | Confidence | Ease | RICE    |
| -------------- | ------ | ---------- | ---- | ------- |
| A. Cut scope   | 3      | 1.0        | 3    | **9.0** |
| B. Parallelize | 2      | 0.7        | 2    | **2.8** |
| C. Add staff   | 1      | 0.4        | 1    | **0.4** |

#### Step 3–4) Rank

1. **A**
2. B
3. C

#### Step 5) Decide + Communicate

* **Do first:** Ruthless scope cuts to preserve core deliverables
* **Delay/Avoid:** Hiring as a primary lever
* **Why:** Scope control is the only lever that reliably works under time compression

---

### 4️⃣ Engineering: Foundational Work vs New Features

**Question:**
"How do you balance foundational engineering work vs new features?"

#### Step 1) List candidates

* **A. Infra work blocking feature velocity**
* **B. Feature requested by top customers**
* **C. Tech debt cleanup with no user visibility**

#### Step 2) Score

| Work                 | Impact | Confidence | Ease | RICE    |
| -------------------- | ------ | ---------- | ---- | ------- |
| A. Blocking infra    | 3      | 1.0        | 2    | **6.0** |
| B. Customer feature  | 2      | 0.7        | 2    | **2.8** |
| C. General tech debt | 1      | 0.7        | 1    | **0.7** |

#### Step 3–4) Rank

1. **A**
2. B
3. C

#### Step 5) Decide + Communicate

* **Prioritize:** Infra that unlocks multiple features
* **Deprioritize:** Invisible tech debt without clear leverage
* **Why:** Foundational work only wins when it compounds future impact

---

## 🎯 Pattern Interviewers Want to See

* ✅ Clear **options**
* ✅ **Numbers > opinions**
* ✅ Explicit **tradeoffs**
* ✅ A confident **decision**

---

If you want, next we can do **P7 Tradeoff Framing** in the same ASCII + sample style.
