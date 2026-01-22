# Executive Study Plan: P1 - Metric Drop Diagnosis
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** 108 questions → 5 concept buckets → 3-5 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY P1 (METRIC DROP) QUESTIONS

**Even when "metric drop" isn't mentioned, look for these keywords/phrases:**

### Explicit Drop Keywords:
- "down", "decline", "decrease", "drop", "dropped", "falling"
- "lower than", "less than", "decreased by X%", "down X%"

### Implicit Drop Indicators:
- **Percentage changes:** "X is down 25%", "declined by 10%", "decreased from A to B"
- **Comparison questions:** "why is X lower?", "what happened to Y?", "X is less than before"
- **Investigation questions:** "how would you investigate X?", "what caused Y to drop?"
- **Incident response:** "sudden drop", "overnight decline", "unexpected decrease"
- **Growth questions (inverted):** "how to increase X?" → Same framework, inverted

### P1 vs P3 Distinction:
- **P1 (Metric Drop):** "Orders down 25%" → Focus: WHERE is drop coming from? (segment by platform/geo/channel)
- **P3 (Funnel):** "55% drop at checkout step" → Focus: WHY do users drop at this STEP? (identify friction)

### P1 vs P4 Distinction:
- **P1 (Metric Drop):** "DAU dropped 15% this week" → Single time point, overall metric
- **P4 (Cohort):** "February cohort has lower retention" → Multiple cohorts over time

### Red Flags (NOT P1):
- "Users drop at checkout step" → P3 (Funnel)
- "Cohort retention declined" → P4 (Cohort/Retention)
- "How to define success?" → P2 (NSM + KPI Ladder)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 3-5 High-Impact Buckets (Pick Based on Role)

**For Business Leader / GM:**
1. ✅ **Classic Metric Drop** (HIGHEST PRIORITY)
2. ✅ **Rate vs Denominator Trap** (HIGH PRIORITY)
3. ✅ **Data Bug / Instrumentation** (MEDIUM-HIGH)
4. ⚠️ **Growth/Improvement Questions** (MEDIUM - same framework, inverted)
5. ❌ **Behavioral/Story Questions** (LOW - skip for now)

**For Data Analyst:**
1. ✅ **Classic Metric Drop** (HIGHEST)
2. ✅ **Data Bug / Instrumentation** (HIGH)
3. ✅ **Rate vs Denominator Trap** (MEDIUM-HIGH)
4. ⚠️ **Root Cause Analysis** (MEDIUM)
5. ❌ **Behavioral/Story Questions** (LOW)

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Classic Metric Drop ("X is down Y%")
**Questions:** ~40 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** A metric (orders, DAU, conversion, engagement) drops suddenly
- **Framework:** Clarify → Data Check → Segment → Hypothesize → Validate → Action
- **Key Insight:** Always segment first to find the "hot spot" - where is the drop coming from?
- **Common Causes:** Product change, external event, performance issue, supply-side change

**Concrete Examples:**
- "Amazon orders down 25% - segment by platform/geo, find iOS+US is -40%, check for app update or payment issue"
- "DAU dropped 15% - first check if it's a data bug (tracking change?), then segment by platform/cohort to find root cause"
- "Conversion down 10% - check if it's real (data bug?), segment by channel/surface, hypothesize product change or performance"

