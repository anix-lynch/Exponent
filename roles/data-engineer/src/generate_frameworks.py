"""
Generate Data Engineer Question Bank with frameworks for each category
"""
import json
import os

# Load categorized questions
with open('data/questions_by_category.json', 'r') as f:
    questions_by_category = json.load(f)

# DE-specific frameworks for each category
FRAMEWORKS = {
    "Data Pipeline Design": """
Data Pipeline Design
├─ Understand requirements
│  ├─ Data sources (where?)
│  ├─ Data volume (how much?)
│  ├─ Data velocity (how fast?)
│  ├─ Data variety (what types?)
│  └─ SLAs (how often?)
│
├─ Design ingestion
│  ├─ Batch vs streaming
│  ├─ Pull vs push
│  ├─ Full vs incremental
│  └─ Data formats (JSON, CSV, Parquet)
│
├─ Plan transformation
│  ├─ Cleaning (nulls, duplicates)
│  ├─ Enrichment (joins, lookups)
│  ├─ Aggregation (group by, window)
│  └─ Business logic
│
├─ Choose storage
│  ├─ Data warehouse (Snowflake, Redshift)
│  ├─ Data lake (S3, ADLS)
│  ├─ Database (PostgreSQL, MongoDB)
│  └─ Cache (Redis, Memcached)
│
├─ Orchestrate workflow
│  ├─ Airflow / Dagster
│  ├─ Dependencies
│  ├─ Scheduling
│  └─ Error handling
│
├─ Monitor & maintain
│  ├─ Data quality checks
│  ├─ Pipeline health
│  ├─ Performance metrics
│  └─ Alerting
│
└─ Scale & optimize
   ├─ Partitioning
   ├─ Parallel processing
   ├─ Caching
   └─ Cost optimization
""",

    "Data Structures & Algorithms": """
Data Structures & Algorithms
├─ Understand the problem
│  ├─ Input format
│  ├─ Output format
│  ├─ Constraints
│  └─ Edge cases
│
├─ Choose data structure
│  ├─ Array/List (sequential)
│  ├─ Hash Map/Set (fast lookup)
│  ├─ Stack/Queue (LIFO/FIFO)
│  ├─ Tree/Graph (hierarchical)
│  └─ Heap (priority)
│
├─ Design algorithm
│  ├─ Brute force first
│  ├─ Identify pattern
│  │  ├─ Two pointers
│  │  ├─ Sliding window
│  │  ├─ BFS/DFS
│  │  ├─ Dynamic programming
│  │  └─ Divide & conquer
│  └─ Optimize
│
├─ Implement
│  ├─ Write clean code
│  ├─ Handle edge cases
│  └─ Test with examples
│
└─ Analyze complexity
   ├─ Time: O(?)
   ├─ Space: O(?)
   └─ Can we do better?
""",

    "System Design": """
System Design
├─ Requirements (5 min)
│  ├─ Functional requirements
│  │  ├─ What features?
│  │  └─ What queries?
│  ├─ Non-functional requirements
│  │  ├─ Scale (QPS, data volume)
│  │  ├─ Latency (ms, sec, min)
│  │  └─ Availability (99.9%?)
│  └─ Constraints
│
├─ High-level design (10 min)
│  ├─ Draw architecture
│  ├─ Data flow
│  ├─ Main components
│  └─ Technology choices
│
├─ Deep dive (20 min)
│  ├─ Data ingestion
│  │  ├─ Batch or stream?
│  │  ├─ Message queue (Kafka)
│  │  └─ Load balancer
│  ├─ Data processing
│  │  ├─ Spark, Flink, Dataflow
│  │  ├─ Transformation logic
│  │  └─ Aggregations
│  ├─ Data storage
│  │  ├─ Data lake (S3, GCS)
│  │  ├─ Data warehouse (Snowflake, BigQuery)
│  │  ├─ Database (PostgreSQL, Cassandra)
│  │  └─ Cache (Redis)
│  └─ Data serving
│     ├─ APIs
│     ├─ Dashboards
│     └─ ML models
│
├─ Scalability
│  ├─ Horizontal scaling
│  ├─ Partitioning/Sharding
│  ├─ Replication
│  └─ Auto-scaling
│
├─ Reliability
│  ├─ Fault tolerance
│  ├─ Retry mechanisms
│  ├─ Dead letter queue
│  └─ Disaster recovery
│
└─ Trade-offs
   ├─ Consistency vs Availability
   ├─ Latency vs Throughput
   ├─ Cost vs Performance
   └─ Batch vs Stream
""",

    "Data Modeling": """
Data Modeling
├─ Understand use cases
│  ├─ What queries?
│  ├─ Read vs write heavy?
│  ├─ OLTP or OLAP?
│  └─ Users & access patterns
│
├─ Identify entities
│  ├─ Business objects
│  ├─ Relationships
│  └─ Attributes
│
├─ Choose approach
│  ├─ Normalized (3NF)
│  │  ├─ Pros: No redundancy
│  │  └─ Cons: Complex joins
│  ├─ Denormalized (Star/Snowflake)
│  │  ├─ Pros: Fast reads
│  │  └─ Cons: Data redundancy
│  └─ Hybrid
│
├─ Design schema
│  ├─ Fact tables (metrics)
│  ├─ Dimension tables (attributes)
│  ├─ Primary keys
│  ├─ Foreign keys
│  └─ Indexes
│
└─ Optimize
   ├─ Partitioning
   ├─ Clustering keys
   ├─ Materialized views
   └─ Compression
""",

    "SQL": """
SQL
├─ Understand requirements
│  ├─ What output?
│  ├─ Which tables?
│  ├─ Filters/conditions?
│  └─ Aggregations needed?
│
├─ Plan query structure
│  ├─ Identify joins
│  ├─ Determine filters
│  ├─ Plan aggregations
│  └─ Consider window functions
│
├─ Write query (use CTEs)
│  ├─ WITH clause for readability
│  ├─ SELECT columns
│  ├─ FROM & JOIN
│  ├─ WHERE (filters)
│  ├─ GROUP BY
│  ├─ HAVING
│  └─ ORDER BY + LIMIT
│
├─ Optimize
│  ├─ Push down filters
│  ├─ Use indexes
│  ├─ Avoid SELECT *
│  ├─ Partition pruning
│  └─ Check EXPLAIN plan
│
└─ Handle edge cases
   ├─ NULLs (COALESCE, IS NULL)
   ├─ Duplicates (DISTINCT)
   ├─ Empty results
   └─ Data type conversions
""",

    "Data Warehousing": """
Data Warehousing
├─ Architecture choice
│  ├─ Traditional DW (on-prem)
│  ├─ Cloud DW (Snowflake, Redshift, BigQuery)
│  ├─ Data Lake (S3, ADLS, GCS)
│  └─ Data Lakehouse (Delta Lake, Iceberg)
│
├─ Schema design
│  ├─ Star schema (1 fact, N dims)
│  ├─ Snowflake schema (normalized)
│  ├─ Fact tables (metrics)
│  ├─ Dimension tables (attributes)
│  └─ SCD (Type 1/2/3)
│
├─ ETL vs ELT
│  ├─ ETL: Transform before load
│  ├─ ELT: Load then transform
│  └─ Choose based on use case
│
├─ Optimization
│  ├─ Partitioning (date, region)
│  ├─ Clustering (filter columns)
│  ├─ Materialized views
│  ├─ Compression (Parquet, ORC)
│  └─ Result caching
│
└─ Cost management
   ├─ Storage costs
   ├─ Compute costs
   ├─ Query optimization
   └─ Data lifecycle policies
""",

    "Behavioral": """
Behavioral (STAR Method)
├─ Situation
│  ├─ Context
│  ├─ Challenge
│  └─ Stakeholders
│
├─ Task
│  ├─ Your role
│  ├─ Goal
│  └─ Constraints
│
├─ Action
│  ├─ What YOU did
│  ├─ Technical decisions
│  ├─ Trade-offs considered
│  └─ Collaboration
│
└─ Result
   ├─ Quantifiable impact
   ├─ What you learned
   └─ What you'd do differently
""",

    "ETL/ELT": """
ETL/ELT
├─ Extract
│  ├─ Source systems (APIs, DBs, files)
│  ├─ Full vs incremental
│  ├─ Change Data Capture (CDC)
│  └─ Error handling
│
├─ Transform
│  ├─ Data cleaning
│  ├─ Data validation
│  ├─ Business logic
│  ├─ Aggregations
│  └─ Tools: Spark, dbt, Dataflow
│
├─ Load
│  ├─ Append vs upsert
│  ├─ Batch vs streaming
│  ├─ Idempotency
│  └─ Error recovery
│
└─ Orchestration
   ├─ Airflow, Prefect, Dagster
   ├─ DAG design
   ├─ Scheduling
   ├─ Monitoring
   └─ Alerting
""",

    "Data Quality": """
Data Quality
├─ Define quality dimensions
│  ├─ Accuracy
│  ├─ Completeness
│  ├─ Consistency
│  ├─ Timeliness
│  ├─ Validity
│  └─ Uniqueness
│
├─ Validation checks
│  ├─ Schema validation
│  ├─ Range checks
│  ├─ Null checks
│  ├─ Uniqueness checks
│  └─ Referential integrity
│
├─ Data profiling
│  ├─ Statistical analysis
│  ├─ Distribution analysis
│  ├─ Outlier detection
│  └─ Pattern recognition
│
├─ Tools
│  ├─ Great Expectations
│  ├─ deequ (AWS)
│  ├─ dbt tests
│  └─ Custom scripts
│
└─ Monitoring
   ├─ Data freshness SLAs
   ├─ Row count anomalies
   ├─ Schema drift
   └─ Data lineage
""",

    "Spark/Big Data": """
Spark & Big Data
├─ Understand Spark
│  ├─ RDDs (low-level)
│  ├─ DataFrames (structured)
│  ├─ Datasets (typed)
│  └─ Lazy evaluation
│
├─ Transformations
│  ├─ Narrow (map, filter)
│  ├─ Wide (groupBy, join)
│  ├─ Actions (collect, count, save)
│  └─ Catalyst optimizer
│
├─ Performance
│  ├─ Partitioning
│  ├─ Caching (persist, cache)
│  ├─ Broadcast joins
│  ├─ Avoid shuffles
│  └─ Tune executor memory/cores
│
├─ Data formats
│  ├─ Parquet (columnar)
│  ├─ Avro (row-based)
│  ├─ ORC (optimized)
│  └─ JSON/CSV
│
└─ Cluster management
   ├─ YARN, Mesos, K8s
   ├─ Driver vs Executor
   ├─ Dynamic allocation
   └─ Resource tuning
""",

    "Cloud Platforms": """
Cloud Platforms
├─ AWS
│  ├─ S3 (storage)
│  ├─ Redshift (DW)
│  ├─ Glue (ETL)
│  ├─ Athena (SQL)
│  ├─ EMR (Spark)
│  ├─ Kinesis (streaming)
│  └─ Lambda (serverless)
│
├─ GCP
│  ├─ GCS (storage)
│  ├─ BigQuery (DW)
│  ├─ Dataflow (ETL)
│  ├─ Dataproc (Spark)
│  ├─ Pub/Sub (messaging)
│  └─ Cloud Functions
│
└─ Azure
   ├─ ADLS (storage)
   ├─ Synapse (DW)
   ├─ Data Factory (ETL)
   ├─ Databricks (Spark)
   ├─ Event Hubs (streaming)
   └─ Functions
""",

    "Coding": """
Coding
├─ Understand problem
│  ├─ Input format
│  ├─ Output format
│  ├─ Constraints
│  └─ Edge cases
│
├─ Design approach
│  ├─ Brute force first
│  ├─ Identify pattern
│  ├─ Optimize
│  └─ Discuss trade-offs
│
├─ Implement
│  ├─ Clean code
│  ├─ Meaningful names
│  ├─ Comments for complex logic
│  ├─ Error handling
│  └─ Test as you go
│
└─ Analyze
   ├─ Time complexity
   ├─ Space complexity
   └─ Can we optimize?
""",

    "Database Design": """
Database Design
├─ Requirements
│  ├─ OLTP or OLAP?
│  ├─ Read vs write heavy?
│  ├─ Query patterns
│  └─ Scale expectations
│
├─ Schema design
│  ├─ Tables & columns
│  ├─ Primary keys
│  ├─ Foreign keys
│  ├─ Indexes
│  └─ Constraints
│
├─ Normalization
│  ├─ 1NF (atomic values)
│  ├─ 2NF (no partial dependencies)
│  ├─ 3NF (no transitive dependencies)
│  └─ When to denormalize
│
├─ Database type
│  ├─ Relational (PostgreSQL, MySQL)
│  ├─ NoSQL (MongoDB, Cassandra)
│  ├─ Key-value (Redis, DynamoDB)
│  └─ Graph (Neo4j)
│
└─ Performance
   ├─ Indexing strategy
   ├─ Partitioning
   ├─ Replication
   └─ Caching
""",

    "Monitoring & Observability": """
Monitoring & Observability
├─ Metrics
│  ├─ Pipeline success/failure
│  ├─ Data volume processed
│  ├─ Processing latency
│  ├─ Resource utilization
│  └─ Cost metrics
│
├─ Logging
│  ├─ Structured logs (JSON)
│  ├─ Log levels
│  ├─ Centralized logging
│  └─ Retention policies
│
├─ Alerting
│  ├─ Data freshness SLAs
│  ├─ Pipeline failures
│  ├─ Data quality issues
│  └─ Anomaly detection
│
├─ Tracing
│  ├─ Data lineage
│  ├─ Distributed tracing
│  └─ Bottleneck identification
│
└─ Dashboards
   ├─ Real-time health
   ├─ Historical trends
   └─ SLA compliance
""",

    "Distributed Systems": """
Distributed Systems
├─ CAP Theorem
│  ├─ Consistency
│  ├─ Availability
│  └─ Partition Tolerance
│
├─ Consistency models
│  ├─ Strong consistency
│  ├─ Eventual consistency
│  └─ Causal consistency
│
├─ Replication
│  ├─ Master-slave
│  ├─ Multi-master
│  └─ Quorum-based
│
├─ Partitioning
│  ├─ Hash-based
│  ├─ Range-based
│  └─ Consistent hashing
│
└─ Fault tolerance
   ├─ Replication
   ├─ Checkpointing
   └─ Retry mechanisms
""",

    "Streaming Data": """
Streaming Data
├─ Streaming platforms
│  ├─ Kafka
│  ├─ Kinesis
│  ├─ Pub/Sub
│  └─ Event Hubs
│
├─ Processing frameworks
│  ├─ Spark Streaming
│  ├─ Flink
│  ├─ Storm
│  └─ Kafka Streams
│
├─ Windowing
│  ├─ Tumbling (fixed)
│  ├─ Sliding (overlapping)
│  ├─ Session (gap-based)
│  └─ Watermarks
│
├─ State management
│  ├─ Stateless operations
│  ├─ Stateful operations
│  └─ Checkpointing
│
└─ Challenges
   ├─ Out-of-order events
   ├─ Late arrivals
   ├─ Exactly-once semantics
   └─ Backpressure
""",

    "Performance Optimization": """
Performance Optimization
├─ Identify bottlenecks
│  ├─ Profiling tools
│  ├─ Query execution plans
│  ├─ Resource monitoring
│  └─ Slow query logs
│
├─ Query optimization
│  ├─ Use indexes
│  ├─ Push down filters
│  ├─ Avoid SELECT *
│  ├─ Partition pruning
│  └─ Materialized views
│
├─ Data optimization
│  ├─ Compression
│  ├─ Columnar storage
│  ├─ Partitioning
│  └─ Clustering
│
├─ Compute optimization
│  ├─ Increase parallelism
│  ├─ Tune memory/CPU
│  ├─ Caching
│  └─ Broadcast joins
│
└─ Architecture optimization
   ├─ Denormalize for reads
   ├─ Pre-aggregate data
   ├─ Use CDNs
   └─ Horizontal scaling
""",

    "Schema Design": """
Schema Design
├─ Schema evolution
│  ├─ Add columns (backward compatible)
│  ├─ Remove columns (forward compatible)
│  ├─ Change types (breaking)
│  └─ Schema registry
│
├─ Data types
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
└─ Best practices
   ├─ Appropriate types
   ├─ Avoid nullable keys
   ├─ Document schema
   └─ Version schemas
""",

    "Data Governance": """
Data Governance
├─ Data privacy
│  ├─ PII handling
│  ├─ GDPR compliance
│  ├─ CCPA compliance
│  ├─ Anonymization
│  └─ Data masking
│
├─ Data security
│  ├─ Encryption at rest
│  ├─ Encryption in transit
│  ├─ Access control (IAM, RBAC)
│  ├─ Audit logs
│  └─ Retention policies
│
├─ Data quality
│  ├─ Validation
│  ├─ Profiling
│  └─ Lineage
│
├─ Metadata management
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
"""
}

