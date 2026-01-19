# 🧠 Data Engineer Interview Mindmap (Systematic)

## 📚 Resources

**GitHub Repo**: https://github.com/anix-lynch/Exponent

**Source**: https://www.tryexponent.com/questions?page=1&role=data-engineer

**🎯 YOUR #1 GOAL ROLE - Master these patterns!**

---

## 📊 Question Distribution

```
Data Pipeline Design....................   76 questions
Data Structures & Algorithms............   32 questions
System Design...........................   20 questions
Data Modeling...........................   12 questions
SQL.....................................   12 questions
Data Warehousing........................   10 questions
Behavioral..............................    5 questions
ETL/ELT.................................    4 questions
Data Quality............................    4 questions
Spark/Big Data..........................    4 questions
Cloud Platforms.........................    3 questions
Coding..................................    3 questions
Database Design.........................    3 questions
Monitoring & Observability..............    2 questions
Distributed Systems.....................    1 question
Streaming Data..........................    1 question
Performance Optimization................    1 question
Schema Design...........................    1 question
Data Governance.........................    1 question
```

**Total: 151 questions across 19 categories**

---

## 🔟 How to USE this in interviews

When a question comes:

1. **Name the category silently**
2. **Apply that category's framework**
3. **Speak in structured bullets**

---

## 0️⃣ Core Data Engineering Meta-Structure

Every DE interview tests:

- **Pipeline thinking** (end-to-end data flow)
- **Scale awareness** (TB/PB data volumes)
- **Trade-off analysis** (batch vs stream, cost vs performance)
- **Data quality mindset** (garbage in = garbage out)

So every answer should follow:

```
Source → Ingest → Transform → Store → Serve → Monitor
```

---

## 1️⃣ Data Pipeline Design (CRITICAL - 76 questions)

**What they're really testing:**
Can you design end-to-end data pipelines that are scalable, reliable, and maintainable?

**Mindmap**

```
Data Pipeline Design
├─ 1. Understand Requirements
│  ├─ Data sources (APIs, DBs, files, streams)
│  ├─ Data volume (GB/TB/PB per day)
│  ├─ Data velocity (batch/real-time/near-real-time)
│  ├─ Data variety (structured/semi/unstructured)
│  └─ SLAs (latency, freshness, availability)
│
├─ 2. Ingestion Layer
│  ├─ Batch ingestion
│  │  ├─ Full load vs incremental
│  │  ├─ Tools: Airflow, Luigi, Prefect
│  │  └─ Scheduling (cron, event-driven)
│  │
│  └─ Streaming ingestion
│     ├─ Kafka, Kinesis, Pub/Sub
│     ├─ Change Data Capture (CDC)
│     └─ Backpressure handling
│
├─ 3. Transformation Layer
│  ├─ ETL vs ELT decision
│  ├─ Data cleaning & validation
│  ├─ Business logic application
│  ├─ Aggregations & joins
│  └─ Tools: Spark, dbt, Dataflow
│
├─ 4. Storage Layer
│  ├─ Data lake (S3, GCS, ADLS)
│  ├─ Data warehouse (Snowflake, Redshift, BigQuery)
│  ├─ Data lakehouse (Delta Lake, Iceberg)
│  ├─ Partitioning strategy
│  └─ Compression & file formats (Parquet, Avro, ORC)
│
├─ 5. Serving Layer
│  ├─ OLAP queries (analytics)
│  ├─ OLTP queries (transactional)
│  ├─ APIs & microservices
│  ├─ Dashboards & BI tools
│  └─ ML model serving
│
├─ 6. Data Quality
│  ├─ Schema validation
│  ├─ Data profiling
│  ├─ Anomaly detection
│  ├─ Data lineage tracking
│  └─ Tools: Great Expectations, deequ
│
└─ 7. Monitoring & Observability
   ├─ Pipeline health metrics
   ├─ Data freshness alerts
   ├─ Error handling & retries
   ├─ Logging & tracing
   └─ Cost monitoring
```

📌 **Always start with**: Source, Volume, Velocity, Variety, SLAs. Then walk through the 7 layers.

---

## 2️⃣ Data Structures & Algorithms (HIGH - 32 questions)

**What they're really testing:**
Can you write efficient code to process and manipulate data at scale?

**Mindmap**