**Representative Questions (Do 5 only):**
- Q22: Amazon orders are down 25% - what do you do?
- Q1627: If you noticed a 10% decrease in an app's conversion rate, what steps would you take to investigate and resolve the issue?
- Q1700: Instagram sees a 5% decrease in Daily Active Users (DAU) over a week. How do you determine the root cause?
- Q2468: What would you do if Dropbox uploads were down 50%?
- Q2681: You are the PM of Messenger and notice a significant drop in DAU. How would you investigate the cause?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Clarify → Data Check → Segment → Hypothesize → Validate → Action`

**Memorizable Answer:**

When I see a metric drop, I follow a structured approach.

**1️⃣ Clarify** → What exactly dropped? Is it a count or rate? What's the scope and baseline?

**2️⃣ Data Check** → Is this real? Any tracking changes, ETL lag, or instrumentation issues?

**3️⃣ Segment** → If it's real, I segment by platform, geography, channel, and surface to find the hot spot.

**4️⃣ Hypothesize** → Top 3-5 causes ranked by likelihood and impact: product change, external event, performance issue, or supply-side change.

**5️⃣ Validate** → Quick checks: correlation in time, counter-metrics, funnel localization.

**6️⃣ Action** → Rollback if severe, run experiment if unclear, or fix the specific segment.

**Key Principle:** Always segment first to find WHERE the drop is coming from.

---

**How to Adapt This Narrative for Each Question:**

- **Q22 (Amazon orders down 25%):** Start with urgency
  - "A 25% drop is severe → immediately check data bug first"
  - "Segment by platform/geo → if iOS+US down 40% but web flat, that's the hot spot"
  - "Check: app update, payment issues, checkout crashes"
  - "If confirmed → rollback or hotfix immediately"

- **Q1627 (10% conversion rate decrease):** Emphasize rate vs count
  - "First clarify: conversion count down OR rate down? Big difference"
  - "If rate: check if sessions up (bad traffic) or orders down (real problem)"
  - "Segment by channel, landing page, device to find drop location"
  - "Common causes: low-quality campaign, broken landing page, pricing mismatch"

- **Q1700 (DAU drop 5% over week):** Focus on time dimension
  - "5% over week = gradual decline, not sudden incident"
  - "Check data issues first: tracking changes, ETL lag, sampling changes"
  - "Segment by platform, geo, cohort (new vs returning) → acquisition or retention?"
  - "Check product changes in timeframe + external factors (seasonality, competition)"

- **Q2468 (Dropbox uploads down 50%):** Emphasize severity
  - "50% drop = critical → could be major incident"
  - "Immediately check data bug: upload tracking break? ETL pipeline issue?"
  - "If real → segment by platform, geo, user type to find hot spot"
  - "Likely causes: service outage, API change, storage quota"
  - "Validate: error rates, latency, support tickets"

- **Q2681 (Messenger DAU significant drop):** Focus on communication app context
  - "DAU drop in comm app = critical → users might be switching platforms"
  - "Verify not data issue → segment by platform, geo, user cohort"
  - "Check: competitor launches, product changes breaking core functionality, performance issues"
  - "Also check engagement: messages sent/received down? → tells if acquisition or retention"

---

### BUCKET 2: Rate vs Denominator Trap
**Questions:** ~15 | **Priority:** 🟢 GREEN (High-yield trap to avoid)

**Board Slide Bullets:**
- **What:** Conversion rate drops, but is it orders down OR sessions up (bad traffic)?
- **Key Insight:** Rate = numerator/denominator - always check both!
- **Common Trap:** Blaming conversion when denominator changed (new low-quality channel, bot traffic)
- **Fix:** Check numerator and denominator separately, segment by channel/source

**Concrete Examples:**
- "Conversion rate dropped 10% - check if orders down (real problem) or sessions up (bad traffic diluting rate)"
- "Email open rate down - check if opens down (real) or emails sent up (deliverability issue)"
- "CTR down - check if clicks down (real) or impressions up (ranking change)"

**Representative Questions (Do 5 only):**
- Q162: Click-through rate on Netflix is down by 10%. What would you do?
- Q1019: High Volume Low Success.
- Q1743: Metrics moved in different directions, how do you interpret the results and decide next steps?
- Q2175: Users are creating more Instagram Stories, but engagement is down. What metrics would you track to improve this?
- Q2159: The usage of Meta AI within Instagram DMs is up while the usage of Meta AI within the Search Bar of IG Discover page is down. How would you investigate?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Check Numerator & Denominator Separately → Segment → Identify Cause → Fix`

**Memorizable Answer:**

When I see a rate metric drop, I always check both numerator and denominator separately.

**1️⃣ Check Both** → Rate = numerator/denominator. A drop could mean numerator down (real problem) OR denominator up (bad traffic diluting rate).

