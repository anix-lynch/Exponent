# L14 - System Design (Conceptual)

**Formula:** `Components → Data Flow → Boundaries → Scale Considerations`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "Design X"
(NO code, NO APIs, NO schemas — architecture thinking only)
│
├─ 1) Define the GOAL (WHAT problem are we solving?)
│   │
│   ├─ Primary user goal
│   ├─ Success metric (latency, reliability, accuracy, cost)
│   └─ Non-goals (explicitly say what's out of scope)
│
│   ⚠ Rule: If the goal isn't clear, architecture will be wrong
│
├─ 2) Identify CORE COMPONENTS (WHAT blocks exist?)
│   │
│   ├─ Clients (web, mobile, internal tools)
│   ├─ Ingestion layer (APIs, SDKs, event collectors)
│   ├─ Processing layer (sync vs async)
│   ├─ Storage (hot / warm / cold)
│   ├─ Compute (stateless vs stateful)
│   ├─ Orchestration / queues
│   ├─ Observability (metrics, logs, alerts)
│   └─ Admin / control plane
│
│   ⚠ Rule: Name boxes before wiring arrows
│
├─ 3) Data FLOW (HOW data moves end-to-end)
│   │
│   ├─ Request path (read)
│   ├─ Write path (create/update)
│   ├─ Async paths (queues, streams, retries)
│   ├─ Failure paths (timeouts, backpressure)
│   └─ Control vs data plane separation
│
│   ⚠ Rule: Always describe the happy path first
│
├─ 4) Boundaries & CONSTRAINTS (WHAT limits us?)
│   │
│   ├─ Latency SLOs
│   ├─ Consistency requirements
│   ├─ Throughput limits
│   ├─ Regulatory / privacy constraints
│   ├─ Team ownership boundaries
│   └─ Cost ceilings
│
│   ⚠ Rule: Constraints shape architecture more than features
│
├─ 5) Scale & FAILURE MODES (WHAT breaks at 10×?)
│   │
│   ├─ Bottlenecks (DB, network, fan-out)
│   ├─ Single points of failure
│   ├─ Backpressure strategy
│   ├─ Caching layers
│   ├─ Sharding / partitioning
│   └─ Graceful degradation
│
│   ⚠ Rule: Talk about failure BEFORE optimization
│
└─ OUTPUT: "System of boxes + arrows, bounded by constraints,
           designed to scale and fail safely."
```

---

## 📌 Canonical Example: URL Shortening Service

**Question:**
"Design a URL shortening service"

```
Goal
├─ Shorten URLs
├─ Low latency reads
├─ High availability

Components
├─ Client
├─ API gateway
├─ ID generator
├─ URL store
├─ Cache
├─ Analytics pipeline

Data Flow
├─ Write: client → API → ID gen → DB → cache
├─ Read: client → API → cache → DB fallback

Boundaries
├─ Read-heavy
├─ Strong consistency on write
├─ Low latency (<50ms)

Scale
├─ Cache hot paths
├─ Shard by short_id
├─ Async analytics
```

---

## 🚨 Common System Design Traps

```
| Trap                     | Why It's Bad                          |
|--------------------------|----------------------------------------|
| Jumping into tech stack  | Misses architecture reasoning          |
| No failure discussion    | Signals inexperience                   |
| Over-engineering early   | Violates stated constraints            |
| Ignoring non-goals       | Scope creep                            |
| No scale story           | Design feels incomplete                |
```

---

## 💬 Interview One-Liners

* "Let me clarify the primary goal and constraints first."
* "I'll start with a simple box-and-arrow design, then scale it."
* "The read path is latency-sensitive; writes can be async."
* "At 10× traffic, this database becomes the bottleneck."

---

## 🔑 5-Second Recall

```
Goal → Components → Flow → Constraints → Scale
```

If you want next:

* **L14 vs coding system design (how to tell them apart)**
* **Fast mental templates for common systems (feeds, search, payments)**
* **Mock L14 walkthrough (you talk, I correct in real time)**
