# Executive Study Plan: P3 - Funnel Analysis
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** 40 questions → 5 concept buckets → 3-5 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY P3 (FUNNEL) QUESTIONS

**Even when "funnel" isn't mentioned, look for these keywords/phrases:**

### Explicit Funnel Keywords:
- "funnel", "drop-off", "drop off", "conversion", "conversion rate"
- "step", "stage", "process", "journey", "flow"

### Implicit Funnel Indicators:
- **Percentage drops:** "55% don't complete", "25% drop-off", "X% of users don't..."
- **Step-specific issues:** "users drop at checkout", "sign-up is failing", "application incomplete"
- **Optimization questions:** "how to improve conversion?", "optimize booking", "increase sign-up rate"
- **Process questions:** "which step to fix first?", "where do users get stuck?", "what's the bottleneck?"
- **Retention/engagement:** "how to improve retention?", "boost engagement", "users don't return"
- **Completion questions:** "users don't complete X", "low completion rate", "high abandonment"

### P3 vs P1 Distinction:
- **P1 (Metric Drop):** "Orders down 25%" → Focus: WHERE is drop coming from? (segment by platform/geo)
- **P3 (Funnel):** "55% drop at checkout" → Focus: WHY do users drop at this STEP? (identify friction)

### P3 vs P4 Distinction:
- **P3 (Funnel):** "Users drop at checkout step" → Single journey, where do they drop?
- **P4 (Cohort):** "February cohort has lower retention" → Multiple sessions, who drops over time?

### Red Flags (NOT P3):
- "Overall metric is down" → P1 (Metric Drop)
- "Cohort retention declined" → P4 (Cohort/Retention)
- "How to define success?" → P2 (NSM + KPI Ladder)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 3-5 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Classic Funnel Drop-off** (HIGHEST PRIORITY)
2. ✅ **Conversion Optimization** (HIGH PRIORITY)
3. ✅ **Funnel Prioritization** (MEDIUM-HIGH)
4. ⚠️ **Retention/Engagement Funnels** (MEDIUM)
5. ❌ **Multi-step Complex Funnels** (LOW - skip for now)

**For Data Engineer:**
1. ✅ **Classic Funnel Drop-off** (HIGHEST) - Data pipeline, ETL funnel analysis
2. ✅ **Conversion Optimization** (HIGH) - Data quality, processing optimization
3. ⚠️ **Funnel Prioritization** (MEDIUM) - Pipeline stage prioritization
4. ❌ **Retention/Engagement Funnels** (LOW - skip for now)
3. ✅ **Funnel Prioritization** (MEDIUM-HIGH)
4. ⚠️ **Retention/Engagement Funnels** (MEDIUM)
5. ❌ **Multi-step Complex Funnels** (LOW)

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Classic Funnel Drop-off ("X% drop at step Y")
**Questions:** ~15 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** Specific drop-off at a funnel step (sign-up, checkout, application, onboarding)
- **Framework:** Define Funnel Steps → Measure Drop-off → Identify Friction → Hypothesize Fix → Test
- **Key Insight:** Find the biggest drop, then ask WHY users get stuck at that step
- **Common Friction Types:** UX (confusing, slow), Trust (price shock, permissions), Value (unclear benefit), Technical (bugs, latency)
- **Fix Approach:** Reduce friction, test incrementally, measure conversion improvement

**Concrete Examples:**
- "55% drop at application submission - likely form too long or unclear required fields"
- "25% drop-off during sign-up - likely email verification friction or too many steps"
- "42% drop at checkout - likely shipping cost surprise or forced account creation"

