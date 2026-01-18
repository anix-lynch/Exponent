# 🟢🟡🔴 PATTERN MATCHING CHEATSHEET

**Purpose:** Instant pattern recognition for interview questions

**How to use:** 
1. Read question
2. Match to pattern (use keywords/structure)
3. Pull up framework
4. Answer

**No thinking, just pattern matching.**

---

## 🟢 NORTHSTAR PATTERNS (12)

**Master these → answer 80% of all interviews**

```
🟢 NORTHSTAR PATTERNS (12)
│
├─ 1) Metric Drop Diagnosis Tree
│   ├─ #Metrics #RootCause #Segmentation
│   └─ "X is down/up by Y% — why?"
│      (clarify metric → segment → hypothesize → validate)
│
├─ 2) North Star Metric + KPI Ladder
│   ├─ #Metrics #Strategy #Alignment
│   └─ "How do we define success?"
│      (NSM → input KPIs → guardrails)
│
├─ 3) Funnel Decomposition + Conversion Fix
│   ├─ #Funnels #ProductAnalytics #Growth
│   └─ "Where are users dropping?"
│      (steps → rates → biggest leak → fixes)
│
├─ 4) Cohort / Retention / Churn Reasoning
│   ├─ #Retention #Cohorts #Lifecycle
│   └─ "Who is leaving and when?"
│      (time-based cohorts → behavior → drivers)
│
├─ 5) Segmentation (Who / Where / Why) + Targeting
│   ├─ #Segmentation #Customer #Strategy
│   └─ "Which users matter most?"
│      (persona × behavior × value)
│
├─ 6) Prioritization Framework (RICE / Impact–Effort)
│   ├─ #Prioritization #Execution #Tradeoffs
│   └─ "What should we do first?"
│      (impact, confidence, cost, constraints)
│
├─ 7) Tradeoff Framing + Guardrails
│   ├─ #Tradeoffs #SecondOrderEffects
│   └─ "A vs B — what do we give up?"
│      (winners/losers, risks, guardrails)
│
├─ 8) Experiment Design & Causal Reasoning
│   ├─ #Experimentation #Causality #ABTesting
│   └─ "Does X actually cause Y?"
│      (hypothesis → metric → design → pitfalls)
│
├─ 9) Decision-Making Under Uncertainty
│   ├─ #Ambiguity #DecisionMaking #Assumptions
│   └─ "We don't know enough — now what?"
│      (assumptions → bets → validation plan)
│
├─ 10) Executive Communication (1-Pager / Narrative)
│   ├─ #Communication #ExecReadout
│   └─ "Summarize this for leadership."
│      (context → insight → recommendation)
│
├─ 11) Stakeholder Alignment + Influence Without Authority
│   ├─ #Stakeholders #Leadership #Alignment
│   └─ "Teams disagree — how do we move?"
│      (incentives, concerns, coalition)
│
└─ 12) Operational Excellence (Risk / Monitoring / Escalation)
    ├─ #Execution #Operations #Delivery
    └─ "How do we ship and keep it healthy?"
       (risks, metrics, alerts, ownership)
```

**If you want, I can next:**
- map **ALL_CATEGORIES.md → these 12 patterns**, or
- tag **sample questions** to prove coverage, or
- generate the **🟢 Top-30 Northstar Questions** list

---

## 🟡 LOW-HANGING FRUIT (Template-able, Non-Northstar, Non-Coding)

**Purpose:**
• Medium frequency
• Cross-role but not universal
• Reasoning > implementation
• Preserves original skill tags for backward compatibility
• Each item = a reusable mini-pattern (like Northstar, but narrower)

