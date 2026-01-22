# Executive Study Plan: L6 - Ops Tradeoffs
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~5 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L6 (OPS TRADEOFFS) QUESTIONS

**Even when "ops tradeoffs" isn't mentioned, look for these keywords/phrases:**

### Explicit Ops Tradeoff Keywords:
- "tradeoffs", "balance", "speed vs quality", "reliability vs speed", "SLO", "SLA", "error budget"
- "fast releases vs uptime", "ship fast vs stable", "deployment strategy", "release cadence"
- "how do you balance", "speed vs reliability", "quality vs speed"

### Implicit L6 Indicators:
- **Balance questions:** "How do you balance fast releases with uptime?", "Speed vs quality vs reliability?"
- **SLO/SLA questions:** "How do you set SLOs?", "What's your error budget?", "How do you manage SLAs?"
- **Deployment questions:** "How do you deploy safely?", "Release strategy", "Canary vs blue-green"

### L6 vs P7 Distinction:
- **L6 (Ops Tradeoffs):** "How do you balance fast releases with uptime?" → Focus: Speed vs Quality vs Reliability, SLOs, Error budgets
- **P7 (Tradeoff Framing):** "How do you make tradeoffs?" → Focus: General tradeoff analysis framework

### L6 vs P12 Distinction:
- **L6 (Ops Tradeoffs):** "How do you balance speed vs reliability?" → Focus: Operational tradeoffs, error budgets
- **P12 (Operational Excellence):** "How do you ensure system reliability?" → Focus: Operational process

### Red Flags (NOT L6):
- "How do you make tradeoffs?" → P7 (Tradeoff Framing)
- "How do you ensure system reliability?" → P12 (Operational Excellence)
- "How do you monitor a system?" → L5 (Observability)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Ops Tradeoffs Framework** (HIGHEST PRIORITY)
2. ⚠️ **SLOs & Error Budgets** (MEDIUM)

**For Data Engineer:**
1. ✅ **Ops Tradeoffs Framework** (HIGHEST) - Core framework
2. ✅ **SLOs & Error Budgets** (HIGH) - Practical application

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Ops Tradeoffs Framework
**Questions:** ~3 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "How do you balance fast releases with uptime?" or "Speed vs quality vs reliability?" - core ops tradeoffs framework
- **Framework:** Speed vs Quality vs Reliability → SLAs → Error Budget → Decide
- **Speed vs Quality vs Reliability:** Speed (Fast deploys, Rapid iteration, Short time-to-market), Quality (Fewer bugs, Correctness, User trust), Reliability (Uptime, Consistency, Predictability), Rule: You can maximize 2, never all 3
- **SLAs/SLOs:** SLI (signal: Availability, Latency, Success rate), SLO (target: 99.9% uptime, p95 < 300ms, <0.1% errors), SLA (external promise: What customers can hold you to)
- **Error Budget:** Error Budget = 1 − SLO (99.9% SLO → 0.1% budget, Budget = permission to move fast), Budget healthy? (YES → Ship faster, NO → Freeze launches, fix reliability), Shared contract (Product wants speed, Ops wants stability)
- **Decide + Communicate:** Make tradeoff explicit, Align stakeholders, Revisit when conditions change

**Concrete Examples:**
- "Fast releases vs uptime: Tradeoff (Speed + Reliability, accept slightly lower quality via flags), SLO (99.9% availability), Error Budget (Healthy → canary deploys OK, Burned → freeze features), Decision (Slow down launches until budget recovers)"
- "Ops tradeoffs: Identify tension (Speed vs Quality vs Reliability), Set SLOs, Manage error budget, Make explicit decision"

