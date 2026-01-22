# Executive Study Plan: P7 - Tradeoff Framing
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** 97 questions → 5 concept buckets → 3-5 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY P7 (TRADEOFF FRAMING) QUESTIONS

**Even when "tradeoff" isn't mentioned, look for these keywords/phrases:**

### Explicit Tradeoff Keywords:
- "tradeoff", "trade-off", "balance", "decide between", "should we do X or Y?"
- "is it worth", "what are we giving up", "why not the other option"

### Implicit P7 Indicators:
- **Decision questions:** "should we do X?", "is X a good idea?", "would you recommend X?"
- **Balance questions:** "how do you balance X and Y?", "balance short-term vs long-term"
- **Build vs buy:** "build vs buy", "in-house vs partnership", "build vs partner"
- **User vs business:** "user experience vs revenue", "user wellbeing vs engagement"
- **Strategic decisions:** "should we enter market X?", "should we invest in Y?", "should we launch Z?"

### P7 vs P6 Distinction:
- **P7 (Tradeoff Framing):** "Should we do X or Y?" → Focus: FRAME tradeoffs (Winners/Losers/Guardrails)
- **P6 (Prioritization):** "Which features to build first?" → Focus: RANK options using RICE

### P7 vs P5 Distinction:
- **P7 (Tradeoff Framing):** "Should we enter market X?" → Focus: FRAME tradeoffs between options
- **P5 (Segmentation):** "Which users should we focus on?" → Focus: DEFINE segments

### P7 vs P1 Distinction:
- **P7 (Tradeoff Framing):** "Should we do X?" → Focus: FRAME decision tradeoffs
- **P1 (Metric Drop):** "Orders down 25%" → Focus: DIAGNOSE why metric dropped

### Red Flags (NOT P7):
- "Which features to build first?" → P6 (Prioritization)
- "Which users should we focus on?" → P5 (Segmentation)
- "Orders down 25%" → P1 (Metric Drop)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 3-5 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Classic Feature/Product Tradeoffs** (HIGHEST PRIORITY)
2. ✅ **Build vs Buy vs Partner Tradeoffs** (HIGH PRIORITY)
3. ✅ **User Experience vs Business Value Tradeoffs** (MEDIUM-HIGH)
4. ⚠️ **Strategic/Investment Tradeoffs** (MEDIUM)
5. ❌ **Time Horizon Tradeoffs** (LOW - skip for now)

**For Data Engineer:**
1. ✅ **Build vs Buy vs Partner Tradeoffs** (HIGHEST) - Infrastructure, tooling, data platform decisions
2. ✅ **Classic Feature/Product Tradeoffs** (HIGH) - System architecture, data pipeline tradeoffs
3. ⚠️ **Time Horizon Tradeoffs** (MEDIUM) - Short-term fixes vs long-term architecture
4. ❌ **User Experience vs Business Value Tradeoffs** (LOW - skip for now)

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Classic Feature/Product Tradeoffs
**Questions:** ~30 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Should we do X or Y?" or "Is X a good idea?" - core tradeoff framework
- **Framework:** Define Options → Winners/Losers → Guardrails → Decide + Communicate
- **Define Options:** List 2-3 clear options (Option A, Option B, Option C if needed)
- **Winners/Losers:** For each option, identify winners (Users, Business, Engineering/Ops, Long-term Strategy) and losers
- **Guardrails:** Non-negotiables (must not break X, must stay within Y, must protect Z)
- **Decide + Communicate:** Pick option, explain why, acknowledge what we're giving up, how we'll monitor risk

**Concrete Examples:**
- "Should Google Flights introduce ads? Option A: No Ads (Users win, Business loses revenue). Option B: Ads (Business wins revenue, Users lose UX). Guardrails: Must not bias rankings, must label ads. Decision: Introduce limited ads with guardrails."
- "Should we launch feature X? Option A: Launch (Users get value, Business gets engagement). Option B: Don't launch (Avoid risk, save resources). Guardrails: Must not break core experience. Decision: Launch with monitoring."

