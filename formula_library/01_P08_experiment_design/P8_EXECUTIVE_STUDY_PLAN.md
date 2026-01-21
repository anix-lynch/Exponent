# Executive Study Plan: P8 - Experiment Design
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** 32 questions → 4 concept buckets → 3-4 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY P8 (EXPERIMENT DESIGN) QUESTIONS

**Even when "experiment" or "A/B test" isn't mentioned, look for these keywords/phrases:**

### Explicit Experiment Keywords:
- "experiment", "A/B test", "test", "validate", "pilot", "beta"
- "how would you test", "design an experiment", "measure success"

### Implicit P8 Indicators:
- **Testing questions:** "how would you test X?", "how would you validate Y?", "design an experiment for Z"
- **Evaluation questions:** "how would you evaluate X?", "how would you measure success of Y?"
- **Decision questions:** "how do you decide whether to ship X?", "should we launch Y?"
- **Beta/pilot questions:** "how would you pilot X?", "assess success of beta launch"
- **Sample size questions:** "what sample size?", "how many users needed?"

### P8 vs P9 Distinction:
- **P8 (Experiment Design):** "How would you test X?" → Focus: DESIGN experiment (Hypothesis → Metric → Design → Run → Validate)
- **P9 (Decision Under Uncertainty):** "Should we do X with incomplete info?" → Focus: CLARIFY assumptions and validate (Assumptions → Risks → Validation → Decide)

### P8 vs P6 Distinction:
- **P8 (Experiment Design):** "How would you test feature X?" → Focus: DESIGN experiment to test
- **P6 (Prioritization):** "Which features to build first?" → Focus: RANK options using RICE

### Red Flags (NOT P8):
- "Which features to build first?" → P6 (Prioritization)
- "Should we do X with incomplete info?" → P9 (Decision Under Uncertainty)
- "Orders down 25%" → P1 (Metric Drop)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 3-4 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Classic A/B Test Design** (HIGHEST PRIORITY)
2. ✅ **Feature Evaluation Experiments** (HIGH PRIORITY)
3. ✅ **Market/Product Expansion Experiments** (MEDIUM-HIGH)
4. ⚠️ **Experiment Validation & Biases** (MEDIUM)

**For Data Engineer:**
1. ✅ **Classic A/B Test Design** (HIGHEST) - Infrastructure, data pipeline experiments
2. ✅ **Experiment Validation & Biases** (HIGH) - Data quality, logging validation
3. ⚠️ **Feature Evaluation Experiments** (MEDIUM) - System performance experiments
4. ❌ **Market/Product Expansion Experiments** (LOW - skip for now)

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Classic A/B Test Design
**Questions:** ~10 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "How do you A/B test X?" or "Design an experiment for Y" - core experiment framework
- **Framework:** Hypothesis → Metric → Design → Run → Validate → Decide
- **Hypothesis:** "If we change X for users Y, then outcome Z will change because R"
- **Metric:** Primary (decision metric), Guardrails (prevent harm), Diagnostics (explain why)
- **Design:** Unit of randomization (user/session/geo), Population, Variants (Control/Treatment), Duration, Instrumentation
- **Run:** Ramp (1% → 10% → 50% → 100%), Monitor guardrails, Freeze conflicting changes
- **Validate:** SRM check, Balance check, Correct attribution, No logging changes
- **Decide:** Ship/Iterate/Rollback based on results

**Concrete Examples:**
- "A/B test new feature: Hypothesis (if we add X, then engagement increases), Metric (primary: engagement, guardrails: churn), Design (user randomization, 50/50 split, 2 weeks), Run (ramp gradually), Validate (check SRM, balance), Decide (ship if positive)"
- "Test checkout redesign: Hypothesis (simpler checkout increases conversion), Metric (primary: conversion, guardrails: refunds), Design (user randomization), Run (ramp), Validate (check balance), Decide (ship if conversion up)"

