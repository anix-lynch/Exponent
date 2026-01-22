# Executive Study Plan: L12 - Metrics Interpretation
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~5 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L12 (METRICS INTERPRETATION) QUESTIONS

**Even when "metrics interpretation" isn't mentioned, look for these keywords/phrases:**

### Explicit Metrics Interpretation Keywords:
- "metric interpretation", "what does this metric mean", "is this metric good", "metric moved"
- "proxy", "vanity metric", "gaming", "Simpson's paradox", "metric validity"
- "should we care", "is this good", "what does this tell us"

### Implicit L12 Indicators:
- **Interpretation questions:** "Signup conversion increased 10%. Is that good?", "What does this metric mean?", "Should we care about this change?"
- **Proxy questions:** "Is this a good proxy?", "Does this metric mean what we think?", "Proxy validity"
- **Gaming questions:** "Can this be gamed?", "Is this being manipulated?", "Metric gaming"

### L12 vs P1 Distinction:
- **L12 (Metrics Interpretation):** "Is this metric good?" → Focus: Does metric mean what we think? Can it be gamed? Should we care?
- **P1 (Metric Drop):** "Orders down 25%" → Focus: WHERE is drop coming from? (Segment to find hot spot)

### L12 vs L1 Distinction:
- **L12 (Metrics Interpretation):** "Is this metric good?" → Focus: Proxy validity, gaming risk, interpretation
- **L1 (Data Trust):** "Debug a metric that was off" → Focus: Is data trustworthy? (Source, freshness, completeness)

### Red Flags (NOT L12):
- "Orders down 25%" → P1 (Metric Drop)
- "Debug a metric that was off" → L1 (Data Trust)
- "How do you define success?" → P2 (NSM + KPI Ladder)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Metrics Interpretation Framework** (HIGHEST PRIORITY)
2. ✅ **Metric Traps & Gaming** (HIGH PRIORITY)

