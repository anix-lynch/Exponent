# 🤖 TAGGING ALGORITHM [FOR LLM EYES ONLY]

**Purpose:** Deterministic classification of 2,893 questions into 🟢🟡🔴

**Usage:** Feed this file + ALL_QUESTIONS_RAW.md → Get bucketed output

**No creativity. No interpretation. Follow the tree.**

---

## DECISION TREE (EXECUTE IN ORDER)

```
START: Read question
│
├─ STEP 1: Check IMMEDIATE REJECT triggers
│  └─ If ANY trigger matches → 🔴 IGNORE (STOP)
│
├─ STEP 2: Check NORTHSTAR eligibility
│  ├─ Does it match a Northstar pattern? (check keywords)
│  ├─ Does it pass ALL 4 gates? (see gates below)
│  └─ If YES to both → 🟢 NORTHSTAR (STOP)
│
├─ STEP 3: Check LHF eligibility
│  ├─ Does it match an LHF pattern? (check keywords)
│  ├─ Does it pass ALL 4 gates? (see gates below)
│  └─ If YES to both → 🟡 LHF (STOP)
│
└─ STEP 4: Default
   └─ If nothing matched → 🔴 IGNORE
```

---

## STEP 1: IMMEDIATE REJECT TRIGGERS (🔴)

**Check these FIRST. If ANY match → 🔴 IGNORE immediately.**

### Trigger Set A: Code/Implementation Required

```python
REJECT_IF_CONTAINS = [
    # Explicit code requests
    "write a function",
    "implement",
    "write code",
    "code this",
    "write a program",
    "algorithm to",
    "pseudocode",
    
    # SQL syntax (not conceptual)
    "write a query",
    "write sql",
    "sql query to",
    "select * from",
    
    # Data structures
    "linked list",
    "binary tree",
    "hash table",
    "array manipulation",
    "reverse a",
    "merge k",
    "valid parentheses",
    
    # Algorithms
    "leetcode",
    "two sum",
    "dynamic programming",
    "sliding window",
    "backtracking",
]
```

### Trigger Set B: Math/Theory Depth

```python
REJECT_IF_CONTAINS = [
    "derive the",
    "prove that",
    "proof of",
    "calculate by hand",
    "show the math",
    "loss function",
    "gradient descent",
    "backpropagation",
    "probability distribution",
    "bayesian",
]
```

### Trigger Set C: Niche/One-Off

```python
REJECT_IF_CONTAINS = [
    "brain teaser",
    "how many golf balls",
    "how many piano tuners",
    "estimate the weight",
    "riddle",
]
```

**If ANY trigger matches → 🔴 IGNORE (do not proceed to Step 2)**

---

## STEP 2: NORTHSTAR ELIGIBILITY (🟢)

**Only check if passed Step 1 (no reject triggers)**

### The 4 Gates (ALL must pass)

```
Gate 1: Matches ONE of the 12 Northstar patterns (see keyword table below)
Gate 2: Requires NO code, NO syntax, NO low-level internals
Gate 3: Answer structure applies across ≥3 roles
Gate 4: Focuses on reasoning, diagnosis, prioritization, or decision-making
```

### Northstar Pattern Keyword Table