**Representative Questions (Do 5 only):**
- Q1041: How do you A/B test a new feature?
- Q1308: How would you design an experiment to validate the success of a new landing page?
- Q1079: How do you design an experiment to avoid common pitfalls in interpreting results?
- Q1082: How do you determine the necessary sample size for an A/B test?
- Q2327: What is the benefit of A/B testing?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When designing an A/B test, I follow the Hypothesis → Metric → Design → Run → Validate → Decide framework. First, I state a clear hypothesis: 'If we change X for users Y, then outcome Z will change because R.' Then I define metrics: Primary metric (the decision metric), Guardrails (prevent harm like churn, errors), and Diagnostics (explain why). Next, I design the experiment: Unit of randomization (user/session/geo), Population (who's eligible), Variants (Control vs Treatment), Duration (full cycles), and Instrumentation (tracking). I run the experiment with gradual ramp (1% → 10% → 50% → 100%) while monitoring guardrails daily and freezing conflicting changes. I validate results by checking SRM (sample ratio mismatch), balance (groups comparable), attribution (exposure vs outcome), and logging (no changes). Finally, I decide: Ship if primary metric improves and guardrails stable, Iterate if mixed results, or Rollback if guardrails worsen."

**How to Adapt This Narrative for Each Question:**

- **Q1041 (A/B test a new feature):** Focus on feature testing → "To A/B test a new feature, I'd start with a hypothesis: 'If we add feature X for users Y, then engagement will increase because it solves problem Z.' I'd define metrics: Primary (engagement rate), Guardrails (churn, errors, latency), Diagnostics (feature usage, drop-offs). I'd design: Randomize by user, target relevant population, Control (no feature) vs Treatment (with feature), run for 2 weeks, track exposure and outcomes. I'd run with gradual ramp, monitor guardrails daily, freeze other changes. I'd validate: Check SRM, balance, attribution. I'd decide: Ship if engagement up and guardrails stable."

- **Q1308 (Design experiment for landing page):** Emphasize landing page context → "To validate a new landing page, I'd hypothesize: 'If we redesign landing page with clearer value prop, then conversion will increase because less friction.' Metrics: Primary (conversion rate), Guardrails (bounce rate, time on page), Diagnostics (scroll depth, CTA clicks). Design: Randomize by session, all visitors, Control (old page) vs Treatment (new page), 2 weeks, track page views and conversions. Run with ramp, monitor guardrails. Validate: Check SRM, balance, attribution. Decide: Ship if conversion up."

- **Q1079 (Avoid common pitfalls):** Focus on pitfalls → "To avoid pitfalls, I'd ensure: 1) Clear hypothesis (not fishing), 2) Proper randomization (avoid selection bias), 3) Sufficient sample size (avoid false positives), 4) Guardrails (prevent harm), 5) Correct attribution (exposure vs outcome), 6) No peeking (avoid multiple testing), 7) Balance check (groups comparable), 8) SRM check (traffic split correct). I'd design with these in mind and validate all checks before deciding."

---

### BUCKET 2: Feature Evaluation Experiments
**Questions:** ~8 | **Priority:** 🟢 GREEN (High-yield)

**Board Slide Bullets:**
- **What:** "How would you evaluate feature X?" or "Is feature worth rolling out?" - same framework, applied to feature evaluation
- **Approach:** Same experiment framework, with focus on feature-specific metrics
- **Feature Metrics:** Usage, engagement, retention, revenue impact
- **Decision:** Roll out if positive, iterate if mixed, kill if negative

**Concrete Examples:**
- "Evaluate new feature: Test with A/B framework, measure usage/engagement, decide roll out if positive"
- "Is feature worth rolling out: Design experiment, measure impact, decide based on results"

**Representative Questions (Do 5 only):**
- Q1344: How would you evaluate whether a new feature is worth rolling out to all users?
- Q969: Given experiment results, how do you decide whether to ship the feature?
- Q849: Facebook is considering adding a 7th reaction. How would you determine its necessity and measure its success?
- Q25: An engineer wants to make a major change to the ranking algorithm. How would you evaluate it?
- Q1811: Should Facebook launch a group video calling feature? How would you make this determination using a dataset of call logs for current 1:1 calling?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "To evaluate a feature, I'd use the experiment framework. I'd state a hypothesis about the feature's impact, define metrics (primary: feature value, guardrails: user harm), design an experiment (A/B test), run it with gradual ramp, validate results, and decide whether to roll out. If the feature shows positive impact and guardrails are stable, I'd roll out. If mixed, I'd iterate. If negative, I'd kill it."

**How to Adapt This Narrative for Each Question:**

- **Q1344 (Evaluate feature worth rolling out):** Focus on evaluation → "To evaluate if a feature is worth rolling out, I'd design an A/B test. Hypothesis: 'If we add feature X, then user value Y will increase.' Metrics: Primary (feature value metric like engagement), Guardrails (churn, errors), Diagnostics (usage, retention). Design: Randomize by user, relevant population, Control vs Treatment, 2 weeks. Run with ramp, monitor guardrails. Validate: Check SRM, balance, attribution. Decide: Roll out if primary metric improves significantly and guardrails stable, Iterate if mixed, Kill if negative or guardrails worsen."

- **Q969 (Decide whether to ship from results):** Emphasize decision from results → "Given experiment results, I'd evaluate: 1) Primary metric: Is it statistically significant and meaningful? 2) Guardrails: Are they stable (no harm)? 3) Diagnostics: Do they explain why? 4) Segment analysis: Which segments moved? If primary metric is positive and significant, guardrails stable, and diagnostics make sense, I'd ship. If mixed, I'd iterate on what worked. If negative or guardrails worsen, I'd rollback."

---

### BUCKET 3: Market/Product Expansion Experiments
**Questions:** ~6 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "How would you test market expansion?" or "Test product expansion" - same framework, applied to expansion
- **Approach:** Same experiment framework, with focus on market/product-specific metrics
- **Expansion Metrics:** Adoption, engagement, revenue, market fit
- **Decision:** Expand if positive, iterate if mixed, don't expand if negative

**Concrete Examples:**
- "Test market expansion: Design experiment in test market, measure adoption/engagement, decide expand if positive"
- "Test product expansion: Pilot in test region, measure success, decide expand if positive"

**Representative Questions (Do 5 only):**
- Q1572: How would you test the impact of expanding into a new international market?
- Q1573: How would you test the viability of expanding Airbnb's "Restaurant" product to a new region?
- Q2189: We're considering launching in a new city. What data would you look at before recommending a go/no-go decision?
- Q64: As a PM for Jio Mart, how would you pilot drone delivery?
- Q1379: How would you identify market/product fit for connecting mentors with mentees and validate an MVP in this space?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "To test market or product expansion, I'd use the experiment framework. I'd state a hypothesis about expansion success, define metrics (primary: expansion success, guardrails: core business impact), design an experiment (pilot in test market/region), run it, validate results, and decide whether to expand. If expansion shows positive impact and doesn't hurt core business, I'd expand. If mixed, I'd iterate. If negative, I'd not expand."

**How to Adapt This Narrative for Each Question:**

- **Q1572 (Test international market expansion):** Focus on market expansion → "To test international expansion, I'd design a pilot experiment. Hypothesis: 'If we launch in market X, then adoption Y will be positive because market fit Z.' Metrics: Primary (adoption, engagement, revenue), Guardrails (core business impact, resource drain), Diagnostics (user segments, usage patterns). Design: Pilot in one test market, Control (don't launch) vs Treatment (launch), 3-6 months, track market metrics. Run: Launch in test market, monitor guardrails. Validate: Check market metrics, compare to baseline, assess market fit. Decide: Expand to more markets if positive, Iterate if mixed, Don't expand if negative."

---

### BUCKET 4: Experiment Validation & Biases
**Questions:** ~5 | **Priority:** 🟡 YELLOW

**Board Slide Bullets:**
- **What:** "Common biases in experiments" or "How to validate experiment results" - ensuring experiment validity
- **Common Biases:** Selection bias, novelty effect, seasonality, multiple testing, peeking, attribution errors
- **Validation Checks:** SRM (sample ratio mismatch), Balance check, Attribution check, Logging check
- **Avoid Pitfalls:** Clear hypothesis, proper randomization, sufficient sample size, guardrails, correct attribution

**Concrete Examples:**
- "Common biases: Selection bias (non-random assignment), Novelty effect (temporary boost), Seasonality (time effects), Multiple testing (false positives), Peeking (early stopping)"
- "Validation checks: SRM (traffic split correct?), Balance (groups comparable?), Attribution (exposure vs outcome?), Logging (events firing correctly?)"

**Representative Questions (Do 5 only):**
- Q2199: What are some common biases that might invalidate an experiment?
- Q2326: What is the benefit of a control group when testing?
- Q2521: When experimentation is constrained, how do you make decisions using imperfect or historical data?
- Q216: Describe a time when an experiment you conducted yielded unexpected results. How did you react to the outcome?
- Q1924: Tell me about a time when you had a hypothesis that turned out to be wrong.

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "To ensure experiment validity, I'd check for common biases and validate results. Common biases: Selection bias (non-random), Novelty effect (temporary), Seasonality (time effects), Multiple testing (false positives), Peeking (early stopping). Validation checks: SRM (traffic split correct?), Balance (groups comparable?), Attribution (exposure vs outcome?), Logging (events correct?). I'd avoid pitfalls: Clear hypothesis, proper randomization, sufficient sample size, guardrails, correct attribution, no peeking."

**How to Adapt This Narrative for Each Question:**

- **Q2199 (Common biases):** Focus on biases → "Common biases that invalidate experiments: 1) Selection bias (non-random assignment), 2) Novelty effect (temporary boost from newness), 3) Seasonality (time-based effects), 4) Multiple testing (testing many hypotheses increases false positives), 5) Peeking (stopping early based on interim results), 6) Attribution errors (wrong exposure vs outcome window), 7) Spillover (treatment affects control group). I'd mitigate these through proper randomization, sufficient duration, guardrails, and validation checks."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Classic A/B Test Design** → Study Bucket 1, practice 5 questions
2. **Feature Evaluation Experiments** → Study Bucket 2, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
3. **Market/Product Expansion Experiments** → Study Bucket 3, practice 5 questions
4. **Experiment Validation & Biases** → Study Bucket 4, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through experiment framework in 2 minutes (Hypothesis → Metric → Design → Run → Validate → Decide)
- [ ] Define clear hypothesis (If X then Y because Z)
- [ ] Identify primary metric, guardrails, and diagnostics
- [ ] Design experiment (randomization, population, variants, duration)
- [ ] Explain validation checks (SRM, balance, attribution)
- [ ] Make decision (Ship/Iterate/Rollback)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the experiment framework to a non-technical person in 2 minutes
- You have 4 reusable narratives (one per bucket) that you can adapt
- You've practiced 15-20 representative questions total (5 per bucket)
- You focus on **Hypothesis → Metric → Design → Run → Validate → Decide framework**, not memorizing answers

**Remember:** P8 is about designing valid experiments. The framework: Hypothesis → Metric → Design → Run → Validate → Decide.
