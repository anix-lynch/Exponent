# Executive Study Plan: P9 - Decision Under Uncertainty
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** 7 questions → 3 concept buckets → 2-3 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY P9 (DECISION UNDER UNCERTAINTY) QUESTIONS

**Even when "uncertainty" isn't mentioned, look for these keywords/phrases:**

### Explicit Uncertainty Keywords:
- "uncertainty", "incomplete information", "lack of data", "don't know", "assumptions"
- "go/no-go decision", "decide with limited info", "make decision without data"

### Implicit P9 Indicators:
- **Information gaps:** "project lacked key information", "limited data", "incomplete info"
- **Decision questions with unknowns:** "should we do X?" (but we don't know Y), "decide with incomplete info"
- **Assumption questions:** "what assumptions are you making?", "what must be true?"
- **Risk questions:** "what are the risks?", "what could go wrong?"
- **Validation questions:** "how would you validate?", "what would you check first?"

### P9 vs P8 Distinction:
- **P9 (Decision Under Uncertainty):** "Should we do X with incomplete info?" → Focus: CLARIFY assumptions and validate (Assumptions → Risks → Validation → Decide)
- **P8 (Experiment Design):** "How would you test X?" → Focus: DESIGN experiment (Hypothesis → Metric → Design → Run → Validate)

### P9 vs P7 Distinction:
- **P9 (Decision Under Uncertainty):** "Should we do X with incomplete info?" → Focus: CLARIFY assumptions and validate before deciding
- **P7 (Tradeoff Framing):** "Should we do X or Y?" → Focus: FRAME tradeoffs (Winners/Losers/Guardrails)

### P9 vs P6 Distinction:
- **P9 (Decision Under Uncertainty):** "Should we do X with incomplete info?" → Focus: CLARIFY assumptions and validate
- **P6 (Prioritization):** "Which features to build first?" → Focus: RANK options using RICE

### Red Flags (NOT P9):
- "How would you test X?" → P8 (Experiment Design)
- "Should we do X or Y?" → P7 (Tradeoff Framing)
- "Which features to build first?" → P6 (Prioritization)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2-3 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Go/No-Go Decisions** (HIGHEST PRIORITY)
2. ✅ **Market Entry Under Uncertainty** (HIGH PRIORITY)
3. ⚠️ **Feature/Product Decisions with Incomplete Info** (MEDIUM)

**For Data Engineer:**
1. ✅ **Go/No-Go Decisions** (HIGHEST) - Technical feasibility, infrastructure decisions
2. ⚠️ **Feature/Product Decisions with Incomplete Info** (MEDIUM) - Data pipeline, architecture decisions
3. ❌ **Market Entry Under Uncertainty** (LOW - skip for now)

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Go/No-Go Decisions
**Questions:** ~3 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Go/no-go decision" or "Should we proceed with incomplete info?" - core uncertainty framework
- **Framework:** Clarify Assumptions → Identify Risks → Validation Plan → Decide
- **Clarify Assumptions:** What do we believe is true? (User behavior, Market/demand, Technical feasibility, Timing/dependencies) → Classify as Critical (decision breaks if wrong) vs Non-critical
- **Identify Risks:** If assumption is wrong, what happens? (Revenue risk, User trust/UX risk, Technical/scalability risk, Legal/compliance risk, Opportunity cost) → Rank by impact × likelihood
- **Validation Plan:** What's the cheapest signal to reduce uncertainty? (Qualitative: interviews, expert review | Quantitative: logs, metrics, small experiments | Proxies: analogous products, historical data | Time-boxed spike/prototype) → Decide upfront: What result would change decision? What result is "good enough"?
- **Decide:** Proceed now (if upside >> downside and risks bounded), Delay and validate (if one critical unknown dominates), Kill/pivot (if downside irreversible or catastrophic)

**Concrete Examples:**
- "Go/no-go for feature: Assumptions (users want it, technically feasible), Risks (if wrong: wasted effort, user disappointment), Validation (user interviews, small prototype), Decide (proceed if validation positive, delay if critical unknown)"
- "Go/no-go for market entry: Assumptions (market demand, competition manageable), Risks (if wrong: wasted investment, opportunity cost), Validation (market research, pilot), Decide (proceed if validation positive)"

**Representative Questions (Do 5 only):**
- Q150: Can you outline a framework for a go/no-go decision? For example, you are a PM who just onboarded and need to decide whether to ship a feature that the previous PM worked on. (feature decision angle)
- Q16: A potential client asks for a guarantee on a feature's delivery date. Your team hasn't considered this feature before. What would you do? (commitment under uncertainty angle)
- Q215: Describe a time when a project lacked key information. (information gaps angle)
- Q150: Can you outline a framework for a go/no-go decision? For example, you are a PM who just onboarded and need to decide whether to ship a feature that the previous PM worked on. (go/no-go framework angle)
- Q16: A potential client asks for a guarantee on a feature's delivery date. Your team hasn't considered this feature before. What would you do? (risk management angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Clarify Assumptions → Identify Risks → Validation Plan → Decide`

**Memorizable Answer:**

When making a go/no-go decision with incomplete information, I use the Clarify Assumptions → Identify Risks → Validation Plan → Decide framework.

**1️⃣ Clarify Assumptions** → What do we believe is true? (User behavior, market demand, technical feasibility, timing/dependencies). Classify as Critical (decision breaks if wrong) vs Non-critical.

**2️⃣ Identify Risks** → If assumption is wrong, what happens? (Revenue risk, user trust risk, technical risk, legal risk, opportunity cost). Rank by impact × likelihood.

**3️⃣ Create Validation Plan** → What's the cheapest signal to reduce uncertainty?
  - **Qualitative:** Interviews, expert review
  - **Quantitative:** Logs, metrics, small experiments
  - **Proxies:** Analogous products, historical data
  - **Time-boxed spike/prototype**

**4️⃣ Decide Upfront** → What result would change the decision? What result is "good enough"?

**5️⃣ Decide** → Proceed now (if upside >> downside and risks bounded), Delay and validate (if one critical unknown dominates), Kill/pivot (if downside irreversible or catastrophic).

**Key Principle:** Clarify what you don't know, validate cheaply, decide with bounded risk.

---

**How to Adapt This Narrative for Each Question:**

- **Q150 (Go/no-go framework for feature):** Focus on feature decision
  - "Clarify assumptions: Users want it (critical), technically feasible (critical), fits strategy (non-critical)"
  - "Identify risks: If users don't want it → wasted effort (high impact), If not feasible → project failure (high impact)"
  - "Create validation plan: User interviews (qualitative), small prototype (quantitative), analogous features (proxy)"
  - "Decide upfront: If 70%+ users want it and prototype works → proceed. If <50% want it or prototype fails → kill. If mixed → delay and iterate"
  - "Decide: Proceed if validation positive, Delay if critical unknown, Kill if validation negative"

- **Q16 (Guarantee delivery date for unknown feature):** Emphasize commitment under uncertainty
  - "Clarify assumptions: Scope is clear (critical), team can deliver (critical), dependencies known (critical)"
  - "Identify risks: If scope unclear → missed deadline (high impact), If team can't deliver → broken promise (high impact), If dependencies unknown → delays (high impact)"
  - "Create validation plan: Scope clarification (qualitative), team assessment (qualitative), dependency mapping (qualitative), time-boxed spike (quantitative)"
  - "Decide upfront: If scope clear, team confident, dependencies known → can commit. If any critical unknown → cannot commit yet"
  - "Respond: 'I can't commit to a date yet because we need to validate assumptions. Let me do a quick spike (1-2 days) to clarify scope, assess feasibility, and map dependencies. Then I can give you a realistic timeline.'"

---

### BUCKET 2: Market Entry Under Uncertainty
**Questions:** ~2 | **Priority:** 🟢 GREEN (High-yield)

**Board Slide Bullets:**
- **What:** "Should we enter market X?" or "Market entry decision with incomplete info" - same framework, applied to market entry
- **Approach:** Same uncertainty framework, with focus on market-specific assumptions and risks
- **Market Assumptions:** Market demand, competition, regulatory environment, market fit
- **Market Risks:** Wasted investment, opportunity cost, competitive response, regulatory issues
- **Validation:** Market research, competitive analysis, pilot/test market, analogous markets

**Concrete Examples:**
- "Market entry decision: Assumptions (demand exists, competition manageable), Risks (wasted investment, opportunity cost), Validation (market research, pilot), Decide (enter if validation positive)"
- "New city launch: Assumptions (demand, supply available), Risks (wasted investment), Validation (market data, pilot), Decide (launch if validation positive)"

**Representative Questions (Do 5 only):**
- Q12: A leading Canadian grocery chain is considering opening its first store in Montreal. Should they? If yes, what should be the ratio of self-checkout kiosks to cashier counters? (market entry angle)
- Q2656: You are a PM at Amazon deciding on entering the smartphone market. How would you proceed to make a decision before the senior management meeting? (strategic decision angle)
- Q91: As a VC offering you $20M to build any technology-enabled product/service, how would you get started? (startup ideation angle)
- Q12: A leading Canadian grocery chain is considering opening its first store in Montreal. Should they? If yes, what should be the ratio of self-checkout kiosks to cashier counters? (location and operations angle)
- Q2656: You are a PM at Amazon deciding on entering the smartphone market. How would you proceed to make a decision before the senior management meeting? (pre-meeting preparation angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Clarify Market Assumptions → Identify Market Risks → Validation Plan → Decide`

**Memorizable Answer:**

When deciding on market entry with incomplete information, I use the same uncertainty framework.

**1️⃣ Clarify Market Assumptions** → Demand exists (critical), competition is manageable (critical), regulatory environment is favorable (critical), market fit is good (critical).

**2️⃣ Identify Market Risks** → If demand doesn't exist → wasted investment (high impact), If competition too strong → failure (high impact), If regulatory issues → blocked (high impact).

**3️⃣ Create Validation Plan** → Market research (qualitative/quantitative), competitive analysis (qualitative), pilot/test market (quantitative), analogous markets (proxy).

**4️⃣ Decide Upfront** → If market research positive, competition manageable, pilot successful → enter. If any critical assumption fails → don't enter.

**5️⃣ Decide** → Enter if validation positive, Delay if critical unknown, Don't enter if validation negative.

**Key Principle:** Same framework, applied to market entry decisions.

---

**How to Adapt This Narrative for Each Question:**

- **Q12 (Grocery chain open store in Montreal):** Focus on market entry
  - "Clarify assumptions: Demand exists (critical - do people shop at grocery stores?), Competition manageable (critical - how many competitors?), Location suitable (critical - where to open?), Self-checkout preference (non-critical - ratio question)"
  - "Identify risks: If demand low → wasted investment (high impact), If competition too strong → failure (high impact), If location bad → low traffic (high impact)"
  - "Create validation plan: Market research (demand, competition), Location analysis (traffic, demographics), Pilot (test in similar market), Analogous stores (other cities)"
  - "Decide upfront: If market research positive, location good, pilot successful → open"
  - "For self-checkout ratio: Validate through user research and pilot testing"
  - "Decide: Open if validation positive, with self-checkout ratio based on user preference data"

- **Q2656 (Amazon enter smartphone market):** Emphasize strategic decision
  - "Clarify assumptions: Market demand exists (critical), We can compete (critical), Technical feasibility (critical), Strategic fit (critical)"
  - "Identify risks: If demand low → wasted billions (high impact), If can't compete → failure (high impact), If not feasible → project failure (high impact)"
  - "Create validation plan: Market research (demand, competition), Technical assessment (feasibility), Strategic analysis (fit), Pilot (small test)"
  - "Decide upfront: If market research positive, technical feasible, strategic fit → proceed"
  - "Prepare for meeting: Assumptions, risks, validation plan, recommendation (proceed/don't proceed) with rationale"

---

### BUCKET 3: Feature/Product Decisions with Incomplete Info
**Questions:** ~2 | **Priority:** 🟡 YELLOW

**Board Slide Bullets:**
- **What:** "Decide on feature/product with incomplete info" - same framework, applied to feature/product decisions
- **Approach:** Same uncertainty framework, with focus on feature/product-specific assumptions and risks
- **Feature Assumptions:** User need, technical feasibility, business value, timing
- **Feature Risks:** Wasted effort, user disappointment, technical failure, opportunity cost
- **Validation:** User research, technical spike, business case, prototype

**Concrete Examples:**
- "Feature decision: Assumptions (users want it, feasible), Risks (wasted effort), Validation (user research, spike), Decide (build if validation positive)"
- "Product decision: Assumptions (market fit, feasible), Risks (wasted investment), Validation (market research, MVP), Decide (launch if validation positive)"

**Representative Questions (Do 5 only):**
- Q185: Decide product-market fit for sticky post-its. (PMF assessment angle)
- Q91: As a VC offering you $20M to build any technology-enabled product/service, how would you get started? (startup ideation angle)
- Q185: Decide product-market fit for sticky post-its. (product validation angle)
- Q91: As a VC offering you $20M to build any technology-enabled product/service, how would you get started? (market opportunity angle)
- Q150: Can you outline a framework for a go/no-go decision? For example, you are a PM who just onboarded and need to decide whether to ship a feature that the previous PM worked on. (feature decision angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Clarify Feature Assumptions → Identify Feature Risks → Validation Plan → Decide`

**Memorizable Answer:**

When deciding on a feature or product with incomplete information, I use the same uncertainty framework.

**1️⃣ Clarify Assumptions** → User need exists (critical), Technical feasibility (critical), Business value (critical), Timing right (non-critical).

**2️⃣ Identify Risks** → If no user need → wasted effort (high impact), If not feasible → failure (high impact), If no business value → wasted investment (high impact).

**3️⃣ Create Validation Plan** → User research (qualitative), Technical spike (quantitative), Business case (qualitative), Prototype/MVP (quantitative).

**4️⃣ Decide Upfront** → If user need validated, feasible, business value positive → proceed.

**5️⃣ Decide** → Proceed if validation positive, Delay if critical unknown, Kill if validation negative.

**Key Principle:** Same framework, applied to feature/product decisions.

---

**How to Adapt This Narrative for Each Question:**

- **Q185 (Decide PMF for sticky post-its):** Focus on PMF
  - "Clarify assumptions: Users have need (critical - do people need sticky notes?), Product solves need (critical - do post-its solve it?), Market size sufficient (critical - big enough market?), Competition manageable (non-critical)"
  - "Identify risks: If no need → no market (high impact), If doesn't solve → failure (high impact), If market too small → not viable (high impact)"
  - "Create validation plan: User research (interviews, surveys), Market analysis (size, competition), Product testing (prototype), Analogous products (similar products)"
  - "Decide upfront: If need validated, product solves, market sufficient → PMF exists"
  - "Decide: PMF exists if validation positive, PMF doesn't exist if validation negative"

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Go/No-Go Decisions** → Study Bucket 1, practice 5 questions
2. **Market Entry Under Uncertainty** → Study Bucket 2, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
3. **Feature/Product Decisions with Incomplete Info** → Study Bucket 3, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through uncertainty framework in 2 minutes (Clarify Assumptions → Identify Risks → Validation Plan → Decide)
- [ ] Clarify assumptions (what must be true?) and classify as critical vs non-critical
- [ ] Identify risks (what breaks if assumption wrong?) and rank by impact × likelihood
- [ ] Create validation plan (cheapest signal to reduce uncertainty)
- [ ] Make decision (Proceed/Delay/Kill) with rationale

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the uncertainty framework to a non-technical person in 2 minutes
- You have 3 reusable narratives (one per bucket) that you can adapt
- You've practiced 10-15 representative questions total (5 per bucket)
- You focus on **Clarify Assumptions → Identify Risks → Validation Plan → Decide framework**, not memorizing answers

**Remember:** P9 is about making decisions with incomplete information. The framework: Clarify Assumptions → Identify Risks → Validation Plan → Decide.