**Representative Questions (Do 5 only):**
- Q4: 55% of users do not complete the application from the application page to the submission page. Why do you think this is the case?
- Q13: A newly launched mobile app has a 25% drop-off during sign-up. How would you investigate the issue?
- Q2715: You're a PM at a food delivery app where conversion rates have declined over the past week. How would you investigate the causes? (Conversion: From users browsing to placing orders.)
- Q2731: You're a PM at Facebook. How would you decide whether to remove the profile photo step from the onboarding experience?
- Q2830: You're a PM in the Onboarding team. You have to increase the conversion of the onboarding funnel by 15% in 3 months.

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Funnel Steps → Measure Drop-off → Identify Friction → Hypothesize Fix → Test`

**Memorizable Answer:**

When I see a funnel drop-off, I follow a systematic approach.

**1️⃣ Define Funnel Steps** → Exact user journey from entry to conversion.

**2️⃣ Measure Drop-off** → Between each step to find the biggest bottleneck.

**3️⃣ Identify Friction** → Ask WHY: UX friction (confusing, slow, too many fields)? Trust friction (price shock, permissions, privacy)? Value friction (unclear benefit)? Technical friction (bugs, latency)?

**4️⃣ Diagnose** → Use session replays, segment analysis, qualitative feedback.

**5️⃣ Hypothesize Fix** → 1-2 targeted fixes addressing root cause, prioritize by impact and effort.

**6️⃣ Test** → A/B tests or staged rollouts, measure conversion improvement, use guardrails to ensure downstream metrics don't degrade.

**Key Principle:** Find the biggest drop, then ask WHY users get stuck at that step.

---

**How to Adapt This Narrative for Each Question:**

- **Q4 (55% drop at application submission):** Focus on form friction
  - "Define funnel: open application → start application → fill form → submit"
  - "Biggest drop: fill form → submit"
  - "Hypothesize: form too long, required fields unclear, users unsure why info needed"
  - "Check session replays to see where users abandon"
  - "Fixes: reduce required fields, add progress bar, save progress, explain why each field needed"
  - "A/B test and measure submission rate improvement"

- **Q13 (25% drop-off during sign-up):** Emphasize sign-up flow
  - "Define funnel: app open → click sign-up → enter email/password → verify email → complete sign-up"
  - "Measure drop-off at each step"
  - "Likely friction: email verification (slow email, goes to spam, user distracted)"
  - "Check: verification email delivery time, spam rate, completion rate by device"
  - "Fixes: allow limited access before verification, resend CTA, inline verification"
  - "Test and measure sign-up completion rate"

- **Q2715 (Conversion declined over week):** Focus on investigation
  - "First check if data bug, then define funnel: browse → product view → add to cart → checkout → purchase"
  - "Measure drop-off at each step, compare to baseline"
  - "Segment by platform, geography, user type to find hot spot"
  - "Likely causes: product change, pricing change, technical issue"
  - "Check: error rates, latency, support tickets"
  - "Validate with quick checks, propose fixes based on root cause"

- **Q2731 (Remove profile photo step?):** Emphasize decision framework
  - "Measure current funnel: sign-up → enter info → upload photo → complete"
  - "Check drop-off at photo step - if high, removing might help"
  - "Also check: does photo improve downstream metrics (connections, engagement)?"
  - "Run A/B test: one group with photo, one without"
  - "Measure: sign-up completion rate, downstream engagement, user satisfaction"
  - "If removing photo increases sign-up without hurting engagement → remove it"

- **Q2830 (Increase onboarding conversion 15%):** Focus on improvement
  - "Measure current funnel, identify biggest drop-off"
  - "Segment by user type to see if universal or specific"
  - "Hypothesize top 3-5 friction points, prioritize by impact and effort"
  - "Likely fixes: reduce steps, add progress indicator, allow skip optional steps, improve value communication"
  - "Test fixes incrementally, measure conversion improvement, scale what works"
  - "Target: 15% lift in 3 months through systematic optimization"

---

### BUCKET 2: Conversion Optimization ("How to improve conversion?")
**Questions:** ~10 | **Priority:** 🟢 GREEN (High-yield)

**Board Slide Bullets:**
- **What:** "How would you improve conversion?" or "How to optimize booking/checkout/purchase?"
- **Framework:** Same funnel analysis, but focus on optimization opportunities
- **Key Insight:** Find biggest drop-off, identify friction, test fixes, measure improvement
- **Approach:** Map current funnel → Identify bottlenecks → Hypothesize fixes → Test → Scale

**Concrete Examples:**
- "Improve booking conversion: map funnel, find drop at payment step, test guest checkout"
- "Optimize checkout: reduce steps, show shipping cost earlier, allow guest checkout"
- "Increase sign-up: reduce friction, add social login, show value earlier"

**Representative Questions (Do 5 only):**
- Q1521: How would you optimize booking.com to improve conversion rates?
- Q1465: How would you increase the conversion rate for YouTube Premium?
- Q2720: You're a PM at a travel booking platform. Which step of the booking process would you address first to reduce drop-offs?
- Q2726: You're a PM at an e-commerce site. What percentage discount should different customers get during onboarding?
- Q1756: Only 1 in 5 riders tips their driver after a ride. How would you improve this?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Map Funnel → Identify Bottleneck → Segment → Hypothesize Friction → Prioritize → Test`

