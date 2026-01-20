# L13 - SQL Reasoning (Conceptual)

**Formula:** `Conceptual Join → Aggregation Logic → Filter Logic → Output`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "How would you compute X?"
(no SQL syntax, no code — thinking only)
│
├─ 1) Define the OUTPUT (WHAT is the final table?)
│   │
│   ├─ Grain: one row per what?
│   │   (user / order / day / experiment / cohort)
│   ├─ Columns: metrics + dimensions
│   └─ Time window: last 7d, 30d, all-time
│
│   ⚠ Rule: If you can't say the grain, you don't understand the query
│
├─ 2) Conceptual JOIN (WHAT data must come together?)
│   │
│   ├─ Fact table (events, orders, transactions)
│   ├─ Dimension tables (users, products, dates)
│   ├─ Join keys (user_id, order_id, product_id)
│   └─ Join type:
│       ├─ INNER → only matched rows
│       ├─ LEFT → keep base table intact
│
│   ⚠ Rule: Pick the BASE table first, then join outward
│
├─ 3) Filter Logic (WHICH rows count?)
│   │
│   ├─ Time filters (event_date BETWEEN …)
│   ├─ Status filters (completed, paid, active)
│   ├─ Segment filters (country, platform, plan)
│   └─ Exclusions (test users, refunds, bots)
│
│   ⚠ Rule: Filters change meaning — say them explicitly
│
├─ 4) Aggregation Logic (HOW are numbers computed?)
│   │
│   ├─ Count vs count distinct
│   ├─ Sum vs average
│   ├─ Group by which dimensions?
│   └─ Order of ops:
│       Filter → Join → Aggregate
│
│   ⚠ Rule: Aggregation happens at the grain, not before
│
├─ 5) Edge Cases & Validation
│   │
│   ├─ Duplicates after joins?
│   ├─ Missing data?
│   ├─ Null handling?
│   └─ Sanity checks (back-of-envelope)
│
└─ OUTPUT: "One row per X, joined with Y, filtered by Z,
           aggregated as W."
```

---

## 📌 Canonical Example: Weekly Active Users by Country

**Question:**
"How would you compute weekly active users by country?"

```
Output
├─ One row per (week, country)
├─ Metric: distinct active users

Join
├─ Base: events table
├─ Join users table on user_id to get country

Filter
├─ Event type = activity
├─ Date within week

Aggregate
├─ COUNT(DISTINCT user_id)
├─ GROUP BY week, country
```

---

## 🚨 Common SQL Reasoning Traps

```
| Trap                    | Why It's Wrong                          |
|-------------------------|-----------------------------------------|
| No grain                | Leads to wrong aggregation              |
| Join before filtering   | Inflates counts                         |
| COUNT(*) blindly        | Duplicate rows after join               |
| Ignoring nulls          | Silent metric distortion                |
| SQL-first thinking      | Syntax ≠ correctness                    |
```

---

## 💬 Interview One-Liners

* "I'll start by defining the grain."
* "The base table should be events, everything else decorates it."
* "I'd filter before aggregating to avoid double counting."
* "This metric is sensitive to join duplication, so I'd sanity-check."

---

## 🔑 5-Second Recall

```
Grain → Join → Filter → Aggregate → Validate
```

If you want, next we can:

* Drill **L13 vs coding SQL questions (how to spot traps)**
* Run **rapid-fire L1–L13 recall**
* Map **L13 answers to real FAANG interview questions**
