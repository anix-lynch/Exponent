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
> "When I see a metric drop, I follow a structured approach. First, I clarify what exactly dropped - is it a count or rate? What's the scope and baseline? Second, I check if it's real - any tracking changes, ETL lag, or instrumentation issues? If it's real, I segment by platform, geography, channel, and surface to find the hot spot. Then I hypothesize top 3-5 causes ranked by likelihood and impact - product change, external event, performance issue, or supply-side change. I validate with quick checks - correlation in time, counter-metrics, funnel localization. Finally, I take action - rollback if severe, run experiment if unclear, or fix the specific segment."

**How to Adapt This Narrative for Each Question:**

- **Q22 (Amazon orders down 25%):** Start with urgency → "A 25% drop in orders is severe - I'd immediately check if it's a data bug first, then segment by platform and geography. If iOS+US is down 40% but web is flat, that's my hot spot. I'd check for app update, payment provider issues, or checkout crashes. If confirmed, I'd rollback or hotfix immediately."

- **Q1627 (10% conversion rate decrease):** Emphasize rate vs count → "First, I clarify if it's conversion count down or conversion rate down - big difference. If it's rate, I check if sessions went up (bad traffic diluting rate) or orders went down. Then I segment by channel, landing page, and device to find where the drop is. Common causes: new low-quality campaign, broken landing page, or pricing mismatch."

- **Q1700 (DAU drop 5% over week):** Focus on time dimension → "A 5% DAU drop over a week suggests gradual decline, not sudden incident. I'd first check for data issues - tracking changes, ETL lag, or sampling changes. Then segment by platform, geography, and cohort (new vs returning) to see if it's acquisition or retention. I'd check for product changes in that timeframe and external factors like seasonality or competition."

- **Q2468 (Dropbox uploads down 50%):** Emphasize severity → "A 50% drop is critical - this could be a major incident. I'd immediately check for data bug - did upload tracking break? ETL pipeline issue? If real, I'd segment by platform, geography, and user type to find hot spot. Likely causes: service outage, API change, or storage quota issue. I'd check error rates, latency, and support tickets to validate."

- **Q2681 (Messenger DAU significant drop):** Focus on communication app context → "For a communication app, DAU drop is critical - users might be switching platforms. I'd first verify it's not a data issue, then segment by platform, geography, and user cohort. I'd check for competitor launches, product changes that broke core functionality, or performance issues. I'd also check engagement metrics - are messages sent/received down? That tells me if it's acquisition or retention."

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
> "When I see a rate metric drop, I always check both numerator and denominator separately. A conversion rate drop could mean orders down (real problem) or sessions up (bad traffic diluting the rate). I segment by channel, landing page, and source to find where the denominator changed. Common causes: new low-quality campaign, bot traffic, or denominator definition change. I check counter-metrics - if sessions up but bounce rate also up, that's bad traffic. The fix depends on which one moved - if numerator down, fix conversion; if denominator up with bad quality, fix traffic source."

**How to Adapt This Narrative for Each Question:**

- **Q162 (CTR down 10%):** Focus on CTR specifically → "CTR is clicks/impressions. I'd check if clicks down (real problem) or impressions up (ranking/algorithm change). If impressions up but clicks flat, that's a ranking issue - content might be shown to wrong audience. I'd segment by content type, device, and user segment to find where impressions changed."

- **Q1019 (High Volume Low Success):** Emphasize the pattern → "High volume but low success suggests denominator up (more attempts) but numerator down (fewer successes). This could be bad traffic, quality degradation, or process issue. I'd segment by source, channel, and user type to find where volume increased but success rate dropped. Likely causes: new low-quality channel, bot traffic, or process change that increased attempts but not successes."

- **Q1743 (Metrics moved different directions):** Focus on interpretation → "When metrics move in opposite directions, I need to understand the relationship. If one rate up but another down, I check if they're related - maybe denominator changed. I'd create a framework: which metrics are leading vs lagging? Which are inputs vs outputs? Then I'd segment to see if different user segments are driving different trends. The key is understanding the causal relationship, not just looking at metrics in isolation."

