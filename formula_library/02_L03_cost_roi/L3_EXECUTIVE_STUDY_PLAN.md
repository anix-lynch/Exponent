# Executive Study Plan: L3 - Cost / ROI
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~30 questions → 3 concept buckets → 2-3 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L3 (COST / ROI) QUESTIONS

**Even when "cost" or "ROI" isn't mentioned, look for these keywords/phrases:**

### Explicit Cost/ROI Keywords:
- "cost", "ROI", "return on investment", "breakeven", "payback"
- "CAC", "LTV", "cost per acquisition", "lifetime value", "unit economics"
- "should we build", "is it worth it", "financial analysis", "cost-saving"

### Implicit L3 Indicators:
- **Build decisions:** "Should we build X?", "Is it worth building?", "What's the ROI?"
- **Cost questions:** "What is the cost for X?", "How much does X cost?", "Cost-saving opportunity"
- **Financial analysis:** "Break-even analysis", "Revenue estimation", "Market sizing"
- **Estimation questions:** "Estimate X revenue", "How many X will ship?", "Market size"

### L3 vs P14 Distinction:
- **L3 (Cost / ROI):** "Should we build X?" → Focus: Cost drivers, benefits, breakeven, decision
- **P14 (Revenue Optimization):** "How would you increase revenue?" → Focus: Revenue levers (Price, Volume, Mix)

### L3 vs P6 Distinction:
- **L3 (Cost / ROI):** "Should we build X?" → Focus: Financial analysis, ROI calculation
- **P6 (Prioritization):** "How do you prioritize features?" → Focus: Prioritization framework (RICE, impact/effort)

### Red Flags (NOT L3):
- "How would you increase revenue?" → P14 (Revenue Optimization)
- "How do you prioritize features?" → P6 (Prioritization)
- "How do you scale a system?" → L2 (Scale & Capacity)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2-3 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Cost / ROI Framework** (HIGHEST PRIORITY)
2. ✅ **Build Decisions** (HIGH PRIORITY)
3. ⚠️ **Financial Estimation** (MEDIUM)