**Memorizable Answer:**

When optimizing conversion, I map the current funnel to understand where users drop.

**1️⃣ Map Funnel** → Current user journey from entry to conversion.

**2️⃣ Measure Drop-off** → At each step, identify the biggest bottleneck.

**3️⃣ Segment** → By user type, device, geography to see if friction is universal or specific.

**4️⃣ Hypothesize Friction** → Top 3-5 friction points: UX (too many steps, confusing), trust (price surprise, permissions), value (unclear benefit), or technical (slow, bugs).

**5️⃣ Prioritize Fixes** → By impact and effort, then test incrementally.

**6️⃣ Measure & Guardrails** → Conversion improvement, ensure downstream metrics don't degrade.

**Key Principle:** Systematic optimization - fix one step at a time, measure impact, then move to next.

---

**How to Adapt This Narrative for Each Question:**

- **Q1521 (Optimize booking.com conversion):** Focus on booking flow
  - "Map funnel: search → results → select hotel → enter details → payment → confirmation"
  - "Measure drop-off at each step"
  - "Likely bottlenecks: price comparison (users leave to compare), payment friction (too many fields), trust (reviews, cancellation policy)"
  - "Segment by device (mobile vs desktop) and geography"
  - "Fixes: show price comparison, simplify payment, highlight trust signals"
  - "Test and measure booking conversion improvement"

- **Q1465 (Increase YouTube Premium conversion):** Emphasize subscription
  - "Map funnel: watch video → see Premium prompt → click learn more → see pricing → start trial → convert"
  - "Measure drop-off at each step"
  - "Likely friction: pricing (too expensive), value (unclear benefit), trial (too short)"
  - "Segment by user type (heavy vs light watchers)"
  - "Fixes: show value earlier, offer longer trial, highlight ad-free benefit"
  - "Test and measure conversion rate improvement"

- **Q2720 (Which booking step to address first?):** Focus on prioritization
  - "Map funnel, measure drop-off at each step"
  - "Calculate: drop-off % × users at that step = total users lost"
  - "Step with highest total users lost is the priority"
  - "Also consider: ease of fix (quick wins first), impact on downstream (don't break later steps), user segment (fix for biggest segment first)"
  - "Typically, payment step has highest drop-off → start there"

- **Q2726 (What discount for onboarding?):** Emphasize personalization
  - "Measure current funnel and conversion by user segment"
  - "Segment by: user value (high vs low intent), acquisition cost (high vs low CAC), behavior (new vs returning)"
  - "Test different discount levels by segment"
  - "High-intent users might need smaller discount, low-intent might need larger"
  - "Measure: conversion rate, LTV, overall ROI"
  - "Goal: maximize conversion while maintaining unit economics"

- **Q1756 (Improve tipping rate):** Focus on behavioral change
  - "Map funnel: ride completes → rating screen → tip prompt → tip entered → tip submitted"
  - "Measure drop-off at each step"
  - "Likely friction: tip prompt timing (too late), default amount (unclear), value (unclear why tip)"
  - "Segment by ride type and user segment"
  - "Fixes: show tip prompt earlier, suggest default amounts, explain driver benefit"
  - "Test and measure tipping rate improvement"

---