- **Q2175 (Stories up, engagement down):** Emphasize the contradiction → "More Stories created but engagement down suggests denominator up (more content) but numerator down (less engagement per Story). I'd check if it's quality issue - are new Stories lower quality? Or quantity issue - too many Stories diluting engagement? I'd segment by creator type, Story type, and time period to see if new creators or new content formats are driving the volume but not engagement."

- **Q2159 (Usage divergence):** Focus on comparative analysis → "When usage diverges between surfaces, I segment each surface separately. DMs up but Search down suggests different user behaviors or product changes. I'd check: did we change one surface but not the other? Are different user segments using each? Is there cannibalization? I'd look at user overlap - are the same users using both, or different users? Then I'd check product changes, performance, and feature availability on each surface."

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
> "Before investigating any metric drop, I always check if it's a data bug first. I ask: did tracking code change? Event name change? ETL pipeline delayed? Sampling or filtering change? I check instrumentation logs, pipeline status, and compare to backup signals. If it's a data bug, I fix the measurement and re-read metrics - no point investigating business causes for a measurement issue. I also check for timing issues - delayed events, backfill, or timezone problems. The key is verifying the drop is real before spending time on root cause analysis."

**How to Adapt This Narrative for Each Question:**

- **Q778 (Events down 100%):** Emphasize complete drop-off → "A 100% drop is almost always a data bug, not a business issue. I'd immediately check: did event tracking break? Event name change? Pipeline completely down? I'd check instrumentation logs, pipeline status, and compare to server-side signals. If events completely missing, it's definitely a tracking or pipeline issue, not user behavior."

- **Q994 (Google searches down 35%):** Focus on incident response → "A 35% drop in searches is severe - could be data bug or real incident. I'd first check: did search tracking change? Pipeline issue? Then check if it's platform-specific (mobile vs desktop), geography-specific, or universal. If universal and sudden, likely data bug or major outage. I'd check error rates, latency, and compare to backup signals like server logs."

- **Q9 (Key metric declining - what first?):** Emphasize prioritization → "When a key metric declines, my first step is always data validation - is this real? I check instrumentation, pipeline, and compare to backup signals. Only after confirming it's real do I investigate business causes. I prioritize by: data check first (fastest to rule out), then segment to find hot spot (narrows scope), then hypothesize top causes (focuses investigation). I don't build anything until I know the root cause."

- **Q2429 (Questions before analysis):** Focus on preparation → "Before starting any analysis, I ask: is the data accurate? When was it last updated? Any known data issues? What's the definition of the metric? What's the baseline? Any recent changes to tracking or pipeline? These questions help me avoid wasting time on data bugs. I also ask: what's the business context? What changed recently? What's the expected vs actual?"

- **Q1368 (Qualitative vs quantitative contradiction):** Emphasize data validation → "When qualitative and quantitative data contradict, I first verify the quantitative data is accurate - could be a data bug making numbers wrong. I check instrumentation, sampling, and definitions. If quantitative is correct, then I investigate why qualitative differs - maybe different user segments, timing, or definition mismatch. The key is not assuming one is right - validate both, then reconcile."

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
> "When asked to increase a metric, I use the same framework as diagnosing a drop, but inverted. First, I clarify the metric definition and current baseline. Then I segment to find opportunities - which user segments, channels, or surfaces have the most headroom? I hypothesize growth levers: acquisition (get more users), activation (get them to first value), retention (get them to come back), or revenue (monetize better). I prioritize by impact x ease, then test the highest-leverage lever. I measure incrementally and scale what works."

**How to Adapt This Narrative for Each Question:**

- **Q40 (Increase Airbnb bookings):** Focus on marketplace context → "To increase bookings, I'd segment by user type (guests vs hosts), geography, and listing type. I'd check: is it acquisition (need more users), activation (users not booking first time), or retention (users not rebooking)? For a marketplace, I'd also check supply-side - enough listings? Quality listings? Then I'd prioritize levers: if activation low, improve search/discovery; if retention low, improve experience; if supply constrained, grow host base."

