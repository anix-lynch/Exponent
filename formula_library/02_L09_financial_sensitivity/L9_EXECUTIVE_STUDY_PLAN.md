# Executive Study Plan: L9 - Financial Sensitivity
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~10 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L9 (FINANCIAL SENSITIVITY) QUESTIONS

**Even when "financial sensitivity" isn't mentioned, look for these keywords/phrases:**

### Explicit Financial Sensitivity Keywords:
- "financial sensitivity", "sensitivity analysis", "what moves revenue", "what moves profitability"
- "levers", "price vs volume", "churn impact", "LTV", "revenue drivers"
- "which lever", "what impacts", "sensitivity", "elasticity"

### Implicit L9 Indicators:
- **Lever questions:** "What moves revenue most?", "Which lever has biggest impact?", "What drives profitability?"
- **Sensitivity questions:** "How sensitive is revenue to price?", "What's the impact of churn?", "Price vs volume?"
- **Financial impact questions:** "What moves the business outcome?", "Which factor matters most?"

### L9 vs P14 Distinction:
- **L9 (Financial Sensitivity):** "What moves revenue most?" → Focus: Identify levers, test sensitivity, prioritize
- **P14 (Revenue Optimization):** "How would you increase revenue?" → Focus: Revenue levers (Price, Volume, Mix) → Test → Measure → Iterate

### L9 vs L3 Distinction:
- **L9 (Financial Sensitivity):** "What moves revenue most?" → Focus: Sensitivity analysis, which lever matters most
- **L3 (Cost / ROI):** "Should we build X?" → Focus: Cost drivers, benefits, breakeven, decision

### Red Flags (NOT L9):
- "How would you increase revenue?" → P14 (Revenue Optimization)
- "Should we build X?" → L3 (Cost / ROI)
- "How do you calculate ROI?" → L3 (Cost / ROI)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Financial Sensitivity Framework** (HIGHEST PRIORITY)
2. ✅ **Lever Prioritization** (HIGH PRIORITY)

**For Data Engineer:**
1. ✅ **Financial Sensitivity Framework** (HIGHEST) - Understand business drivers
2. ⚠️ **Lever Prioritization** (MEDIUM) - Less relevant for DE

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Financial Sensitivity Framework
**Questions:** ~8 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "What moves revenue most?" or "Which lever has biggest impact?" - core financial sensitivity framework
- **Framework:** Levers (Price, Volume, Churn) → Impact → Constraints → Prioritize
- **Identify Levers:** Price (ARPU, fees, discounting, pricing tiers), Volume (Users, orders, sessions, transactions, engagement), Churn (Retention, repeat rate, lifetime value, customer lifetime)
- **Sensitivity Test:** +1% Price → Δ Revenue? (Price elasticity, churn risk), +1% Volume → Δ Revenue? (Scalability, marginal cost), -1% Churn → Δ LTV? (Lifetime value impact, compounding effect), Rule: Use direction + relative size, not exact math
- **Constraints:** Price elasticity (How much demand drops with price increase), Supply/ops limits (Capacity constraints, operational bottlenecks), Market saturation (Addressable market size, growth ceiling), Competitive response (How competitors react), Switching costs (How easy/hard for users to leave), Regulatory/legal (Pricing regulations, compliance limits)
- **Prioritize:** High impact × low risk first, Short-term vs long-term split, One primary lever (not all), Output: "We focus on X because it moves Y the most"

**Concrete Examples:**
- "Subscription app profitability: Levers (Price: +5% risks churn, Volume: CAC rising, Churn: 1% ↓ churn = big LTV gain), Constraints (Competitive pricing pressure, high switching costs), Decision (Focus on retention first)"
- "Financial sensitivity: Identify levers, test sensitivity, assess constraints, prioritize focus"

**Representative Questions (Do 5 only):**
- Q34: As a leader at Spotify, how would you triple its revenue in the next three years? (revenue growth/sensitivity angle)
- Q35: As a leader at Target, how would you increase revenue? (revenue growth/sensitivity angle)
- Q52: As a PM at Reddit, how would you develop a strategy to monetize end consumers? (monetization/sensitivity angle)
- Q73: As a PM for Zepto, how would you develop a strategy to increase the average order value per user? (AOV increase/sensitivity angle)
- Q77: As a Product Manager at Clipboard Health, how would you adjust Lyft's driver payments to maximize net revenue over 12 months? (pricing optimization/sensitivity angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Levers (Price, Volume, Churn) → Impact → Constraints → Prioritize`

**Memorizable Answer:**

When analyzing financial sensitivity, I use Levers (Price, Volume, Churn) → Impact → Constraints → Prioritize.