**2️⃣ Segment** → Segment by channel, landing page, and source to find where the denominator changed.

**3️⃣ Identify Cause** → Common causes: new low-quality campaign, bot traffic, or denominator definition change.

**4️⃣ Validate** → Check counter-metrics. If sessions up but bounce rate also up → that's bad traffic.

**5️⃣ Fix** → If numerator down → fix conversion. If denominator up with bad quality → fix traffic source.

**Key Principle:** Always check both numerator and denominator separately - don't assume it's the numerator.

---

**How to Adapt This Narrative for Each Question:**

- **Q162 (CTR down 10%):** Focus on CTR specifically
  - "CTR = clicks/impressions"
  - "Check: clicks down (real problem) OR impressions up (ranking/algorithm change)?"
  - "If impressions up but clicks flat → ranking issue, content shown to wrong audience"
  - "Segment by content type, device, user segment to find where impressions changed"

- **Q1019 (High Volume Low Success):** Emphasize the pattern
  - "High volume + low success = denominator up (more attempts) but numerator down (fewer successes)"
  - "Could be: bad traffic, quality degradation, or process issue"
  - "Segment by source, channel, user type → where did volume increase but success drop?"
  - "Likely causes: new low-quality channel, bot traffic, process change increasing attempts but not successes"

- **Q1743 (Metrics moved different directions):** Focus on interpretation
  - "When metrics move opposite directions → understand the relationship"
  - "Check if they're related → maybe denominator changed"
  - "Framework: which metrics are leading vs lagging? Inputs vs outputs?"
  - "Segment to see if different user segments driving different trends"
  - "Key: understand causal relationship, not just look at metrics in isolation"

- **Q2175 (Stories up, engagement down):** Emphasize the contradiction
  - "More Stories but engagement down = denominator up (more content) but numerator down (less engagement per Story)"
  - "Check: quality issue (new Stories lower quality?) OR quantity issue (too many diluting engagement?)"
  - "Segment by creator type, Story type, time period"
  - "See if new creators or new formats driving volume but not engagement"

- **Q2159 (Usage divergence):** Focus on comparative analysis
  - "Usage diverges between surfaces → segment each separately"
  - "DMs up but Search down → different behaviors or product changes"
  - "Check: did we change one surface? Different user segments? Cannibalization?"
  - "Look at user overlap → same users or different? Then check product changes, performance, feature availability"

---

### BUCKET 3: Data Bug / Instrumentation
**Questions:** ~10 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** Drop might not be real - could be measurement issue
- **Key Insight:** Always check data quality FIRST before investigating business causes
- **Common Causes:** Tracking code change, event name change, ETL lag, pipeline issue, sampling change
- **Fix:** Check instrumentation, pipeline, use backup signals, fix measurement

**Concrete Examples:**
- "DAU dropped 15% - first check if app_open event missing from Android build, or ETL pipeline delayed"
- "Orders down - check if order-completed event renamed or payment tracking broke"
- "Conversion down - check if session tracking changed or bot traffic filtered differently"