```python
NORTHSTAR_PATTERNS = {
    "Pattern_1_Metric_Drop": {
        "keywords": ["down", "dropped", "decreased", "declined", "falling", "drop", "fell", "lower"],
        "structure": "X is down/up by Y%",
        "examples": ["orders down 25%", "searches dropped 35%", "churn increased"]
    },
    
    "Pattern_2_NSM_KPI": {
        "keywords": ["define success", "measure success", "north star", "kpi", "metrics for", "how measure"],
        "structure": "How define/measure success for X?",
        "examples": ["define success for Reels", "metrics for Airbnb Experiences"]
    },
    
    "Pattern_3_Funnel": {
        "keywords": ["conversion", "funnel", "drop-off", "drop off", "users dropping", "abandonment"],
        "structure": "Where are users dropping?",
        "examples": ["conversion dropped", "checkout abandonment", "sign-up funnel"]
    },
    
    "Pattern_4_Cohort_Retention": {
        "keywords": ["churn", "retention", "leaving", "cohort", "attrition", "staying"],
        "structure": "Who is leaving and when?",
        "examples": ["churn increased 40%", "retention is flat", "D7 retention"]
    },
    
    "Pattern_5_Segmentation": {
        "keywords": ["segment", "which users", "who should", "target", "persona", "which customers"],
        "structure": "Which users matter most?",
        "examples": ["which users to target", "segment analysis", "who should we focus on"]
    },
    
    "Pattern_6_Prioritization": {
        "keywords": ["prioritize", "what first", "which feature", "rank", "order", "sequence"],
        "structure": "What should we do first?",
        "examples": ["how prioritize features", "what to build first", "rank initiatives"]
    },
    
    "Pattern_7_Tradeoff": {
        "keywords": ["tradeoff", "trade-off", "vs", "versus", "or", "choose between", "a or b"],
        "structure": "A vs B — what do we give up?",
        "examples": ["pagination vs infinite scroll", "ads vs clean UX", "speed vs quality"]
    },
    
    "Pattern_8_Experiment": {
        "keywords": ["a/b test", "experiment", "test design", "causal", "does x cause", "validate"],
        "structure": "Does X actually cause Y?",
        "examples": ["how a/b test", "is this result valid", "experiment design"]
    },
    
    "Pattern_9_Uncertainty": {
        "keywords": ["unclear", "ambiguous", "don't know", "uncertain", "missing information", "incomplete"],
        "structure": "We don't know enough — now what?",
        "examples": ["unclear requirements", "ambiguous data", "missing information"]
    },
    
    "Pattern_10_Exec_Comm": {
        "keywords": ["present to", "ceo", "executive", "leadership", "summarize for", "communicate to"],
        "structure": "Summarize this for leadership",
        "examples": ["present to CEO", "exec summary", "communicate to leadership"]
    },
    
    "Pattern_11_Influence": {
        "keywords": ["stakeholder", "align", "disagree", "influence", "without authority", "buy-in"],
        "structure": "Teams disagree — how do we move?",
        "examples": ["stakeholder alignment", "influence without authority", "get buy-in"]
    },
    
    "Pattern_12_Ops_Excellence": {
        "keywords": ["deliver", "ship", "risk", "monitor", "escalate", "execute", "launch"],
        "structure": "How do we ship and keep it healthy?",
        "examples": ["deliver project", "manage risk", "monitor health", "execution plan"]
    }
}
```

### Northstar Matching Logic

```python
def check_northstar(question):
    # Check if matches any pattern
    matched_patterns = []
    for pattern_name, pattern_data in NORTHSTAR_PATTERNS.items():
        if any(keyword in question.lower() for keyword in pattern_data["keywords"]):
            matched_patterns.append(pattern_name)
    
    if not matched_patterns:
        return False, None
    
    # Check Gate 2: No code required
    if contains_reject_trigger(question):
        return False, None
    
    # Gate 3 & 4: Assume true if pattern matched (validate manually if needed)
    
    # If multiple patterns match, pick primary
    primary_pattern = matched_patterns[0]  # First match wins
    
    return True, primary_pattern
```

**If ALL 4 gates pass → 🟢 NORTHSTAR**

---

## STEP 3: LHF ELIGIBILITY (🟡)

**Only check if NOT 🟢 Northstar**

### The 4 Gates (ALL must pass)

```
Gate 1: Still reasoning-first (not implementation-first)
Gate 2: Introduces domain constraints (data, finance, systems, ops)
Gate 3: Can be answered conceptually without writing code
Gate 4: Maps to a reusable secondary pattern (not one-off)
```

### LHF Pattern Keyword Table