### BUCKET 3: Retention/Engagement Funnels
**Questions:** ~8 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "How to improve retention/engagement?" - funnel over time, not just one session
- **Framework:** Define retention funnel → Measure drop-off over time → Identify friction → Fix
- **Key Insight:** Retention funnels measure behavior over time (D1, D7, D30), not just conversion
- **Approach:** Map user journey over time → Find where users drop → Identify why → Fix

**Concrete Examples:**
- "Retention funnel: Sign up → First value → Return D7 → Return D30 - find where users drop"
- "Engagement funnel: Open app → First action → Core value action → Return next week"
- "Adoption high but retention low: users try but don't see long-term value"

**Representative Questions (Do 5 only):**
- Q1846: Suppose adoption is high, but retention is low—how would you diagnose and communicate the issue?
- Q2157: The product team reports a decline in 30-day user retention. How would you approach this problem?
- Q1256: How would you boost retention for DashPass?
- Q1410: How would you improve retention on LinkedIn?
- Q2738: You're a PM at Instacart. What would you do to improve retention?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Map Journey Over Time → Measure Drop-off → Segment by Cohort → Identify Friction → Fix`

**Memorizable Answer:**

For retention/engagement funnels, I map the user journey over time.

**1️⃣ Map Journey Over Time** → Sign up → first value → return D7 → return D30.

**2️⃣ Measure Drop-off** → At each time point to find where users churn.

**3️⃣ Segment by Cohort** → See if it's a recent issue or ongoing.

**4️⃣ Identify Friction** → Users don't see long-term value? No habit formed? Value not delivered?

**5️⃣ Hypothesize Fixes** → Guide users to core value action, add reminders/nudges, improve onboarding, enhance product value.

**6️⃣ Test & Measure** → Retention improvement (D7, D30).

**Key Principle:** Understand why users don't return, not just that they don't return.

---

**How to Adapt This Narrative for Each Question:**

- **Q1846 (Adoption high, retention low):** Focus on diagnosis
  - "Map funnel: sign up → first action → core value action → return D7"
  - "Drop likely after first action - users try but don't return"
  - "Segment by user type and first action to see patterns"
  - "Likely causes: users don't see long-term value, no habit formed, value not delivered"
  - "Check: what do retained users do differently?"
  - "Communicate: adoption is good (users try), but retention is low (users don't return) - need to improve value delivery or habit formation"

- **Q2157 (30-day retention decline):** Emphasize investigation
  - "First check if data bug, then map retention funnel: sign up → first value → return D7 → return D30"
  - "Measure drop-off at each point, compare to baseline"
  - "Segment by cohort to see if recent or ongoing"
  - "Check: product changes, external factors, user behavior changes"
  - "Identify where users drop and why, propose fixes based on root cause"

- **Q1256 (Boost DashPass retention):** Focus on subscription
  - "Map funnel: sign up → first order → second order → month renewal"
  - "Measure drop-off at each step"
  - "Likely friction: users don't see value (delivery fee savings), don't order enough, forget to use"
  - "Segment by order frequency and user type"
  - "Fixes: show savings prominently, remind users of benefit, offer incentives for repeat orders"
  - "Test and measure retention improvement"

---

### BUCKET 4: Funnel Prioritization ("Which step to fix first?")
**Questions:** ~4 | **Priority:** 🟡 YELLOW

**Board Slide Bullets:**
- **What:** "Which step would you address first?" or "How do you prioritize funnel fixes?"
- **Framework:** Calculate impact = drop-off % × users at that step, then consider ease and downstream impact
- **Key Insight:** Fix the step with highest total users lost, not just highest drop-off %
- **Prioritization:** Impact (users saved) × Ease (effort to fix) × Risk (downstream impact)

**Concrete Examples:**
- "Step with 50% drop-off but 100 users = 50 users lost"
- "Step with 20% drop-off but 1000 users = 200 users lost (fix this first!)"
- "Prioritize by: total users lost, ease of fix, downstream impact"

