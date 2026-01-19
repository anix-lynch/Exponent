# 🤖 TAGGING ALGORITHM [FOR LLM EYES ONLY]

**Purpose:** Deterministic classification of 2,893 questions into 🟢🟡🔴

**Usage:** Feed this file + ALL_QUESTIONS_NORMALIZED.md → Get bucketed output

**Approach:** Intent-based (not just keyword matching)

---

## 🧠 INTENT-BASED CLASSIFICATION (NOT FINE-TUNING)

**What this means:**
- Classify the question's **PRIMARY INTENT**, not just surface keywords
- "Squares of a sorted array" → Intent: ALGORITHM_PUZZLE → 🔴
- "How would you compute top salaries?" → Intent: REASONING → 🟡
- "Write a query for top salaries" → Intent: SYNTAX_RECALL → 🔴

**How it works:**
1. **Layer 1:** Fast keyword triggers (explicit)
2. **Layer 2:** Intent detection via semantic patterns (deterministic scoring)
3. **Boundary rules:** Handle edge cases (SQL syntax vs reasoning, etc.)

**Still deterministic. Still auditable. No model training required.**

---

**No creativity. No interpretation. Follow the tree.**

---

## ⚡ 5-SECOND DECISION GUIDE (CHECK THIS FIRST)

```
INTENT CHECK (not just keywords):

If asking to PRODUCE artifact (code/query/algorithm/proof) → 🔴
If LeetCode-style shape (given array, return X, constraints) → 🔴

Else if REASONING about metric/success/funnel/churn/segment/prioritize/experiment/exec/influence/ops → 🟢

Else if REASONING about trust/scale/ROI/constraints/observability/risk/conceptual system → 🟡

Else → 🔴
```

**Key distinction: "Write a query" vs "How would you compute" = different intents**

**Use this for 90% of questions. Only use full decision tree for edge cases.**

---

## 🎯 BOUNDARY EXAMPLES (RISKY EDGES)

**SQL:**
- ❌ "Write a SQL query to find top 3 salaries" → 🔴 (code required)
- ✅ "How would you compute top 3 salaries per department?" → 🟡 (conceptual)

**System Design:**
- ❌ "Design a rate limiter with code" → 🔴 (implementation)
- ✅ "What high-level components would a rate limiter need?" → 🟡 (conceptual)

**Behavioral:**
- ❌ "Tell me about a time you handled conflict" → 🔴 (past story, not framework)
- ✅ "Stakeholders disagree on priorities in this scenario — what do you do?" → 🟢 (framework)

**Metric Questions:**
- ❌ "Calculate the p-value for this A/B test" → 🔴 (math calculation)
- ✅ "How would you know if this A/B test result is valid?" → 🟢 (reasoning)

**Ambiguity:**
- ❌ "How do you handle ambiguity?" → 🔴 (abstract, no scenario)
- ✅ "Requirements are unclear for this feature — what do you do?" → 🟢 (specific scenario)

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

## STEP 1: IMMEDIATE REJECT (🔴) — INTENT-BASED

**Reject if the PRIMARY INTENT is to produce an artifact or test implementation skill.**

**Two-layer detection: Fast path (keywords) + Intent path (semantic patterns)**

---

### LAYER 1: EXPLICIT TRIGGERS (Fast Path)

**If ANY of these keywords/phrases → 🔴 immediately**

```python
# A) Code Production Verbs
EXPLICIT_CODE_VERBS = [
    "write a function", "implement", "write code", "code this",
    "write a program", "build a", "create a function",
    "develop an algorithm", "pseudocode"
]

# B) SQL Syntax Requests
EXPLICIT_SQL = [
    "write a query", "write sql", "sql query to",
    "select * from", "select from", "create table"
]

# C) Known LeetCode Problems
LEETCODE_PROBLEMS = [
    "two sum", "valid parentheses", "reverse a linked list",
    "merge k sorted", "longest substring", "climbing stairs",
    "coin change", "word break", "house robber"
]

# D) Math/Theory Production
MATH_PRODUCTION = [
    "derive the", "prove that", "proof of",
    "calculate by hand", "show the math",
    "gradient descent", "backpropagation"
]

# E) Brain Teasers
BRAIN_TEASERS = [
    "how many golf balls", "how many piano tuners",
    "estimate the weight", "riddle"
]
```