**1️⃣ Identify Levers** → 
  - **Price:** ARPU (average revenue per user), fees, discounting, pricing tiers (what can we charge?)
  - **Volume:** Users, orders, sessions, transactions, engagement (how many users/transactions?)
  - **Churn:** Retention, repeat rate, lifetime value, customer lifetime (how long do users stay?)

**2️⃣ Test Sensitivity** → 
  - **+1% Price → Δ Revenue?** Price elasticity (how much demand drops), Churn risk (will users leave?), Revenue impact (if inelastic, +1% price = +1% revenue, if elastic, demand drops more)
  - **+1% Volume → Δ Revenue?** Scalability (can we handle more volume?), Marginal cost (does cost scale with volume?), Revenue impact (if scalable, +1% volume = +1% revenue, if not, costs increase)
  - **-1% Churn → Δ LTV?** Lifetime value impact (longer lifetime = more revenue), Compounding effect (small churn changes compound over time), Revenue impact (-1% churn can = +5-10% LTV)

**Rule:** Use direction + relative size, not exact math. Sensitivity beats precision early on. Small churn changes compound more than price hikes. Not all growth is profitable growth.

**3️⃣ Assess Constraints** → 
  - **Price elasticity:** How much demand drops with price increase
  - **Supply/ops limits:** Capacity constraints, operational bottlenecks
  - **Market saturation:** Addressable market size, growth ceiling
  - **Competitive response:** How competitors react to changes
  - **Switching costs:** How easy/hard for users to leave
  - **Regulatory/legal:** Pricing regulations, compliance limits

**4️⃣ Prioritize** → 
  - **High impact × low risk first:** Maximize outcome while minimizing downside
  - **Short-term vs long-term split:** Balance immediate gains with sustainable growth
  - **One primary lever (not all):** Pick one lever to lead, others to support

**Quick sensitivity grid:**
  - **Price:** High impact, High risk, Medium control → Careful
  - **Volume:** Medium impact, Medium risk, Low control → Secondary
  - **Churn:** High impact, Low risk, High control → Primary often

**Output:** "We focus on X because it moves Y the most."

**Key Principle:** Pick one lever to lead, others to support.

---

**How to Adapt This Narrative for Each Question:**

- **Q34 (Spotify triple revenue in 3 years):** Focus on 3x revenue growth
  - "Identify Levers: Price (increase subscription price, add tiers), Volume (increase subscribers, engagement), Churn (reduce churn, increase retention)"
  - "Sensitivity Test: +1% Price (if inelastic, +1% revenue, but risk churn), +1% Volume (if scalable, +1% revenue, but CAC might increase), -1% Churn (can = +5-10% LTV, compounding effect)"
  - "Constraints: Price elasticity (music streaming is competitive, price-sensitive), Supply/ops (can scale infrastructure), Market saturation (growing market, room to grow), Competitive response (competitors will match), Switching costs (low - easy to switch), Regulatory (no major constraints)"
  - "Prioritize: Primary lever (Volume - increase subscribers - market growing, scalable, high impact), Secondary (Churn - reduce churn - high impact, low risk, high control), Careful (Price - test carefully - high impact but high risk)"
  - "Focus on: Volume (grow subscribers through - better content, international expansion, partnerships, freemium conversion), Churn (reduce churn through - better recommendations, exclusive content, user experience), Price (test price increases carefully, add premium tiers)"
  - "Prioritize Volume as primary lever because: High impact (3x = need significant growth), Scalable (infrastructure can handle), Market opportunity (growing market)"

- **Q73 (Zepto increase AOV):** Emphasize AOV sensitivity
  - "Identify Levers: Price (increase item prices, add premium items), Volume (increase items per order), Churn (increase order frequency - more orders = higher total value)"
  - "Sensitivity Test: +1% Price (if inelastic, +1% AOV, but risk fewer orders), +1% Volume (more items per order = higher AOV), -1% Churn (more frequent orders = higher lifetime value)"
  - "Constraints: Price elasticity (grocery delivery is price-sensitive), Supply/ops (can handle more items), Market saturation (growing market), Competitive response (competitors will match), Switching costs (low), Regulatory (no major constraints)"
  - "Prioritize: Primary lever (Volume - increase items per order - high impact, medium risk, high control - can influence through recommendations, bundles, minimum order incentives), Secondary (Churn - increase order frequency - high impact, low risk, high control), Careful (Price - test carefully - high impact but high risk)"
  - "Focus on: Volume (increase items per order through - product recommendations, bundles, 'frequently bought together', minimum order incentives, cross-sell), Churn (increase order frequency through - subscriptions, reminders, loyalty program), Price (test price increases carefully, add premium items)"
  - "Prioritize Volume as primary lever because: High impact (more items = higher AOV), High control (can influence through recommendations, UX), Lower risk (less likely to reduce orders than price increase)"