**Representative Questions (Do 5 only):**
- Q778: Events created are down 100% on Facebook - why?
- Q994: Google searches are down 35%. What happened?
- Q9: A key metric is declining—what would you investigate first and how would you prioritize what to build?
- Q2429: What questions would you ask before starting an analysis?
- Q1368: How would you handle a situation where qualitative insights contradict quantitative data?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Check Data Quality First → Verify Real → Then Investigate Business Causes`

**Memorizable Answer:**

Before investigating any metric drop, I always check if it's a data bug first.

**1️⃣ Ask Data Questions** → Did tracking code change? Event name change? ETL pipeline delayed? Sampling or filtering change?

**2️⃣ Check Signals** → Check instrumentation logs, pipeline status, compare to backup signals.

**3️⃣ Verify Real** → If it's a data bug, fix measurement and re-read metrics. No point investigating business causes for a measurement issue.

**4️⃣ Check Timing** → Delayed events, backfill, or timezone problems.

**Key Principle:** Verify the drop is real before spending time on root cause analysis.

---

**How to Adapt This Narrative for Each Question:**

- **Q778 (Events down 100%):** Emphasize complete drop-off
  - "100% drop = almost always data bug, not business issue"
  - "Immediately check: event tracking break? Event name change? Pipeline down?"
  - "Check instrumentation logs, pipeline status, compare to server-side signals"
  - "If events completely missing → definitely tracking/pipeline issue, not user behavior"

- **Q994 (Google searches down 35%):** Focus on incident response
  - "35% drop = severe → could be data bug OR real incident"
  - "First check: search tracking change? Pipeline issue?"
  - "Then check: platform-specific (mobile vs desktop)? Geo-specific? Universal?"
  - "If universal + sudden → likely data bug or major outage"
  - "Validate: error rates, latency, compare to backup signals (server logs)"

- **Q9 (Key metric declining - what first?):** Emphasize prioritization
  - "First step = data validation → is this real?"
  - "Check instrumentation, pipeline, compare to backup signals"
  - "Only after confirming real → investigate business causes"
  - "Prioritize: data check first (fastest), then segment (narrows scope), then hypothesize (focuses investigation)"
  - "Don't build anything until root cause known"

- **Q2429 (Questions before analysis):** Focus on preparation
  - "Before analysis, ask: data accurate? Last updated? Known issues? Metric definition? Baseline?"
  - "Recent changes to tracking or pipeline?"
  - "Also ask: business context? What changed recently? Expected vs actual?"
  - "These questions avoid wasting time on data bugs"

- **Q1368 (Qualitative vs quantitative contradiction):** Emphasize data validation
  - "When they contradict → first verify quantitative data accurate"
  - "Could be data bug making numbers wrong"
  - "Check instrumentation, sampling, definitions"
  - "If quantitative correct → investigate why qualitative differs (different segments, timing, definition mismatch)"
  - "Key: don't assume one is right → validate both, then reconcile"

---

### BUCKET 4: Growth/Improvement Questions ("How to increase X?")
**Questions:** ~25 | **Priority:** 🟡 YELLOW (Same framework, inverted)

**Board Slide Bullets:**
- **What:** "How would you increase bookings/engagement/DAU?" - inverse of drop
- **Key Insight:** Same framework, but start from baseline and identify levers
- **Approach:** Clarify metric → Segment to find opportunities → Hypothesize growth levers → Test → Scale
- **Common Levers:** Acquisition (new users), Activation (first value), Retention (come back), Revenue (monetize)

**Concrete Examples:**
- "How to increase bookings? Segment by user type, find new users convert low, focus on activation"
- "How to increase DAU? Segment by cohort, find D7 retention low, focus on habit formation"
- "How to increase engagement? Segment by content type, find video underperforms, improve recommendations"

**Representative Questions (Do 5 only):**
- Q40: As a PM at Airbnb, how would you increase bookings?
- Q1027: How can you improve Facebook's DAU?
- Q1242: How would you analyze why user engagement is declining?
- Q161: Choosing a mobile app, how would you increase user engagement by 100x?
- Q2655: You are a PM at Amazon and want to increase the NPS. What would you do?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Clarify → Segment → Hypothesize Levers → Prioritize → Test → Scale`

**Memorizable Answer:**

When asked to increase a metric, I use the same framework as diagnosing a drop, but inverted.

**1️⃣ Clarify** → Metric definition and current baseline.

**2️⃣ Segment** → Find opportunities. Which user segments, channels, or surfaces have the most headroom?

**3️⃣ Hypothesize Levers** → Acquisition (get more users), Activation (get them to first value), Retention (get them to come back), or Revenue (monetize better).

**4️⃣ Prioritize** → By impact × ease, then test the highest-leverage lever.

**5️⃣ Measure & Scale** → Measure incrementally and scale what works.

**Key Principle:** Same systematic approach, but focus on opportunities instead of problems.

---

**How to Adapt This Narrative for Each Question:**

