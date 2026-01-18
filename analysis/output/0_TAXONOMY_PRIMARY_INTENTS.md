# PRIMARY INTENTS - The 9 Universal Question Types

**Purpose:** Stable classification layer that captures what the interviewer is really testing

**Key Principle:** One question = ONE primary intent (no mixing)

---

## The 9 Primary Intents

### 1️⃣ DIAGNOSE_METRICS

**Definition:** Investigate why a metric changed (dropped, spiked, or shifted)

**Pattern:** "X is down/up by Y%, what happened?"

**What they're testing:** Root cause analysis, structured thinking, data intuition

**Examples:**
- ✅ "Amazon orders are down 25% — what do you do?"
- ✅ "Google searches dropped 35% — diagnose it"
- ✅ "Churn increased 40% — find the cause"

**NOT this intent:**
- ❌ "How would you improve retention?" (that's GROWTH_STRATEGY)
- ❌ "What metrics would you track?" (that's DEFINE_SUCCESS)

---

### 2️⃣ DEFINE_SUCCESS

**Definition:** Choose the right metrics/KPIs/OKRs and explain why

**Pattern:** "How would you measure success for X?"

**What they're testing:** Business judgment, metric selection, understanding of levers

**Examples:**
- ✅ "How would you define success for Airbnb Experiences?"
- ✅ "What's the North Star Metric for Instagram Reels?"
- ✅ "How many ads should Yelp show users?"

**NOT this intent:**
- ❌ "Revenue dropped 20%" (that's DIAGNOSE_METRICS)
- ❌ "How would you increase revenue?" (that's GROWTH_STRATEGY)

---

### 3️⃣ PRIORITIZE_TRADEOFFS

**Definition:** Choose between competing options with constraints

**Pattern:** "Should we do A or B?" / "How would you prioritize X, Y, Z?"

**What they're testing:** Decision framework, tradeoff reasoning, 2nd-order thinking

**Examples:**
- ✅ "Pagination vs infinite scroll on a job board?"
- ✅ "How prioritize when everything is urgent?"
- ✅ "Should we add ads or keep the experience clean?"

**NOT this intent:**
- ❌ "How would you grow users?" (that's GROWTH_STRATEGY)
- ❌ "Tell me about a time you prioritized" (that's BEHAVIORAL_LEADERSHIP)

---

### 4️⃣ GROWTH_STRATEGY

**Definition:** Increase acquisition, retention, monetization, or expand into new markets

**Pattern:** "How would you increase/grow/expand X?"

**What they're testing:** Strategic thinking, growth levers, market understanding

**Examples:**
- ✅ "How would you increase Amazon Prime revenue by 20%?"
- ✅ "Should Uber expand into Uber Eats?"
- ✅ "How would Notion expand into Europe?"

**NOT this intent:**
- ❌ "Revenue is down 20%" (that's DIAGNOSE_METRICS)
- ❌ "What metrics for growth?" (that's DEFINE_SUCCESS)

---

### 5️⃣ EXPERIMENT_CAUSALITY

**Definition:** Design A/B tests, interpret results, understand causal inference

**Pattern:** "How would you test X?" / "Is this experiment result valid?"

**What they're testing:** Statistical rigor, experimental design, avoiding false conclusions

**Examples:**
- ✅ "How would you A/B test a new checkout flow?"
- ✅ "Conversion increased 10% in test group — is it causal?"
- ✅ "What are the pitfalls of this experiment design?"

**NOT this intent:**
- ❌ "How would you measure success?" (that's DEFINE_SUCCESS)
- ❌ "Conversion dropped 10%" (that's DIAGNOSE_METRICS)

---

### 6️⃣ EXEC_COMMUNICATION

**Definition:** Communicate insights, recommendations, or bad news to executives/stakeholders

**Pattern:** "How would you present X to leadership?"

**What they're testing:** Executive presence, clarity, storytelling, influence

**Examples:**
- ✅ "How would you communicate complex topics to executives?"
- ✅ "How would you deliver bad news upward?"
- ✅ "Present your recommendation to the CEO"

**NOT this intent:**
- ❌ "Tell me about a time you influenced" (that's BEHAVIORAL_LEADERSHIP)
- ❌ "How do you work with stakeholders?" (that's EXECUTION_DELIVERY)

---

### 7️⃣ EXECUTION_DELIVERY

**Definition:** Plan, execute, unblock, manage risk, deliver projects

**Pattern:** "How would you execute/deliver/manage X?"

**What they're testing:** Project management, risk mitigation, operational excellence

**Examples:**
- ✅ "How would you handle scheduling dependencies between nightly jobs?"
- ✅ "A cross-functional team is moving slowly — what do you do?"
- ✅ "How would you restructure a program that's gone through many changes?"

**NOT this intent:**
- ❌ "Tell me about a time you delivered a project" (that's BEHAVIORAL_LEADERSHIP)
- ❌ "How would you grow users?" (that's GROWTH_STRATEGY)

---

### 8️⃣ TECH_FOUNDATIONS

**Definition:** Write SQL, design systems, build data pipelines, code algorithms

**Pattern:** "Write a query..." / "Design a system..." / "Implement X..."

**What they're testing:** Technical skills, system design, coding ability

**Examples:**
- ✅ "Write a query to find the top 3 salaries per department"
- ✅ "Design a data pipeline for Alexa user requests"
- ✅ "Reverse a linked list"

**NOT this intent:**
- ❌ "How would you design a product?" (that's GROWTH_STRATEGY or PRIORITIZE_TRADEOFFS)
- ❌ "Explain SQL vs NoSQL" (concept question, not technical execution)

---

### 9️⃣ BEHAVIORAL_LEADERSHIP

**Definition:** Past stories demonstrating judgment, conflict resolution, failure, influence

**Litmus test:** Cannot answer without saying "Here's a specific time when..."

**What they're testing:** Self-awareness, maturity, ownership, values

**Examples:**
- ✅ "Tell me about a time you disagreed with a stakeholder"
- ✅ "Describe a project that failed"
- ✅ "How did you handle conflict with your team?"

**NOT this intent:**
- ❌ "How do you prioritize tasks?" (that's PRIORITIZE_TRADEOFFS)
- ❌ "How do you communicate with executives?" (that's EXEC_COMMUNICATION)
- ❌ "What's your leadership style?" (abstract, not a story)

---

## Conflict Resolution Rules

**When a question could fit multiple intents:**

1. **Diagnostic > Strategy**
   - "Revenue is down, how fix?" → DIAGNOSE_METRICS (find cause first)
   
2. **Behavioral > Everything**
   - If it asks for a past story, it's BEHAVIORAL_LEADERSHIP (even if about metrics)

3. **Tech > Abstract**
   - "Write a query" → TECH_FOUNDATIONS (not DEFINE_SUCCESS)

4. **Experiment > Metrics**
   - "How test X?" → EXPERIMENT_CAUSALITY (not DEFINE_SUCCESS)

5. **Default to most specific**
   - When unclear, pick the intent that requires the most specific framework

---

## Why This Works

**Stable:** 9 intents won't change (unlike 109 categories)

**Mutually Exclusive:** Every question has ONE primary intent

**Actionable:** Each intent maps to a specific answer framework

**Universal:** Works across all roles (PM, Analyst, Engineer, BizOps, etc.)

---

## Next Step

Use these 9 intents to classify ALL_QUESTIONS_RAW.md → then build the 12 North Star Patterns