**For Data Engineer:**
1. ✅ **Cost / ROI Framework** (HIGHEST) - Understand cost drivers
2. ⚠️ **Build Decisions** (MEDIUM) - Technical build decisions
3. ❌ **Financial Estimation** (LOW - skip for now)

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Cost / ROI Framework
**Questions:** ~15 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Should we build X?" or "What's the ROI?" - core cost/ROI framework
- **Framework:** Cost Drivers → Benefits → Breakeven → Decide
- **Cost Drivers:** Build cost (Eng time: people × weeks, Opportunity cost: what we don't build, One-time infra setup), Run cost (Compute/storage/bandwidth, Third-party APIs, Support & ops), Risk cost (Reliability risk, Compliance/legal, Brand damage)
- **Benefits:** Revenue (New users, Higher conversion, ARPU/LTV lift), Cost savings (Automation, Infra reduction, Support deflection), Strategic (Learning, Moat/differentiation, Risk reduction)
- **Breakeven:** Simple math (Monthly benefit, Monthly cost, Payback period), Sensitivity (Best case, Base case, Worst case)
- **Decide:** Greenlight (Short payback, Asymmetric upside), Scope down (MVP first, Cheaper experiment), Kill/Defer (Long breakeven, High downside)

**Concrete Examples:**
- "Build decision: Cost drivers (Build: 3 eng × 1 month = $90k, Run: $2k/month), Benefits (Faster launches, fewer rollbacks, $8k/month saved), Breakeven ($90k / $8k = 11 months), Decision (Build MVP or buy)"
- "ROI analysis: Identify costs, quantify benefits, calculate breakeven, make decision"

**Representative Questions (Do 5 only):**
- Q3.1: What is the cost for a new Facebook customer acquisition? (CAC calculation angle)
- Q108: As the new CEO of Blue Origin, what actions would you take to make the company break even? (break-even analysis angle)
- Q219: Describe a time when you identified a cost-saving opportunity. (cost optimization angle)
- Q124: Assuming AR-enabled glasses exist in 2031, how many do you think will ship that year? What factors will you consider in your estimation? (market estimation angle)
- Q739: Estimate Airbnb's Revenue. (revenue estimation angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When evaluating cost and ROI, I use Cost Drivers → Benefits → Breakeven → Decide. First, I identify Cost Drivers: Build cost (Eng time: people × weeks - engineering effort, Opportunity cost: what we don't build - tradeoffs, One-time infra setup: initial infrastructure investment), Run cost (Compute/storage/bandwidth: ongoing infrastructure costs, Third-party APIs: external service fees, Support & ops: operational overhead, maintenance), Risk cost (Reliability risk: potential downtime, service degradation, Compliance/legal: regulatory, legal exposure, Brand damage: reputation risk, user trust impact). Second, I quantify Benefits: Revenue (New users: user acquisition, market expansion, Higher conversion: improved conversion rates, ARPU/LTV lift: average revenue per user, lifetime value increase), Cost savings (Automation: reduce manual work, operational efficiency, Infra reduction: lower infrastructure costs, Support deflection: fewer support tickets, self-service), Strategic (Learning: knowledge, insights, experimentation value, Moat/differentiation: competitive advantage, Risk reduction: mitigate existing risks). Third, I calculate Breakeven: Simple math (Monthly benefit: recurring value - revenue or savings, Monthly cost: ongoing operational costs, Payback period: build cost / monthly net benefit), Sensitivity (Best case: optimistic scenario - high adoption, high value, Base case: realistic scenario - expected outcomes, Worst case: pessimistic scenario - low adoption, high costs), Sanity checks (Unit economics: does usage scale cost?, Reversibility: can we undo this?, Fixed vs variable: what grows with scale?). Finally, I Decide: Greenlight (Short payback: < 6-12 months typically acceptable, Asymmetric upside: high potential reward vs risk), Scope down (MVP first: build minimal version to test assumptions, Cheaper experiment: validate with lower investment), Kill/Defer (Long breakeven: payback period too long > 18-24 months, High downside: significant risk, low confidence). The key principle: ROI is not 'big upside.' It's 'good outcomes even if we're wrong.'"

**How to Adapt This Narrative for Each Question:**

- **Q3.1 (Facebook CAC):** Focus on CAC calculation → "To calculate Facebook customer acquisition cost, I'd: Cost Drivers (Build cost: Marketing spend - ads, campaigns, creative, Eng time: if building acquisition tools, Opportunity cost: other marketing channels not pursued, Run cost: Ongoing ad spend, platform fees, tools, Support & ops: Marketing team, analytics, Risk cost: Brand risk, compliance), Benefits (Revenue: New users acquired, Higher conversion: Better targeting improves conversion, ARPU/LTV lift: Better users = higher LTV, Cost savings: Automation - better targeting reduces waste, Strategic: Learning - what works, Moat - better acquisition), Breakeven (Monthly benefit: Revenue from new users - ARPU × users acquired, Monthly cost: Ad spend, platform fees, Payback period: Total acquisition cost / monthly net benefit per user, Sensitivity: Best case - high LTV users, Base case - average users, Worst case - low retention), Decide (If CAC < LTV/3: Greenlight, If close: Scope down - test smaller, If CAC > LTV: Kill/Defer - not sustainable). I'd calculate: CAC = Total marketing spend / New customers acquired."

- **Q108 (Blue Origin break even):** Emphasize break-even strategy → "To make Blue Origin break even, I'd: Cost Drivers (Build cost: R&D, manufacturing, infrastructure, Eng time: engineering teams, Opportunity cost: what we're not building, Run cost: Operations, launches, maintenance, Support & ops: Teams, facilities, Risk cost: Safety, regulatory, brand), Benefits (Revenue: Launch services, contracts, customers, Higher conversion: Better pricing, services, ARPU/LTV lift: Recurring customers, Cost savings: Operational efficiency, automation, Strategic: Learning, moat, risk reduction), Breakeven (Monthly benefit: Revenue from launches, contracts, Monthly cost: Operations, R&D, Payback period: Total investment / monthly net benefit, Sensitivity: Best case - high launch frequency, Base case - expected launches, Worst case - delays, low demand), Decide (If short payback: Greenlight - increase launches, If long: Scope down - reduce costs, focus on profitable segments, Kill/Defer - exit unprofitable lines). I'd focus on: Increase revenue (More launches, better pricing, contracts), Reduce costs (Operational efficiency, automation, focus), Optimize mix (Focus on profitable segments)."