```
DSA for Data Engineering
├─ 1. Arrays & Strings
│  ├─ Two pointers technique
│  ├─ Sliding window
│  ├─ String manipulation
│  └─ Use case: Log parsing, data validation
│
├─ 2. Hash Maps & Sets
│  ├─ Fast lookups O(1)
│  ├─ Deduplication
│  ├─ Counting & frequency
│  └─ Use case: Join operations, aggregations
│
├─ 3. Trees & Graphs
│  ├─ Binary trees (hierarchical data)
│  ├─ Graph traversal (BFS/DFS)
│  ├─ Topological sort
│  └─ Use case: DAG pipelines, dependency resolution
│
├─ 4. Heaps & Priority Queues
│  ├─ Top-K problems
│  ├─ Streaming data processing
│  └─ Use case: Finding top N records
│
├─ 5. Dynamic Programming
│  ├─ Memoization
│  ├─ Optimization problems
│  └─ Use case: Cost optimization, scheduling
│
└─ 6. Sorting & Searching
   ├─ Time complexity awareness
   ├─ Binary search
   └─ Use case: Data ordering, range queries
```

📌 **Think in terms of**: Time complexity (O(n)), Space complexity, and real-world data scale (millions of rows).

---

## 3️⃣ System Design (HIGH - 20 questions)

**What they're really testing:**
Can you architect data systems that handle TB/PB scale with high availability and low latency?

**Mindmap**

```
System Design for Data
├─ 1. Requirements Gathering
│  ├─ Functional requirements
│  │  ├─ What data to process?
│  │  ├─ What queries to support?
│  │  └─ What SLAs to meet?
│  │
│  └─ Non-functional requirements
│     ├─ Scale (QPS, data volume)
│     ├─ Latency (ms, seconds, minutes)
│     ├─ Availability (99.9%, 99.99%)
│     └─ Consistency vs Availability (CAP theorem)
│
├─ 2. High-Level Architecture
│  ├─ Data ingestion layer
│  ├─ Processing layer
│  ├─ Storage layer
│  ├─ Serving layer
│  └─ Draw boxes and arrows!
│
├─ 3. Deep Dive Components
│  ├─ Load balancers
│  ├─ Message queues (Kafka, SQS)
│  ├─ Compute (Spark, Flink, Dataflow)
│  ├─ Storage (S3, HDFS, databases)
│  └─ Caching (Redis, Memcached)
│
├─ 4. Data Flow
│  ├─ Batch processing (Spark, MapReduce)
│  ├─ Stream processing (Flink, Spark Streaming)
│  ├─ Lambda architecture (batch + stream)
│  └─ Kappa architecture (stream-only)
│
├─ 5. Scalability
│  ├─ Horizontal scaling (add more nodes)
│  ├─ Vertical scaling (bigger machines)
│  ├─ Partitioning/Sharding
│  ├─ Replication
│  └─ Auto-scaling
│
├─ 6. Reliability
│  ├─ Fault tolerance
│  ├─ Retry mechanisms
│  ├─ Dead letter queues
│  ├─ Disaster recovery
│  └─ Backup strategies
│
└─ 7. Trade-offs
   ├─ Consistency vs Availability
   ├─ Latency vs Throughput
   ├─ Cost vs Performance
   ├─ Batch vs Stream
   └─ Normalized vs Denormalized
```

📌 **Always discuss trade-offs**: No perfect solution, only trade-offs based on requirements.

---

## 4️⃣ Data Modeling (IMPORTANT - 12 questions)

**What they're really testing:**
Can you design schemas that are efficient, maintainable, and support business queries?

**Mindmap**