```
🟡 LHF
│
├─ 1) Data Readiness & Trust Pattern
│   Tags: #DataQuality #DataWarehousing #DataAnalysis
│   └─ "Can we trust this data?"
│      (sources, freshness, bias, missingness, lineage)
│
├─ 2) Scale & Capacity Reasoning
│   Tags: #Scalability #PerformanceOptimization #SystemDesign
│   └─ "What breaks at 10×?"
│      (load, latency, cost, people, infra limits)
│
├─ 3) Cost / ROI Framing
│   Tags: #FinancialAnalysis #BusinessMetrics
│   └─ "Is this worth it?"
│      (cost drivers, marginal gains, breakeven)
│
├─ 4) System Constraints Mapping
│   Tags: #StrategicPlanning #Execution #ProgramManagement
│   └─ "What constraints limit us?"
│      (legal, infra, org, time, dependencies)
│
├─ 5) Instrumentation & Observability
│   Tags: #MonitoringObservability #Metrics
│   └─ "What should we log or watch?"
│      (signals, alerts, leading vs lagging indicators)
│
├─ 6) Operational Tradeoffs (Ops-level)
│   Tags: #TradeOffs #Execution
│   └─ "Speed vs quality vs reliability"
│      (SLAs, error budgets, failure modes)
│
├─ 7) Data Modeling for Decision-Making
│   Tags: #DataModeling #AnalyticsMetrics
│   └─ "What entities & metrics matter?"
│      (facts vs dimensions, grain, joins conceptually)
│
├─ 8) Market & Competitive Snapshot
│   Tags: #MarketAnalysis #CompetitiveAnalysis
│   └─ "What alternatives exist and why?"
│      (substitutes, differentiation, positioning)
│
├─ 9) Financial Sensitivity Analysis
│   Tags: #FinancialModeling #Pricing
│   └─ "What moves the needle most?"
│      (price, volume, churn, CAC, LTV)
│
├─ 10) Process & Workflow Optimization
│    Tags: #ProcessImprovement #BusinessAnalysis
│    └─ "Where are the bottlenecks?"
│       (handoffs, queues, ownership)
│
├─ 11) Risk Enumeration & Mitigation
│    Tags: #OperationalRisk #Leadership
│    └─ "What could go wrong?"
│       (failure modes, blast radius, mitigations)
│
├─ 12) Advanced Metrics Interpretation
│    Tags: #ProductAnalytics #MetricsKPIs
│    └─ "Metric X moved — should we care?"
│       (proxy validity, gaming, lag vs lead)
│
├─ 13) SQL-for-Reasoning (Conceptual)
│    Tags: #SQL #DataAnalysis
│    └─ "How would you compute this?"
│       (grouping logic, joins conceptually — not syntax)
│
└─ 14) System Design (Conceptual Scale)
     Tags: #SystemDesign
     └─ "What components exist?"
        (high-level blocks, data flow, boundaries — no code)
```

---

## 🔴 IGNORE PATTERNS — Do NOT optimize for these

**Low ROI for your target roles**

```
🔴 IGNORE
│
├─ 1) Pure Coding / Algorithmic Problem Solving
│   └─ "Can you implement this exactly?"
│      (LeetCode-style, puzzles, trick logic)
│   #Data Structures & Algorithms
│   #Coding
│   #Low-Level Algorithms
│
├─ 2) ML / AI Theory Depth
│   └─ "Explain the math behind the model"
│      (derivations, proofs, internals)
│   #Machine Learning (theory-heavy)
│   #Deep Learning
│   #Reinforcement Learning
│   #Model Evaluation (academic)
│
├─ 3) Academic Statistics & Math
│   └─ "Derive / prove / compute by hand"
│      (distributions, formulas, exams)
│   #Statistics & Probability (theory)
│   #Academic Statistics
│   #Niche Domain Math
│
├─ 4) Low-Level Systems Engineering
│   └─ "How would you implement this at byte-level?"
│      (memory, threads, kernels)
│   #Concurrency
│   #Distributed Systems (internals)
│   #Operating Systems Concepts
│
├─ 5) Framework / Tool Memorization
│   └─ "Name the exact API / syntax"
│      (tools change, low signal)
│   #APIs (syntax-specific)
│   #Tool-Specific Questions
│   #Vendor-Specific Trivia
│
├─ 6) Ultra-Niche Domain Expertise
│   └─ "Only relevant to one narrow role/company"
│   #Computer Vision (specialized)
│   #Natural Language Processing (research-heavy)
│   #Generative AI (model internals)
│   #LLMs (architecture internals)
│
└─ 7) Wildcard / Gimmick Questions
    └─ "Clever but not transferable"
       (brain teasers, hypotheticals with no reuse)
    #Brain Teasers
    #Trick Questions
    #One-Off Case Math
```

---

## QUICK PATTERN MATCHING GUIDE

### Step 1: Read the question

### Step 2: Match keywords to pattern

**Metric keywords:**
- "down", "up", "dropped", "increased", "flat" → **Pattern #1 (Metric Drop)**
- "define success", "measure", "KPI", "north star" → **Pattern #2 (NSM + KPI)**
- "conversion", "funnel", "drop-off" → **Pattern #3 (Funnel)**
- "churn", "retention", "leaving" → **Pattern #4 (Cohort/Retention)**

**Strategy keywords:**
- "segment", "target", "who", "which users" → **Pattern #5 (Segmentation)**
- "prioritize", "choose", "first" → **Pattern #6 (Prioritization)**
- "A vs B", "tradeoff", "give up" → **Pattern #7 (Tradeoff)**

**Execution keywords:**
- "test", "experiment", "A/B", "causal" → **Pattern #8 (Experiment)**
- "unclear", "ambiguous", "don't know" → **Pattern #9 (Uncertainty)**
- "present", "CEO", "executive", "summarize" → **Pattern #10 (Exec Comm)**
- "stakeholder", "align", "disagree" → **Pattern #11 (Influence)**
- "deliver", "ship", "risk", "monitor" → **Pattern #12 (Ops Excellence)**

### Step 3: Pull up the framework (from 1_NORTHSTAR_PATTERNS.md)

### Step 4: Apply framework to question

---

## EXAMPLE PATTERN MATCHING

### Example 1:
**Question:** "Amazon orders are down 25% — what do you do?"

**Pattern Match:**
- Keywords: "down 25%" → **Pattern #1 (Metric Drop Diagnosis)**
- Framework: Clarify metric → Segment → Hypothesize → Validate

**Answer Structure:**
```
1. Clarify: What's the exact metric? (total orders, unique customers, GMV?)
2. Segment: Where is the drop? (geography, device, user type, product category)
3. Hypothesize: Internal bug? External factor? Seasonality?
4. Validate: Check logs, compare cohorts, look at funnels
```

---

### Example 2:
**Question:** "How would you define success for Instagram Reels?"

**Pattern Match:**
- Keywords: "define success" → **Pattern #2 (NSM + KPI Ladder)**
- Framework: NSM → Input KPIs → Guardrails

**Answer Structure:**
```
1. NSM: Time spent on Reels (captures engagement + value)
2. Input KPIs: 
   - Reels created per user
   - Reels viewed per session
   - Share rate
3. Guardrails:
   - Don't cannibalize Feed engagement
   - Watch time quality (not just autoplay)
```

---

### Example 3:
**Question:** "Should Uber expand into Uber Eats?"

**Pattern Match:**
- Keywords: "should we", "expand" → **Pattern #7 (Tradeoff)** + **Pattern #5 (Segmentation)**
- Framework: Winners/Losers → Risks → Guardrails

**Answer Structure:**
```
1. Winners: Drivers (more income), Users (convenience), Uber (new revenue)
2. Losers: Focus (split attention), Brand (food vs rides), Restaurants (take rate)
3. Risks: Operational complexity, unit economics, competition
4. Guardrails: Start in 1 city, measure cannibalization, set profitability targets
```

---

## TRAFFIC LIGHT SCORING

**How to score a question:**

```
Score = 0-10

+3  appears in 5+ roles (cross-role)
+3  pattern repeats 10+ times (high frequency)
+2  one framework answers many variants (template-able)
+1  shows judgment/tradeoffs (senior signal)
+1  can master in 60-90 min (fast ROI)

SUBTRACT:
-3  niche / one-off / trivia
-3  heavy memorization (DSA, ML math)
-2  tool-specific / prompt-specific
```

**Traffic Light:**
- **🟢 (8-10):** Northstar pattern
- **🟡 (5-7):** Low-hanging fruit
- **🔴 (0-4):** Ignore

---

## NEXT STEPS

1. **Memorize the 12 Northstar patterns** (1 hour)
2. **Practice pattern matching** on 50 sample questions (2 hours)
3. **Build your Top-30 list** (30 questions across 12 patterns)
4. **Drill frameworks** until automatic (10-20 hours)

**Total prep time: 15-25 hours to master 80% of interviews**

---

## FILES TO USE

- **0_TAXONOMY_PRIMARY_INTENTS.md** - Understand the 9 intents
- **1_NORTHSTAR_PATTERNS.md** - Full frameworks with ASCII trees
- **🟢🟡🔴_PATTERN_MATCHING_CHEATSHEET.md** - This file (quick reference)
- **ALL_QUESTIONS_RAW.md** - Source of truth (2,893 questions)

**Next:** Tag questions using this cheatsheet → Build Top-30 🟢 list
