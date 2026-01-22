# Executive Study Plan: L13 - SQL Reasoning (Conceptual)
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~20 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L13 (SQL REASONING) QUESTIONS

**Even when "SQL" isn't mentioned, look for these keywords/phrases:**

### Explicit SQL Keywords:
- "SQL", "query", "how would you compute", "how would you calculate", "write a query"
- "data analysis", "aggregate", "join", "filter", "group by", "conceptual SQL"
- "employee earnings", "revenue by segment", "user retention", "conversion rate"

### Implicit L13 Indicators:
- **Computation questions:** "How would you compute X?", "How would you calculate Y?", "What query would you write?"
- **Data analysis questions:** "How do you analyze X?", "How do you measure Y?", "What metrics would you calculate?"
- **Conceptual questions:** "How would you think about computing X?" (No actual SQL code, just reasoning)

### L13 vs L7 Distinction:
- **L13 (SQL Reasoning):** "How would you compute weekly active users?" → Focus: Conceptual SQL reasoning (Grain, join, filter, aggregate)
- **L7 (Data Modeling):** "Design a data warehouse schema" → Focus: How to structure data (Entities, relationships, grain, validate)

### L13 vs P1 Distinction:
- **L13 (SQL Reasoning):** "How would you compute X?" → Focus: How to calculate a metric
- **P1 (Metric Drop):** "Orders down 25%" → Focus: WHERE is drop coming from? (Segment to find hot spot)

### Red Flags (NOT L13):
- "Design a data warehouse schema" → L7 (Data Modeling)
- "Orders down 25%" → P1 (Metric Drop)
- "How do you define success?" → P2 (NSM + KPI Ladder)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **SQL Reasoning Framework** (HIGHEST PRIORITY)
2. ⚠️ **Query Design** (MEDIUM)

**For Data Engineer:**
1. ✅ **SQL Reasoning Framework** (HIGHEST) - Core framework
2. ✅ **Query Design** (HIGH) - Practical application

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: SQL Reasoning Framework
**Questions:** ~15 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "How would you compute X?" or "What query would you write?" - core SQL reasoning framework
- **Framework:** Define Output → Conceptual Join → Filter Logic → Aggregation Logic → Edge Cases & Validation
- **Define Output:** What is the final table? (Grain: one row per what? - user/order/day/experiment/cohort, Columns: metrics + dimensions, Time window: last 7d, 30d, all-time), Rule: If you can't say the grain, you don't understand the query
- **Conceptual Join:** What data must come together? (Fact table: events, orders, transactions, Dimension tables: users, products, dates, Join keys: user_id, order_id, product_id, Join type: INNER → only matched rows, LEFT → keep base table intact), Rule: Pick the BASE table first, then join outward
- **Filter Logic:** Which rows count? (Time filters: event_date BETWEEN …, Status filters: completed, paid, active, Segment filters: country, platform, plan, Exclusions: test users, refunds, bots), Rule: Filters change meaning — say them explicitly
- **Aggregation Logic:** How are numbers computed? (Count vs count distinct, Sum vs average, Group by which dimensions?, Order of ops: Filter → Join → Aggregate), Rule: Aggregation happens at the grain, not before
- **Edge Cases & Validation:** Check for issues (Duplicates after joins?, Missing data?, Null handling?, Sanity checks - back-of-envelope)

**Concrete Examples:**
- "Weekly active users by country: Output (One row per week, country, Metric: distinct active users), Join (Base: events table, Join users table on user_id to get country), Filter (Event type = activity, Date within week), Aggregate (COUNT(DISTINCT user_id), GROUP BY week, country)"
- "SQL reasoning: Define output grain, identify joins, specify filters, determine aggregation, validate"

