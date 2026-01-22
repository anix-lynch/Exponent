# Executive Study Plan: L14 - System Design (Conceptual)
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~30 questions → 3 concept buckets → 2-3 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L14 (SYSTEM DESIGN) QUESTIONS

**Even when "system design" isn't mentioned, look for these keywords/phrases:**

### Explicit System Design Keywords:
- "design a system", "design X", "system architecture", "how would you build", "design a pipeline"
- "data pipeline", "ETL", "data warehouse", "monitoring system", "metrics service"
- "conceptual design", "high-level design", "architecture", "components", "data flow"

### Implicit L14 Indicators:
- **Design questions:** "Design a system for X", "How would you build X?", "Design a pipeline"
- **Architecture questions:** "What's the architecture?", "How does data flow?", "What are the components?"
- **System questions:** "Design a monitoring system", "Design a metrics service", "Design a data pipeline"

### L14 vs L2 Distinction:
- **L14 (System Design):** "Design a system for X" → Focus: Components, data flow, boundaries, scale (conceptual architecture)
- **L2 (Scale & Capacity):** "What breaks if traffic grows 10x?" → Focus: Identify bottlenecks, design mitigation

### L14 vs L5 Distinction:
- **L14 (System Design):** "Design a monitoring system" → Focus: System architecture, components, data flow
- **L5 (Observability):** "How do you monitor a system?" → Focus: Metrics, alerts, dashboards, escalation

### Red Flags (NOT L14):
- "What breaks if traffic grows 10x?" → L2 (Scale & Capacity)
- "How do you monitor a system?" → L5 (Observability)
- "How do you ensure system reliability?" → P12 (Operational Excellence)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2-3 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **System Design Framework** (HIGHEST PRIORITY)
2. ✅ **Data Pipeline Design** (HIGH PRIORITY)
3. ⚠️ **General System Design** (MEDIUM)