TESTING_EXPLANATIONS = {
    "Data Pipeline Design": "Can you design robust, scalable data pipelines from source to destination?",
    "Data Structures & Algorithms": "Can you write efficient code to process and manipulate data at scale?",
    "System Design": "Can you architect data systems that handle TB/PB scale with high availability?",
    "Data Modeling": "Can you design schemas that are efficient, maintainable, and support business queries?",
    "SQL": "Can you write complex, optimized SQL queries for data transformation and analysis?",
    "Data Warehousing": "Do you understand modern data warehouse architectures and best practices?",
    "Behavioral": "Can you work effectively in a team and handle challenges?",
    "ETL/ELT": "Do you understand data transformation workflows and orchestration?",
    "Data Quality": "Can you ensure data reliability and trustworthiness?",
    "Spark/Big Data": "Can you process large-scale data efficiently using distributed computing?",
    "Cloud Platforms": "Are you familiar with cloud-native data services?",
    "Coding": "Can you write clean, efficient Python/Scala code for data processing?",
    "Database Design": "Can you design database schemas for different use cases?",
    "Monitoring & Observability": "Can you ensure pipeline reliability and quickly debug issues?",
    "Distributed Systems": "Do you understand distributed computing principles?",
    "Streaming Data": "Can you process real-time data streams?",
    "Performance Optimization": "Can you identify and fix performance bottlenecks?",
    "Schema Design": "Can you design flexible, maintainable schemas?",
    "Data Governance": "Do you understand data privacy, security, and compliance?"
}