---

### LAYER 2: INTENT DETECTION (Semantic Patterns)

**Even if no explicit keywords, reject if it matches these INTENT patterns:**

#### 🔴 **INTENT A: IMPLEMENTATION_REQUIRED**

**Pattern:** Question asks to PRODUCE executable logic (not discuss it)

**Signals (if 2+ match → 🔴):**
```
✓ Contains verb+noun pair:
  - Verbs: [implement, build, create, develop, optimize, debug, refactor]
  - Nouns: [function, class, method, program, script, algorithm, data structure, parser, cache, rate limiter]
  
✓ Has input/output specification:
  - "given an array/string/tree/graph"
  - "return the"
  - "output should be"
  
✓ Mentions constraints:
  - "O(n)", "O(log n)", "time complexity"
  - "in-place", "without extra space"
  - "constraints:", "1 ≤ n ≤ 10^5"
  
✓ Problem shape (transformation):
  - "given X, find Y"
  - "determine if you can"
  - "maximize/minimize subject to"
```

**Examples caught by intent:**
- "Build a regex parser" → build + parser → 🔴
- "Create a rate limiter" → create + rate limiter → 🔴
- "Given an array, find the longest increasing subsequence" → given array + return → 🔴
- "Squares of a sorted array" → transformation problem shape → 🔴

---

#### 🔴 **INTENT B: ALGORITHM_PUZZLE**

**Pattern:** Classic CS puzzle with single correct answer

**Signals (if 2+ match → 🔴):**
```
✓ Data structure manipulation:
  - "array", "string", "tree", "graph", "linked list", "heap"
  - Combined with action: "reverse", "rotate", "merge", "sort"
  
✓ Algorithmic patterns:
  - "dynamic programming", "sliding window", "two pointers"
  - "backtracking", "greedy", "divide and conquer"
  
✓ Optimization problem:
  - "minimum/maximum number of"
  - "shortest/longest path"
  - "most/least efficient"
  
✓ Correctness focus (not judgment):
  - Single testable answer
  - No business context
  - No tradeoffs or stakeholder considerations
```

**Examples caught by intent:**
- "Knapsack problem" → optimization + no business context → 🔴
- "Find element at position in sorted array" → data structure + single answer → 🔴
- "Abbreviate an array of strings" → transformation + no judgment → 🔴

---

#### 🔴 **INTENT C: SYNTAX_RECALL**

**Pattern:** Testing exact syntax or API knowledge

**Signals (if ANY match → 🔴):**
```
✓ SQL syntax:
  - Contains "SELECT", "JOIN", "GROUP BY", "WHERE" as code
  - "Write a query to..."
  
✓ Framework/library specific:
  - "using NumPy", "in Pandas", "with React"
  - "API endpoint for", "REST API that"
  
✓ Low-level implementation:
  - "implement in Python/Java/C++"
  - "using only built-in functions"
```

---

#### 🔴 **INTENT D: MATHEMATICAL_PROOF**

**Pattern:** Requires deriving formulas or proving theorems

**Signals (if ANY match → 🔴):**
```
✓ Proof language:
  - "prove", "derive", "show that", "demonstrate"
  
✓ Theory depth:
  - "loss function", "gradient", "bayesian inference"
  - "probability distribution", "hypothesis testing" (when asking for math)
  - "p-value calculation", "confidence interval derivation"
```

---

### INTENT DETECTION LOGIC

