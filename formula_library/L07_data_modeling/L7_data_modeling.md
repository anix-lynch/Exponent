# L7 - Data Modeling

**Formula:** `Entities → Relationships → Metrics → Grain → Validate`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "How should this data be structured to answer decisions?"
│
├─ 1) Entities (WHAT things exist?)
│   │
│   ├─ Core nouns in the business
│   │   ├─ User
│   │   ├─ Order
│   │   ├─ Product
│   │   ├─ Session
│   │   └─ Event
│   │
│   └─ Rule: If it has its own lifecycle → entity
│
├─ 2) Relationships (HOW do they connect?)
│   │
│   ├─ One-to-one
│   ├─ One-to-many
│   └─ Many-to-many
│
│   Examples
│   ├─ User → Orders (1:N)
│   ├─ Order ↔ Products (M:N via Order_Items)
│   └─ User → Sessions (1:N)
│
├─ 3) Metrics (WHAT do we measure?)
│   │
│   ├─ Counts
│   │   ├─ # orders
│   │   ├─ # sessions
│   │   └─ # users
│   │
│   ├─ Sums
│   │   ├─ Revenue
│   │   └─ Spend
│   │
│   └─ Ratios
│       ├─ Conversion rate
│       └─ Retention
│
│   ⚠ Rule: Metrics live on facts, not dimensions
│
├─ 4) Grain (WHAT does one row represent?)
│   │
│   ├─ One row per:
│   │   ├─ Event
│   │   ├─ Session
│   │   ├─ Order
│   │   └─ User-day
│   │
│   ⚠ Rule: Never mix grains in one table
│
├─ 5) Validate (CAN we answer the question?)
│   │
│   ├─ Can we compute metrics without double-counting?
│   ├─ Do joins stay clean?
│   ├─ Does aggregation feel natural?
│   └─ Do edge cases break it?
│
└─ OUTPUT: Clean Fact + Dimension model
```

---

## 📊 Canonical Shapes

```
FACT tables (things that happen)
├─ fact_events (event_id, user_id, ts, event_type)
├─ fact_orders (order_id, user_id, revenue, ts)
└─ fact_sessions (session_id, user_id, duration)

DIM tables (descriptions)
├─ dim_users (user_id, country, signup_date)
├─ dim_products (product_id, category, price)
└─ dim_time (date, week, month)
```

---

## 🚨 Anti-Patterns (Instant Red Flags)

```
✗ Metric columns inside dimension tables
✗ One table doing everything
✗ Multiple grains mixed
✗ Pre-aggregated numbers with no raw facts
✗ "Just denormalize everything" with no reason
```

---

## 📌 Interview Example: E-Commerce Data Model

**Question:**
"How would you model data for an e-commerce company?"

```
Entities
├─ Users, Products, Orders, Sessions
Relationships
├─ User → Orders
├─ Order → Products
Metrics
├─ Revenue, Orders, Conversion
Grain
├─ fact_orders: 1 row per order
Validate
└─ Can compute daily revenue & user cohorts
```

---

## 💬 One-Liners You Can Drop

* "Grain is the most important decision."
* "Facts store metrics; dimensions store context."
* "If joins feel painful, the model is wrong."
* "Model for questions, not for storage."

---

## 🔑 5-Second Recall

```
What exists?
→ How they connect
→ What we measure
→ One row means what?
→ Can we answer questions cleanly?
```

Next up if you want:
• **L8 – Market / Competitive**
• **L9 – Financial Sensitivity**
• or compress **L7** into a **15-second spoken answer** for interviews.