```
Data Modeling
├─ 1. Understand Use Cases
│  ├─ What queries will be run?
│  ├─ Read-heavy or write-heavy?
│  ├─ OLTP or OLAP?
│  └─ Who are the users?
│
├─ 2. Identify Entities
│  ├─ Business objects (users, orders, products)
│  ├─ Events (clicks, purchases, views)
│  └─ Relationships (one-to-many, many-to-many)
│
├─ 3. Choose Modeling Approach
│  ├─ Normalized (3NF)
│  │  ├─ Pros: No redundancy, easy updates
│  │  └─ Cons: Complex joins, slower reads
│  │
│  ├─ Denormalized (Star/Snowflake)
│  │  ├─ Pros: Fast reads, simple queries
│  │  └─ Cons: Data redundancy, harder updates
│  │
│  └─ Hybrid approach
│
├─ 4. Define Schema
│  ├─ Fact tables (metrics, measurements)
│  ├─ Dimension tables (descriptive attributes)
│  ├─ Primary keys
│  ├─ Foreign keys
│  └─ Indexes
│
├─ 5. Optimize for Performance
│  ├─ Partitioning (by date, region, etc.)
│  ├─ Clustering/Sorting keys
│  ├─ Materialized views
│  ├─ Aggregation tables
│  └─ Compression
│
└─ 6. Data Types & Constraints
   ├─ Choose appropriate types (INT vs BIGINT)
   ├─ NOT NULL constraints
   ├─ UNIQUE constraints
   └─ Check constraints
```

📌 **Star schema for analytics, normalized for transactional**. Always ask about query patterns first!

---

## 5️⃣ SQL (IMPORTANT - 12 questions)

**What they're really testing:**
Can you write complex, optimized SQL queries for data transformation and analysis?

**Mindmap**

```
SQL for Data Engineering
├─ 1. Understand the Problem
│  ├─ What tables are involved?
│  ├─ What is the desired output?
│  ├─ What are the edge cases?
│  └─ Explain logic before writing
│
├─ 2. Core Operations
│  ├─ SELECT / WHERE / ORDER BY
│  ├─ JOINs (INNER, LEFT, RIGHT, FULL)
│  ├─ GROUP BY / HAVING
│  ├─ Subqueries
│  └─ CTEs (WITH clause)
│
├─ 3. Aggregations
│  ├─ COUNT / SUM / AVG / MIN / MAX
│  ├─ DISTINCT
│  ├─ GROUP BY multiple columns
│  └─ HAVING for filtered aggregations
│
├─ 4. Window Functions
│  ├─ ROW_NUMBER() - unique row numbers
│  ├─ RANK() / DENSE_RANK() - rankings with ties
│  ├─ LAG() / LEAD() - access previous/next rows
│  ├─ SUM() OVER / AVG() OVER - running totals
│  └─ PARTITION BY for grouped calculations
│
├─ 5. Advanced Techniques
│  ├─ CASE statements (conditional logic)
│  ├─ UNION / UNION ALL
│  ├─ INTERSECT / EXCEPT
│  ├─ Self-joins
│  └─ Recursive CTEs
│
├─ 6. Optimization
│  ├─ Use indexes wisely
│  ├─ Push down filters (WHERE early)
│  ├─ Avoid SELECT *
│  ├─ Use EXPLAIN to check query plan
│  └─ Partition pruning
│
└─ 7. Edge Cases
   ├─ Handle NULLs (COALESCE, IS NULL)
   ├─ Duplicates (DISTINCT, GROUP BY)
   ├─ Empty results
   └─ Data type mismatches
```

📌 **Structure first, optimize later**: Write readable CTEs, then optimize if needed. Always explain your logic!

---

## 6️⃣ Data Warehousing (IMPORTANT - 10 questions)

**What they're really testing:**
Do you understand modern data warehouse architectures and best practices?

**Mindmap**

```
Data Warehousing
├─ 1. Architecture Patterns
│  ├─ Traditional DW (on-prem, ETL)
│  ├─ Cloud DW (Snowflake, Redshift, BigQuery)
│  ├─ Data Lake (S3, ADLS, GCS)
│  ├─ Data Lakehouse (Delta Lake, Iceberg, Hudi)
│  └─ Medallion architecture (Bronze/Silver/Gold)
│
├─ 2. Schema Design
│  ├─ Star schema (1 fact, N dimensions)
│  ├─ Snowflake schema (normalized dimensions)
│  ├─ Fact tables (metrics, additive measures)
│  ├─ Dimension tables (descriptive attributes)
│  └─ Slowly Changing Dimensions (SCD Type 1/2/3)
│
├─ 3. ETL vs ELT
│  ├─ ETL: Transform before loading
│  │  ├─ Pros: Clean data in DW
│  │  └─ Cons: Slower, less flexible
│  │
│  └─ ELT: Load then transform
│     ├─ Pros: Fast loading, flexible
│     └─ Cons: DW does heavy lifting
│
├─ 4. Partitioning & Clustering
│  ├─ Partition by date/region
│  ├─ Cluster by frequently filtered columns
│  ├─ Improves query performance
│  └─ Reduces scan costs
│
├─ 5. Performance Optimization
│  ├─ Materialized views
│  ├─ Result caching
│  ├─ Query optimization
│  ├─ Compression (Parquet, ORC)
│  └─ Columnar storage
│
└─ 6. Cost Management
   ├─ Storage costs (hot vs cold)
   ├─ Compute costs (on-demand vs reserved)
   ├─ Data transfer costs
   └─ Query optimization to reduce scans
```