---

### BUCKET 2: Lever Prioritization
**Questions:** ~2 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Which lever should we focus on?" or "What moves the business most?" - same framework, with focus on prioritization
- **Approach:** Same financial sensitivity framework, with focus on lever prioritization
- **Prioritization:** Sensitivity grid (Impact, Risk, Control), High impact × low risk first, One primary lever
- **Decision Framework:** Primary lever (Focus here), Secondary levers (Support primary), Avoid (High risk, low impact)

**Concrete Examples:**
- "Lever prioritization: Price (High impact, High risk, Medium control → Careful), Volume (Medium impact, Medium risk, Low control → Secondary), Churn (High impact, Low risk, High control → Primary)"
- "Prioritize levers: Test sensitivity, assess constraints, pick primary lever, support with secondary"

**Representative Questions (Do 5 only):**
- Q34: As a leader at Spotify, how would you triple its revenue in the next three years? (lever prioritization angle)
- Q35: As a leader at Target, how would you increase revenue? (lever prioritization angle)
- Q52: As a PM at Reddit, how would you develop a strategy to monetize end consumers? (lever prioritization angle)
- Q73: As a PM for Zepto, how would you develop a strategy to increase the average order value per user? (lever prioritization angle)
- Q77: As a Product Manager at Clipboard Health, how would you adjust Lyft's driver payments to maximize net revenue over 12 months? (lever prioritization angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Sensitivity Grid → Prioritize → One Primary Lever`

**Memorizable Answer:**

When prioritizing levers, I use the same financial sensitivity framework but focus on prioritization.

**1️⃣ Create Sensitivity Grid** → Lever | Impact | Risk | Control | Verdict

**2️⃣ Test Each Lever** → 
  - **Price:** High impact, High risk, Medium control → Careful
  - **Volume:** Medium impact, Medium risk, Low control → Secondary
  - **Churn:** High impact, Low risk, High control → Primary often

**3️⃣ Prioritize** → 
  - **High impact × low risk first:** Maximize outcome, minimize downside
  - **One primary lever:** Not all - pick one to lead, others to support
  - **Short-term vs long-term:** Balance immediate gains with sustainable growth

**Output:** "We focus on X because it moves Y the most."

**Key Principle:** Pick one lever to lead, others to support.

---

**How to Adapt This Narrative for Each Question:**

- **Q77 (Lyft driver payments maximize revenue):** Focus on pricing optimization
  - "Identify Levers: Price (driver payment rate - lower = higher margin, but risk driver churn), Volume (number of rides - more rides = more revenue, but need drivers), Churn (driver retention - retain drivers = lower acquisition cost, more rides)"
  - "Sensitivity Test: +1% Price reduction (if drivers don't churn, +1% margin, but risk driver churn), +1% Volume (more rides = more revenue, but need to attract/retain drivers), -1% Driver churn (lower acquisition cost, more rides, higher revenue)"
  - "Constraints: Price elasticity (drivers are price-sensitive, will churn if pay too low), Supply/ops (need enough drivers), Market saturation (growing market), Competitive response (Uber will match), Switching costs (low - drivers can switch), Regulatory (minimum wage, regulations)"
  - "Prioritize: Primary lever (Balance Price and Churn - optimize driver payment to maximize revenue - high impact, need to balance risk), Secondary (Volume - increase rides - medium impact, depends on drivers), Avoid (aggressive price cuts - high risk of driver churn)"
  - "Focus on: Optimize driver payment (find sweet spot - high enough to retain drivers, low enough to maximize margin, Test different rates, monitor driver churn, revenue impact), Support with Volume (increase rides through - better matching, incentives, driver supply), Monitor Churn (track driver retention, adjust payment if churn increases)"
  - "Prioritize balancing Price and Churn because: High impact (driver payment directly affects margin and driver supply), Need balance (too low = driver churn, too high = low margin)"

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Financial Sensitivity Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Lever Prioritization** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through financial sensitivity framework in 2 minutes (Levers → Impact → Constraints → Prioritize)
- [ ] Identify levers (Price, Volume, Churn)
- [ ] Test sensitivity (+1% Price, +1% Volume, -1% Churn)
- [ ] Assess constraints (Elasticity, supply limits, market saturation, competitive response)
- [ ] Prioritize (High impact × low risk, one primary lever)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the financial sensitivity framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Levers (Price, Volume, Churn) → Impact → Constraints → Prioritize framework**, not memorizing answers

**Remember:** L9 is about financial sensitivity. The framework: Levers (Price, Volume, Churn) → Impact → Constraints → Prioritize. Key principles: Small churn changes compound more than price hikes. Not all growth is profitable growth. Sensitivity beats precision early on. Pick one lever to lead, others to support.
