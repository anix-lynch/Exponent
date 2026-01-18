# System Design - All Questions

**Strength:** 65% 🟢
**Roles:** Data Engineer, ML Engineer, Product Manager, Software Engineer, Technical Program Manager, BizOps Strategy

**🎯 Mental Model:**
```
System Design Framework
├─ 1. Requirements
│  ├─ Functional (what it does)
│  ├─ Non-functional (scale, latency)
│  └─ Constraints (budget, time)
│
├─ 2. High-Level Design
│  ├─ Client → API → Database
│  ├─ Key components
│  └─ Data flow
│
├─ 3. Deep Dive
│  ├─ Database schema
│  ├─ API design
│  ├─ Caching strategy
│  └─ Load balancing
│
└─ 4. Scale & Optimize
   ├─ Bottlenecks
   ├─ Sharding/replication
   └─ Monitoring
```

## All 145 Questions:

1. Design a database schema for a fitness app.
2. Design a high-tech gym.
3. Design a rewarding system.
4. What is a Medallion Architecture?
5. Design a database schema for a ride sharing app.
6. Design a data pipeline that updates hourly and powers a dashboard showing the most common Alexa user requests, broken down by country.
7. Design a data pipeline that complies with GDPR.
8. Design a system to ingest large amounts of JSON data from multiple S3 buckets
9. Design a next word prediction system.
10. Design a denoising system for sounds.
11. Design an agentic AI system that can autonomously adapt to new tasks.
12. Design a system to detect bot players.
13. Design a language detection system.
14. Design a system that offers discounts to customers.
15. Design a system that recommends the next Confluence pages a user should view.
16. Design a fake news detection system.
17. Design a monitoring system for TikTok.
18. Design an automated comment moderation system.
19. How would you design an effective chunking strategy for information in a RAG (Retrieval-Augmented Generation) system?
20. Design a system to communicate with a bank.
21. Design a machine learning system that makes stock predictions from Reddit comments.
22. Design an indexer and a retriever
23. Design a task scheduler in Python.
24. Design an auto-complete feature.
25. Design a recommender system feature for Dropbox that suggests files to users when they open the app on their phone.
26. Design a system that filters waste by detecting paper and putting it in the correct bin.
27. Design the backend architecture for Spotify.
28. Name your top three favorite products, select one, and outline a plan to scale it by tenfold.
29. Design the architecture for a hardware device that measures temperature and social distance among employees in warehouses during COVID.
30. Design the architecture for Google Maps to load in under 100ms.
31. Design a food truck's front-end and backend system.
32. You are a product manager at Facebook working on the news feed. Design a system to determine if Facebook should display an ad or a friend recommendation after every 20 posts in the feed for the users.
33. As a PM at Exponent, how would you design a system to prevent multiple users from sharing the same account or encourage unique accounts?
34. Implement an LRU cache with serialization and evolving constraints.
35. Design a file upload feature for an AI chat application.
36. Design a system to log messages in order
37. Design a distributed logging system.
38. Design Instagram.
39. Design a fire alarm for the deaf.
40. Design Amazon Prime video.
41. Design a task management system with tasks broken into sub-tasks.
42. Design a file cache system.
43. Design a system to schedule jobs in a distributed environment.
44. Design a banking system to facilitate account creation, deposits, transfers, and listing the most active accounts by total monetary activity, with commands entered via parsing CSV/JSON.
45. Design an app for renting bicycles.
46. Design a system to upgrade hundreds of thousands of machines on the Moon.
47. Design a reservation and payment system for a parking garage.
48. Design a system that ingests book reviews from Amazon.com and provides book recommendations on your website.
49. Design a peer-to-peer file distribution system that spreads a 10GB file from a single bandwidth-constrained source to thousands of interconnected hosts, each with limited input/output bandwidth, un...
50. Design a file system.
51. Design an end-to-end batching system for LLM queries.
52. Design a Yelp-like restaurant review app.
53. Design a rate limiter.
54. Design a web crawler.
55. Design a system for a rock paper scissors game.
56. Build a hit counter that tracks the number of hits in the last 5 minutes, supporting multiple keys (e.g., “a”, “b”). Then, use this counter to implement a simple rate limiter.
57. Design a metrics and logging service.
58. Design a scalable system for a token-generation service used by an LLM that needs to handle up to 100,000 requests per second.
59. System Design: Design an AirTag system.
60. Design a distributed file system.
61. Design a typeahead box for a search engine.
62. Design an online banking application.
63. Design a web crawler to download content from www.example.com without detection.
64. Design a system to map IP address ranges to geographic region labels.
65. Design a key-value store.
66. Design a performance tracking app for cyclists.
67. Design an algorithm to predict the next word or phrase one is typing on a phone.
68. Design a service like Azure Key Vault that securely stores and retrieves secrets, certificates, and keys for applications and users.
69. Design a leaderboard system.
70. Design a truck tracking system that supports filtering by truck number and includes an interface for updating driver status.
71. Design a streaming service like Netflix.
72. Design a chair for the disabled.
73. Design a user login system.
74. Design and implement logic to synchronize audio playback timing with transcript highlighting.
75. Design a URL shortener.
76. Design a DNS cache.
77. Design a visual landmark recognition system.
78. Design APIs for Facebook live commenting.
79. Design a metrics service.
80. Design a kayak rental service.
81. Design an alarm system for streaming metrics.
82. Design an agent that selects music based on real-world signals like weather.
83. Design a monitoring system for 1000 web servers.
84. Design a web scraping engine.
85. Design a system to store multiple images in a single file.
86. Design a plan to migrate an existing authentication system to a new one.
87. Design an AB test system.
88. Design a custom policy extension for an LRU Cache.
89. Design a load balancer.
90. Design a system like YouTube.
91. Design an API for searching a folder.
92. Design a marketplace where freelancers bid on contract jobs with the lowest bid winning the contract.
93. Design a currency exchange system.
94. Design a smart electric meter software system for an apartment building featuring separate dashboards for tenants and the owner, showing electricity usage by specific units and floors.
95. Design the architecture to send chargeback transactions to Visa.
96. Design a microservices architecture using Java Spring Boot.
97. Design an Applicant Tracking System (ATS).
98. Design Amazon Storage.
99. Design an LCU cache.
100. Design a messaging platform.
101. Design a fitness tracker like Nike Training Club.
102. Design a module to fetch a unique User ID from a pool of available User IDs and return the ID to the pool for later use.
103. Design a restaurant application that gives the expected waiting time based on waiters, tables, and customers.
104. Design a Tic Tac Toe game that allows remote play.
105. Design a music player application using the MVC (Model-View-Controller) architecture.
106. Design a distributed training system for a trillion-parameter language model.
107. Design a price alert tracking UI
108. Design a queue using static memory allocation.
109. Design an iterator.
110. Design a system that calculates the Peak-Period Price (surge pricing), given that it is calculated based on the number of opened apps (users) in some area divided by the number of drivers in the sa...
111. Design Instagram.
112. Design a cashless candy dispensing machine.
113. Design Twitter.
114. Design a reservation and payment system for a parking garage.
115. You're a PM in the middle of a sprint when a P1 issue arises that impacts the sprint goal due to requirements and design problems. How would you handle this?
116. Design Weather App
117. Design a radar tower model for a moving ship.
118. Design a fake news detection system.
119. Design an elevator.
120. Design a streaming service like Netflix.
121. Design a solution for attending large events and concerts.
122. Design a live event streaming system that captures user polls and allows user interaction
123. How would you scale the design of a messaging system that only involves emojis for users in Europe and US?  How would you identify the origin of traffic?
124. Design Google Street View using 1000 cars to map every address and image worldwide.
125. You are designing an A/B test on Bing. When would you run a user-tied flight versus an untied flight, and what are the benefits and drawbacks of each?
126. Design a music streaming service for Facebook.
127. Google wants to award its 5 trillionth query with a prize. How would you design this solution?
128. Design Twitch or any live streaming platform.
129. Tell me about a time when you were involved in system architecture. What components were involved and what was your role?
130. Design a voting system.
131. Design a voting app.
132. Design a solution for the world of online learning.
133. Design an airline booking system.
134. Design an app where customer listening history is collected after they have listened to a song for more than 30 seconds for analytics use.
135. Design the backend of a feature that allows users to download their data from their Facebook account.
136. Design a chess board and a Netflix recommendation engine.
137. Explain how you would design Google Play Store, including your choice of database, its structure, and rationale.
138. Design a kitchen.
139. Design a system for doctors to upload X-rays and get ML results for preliminary diagnosis.
140. Design an election system for the University of Washington.
141. Design a technical system that replaces faulty parts in a data center.
142. Explain in detail the architecture of the platform you're working on.
143. Design a video sharing app that verifies the authenticity of videos.
144. Question related to data architecture.
145. Design a group chat application.