📌 **Cloud DW = ELT, Traditional DW = ETL**. Always consider cost vs performance trade-offs!

---

## 7️⃣ ETL/ELT (4 questions)

**What they're really testing:**
Do you understand data transformation workflows and orchestration?

**Mindmap**

```
ETL/ELT
├─ Extract
│  ├─ Source systems (APIs, DBs, files)
│  ├─ Full vs incremental extraction
│  ├─ Change Data Capture (CDC)
│  └─ Error handling
│
├─ Transform
│  ├─ Data cleaning (nulls, duplicates)
│  ├─ Data validation (schema, types)
│  ├─ Business logic (calculations, aggregations)
│  ├─ Data enrichment (lookups, joins)
│  └─ Tools: Spark, dbt, Dataflow
│
├─ Load
│  ├─ Append vs upsert vs full refresh
│  ├─ Batch loading
│  ├─ Streaming loading
│  └─ Idempotency (safe to re-run)
│
└─ Orchestration
   ├─ Workflow scheduling (Airflow, Prefect)
   ├─ Dependency management (DAGs)
   ├─ Retry logic
   ├─ Alerting & monitoring
   └─ Backfilling historical data
```

📌 **ETL for clean data, ELT for speed and flexibility**. Always make pipelines idempotent!

---

## 8️⃣ Data Quality (4 questions)

**What they're really testing:**
Can you ensure data reliability and trustworthiness?

**Mindmap**

```
Data Quality
├─ 1. Data Quality Dimensions
│  ├─ Accuracy (correct values)
│  ├─ Completeness (no missing data)
│  ├─ Consistency (same across systems)
│  ├─ Timeliness (fresh data)
│  ├─ Validity (conforms to schema)
│  └─ Uniqueness (no duplicates)
│
├─ 2. Validation Checks
│  ├─ Schema validation
│  ├─ Range checks (min/max)
│  ├─ Null checks
│  ├─ Uniqueness checks
│  └─ Referential integrity
│
├─ 3. Data Profiling
│  ├─ Statistical analysis
│  ├─ Distribution analysis
│  ├─ Outlier detection
│  └─ Pattern recognition
│
├─ 4. Tools & Frameworks
│  ├─ Great Expectations
│  ├─ deequ (AWS)
│  ├─ dbt tests
│  └─ Custom validation scripts
│
└─ 5. Monitoring & Alerting
   ├─ Data freshness SLAs
   ├─ Row count anomalies
   ├─ Schema drift detection
   └─ Data lineage tracking
```

📌 **Garbage in = garbage out**. Always validate data at ingestion and transformation stages!

---

## 9️⃣ Spark/Big Data (4 questions)

**What they're really testing:**
Can you process large-scale data efficiently using distributed computing?

**Mindmap**

```
Spark & Big Data
├─ 1. Spark Fundamentals
│  ├─ RDDs (low-level API)
│  ├─ DataFrames (structured API)
│  ├─ Datasets (typed API)
│  └─ Lazy evaluation
│
├─ 2. Transformations
│  ├─ Narrow (map, filter) - no shuffle
│  ├─ Wide (groupBy, join) - shuffle
│  ├─ Actions (collect, count, save)
│  └─ Catalyst optimizer
│
├─ 3. Performance Optimization
│  ├─ Partitioning (repartition, coalesce)
│  ├─ Caching (persist, cache)
│  ├─ Broadcast joins (small tables)
│  ├─ Avoid shuffles
│  └─ Tune executor memory/cores
│
├─ 4. Data Formats
│  ├─ Parquet (columnar, compressed)
│  ├─ Avro (row-based, schema evolution)
│  ├─ ORC (optimized columnar)
│  └─ JSON/CSV (human-readable)
│
└─ 5. Cluster Management
   ├─ YARN, Mesos, Kubernetes
   ├─ Driver vs Executor
   ├─ Dynamic allocation
   └─ Resource tuning
```