**For Data Engineer:**
1. ✅ **System Design Framework** (HIGHEST) - Core framework
2. ✅ **Data Pipeline Design** (HIGHEST) - Core DE skill
3. ✅ **General System Design** (HIGH) - System architecture

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: System Design Framework
**Questions:** ~15 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Design a system for X" or "How would you build X?" - core system design framework
- **Framework:** Define Goal → Components → Data Flow → Boundaries → Scale Considerations
- **Define Goal:** What problem are we solving? (Primary user goal, Success metric: latency, reliability, accuracy, cost, Non-goals: explicitly say what's out of scope), Rule: If the goal isn't clear, architecture will be wrong
- **Components:** What blocks exist? (Clients: web, mobile, internal tools, Ingestion layer: APIs, SDKs, event collectors, Processing layer: sync vs async, Storage: hot/warm/cold, Compute: stateless vs stateful, Orchestration/queues, Observability: metrics, logs, alerts, Admin/control plane), Rule: Name boxes before wiring arrows
- **Data Flow:** How data moves end-to-end (Request path - read, Write path - create/update, Async paths - queues, streams, retries, Failure paths - timeouts, backpressure, Control vs data plane separation), Rule: Always describe the happy path first
- **Boundaries & Constraints:** What limits us? (Latency SLOs, Consistency requirements, Throughput limits, Regulatory/privacy constraints, Team ownership boundaries, Cost ceilings), Rule: Constraints shape architecture more than features
- **Scale & Failure Modes:** What breaks at 10×? (Bottlenecks: DB, network, fan-out, Single points of failure, Backpressure strategy, Caching layers, Sharding/partitioning, Graceful degradation), Rule: Talk about failure BEFORE optimization

**Concrete Examples:**
- "URL shortening service: Goal (Shorten URLs, low latency reads, high availability), Components (Client, API gateway, ID generator, URL store, Cache, Analytics pipeline), Data Flow (Write: client → API → ID gen → DB → cache, Read: client → API → cache → DB fallback), Boundaries (Read-heavy, strong consistency on write, low latency <50ms), Scale (Cache hot paths, shard by short_id, async analytics)"
- "System design: Define goal, identify components, map data flow, set boundaries, design for scale"

**Representative Questions (Do 5 only):**
- Q287: Design a data pipeline that updates hourly and powers a dashboard showing the most common Alexa user requests, broken down by country. (data pipeline design angle)
- Q230: Describe an endpoint and provide two examples. (API/system design angle)
- Q361: Design a metrics and logging service. (metrics service design angle)
- Q362: Design a metrics service. (metrics service design angle)
- Q367: Design a monitoring system for 1000 web servers. (monitoring system design angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Goal → Components → Data Flow → Boundaries → Scale Considerations`

**Memorizable Answer:**

When designing a system, I use Define Goal → Components → Data Flow → Boundaries → Scale Considerations.

**1️⃣ Define Goal** → What problem are we solving?
  - **Primary user goal:** What is the main user need or business objective?
  - **Success metric:** Latency, reliability, accuracy, cost (what defines success?)
  - **Non-goals:** Explicitly say what's out of scope (what we're NOT building)

**Rule:** If the goal isn't clear, architecture will be wrong.

**2️⃣ Core Components** → What blocks exist?
  - **Clients:** Web, mobile, internal tools (what are the entry points?)
  - **Ingestion layer:** APIs, SDKs, event collectors (how does data enter?)
  - **Processing layer:** Sync vs async (how is data processed?)
  - **Storage:** Hot/warm/cold (where is data stored?)
  - **Compute:** Stateless vs stateful (how is computation handled?)
  - **Orchestration/queues:** How are tasks coordinated?
  - **Observability:** Metrics, logs, alerts (how do we monitor?)
  - **Admin/control plane:** How is the system managed?

**Rule:** Name boxes before wiring arrows.

**3️⃣ Data Flow** → How data moves end-to-end:
  - **Request path (read):** How do read requests flow through the system?
  - **Write path (create/update):** How do write requests flow through?
  - **Async paths:** Queues, streams, retries (how are async ops handled?)
  - **Failure paths:** Timeouts, backpressure (how are failures handled?)
  - **Control vs data plane separation:** How are control and data separated?

**Rule:** Always describe the happy path first.

**4️⃣ Boundaries & Constraints** → What limits us?
  - **Latency SLOs:** What are the latency requirements?
  - **Consistency:** Strong vs eventual consistency?
  - **Throughput:** How many requests per second must we handle?
  - **Regulatory/privacy constraints:** GDPR, data residency, compliance?
  - **Team ownership boundaries:** Who owns what?
  - **Cost ceilings:** What are the budget constraints?

**Rule:** Constraints shape architecture more than features.

**5️⃣ Scale & Failure Modes** → What breaks at 10×?
  - **Bottlenecks:** DB, network, fan-out (what fails first?)
  - **Single points of failure:** What can't fail?
  - **Backpressure strategy:** How do we handle overload?
  - **Caching layers:** Where do we cache?
  - **Sharding/partitioning:** How do we distribute load?
  - **Graceful degradation:** How do we degrade gracefully?

**Rule:** Talk about failure BEFORE optimization.

**Output:** "System of boxes + arrows, bounded by constraints, designed to scale and fail safely."

---

**How to Adapt This Narrative for Each Question:**

- **Q287 (Data pipeline for Alexa requests):** Focus on data pipeline design
  - "Define Goal: Primary user goal (process Alexa requests, aggregate by country, update hourly), Success metric (data freshness - hourly updates, throughput - handle request volume, accuracy - correct aggregation, cost - efficient processing), Non-goals (real-time processing, complex ML features)"
  - "Components: Ingestion (request logs/events collector), Processing (ETL/ELT engine - Spark, Dataflow), Storage (data warehouse - for dashboard), Staging (temporary storage), Orchestration (scheduler - Airflow), Observability (monitoring, alerts)"
  - "Data Flow: Happy path (request logs → Ingestion → Processing - aggregate by country, count requests → Storage → Dashboard), Write path (batch processing hourly), Read path (dashboard queries warehouse), Async paths (scheduled jobs, retries), Failure paths (retry failed jobs, dead letter queue, data quality checks)"
  - "Boundaries: Latency (hourly batch acceptable, not real-time), Consistency (eventual consistency OK, data freshness SLA), Throughput (handle request volume, process within hour), Cost (optimize compute, use spot instances), Regulatory (data privacy, compliance)"
  - "Scale: Bottlenecks (processing might be slow, storage might be expensive), Failure modes (job failures, data quality issues), Mitigation (parallel processing, efficient storage, monitoring, alerts)"
  - "Design: Ingestion (collect request logs from Alexa devices), Processing (aggregate requests by country, count most common requests, hourly batch), Storage (store aggregated data in warehouse), Dashboard (query warehouse for visualization)"

- **Q361 (Metrics and logging service):** Emphasize metrics service design
  - "Define Goal: Primary user goal (collect, store, query metrics and logs), Success metric (low latency queries, high throughput ingestion, reliability, cost), Non-goals (real-time analytics, complex ML)"
  - "Components: Clients (applications, services), Ingestion (metrics/logs collectors, SDKs), Processing (aggregation, indexing), Storage (time-series DB - metrics, Log storage - logs), Query (API, query engine), Observability (self-monitoring)"
  - "Data Flow: Write path (client → Collector → Processing → Storage), Read path (client → Query API → Storage → Results), Async paths (batch processing, indexing), Failure paths (retries, buffering, backpressure)"
  - "Boundaries: Latency (query latency <100ms, ingestion latency acceptable), Consistency (eventual consistency OK), Throughput (high ingestion rate), Cost (efficient storage, compression)"
  - "Scale: Bottlenecks (storage might be expensive, query might be slow), Failure modes (ingestion overload, storage full), Mitigation (compression, indexing, caching, sharding)"
  - "Design: Collection layer (agents, SDKs for metrics/logs), Storage layer (time-series DB for metrics, log storage for logs), Query layer (API for querying, dashboards), Alert layer (alerting engine, notifications)"

---

### BUCKET 2: Data Pipeline Design
**Questions:** ~10 | **Priority:** 🟢 GREEN (High-yield)

**Board Slide Bullets:**
- **What:** "Design a data pipeline" or "ETL system" - same framework, with focus on data pipelines
- **Approach:** Same system design framework, with focus on data pipeline components
- **Pipeline Components:** Ingestion, Processing (ETL/ELT), Storage, Orchestration, Observability
- **Pipeline Flow:** Source → Ingestion → Processing → Storage → Consumption

**Concrete Examples:**
- "ETL pipeline: Source (Application logs), Ingestion (Collectors, APIs), Processing (ETL engine - transform, aggregate), Storage (Data warehouse), Consumption (Dashboards, APIs)"
- "Data pipeline: Design ingestion, processing, storage, orchestration, observability"

**Representative Questions (Do 5 only):**
- Q287: Design a data pipeline that updates hourly and powers a dashboard showing the most common Alexa user requests, broken down by country. (data pipeline design angle)
- Q289: Design a Data Warehouse Schema for a Ride-Sharing Service. (data warehouse/pipeline angle)
- Q290: Design a Data Warehouse Schema for Airbnb. (data warehouse/pipeline angle)
- Q291: Design a data warehouse schema for Amazon. (data warehouse/pipeline angle)
- Q292: Design a data warehouse schema for an e-commerce company. (data warehouse/pipeline angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Goal → Components (Pipeline Focus) → Data Flow → Boundaries → Scale`

**Memorizable Answer:**

When designing data pipelines, I use the same system design framework but focus on pipeline components.

**1️⃣ Define Goal** → What data do we need? What's the update frequency? What's the consumption pattern?

**2️⃣ Components** → 
  - **Ingestion:** Batch jobs, stream processors, API collectors (how does data enter?)
  - **Processing:** ETL/ELT engines (Spark, Flink, Dataflow - how is data transformed?)
  - **Storage:** Data lake (S3), warehouse (Snowflake), staging DB (where is data stored?)
  - **Transformation:** Data cleaning, aggregation, enrichment (what transformations?)
  - **Orchestration:** Schedulers (Airflow, workflow managers - how are jobs scheduled?)
  - **Observability:** Monitoring, alerts (how do we monitor?)

**3️⃣ Data Flow** → 
  - **Ingest:** Source systems → message queue → batch/stream processor
  - **Transform:** Raw data → cleaned → transformed → aggregated → loaded
  - **Store:** Processed data → data warehouse → serve to dashboards/APIs
  - **Failure:** Retry failed jobs, dead letter queue, data quality checks

**4️⃣ Boundaries** → 
  - **Latency:** Batch processing acceptable (hourly/daily, not real-time)
  - **Consistency:** Eventual consistency OK, data freshness SLA
  - **Throughput:** Handle TB/PB scale, process within time window
  - **Cost:** Optimize compute costs, use spot instances

**5️⃣ Scale** → 
  - **Bottlenecks:** Processing might be slow, storage expensive
  - **Failure modes:** Job failures, data quality issues
  - **Mitigation:** Parallel processing, efficient storage, monitoring

---

**How to Adapt This Narrative for Each Question:**

- **Q287 (Alexa requests pipeline):** Already covered in Bucket 1.

---

### BUCKET 3: General System Design
**Questions:** ~5 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Design a system for X" or "How would you build X?" - same framework, with focus on general systems
- **Approach:** Same system design framework, with focus on general system architecture
- **System Types:** APIs, services, platforms, applications
- **Design Principles:** Start with goal, Identify components, Map data flow, Set boundaries, Design for scale

**Concrete Examples:**
- "API design: Goal (Provide data access, low latency, high availability), Components (API gateway, services, database, cache), Data Flow (Request → API → Service → DB → Response), Boundaries (Latency <100ms, high throughput), Scale (Caching, load balancing, sharding)"
- "General system: Define goal, components, data flow, boundaries, scale"

**Representative Questions (Do 5 only):**
- Q230: Describe an endpoint and provide two examples. (API/system design angle)
- Q361: Design a metrics and logging service. (service design angle)
- Q362: Design a metrics service. (service design angle)
- Q367: Design a monitoring system for 1000 web servers. (monitoring system design angle)
- Q368: Design a monitoring system for TikTok. (monitoring system design angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Define Goal → Components → Data Flow → Boundaries → Scale (General System Focus)`

**Memorizable Answer:**

When designing general systems, I use the same system design framework.

**1️⃣ Define Goal** → What problem are we solving? Success metrics? Non-goals?

**2️⃣ Components** → Clients, APIs, services, storage, compute, observability.

**3️⃣ Data Flow** → Request path, write path, async paths, failure paths.

**4️⃣ Boundaries** → Latency, consistency, throughput, cost, regulatory.

**5️⃣ Scale** → Bottlenecks, failure modes, mitigation.

**Key Principle:** Start with the goal and work through components, flow, boundaries, and scale systematically.

---

**How to Adapt This Narrative for Each Question:**

- **Q230 (Endpoint design):** Focus on API endpoint
  - "Define Goal: Primary user goal (provide data/functionality access), Success metric (low latency, high availability, reliability), Non-goals (complex features initially)"
  - "Components: Client (web/mobile apps), API gateway (routing, auth, rate limiting), Service (business logic), Database (data storage), Cache (performance), Observability (monitoring)"
  - "Data Flow: Request path (client → API gateway → Service → DB/Cache → Response), Write path (client → API → Service → DB → Response), Async paths (background jobs, queues), Failure paths (error handling, retries, timeouts)"
  - "Boundaries: Latency (<100ms target), Consistency (strong vs eventual), Throughput (X requests/sec), Cost (budget constraints)"
  - "Scale: Bottlenecks (DB might be slow, API might be overloaded), Failure modes (service down, DB overload), Mitigation (caching, load balancing, DB optimization)"
  - "Design: RESTful endpoint (GET /users/{id}, POST /users), Clear request/response format, Error handling, Rate limiting, Authentication, Monitoring"

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **System Design Framework** → Study Bucket 1, practice 5 questions
2. **Data Pipeline Design** → Study Bucket 2, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
3. **General System Design** → Study Bucket 3, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through system design framework in 2 minutes (Define Goal → Components → Data Flow → Boundaries → Scale)
- [ ] Define goal (Primary user goal, success metrics, non-goals)
- [ ] Identify components (Clients, ingestion, processing, storage, compute, observability)
- [ ] Map data flow (Request path, write path, async paths, failure paths)
- [ ] Set boundaries (Latency, consistency, throughput, cost, regulatory)
- [ ] Consider scale (Bottlenecks, failure modes, mitigation)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the system design framework to a non-technical person in 2 minutes
- You have 3 reusable narratives (one per bucket) that you can adapt
- You've practiced 15 representative questions total (5 per bucket)
- You focus on **Define Goal → Components → Data Flow → Boundaries → Scale framework**, not memorizing answers

**Remember:** L14 is about system design (conceptual, not code). The framework: Define Goal → Components → Data Flow → Boundaries → Scale. Key principles: If the goal isn't clear, architecture will be wrong. Name boxes before wiring arrows. Always describe the happy path first. Constraints shape architecture more than features. Talk about failure BEFORE optimization.