# Generate Question Bank
output = []
output.append("")
output.append("╔════════════════════════════════════════════════════════════════════════════════╗")
output.append("║                                                                                ║")
output.append("║          DATA ENGINEER INTERVIEW PREPARATION FRAMEWORK                         ║")
output.append("║          Mental Models & Complete Question Bank (#1 GOAL ROLE)                 ║")
output.append("║                                                                                ║")
output.append("╚════════════════════════════════════════════════════════════════════════════════╝")
output.append("")
output.append("This framework provides comprehensive mental models for approaching each type of data")
output.append("engineer interview question. This is your #1 goal role - master these patterns!")
output.append("")
output.append("Focus on understanding the PATTERN and FRAMEWORK, not memorizing answers.")
output.append("")
output.append(f"Total Questions: {sum(len(qs) for qs in questions_by_category.values())} across {len(questions_by_category)} categories")
output.append("")
output.append("")

# Sort categories by question count (descending)
sorted_categories = sorted(questions_by_category.items(), key=lambda x: len(x[1]), reverse=True)

for category, questions in sorted_categories:
    output.append("=" * 80)
    output.append(category.upper())
    output.append("=" * 80)
    output.append("")
    output.append(f"📊 Total Questions: {len(questions)}")
    output.append("")
    output.append("🎯 What they're really testing:")
    output.append(TESTING_EXPLANATIONS.get(category, "Can you handle this type of question effectively?"))
    output.append("")
    output.append("🗺️  Mental Model Framework:")
    output.append("```")
    output.append(FRAMEWORKS.get(category, "Framework coming soon..."))
    output.append("```")
    output.append("")
    output.append(f"📝 All {len(questions)} Questions:")
    output.append("")
    
    for i, q in enumerate(questions, 1):
        output.append(f"{i}. {q['question']}")
    
    output.append("")
    output.append("")

# Write to file
output_file = 'Data_Engineer_Question_Bank.md'
with open(output_file, 'w') as f:
    f.write('\n'.join(output))

print(f"✅ Generated {output_file}")
print(f"📊 Total: {sum(len(qs) for qs in questions_by_category.values())} questions across {len(questions_by_category)} categories")