**Representative Questions (Do 5 only):**
- Q698: Determine if Google should introduce ads to Google Flights.
- Q701: Determine if we should launch a feature of Instagram Store that allows purchases without logging in.
- Q1314: How would you determine if Facebook Messenger should introduce group calling?
- Q1376: How would you help the Instagram team decide whether to launch the Rooms feature after a successful launch on Facebook?
- Q1797: Robinhood is planning to introduce a new feature which allows users to trade fractional shares. How would you decide whether this is a good idea or not?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Options → Winners/Losers → Guardrails → Decide + Communicate`

**Memorizable Answer:**

When facing a feature or product decision, I frame it as a tradeoff.

**1️⃣ Define Clear Options** → Option A, Option B, sometimes Option C.

**2️⃣ Identify Winners/Losers** → For each option across stakeholders:
  - **Users:** Better/worse experience
  - **Business:** Revenue, growth, costs
  - **Engineering/Ops:** Effort, complexity
  - **Long-term Strategy:** Strategic value, risks

**3️⃣ Establish Guardrails** → Non-negotiables that must be protected (must not break core experience, must stay within constraints, must protect user trust).

**4️⃣ Decide** → Pick an option, explain why, acknowledge what we're giving up, outline how we'll monitor risks.

**Key Principle:** Frame tradeoffs clearly - identify winners/losers, set guardrails, make decision with rationale.

---

**How to Adapt This Narrative for Each Question:**

- **Q698 (Google Flights introduce ads):** Focus on ad introduction
  - "Frame as tradeoff between user experience and revenue"
  - "Option A: No Ads → Users win (clean UX, high trust), Business loses (missed revenue), Long-term Strategy wins (brand trust)"
  - "Option B: Ads → Business wins (new revenue stream), Users lose (worse experience, bias risk), Long-term Strategy risks (trust erosion)"
  - "Guardrails: Must not bias flight rankings, must clearly label ads, must cap ad density, must monitor user trust metrics"
  - "Decision: Introduce limited ads with guardrails"
  - "Rationale: Revenue value > UX cost if constrained properly"
  - "Tradeoff: Slight UX degradation. Monitoring: CTR, conversion, trust surveys"

- **Q701 (Instagram Store purchases without login):** Emphasize feature decision
  - "Frame as tradeoff between user convenience and security/data"
  - "Option A: Require login → Users lose (friction), Business wins (user data, security), Engineering wins (simpler auth)"
  - "Option B: No login → Users win (convenience, faster checkout), Business loses (less user data, fraud risk), Engineering loses (complexity)"
  - "Guardrails: Must protect payment security, must prevent fraud, must comply with regulations"
  - "Decision: Allow guest checkout with limited features"
  - "Rationale: Convenience drives conversion, but we protect security"
  - "Tradeoff: Less user data collection. Monitoring: Conversion rate, fraud rate, user data capture"

- **Q1314 (Facebook Messenger group calling):** Focus on feature addition
  - "Frame as tradeoff between feature value and complexity"
  - "Option A: Add group calling → Users win (new capability), Business wins (engagement, differentiation), Engineering loses (complexity, infrastructure)"
  - "Option B: Don't add → Engineering wins (simpler), Users lose (missing feature), Business loses (competitive disadvantage)"
  - "Guardrails: Must maintain call quality, must scale infrastructure, must protect privacy"
  - "Decision: Add group calling with phased rollout"
  - "Rationale: High user value, strategic importance"
  - "Tradeoff: Engineering complexity. Monitoring: Usage, quality metrics, infrastructure costs"

---

### BUCKET 2: Build vs Buy vs Partner Tradeoffs
**Questions:** ~10 | **Priority:** 🟢 GREEN (High-yield)

**Board Slide Bullets:**
- **What:** "Build vs buy vs partner" or "In-house vs partnership" - strategic decision tradeoffs
- **Framework:** Same tradeoff framework, applied to build/buy/partner decisions
- **Build:** Control, customization, but high cost, time, maintenance
- **Buy:** Speed, proven solution, but cost, less control, vendor dependency
- **Partner:** Speed, leverage, but dependency, revenue share, less control
- **Decision Factors:** Strategic importance, time to market, cost, control needs, core vs non-core

**Concrete Examples:**
- "Build vs buy payment solution: Build = control, customization, but high cost/time. Buy = speed, proven, but cost/dependency. Partner = speed, leverage, but dependency/revenue share. Decision: Partner if non-core, Build if strategic."
- "Build vs buy AI model: Build = control, customization, but high cost/time. Buy = speed, proven, but cost/dependency. Decision: Buy if non-core, Build if strategic differentiator."

**Representative Questions (Do 5 only):**
- Q151: Can you provide an example of a strategy you developed to address a technology gap at your company, and explain how you decided between build, buy, or partnership?
- Q1072: How do you decide between building a solution in-house or buying an existing one?
- Q1290: How would you decide between using an open-source model in-house versus a commercial API like OpenAI or Claude?
- Q1603: If Meta Pay did not exist, would you recommend that Meta develop its own payment solution internally or seek a partnership? Justify your decision.
- Q2289: What factors do you evaluate before deciding whether to build, fine-tune, or buy a generative AI model?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Options (Build/Buy/Partner) → Winners/Losers → Guardrails → Decide`

