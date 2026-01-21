# P3 - Funnel Analysis

**Formula:** `Define Funnel Steps → Measure Drop-off → Identify Friction → Hypothesize Fix → Test`

---

## 🧠 Mental Model (ASCII Tree)

```
START
│
├─ 1) DEFINE FUNNEL STEPS
│   ├─ What is the exact user journey?
│   │   ├─ Step 1: Entry (impression / visit)
│   │   ├─ Step 2: Activation (sign-up / click / view)
│   │   ├─ Step 3: Core Action (search / add / message)
│   │   ├─ Step 4: Conversion (purchase / booking / post)
│   │   └─ Step 5: Success (repeat / retention)
│   │
│   └─ Guardrail:
│       └─ Steps must be USER actions (not internal events)
│
├─ 2) MEASURE DROP-OFF
│   ├─ Compute conversion between each step
│   │   ├─ Step 1 → 2: X%
│   │   ├─ Step 2 → 3: Y%
│   │   ├─ Step 3 → 4: Z%
│   │
│   └─ Identify:
│       └─ Largest % drop (this is the bottleneck)
│
├─ 3) IDENTIFY FRICTION
│   ├─ Ask WHY users fail at this step
│   │   ├─ UX friction? (confusing, slow, too many fields)
│   │   ├─ Trust friction? (price shock, permissions, privacy)
│   │   ├─ Value friction? (unclear benefit)
│   │   ├─ Technical friction? (bugs, latency)
│   │   └─ Segment-specific? (new vs power users)
│   │
│   └─ Use:
│       ├─ Session replays
│       ├─ Funnel by segment
│       └─ Qual + logs
│
├─ 4) HYPOTHESIZE FIX
│   ├─ Generate 1–2 clear hypotheses
│   │   ├─ If we reduce friction X,
│   │   └─ Then conversion at step Y increases
│   │
│   └─ Prioritize:
│       ├─ High impact
│       ├─ Low effort
│       └─ Isolated to one step
│
├─ 5) TEST
│   ├─ A/B test or staged rollout
│   ├─ Primary metric = step conversion
│   ├─ Guardrails = downstream impact
│   └─ Decide: ship / iterate / rollback
│
END
```

---

## 📌 Sample: E-commerce Checkout Conversion Drop

**Question:**
"Checkout conversion dropped on an e-commerce site. What do you do?"

```
1) DEFINE FUNNEL
   Visit → Product View → Add to Cart → Checkout → Purchase

2) MEASURE DROP-OFF
   Visit → Product View: 65%
   Product View → Add to Cart: 18%
   Add to Cart → Checkout: 70%
   Checkout → Purchase: 42%   ❌ BIGGEST DROP

3) IDENTIFY FRICTION (Checkout Step)
   ├─ Unexpected shipping cost?
   ├─ Forced account creation?
   ├─ Payment errors on mobile?
   └─ Slow load time (>5s)?

4) HYPOTHESIZE FIX
   Hypothesis A:
   ├─ If we show shipping cost earlier,
   └─ Then checkout → purchase improves

   Hypothesis B:
   ├─ If we allow guest checkout,
   └─ Then mobile conversion improves

5) TEST
   ├─ A/B test guest checkout
   ├─ Metric: checkout → purchase %
   ├─ Guardrail: fraud, refund rate
   └─ Ship winner
```

---

## 🔑 Mental Shortcut (Interview Mode)

```
"First I define the funnel.
Then I find the biggest drop.
Then I ask why users get stuck.
Then I propose a fix.
Then I test it."
```

---

## 📚 Universal Funnel Answer Template (Memorize This)

```
1) Define the funnel steps
2) Find the biggest drop
3) Hypothesize why (UX / value / trust / tech)
4) Propose 1–2 fixes
5) Measure again
```

You'll see it repeated in all examples below.

---

## 📚 5 Funnel Analysis Drill Examples

### 1️⃣ "55% of users don't complete the application"

**Sample answer:**

```
Define funnel:
- Open application
- Start application
- Fill form
- Submit

Find drop:
- Biggest drop between Fill form → Submit

Hypothesis:
- Form too long
- Required fields unclear
- Users unsure why info is needed

Fix:
- Reduce required fields
- Add progress bar
- Save progress

Measure:
- Submission rate
```

---

### 2️⃣ "25% drop-off during sign-up"

**Sample answer:**

```
Define funnel:
- App open
- Click sign up
- Enter email/password
- Verify email
- Complete sign-up

Find drop:
- Drop at email verification

Hypothesis:
- Verification email slow
- Email goes to spam
- User distracted

Fix:
- Allow limited access before verification
- Resend CTA
- Inline verification

Measure:
- Sign-up completion rate
```

---

### 3️⃣ "Adoption is high, but retention is low"

**Sample answer:**

```
Define funnel:
- Sign up
- First action
- Core value action
- Return in 7 days

Find drop:
- Users do first action but don't return

Hypothesis:
- Users don't see long-term value
- No habit formed

Fix:
- Guide users to core value action
- Add reminders / nudges

Measure:
- D7 retention
```

---

### 4️⃣ "One million paying users are inactive (Netflix-style)"

**Sample answer:**

```
Define funnel:
- Pay subscription
- Browse content
- Play video
- Finish episode
- Return next week

Find drop:
- Users browse but don't play

Hypothesis:
- Choice overload
- Recommendations not relevant

Fix:
- Personalize homepage
- Auto-play recommendations

Measure:
- Weekly active users
```

---

### 5️⃣ "40% increase in first-month churn (HelloFresh-style)"

**Sample answer:**

```
Define funnel:
- Sign up
- First delivery
- Second delivery
- Month renewal

Find drop:
- After first delivery

Hypothesis:
- Food quality mismatch
- Delivery timing issues
- Price surprise

Fix:
- Improve first-box customization
- Better expectation setting

Measure:
- Month-1 retention
```

---

## 🎯 Ultra-Short Interview Version (Gold)

> "I'd map the funnel, find the biggest drop, identify the friction, propose targeted fixes, and re-measure conversion."

---

## 🔑 Key Distinction to Lock In Your Head

```
Funnel = where users drop
Cohort = who drops over time
```

**Funnel (P3):** "Users drop at checkout step" → fix checkout friction

**Cohort (P4):** "February cohort has lower retention than January" → compare cohorts over time

---

If you want, next we can:

* redo **P4 (Cohort / Retention / Churn)** in this exact style
* or compress **P3 into a 5-second verbal answer** for interviews
* or build a **one-page ASCII cheat sheet for P1–P3 combined**