```python
LHF_PATTERNS = {
    "LHF_1_Data_Trust": {
        "keywords": ["trust", "data quality", "bias", "missing", "freshness", "lineage", "reliable"],
        "question": "Can we trust this data?"
    },
    
    "LHF_2_Scale": {
        "keywords": ["scale", "10x", "capacity", "load", "latency", "breaks at"],
        "question": "What breaks at 10×?"
    },
    
    "LHF_3_Cost_ROI": {
        "keywords": ["cost", "roi", "worth it", "breakeven", "marginal", "financial"],
        "question": "Is this worth it?"
    },
    
    "LHF_4_Constraints": {
        "keywords": ["constraints", "limits", "legal", "compliance", "dependencies", "blockers"],
        "question": "What constraints limit us?"
    },
    
    "LHF_5_Observability": {
        "keywords": ["monitor", "log", "alert", "observe", "instrument", "track"],
        "question": "What should we log or watch?"
    },
    
    "LHF_6_Ops_Tradeoffs": {
        "keywords": ["sla", "error budget", "reliability", "uptime", "failure mode"],
        "question": "Speed vs quality vs reliability"
    },
    
    "LHF_7_Data_Modeling": {
        "keywords": ["data model", "entities", "schema", "facts", "dimensions", "grain"],
        "question": "What entities & metrics matter?"
    },
    
    "LHF_8_Market_Competitive": {
        "keywords": ["market", "competitive", "alternatives", "substitutes", "differentiation"],
        "question": "What alternatives exist and why?"
    },
    
    "LHF_9_Financial_Sensitivity": {
        "keywords": ["price", "volume", "cac", "ltv", "unit economics", "sensitivity"],
        "question": "What moves the needle most?"
    },
    
    "LHF_10_Process_Optimization": {
        "keywords": ["bottleneck", "handoff", "workflow", "process", "queue", "efficiency"],
        "question": "Where are the bottlenecks?"
    },
    
    "LHF_11_Risk": {
        "keywords": ["risk", "failure mode", "blast radius", "mitigation", "contingency"],
        "question": "What could go wrong?"
    },
    
    "LHF_12_Metrics_Interpretation": {
        "keywords": ["proxy", "gaming", "lag", "lead", "metric moved", "should we care"],
        "question": "Metric X moved — should we care?"
    },
    
    "LHF_13_SQL_Reasoning": {
        "keywords": ["how compute", "grouping", "join", "aggregate", "conceptually"],
        "question": "How would you compute this?"
        # NOTE: Only if NO "write a query" trigger
    },
    
    "LHF_14_System_Design_Conceptual": {
        "keywords": ["components", "data flow", "high-level", "architecture", "blocks"],
        "question": "What components exist?"
        # NOTE: Only if NO code/implementation required
    }
}
```

**If ALL 4 gates pass → 🟡 LHF**

---

## STEP 4: DEFAULT (🔴)

**If nothing matched in Steps 2-3 → 🔴 IGNORE**

---

## CONFLICT RESOLUTION RULES

### Priority Order (strict precedence)

```
1. IGNORE trumps everything
   - If ANY reject trigger → 🔴 (even if Northstar keywords present)

2. NORTHSTAR trumps LHF
   - If both match → 🟢

3. Multiple Northstar patterns
   - Pick first match (order: Pattern 1 → 12)

4. Multiple LHF patterns
   - Pick first match (order: LHF 1 → 14)

5. When unclear
   - Default to 🔴 IGNORE
```

### Example Conflicts

```
Q: "Write a SQL query to find orders that dropped 25%"
- Matches: Pattern #1 (Metric Drop) keywords ✓
- Matches: REJECT trigger ("write a query") ✓
→ IGNORE wins → 🔴

Q: "How would you diagnose why orders dropped and what data would you need?"
- Matches: Pattern #1 (Metric Drop) ✓
- Matches: LHF #1 (Data Trust) ✓
→ NORTHSTAR wins → 🟢 (Pattern #1)

Q: "Explain the difference between SQL and NoSQL"
- Matches: No Northstar pattern ✗
- Matches: No LHF pattern ✗
→ Default → 🔴
```

---

## OUTPUT FORMAT

**For each question, output:**

```
Question ID: {number}
Question: {text}
Bucket: 🟢 | 🟡 | 🔴
Pattern: {Pattern name or "N/A"}
Reasoning: {1 sentence why}
Confidence: High | Medium | Low
```

**Example:**

```
Question ID: 42
Question: Amazon orders are down 25% — what do you do?
Bucket: 🟢
Pattern: Pattern_1_Metric_Drop
Reasoning: Matches metric drop keywords, no code required, reasoning-first
Confidence: High
```

---

## WORKED EXAMPLES (50 EXAMPLES)

### Example Set 1: Clear 🟢 Northstar

