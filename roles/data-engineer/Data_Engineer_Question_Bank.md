
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║          DATA ENGINEER INTERVIEW PREPARATION FRAMEWORK                         ║
║          Mental Models & Complete Question Bank (#1 GOAL ROLE)                 ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

This framework provides comprehensive mental models for approaching each type of data
engineer interview question. This is your #1 goal role - master these patterns!

Focus on understanding the PATTERN and FRAMEWORK, not memorizing answers.

Total Questions: 180 across 20 categories


================================================================================
DATA PIPELINE DESIGN 🔴
================================================================================

📊 Total Questions: 50

🎯 What they're really testing:
Can you design robust, scalable data pipelines from source to destination?

🗺️  Mental Model Framework:
```

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

```

📝 All 50 Questions:

1. 🔴 + Share interview
2. 🔴 Share interview
3. 🔴 I was asked this
4. 🔴 Design a document processing pipeline.
5. 🔴 Reverse a linked list.
6. 🔴 Find the number of users who called three or more people in the last week.
7. 🔴 Tell me about your past projects.
8. 🔴 Find the container with the maximum volume of water.
9. 🔴 Tell me about a skill you recently learned.
10. 🔴 Given n houses in a line with money in each, find the maximum amount a robber can steal, without stealing from two adjacent houses.
11. 🔴 + Share interview experience
12. 🔴 SQL Stored Procedures
13. 🔴 Given an integer array nums and an integer k, return true if nums has a subarray of at least two elements whose sum is a multiple of k.
14. 🔴 Find the longest substring without repeating characters.
15. 🔴 Given a collection of intervals, merge all overlapping intervals. Example: [[1,3],[2,6],[8,10]] → [[1,6],[8,10]]
16. 🔴 Write a query to find all dates where the stadium had three or more consecutive days with attendance of 100 or more people.
17. 🔴 Move all zeros to the end of an array.
18. 🔴 Product of Array Except Self
19. 🔴 On DoorDash, there are missing item and wrong item issues for deliveries. How would you analyze each of them?
20. 🔴 Write SQL code to publish the Fibonacci series.
21. 🔴 You're a PM at a food delivery app where conversion rates have declined over the past week. How would you investigate the causes? (Conversion: From users browsing to placing orders.)
22. 🔴 Find the median of two sorted arrays.
23. 🔴 Find a triplet in an array with a given sum.
24. 🔴 Design an ETL Pipeline for a ML Platform for AWS
25. 🔴 Given a linked list, determine if it has a cycle. If yes, return the node where the cycle begins.
26. 🔴 Given the root of a binary tree of integers, return the maximum path sum.
27. 🔴 Given an array of task durations (in minutes), return the pairs of tasks that can be completed within 60 minutes. For example, for [1, 43, 20, 59, 30, 30], return [[0, 3], [4, 5]].
28. 🔴 Split an array into equal sum subarrays
29. 🔴 Design Netflix's Clickstream Data Pipeline
30. 🔴 Which sorting algorithms use divide and conquer?
31. 🔴 Explain the key differences between BETWEEN and HAVING clauses in SQL.
32. 🔴 Merge k sorted linked lists.
33. 🔴 Given a rotated sorted array (e.g., [4,5,6,7,0,1,2]), search for a target value in O(log n) time.
34. 🔴 Find the maximum subarray sum.
35. 🔴 Given a sorted array of integers (may include negatives), return an array of the squares of each number, also sorted.
36. 🔴 Determine if a given binary tree is a binary search tree (BST).
37. 🔴 Design an ETL Pipeline for Slack for School
38. 🔴 Partition an array into two sub-arrays with equal sum.
39. 🔴 How would you handle scheduling dependencies between two nightly Jobs to ensure the second Job does not fail if the first Job runs longer than expected?
40. 🔴 Calculate the trapped rainwater between bars in a given array.
41. 🔴 Tell me about your e-commerce experience.
42. 🔴 How would you handle a task in a nightly job that fails unexpectedly during 10 percent of the runs?
43. 🔴 Find the lowest common ancestor (LCA) of two nodes in a binary tree.
44. 🔴 Find the longest palindromic subsequence using dynamic programming.
45. 🔴 Design a data pipeline that updates hourly and powers a dashboard showing the most common Alexa user requests, broken down by country.
46. 🔴 Design a data pipeline that complies with GDPR.
47. 🔴 Design an algorithm to serialize a binary tree to a string and deserialize the string back to the tree structure.
48. 🔴 Calculate the height of a binary tree.
49. 🔴 Print all possible solutions to the N-Queens problem.
50. 🔴 Given an array of children’s ratings, assign at least one candy to each child so that higher-rated children get more than their neighbors, and return the minimum total candies needed.


================================================================================
BEHAVIORAL 💗
================================================================================

📊 Total Questions: 24

🎯 What they're really testing:
Can you work effectively in a team and handle challenges?

🗺️  Mental Model Framework:
```

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

```

📝 All 24 Questions:

1. 💗 Why do you think we should not hire you?
2. 💗 Tell me about a time you made a mistake.
3. 💗 Tell me about a time you disagreed with someone and how you resolved it.
4. 💗 Tell me about yourself.
5. 💗 What is the project you are most proud of?
6. 💗 Why do you want to work at Anthropic?
7. 💗 What types of team members do you find difficult to work with?
8. 💗 Can you provide an example of how you manage conflict?
9. 💗 Tell me about a relevant complex program you've managed. How did you handle stakeholder & team management, and escalating issues while prioritizing work?
10. 💗 Why do you want to work at OpenAI?
11. 💗 Tell me about a mistake you made and what you learned from it.
12. 💗 Why do you want to work at Visa?
13. 💗 Why do you want to work at Atlassian?
14. 💗 What parts of OpenAI's mission statement resonate with you?
15. 💗 How do you influence without authority?
16. 💗 How do you approach personal growth and learning?
17. 💗 How do you encourage collaboration among cross-functional teams?
18. 💗 What other companies are you interviewing at and why?
19. 💗 Why do you want to work at Walmart Labs?
20. 💗 Why did you become an engineer?
21. 💗 Why do you want to work at Salesforce?
22. 💗 Why do you want to work at Discord?
23. 💗 How will you develop yourself professionally as a data engineer?
24. 💗 What data tools have you worked with, and what specific projects did you use those tools for?


================================================================================
DATA STRUCTURES & ALGORITHMS ⚠️ SKIP
================================================================================

📊 Total Questions: 20

🎯 What they're really testing:
Can you write efficient code to process and manipulate data at scale?

🗺️  Mental Model Framework:
```

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

```

📝 All 20 Questions:

1. ⚠️ Is this a valid palindrome?
2. ⚠️ Reverse a Sentence
3. ⚠️ ~~Valid Parentheses~~ *(incomplete - coding problem title only)*
4. ⚠️ ~~Course Schedule~~ *(incomplete - coding problem title only)*
5. ⚠️ Given stock prices for the next n days, how can you maximize your profit by buying or selling one share per day?
6. ⚠️ ~~Climbing Stairs~~ *(incomplete - coding problem title only)*
7. ⚠️ Given an nxn grid of 1s and 0s, return the number of islands in the input.
8. ⚠️ Given an array, find the two sum.
9. ⚠️ Given an m x n matrix representing a box with obstacles and stones, rotate the box 90 degrees clockwise and let stones fall due to gravity.
10. ⚠️ Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. Example: n=3 → ["((()))","(()())","(())()","()(())","()()()"]
11. ⚠️ Build a Calculator
12. ⚠️ Given a Roman numeral string (e.g., "MCMXCIV"), convert it to an integer (e.g., 1994).
13. ⚠️ Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in clockwise spiral order.
14. ⚠️ Merge two sorted lists
15. ⚠️ Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
16. ⚠️ Solve John Conway's "Game of Life".
17. ⚠️ Build a Basic Regex Parser
18. ⚠️ Top k frequent elements
19. ⚠️ Given an array of integers and a window size k, find the maximum value in each sliding window as it moves from left to right.
20. ⚠️ Print all combinations of numbers from 1 to n that sum to n.


================================================================================
SYSTEM DESIGN 🟠
================================================================================

📊 Total Questions: 20

🎯 What they're really testing:
Can you architect data systems that handle TB/PB scale with high availability?

🗺️  Mental Model Framework:
```

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

```

📝 All 20 Questions:

1. 🟠 Design a document processing pipeline.
2. 🟠 Design a database schema for a fitness app.
3. 🟠 Design a data warehouse schema for Instagram.
4. 🟠 Design a high-tech gym.
5. 🟠 Design a Data Warehouse Schema for a Ride-Sharing Service
6. 🟠 Design an ETL Pipeline for a ML Platform for AWS
7. 🟠 Design a Data Warehouse Schema for Stripe
8. 🟠 Design a data warehouse schema for Spotify.
9. 🟠 Design a data warehouse schema for Amazon.
10. 🟠 Design Netflix's Clickstream Data Pipeline
11. 🟠 Design a Data Warehouse Schema for Customer Support
12. 🟠 Design a Data Warehouse Schema for Airbnb
13. 🟠 Design an ETL Pipeline for Slack for School
14. 🟠 Design a rewarding system.
15. 🟠 What is a Medallion Architecture?
16. 🟠 Design a database schema for a ride sharing app.
17. 🟠 Design a data warehouse schema for LinkedIn.
18. 🟠 Design a data pipeline that updates hourly and powers a dashboard showing the most common Alexa user requests, broken down by country.
19. 🟠 Design a data pipeline that complies with GDPR.
20. 🟠 Design a system to ingest large amounts of JSON data from multiple S3 buckets


================================================================================
SQL 💗
================================================================================

📊 Total Questions: 19

🎯 What they're really testing:
Can you write complex, optimized SQL queries for data transformation and analysis?

🗺️  Mental Model Framework:
```

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

```

📝 All 19 Questions:

1. 💗 Write a SQL query to find the employees who earn more than their managers.
2. 💗 Write a SQL query to calculate monthly post engagement metrics: total posts, average likes per post, engagement rate, and month-over-month growth.
3. 💗 Write a query to find the top 3 unique salaries in each department and list all employees who have those salaries.
4. 💗 Write a SQL query to find the number of likes for each Instagram post in the last 30 days.
5. 💗 Write a SQL query to find the top 3 highest-earning employees in each department.
6. 💗 Write a SQL query to find the employee with the highest salary in each department.
7. 💗 ~~Lyft Ride Requests~~ *(incomplete - coding problem title only)*
8. 💗 ~~Employee Hierarchy~~ *(incomplete - coding problem title only)*
9. 💗 Write a SQL query to find the most recent transaction for each customer.
10. 💗 ~~Duolingo Leaderboards~~ *(incomplete - coding problem title only)*
11. 💗 Write a SQL query to identify products with high order volume but low success rate (< 50% fulfillment).
12. 💗 Write a SQL query to calculate the average test score for each student, excluding their lowest score.
13. 💗 Write a SQL query to analyze user session data: calculate average session duration, pages per session, and bounce rate by traffic source.
14. 💗 ~~Marketing Channel Attribution~~ *(incomplete - coding problem title only)*
15. 💗 Write a SQL query to analyze post engagement metrics (likes, comments, shares) grouped by user age ranges (18-24, 25-34, 35-44, 45+).
16. 💗 Write a SQL query to analyze customer transaction patterns: monthly revenue, average order value, customer retention rate, and identify top 10% customers by spend.
17. 💗 Find Customer Lifetime Value (LTV)
18. 💗 Write a SQL query to find all purchases made within 7 days of a marketing campaign click, grouped by campaign.
19. 💗 Write a SQL query to identify potentially fraudulent transactions: multiple transactions from same card in different cities within 1 hour, or transactions above $10,000.


================================================================================
DATA MODELING 🟡
================================================================================

📊 Total Questions: 11

🎯 What they're really testing:
Can you design schemas that are efficient, maintainable, and support business queries?

🗺️  Mental Model Framework:
```

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

```

📝 All 11 Questions:

1. 🟡 Design a database schema for a fitness app.
2. 🟡 Given a bookstore database schema, write SQL queries using joins and aggregations to answer questions about sales, inventory, and customer data.
3. 🟡 Design a data warehouse schema for Instagram.
4. 🟡 Design a Data Warehouse Schema for a Ride-Sharing Service
5. 🟡 Design a Data Warehouse Schema for Stripe
6. 🟡 Design a data warehouse schema for Spotify.
7. 🟡 Design a data warehouse schema for Amazon.
8. 🟡 Design a Data Warehouse Schema for Customer Support
9. 🟡 Design a Data Warehouse Schema for Airbnb
10. 🟡 Design a database schema for a ride sharing app.
11. 🟡 Design a data warehouse schema for LinkedIn.


================================================================================
DATA WAREHOUSING 🟡
================================================================================

📊 Total Questions: 10

🎯 What they're really testing:
Do you understand modern data warehouse architectures and best practices?

🗺️  Mental Model Framework:
```

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

```

📝 All 10 Questions:

1. 🟡 What's the difference between a data lakehouse and a data warehouse?
2. 🟡 Design a data warehouse schema for Instagram.
3. 🟡 Design a Data Warehouse Schema for a Ride-Sharing Service
4. 🟡 Design a Data Warehouse Schema for Stripe
5. 🟡 Design a data warehouse schema for Spotify.
6. 🟡 Design a data warehouse schema for Amazon.
7. 🟡 Design a Data Warehouse Schema for Customer Support
8. 🟡 Design a Data Warehouse Schema for Airbnb
9. 🟡 Design a data warehouse schema for LinkedIn.
10. 🟡 What is the difference between OLTP and OLAP?


================================================================================
SPARK/BIG DATA ⚪
================================================================================

📊 Total Questions: 7

🎯 What they're really testing:
Can you process large-scale data efficiently using distributed computing?

🗺️  Mental Model Framework:
```

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

```

📝 All 7 Questions:

1. ⚪ When is Hadoop better than PySpark?
2. ⚪ What is Pyspark?
3. ⚪ When should you use Delta Live Tables over standard data pipelines built on Spark and Delta Lake?
4. ⚪ Explain the differences between Parquet and Avro.
5. ⚪ What is delta lake?
6. ⚪ Explain the differences between wide and narrow dependencies in Apache Spark.
7. ⚪ When should you use a job cluster instead of an all-purpose cluster?


================================================================================
DATA QUALITY ⚪
================================================================================

📊 Total Questions: 5

🎯 What they're really testing:
Can you ensure data reliability and trustworthiness?

🗺️  Mental Model Framework:
```

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

```

📝 All 5 Questions:

1. ⚪ ~~Remove Duplicate Emails~~ *(incomplete - coding problem title only)*
2. ⚪ On DoorDash, there are missing item and wrong item issues for deliveries. How would you analyze each of them?
3. ⚪ Find the Duplicates
4. ⚪ Determine if an array of integers from 1 to n contains a duplicate in constant time and space.
5. ⚪ Given a large set of CSV files with thousands of paragraphs each, how would you detect duplicates within each file, and how would you scale this solution for many files?


================================================================================
CODING ⚠️ SKIP
================================================================================

📊 Total Questions: 4

🎯 What they're really testing:
Can you write clean, efficient Python/Scala code for data processing?

🗺️  Mental Model Framework:
```

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

```

📝 All 4 Questions:

1. ⚠️ Implement LRU Cache.
2. ⚠️ Given the head of two singly linked lists, write a function to return the point where they intersect (if any).
3. ⚠️ Write a function to return all prime numbers up to a given number n.
4. ⚠️ Implement a hashmap without using any libraries.


================================================================================
DATABASE DESIGN 🟡
================================================================================

📊 Total Questions: 3

🎯 What they're really testing:
Can you design database schemas for different use cases?

🗺️  Mental Model Framework:
```

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

```

📝 All 3 Questions:

1. 🟡 What is the difference between NoSQL and SQL?
2. 🟡 What is the best way to connect SQL databases and why?
3. 🟡 What types of indexes are in a relational database?


================================================================================
ETL/ELT 🟡
================================================================================

📊 Total Questions: 2

🎯 What they're really testing:
Do you understand data transformation workflows and orchestration?

🗺️  Mental Model Framework:
```

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

```

📝 All 2 Questions:

1. 🟡 Design an ETL Pipeline for a ML Platform for AWS
2. 🟡 Design an ETL Pipeline for Slack for School


================================================================================
CLOUD PLATFORMS ⚪
================================================================================

📊 Total Questions: 2

🎯 What they're really testing:
Are you familiar with cloud-native data services?

🗺️  Mental Model Framework:
```

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

```

📝 All 2 Questions:

1. ⚪ How would you handle slow query performance for a single-user SQL endpoint in Databricks, where all sequentially run queries are affected?
2. ⚪ Design a system to ingest large amounts of JSON data from multiple S3 buckets


================================================================================
PERFORMANCE OPTIMIZATION ⚪
================================================================================

📊 Total Questions: 2

🎯 What they're really testing:
Can you identify and fix performance bottlenecks?

🗺️  Mental Model Framework:
```

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

```

📝 All 2 Questions:

1. ⚪ How would you handle slow query performance for a single-user SQL endpoint in Databricks, where all sequentially run queries are affected?
2. ⚪ Explain the differences between multithreading and multiprocessing.


================================================================================
MONITORING & OBSERVABILITY ⚪
================================================================================

📊 Total Questions: 1

🎯 What they're really testing:
Can you ensure pipeline reliability and quickly debug issues?

🗺️  Mental Model Framework:
```

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

```

📝 All 1 Questions:

1. ⚪ Create geographic and demographic dashboards for weekly, monthly, and yearly analytics using order data (100M daily records for 5 years) and customer data (1B customers).


================================================================================
DISTRIBUTED SYSTEMS ⚪
================================================================================

📊 Total Questions: 0

🎯 What they're really testing:
Do you understand distributed computing principles?

🗺️  Mental Model Framework:
```

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

```

📝 All 0 Questions:



================================================================================
STREAMING DATA ⚪
================================================================================

📊 Total Questions: 0

🎯 What they're really testing:
Can you process real-time data streams?

🗺️  Mental Model Framework:
```

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

```

📝 All 0 Questions:



================================================================================
BATCH PROCESSING ⚪
================================================================================

📊 Total Questions: 0

🎯 What they're really testing:
Can you handle this type of question effectively?

🗺️  Mental Model Framework:
```
Framework coming soon...
```

📝 All 0 Questions:



================================================================================
SCHEMA DESIGN ⚪
================================================================================

📊 Total Questions: 0

🎯 What they're really testing:
Can you design flexible, maintainable schemas?

🗺️  Mental Model Framework:
```

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

```

📝 All 0 Questions:



================================================================================
DATA GOVERNANCE ⚪
================================================================================

📊 Total Questions: 0

🎯 What they're really testing:
Do you understand data privacy, security, and compliance?

🗺️  Mental Model Framework:
```

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

```

📝 All 0 Questions:


