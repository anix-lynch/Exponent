# Executive Study Plan: P13D - Design Marketplace / Two-Sided Platforms
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~20 questions → 3 concept buckets → 2-3 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY P13D (DESIGN MARKETPLACE / TWO-SIDED PLATFORMS) QUESTIONS

**Even when "marketplace" isn't mentioned, look for these keywords/phrases:**

### Explicit Marketplace Keywords:
- "marketplace", "two-sided", "platform", "matching", "supply and demand"
- "bike-sharing", "rental", "lending", "borrowing", "reservations"
- "supply side", "demand side", "liquidity", "cold start"

### Implicit P13D Indicators:
- **Two-sided focus:** "Design a platform that matches X with Y", "Design a system for X and Y"
- **Matching focus:** "Design a product for matching", "Design a system for connecting"
- **Sharing economy:** "Design bike-sharing", "Design rental service", "Design lending platform"
- **Liquidity concerns:** "How to get started?", "Cold start problem", "Chicken and egg"

### P13D vs P13B Distinction:
- **P13D (Marketplace):** "Design a bike-sharing system" → Focus: Two-sided platform, supply/demand, liquidity
- **P13B (Consumer Platforms):** "Design a social media app" → Focus: Single-sided engagement, core loop

### P13D vs P13C Distinction:
- **P13D (Marketplace):** "Design a marketplace" → Focus: Two-sided platform, matching, liquidity
- **P13C (B2B/SaaS):** "Design a B2B product" → Focus: Enterprise tool, workflow automation

### P13D vs P13A Distinction:
- **P13D (Marketplace):** "Design a bike-sharing system" → Focus: Two-sided platform, supply/demand
- **P13A (Single-User Products):** "Design a better alarm clock" → Focus: Single user, no two-sided market

### Red Flags (NOT P13D):
- "Design a consumer app" → P13B (Consumer Platforms)
- "Design a B2B product" → P13C (B2B/SaaS)
- "Design a physical product" → P13A (Single-User Products)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2-3 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Marketplace Design** (HIGHEST PRIORITY)
2. ✅ **Liquidity & Cold Start** (HIGH PRIORITY)
3. ⚠️ **Balancing Supply/Demand** (MEDIUM)

**For Data Engineer:**
1. ✅ **Marketplace Design** (HIGHEST) - Understand two-sided systems, matching algorithms
2. ✅ **Liquidity & Cold Start** (HIGH) - Technical challenges, data needs
3. ⚠️ **Balancing Supply/Demand** (MEDIUM) - Metrics, algorithms

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Marketplace Design
**Questions:** ~15 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Design a marketplace" or "Design a two-sided platform" - core marketplace framework
- **Framework:** Sides → Value Exchange → Liquidity Risks → MVP → Balancing Levers
- **Sides:** Supply side (Who are suppliers? What do they provide? What are their incentives?), Demand side (Who are buyers/users? What do they need? What are their incentives?)
- **Value Exchange:** What is the value exchange? (Supply → Demand value, Demand → Supply value, Platform value), How is value created? (Matching efficiency, Trust & safety, Network effects)
- **Liquidity Risks:** Cold start problem (No supply → no demand, No demand → no supply), Liquidity strategies (Seed supply/demand, Incentivize early adopters, Phased launch)
- **MVP:** Minimum viable marketplace (Core matching, Basic trust mechanisms, Payment/transaction), Launch strategy (Geographic focus, Category focus, Supply-first or demand-first)
- **Balancing Levers:** Supply/demand balance (Pricing, Incentives, Matching algorithms), Success metrics (Match rate, Liquidity, GMV, Take rate)

**Concrete Examples:**
- "Design bike-sharing: Sides (Supply: Bike owners/operators, Demand: Riders), Value Exchange (Supply provides bikes, Demand pays, Platform matches), Liquidity Risks (Need bikes and riders simultaneously), MVP (Core matching, payment, basic tracking), Balancing Levers (Pricing, incentives, matching)"
- "Design restaurant reservations: Sides (Supply: Restaurants, Demand: Diners), Value Exchange (Supply provides tables, Demand pays, Platform matches), Liquidity Risks (Need restaurants and diners), MVP (Core booking, payment, basic trust), Balancing Levers (Pricing, availability, matching)"

**Representative Questions (Do 5 only):**
- Q264: Design a bike-sharing system for your city. (bike-sharing marketplace angle)
- Q45: As a PM at Meta, design a product for making restaurant reservations. (reservations marketplace angle)
- Q395: Design a platform that matches people wanting to learn skills with relevant mentors. (education marketplace angle)
- Q403: Design a product for borrowing and lending. (lending marketplace angle)
- Q83: As a product manager for Meta, design a product for volunteers. (volunteer marketplace angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When designing a marketplace, I use Sides → Value Exchange → Liquidity Risks → MVP → Balancing Levers. First, I identify Sides: Supply side (Who are suppliers? What do they provide? What are their incentives?), Demand side (Who are buyers/users? What do they need? What are their incentives?). Then I define Value Exchange: What is the value exchange? (Supply → Demand value, Demand → Supply value, Platform value), How is value created? (Matching efficiency, Trust & safety, Network effects). Next, I assess Liquidity Risks: Cold start problem (No supply → no demand, No demand → no supply), Liquidity strategies (Seed supply/demand, Incentivize early adopters, Phased launch). I design MVP: Minimum viable marketplace (Core matching, Basic trust mechanisms, Payment/transaction), Launch strategy (Geographic focus, Category focus, Supply-first or demand-first). Finally, I define Balancing Levers: Supply/demand balance (Pricing, Incentives, Matching algorithms), Success metrics (Match rate, Liquidity, GMV, Take rate). The key is solving the cold start problem and keeping supply/demand balanced."

**How to Adapt This Narrative for Each Question:**

- **Q264 (Design bike-sharing system):** Focus on bike-sharing → "To design a bike-sharing system, I'd: Sides (Supply: Bike owners/operators (provide bikes, want revenue), Demand: Riders (need transportation, want convenience)), Value Exchange (Supply provides bikes, Demand pays for rides, Platform matches efficiently, creates network effects), Liquidity Risks (Cold start: Need bikes and riders simultaneously, No bikes → no riders, No riders → no bikes), Liquidity strategies (Seed supply: Deploy bikes in high-traffic areas, Seed demand: Launch in dense urban areas, Incentivize early adopters: Free rides, discounts, Phased launch: Start in one neighborhood), MVP (Core matching (app to find bikes, unlock, return), Basic trust (bike quality, safety), Payment (ride payment, deposit), Basic tracking (bike location, availability)), Launch strategy (Geographic focus: Dense urban area, Category focus: Short trips, Supply-first: Deploy bikes first), Balancing Levers (Pricing: Dynamic pricing based on demand, Incentives: Rewards for returning bikes, Matching: Algorithm to optimize bike placement), Success Metrics (Match rate: Rides per bike per day, Liquidity: Bike utilization, GMV: Total ride value, Take rate: Platform commission). I'd prioritize solving the cold start problem and ensuring bike availability."

- **Q45 (Design restaurant reservations):** Emphasize reservations → "To design a restaurant reservations product, I'd: Sides (Supply: Restaurants (provide tables, want bookings), Demand: Diners (need reservations, want convenience)), Value Exchange (Supply provides tables, Demand pays (directly or through platform), Platform matches efficiently, creates value through convenience), Liquidity Risks (Cold start: Need restaurants and diners, No restaurants → no diners, No diners → no restaurants), Liquidity strategies (Seed supply: Onboard popular restaurants first, Seed demand: Launch in foodie neighborhoods, Incentivize early adopters: Restaurant discounts, diner rewards, Phased launch: Start in one city), MVP (Core matching (reservation booking, availability), Basic trust (restaurant ratings, cancellation policy), Payment (reservation fee or direct payment), Basic features (time slots, party size)), Launch strategy (Geographic focus: Foodie city, Category focus: Popular restaurants, Supply-first: Onboard restaurants first), Balancing Levers (Pricing: Reservation fees or free, Incentives: Rewards for diners, restaurants, Matching: Algorithm to optimize availability), Success Metrics (Match rate: Reservations per restaurant, Liquidity: Table utilization, GMV: Total reservation value, Take rate: Platform commission). I'd focus on getting restaurants onboard first, then attracting diners."

---

### BUCKET 2: Liquidity & Cold Start
**Questions:** ~5 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "How to get started?" or "Cold start problem" - same framework, with focus on liquidity
- **Approach:** Same marketplace framework, with focus on solving cold start and maintaining liquidity
- **Cold Start Strategy:** Identify which side to seed first (Supply-first vs demand-first), Seed strategy (Onboard early adopters, Provide incentives, Focus on quality), Launch strategy (Geographic focus, Category focus, Phased approach)
- **Liquidity Maintenance:** Monitor supply/demand balance (Metrics, Alerts, Adjustments), Balancing levers (Pricing, Incentives, Matching), Success metrics (Match rate, Liquidity, Utilization)

**Concrete Examples:**
- "Solve cold start: Identify which side to seed first (Supply-first for marketplaces with high supply value, Demand-first for marketplaces with high demand value), Seed strategy (Onboard early adopters, Provide incentives, Focus on quality), Launch strategy (Geographic focus, Category focus)"
- "Maintain liquidity: Monitor supply/demand balance, Use balancing levers (pricing, incentives, matching), Track success metrics"

**Representative Questions (Do 5 only):**
- Q264: Design a bike-sharing system for your city. (cold start angle)
- Q395: Design a platform that matches people wanting to learn skills with relevant mentors. (liquidity angle)
- Q403: Design a product for borrowing and lending. (cold start angle)
- Q45: As a PM at Meta, design a product for making restaurant reservations. (liquidity angle)
- Q83: As a product manager for Meta, design a product for volunteers. (cold start angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When focusing on liquidity and cold start, I use the same marketplace framework but emphasize solving the chicken-and-egg problem. I identify Sides to understand who needs to be on the platform. I define Value Exchange to understand what value each side gets. I assess Liquidity Risks: Cold start problem (No supply → no demand, No demand → no supply), and develop Liquidity strategies: Identify which side to seed first (Supply-first vs demand-first based on value), Seed strategy (Onboard early adopters, Provide incentives, Focus on quality), Launch strategy (Geographic focus, Category focus, Phased approach). I design MVP with liquidity in mind: Core matching that works even with limited supply/demand, Basic trust to build confidence, Payment/transaction to enable value exchange. I define Balancing Levers: Supply/demand balance (Pricing, Incentives, Matching algorithms), Success metrics (Match rate, Liquidity, Utilization). The key is solving the cold start problem and maintaining liquidity as you scale."

**How to Adapt This Narrative for Each Question:**

- **Q264 (Bike-sharing cold start):** Focus on cold start → "To solve the cold start problem for bike-sharing, I'd: Identify which side to seed first (Supply-first: Deploy bikes first, then attract riders - bikes are the constraint), Seed strategy (Onboard early adopters: Deploy bikes in high-traffic areas, Provide incentives: Free rides for first week, Focus on quality: Reliable bikes, good locations), Launch strategy (Geographic focus: Dense urban neighborhood, Category focus: Short trips, Phased approach: Start small, expand). I'd monitor liquidity: Track bike utilization, match rate, and adjust bike placement based on demand. The key is having bikes available when riders need them."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Marketplace Design** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Liquidity & Cold Start** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through marketplace design framework in 2 minutes (Sides → Value Exchange → Liquidity Risks → MVP → Balancing Levers)
- [ ] Identify both sides (supply and demand)
- [ ] Define value exchange (what each side gets)
- [ ] Assess liquidity risks (cold start problem)
- [ ] Design MVP (core matching, trust, payment)
- [ ] Define balancing levers (pricing, incentives, matching)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the marketplace design framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Sides → Value Exchange → Liquidity Risks → MVP → Balancing Levers framework**, not memorizing answers

**Remember:** P13D is about designing marketplaces. The framework: Sides → Value Exchange → Liquidity Risks → MVP → Balancing Levers. Key challenge: Solve the cold start problem and keep supply/demand balanced.