**Memorizable Answer:**

When deciding build vs buy vs partner, I frame it as a tradeoff between control, speed, and cost.

**1️⃣ Option A: Build** → Winners: Control (customization, strategic control), Long-term Strategy (core competency). Losers: Time (slow), Cost (high), Engineering (effort).

**2️⃣ Option B: Buy** → Winners: Speed (fast), Engineering (less effort), Business (proven solution). Losers: Cost (licensing), Control (less customization), Long-term Strategy (vendor dependency).

**3️⃣ Option C: Partner** → Winners: Speed (fast), Business (leverage partner), Engineering (less effort). Losers: Control (dependency), Business (revenue share), Long-term Strategy (partner risk).

**4️⃣ Guardrails** → Must protect strategic capabilities, must maintain quality, must manage dependencies.

**5️⃣ Decision** → Build if strategic/core, Buy if non-core and proven, Partner if speed critical and non-core.

**Key Principle:** Build = control + time/cost, Buy = speed + dependency, Partner = speed + dependency + revenue share.

---

**How to Adapt This Narrative for Each Question:**

- **Q1072 (Build vs buy solution):** Focus on general decision
  - "Frame as tradeoff between control, speed, and cost"
  - "Build: Control and customization win, but time and cost lose"
  - "Buy: Speed and proven solution win, but cost and dependency lose"
  - "Guardrails: Must protect strategic capabilities, must maintain quality"
  - "Decision: Build if strategic/core competency, Buy if non-core and proven solution exists"
  - "Evaluate: strategic importance, time to market, cost, control needs"

- **Q1603 (Meta Pay build vs partner):** Emphasize payment context
  - "Frame build vs partner"
  - "Build: Control and strategic value win (payment is core to Meta), but time and cost lose"
  - "Partner: Speed and leverage win, but control and strategic dependency lose"
  - "Guardrails: Must protect user data, must maintain security, must control user experience"
  - "Decision: Build internally"
  - "Rationale: Payment is strategic, control is critical, long-term value"
  - "Tradeoff: Higher initial cost and time. Monitoring: Build timeline, cost, security"

---

### BUCKET 3: User Experience vs Business Value Tradeoffs
**Questions:** ~15 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "User experience vs revenue" or "User wellbeing vs engagement" - balancing user and business interests
- **Framework:** Same tradeoff framework, with focus on user vs business tradeoffs
- **User Experience:** Clean UX, privacy, wellbeing, but may reduce engagement/revenue
- **Business Value:** Revenue, engagement, growth, but may hurt UX/trust
- **Guardrails:** Must protect core user trust, must maintain minimum UX standards, must align with brand values
- **Decision:** Balance user and business, but prioritize user trust for long-term success