📌 **Avoid shuffles, use broadcast joins for small tables, partition wisely**. Always think about data skew!

---

## 🔟 Cloud Platforms (3 questions)

**What they're really testing:**
Are you familiar with cloud-native data services?

**Mindmap**

```
Cloud Data Services
├─ AWS
│  ├─ S3 (object storage)
│  ├─ Redshift (data warehouse)
│  ├─ Glue (ETL service)
│  ├─ Athena (serverless SQL)
│  ├─ EMR (managed Spark/Hadoop)
│  ├─ Kinesis (streaming)
│  └─ Lambda (serverless compute)
│
├─ GCP
│  ├─ GCS (object storage)
│  ├─ BigQuery (data warehouse)
│  ├─ Dataflow (stream/batch processing)
│  ├─ Dataproc (managed Spark/Hadoop)
│  ├─ Pub/Sub (messaging)
│  └─ Cloud Functions (serverless)
│
└─ Azure
   ├─ ADLS (data lake storage)
   ├─ Synapse Analytics (data warehouse)
   ├─ Data Factory (ETL service)
   ├─ Databricks (Spark platform)
   ├─ Event Hubs (streaming)
   └─ Functions (serverless)
```

📌 **Know the equivalents across clouds**: S3 = GCS = ADLS, Redshift = BigQuery = Synapse.

---

## 1️⃣1️⃣ Coding (3 questions)

**What they're really testing:**
Can you write clean, efficient Python/Scala code for data processing?

**Mindmap**

```
Coding for Data Engineering
├─ 1. Problem Understanding
│  ├─ Read carefully
│  ├─ Clarify inputs/outputs
│  ├─ Ask about edge cases
│  └─ Discuss approach first
│
├─ 2. Code Structure
│  ├─ Functions (single responsibility)
│  ├─ Classes (when needed)
│  ├─ Error handling (try/except)
│  └─ Logging
│
├─ 3. Data Structures
│  ├─ Lists, dicts, sets
│  ├─ Choose based on use case
│  └─ Time/space complexity
│
├─ 4. Common Patterns
│  ├─ File I/O
│  ├─ JSON/CSV parsing
│  ├─ API calls
│  ├─ Data transformations
│  └─ Batch processing
│
└─ 5. Best Practices
   ├─ Readable variable names
   ├─ Comments for complex logic
   ├─ Test as you go
   └─ Handle edge cases
```

📌 **Readability > cleverness**. Write code your team can maintain!

---

## 1️⃣2️⃣ Database Design (3 questions)

**What they're really testing:**
Can you design database schemas for different use cases?

**Mindmap**

```
Database Design
├─ 1. Requirements Analysis
│  ├─ OLTP (transactional) or OLAP (analytical)?
│  ├─ Read-heavy or write-heavy?
│  ├─ Query patterns
│  └─ Scale expectations
│
├─ 2. Schema Design
│  ├─ Tables & columns
│  ├─ Primary keys
│  ├─ Foreign keys
│  ├─ Indexes
│  └─ Constraints
│
├─ 3. Normalization
│  ├─ 1NF (atomic values)
│  ├─ 2NF (no partial dependencies)
│  ├─ 3NF (no transitive dependencies)
│  └─ When to denormalize
│
├─ 4. Database Types
│  ├─ Relational (PostgreSQL, MySQL)
│  ├─ NoSQL (MongoDB, Cassandra)
│  ├─ Key-value (Redis, DynamoDB)
│  ├─ Column-family (HBase, Cassandra)
│  └─ Graph (Neo4j, Neptune)
│
└─ 5. Performance
   ├─ Indexing strategy
   ├─ Partitioning
   ├─ Replication
   └─ Caching
```

📌 **Choose the right database for the job**: Relational for ACID, NoSQL for scale and flexibility.

---

## 1️⃣3️⃣ Monitoring & Observability (2 questions)

**What they're really testing:**
Can you ensure pipeline reliability and quickly debug issues?

**Mindmap**