```python
def check_reject_intent(question):
    """
    Returns (should_reject: bool, reason: str)
    """
    q = question.lower()
    
    # LAYER 1: Explicit triggers (fast path)
    for trigger_list in [EXPLICIT_CODE_VERBS, EXPLICIT_SQL, LEETCODE_PROBLEMS, 
                          MATH_PRODUCTION, BRAIN_TEASERS]:
        for trigger in trigger_list:
            if trigger in q:
                return (True, f"Explicit trigger: {trigger}")
    
    # LAYER 2: Intent detection
    intent_scores = {
        'IMPLEMENTATION': 0,
        'ALGORITHM_PUZZLE': 0,
        'SYNTAX_RECALL': 0,
        'MATH_PROOF': 0
    }
    
    # Score IMPLEMENTATION intent
    impl_verbs = ['implement', 'build', 'create', 'develop', 'optimize', 'debug']
    impl_nouns = ['function', 'class', 'method', 'program', 'algorithm', 'parser', 'cache']
    if any(v in q for v in impl_verbs) and any(n in q for n in impl_nouns):
        intent_scores['IMPLEMENTATION'] += 2
    
    if 'given an' in q or 'given a' in q:
        intent_scores['IMPLEMENTATION'] += 1
        intent_scores['ALGORITHM_PUZZLE'] += 1
    
    if 'return' in q or 'output' in q:
        intent_scores['IMPLEMENTATION'] += 1
    
    if any(x in q for x in ['o(n)', 'o(log', 'time complexity', 'in-place', 'constraints:']):
        intent_scores['IMPLEMENTATION'] += 2
        intent_scores['ALGORITHM_PUZZLE'] += 2
    
    # Score ALGORITHM_PUZZLE intent
    ds_words = ['array', 'string', 'tree', 'graph', 'linked list', 'heap']
    if any(ds in q for ds in ds_words):
        intent_scores['ALGORITHM_PUZZLE'] += 1
    
    if any(x in q for x in ['dynamic programming', 'sliding window', 'backtracking', 'greedy']):
        intent_scores['ALGORITHM_PUZZLE'] += 2
    
    if any(x in q for x in ['minimum', 'maximum', 'shortest', 'longest']) and 'number of' in q:
        intent_scores['ALGORITHM_PUZZLE'] += 1
    
    # Score SYNTAX_RECALL intent
    if any(x in q for x in ['select', 'join', 'group by', 'where']) and 'write' in q:
        intent_scores['SYNTAX_RECALL'] += 2
    
    # Score MATH_PROOF intent
    if any(x in q for x in ['prove', 'derive', 'show that', 'demonstrate']):
        intent_scores['MATH_PROOF'] += 2
    
    # Decision: Reject if any intent score >= 2
    max_intent = max(intent_scores.items(), key=lambda x: x[1])
    if max_intent[1] >= 2:
        return (True, f"Intent detected: {max_intent[0]} (score: {max_intent[1]})")
    
    return (False, "No reject intent detected")
```

---

### BOUNDARY CLARIFICATIONS

**SQL: Syntax vs Reasoning**
- ❌ "Write a SQL query to find top 3 salaries" → 🔴 (syntax)
- ✅ "How would you compute top 3 salaries per department?" → 🟡 (conceptual)

**System Design: Implementation vs Conceptual**
- ❌ "Design and implement a rate limiter" → 🔴 (implementation)
- ✅ "What high-level components would a rate limiter need?" → 🟡 (conceptual)

**Behavioral: Past Story vs Framework**
- ❌ "Tell me about a time you handled conflict" → 🔴 (past story)
- ✅ "Stakeholders disagree on priorities — what do you do?" → 🟢 (framework)

---

**If LAYER 1 OR LAYER 2 triggers → 🔴 IGNORE (do not proceed to Step 2)**

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
Primary_Pattern: {Pattern name or "N/A"}
Secondary_Pattern: {Optional - only if relevant}
Reasoning: {1 sentence why}
Confidence: High | Medium | Low
```

**Example:**

```
Question ID: 42
Question: Amazon orders are down 25% — what do you do?
Bucket: 🟢
Primary_Pattern: Pattern_1_Metric_Drop
Secondary_Pattern: LHF_1_Data_Trust (if data quality is mentioned)
Reasoning: Matches metric drop keywords, no code required, reasoning-first
Confidence: High
```

**Note on Secondary Patterns:**
- Optional field — only add if question clearly involves a secondary concern
- Example: "Orders down 25% — how would you check if the data is trustworthy?" 
  - Primary: 🟢 Pattern_1_Metric_Drop
  - Secondary: 🟡 LHF_1_Data_Trust
- Keeps bucketing simple (3 buckets) but adds instructive detail

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
