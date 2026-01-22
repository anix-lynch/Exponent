# Executive Study Plan: L7 - Data Modeling
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~10 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L7 (DATA MODELING) QUESTIONS

**Even when "data modeling" isn't mentioned, look for these keywords/phrases:**

### Explicit Data Modeling Keywords:
- "data model", "data modeling", "schema", "data warehouse", "database design"
- "fact table", "dimension table", "star schema", "grain", "entities", "relationships"
- "design schema", "design data warehouse", "data structure"

### Implicit L7 Indicators:
- **Schema questions:** "Design a data warehouse schema for X", "How would you model data for X?"
- **Data structure questions:** "How should data be structured?", "What tables would you create?"
- **Entity questions:** "What entities exist?", "How do entities relate?"

### L7 vs L1 Distinction:
- **L7 (Data Modeling):** "Design a data warehouse schema" → Focus: How to structure data (Entities, relationships, grain)
- **L1 (Data Trust):** "Debug a metric that was off" → Focus: Is data trustworthy? (Source, freshness, completeness)

### L7 vs P12 Distinction:
- **L7 (Data Modeling):** "Design a data warehouse schema" → Focus: Data structure design
- **P12 (Operational Excellence):** "How do you ensure system reliability?" → Focus: Operational process

### Red Flags (NOT L7):
- "How do you debug a metric?" → L1 (Data Trust)
- "How do you ensure data quality?" → L1 (Data Trust)
- "How do you query data?" → L13 (SQL Reasoning)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Data Modeling Framework** (HIGHEST PRIORITY)
2. ⚠️ **Schema Design** (MEDIUM)