**Concrete Examples:**
- "Ads vs UX: More ads = more revenue, but worse UX. Fewer ads = better UX, but less revenue. Guardrails: Must not break core experience, must maintain trust. Decision: Optimize ad density to balance revenue and UX."
- "User wellbeing vs engagement: Reduce addictive features = better wellbeing, but lower engagement. Keep addictive features = higher engagement, but worse wellbeing. Guardrails: Must protect user health, must maintain brand values. Decision: Reduce addictive features with guardrails."

**Representative Questions (Do 5 only):**
- Q46: As a PM at Meta, how would you make users feel less guilty about using Instagram while also increasing revenue?
- Q79: As a Product Manager at TikTok, how would you address user concerns regarding the platform's algorithms being excessively addictive?
- Q1296: How would you define the optimal number of ads to show to users on Yelp?
- Q1639: Imagine you are a data scientist for Instagram. How would you balance ads and follower posts and how would you monitor its effectiveness.
- Q2552: Why did Instagram remove the like count on posts?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Options → Winners/Losers → Guardrails → Balance Decision`

**Memorizable Answer:**

When balancing user experience and business value, I frame it as a tradeoff.

**1️⃣ Option A: Prioritize UX** → Users win (better experience, trust), Business loses (revenue, engagement), Long-term Strategy wins (brand trust).

**2️⃣ Option B: Prioritize Business** → Business wins (revenue, engagement), Users lose (worse experience, trust risk), Long-term Strategy risks (trust erosion).

**3️⃣ Guardrails** → Must protect core user trust, must maintain minimum UX standards, must align with brand values.

**4️⃣ Decision** → Balance both, but prioritize user trust for long-term success.

**5️⃣ Rationale** → Short-term revenue gains don't justify long-term trust loss.

**Key Principle:** Optimize to maximize both, not maximize one at expense of other.

---

**How to Adapt This Narrative for Each Question:**

- **Q46 (Instagram reduce guilt + increase revenue):** Focus on dual objective
  - "Frame as balancing user wellbeing and revenue"
  - "Option A: Reduce guilt features (time limits, wellbeing tools) → Users win (less guilt, better wellbeing), Business loses (potentially lower engagement), Long-term Strategy wins (brand trust)"
  - "Option B: Keep current → Business wins (current revenue), Users lose (guilt, addiction), Long-term Strategy risks (trust erosion)"
  - "Guardrails: Must protect user wellbeing, must maintain brand values, must not significantly hurt revenue"
  - "Decision: Add wellbeing features (time limits, usage insights) while optimizing revenue through better targeting and value"
  - "Rationale: Wellbeing features can actually increase trust and long-term engagement"
  - "Tradeoff: Short-term engagement may dip, but long-term value increases"

- **Q1296 (Optimal ad density on Yelp):** Emphasize optimization
  - "Frame as balancing user experience and revenue"
  - "Option A: Fewer ads → Users win (better UX), Business loses (less revenue)"
  - "Option B: More ads → Business wins (more revenue), Users lose (worse UX, trust risk)"
  - "Guardrails: Must not break core experience, must maintain trust, must clearly label ads"
  - "Decision: Optimize ad density through testing"
  - "Rationale: Find sweet spot that maximizes revenue without hurting UX"
  - "Tradeoff: Balance, not maximize one. Monitoring: Revenue per user, UX metrics, trust surveys"

---

### BUCKET 4: Strategic/Investment Tradeoffs
**Questions:** ~20 | **Priority:** 🟡 YELLOW

**Board Slide Bullets:**
- **What:** "Should we enter market X?" or "Should we invest in Y?" - strategic decision tradeoffs
- **Framework:** Same tradeoff framework, applied to strategic decisions
- **Market Entry:** Opportunity, growth, but competition, risk, resource allocation
- **Investment:** Strategic value, future growth, but cost, opportunity cost, risk
- **Decision Factors:** Market size, competition, strategic fit, resources, risk tolerance

**Concrete Examples:**
- "Should we enter market X? Option A: Enter - Business wins (growth, opportunity), but loses (resources, risk). Option B: Don't enter - Business saves resources, but loses opportunity. Decision: Enter if strategic fit and resources allow."
- "Should we invest in Y? Option A: Invest - Long-term Strategy wins (future value), but Business loses (cost, opportunity cost). Option B: Don't invest - Business saves resources, but loses future value. Decision: Invest if strategic and resources allow."

**Representative Questions (Do 5 only):**
- Q41: As a PM at Amazon, how would you decide if the company should enter the smartphone market?
- Q72: As a PM for Uber when it was a ride-hailing app, would you expand into Uber Eats?
- Q102: As the CEO of Google, should the company continue, slow down, maintain, or ramp up investments in the Pixel handset line?
- Q1807: Should Agoda launch a subscription service called 'Agoda Prime'?
- Q1815: Should Google enter into the online furniture-selling market?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Options → Winners/Losers → Guardrails → Strategic Decision`