---

### BUCKET 2: Build Decisions
**Questions:** ~10 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Should we build X?" or "Is it worth building?" - same framework, with focus on build decisions
- **Approach:** Same cost/ROI framework, with focus on build vs buy decisions
- **Build vs Buy:** Evaluate both options, Compare costs, Compare benefits, Make decision
- **Decision Framework:** Greenlight, Scope down, Kill/Defer

**Concrete Examples:**
- "Build vs buy: Cost drivers (Build: eng time, Run: ops, Buy: license, support), Benefits (Build: control, customization, Buy: faster, maintained), Breakeven (Compare payback periods), Decision (Build if strategic, buy if commodity)"
- "Build decision: Evaluate costs, benefits, breakeven, decide"

**Representative Questions (Do 5 only):**
- Q219: Describe a time when you identified a cost-saving opportunity. (cost-saving angle)
- Q108: As the new CEO of Blue Origin, what actions would you take to make the company break even? (break-even strategy angle)
- Q3.1: What is the cost for a new Facebook customer acquisition? (cost analysis angle)
- Q124: Assuming AR-enabled glasses exist in 2031, how many do you think will ship that year? What factors will you consider in your estimation? (market estimation/build decision angle)
- Q739: Estimate Airbnb's Revenue. (revenue estimation/build context angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When making build decisions, I use the same cost/ROI framework but focus on build vs buy. I evaluate Cost Drivers for both: Build (Eng time, opportunity cost, infra setup, run cost, risk), Buy (License cost, support cost, integration cost, vendor lock-in risk). I compare Benefits: Build (Control, customization, strategic value, learning), Buy (Faster time to market, maintained, less risk, focus). I calculate Breakeven for both: Build payback vs Buy payback. I Decide: Build if (Strategic value, customization needed, long-term cost advantage), Buy if (Commodity, faster needed, maintenance burden), Scope down (MVP build, test assumptions, validate before full build). The key is evaluating both options systematically."

**How to Adapt This Narrative for Each Question:**

- **Q219 (Cost-saving opportunity):** Focus on cost-saving → "When identifying cost-saving opportunities, I'd: Cost Drivers (Current costs: What are we spending? Build cost: Eng time, infrastructure, Run cost: Ongoing ops, services, Risk cost: Current risks), Benefits (Cost savings: Where can we reduce? Automation: Reduce manual work, Infra reduction: Optimize infrastructure, Support deflection: Self-service, Strategic: Learning, efficiency), Breakeven (Investment needed: What does it cost to implement? Monthly savings: How much do we save? Payback period: Investment / monthly savings, Sensitivity: Best/base/worst case), Decide (If short payback: Greenlight - implement, If medium: Scope down - test first, If long: Kill/Defer - not worth it). I'd focus on high-impact, low-effort opportunities first."

---

### BUCKET 3: Financial Estimation
**Questions:** ~5 | **Priority:** 🔴 RED (Low impact - skip for now)

**Note:** Similar to Bucket 1, but with focus on estimation. Focus on Buckets 1-2 first.

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Cost / ROI Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Build Decisions** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through cost/ROI framework in 2 minutes (Cost Drivers → Benefits → Breakeven → Decide)
- [ ] Identify cost drivers (Build, run, risk costs)
- [ ] Quantify benefits (Revenue, cost savings, strategic)
- [ ] Calculate breakeven (Payback period, sensitivity)
- [ ] Make decision (Greenlight, scope down, kill/defer)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the cost/ROI framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Cost Drivers → Benefits → Breakeven → Decide framework**, not memorizing answers

**Remember:** L3 is about cost and ROI. The framework: Cost Drivers → Benefits → Breakeven → Decide. Key principle: ROI is not "big upside." It's "good outcomes even if we're wrong."