**For Data Engineer:**
1. ✅ **Data Modeling Framework** (HIGHEST) - Core framework
2. ✅ **Schema Design** (HIGH) - Practical application

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Data Modeling Framework
**Questions:** ~8 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Design a data warehouse schema for X" or "How would you model data for X?" - core data modeling framework
- **Framework:** Entities → Relationships → Metrics → Grain → Validate
- **Entities:** Core nouns in the business (User, Order, Product, Session, Event), Rule: If it has its own lifecycle → entity
- **Relationships:** One-to-one (single relationship), One-to-many (parent-child), Many-to-many (requires junction table), Examples (User → Orders 1:N, Order ↔ Products M:N via Order_Items)
- **Metrics:** Counts (# orders, # sessions, # users), Sums (Revenue, Spend), Ratios (Conversion rate, Retention), Rule: Metrics live on facts, not dimensions
- **Grain:** What does one row represent? (One row per: Event, Session, Order, User-day), Rule: Never mix grains in one table, Grain is the most important decision
- **Validate:** Can we compute metrics without double-counting? Do joins stay clean? Does aggregation feel natural? Do edge cases break it?

**Concrete Examples:**
- "E-commerce data model: Entities (Users, Products, Orders, Sessions), Relationships (User → Orders 1:N, Order → Products M:N), Metrics (Revenue, Orders, Conversion), Grain (fact_orders: 1 row per order), Validate (Can compute daily revenue & user cohorts)"
- "Data modeling: Identify entities, define relationships, specify metrics, choose grain, validate model"

**Representative Questions (Do 5 only):**
- Q279: Design a color propensity model for sponsored products ads at Amazon. (ML model/data modeling angle)
- Q289: Design a Data Warehouse Schema for a Ride-Sharing Service. (data warehouse design angle)
- Q290: Design a Data Warehouse Schema for Airbnb. (data warehouse design angle)
- Q291: Design a data warehouse schema for Amazon. (data warehouse design angle)
- Q292: Design a data warehouse schema for an e-commerce company. (data warehouse design angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When designing a data model, I use Entities → Relationships → Metrics → Grain → Validate. First, I identify Entities: Core nouns in the business (User, Order, Product, Session, Event - things that exist in the business), Rule: If it has its own lifecycle → entity (each entity represents a distinct business concept with its own attributes and lifecycle). Second, I define Relationships: One-to-one (single relationship - e.g., User → Profile), One-to-many (parent-child - e.g., User → Orders, User → Sessions), Many-to-many (requires junction table - e.g., Order ↔ Products via Order_Items), Examples (User → Orders 1:N, Order → Order_Items 1:N, Order_Items → Product M:N via Order_Items). Design relationships to support efficient queries and avoid data redundancy. Third, I specify Metrics: Counts (# orders, # sessions, # users, # events), Sums (Revenue, Spend, Total amount), Ratios (Conversion rate, Retention rate, Average order value). Rule: Metrics live on facts (fact tables), not dimensions. Facts store metrics; dimensions store context. Fourth, I choose Grain: What does one row represent? One row per: Event, Session, Order, User-day, Transaction. Rule: Never mix grains in one table. Grain is the most important decision - it determines what questions you can answer. Example: fact_orders table = 1 row per order, fact_sessions table = 1 row per session. Model for questions, not for storage. Finally, I Validate: Can we compute metrics without double-counting? Check aggregation logic. Do joins stay clean? Verify relationships support efficient queries. Does aggregation feel natural? Can we easily roll up by time, user, product, etc.? Do edge cases break it? Test with nulls, duplicates, orphaned records. Output: Clean Fact + Dimension model. FACT tables: things that happen (events, orders, sessions). DIM tables: descriptions (users, products, time). The key principle: If joins feel painful, the model is wrong."

**How to Adapt This Narrative for Each Question:**

- **Q289 (Ride-sharing data warehouse):** Focus on ride-sharing context → "To design a data warehouse for ride-sharing, I'd: Entities (Core nouns: User (rider), Driver, Trip, Vehicle, Payment - each has its own lifecycle), Relationships (User → Trips 1:N - one user can have many trips, Driver → Trips 1:N - one driver can have many trips, Trip → Payment 1:1 - one trip has one payment, Trip → Vehicle 1:1 - one trip uses one vehicle), Metrics (Counts: # trips, # users, # drivers, Sums: Revenue (sum of trip fares), Total distance, Ratios: Average trip distance, Conversion rate (completed trips / requested trips)), Grain (fact_trips: 1 row per trip - trip_id, user_id, driver_id, vehicle_id, fare, distance, duration, timestamp, fact_events: 1 row per event - event_id, trip_id, event_type (request, accept, start, complete, cancel), timestamp, dim_users: user attributes, dim_drivers: driver attributes, dim_vehicles: vehicle attributes, dim_time: time dimensions), Validate (Can compute: Daily trip count, Revenue by driver, User retention, Average trip distance, Joins: Clean joins between fact_trips and dim tables, Aggregation: Can roll up by time, user, driver, vehicle, Edge cases: Handle cancelled trips, null values, duplicates). I'd design: fact_trips (trip_id, user_id, driver_id, vehicle_id, fare, distance, duration, start_time, end_time), dim_users (user_id, signup_date, city, user_type), dim_drivers (driver_id, signup_date, city, vehicle_type), dim_vehicles (vehicle_id, make, model, year), dim_time (date, week, month, year)."

- **Q290 (Airbnb data warehouse):** Emphasize marketplace context → "To design a data warehouse for Airbnb, I'd: Entities (Core nouns: User (guest/host), Listing, Booking, Review, Payment - each has its own lifecycle), Relationships (User → Bookings 1:N - one user can have many bookings, User → Listings 1:N - one host can have many listings, Listing → Bookings 1:N - one listing can have many bookings, Booking → Review 1:1 - one booking has one review, Booking → Payment 1:1 - one booking has one payment), Metrics (Counts: # bookings, # listings, # users, Sums: Revenue (sum of booking amounts), Total nights booked, Ratios: Occupancy rate, Average booking value, Conversion rate), Grain (fact_bookings: 1 row per booking - booking_id, guest_id, host_id, listing_id, check_in, check_out, nights, revenue, timestamp, fact_events: 1 row per event - event_id, booking_id, event_type (search, view, book, cancel), timestamp, dim_users: user attributes, dim_listings: listing attributes, dim_time: time dimensions), Validate (Can compute: Daily bookings, Revenue by listing, Host performance, Guest retention, Joins: Clean joins, Aggregation: Can roll up by time, user, listing, city, Edge cases: Handle cancelled bookings, null values). I'd design: fact_bookings (booking_id, guest_id, host_id, listing_id, check_in, check_out, nights, revenue, booking_date), dim_users (user_id, signup_date, city, user_type), dim_listings (listing_id, host_id, city, property_type, price_per_night), dim_time (date, week, month, year)."

---

### BUCKET 2: Schema Design
**Questions:** ~2 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Design schema for X" or "Data warehouse design" - same framework, with focus on schema structure
- **Approach:** Same data modeling framework, with focus on fact and dimension tables
- **Schema Structure:** FACT tables (things that happen: events, orders, sessions), DIM tables (descriptions: users, products, time)
- **Design Principles:** Grain consistency, Clean joins, Efficient aggregation, Avoid anti-patterns

**Concrete Examples:**
- "Star schema: fact_orders (order_id, user_id, product_id, revenue, timestamp), dim_users (user_id, country, signup_date), dim_products (product_id, category, price), dim_time (date, week, month)"
- "Schema design: Fact tables for metrics, dimension tables for context, clean relationships"

**Representative Questions (Do 5 only):**
- Q289: Design a Data Warehouse Schema for a Ride-Sharing Service. (schema design angle)
- Q290: Design a Data Warehouse Schema for Airbnb. (schema design angle)
- Q291: Design a data warehouse schema for Amazon. (schema design angle)
- Q292: Design a data warehouse schema for an e-commerce company. (schema design angle)
- Q279: Design a color propensity model for sponsored products ads at Amazon. (ML model/schema angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When designing schemas, I use the same data modeling framework but focus on schema structure. I design FACT tables: Things that happen (fact_events: event_id, user_id, ts, event_type, fact_orders: order_id, user_id, revenue, ts, fact_sessions: session_id, user_id, duration). I design DIM tables: Descriptions (dim_users: user_id, country, signup_date, dim_products: product_id, category, price, dim_time: date, week, month). I ensure: Grain consistency (Never mix grains in one table), Clean joins (Relationships support efficient queries), Efficient aggregation (Can roll up by time, user, product easily), Avoid anti-patterns (No metric columns in dimension tables, No one table doing everything, No multiple grains mixed, No pre-aggregated numbers with no raw facts, No 'just denormalize everything' with no reason). The key is designing for questions, not for storage."

**How to Adapt This Narrative for Each Question:**

- **Q291 (Amazon data warehouse):** Focus on e-commerce schema → "To design Amazon's data warehouse schema, I'd: FACT tables (fact_orders: order_id, user_id, order_date, revenue, items_count, fact_events: event_id, user_id, product_id, event_type (view, add_to_cart, purchase), timestamp, fact_sessions: session_id, user_id, start_time, end_time, page_views), DIM tables (dim_users: user_id, signup_date, country, user_segment, dim_products: product_id, category, price, brand, dim_time: date, week, month, year, dim_categories: category_id, category_name, parent_category), Design principles (Grain: fact_orders = 1 row per order, fact_events = 1 row per event, Clean joins: Foreign keys to dim tables, Efficient aggregation: Can roll up by time, user, product, category, Avoid anti-patterns: No metrics in dim tables, no mixed grains). I'd design: fact_orders (order_id, user_id, order_date, revenue, items_count), fact_events (event_id, user_id, product_id, event_type, timestamp), dim_users (user_id, signup_date, country), dim_products (product_id, category, price), dim_time (date, week, month, year)."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Data Modeling Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Schema Design** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through data modeling framework in 2 minutes (Entities → Relationships → Metrics → Grain → Validate)
- [ ] Identify entities (Core nouns, lifecycle rule)
- [ ] Define relationships (1:1, 1:N, M:N)
- [ ] Specify metrics (Counts, sums, ratios - on facts)
- [ ] Choose grain (One row per X, never mix grains)
- [ ] Validate model (No double-counting, clean joins, natural aggregation)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the data modeling framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Entities → Relationships → Metrics → Grain → Validate framework**, not memorizing answers

**Remember:** L7 is about data modeling. The framework: Entities → Relationships → Metrics → Grain → Validate. Key principles: Grain is the most important decision. Facts store metrics; dimensions store context. If joins feel painful, the model is wrong. Model for questions, not for storage.