```
Monitoring & Observability
├─ 1. Metrics
│  ├─ Pipeline success/failure rates
│  ├─ Data volume processed
│  ├─ Processing latency
│  ├─ Resource utilization (CPU, memory)
│  └─ Cost metrics
│
├─ 2. Logging
│  ├─ Structured logs (JSON)
│  ├─ Log levels (INFO, WARN, ERROR)
│  ├─ Centralized logging (ELK, Splunk)
│  └─ Log retention policies
│
├─ 3. Alerting
│  ├─ Data freshness SLAs
│  ├─ Pipeline failures
│  ├─ Data quality issues
│  ├─ Anomaly detection
│  └─ On-call rotation
│
├─ 4. Tracing
│  ├─ End-to-end data lineage
│  ├─ Distributed tracing
│  ├─ Bottleneck identification
│  └─ Tools: Jaeger, Zipkin
│
└─ 5. Dashboards
   ├─ Real-time pipeline health
   ├─ Historical trends
   ├─ SLA compliance
   └─ Tools: Grafana, Datadog
```

📌 **You can't fix what you can't see**. Always instrument your pipelines!

---

## 1️⃣4️⃣ Behavioral (5 questions)

**What they're really testing:**
Can you work effectively in a team and handle challenges?

**Mindmap (STAR Method)**

```
Behavioral
├─ Situation
│  ├─ Set the context
│  └─ Be specific
│
├─ Task
│  ├─ What was your goal?
│  └─ What was the challenge?
│
├─ Action
│  ├─ What did YOU do?
│  ├─ Technical decisions
│  ├─ Trade-offs considered
│  └─ Collaboration
│
└─ Result
   ├─ Quantifiable impact
   ├─ What you learned
   └─ What you'd do differently
```

📌 **Common themes**: Conflict resolution, technical challenges, project ownership, mentorship, failure/learning.

---

## 1️⃣5️⃣ Distributed Systems (1 question)

**What they're really testing:**
Do you understand distributed computing principles?

**Mindmap**

```
Distributed Systems
├─ CAP Theorem
│  ├─ Consistency
│  ├─ Availability
│  └─ Partition Tolerance
│  (Pick 2 of 3)
│
├─ Consistency Models
│  ├─ Strong consistency
│  ├─ Eventual consistency
│  └─ Causal consistency
│
├─ Replication
│  ├─ Master-slave
│  ├─ Multi-master
│  └─ Quorum-based
│
├─ Partitioning/Sharding
│  ├─ Hash-based
│  ├─ Range-based
│  └─ Consistent hashing
│
└─ Fault Tolerance
   ├─ Replication
   ├─ Checkpointing
   └─ Retry mechanisms
```

📌 **No perfect solution**: Every distributed system makes trade-offs based on requirements.

---

## 1️⃣6️⃣ Streaming Data (1 question)

**What they're really testing:**
Can you process real-time data streams?

**Mindmap**

```
Streaming Data
├─ Streaming Platforms
│  ├─ Kafka
│  ├─ Kinesis
│  ├─ Pub/Sub
│  └─ Event Hubs
│
├─ Processing Frameworks
│  ├─ Spark Streaming
│  ├─ Flink
│  ├─ Storm
│  └─ Kafka Streams
│
├─ Windowing
│  ├─ Tumbling windows (fixed)
│  ├─ Sliding windows (overlapping)
│  ├─ Session windows (gap-based)
│  └─ Watermarks (late data handling)
│
├─ State Management
│  ├─ Stateless (map, filter)
│  ├─ Stateful (aggregations, joins)
│  └─ Checkpointing
│
└─ Challenges
   ├─ Out-of-order events
   ├─ Late arrivals
   ├─ Exactly-once semantics
   └─ Backpressure
```

📌 **Batch = simplicity, Stream = low latency**. Choose based on SLAs!

---

## 1️⃣7️⃣ Performance Optimization (1 question)

**What they're really testing:**
Can you identify and fix performance bottlenecks?

**Mindmap**

```
Performance Optimization
├─ 1. Identify Bottlenecks
│  ├─ Profiling tools
│  ├─ Query execution plans
│  ├─ Resource monitoring
│  └─ Slow query logs
│
├─ 2. Query Optimization
│  ├─ Use indexes
│  ├─ Push down filters
│  ├─ Avoid SELECT *
│  ├─ Use partitioning
│  └─ Materialized views
│
├─ 3. Data Optimization
│  ├─ Compression (Parquet, ORC)
│  ├─ Columnar storage
│  ├─ Partitioning by date/region
│  └─ Clustering keys
│
├─ 4. Compute Optimization
│  ├─ Increase parallelism
│  ├─ Tune memory/CPU
│  ├─ Caching frequently accessed data
│  └─ Broadcast joins
│
└─ 5. Architecture Optimization
   ├─ Denormalize for reads
   ├─ Pre-aggregate data
   ├─ Use CDNs for static data
   └─ Horizontal scaling
```

