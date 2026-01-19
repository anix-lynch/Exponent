# 🧠 Software Engineer Interview Mindmap (Systematic)

## 📚 Resources

**GitHub Repo**: https://github.com/anix-lynch/Exponent

**Source**: https://www.tryexponent.com/questions?page=1&role=swe

---

## 📊 Question Distribution

```
Problem Solving.....................  158 questions
Data Structures & Algorithms........  102 questions
Coding..............................  102 questions
System Design.......................   88 questions
Behavioral..........................   72 questions
Technical Communication.............   29 questions
APIs................................   25 questions
Project Management..................   19 questions
Leadership..........................   16 questions
Databases...........................   12 questions
Testing.............................   11 questions
Object-Oriented Design..............   10 questions
Distributed Systems.................    9 questions
Code Review.........................    7 questions
Debugging...........................    6 questions
Concurrency.........................    5 questions
Security............................    4 questions
Performance Optimization............    4 questions
Scalability.........................    2 questions
```

**Total: 575 questions across 19 categories**

---

## 🔟 How to USE this in interviews

When a question comes:

1. **Name the category silently**
2. **Apply that category's framework**
3. **Speak in structured bullets**

---

## 0️⃣ Core Interview Meta-Structure (applies to EVERYTHING)

No matter the category, interviewers are testing:

- **Problem-solving ability**
- **Communication clarity**
- **Technical depth**
- **Trade-off analysis**

So every answer should follow this shape:

```
Clarify → Plan → Implement → Test → Optimize → Communicate
```

---

## 1️⃣ Data Structures & Algorithms

**What they're really testing:**
Can you solve problems efficiently using the right data structures?

**Mindmap**

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

---

## 2️⃣ System Design

**What they're really testing:**
Can you design scalable, reliable systems?

**Mindmap**

```
System Design
├─ Clarify requirements
│  ├─ Functional requirements
│  ├─ Non-functional requirements
│  ├─ Scale (users, requests, data)
│  └─ Constraints
│
├─ High-level design
│  ├─ Client
│  ├─ Load Balancer
│  ├─ Application Servers
│  ├─ Database
│  └─ Cache
│
├─ Deep dive components
│  ├─ API design
│  ├─ Database schema
│  ├─ Caching strategy
│  └─ Data flow
│
├─ Scale & optimize
│  ├─ Horizontal scaling
│  ├─ Database sharding
│  ├─ CDN
│  └─ Message queues
│
└─ Address concerns
   ├─ Bottlenecks
   ├─ Single points of failure
   ├─ Monitoring
   └─ Trade-offs
```

---

## 3️⃣ Behavioral

**What they're really testing:**
Can you work well with others and learn from experience?

**Mindmap**

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
│  ├─ Why that approach
│  ├─ How you executed
│  └─ Challenges faced
│
└─ Result
   ├─ Outcome (quantify!)
   ├─ Impact
   ├─ What you learned
   └─ What you'd do differently
```

---

## 4️⃣ Coding

**What they're really testing:**
Can you write clean, working code?

**Mindmap**

```
Coding
├─ Understand requirements
│  ├─ Input format
│  ├─ Output format
│  ├─ Constraints
│  └─ Edge cases
│
├─ Plan approach
│  ├─ Break down problem
│  ├─ Choose algorithm
│  ├─ Identify data structures
│  └─ Discuss with interviewer
│
├─ Write code
│  ├─ Start with structure
│  ├─ Implement logic
│  ├─ Handle edge cases
│  └─ Keep it readable
│
├─ Test
│  ├─ Normal cases
│  ├─ Edge cases
│  ├─ Error cases
│  └─ Walk through examples
│
└─ Optimize
   ├─ Time complexity
   ├─ Space complexity
   └─ Code quality
```

---

## 5️⃣ Object-Oriented Design

**What they're really testing:**
Can you design maintainable, extensible code?

**Mindmap**

```
Object-Oriented Design
├─ Clarify requirements
│  ├─ Use cases
│  ├─ Actors
│  └─ Constraints
│
├─ Identify classes
│  ├─ Nouns → Classes
│  ├─ Verbs → Methods
│  └─ Relationships
│
├─ Define relationships
│  ├─ Inheritance (is-a)
│  ├─ Composition (has-a)
│  └─ Association
│
├─ Apply principles
│  ├─ Single Responsibility
│  ├─ Open/Closed
│  ├─ Liskov Substitution
│  ├─ Interface Segregation
│  └─ Dependency Inversion
│
└─ Consider patterns
   ├─ Singleton
   ├─ Factory
   ├─ Observer
   ├─ Strategy
   └─ Decorator
