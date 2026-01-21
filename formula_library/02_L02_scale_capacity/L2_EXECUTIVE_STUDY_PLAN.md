# Executive Study Plan: L2 - Scale & Capacity
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~15 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L2 (SCALE & CAPACITY) QUESTIONS

**Even when "scale" or "capacity" isn't mentioned, look for these keywords/phrases:**

### Explicit Scale Keywords:
- "scale", "scaling", "capacity", "10x", "100x", "handle X requests"
- "bottleneck", "what breaks", "capacity planning", "bandwidth", "storage"
- "high traffic", "concurrent users", "QPS", "RPS", "throughput"

### Implicit L2 Indicators:
- **Scale questions:** "What breaks if traffic grows 10x?", "How do you scale X?", "What's the bottleneck?"
- **Capacity questions:** "How much bandwidth/storage needed?", "Estimate capacity for X", "Headcount forecasting"
- **System design at scale:** "Design system for 100k requests/sec", "Scale to X users", "Handle X traffic"

### L2 vs L5 Distinction:
- **L2 (Scale & Capacity):** "What breaks if traffic grows 10x?" → Focus: Identify bottlenecks, design for scale
- **L5 (Observability):** "How do you monitor a system?" → Focus: Metrics, alerts, dashboards

### L2 vs P12 Distinction:
- **L2 (Scale & Capacity):** "How do you scale a system?" → Focus: Technical scaling, bottlenecks
- **P12 (Operational Excellence):** "How do you ensure system reliability?" → Focus: Operational process

### Red Flags (NOT L2):
- "How do you monitor a system?" → L5 (Observability)
- "How do you ensure data quality?" → L1 (Data Trust)
- "How do you calculate ROI?" → L3 (Cost / ROI)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Scale & Capacity Framework** (HIGHEST PRIORITY)
2. ⚠️ **Capacity Planning** (MEDIUM)

**For Data Engineer:**
1. ✅ **Scale & Capacity Framework** (HIGHEST) - Core framework
2. ✅ **Capacity Planning** (HIGH) - Practical application

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Scale & Capacity Framework
**Questions:** ~10 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "What breaks if traffic grows 10x?" or "How do you scale X?" - core scale framework
- **Framework:** Current Load → 10× Projection → Bottlenecks → Mitigation
- **Current Load:** Traffic (QPS/RPS, Concurrent users, Peak vs average), Data (Rows/day, Storage size, Read/write ratio), Resources (CPU/Memory, Network, Third-party quotas)
- **10× Projection:** Linear growth assumptions (Traffic ×10, Data ×10, Cost ×10), Non-linear risks (Lock contention, Hot keys/hot shards, Fan-out explosions, Tail latency)
- **Bottlenecks:** Compute (Single-threaded services, GC pressure, Cold starts), Storage (Index bloat, Write amplification, Slow scans), Network (Chatty services, Cross-AZ traffic), External deps (Rate limits, SLA violations, Vendor outages)
- **Mitigation:** Architectural (Caching, Async/queues, Sharding/partitioning, Backpressure), Operational (Load shedding, Graceful degradation, Feature flags), Economic (Cost caps, Tiered SLAs, Kill switches)

**Concrete Examples:**
- "10x traffic: Current load (2k RPS, 100GB storage), 10x projection (20k RPS, 1TB storage), Bottlenecks (DB connection pool, cache hit rate, auth service), Mitigation (Redis cache, increase pool, async auth)"
- "Scale system: Understand current load, project 10x, identify bottlenecks, design mitigation"