**For Data Engineer:**
1. ✅ **Metrics Interpretation Framework** (HIGHEST) - Understand metric validity
2. ⚠️ **Metric Traps & Gaming** (MEDIUM) - Less relevant for DE

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Metrics Interpretation Framework
**Questions:** ~3 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Signup conversion increased 10%. Is that good?" or "What does this metric mean?" - core metrics interpretation framework
- **Framework:** Metric Moved → Proxy Validity → Gaming Risk → Context Checks → Decide
- **Metric Moved:** What exactly changed? (Direction: up/down/flat, Magnitude: small blip vs step-change, Scope: which segment, surface, cohort, Time: one day spike vs sustained trend, Aggregation level: overall vs segment-level - check for Simpson's paradox), Rule: Never react to a single datapoint
- **Proxy Validity:** Does this metric mean what we think? (Is it a proxy or the real goal?, How tightly correlated to value?, Leading vs lagging?, Any known blind spots?), Example: CTR ↑ but satisfaction ↓ → weak proxy
- **Gaming & Incentives:** Can it be manipulated? (By users? Spam, bots, churn masking, By teams? Optimize metric, hurt product, By design? Dark patterns, forced clicks, By reporting? Definition drift), Rule: If it's tied to goals/bonuses, it WILL be gamed
- **Context Checks:** Is this causal? (Seasonality?, Launches/experiments?, External events?, Data pipeline issues?, Aggregation bias? Simpson's paradox?, Correlation vs causation)
- **Decide:** Now what? (Ignore → noise or bad proxy, Monitor → unclear, need more data, Investigate → signal but ambiguous, Act → strong signal + aligned proxy), Output: "We believe X changed because Y, so we will Z."

**Concrete Examples:**
- "Signup conversion ↑ 10%: Metric (Direction: up, Magnitude: 10%, Scope: all users, Time: sustained), Proxy (Does signup → activation? Weak link), Gaming (Forced signup wall introduced), Context (Marketing campaign changed traffic mix), Decision (Investigate activation + retention before celebrating)"
- "Metrics interpretation: Check what moved, validate proxy, assess gaming risk, check context, decide"

**Representative Questions (Do 5 only):**
- Q144: Can a university have a lower overall acceptance rate for female-identifying students, even if every department admits them at a higher rate than others? (Simpson's paradox/metric interpretation angle)
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (metric interpretation angle)
- Q117: As the PM for Lyft, what dashboard would you build to track the health of the app? (metric interpretation angle)
- Q183: Debug a metric that was off by x percentage. (metric interpretation angle)
- Q790: Explain data drifting. (metric interpretation angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When interpreting metrics, I use Metric Moved → Proxy Validity → Gaming Risk → Context Checks → Decide. First, I check Metric Moved: What exactly changed? Direction (Up/down/flat - which direction did the metric move?), Magnitude (Small blip vs step-change - how significant is the change?), Scope (Which segment, surface, cohort - where is the change happening?), Time (One day spike vs sustained trend - is this temporary or ongoing?), Aggregation level (Overall metric vs segment-level metrics - check for Simpson's paradox). Rule: Never react to a single datapoint. Second, I validate Proxy Validity: Does this metric mean what we think? Is it a proxy or the real goal? (Is this metric a stand-in for something else, or the actual outcome?), How tightly correlated to value? (Does this metric actually predict business value or user satisfaction?), Leading vs lagging? (Is this a leading indicator - predicts future, or lagging indicator - reflects past?), Any known blind spots? (Are there scenarios where this metric is misleading or incomplete?). Example: CTR ↑ but satisfaction ↓ → weak proxy. Third, I assess Gaming & Incentives: Can it be manipulated? By users? (Spam, bots, churn masking - are users gaming the system?), By teams? (Optimize metric, hurt product - are teams optimizing for the metric at the expense of real value?), By design? (Dark patterns, forced clicks - is the product design encouraging manipulation?), By reporting? (Definition drift - are we changing how we measure this over time?). Rule: If it's tied to goals/bonuses, it WILL be gamed. Fourth, I check Context: Is this causal? Seasonality? (Is this a seasonal pattern we've seen before?), Launches/experiments? (Did we recently launch a feature or run an experiment?), External events? (Are there external factors - news, holidays, market changes - affecting this?), Data pipeline issues? (Could this be a data quality problem or reporting error?), Aggregation bias? (Is the overall metric hiding important segment-level differences - Simpson's paradox?), Correlation vs causation (Is this change actually caused by what we think, or just correlated?). Finally, I Decide: Now what? Ignore (Noise or bad proxy - not worth acting on), Monitor (Unclear, need more data - watch and wait), Investigate (Signal but ambiguous - dig deeper), Act (Strong signal + aligned proxy - take action). Output: 'We believe X changed because Y, so we will Z.' The key principle: A metric moving is not the same as progress. Proxies decay over time. If a metric becomes a target, it stops being a metric. Context beats dashboards."

**How to Adapt This Narrative for Each Question:**

- **Q144 (Simpson's paradox):** Focus on aggregation bias → "To explain Simpson's paradox in university acceptance rates, I'd: Metric Moved (Overall acceptance rate: Lower for female-identifying students, Department-level: Higher acceptance rate for female-identifying students in every department, Aggregation level: Overall metric vs segment-level metrics - this is Simpson's paradox, Direction: Down at overall level, up at department level, Magnitude: Significant difference, Scope: Overall vs department-level, Time: Sustained pattern), Proxy Validity (Is overall acceptance rate a good proxy? No - it's misleading when departments have different application rates, How correlated to fairness? Weak - overall rate doesn't reflect department-level fairness, Blind spots: Overall rate hides department-level differences), Gaming Risk (Can it be gamed? Yes - by changing department application rates, By design: Department selection could be manipulated), Context Checks (Is this causal? No - it's an aggregation artifact, Seasonality: No, Launches: No, External events: No, Data pipeline: No, Aggregation bias: Yes - this is Simpson's paradox - overall metric is misleading when departments have different application rates), Decide (Investigate: Need to look at department-level rates, not overall, Act: Use department-level rates for fairness assessment, not overall rate). I'd explain: Simpson's paradox occurs when overall metric shows opposite trend from segment-level metrics. Here, overall acceptance rate is lower for female-identifying students, but every department accepts them at higher rates. This happens because departments with lower acceptance rates (harder to get into) receive more applications from female-identifying students. The overall rate is misleading - we should look at department-level rates for fairness assessment."

- **Q110 (Gas station surge interpretation):** Emphasize metric interpretation → "To interpret the 4x customer surge, I'd: Metric Moved (Direction: Up - 4x increase, Magnitude: Large - 4x is significant, Scope: All customers, peak times, Time: Sudden surge - not sustained, Aggregation level: Overall vs time-based), Proxy Validity (Is customer count a good proxy? Yes - directly measures demand, How correlated to business value? High - more customers = more revenue, Leading vs lagging: Leading - predicts revenue, Blind spots: Doesn't show customer satisfaction, wait times), Gaming Risk (Can it be gamed? No - real customers, By teams: No, By design: No, By reporting: No), Context Checks (Is this causal? Need to investigate - could be: Event nearby, promotion, competitor issue, seasonality, external event, Data pipeline: Check if data is accurate), Decide (Investigate: Need to understand cause, Act: If real surge, need to handle capacity, If data issue, fix data). I'd interpret: 4x surge is significant - need to investigate cause and handle capacity. Not a proxy issue - customer count is direct metric. Need context: What caused surge? Is it real? How to handle?"

---

### BUCKET 2: Metric Traps & Gaming
**Questions:** ~2 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Is this a vanity metric?" or "Can this be gamed?" - same framework, with focus on traps
- **Approach:** Same metrics interpretation framework, with focus on common traps
- **Common Traps:** Vanity metric (Pageviews with no engagement), Proxy drift (CTR no longer predicts retention), Metric cannibalization (Time spent ↑ but content quality ↓), Local optimization (Team wins, company loses), Dashboard blindness (Green metrics, red user experience)
- **Gaming Prevention:** Don't tie metrics to bonuses, Use multiple metrics, Monitor counter-metrics, Focus on user value

**Concrete Examples:**
- "Vanity metric: Pageviews ↑ but engagement ↓ → Weak proxy, being gamed"
- "Metric traps: Identify vanity metrics, proxy drift, gaming, local optimization"

**Representative Questions (Do 5 only):**
- Q144: Can a university have a lower overall acceptance rate for female-identifying students, even if every department admits them at a higher rate than others? (Simpson's paradox/trap angle)
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (metric interpretation/trap angle)
- Q117: As the PM for Lyft, what dashboard would you build to track the health of the app? (metric interpretation/trap angle)
- Q183: Debug a metric that was off by x percentage. (metric interpretation/trap angle)
- Q790: Explain data drifting. (metric interpretation/trap angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When identifying metric traps and gaming, I use the same metrics interpretation framework but focus on traps. I check for Vanity metrics: Pageviews with no engagement, signups with no activation, downloads with no usage. I check for Proxy drift: CTR no longer predicts retention, signup rate doesn't predict LTV. I check for Metric cannibalization: Time spent ↑ but content quality ↓, engagement ↑ but satisfaction ↓. I check for Local optimization: Team wins (optimizes their metric), company loses (hurts overall value). I check for Dashboard blindness: Green metrics (all metrics look good), red user experience (users unhappy). I prevent gaming: Don't tie metrics to bonuses (If tied to goals/bonuses, it WILL be gamed), Use multiple metrics (Don't optimize single metric), Monitor counter-metrics (Track what might be hurt), Focus on user value (Optimize for real value, not metrics). The key is understanding that a metric moving is not the same as progress. Proxies decay over time. If a metric becomes a target, it stops being a metric."

**How to Adapt This Narrative for Each Question:**

- **Q144 (Simpson's paradox trap):** Focus on aggregation trap → "This is a classic aggregation trap (Simpson's paradox). The overall metric (acceptance rate) is misleading because it aggregates across departments with different application rates. I'd check: Vanity metric? No - acceptance rate is meaningful, Proxy drift? No - it's a direct metric, Metric cannibalization? No, Local optimization? No, Dashboard blindness? Yes - overall metric looks bad, but department-level metrics look good. The trap is using overall metric when segment-level metrics tell different story. I'd prevent: Use department-level rates for fairness assessment, Don't optimize overall rate alone, Monitor both overall and segment-level metrics, Focus on fairness at department level, not overall."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Metrics Interpretation Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Metric Traps & Gaming** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through metrics interpretation framework in 2 minutes (Metric Moved → Proxy Validity → Gaming Risk → Context Checks → Decide)
- [ ] Check metric movement (Direction, magnitude, scope, time, aggregation level)
- [ ] Validate proxy (Is it proxy or real goal? Correlation? Leading vs lagging? Blind spots?)
- [ ] Assess gaming risk (By users? Teams? Design? Reporting?)
- [ ] Check context (Seasonality, launches, external events, data issues, aggregation bias)
- [ ] Decide (Ignore, monitor, investigate, act)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the metrics interpretation framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Metric Moved → Proxy Validity → Gaming Risk → Context Checks → Decide framework**, not memorizing answers

**Remember:** L12 is about metrics interpretation. The framework: Metric Moved → Proxy Validity → Gaming Risk → Context Checks → Decide. Key principles: A metric moving is not the same as progress. Proxies decay over time. If a metric becomes a target, it stops being a metric. Context beats dashboards.