📌 **Measure first, optimize second**. Don't guess where the bottleneck is!

---

## 1️⃣8️⃣ Schema Design (1 question)

**What they're really testing:**
Can you design flexible, maintainable schemas?

**Mindmap**

```
Schema Design
├─ Schema Evolution
│  ├─ Add columns (backward compatible)
│  ├─ Remove columns (forward compatible)
│  ├─ Change types (breaking change)
│  └─ Schema registry (Avro, Protobuf)
│
├─ Data Types
│  ├─ Numeric (INT, BIGINT, DECIMAL)
│  ├─ String (VARCHAR, TEXT)
│  ├─ Date/Time (DATE, TIMESTAMP)
│  ├─ Boolean
│  └─ JSON/JSONB
│
├─ Constraints
│  ├─ NOT NULL
│  ├─ UNIQUE
│  ├─ PRIMARY KEY
│  ├─ FOREIGN KEY
│  └─ CHECK
│
└─ Best Practices
   ├─ Use appropriate types (save space)
   ├─ Avoid nullable keys
   ├─ Document schema
   └─ Version schemas
```

📌 **Plan for change**: Schemas evolve over time. Design for backward compatibility!

---

## 1️⃣9️⃣ Data Governance (1 question)

**What they're really testing:**
Do you understand data privacy, security, and compliance?

**Mindmap**

```
Data Governance
├─ Data Privacy
│  ├─ PII (Personally Identifiable Information)
│  ├─ GDPR compliance
│  ├─ CCPA compliance
│  ├─ Data anonymization
│  └─ Data masking
│
├─ Data Security
│  ├─ Encryption at rest
│  ├─ Encryption in transit
│  ├─ Access control (IAM, RBAC)
│  ├─ Audit logs
│  └─ Data retention policies
│
├─ Data Quality
│  ├─ Data validation
│  ├─ Data profiling
│  └─ Data lineage
│
├─ Metadata Management
│  ├─ Data catalog
│  ├─ Schema registry
│  ├─ Data dictionary
│  └─ Tags & classifications
│
└─ Compliance
   ├─ Regulatory requirements
   ├─ Data residency
   ├─ Right to be forgotten
   └─ Audit trails
```

📌 **Data governance is not optional**: Compliance failures can shut down companies!

---

## 🚀 Study Strategy for YOUR #1 GOAL

### Week 1-2: Data Pipeline Design (76 questions - 50%)
- Master the 7-step framework
- Practice designing end-to-end pipelines
- Focus on batch vs streaming decisions
- Learn orchestration tools (Airflow)

### Week 3-4: Data Structures & Algorithms (32 questions - 21%)
- Daily LeetCode practice (Medium level)
- Focus on: Hash maps, trees, dynamic programming
- Common patterns: Two pointers, sliding window
- Think about scale (millions of rows)

### Week 5-6: System Design (20 questions - 13%)
- Practice designing data systems at TB/PB scale
- Study: Data warehouses, streaming systems, batch processing
- Learn trade-offs: Cost vs performance, batch vs stream
- Draw architecture diagrams

### Ongoing: SQL, Data Modeling, Data Warehousing
- Weekly SQL practice (window functions, CTEs, optimization)
- Study star schema, snowflake schema, SCD
- Learn cloud DW services (Snowflake, BigQuery, Redshift)

**Master these three areas (Pipeline + DSA + System Design) and you'll ace 83% of DE interviews!**

---

## 🎯 Final Tips

1. **Always think at scale**: TB/PB, not GB
2. **Discuss trade-offs**: No perfect solution, only trade-offs
3. **Draw diagrams**: Visual communication is key
4. **Ask clarifying questions**: Requirements are never complete
5. **Think end-to-end**: Source → Ingest → Transform → Store → Serve → Monitor

---

**Good luck with your #1 goal role! 🚀**

**See [`Data_Engineer_Question_Bank.md`](./Data_Engineer_Question_Bank.md) for all questions with embedded frameworks.**