- **Q40 (Increase Airbnb bookings):** Focus on marketplace context
  - "Segment by user type (guests vs hosts), geo, listing type"
  - "Check: acquisition (need more users)? Activation (users not booking first time)? Retention (not rebooking)?"
  - "For marketplace → also check supply-side: enough listings? Quality listings?"
  - "Prioritize: if activation low → improve search/discovery; if retention low → improve experience; if supply constrained → grow host base"

- **Q1027 (Improve Facebook DAU):** Emphasize engagement metric
  - "DAU = daily engagement"
  - "Segment by cohort (new vs returning), platform, geo → where is engagement lowest?"
  - "Check: acquisition (not enough new users)? Activation (new users not coming back)? Retention (existing churning)?"
  - "Hypothesize levers: better content feed, notifications, features driving daily habit"
  - "Test with experiments, measure incremental DAU lift"

- **Q1242 (Analyze engagement decline):** Combine drop + improvement
  - "First check data bug, then segment to find where dropping"
  - "But goal is improvement → also identify segments with highest engagement to learn from"
  - "Compare high vs low engagement segments → find what drives engagement"
  - "Apply insights to declining segments"

- **Q161 (Increase engagement 100x):** Focus on magnitude
  - "100x = fundamental changes, not incremental"
  - "Segment to find highest-engagement segment → understand what drives their engagement"
  - "Scale those drivers"
  - "Also look for new engagement vectors → feature creating new engagement type"
  - "Key: not just optimizing existing, but creating new engagement loops that compound"

- **Q2655 (Increase Amazon NPS):** Focus on satisfaction metric
  - "NPS = customer satisfaction"
  - "Segment by customer type, purchase category, experience type → where is satisfaction lowest?"
  - "Check: product quality? Delivery? Customer service? Price?"
  - "Identify pain points via support tickets and reviews → prioritize fixes by NPS impact"
  - "Also identify promoters → understand what drives satisfaction, amplify those"

---

### BUCKET 5: Root Cause Analysis ("Why did X happen?")
**Questions:** ~18 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Why did X happen?" or "What caused Y?" - deeper investigation
- **Key Insight:** Same framework, but emphasize hypothesis generation and validation
- **Approach:** Clarify → Segment → Generate multiple hypotheses → Validate with data → Identify root cause
- **Common Causes:** Product change, external event, performance, supply-side, data quality

