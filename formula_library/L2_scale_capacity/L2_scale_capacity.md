# L2 - Scale & Capacity

**Formula:** `Current Load → 10× Projection → Bottlenecks → Mitigation`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "What breaks if usage grows fast?"
│
├─ 1) Current Load (WHAT do we run today?)
│   │
│   ├─ Traffic
│   │   ├─ QPS / RPS
│   │   ├─ Concurrent users
│   │   └─ Peak vs average
│   │
│   ├─ Data
│   │   ├─ Rows/day
│   │   ├─ Storage size
│   │   └─ Read/write ratio
│   │
│   └─ Resources
│       ├─ CPU / Memory
│       ├─ Network
│       └─ Third-party quotas
│
├─ 2) 10× Projection (WHAT changes at 10×?)
│   │
│   ├─ Linear growth assumptions
│   │   ├─ Traffic ×10
│   │   ├─ Data ×10
│   │   └─ Cost ×10
│   │
│   └─ Non-linear risks
│       ├─ Lock contention
│       ├─ Hot keys / hot shards
│       ├─ Fan-out explosions
│       └─ Tail latency
│
├─ 3) Bottlenecks (WHAT fails first?)
│   │
│   ├─ Compute
│   │   ├─ Single-threaded services
│   │   ├─ GC pressure
│   │   └─ Cold starts
│   │
│   ├─ Storage
│   │   ├─ Index bloat
│   │   ├─ Write amplification
│   │   └─ Slow scans
│   │
│   ├─ Network
│   │   ├─ Chatty services
│   │   └─ Cross-AZ traffic
│   │
│   └─ External deps
│       ├─ Rate limits
│       ├─ SLA violations
│       └─ Vendor outages
│
└─ 4) Mitigation (HOW do we survive?)
    │
    ├─ Architectural
    │   ├─ Caching
    │   ├─ Async / queues
    │   ├─ Sharding / partitioning
    │   └─ Backpressure
    │
    ├─ Operational
    │   ├─ Load shedding
    │   ├─ Graceful degradation
    │   └─ Feature flags
    │
    └─ Economic
        ├─ Cost caps
        ├─ Tiered SLAs
        └─ Kill switches
```

---

## 🔑 Golden Rule

Scaling isn't "can it run?"
It's **"what fails first, and is that acceptable?"**

---

## 📌 Sample: API Traffic 10× Growth

**Question:**
"What breaks if our API traffic grows 10×?"

```
Current: 2k RPS
│
├─ 10× → 20k RPS
│
├─ Bottleneck
│   ├─ DB connection pool exhausted
│   ├─ Cache hit rate drops
│   └─ Auth service rate-limited
│
└─ Mitigation
    ├─ Add Redis read-through cache
    ├─ Increase pool + shard reads
    └─ Async auth + token reuse
```

**Conclusion:** DB + auth fail first, not app code.

---

## 📊 Scale Sanity Checklist

```
Area        | Question
-------------------------------
Traffic     | Peak vs average?
State       | What is shared?
Fan-out     | 1 → N calls?
Hot spots   | Single keys/users?
Deps        | Who rate-limits us?
Cost        | Does 10× bankrupt us?
```

---

## 💬 Language That Works

* "At 10× load, the first bottleneck is likely ___."
* "This scales linearly until ___, then breaks."
* "We can survive 10× traffic but not 10× cost."

---

## 🔑 5-Second Recall

```
What do we have today?
→ What does 10× look like?
→ What breaks first?
→ How do we soften the failure?
```

If you want, next up: **L3 – Cost / ROI**, or I can compress **L2** into a **tight interview answer** you can recite under pressure.