**Representative Questions (Do 5 only):**
- Q736: Employee Earnings. (SQL query/employee data angle)
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (data analysis/SQL reasoning angle)
- Q117: As the PM for Lyft, what dashboard would you build to track the health of the app? (metrics/SQL reasoning angle)
- Q183: Debug a metric that was off by x percentage. (data analysis/SQL reasoning angle)
- Q790: Explain data drifting. (data analysis/SQL reasoning angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Output → Conceptual Join → Filter Logic → Aggregation Logic → Edge Cases & Validation`

**Memorizable Answer:**

When reasoning about SQL queries, I use Define Output → Conceptual Join → Filter Logic → Aggregation Logic → Edge Cases & Validation.

**1️⃣ Define Output** → What is the final table?
  - **Grain:** One row per what? (User/order/day/experiment/cohort - what does one row represent?)
  - **Columns:** Metrics + dimensions (what metrics do we need? What dimensions to group by?)
  - **Time window:** Last 7d, 30d, all-time (what time period are we analyzing?)

**Rule:** If you can't say the grain, you don't understand the query.

**2️⃣ Conceptual Join** → What data must come together?
  - **Fact table:** Events, orders, transactions (what is the base table with the metrics?)
  - **Dimension tables:** Users, products, dates (what tables provide context or attributes?)
  - **Join keys:** user_id, order_id, product_id (what columns link the tables together?)
  - **Join type:** INNER (only matched rows), LEFT (keep base table intact)

**Rule:** Pick the BASE table first, then join outward.

**3️⃣ Filter Logic** → Which rows count?
  - **Time filters:** event_date BETWEEN …, date >= … (what time period are we filtering?)
  - **Status filters:** Completed, paid, active (what status or state conditions?)
  - **Segment filters:** Country, platform, plan (what demographic or segment filters?)
  - **Exclusions:** Test users, refunds, bots (what should we exclude?)

**Rule:** Filters change meaning — say them explicitly.

**4️⃣ Aggregation Logic** → How are numbers computed?
  - **Count vs count distinct:** COUNT(*) counts all rows, COUNT(DISTINCT column) counts unique values
  - **Sum vs average:** SUM for totals, AVG for averages (what aggregation function is appropriate?)
  - **Group by:** Which dimensions? (what columns determine the grain of the output?)
  - **Order of ops:** Filter → Join → Aggregate (filter before aggregating to avoid double counting)

**Rule:** Aggregation happens at the grain, not before.

**5️⃣ Edge Cases & Validation** → 
  - **Duplicates after joins?** Do joins create duplicate rows that will inflate counts?
  - **Missing data?** Are there NULL values that need handling?
  - **Null handling?** How do we handle NULLs in aggregations?
  - **Sanity checks:** Back-of-envelope - do the numbers make sense?

**Output:** "One row per X, joined with Y, filtered by Z, aggregated as W."

**Key Principle:** Start by defining the grain. The base table should be events, everything else decorates it. Filter before aggregating to avoid double counting. This metric is sensitive to join duplication, so sanity-check.

---

**How to Adapt This Narrative for Each Question:**

- **Q736 (Employee Earnings):** Focus on SQL reasoning
  - "Define Output: Grain (one row per employee or employee + time period if needed), Columns (employee ID, name, total earnings, dimensions - department, role, time period), Time window (all-time or specific period)"
  - "Conceptual Join: Base table (payroll/earnings table - fact table with earnings data), Dimension tables (employees table - employee attributes, Departments table - department info), Join keys (employee_id), Join type (INNER to get employees with earnings, LEFT if we want all employees)"
  - "Filter Logic: Time filters (if time period specified, filter by date), Status filters (active employees only? Include terminated?), Segment filters (specific departments? Roles?), Exclusions (test employees, contractors?)"
  - "Aggregation Logic: If one row per employee (SUM(earnings) GROUP BY employee_id), If by time period (SUM(earnings) GROUP BY employee_id, time_period), Count vs count distinct (COUNT(DISTINCT employee_id) for unique employees), Order (filter → Join → Aggregate)"
  - "Edge Cases: Duplicates (check if joins create duplicates), Missing data (handle NULL earnings), Null handling (use COALESCE or exclude NULLs), Sanity checks (do earnings make sense? Compare to expected ranges)"
  - "Structure: SELECT employee_id, employee_name, SUM(earnings) as total_earnings FROM earnings_table e JOIN employees emp ON e.employee_id = emp.employee_id WHERE [filters] GROUP BY employee_id, employee_name"

- **Q110 (Gas station surge analysis):** Emphasize data analysis reasoning
  - "Define Output: Grain (one row per time period - hour/day), Columns (customer count, metrics - revenue, transactions, dimensions - time, location), Time window (last week vs normal period)"
  - "Conceptual Join: Base table (transactions/visits table), Dimension tables (time table - for time analysis, Location table - if multiple locations), Join keys (transaction_id, time_id), Join type (INNER)"
  - "Filter Logic: Time filters (peak times vs off-peak, compare periods), Status filters (completed transactions only), Segment filters (all customers or segments?), Exclusions (test transactions, errors?)"
  - "Aggregation Logic: Count (COUNT(DISTINCT customer_id) for unique customers), Sum (SUM(revenue) for total revenue), Group by (time period - hour/day), Order (filter → Join → Aggregate)"
  - "Edge Cases: Duplicates (check for duplicate transactions), Missing data (handle missing timestamps), Null handling (exclude NULL customer_ids), Sanity checks (does 4x make sense? Compare to historical)"
  - "Compute: Customer count by time period, compare peak vs normal, identify cause of surge"

---

### BUCKET 2: Query Design
**Questions:** ~5 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Design a query for X" or "How would you structure a query?" - same framework, with focus on query structure
- **Approach:** Same SQL reasoning framework, with focus on query design patterns
- **Query Patterns:** Aggregation queries, Join queries, Time-series queries, Cohort queries
- **Design Principles:** Start with grain, Filter before aggregating, Avoid double counting, Handle nulls

**Concrete Examples:**
- "Aggregation query: Define grain (one row per X), Join tables, Filter rows, Aggregate metrics, Validate"
- "Query design: Start with output grain, identify data needed, specify filters, determine aggregation"

**Representative Questions (Do 5 only):**
- Q736: Employee Earnings. (query design angle)
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (query design angle)
- Q117: As the PM for Lyft, what dashboard would you build to track the health of the app? (query design angle)
- Q183: Debug a metric that was off by x percentage. (query design angle)
- Q790: Explain data drifting. (query design angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Output → Conceptual Join → Filter Logic → Aggregation Logic → Edge Cases (Query Design Focus)`

**Memorizable Answer:**

When designing queries, I use the same SQL reasoning framework but focus on query structure.

**1️⃣ Start with Output** → Define grain clearly (one row per X), Specify columns (metrics + dimensions), Set time window.

**2️⃣ Identify Data Needed** → Fact tables (base data), Dimension tables (context), Join strategy (which tables? What keys? What type?).

**3️⃣ Specify Filters** → Time, status, segments, exclusions.

**4️⃣ Determine Aggregation** → Count vs count distinct, Sum vs average, Group by dimensions.

**5️⃣ Validate** → Check for duplicates, handle nulls, sanity check.

**Key Principle:** Start with the grain and work backwards. Filter before aggregating to avoid double counting.

---

**How to Adapt This Narrative for Each Question:**

- **Q736 (Employee earnings query):** Already covered in Bucket 1.

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **SQL Reasoning Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Query Design** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through SQL reasoning framework in 2 minutes (Define Output → Conceptual Join → Filter Logic → Aggregation Logic → Edge Cases)
- [ ] Define output (Grain, columns, time window)
- [ ] Identify joins (Base table, dimension tables, join keys, join type)
- [ ] Specify filters (Time, status, segments, exclusions)
- [ ] Determine aggregation (Count vs count distinct, sum vs average, group by)
- [ ] Validate (Duplicates, nulls, sanity checks)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the SQL reasoning framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Define Output → Conceptual Join → Filter Logic → Aggregation Logic → Edge Cases framework**, not memorizing answers

**Remember:** L13 is about SQL reasoning (conceptual, not code). The framework: Define Output → Conceptual Join → Filter Logic → Aggregation Logic → Edge Cases. Key principles: If you can't say the grain, you don't understand the query. Pick the BASE table first, then join outward. Filter before aggregating to avoid double counting. Aggregation happens at the grain, not before.