**Representative Questions (Do 5 only):**
- Q6: A competitor is gaining market share. How would you investigate why?
- Q2542: Why are online orders on The New Yorker down 30%?
- Q2549: Why did Codecademy's signups increase by 15%?
- Q2619: Why is Gmail search slower than Google search?
- Q2622: Why might Venmo be seeing a decrease in users adding their bank accounts?

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Segment → Generate Multiple Hypotheses → Validate Each → Identify Root Cause`

**Memorizable Answer:**

When investigating why something happened, I use the same segmentation and hypothesis framework, but generate multiple hypotheses and systematically validate each.

**1️⃣ Segment** → Find patterns. When did it start? Which segments affected?

**2️⃣ Generate Hypotheses** → 3-5 hypotheses ranked by likelihood and impact.

**3️⃣ Validate Each** → Quick data checks: correlation in time, counter-metrics, A/B comparisons.

**4️⃣ Find Root Cause** → Don't stop at correlation - look for causal evidence. Root cause is usually the hypothesis that explains the most variance and has supporting evidence.

**Key Principle:** Generate multiple hypotheses, validate systematically, find the one with strongest evidence.

---

**How to Adapt This Narrative for Each Question:**

- **Q6 (Competitor gaining market share):** Focus on competitive analysis
  - "Segment our metrics by user segment, geo, product area → where are we losing?"
  - "Check: did they launch new feature? Better pricing? Marketing campaign?"
  - "Also check our metrics → are we losing users or are they growing faster?"
  - "Validate: user feedback, support tickets, competitive intelligence → what's driving their growth?"

- **Q2542 (Orders down 30%):** Emphasize systematic investigation
  - "30% drop = systematic investigation needed"
  - "First check data quality → then segment by geo, platform, user type to find hot spot"
  - "Generate hypotheses: product change, external event (holiday, competitor), performance issue, supply constraint"
  - "Validate: correlation in time with product releases, counter-metrics (traffic, engagement), compare affected vs unaffected segments"

- **Q2549 (Signups increased 15%):** Focus on positive change
  - "Investigating increase → same framework but look for what changed positively"
  - "Segment to see which channels, geos, user types drove increase"
  - "Check: marketing campaign? Product change? External event?"
  - "Validate: correlation in time, acquisition channels, compare to baseline"
  - "Understanding what drove growth helps replicate it"

- **Q2619 (Gmail search slower):** Focus on performance metric
  - "Performance issues = technical investigation"
  - "Segment by query type, user location, time → see patterns"
  - "Check: universal or specific queries? All users or specific geos?"
  - "Generate hypotheses: infrastructure issue, algorithm change, data volume increase, feature change"
  - "Validate: latency metrics, error rates, compare to Google search infrastructure"

- **Q2622 (Venmo bank account decrease):** Emphasize user behavior
  - "Decrease in adding bank accounts = friction or trust issue"
  - "Segment by user type (new vs existing), device, geo → find patterns"
  - "Check: did we change flow? Add friction? Security concern?"
  - "Generate hypotheses: UX change made it harder, security concern, alternative payment preference"
  - "Validate: funnel drop-off, support tickets, user feedback"

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Classic Metric Drop** → Study Bucket 1, practice 5 questions
2. **Rate vs Denominator Trap** → Study Bucket 2, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
3. **Data Bug / Instrumentation** → Study Bucket 3, practice 5 questions
4. **Growth/Improvement Questions** → Study Bucket 4, practice 5 questions
5. **Root Cause Analysis** → Study Bucket 5, practice 5 questions

---

## 🔍 HOW TO IDENTIFY P1 (METRIC DROP) QUESTIONS

**Even when "metric drop" isn't mentioned, look for these keywords/phrases:**

### Explicit Drop Keywords:
- "down", "decline", "decrease", "drop", "dropped", "falling"
- "lower than", "less than", "decreased by X%", "down X%"

### Implicit Drop Indicators:
- **Percentage changes:** "X is down 25%", "declined by 10%", "decreased from A to B"
- **Comparison questions:** "why is X lower?", "what happened to Y?", "X is less than before"
- **Investigation questions:** "how would you investigate X?", "what caused Y to drop?"
- **Incident response:** "sudden drop", "overnight decline", "unexpected decrease"
- **Growth questions (inverted):** "how to increase X?" → Same framework, inverted

### P1 vs P3 Distinction:
- **P1 (Metric Drop):** "Orders down 25%" → Focus: WHERE is drop coming from? (segment by platform/geo/channel)
- **P3 (Funnel):** "55% drop at checkout step" → Focus: WHY do users drop at this STEP? (identify friction)

### P1 vs P4 Distinction:
- **P1 (Metric Drop):** "DAU dropped 15% this week" → Single time point, overall metric
- **P4 (Cohort):** "February cohort has lower retention" → Multiple cohorts over time

### Red Flags (NOT P1):
- "Users drop at checkout step" → P3 (Funnel)
- "Cohort retention declined" → P4 (Cohort/Retention)
- "How to define success?" → P2 (NSM + KPI Ladder)

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through "X is down Y%" framework in 2 minutes (Clarify → Data Check → Segment → Hypothesize → Validate → Action)
- [ ] Explain rate vs denominator trap with concrete example
- [ ] List 3 data bug checks before investigating business causes
- [ ] Adapt the framework to "how to increase X" questions
- [ ] Generate 3-5 hypotheses for any metric change and rank by likelihood x impact

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the P1 framework to a non-technical person in 2 minutes
- You have 5 reusable narratives (one per bucket) that you can adapt
- You've practiced 15-25 representative questions total (5 per bucket, not all 108!)
- You focus on **structure, segmentation, and systematic investigation**, not memorizing answers

**Remember:** P1 is about systematic thinking, not domain expertise. The framework works for any metric drop, regardless of industry.