- **Q1027 (Improve Facebook DAU):** Emphasize engagement metric → "DAU is about daily engagement. I'd segment by user cohort (new vs returning), platform, and geography to find where engagement is lowest. I'd check: is it acquisition (not enough new users), activation (new users not coming back), or retention (existing users churning)? I'd hypothesize levers: better content feed, notifications, or features that drive daily habit. I'd test with experiments and measure incremental DAU lift."

- **Q1242 (Analyze engagement decline):** Combine drop + improvement → "To analyze engagement decline, I'd first check if it's a data bug, then segment to find where it's dropping. But the goal is improvement, so I'd also identify segments with highest engagement to learn from. I'd compare high vs low engagement segments to find what drives engagement, then apply those insights to declining segments."

- **Q161 (Increase engagement 100x):** Focus on magnitude → "A 100x increase requires fundamental changes, not incremental. I'd segment to find the highest-engagement user segment, understand what drives their engagement, then scale those drivers. I'd also look for new engagement vectors - maybe a feature that creates new engagement type. The key is not just optimizing existing engagement, but creating new engagement loops that compound."

- **Q2655 (Increase Amazon NPS):** Focus on satisfaction metric → "NPS is about customer satisfaction. I'd segment by customer type, purchase category, and experience type to find where satisfaction is lowest. I'd check: is it product quality, delivery, customer service, or price? I'd identify pain points through support tickets and reviews, then prioritize fixes by impact on NPS. I'd also identify promoters to understand what drives satisfaction and amplify those."

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
> "When investigating why something happened, I use the same segmentation and hypothesis framework, but I generate multiple hypotheses and systematically validate each. I segment to find patterns - when did it start? Which segments affected? Then I generate 3-5 hypotheses ranked by likelihood and impact. I validate each with quick data checks - correlation in time, counter-metrics, A/B comparisons. I don't stop at correlation - I look for causal evidence. The root cause is usually the hypothesis that explains the most variance and has supporting evidence."

**How to Adapt This Narrative for Each Question:**

- **Q6 (Competitor gaining market share):** Focus on competitive analysis → "To investigate why a competitor is gaining share, I'd segment our metrics by user segment, geography, and product area to see where we're losing. I'd check: did they launch a new feature? Better pricing? Marketing campaign? I'd also check our own metrics - are we losing users or are they growing faster? I'd validate by looking at user feedback, support tickets, and competitive intelligence to understand what's driving their growth."

- **Q2542 (Orders down 30%):** Emphasize systematic investigation → "A 30% drop needs systematic investigation. I'd first check data quality, then segment by geography, platform, and user type to find the hot spot. I'd generate hypotheses: product change, external event (holiday, competitor), performance issue, or supply constraint. I'd validate by checking correlation in time with product releases, checking counter-metrics (traffic, engagement), and comparing affected vs unaffected segments."

- **Q2549 (Signups increased 15%):** Focus on positive change → "When investigating an increase, I use the same framework but look for what changed positively. I'd segment to see which channels, geographies, or user types drove the increase. I'd check: marketing campaign? Product change? External event? I'd validate by checking correlation in time, looking at acquisition channels, and comparing to baseline. Understanding what drove growth helps replicate it."

- **Q2619 (Gmail search slower):** Focus on performance metric → "Performance issues need technical investigation. I'd segment by query type, user location, and time to see patterns. I'd check: is it universal or specific queries? All users or specific geographies? I'd generate hypotheses: infrastructure issue, algorithm change, data volume increase, or feature change. I'd validate by checking latency metrics, error rates, and comparing to Google search infrastructure."

- **Q2622 (Venmo bank account decrease):** Emphasize user behavior → "A decrease in users adding bank accounts suggests friction or trust issue. I'd segment by user type (new vs existing), device, and geography to find patterns. I'd check: did we change the flow? Add friction? Security concern? I'd generate hypotheses: UX change made it harder, security concern, or alternative payment method preference. I'd validate by checking funnel drop-off, support tickets, and user feedback."

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