```
1. "Amazon orders are down 25%"
   → 🟢 Pattern_1_Metric_Drop
   Reason: Matches "down 25%", no code, reasoning-first

2. "How would you define success for Instagram Reels?"
   → 🟢 Pattern_2_NSM_KPI
   Reason: Matches "define success", no code, cross-role

3. "Conversion rate dropped from 10% to 7%"
   → 🟢 Pattern_3_Funnel
   Reason: Matches "conversion" + "dropped", funnel analysis

4. "Churn increased 40% in the last month"
   → 🟢 Pattern_4_Cohort_Retention
   Reason: Matches "churn increased", retention analysis

5. "Which user segments should we target first?"
   → 🟢 Pattern_5_Segmentation
   Reason: Matches "segments" + "target", segmentation framework

6. "How would you prioritize these 5 features?"
   → 🟢 Pattern_6_Prioritization
   Reason: Matches "prioritize", RICE framework applies

7. "Should we use pagination or infinite scroll?"
   → 🟢 Pattern_7_Tradeoff
   Reason: Matches "or", A vs B tradeoff analysis

8. "How would you A/B test this new checkout flow?"
   → 🟢 Pattern_8_Experiment
   Reason: Matches "A/B test", experiment design

9. "The requirements are unclear — how would you proceed?"
   → 🟢 Pattern_9_Uncertainty
   Reason: Matches "unclear", decision under uncertainty

10. "Present your recommendation to the CEO"
    → 🟢 Pattern_10_Exec_Comm
    Reason: Matches "CEO", executive communication
```

### Example Set 2: Clear 🔴 Ignore

```
11. "Write a function to reverse a linked list"
    → 🔴 IGNORE
    Reason: REJECT trigger "write a function" + "linked list"

12. "Implement a hash table from scratch"
    → 🔴 IGNORE
    Reason: REJECT trigger "implement" + code required

13. "Write a SQL query to find the top 3 salaries per department"
    → 🔴 IGNORE
    Reason: REJECT trigger "write a query" + SQL syntax

14. "Derive the gradient descent formula"
    → 🔴 IGNORE
    Reason: REJECT trigger "derive" + ML math

15. "Prove that this algorithm is O(n log n)"
    → 🔴 IGNORE
    Reason: REJECT trigger "prove" + algorithm theory

16. "How many golf balls fit in a school bus?"
    → 🔴 IGNORE
    Reason: REJECT trigger "brain teaser"

17. "Explain backpropagation in neural networks"
    → 🔴 IGNORE
    Reason: ML theory depth, not reasoning-first

18. "What is the difference between TCP and UDP?"
    → 🔴 IGNORE
    Reason: Low-level systems, not cross-role

19. "Implement a LRU cache"
    → 🔴 IGNORE
    Reason: REJECT trigger "implement" + code

20. "Find the two sum in an array"
    → 🔴 IGNORE
    Reason: LeetCode-style, algorithm puzzle
```

### Example Set 3: Clear 🟡 LHF

```
21. "How would you check if this data is trustworthy?"
    → 🟡 LHF_1_Data_Trust
    Reason: Matches "trustworthy", data quality reasoning

22. "What would break if we scaled to 10x traffic?"
    → 🟡 LHF_2_Scale
    Reason: Matches "10x", scale reasoning

23. "Is this project worth the cost?"
    → 🟡 LHF_3_Cost_ROI
    Reason: Matches "worth the cost", ROI analysis

24. "What constraints limit our launch timeline?"
    → 🟡 LHF_4_Constraints
    Reason: Matches "constraints limit", constraint mapping

25. "What should we monitor after launch?"
    → 🟡 LHF_5_Observability
    Reason: Matches "monitor", observability pattern

26. "What are the failure modes of this system?"
    → 🟡 LHF_11_Risk
    Reason: Matches "failure modes", risk enumeration

27. "How would you model user behavior data?"
    → 🟡 LHF_7_Data_Modeling
    Reason: Matches "model", data modeling (conceptual)

28. "What are our main competitors and how do we differ?"
    → 🟡 LHF_8_Market_Competitive
    Reason: Matches "competitors" + "differ", market analysis

29. "Which lever (price, volume, churn) has the biggest impact?"
    → 🟡 LHF_9_Financial_Sensitivity
    Reason: Matches financial levers, sensitivity analysis

30. "Where are the bottlenecks in our workflow?"
    → 🟡 LHF_10_Process_Optimization
    Reason: Matches "bottlenecks", process optimization
```