**Memorizable Answer:**

When making strategic or investment decisions, I frame it as a tradeoff.

**1️⃣ Option A: Proceed** → Business wins (opportunity, growth), Long-term Strategy wins (strategic value), but Business loses (resources, risk), Engineering loses (effort).

**2️⃣ Option B: Don't Proceed** → Business saves resources, Engineering saves effort, but Business loses (opportunity), Long-term Strategy loses (future value).

**3️⃣ Guardrails** → Must align with strategic goals, must have resources, must manage risk.

**4️⃣ Decision** → Proceed if strategic fit, resources available, and risk manageable.

**5️⃣ Rationale** → Strategic value justifies investment if aligned.

**Key Principle:** Strategic value justifies investment if aligned - but resources and risk must be manageable.

---

**How to Adapt This Narrative for Each Question:**

- **Q72 (Uber expand into Uber Eats):** Focus on market expansion
  - "Frame as tradeoff between focus and diversification"
  - "Option A: Expand to Eats → Business wins (new market, growth), Long-term Strategy wins (platform expansion), but Business loses (resources, focus), Engineering loses (complexity)"
  - "Option B: Stay focused on rides → Business maintains focus, Engineering maintains simplicity, but Business loses (market opportunity), Long-term Strategy loses (platform potential)"
  - "Guardrails: Must not hurt core rides business, must have resources, must manage complexity"
  - "Decision: Expand to Eats"
  - "Rationale: Leverages existing driver network, strategic platform play, manageable risk"
  - "Tradeoff: Resource allocation and complexity. Monitoring: Eats growth, rides impact, resource utilization"

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Classic Feature/Product Tradeoffs** → Study Bucket 1, practice 5 questions
2. **Build vs Buy vs Partner Tradeoffs** → Study Bucket 2, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
3. **User Experience vs Business Value Tradeoffs** → Study Bucket 3, practice 5 questions
4. **Strategic/Investment Tradeoffs** → Study Bucket 4, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through tradeoff framework in 2 minutes (Define Options → Winners/Losers → Guardrails → Decide)
- [ ] Identify winners and losers for each option (Users, Business, Engineering, Long-term Strategy)
- [ ] Establish guardrails (non-negotiables)
- [ ] Make a clear decision and communicate tradeoffs
- [ ] Explain what you're giving up and how you'll monitor risks

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the tradeoff framework to a non-technical person in 2 minutes
- You have 4 reusable narratives (one per bucket) that you can adapt
- You've practiced 15-20 representative questions total (5 per bucket)
- You focus on **framing tradeoffs clearly, identifying winners/losers, establishing guardrails, and making decisions**, not memorizing answers

**Remember:** P7 is about framing tradeoffs and making decisions. The framework: Define Options → Winners/Losers → Guardrails → Decide + Communicate.