**Representative Questions (Do 5 only):**
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (capacity surge angle)
- Q473: Design a scalable system for a token-generation service used by an LLM that needs to handle up to 100,000 requests per second. (high-scale system design angle)
- Q179: Create a simple model to forecast our headcount needs for the next 12-weeks as we scale up. (headcount forecasting angle)
- Q742: Estimate how much bandwidth is needed for launching YouTube TV. (bandwidth estimation angle)
- Q745: Estimate the amount of storage needed for Google Photos. (storage estimation angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When thinking about scale and capacity, I use Current Load → 10× Projection → Bottlenecks → Mitigation. First, I understand Current Load: Traffic (QPS/RPS: queries/requests per second, Concurrent users: how many users active simultaneously, Peak vs average: understand traffic patterns), Data (Rows/day: data ingestion rate, Storage size: current data volume, Read/write ratio: access patterns), Resources (CPU/Memory: compute utilization, Network: bandwidth usage, Third-party quotas: external service limits). Second, I project 10×: Linear growth assumptions (Traffic ×10: requests, users, sessions, Data ×10: storage, ingestion, processing, Cost ×10: infrastructure, services, operations), Non-linear risks (Lock contention: database locks become bottleneck, Hot keys/hot shards: uneven distribution causes hotspots, Fan-out explosions: one request triggers many downstream calls, Tail latency: p99/p999 latency degrades faster than average). Third, I identify Bottlenecks: Compute (Single-threaded services: can't parallelize, GC pressure: garbage collection overhead, Cold starts: latency spikes from initialization), Storage (Index bloat: indexes grow, queries slow, Write amplification: writes trigger more I/O, Slow scans: full table scans become expensive), Network (Chatty services: too many small requests, Cross-AZ traffic: inter-region latency and cost), External deps (Rate limits: third-party API throttling, SLA violations: external service degradation, Vendor outages: dependency failures). Finally, I design Mitigation: Architectural (Caching: reduce load on backend systems, Async/queues: decouple and buffer requests, Sharding/partitioning: distribute load across nodes, Backpressure: slow down producers when consumers are overwhelmed), Operational (Load shedding: drop low-priority requests during overload, Graceful degradation: reduce features to maintain core functionality, Feature flags: disable non-critical features under load), Economic (Cost caps: limit spending to prevent runaway costs, Tiered SLAs: different service levels for different users, Kill switches: emergency shutdowns for cost control). The key principle: Scaling isn't 'can it run?' It's 'what fails first, and is that acceptable?'"

**How to Adapt This Narrative for Each Question:**

- **Q473 (100k requests/sec token service):** Focus on high-scale system → "To design a scalable token-generation service for 100k requests/sec, I'd: Current Load (Traffic: 100k RPS target, Data: token generation rate, storage needs, Resources: CPU/memory for token generation, network bandwidth), 10× Projection (If we need to scale to 1M RPS: Linear - 10× traffic, 10× compute, Non-linear risks - lock contention in token generation, hot keys if not distributed, fan-out if each request triggers multiple operations), Bottlenecks (Compute: Token generation might be CPU-bound, single-threaded bottlenecks, GC pressure, Storage: Token storage/retrieval, index bloat, Network: Bandwidth for 100k RPS, External deps: Rate limits from LLM APIs), Mitigation (Architectural: Caching - cache common tokens, Async/queues - queue token requests, Sharding - distribute across nodes, Backpressure - slow down when overloaded, Operational: Load shedding - drop low-priority requests, Graceful degradation - reduce token quality under load, Feature flags - disable non-critical features, Economic: Cost caps - limit spending, Tiered SLAs - premium vs standard). I'd prioritize identifying the first bottleneck (likely compute or network) and design mitigation around that."

- **Q110 (Gas station 4x capacity surge):** Emphasize operational capacity → "To handle a 4x capacity surge at a gas station, I'd: Current Load (Traffic: Normal customer flow, peak times, Data: Transactions, inventory, Resources: Pumps, staff, payment systems), 4× Projection (4× customers, 4× transactions, 4× resource needs, Non-linear risks - queue buildup, payment system overload, staff burnout), Bottlenecks (Compute: Payment processing might be slow, Staff: Not enough people, Storage: Inventory might run out, Network: Payment network might be slow, External deps: Payment processor rate limits), Mitigation (Architectural: Queue management - organize customer flow, Caching - pre-authorize payments, Operational: Load shedding - prioritize high-value customers, Graceful degradation - accept cash only if payment system fails, Feature flags - disable non-essential services, Economic: Cost caps - limit discounts, Tiered service - premium vs standard). I'd focus on identifying the first bottleneck (likely payment system or staff) and mitigate that."

---

### BUCKET 2: Capacity Planning
**Questions:** ~5 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Estimate bandwidth/storage needed" or "Capacity planning" - same framework, with focus on estimation
- **Approach:** Same scale framework, with focus on capacity estimation
- **Estimation:** Current usage, Growth projection, Peak vs average, Buffer for spikes
- **Planning:** Headcount, Infrastructure, Bandwidth, Storage, Cost

**Concrete Examples:**
- "Bandwidth estimation: Current usage (X GB/day), Growth projection (10x), Peak vs average (2x peak), Buffer (20%), Total = X × 10 × 2 × 1.2"
- "Capacity planning: Understand current, project growth, identify needs, plan infrastructure"

**Representative Questions (Do 5 only):**
- Q742: Estimate how much bandwidth is needed for launching YouTube TV. (bandwidth estimation angle)
- Q745: Estimate the amount of storage needed for Google Photos. (storage estimation angle)
- Q748: Estimate the bandwidth required to support Spotify. (bandwidth estimation angle)
- Q179: Create a simple model to forecast our headcount needs for the next 12-weeks as we scale up. (headcount forecasting angle)
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (capacity planning angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When doing capacity planning, I use the same scale framework but focus on estimation. I start with Current Load: Understand current usage (Traffic, data, resources). Then I project Growth: Estimate future needs (10x, 100x, or specific growth rate). I account for Non-linear factors: Peak vs average (2-3x multiplier), Buffer for spikes (20-30% safety margin), Seasonality (holiday spikes, events). I identify Capacity needs: Headcount (People needed), Infrastructure (Servers, storage, bandwidth), Cost (Budget required). I prioritize based on Bottlenecks: What fails first? Design mitigation for that. The key is realistic estimation with buffers for uncertainty."

**How to Adapt This Narrative for Each Question:**

- **Q742 (YouTube TV bandwidth):** Focus on bandwidth estimation → "To estimate bandwidth for YouTube TV launch, I'd: Current Load (Understand: Current YouTube video streaming bandwidth, typical video bitrates, concurrent viewers), Growth Projection (Estimate: Launch target - X million users, Average watch time, Peak concurrent viewers, Video quality - 1080p, 4K), Non-linear factors (Peak vs average: 2-3x multiplier for peak hours, Buffer: 20-30% safety margin, Seasonality: Holiday spikes, events), Capacity needs (Bandwidth: Peak concurrent × bitrate × peak multiplier × buffer, Infrastructure: CDN capacity, edge servers, Cost: Bandwidth costs, CDN costs), Bottlenecks (First failure: Likely CDN capacity or bandwidth, Mitigation: CDN distribution, adaptive bitrate, caching). I'd estimate: Peak concurrent viewers × average bitrate × peak multiplier × buffer = total bandwidth needed."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Scale & Capacity Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Capacity Planning** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through scale framework in 2 minutes (Current Load → 10× Projection → Bottlenecks → Mitigation)
- [ ] Identify bottlenecks (Compute, storage, network, external deps)
- [ ] Design mitigation (Architectural, operational, economic)
- [ ] Estimate capacity (Current usage, growth projection, buffers)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the scale framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Current Load → 10× Projection → Bottlenecks → Mitigation framework**, not memorizing answers

**Remember:** L2 is about scale and capacity. The framework: Current Load → 10× Projection → Bottlenecks → Mitigation. Key principle: Scaling isn't "can it run?" It's "what fails first, and is that acceptable?"
