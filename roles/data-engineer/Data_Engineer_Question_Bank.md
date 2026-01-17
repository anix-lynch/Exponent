
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║          DATA ENGINEER INTERVIEW PREPARATION FRAMEWORK                         ║
║          Mental Models & Complete Question Bank (#1 GOAL ROLE)                 ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

This framework provides comprehensive mental models for approaching each type of data
engineer interview question. This is your #1 goal role - master these patterns!

Focus on understanding the PATTERN and FRAMEWORK, not memorizing answers.

Total Questions: 151 across 19 categories


================================================================================
DATA PIPELINE DESIGN
================================================================================

📊 Total Questions: 76

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

📝 All 76 Questions:

1. + Share interview
2. Share interview
3. Why do you think we should not hire you?
4. I was asked this
5. Design a document processing pipeline.
6. Employee Earnings.
7. Find the number of users who called three or more people in the last week.
8. Tell me about yourself.
9. What is the project you are most proud of?
10. Is this a valid palindrome?
11. Find the container with the maximum volume of water.
12. Tell me about a skill you recently learned.
13. Why do you want to work at Anthropic?
14. + Share interview experience
15. Monthly Post Success Analysis.
16. Tell me about a relevant complex program you've managed. How did you handle stakeholder & team management, and escalating issues while prioritizing work?
17. Instagram Likes
18. Top Earning Employees
19. Reverse a Sentence
20. Top Salaries by Department
21. Lyft Ride Requests
22. Valid Parentheses
23. Why do you want to work at OpenAI?
24. Course Schedule
25. Employee Hierarchy
26. Most Recent Transaction
27. Duolingo Leaderboards
28. On DoorDash, there are missing item and wrong item issues for deliveries. How would you analyze each of them?
29. Given stock prices for the next n days, how can you maximize your profit by buying or selling one share per day?
30. Tell me about a mistake you made and what you learned from it.
31. Why do you want to work at Visa?
32. High Volume Low Success.
33. Climbing Stairs
34. Calculate Test Scores
35. You're a PM at a food delivery app where conversion rates have declined over the past week. How would you investigate the causes?

(Conversion: From users browsing to placing orders.)
36. Session Data Analysis.
37. Given an nxn grid of 1s and 0s, return the number of islands in the input.
38. Design an ETL Pipeline for a ML Platform for AWS
39. Marketing Channel Attribution
40. Why do you want to work at Atlassian?
41. What parts of OpenAI's mission statement resonate with you?
42. Rotating the Box
43. Post Success By Age Group.
44. Generate Parentheses
45. Design Netflix's Clickstream Data Pipeline
46. Build a Calculator
47. How do you influence without authority?
48. Analyze Monthly Customer Transactions
49. Roman to Integer
50. How do you approach personal growth and learning?
51. Find Customer Lifetime Value (LTV)
52. Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in clockwise spiral order.
53. Find Campaign Purchases
54. Merge two sorted lists
55. Design an ETL Pipeline for Slack for School
56. Set Matrix Zeroes
57. How do you encourage collaboration among cross-functional teams?
58. What other companies are you interviewing at and why?
59. Solve John Conway's "Game of Life".
60. Why do you want to work at Walmart Labs?
61. Fraudulent Transactions
62. Explain the differences between multithreading and multiprocessing.
63. Build a Basic Regex Parser
64. Why did you become an engineer?
65. Why do you want to work at Salesforce?
66. Why do you want to work at Discord?
67. Design a data pipeline that updates hourly and powers a dashboard showing the most common Alexa user requests, broken down by country.
68. Design a data pipeline that complies with GDPR.
69. When should you use Delta Live Tables over standard data pipelines built on Spark and Delta Lake?
70. Top k frequent elements
71. How will you develop yourself professionally as a data engineer?
72. Explain the differences between Parquet and Avro.
73. Sliding Window Maximum
74. Print all combinations of numbers from 1 to n that sum to n.
75. When should you use a job cluster instead of an all-purpose cluster?
76. What data tools have you worked with, and what specific projects did you use those tools for?


================================================================================
DATA STRUCTURES & ALGORITHMS
================================================================================

📊 Total Questions: 32

🎯 What they're really testing:
Can you solve algorithmic problems efficiently?

🗺️  Mental Model Framework:
```

Data Structures & Algorithms
├─ Understand the problem
│  ├─ Read carefully
│  ├─ Ask clarifying questions
│  ├─ Identify inputs/outputs
│  └─ Confirm edge cases
│
├─ Choose data structure
│  ├─ Array / List
│  ├─ Hash Map / Set
│  ├─ Stack / Queue
│  ├─ Tree / Graph
│  └─ Heap / Priority Queue
│
├─ Design algorithm
│  ├─ Brute force first
│  ├─ Identify patterns
│  ├─ Optimize approach
│  └─ Write pseudocode
│
├─ Implement solution
│  ├─ Write clean code
│  ├─ Handle edge cases
│  ├─ Test as you go
│  └─ Explain your thinking
│
└─ Analyze complexity
   ├─ Time: O(?)
   ├─ Space: O(?)
   └─ Can we do better?

```

📝 All 32 Questions:

1. Reverse a linked list.
2. Implement LRU Cache.
3. Given n houses in a line with money in each, find the maximum amount a robber can steal, without stealing from two adjacent houses.
4. Given an integer array nums and an integer k, return true if nums has a subarray of at least two elements whose sum is a multiple of k.
5. Merge Intervals
6. Move all zeros to the end of an array.
7. Product of Array Except Self
8. Create geographic and demographic dashboards for weekly, monthly, and yearly analytics using order data (100M daily records for 5 years) and customer data (1B customers).
9. Find the median of two sorted arrays.
10. Find a triplet in an array with a given sum.
11. Given an array, find the two sum.
12. Given the head of two singly linked lists, write a function to return the point where they intersect (if any).
13. Linked List Cycle
14. Given the root of a binary tree of integers, return the maximum path sum.
15. Given an array of task durations (in minutes), return the pairs of tasks that can be completed within 60 minutes. For example, for [1, 43, 20, 59, 30, 30], return [[0, 3], [4, 5]].
16. Split an array into equal sum subarrays
17. Which sorting algorithms use divide and conquer?
18. Merge k sorted linked lists.
19. Search in rotated sorted array
20. Find the maximum subarray sum.
21. Squares of sorted array
22. Determine if a given binary tree is a binary search tree (BST).
23. Partition an array into two sub-arrays with equal sum.
24. Implement a hashmap without using any libraries.
25. Calculate the trapped rainwater between bars in a given array.
26. Determine if an array of integers from 1 to n contains a duplicate in constant time and space.
27. Find the lowest common ancestor (LCA) of two nodes in a binary tree.
28. Find the longest palindromic subsequence using dynamic programming.
29. Serialize and deserialize binary tree
30. Calculate the height of a binary tree.
31. Given an array of children’s ratings, assign at least one candy to each child so that higher-rated children get more than their neighbors, and return the minimum total candies needed.
32. Given a large set of CSV files with thousands of paragraphs each, how would you detect duplicates within each file, and how would you scale this solution for many files?


================================================================================
SYSTEM DESIGN
================================================================================

📊 Total Questions: 20

🎯 What they're really testing:
Can you design large-scale data systems?

🗺️  Mental Model Framework:
```

System Design (Data Engineering Focus)
├─ Clarify requirements
│  ├─ Functional requirements
│  ├─ Data volume (TB? PB?)
│  ├─ Query patterns
│  ├─ Latency requirements
│  └─ Consistency needs
│
├─ High-level architecture
│  ├─ Data sources
│  ├─ Ingestion layer
│  ├─ Processing layer
│  ├─ Storage layer
│  └─ Serving layer
│
├─ Data flow design
│  ├─ Batch pipelines
│  ├─ Streaming pipelines
│  ├─ Lambda architecture
│  └─ Kappa architecture
│
├─ Storage strategy
│  ├─ Hot vs cold data
│  ├─ Partitioning strategy
│  ├─ Indexing strategy
│  └─ Compression
│
├─ Scale & optimize
│  ├─ Horizontal scaling
│  ├─ Sharding
│  ├─ Caching
│  └─ CDN
│
└─ Address concerns
   ├─ Data quality
   ├─ Fault tolerance
   ├─ Monitoring
   └─ Cost

```

📝 All 20 Questions:

1. Design a document processing pipeline.
2. Design a database schema for a fitness app.
3. Design a data warehouse schema for Instagram.
4. Design a high-tech gym.
5. Design a Data Warehouse Schema for a Ride-Sharing Service
6. Design an ETL Pipeline for a ML Platform for AWS
7. Design a Data Warehouse Schema for Stripe
8. Design a data warehouse schema for Spotify.
9. Design a data warehouse schema for Amazon.
10. Design Netflix's Clickstream Data Pipeline
11. Design a Data Warehouse Schema for Customer Support
12. Design a Data Warehouse Schema for Airbnb
13. Design an ETL Pipeline for Slack for School
14. Design a rewarding system.
15. What is a Medallion Architecture?
16. Design a database schema for a ride sharing app.
17. Design a data warehouse schema for LinkedIn.
18. Design a data pipeline that updates hourly and powers a dashboard showing the most common Alexa user requests, broken down by country.
19. Design a data pipeline that complies with GDPR.
20. Design a system to ingest large amounts of JSON data from multiple S3 buckets


================================================================================
DATA MODELING
================================================================================

📊 Total Questions: 12

🎯 What they're really testing:
Can you design effective data models for analytics and applications?

🗺️  Mental Model Framework:
```

Data Modeling
├─ Understand use cases
│  ├─ What queries?
│  ├─ What reports?
│  ├─ What analytics?
│  └─ What applications?
│
├─ Identify entities
│  ├─ Users, Products, Orders
│  ├─ Events, Sessions
│  ├─ Transactions
│  └─ Relationships
│
├─ Choose modeling approach
│  ├─ Normalized (3NF)
│  ├─ Denormalized
│  ├─ Star schema
│  ├─ Snowflake schema
│  └─ Data vault
│
├─ Design tables
│  ├─ Fact tables
│  ├─ Dimension tables
│  ├─ Bridge tables
│  └─ Keys (PK, FK, SK)
│
├─ Define granularity
│  ├─ Transaction level
│  ├─ Daily aggregates
│  ├─ User level
│  └─ Time periods
│
└─ Optimize for queries
   ├─ Indexing strategy
   ├─ Partitioning
   ├─ Materialized views
   └─ Pre-aggregation

```

📝 All 12 Questions:

1. Design a database schema for a fitness app.
2. Given a bookstore database schema, write SQL queries using joins and aggregations to answer questions about sales, inventory, and customer data.
3. Design a data warehouse schema for Instagram.
4. Design a Data Warehouse Schema for a Ride-Sharing Service
5. Design a Data Warehouse Schema for Stripe
6. Design a data warehouse schema for Spotify.
7. Design a data warehouse schema for Amazon.
8. Design a Data Warehouse Schema for Customer Support
9. Design a Data Warehouse Schema for Airbnb
10. Tell me about your e-commerce experience.
11. Design a database schema for a ride sharing app.
12. Design a data warehouse schema for LinkedIn.


================================================================================
SQL
================================================================================

📊 Total Questions: 12

🎯 What they're really testing:
Can you write efficient SQL for data transformation and analysis?

🗺️  Mental Model Framework:
```

SQL (Data Engineering Focus)
├─ Understand requirements
│  ├─ What output?
│  ├─ What aggregation?
│  ├─ What filters?
│  └─ What performance needs?
│
├─ Identify tables & joins
│  ├─ Which tables?
│  ├─ Join keys
│  ├─ Join type (INNER/LEFT/etc)
│  └─ Join order
│
├─ Write query structure
│  ├─ SELECT (what columns)
│  ├─ FROM & JOIN
│  ├─ WHERE (filters)
│  ├─ GROUP BY (aggregation)
│  ├─ HAVING (post-agg filter)
│  ├─ ORDER BY + LIMIT
│  └─ Window functions
│
├─ Optimize
│  ├─ Use indexes
│  ├─ Avoid subqueries if possible
│  ├─ Use CTEs for readability
│  ├─ Partition pruning
│  └─ Push down filters
│
└─ Validate
   ├─ Check edge cases
   ├─ NULL handling
   ├─ Test with sample data
   └─ Explain plan

```

📝 All 12 Questions:

1. SQL Stored Procedures
2. Write a query to find the top 3 unique salaries in each department and list all employees who have those salaries.
3. Given a bookstore database schema, write SQL queries using joins and aggregations to answer questions about sales, inventory, and customer data.
4. Find the longest substring without repeating characters.
5. Write a query to find all dates where the stadium had three or more consecutive days with attendance of 100 or more people.
6. Write SQL code to publish the Fibonacci series.
7. Explain the key differences between BETWEEN and HAVING clauses in SQL.
8. What is the difference between NoSQL and SQL?
9. How would you handle slow query performance for a single-user SQL endpoint in Databricks, where all sequentially run queries are affected?
10. What is the best way to connect SQL databases and why?
11. How would you handle scheduling dependencies between two nightly Jobs to ensure the second Job does not fail if the first Job runs longer than expected?
12. How would you handle a task in a nightly job that fails unexpectedly during 10 percent of the runs?


================================================================================
DATA WAREHOUSING
================================================================================

📊 Total Questions: 10

🎯 What they're really testing:
Do you understand data warehouse concepts and best practices?

🗺️  Mental Model Framework:
```

Data Warehousing
├─ Architecture
│  ├─ Source systems
│  ├─ Staging layer
│  ├─ Integration layer
│  ├─ Presentation layer
│  └─ Semantic layer
│
├─ Modeling approaches
│  ├─ Kimball (dimensional)
│  ├─ Inmon (normalized)
│  ├─ Data vault
│  └─ Hybrid
│
├─ Schema design
│  ├─ Star schema
│  ├─ Snowflake schema
│  ├─ Fact tables
│  └─ Dimension tables (SCD)
│
├─ Performance optimization
│  ├─ Partitioning
│  ├─ Clustering
│  ├─ Indexing
│  ├─ Materialized views
│  └─ Caching
│
└─ Modern platforms
   ├─ Snowflake
   ├─ Redshift
   ├─ BigQuery
   └─ Databricks

```

📝 All 10 Questions:

1. What's the difference between a data lakehouse and a data warehouse?
2. Design a data warehouse schema for Instagram.
3. Design a Data Warehouse Schema for a Ride-Sharing Service
4. Design a Data Warehouse Schema for Stripe
5. Design a data warehouse schema for Spotify.
6. Design a data warehouse schema for Amazon.
7. Design a Data Warehouse Schema for Customer Support
8. Design a Data Warehouse Schema for Airbnb
9. Design a data warehouse schema for LinkedIn.
10. What is the difference between OLTP and OLAP?


================================================================================
BEHAVIORAL
================================================================================

📊 Total Questions: 5

🎯 What they're really testing:
Can you work effectively in a team and learn from experience?

🗺️  Mental Model Framework:
```

Behavioral (STAR Method)
├─ Situation
│  ├─ Context
│  ├─ Challenge
│  ├─ Data scale
│  └─ Stakeholders
│
├─ Task
│  ├─ Your role
│  ├─ Technical goal
│  ├─ Business goal
│  └─ Timeline
│
├─ Action
│  ├─ What YOU did
│  ├─ Technologies used
│  ├─ How you designed it
│  └─ How you optimized
│
└─ Result
   ├─ Outcome (quantify!)
   ├─ Performance metrics
   ├─ Business impact
   └─ What you learned

```

📝 All 5 Questions:

1. Tell me about a time you made a mistake.
2. Tell me about a time you disagreed with someone and how you resolved it.
3. Tell me about your past projects.
4. What types of team members do you find difficult to work with?
5. Can you provide an example of how you manage conflict?


================================================================================
ETL/ELT
================================================================================

📊 Total Questions: 4

🎯 What they're really testing:
Can you design and implement data transformation workflows?

🗺️  Mental Model Framework:
```

ETL/ELT
├─ Extract
│  ├─ Source systems (APIs, DBs, files)
│  ├─ Full vs incremental
│  ├─ Change data capture
│  └─ Error handling
│
├─ Transform (ETL) or Load first (ELT)
│  ├─ ETL: Transform before load
│  │  └─ Use when: limited compute in warehouse
│  └─ ELT: Load then transform
│     └─ Use when: powerful warehouse (Snowflake)
│
├─ Transformation logic
│  ├─ Data cleaning
│  ├─ Data validation
│  ├─ Business rules
│  ├─ Joins & enrichment
│  └─ Aggregations
│
├─ Load
│  ├─ Target system
│  ├─ Load strategy (append, upsert, replace)
│  ├─ Batch size
│  └─ Error handling
│
└─ Orchestrate
   ├─ Dependencies
   ├─ Scheduling
   ├─ Monitoring
   └─ Alerting

```

📝 All 4 Questions:

1. Design an ETL Pipeline for a ML Platform for AWS
2. Design an ETL Pipeline for Slack for School
3. When should you use Delta Live Tables over standard data pipelines built on Spark and Delta Lake?
4. What is delta lake?


================================================================================
DATA QUALITY
================================================================================

📊 Total Questions: 4

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 4 Questions:

1. Remove Duplicate Emails
2. Find the Duplicates
3. Determine if an array of integers from 1 to n contains a duplicate in constant time and space.
4. Given a large set of CSV files with thousands of paragraphs each, how would you detect duplicates within each file, and how would you scale this solution for many files?


================================================================================
SPARK/BIG DATA
================================================================================

📊 Total Questions: 4

🎯 What they're really testing:
Can you process large-scale data with Spark?

🗺️  Mental Model Framework:
```

Spark / Big Data
├─ Understand Spark basics
│  ├─ RDD vs DataFrame vs Dataset
│  ├─ Transformations vs Actions
│  ├─ Lazy evaluation
│  └─ DAG execution
│
├─ Read data
│  ├─ File formats (Parquet, ORC, CSV)
│  ├─ Partitioning
│  ├─ Schema inference
│  └─ Sampling
│
├─ Transform data
│  ├─ Select, filter, where
│  ├─ GroupBy, aggregate
│  ├─ Joins (broadcast, shuffle)
│  ├─ Window functions
│  └─ UDFs
│
├─ Optimize
│  ├─ Partitioning strategy
│  ├─ Broadcast joins
│  ├─ Caching
│  ├─ Coalesce vs repartition
│  └─ Avoid shuffles
│
└─ Write data
   ├─ Output format
   ├─ Partitioning
   ├─ Compression
   └─ Write mode

```

📝 All 4 Questions:

1. When is Hadoop better than PySpark?
2. What is Pyspark?
3. When should you use Delta Live Tables over standard data pipelines built on Spark and Delta Lake?
4. Explain the differences between wide and narrow dependencies in Apache Spark.


================================================================================
CLOUD PLATFORMS
================================================================================

📊 Total Questions: 3

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 3 Questions:

1. Design an ETL Pipeline for a ML Platform for AWS
2. How would you handle slow query performance for a single-user SQL endpoint in Databricks, where all sequentially run queries are affected?
3. Design a system to ingest large amounts of JSON data from multiple S3 buckets


================================================================================
CODING
================================================================================

📊 Total Questions: 3

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 3 Questions:

1. Write SQL code to publish the Fibonacci series.
2. Write a function to return all prime numbers up to a given number n.
3. Print all possible solutions to the N-Queens problem.


================================================================================
DATABASE DESIGN
================================================================================

📊 Total Questions: 3

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 3 Questions:

1. What is the difference between NoSQL and SQL?
2. What is the best way to connect SQL databases and why?
3. What types of indexes are in a relational database?


================================================================================
MONITORING & OBSERVABILITY
================================================================================

📊 Total Questions: 2

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 2 Questions:

1. Create geographic and demographic dashboards for weekly, monthly, and yearly analytics using order data (100M daily records for 5 years) and customer data (1B customers).
2. Design a data pipeline that updates hourly and powers a dashboard showing the most common Alexa user requests, broken down by country.


================================================================================
DISTRIBUTED SYSTEMS
================================================================================

📊 Total Questions: 1

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 1 Questions:

1. Partition an array into two sub-arrays with equal sum.


================================================================================
STREAMING DATA
================================================================================

📊 Total Questions: 1

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 1 Questions:

1. Design Netflix's Clickstream Data Pipeline


================================================================================
PERFORMANCE OPTIMIZATION
================================================================================

📊 Total Questions: 1

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 1 Questions:

1. How would you handle slow query performance for a single-user SQL endpoint in Databricks, where all sequentially run queries are affected?


================================================================================
SCHEMA DESIGN
================================================================================

📊 Total Questions: 1

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 1 Questions:

1. What types of indexes are in a relational database?


================================================================================
DATA GOVERNANCE
================================================================================

📊 Total Questions: 1

🎯 What they're really testing:
Can you handle this aspect of data engineering?

🗺️  Mental Model Framework:
```

General DE Approach
├─ Understand requirements
├─ Design solution
├─ Implement efficiently
├─ Test thoroughly
└─ Monitor & optimize

```

📝 All 1 Questions:

1. Design a data pipeline that complies with GDPR.