### Example Set 4: Edge Cases & Conflicts

```
31. "Orders dropped 25% — write a SQL query to investigate"
    → 🔴 IGNORE
    Reason: Has Northstar keywords BUT "write a query" trigger → IGNORE wins

32. "How would you conceptually join these two datasets?"
    → 🟡 LHF_13_SQL_Reasoning
    Reason: "Conceptually" + no "write a query" → LHF (not code)

33. "Design a high-level architecture for a data pipeline"
    → 🟡 LHF_14_System_Design_Conceptual
    Reason: "High-level" + no implementation → LHF

34. "Design a data pipeline and write the ETL code"
    → 🔴 IGNORE
    Reason: "Write the code" trigger → IGNORE

35. "How would you explain this metric drop to executives?"
    → 🟢 Pattern_10_Exec_Comm
    Reason: Primary intent is exec communication (not metric diagnosis)

36. "Diagnose why churn increased and present to the CEO"
    → 🟢 Pattern_4_Cohort_Retention
    Reason: Primary intent is diagnosis (exec comm is secondary)

37. "What's your approach to prioritization?"
    → 🔴 IGNORE
    Reason: Abstract/generic, no specific scenario (not pattern-matchable)

38. "Tell me about a time you prioritized competing features"
    → 🔴 IGNORE
    Reason: Behavioral (past story), not framework question

39. "How do you handle ambiguity?"
    → 🔴 IGNORE
    Reason: Abstract/generic, no specific scenario

40. "You have unclear requirements for a new feature — what do you do?"
    → 🟢 Pattern_9_Uncertainty
    Reason: Specific scenario, decision under uncertainty

41. "Estimate the market size for electric scooters"
    → 🔴 IGNORE
    Reason: Estimation/market sizing, not a reusable pattern

42. "How would you segment the electric scooter market?"
    → 🟢 Pattern_5_Segmentation
    Reason: Segmentation framework applies

43. "What metrics would you track for a new product?"
    → 🟢 Pattern_2_NSM_KPI
    Reason: Metric definition, NSM + KPI framework

44. "Track this metric using SQL"
    → 🔴 IGNORE
    Reason: "Using SQL" implies implementation

45. "How would you know if this A/B test result is valid?"
    → 🟢 Pattern_8_Experiment
    Reason: Experiment interpretation, causal reasoning

46. "Calculate the p-value for this A/B test"
    → 🔴 IGNORE
    Reason: Math calculation, not reasoning

47. "What would you do if stakeholders disagree on priorities?"
    → 🟢 Pattern_11_Influence
    Reason: Stakeholder alignment, influence pattern

48. "How do you communicate with stakeholders?"
    → 🔴 IGNORE
    Reason: Abstract/generic, no specific scenario

49. "Design a dashboard for executives"
    → 🟡 LHF_5_Observability
    Reason: Monitoring/metrics, but not Northstar (too narrow)

50. "What's the most important metric for a marketplace?"
    → 🟢 Pattern_2_NSM_KPI
    Reason: North Star Metric question
```

---

## VALIDATION CHECKLIST

**After tagging, verify:**

```
[ ] All questions with "write", "implement", "code" → 🔴
[ ] All questions with "down/up X%" → 🟢 (unless code required)
[ ] All questions with "define success" → 🟢
[ ] All LeetCode-style → 🔴
[ ] All ML theory → 🔴
[ ] All "tell me about a time" → 🔴 (behavioral, not framework)
[ ] All abstract "how do you" → 🔴 (unless specific scenario)
```

---

## FINAL INSTRUCTION

**Execute this algorithm on ALL_QUESTIONS_RAW.md:**

1. Read question
2. Check REJECT triggers (Step 1)
3. Check NORTHSTAR (Step 2)
4. Check LHF (Step 3)
5. Default to IGNORE (Step 4)
6. Output in specified format

**No creativity. No interpretation. Follow the tree.**

**Confidence levels:**
- **High:** Clear pattern match, no ambiguity
- **Medium:** Pattern match but edge case
- **Low:** Unclear, defaulted to 🔴

**When in doubt → 🔴 IGNORE**