**Representative Questions (Do 5 only):**
- Q1571: How would you structure the CEO's calendar and priorities? (executive operations/ops tradeoffs angle)
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (capacity/ops tradeoffs angle)
- Q179: Create a simple model to forecast our headcount needs for the next 12-weeks as we scale up. (scaling/ops tradeoffs angle)
- Q473: Design a scalable system for a token-generation service used by an LLM that needs to handle up to 100,000 requests per second. (scale/ops tradeoffs angle)
- Q117: As the PM for Lyft, what dashboard would you build to track the health of the app? (monitoring/ops tradeoffs angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When thinking about ops tradeoffs, I use Speed vs Quality vs Reliability → SLAs → Error Budget → Decide. First, I identify the tension: Speed (Fast deploys, rapid iteration, short time-to-market), Quality (Fewer bugs, correctness, user trust), Reliability (Uptime, consistency, predictability). The key rule: You can maximize 2, never all 3. I pick which 2 to optimize based on context: Early startup → Speed + Quality, Regulated/payments system → Reliability + Quality, Core user-facing feature → Quality + Reliability, Incident ongoing → Reliability first, Innovation window open → Speed first. Second, I set SLAs/SLOs: SLI (signal: Availability, Latency, Success rate), SLO (target: 99.9% uptime, p95 < 300ms, <0.1% errors), SLA (external promise: What customers can hold you to). Third, I manage Error Budget: Error Budget = 1 − SLO (99.9% SLO → 0.1% budget, Budget = permission to move fast), Budget healthy? (YES → Ship faster, canary deploys OK, NO → Freeze launches, fix reliability), Shared contract (Product wants speed, Ops wants stability - error budget aligns them). Finally, I Decide + Communicate: Make tradeoff explicit (Don't let it be implicit - someone silently pays the cost, usually users or on-call), Align stakeholders (Product, ops, engineering all agree on tradeoff), Revisit when conditions change (As business matures, tradeoffs shift). The key principle: If tradeoffs are implicit, someone is silently paying the cost (usually users or on-call)."

**How to Adapt This Narrative for Each Question:**

- **Q1571 (CEO calendar and priorities):** Focus on executive operations → "To structure CEO's calendar and priorities, I'd: Identify tension (Speed: Fast decisions, rapid execution, Quality: Thoughtful decisions, thorough analysis, Reliability: Consistent execution, predictable outcomes), Pick 2 to optimize (Based on context: Early stage → Speed + Quality, Growth stage → Speed + Reliability, Mature stage → Quality + Reliability), Set SLAs (SLO: CEO availability, response time, decision quality, SLA: External commitments, board meetings), Error Budget (Budget: How much can we move fast? Healthy → can take on more, Burned → need to slow down, focus on execution), Decide + Communicate (Make tradeoff explicit: What are we optimizing for? Speed vs quality vs reliability, Align stakeholders: Leadership team agrees, Revisit: As company grows, tradeoffs shift). I'd prioritize: High-impact decisions (strategic, board-level), Time-sensitive (market opportunities), Relationship-building (key stakeholders). I'd use error budget concept: If calendar is healthy (not overbooked), can take on more. If burned (overbooked, stressed), need to slow down, delegate, or say no."

- **Q110 (Gas station 4x capacity surge):** Emphasize ops tradeoffs → "To handle 4x capacity surge, I'd: Identify tension (Speed: Serve customers quickly, Quality: Good service, Reliability: Consistent experience), Pick 2 (During surge: Speed + Reliability - prioritize getting customers through, accept slightly lower quality), Set SLAs (SLO: Customer wait time < 5 min, Service quality acceptable, SLA: Customer satisfaction), Error Budget (Budget: How much can we handle? Healthy → can handle surge, Burned → need to slow down, limit capacity), Decide + Communicate (Make tradeoff explicit: During surge, we prioritize speed and reliability over perfect quality, Align stakeholders: Staff knows priorities, Revisit: After surge, return to normal tradeoffs). I'd optimize: Speed (Fast service, quick checkout), Reliability (Consistent experience, no breakdowns), Accept lower quality (Slightly rushed service, less personalization)."

---

### BUCKET 2: SLOs & Error Budgets
**Questions:** ~2 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "How do you set SLOs?" or "What's your error budget?" - same framework, with focus on SLOs
- **Approach:** Same ops tradeoffs framework, with focus on SLOs and error budgets
- **SLO Design:** SLI (What we measure), SLO (Target we promise), SLA (External commitment)
- **Error Budget Management:** Calculate budget, Monitor health, Make decisions based on budget

**Concrete Examples:**
- "SLO design: SLI (Availability, latency, success rate), SLO (99.9% uptime, p95 < 300ms), Error Budget (0.1% = permission to move fast)"
- "Error budget: Calculate (1 - SLO), Monitor (Healthy vs burned), Decide (Ship faster if healthy, freeze if burned)"

**Representative Questions (Do 5 only):**
- Q1571: How would you structure the CEO's calendar and priorities? (SLOs/error budget angle)
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (SLOs/error budget angle)
- Q117: As the PM for Lyft, what dashboard would you build to track the health of the app? (SLOs/error budget angle)
- Q179: Create a simple model to forecast our headcount needs for the next 12-weeks as we scale up. (SLOs/error budget angle)
- Q473: Design a scalable system for a token-generation service used by an LLM that needs to handle up to 100,000 requests per second. (SLOs/error budget angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When designing SLOs and error budgets, I use the same ops tradeoffs framework but focus on SLO design and error budget management. I design SLOs: SLI (What we measure: Availability, Latency, Success rate), SLO (Target we promise: 99.9% uptime, p95 < 300ms, <0.1% errors), SLA (External commitment: What customers can hold us to). I calculate Error Budget: Error Budget = 1 − SLO (99.9% SLO → 0.1% budget, Budget = permission to move fast). I monitor budget health: Healthy (YES → Ship faster, canary deploys OK, take risks), Burned (NO → Freeze launches, fix reliability, be conservative). I make decisions: If budget healthy → move fast, If budget burned → slow down, fix issues. The key is using error budget as a shared contract between product (wants speed) and ops (wants stability)."

**How to Adapt This Narrative for Each Question:**

- **Q1571 (CEO calendar SLOs):** Focus on SLOs for executive operations → "To set SLOs for CEO calendar, I'd: SLI (What we measure: CEO availability, Response time, Decision quality, Meeting effectiveness), SLO (Target: 80% calendar utilization, <24h response time, High-quality decisions, SLA: External commitments met, board meetings prepared), Error Budget (Budget: 20% buffer = permission to take on urgent items, Healthy → can take on more, Burned → need to slow down, delegate, say no), Decisions (If healthy: Can take on strategic initiatives, If burned: Need to prioritize, delegate, or decline). I'd use error budget to balance: Speed (Fast decisions, rapid execution) vs Reliability (Consistent availability, predictable schedule)."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Ops Tradeoffs Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **SLOs & Error Budgets** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through ops tradeoffs framework in 2 minutes (Speed vs Quality vs Reliability → SLAs → Error Budget → Decide)
- [ ] Identify tension (Speed, quality, reliability - pick 2)
- [ ] Set SLOs (SLI, SLO, SLA)
- [ ] Manage error budget (Calculate, monitor, decide)
- [ ] Make tradeoff explicit (Communicate, align stakeholders)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the ops tradeoffs framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Speed vs Quality vs Reliability → SLAs → Error Budget → Decide framework**, not memorizing answers

**Remember:** L6 is about ops tradeoffs. The framework: Speed vs Quality vs Reliability → SLAs → Error Budget → Decide. Key principle: If tradeoffs are implicit, someone is silently paying the cost (usually users or on-call). You can maximize 2, never all 3.