```

---

## 6️⃣ Distributed Systems

**What they're really testing:**
Do you understand challenges of distributed computing?

**Mindmap**

```
Distributed Systems
├─ Understand requirements
│  ├─ Scale
│  ├─ Consistency needs
│  └─ Availability needs
│
├─ Key concepts
│  ├─ CAP Theorem
│  ├─ Consistency models
│  ├─ Partition tolerance
│  └─ Eventual consistency
│
├─ Design patterns
│  ├─ Sharding
│  ├─ Replication
│  ├─ Load balancing
│  └─ Message queues
│
└─ Handle failures
   ├─ Retry logic
   ├─ Circuit breakers
   ├─ Fallbacks
   └─ Monitoring
```

---

## 7️⃣ Databases

**What they're really testing:**
Can you design and query databases effectively?

**Mindmap**

```
Databases
├─ Choose database type
│  ├─ SQL (relational)
│  ├─ NoSQL (document, key-value)
│  └─ Graph, Time-series
│
├─ Design schema
│  ├─ Tables/Collections
│  ├─ Relationships
│  ├─ Indexes
│  └─ Normalization
│
├─ Write queries
│  ├─ SELECT / WHERE
│  ├─ JOIN
│  ├─ GROUP BY / HAVING
│  └─ Subqueries / CTEs
│
└─ Optimize
   ├─ Indexing strategy
   ├─ Query optimization
   ├─ Caching
   └─ Partitioning
```

---

## 8️⃣ APIs

**What they're really testing:**
Can you design clean, usable APIs?

**Mindmap**

```
APIs
├─ Design principles
│  ├─ RESTful conventions
│  ├─ Resource naming
│  ├─ HTTP methods
│  └─ Status codes
│
├─ Define endpoints
│  ├─ GET /resources
│  ├─ POST /resources
│  ├─ PUT /resources/:id
│  └─ DELETE /resources/:id
│
├─ Request/Response
│  ├─ Headers
│  ├─ Body format (JSON)
│  ├─ Pagination
│  └─ Error handling
│
└─ Best practices
   ├─ Versioning
   ├─ Authentication
   ├─ Rate limiting
   └─ Documentation
```

---

## 9️⃣ Testing

**What they're really testing:**
Do you write testable, reliable code?

**Mindmap**

```
Testing
├─ Test types
│  ├─ Unit tests
│  ├─ Integration tests
│  ├─ End-to-end tests
│  └─ Performance tests
│
├─ Write test cases
│  ├─ Happy path
│  ├─ Edge cases
│  ├─ Error cases
│  └─ Boundary conditions
│
├─ Test-Driven Development
│  ├─ Write test first
│  ├─ Make it fail
│  ├─ Write minimal code
│  └─ Refactor
│
└─ Best practices
   ├─ Test coverage
   ├─ Mocking/Stubbing
   ├─ Continuous Integration
   └─ Test maintainability
```

---

## 🔟 Performance Optimization

**What they're really testing:**
Can you identify and fix performance bottlenecks?

**Mindmap**

```
Performance Optimization
├─ Identify bottleneck
│  ├─ Profiling
│  ├─ Monitoring
│  └─ Metrics
│
├─ Analyze
│  ├─ Time complexity
│  ├─ Space complexity
│  ├─ I/O operations
│  └─ Network calls
│
├─ Optimize
│  ├─ Algorithm improvement
│  ├─ Caching
│  ├─ Database indexing
│  ├─ Lazy loading
│  └─ Parallel processing
│
└─ Measure
   ├─ Before/after metrics
   ├─ A/B testing
   └─ Continuous monitoring
```

---

## Next Steps

If you want, I can:

- Turn this into a **1-page printable cheat sheet**
- Create **daily practice loops**
- Simulate **mock interviews** using this mindmap
- Map **which categories show up at which companies**