**Representative Questions (Do 5 only):**
- Q1696: In a multi-step funnel with drop-offs at each stage, which stage would you prioritize addressing first?
- Q985: Given this user funnel, how would you prioritize addressing drop-off points? Come up with design solutions to increase conversion.
- Q2720: You're a PM at a travel booking platform. Which step of the booking process would you address first to reduce drop-offs?
- Q2706: You work at SFO airport, and the CEO asks you to improve the experience from car drop-off to boarding the plane. What's one recommendation you would make?
- Q2887: You're a PM at CarGurus. You launched in Canada 8 months ago and conversions are lower in Canada than the US. What would you do?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Calculate Impact → Consider Ease & Risk → Prioritize → Fix`

**Memorizable Answer:**

When prioritizing funnel fixes, I calculate impact for each step.

**1️⃣ Calculate Impact** → Drop-off % × users at that step = total users lost.

**2️⃣ Identify Priority** → Step with highest total users lost is usually the priority.

**3️⃣ Consider Factors** → Ease of fix (quick wins first), downstream impact (don't break later steps), user segment (fix for biggest segment first).

**4️⃣ Prioritize** → Impact (users saved) × Ease (effort to fix) × Risk (downstream impact).

**5️⃣ Execute** → Start with high-impact, low-effort fixes, then move to high-impact, high-effort fixes.

**Key Principle:** Fix the step that saves the most users, not just the step with highest drop-off %.

---

**How to Adapt This Narrative for Each Question:**

- **Q1696 (Which stage to prioritize?):** Focus on calculation
  - "Calculate impact for each: drop-off % × users at that step = total users lost"
  - "Example: Step 2 has 50% drop-off but only 100 users reach it = 50 users lost"
  - "Step 4 has 20% drop-off but 1000 users reach it = 200 users lost → fix Step 4 first!"
  - "Also consider: ease of fix and downstream impact"
  - "Step with highest total users lost is the priority"

- **Q985 (Prioritize drop-off points):** Emphasize design solutions
  - "Calculate impact (drop-off % × users at step) for each step"
  - "Identify friction at high-impact steps: UX (too many fields, confusing), trust (price surprise), value (unclear benefit), technical (slow, bugs)"
  - "Propose design solutions: reduce steps, add progress indicator, show value earlier, simplify forms"
  - "Prioritize by impact and ease, then test and measure conversion improvement"

- **Q2706 (SFO airport experience):** Focus on physical funnel
  - "Map funnel: car drop-off → check-in → security → gate → boarding"
  - "Measure time and friction at each step"
  - "Likely bottleneck: security (longest wait, most friction)"
  - "Prioritize: reduce security wait time (biggest impact on experience)"
  - "Solutions: more lanes, better queuing, pre-check promotion"
  - "Measure: total time from drop-off to boarding, user satisfaction"

---

### BUCKET 5: Multi-step Complex Funnels
**Questions:** ~3 | **Priority:** 🔴 RED (Low impact - skip for now)

**Examples:** Complex multi-step processes, enterprise workflows, long sales cycles

**Decision:** These are advanced - only study if you have extra time or they come up in your specific role.

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Classic Funnel Drop-off** → Study Bucket 1, practice 5 questions
2. **Conversion Optimization** → Study Bucket 2, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
3. **Retention/Engagement Funnels** → Study Bucket 3, practice 5 questions
4. **Funnel Prioritization** → Study Bucket 4, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through funnel analysis framework in 2 minutes (Define → Measure → Identify → Hypothesize → Test)
- [ ] Explain how to find the biggest drop-off (calculate drop-off % at each step)
- [ ] List 4 types of friction (UX, Trust, Value, Technical)
- [ ] Describe how to prioritize funnel fixes (impact × ease × risk)
- [ ] Explain the difference between funnel (where users drop) and cohort (who drops over time)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the P3 framework to a non-technical person in 2 minutes
- You have 4 reusable narratives (one per bucket) that you can adapt
- You've practiced 15-20 representative questions total (5 per bucket, not all 40!)
- You focus on **systematic analysis, friction identification, and incremental testing**, not memorizing answers

**Remember:** P3 is about systematic funnel analysis. The framework works for any funnel, regardless of product or industry.

