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
> "When analyzing financial sensitivity, I use Levers (Price, Volume, Churn) → Impact → Constraints → Prioritize. First, I identify Levers: Price (ARPU - average revenue per user, fees, discounting, pricing tiers - what can we charge?), Volume (Users, orders, sessions, transactions, engagement - how many users/transactions?), Churn (Retention, repeat rate, lifetime value, customer lifetime - how long do users stay?). Each lever can impact revenue/profitability, but with different sensitivity and constraints. Second, I test Sensitivity: +1% Price → Δ Revenue? (Price elasticity: how much demand drops with price increase, Churn risk: will users leave?, Revenue impact: if inelastic, +1% price = +1% revenue, if elastic, demand drops more), +1% Volume → Δ Revenue? (Scalability: can we handle more volume?, Marginal cost: does cost scale with volume?, Revenue impact: if scalable, +1% volume = +1% revenue, if not, costs increase), -1% Churn → Δ LTV? (Lifetime value impact: longer lifetime = more revenue, Compounding effect: small churn changes compound over time, Revenue impact: -1% churn can = +5-10% LTV). Rule: Use direction + relative size, not exact math. Sensitivity beats precision early on. Small churn changes compound more than price hikes. Not all growth is profitable growth. Third, I assess Constraints: Price elasticity (How much demand drops with price increase - if elastic, small price increase = big demand drop), Supply/ops limits (Capacity constraints, operational bottlenecks - can we handle more volume?), Market saturation (Addressable market size, growth ceiling - is there room to grow?), Competitive response (How competitors react to changes - will they match prices?), Switching costs (How easy/hard for users to leave - high switching costs = can raise price, low = can't), Regulatory/legal (Pricing regulations, compliance limits - are there constraints?). Finally, I Prioritize: High impact × low risk first (Maximize outcome while minimizing downside), Short-term vs long-term split (Balance immediate gains with sustainable growth), One primary lever (not all) - pick one lever to lead, others to support. Quick sensitivity grid: Price (High impact, High risk, Medium control → Careful), Volume (Medium impact, Medium risk, Low control → Secondary), Churn (High impact, Low risk, High control → Primary often). Output: 'We focus on X because it moves Y the most.' The key principle: Pick one lever to lead, others to support."

**How to Adapt This Narrative for Each Question:**

- **Q34 (Spotify triple revenue in 3 years):** Focus on 3x revenue growth → "To triple Spotify's revenue in 3 years, I'd: Identify Levers (Price: Increase subscription price, add tiers, Volume: Increase subscribers, engagement, Churn: Reduce churn, increase retention), Sensitivity Test (+1% Price: If inelastic, +1% revenue, but risk churn, +1% Volume: If scalable, +1% revenue, but CAC might increase, -1% Churn: Can = +5-10% LTV, compounding effect), Constraints (Price elasticity: Music streaming is competitive, price-sensitive, Supply/ops: Can scale infrastructure, Market saturation: Growing market, room to grow, Competitive response: Competitors will match, Switching costs: Low - easy to switch, Regulatory: No major constraints), Prioritize (Primary lever: Volume - increase subscribers (market growing, scalable, high impact), Secondary: Churn - reduce churn (high impact, low risk, high control), Careful: Price - test carefully (high impact but high risk). I'd focus on: Volume (Grow subscribers through: Better content, international expansion, partnerships, freemium conversion), Churn (Reduce churn through: Better recommendations, exclusive content, user experience), Price (Test price increases carefully, add premium tiers). I'd prioritize Volume as primary lever because: High impact (3x = need significant growth), Scalable (Infrastructure can handle), Market opportunity (Growing market)."

- **Q73 (Zepto increase AOV):** Emphasize AOV sensitivity → "To increase Zepto's AOV per user, I'd: Identify Levers (Price: Increase item prices, add premium items, Volume: Increase items per order, Churn: Increase order frequency - more orders = higher total value), Sensitivity Test (+1% Price: If inelastic, +1% AOV, but risk fewer orders, +1% Volume: More items per order = higher AOV, -1% Churn: More frequent orders = higher lifetime value), Constraints (Price elasticity: Grocery delivery is price-sensitive, Supply/ops: Can handle more items, Market saturation: Growing market, Competitive response: Competitors will match, Switching costs: Low, Regulatory: No major constraints), Prioritize (Primary lever: Volume - increase items per order (High impact, medium risk, high control - can influence through: Recommendations, bundles, minimum order incentives), Secondary: Churn - increase order frequency (High impact, low risk, high control), Careful: Price - test carefully (High impact but high risk). I'd focus on: Volume (Increase items per order through: Product recommendations, bundles, 'frequently bought together', minimum order incentives, cross-sell), Churn (Increase order frequency through: Subscriptions, reminders, loyalty program), Price (Test price increases carefully, add premium items). I'd prioritize Volume as primary lever because: High impact (More items = higher AOV), High control (Can influence through recommendations, UX), Lower risk (Less likely to reduce orders than price increase)."

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
> "When prioritizing levers, I use the same financial sensitivity framework but focus on prioritization. I create a sensitivity grid: Lever | Impact | Risk | Control | Verdict. I test each lever: Price (High impact, High risk, Medium control → Careful), Volume (Medium impact, Medium risk, Low control → Secondary), Churn (High impact, Low risk, High control → Primary often). I prioritize: High impact × low risk first (Maximize outcome, minimize downside), One primary lever (Not all - pick one to lead, others to support), Short-term vs long-term (Balance immediate gains with sustainable growth). The key is picking one lever to lead, others to support. Output: 'We focus on X because it moves Y the most.'"

**How to Adapt This Narrative for Each Question:**

- **Q77 (Lyft driver payments maximize revenue):** Focus on pricing optimization → "To adjust Lyft's driver payments to maximize net revenue, I'd: Identify Levers (Price: Driver payment rate (lower = higher margin, but risk driver churn), Volume: Number of rides (more rides = more revenue, but need drivers), Churn: Driver retention (retain drivers = lower acquisition cost, more rides)), Sensitivity Test (+1% Price reduction: If drivers don't churn, +1% margin, but risk driver churn, +1% Volume: More rides = more revenue, but need to attract/retain drivers, -1% Driver churn: Lower acquisition cost, more rides, higher revenue), Constraints (Price elasticity: Drivers are price-sensitive, will churn if pay too low, Supply/ops: Need enough drivers, Market saturation: Growing market, Competitive response: Uber will match, Switching costs: Low - drivers can switch, Regulatory: Minimum wage, regulations), Prioritize (Primary lever: Balance Price and Churn - optimize driver payment to maximize revenue (High impact, need to balance risk), Secondary: Volume - increase rides (Medium impact, depends on drivers), Avoid: Aggressive price cuts (High risk of driver churn). I'd focus on: Optimize driver payment (Find sweet spot: High enough to retain drivers, low enough to maximize margin, Test different rates, monitor driver churn, revenue impact), Support with Volume (Increase rides through: Better matching, incentives, driver supply), Monitor Churn (Track driver retention, adjust payment if churn increases). I'd prioritize balancing Price and Churn because: High impact (Driver payment directly affects margin and driver supply), Need balance (Too low = driver churn, too high = low margin)."

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
