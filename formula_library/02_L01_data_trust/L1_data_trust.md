# L1 - Data Trust

**Formula:** `Source → Freshness → Completeness → Bias → Sanity Checks`

---

## 🧠 Mental Model (ASCII Tree)

```
START: A metric looks wrong / decision depends on this data
│
├─ 1) Source (WHERE did this come from?)
│   │
│   ├─ Identify origin
│   │   ├─ Primary (product logs, first-party events)
│   │   ├─ Secondary (internal pipelines, transformations)
│   │   └─ External (vendors, partners, scraped data)
│   │
│   └─ Validate ownership
│       ├─ Who maintains it?
│       ├─ Who is on-call when it breaks?
│       └─ Is there documentation / lineage?
│
├─ 2) Freshness (IS it up to date?)
│   │
│   ├─ Expected latency
│   │   ├─ Real-time
│   │   ├─ Hourly
│   │   └─ Daily / Batch
│   │
│   └─ Check gaps
│       ├─ Last updated timestamp
│       ├─ Delays vs SLA
│       └─ Silent failures (no alerts but stale data)
│
├─ 3) Completeness (IS anything missing?)
│   │
│   ├─ Coverage checks
│   │   ├─ Missing rows / days
│   │   ├─ Null or default-heavy fields
│   │   └─ Partial segments dropped
│   │
│   └─ Join loss
│       ├─ Inner joins removing data
│       ├─ Key mismatches
│       └─ Upstream schema changes
│
├─ 4) Bias (WHO is over- or under-represented?)
│   │
│   ├─ Sampling bias
│   │   ├─ Logged-in only
│   │   ├─ Power users
│   │   └─ 특정 지역 / 플랫폼
│   │
│   └─ Measurement bias
│       ├─ Proxy ≠ true behavior
│       ├─ Instrumentation gaps
│       └─ Incentives to game metrics
│
└─ 5) Sanity Checks (DO numbers pass smell test?)
    │
    ├─ Trend checks (sharp jumps/drops)
    ├─ Ratio checks (conversion > 100%?)
    ├─ Cross-metric consistency
    └─ Compare to historical baselines
```

---

## 🔑 Golden Rule

No decision is better than a confident decision on bad data.
If trust is low → **slow down, qualify, or re-measure**.

---

## 📌 Sample: Revenue Drop Investigation

**Question:**
"Revenue dropped 20% last week — can we trust this?"

```
START: Revenue drop observed
│
├─ 1) Source
│   └─ Revenue from billing DB, owned by Finance
│
├─ 2) Freshness
│   └─ Data is T+2 days late (pipeline delay)
│
├─ 3) Completeness
│   └─ Mobile payments missing after SDK update
│
├─ 4) Bias
│   └─ Only web users counted → under-reporting
│
└─ 5) Sanity Checks
    └─ Orders flat, ARPU stable → drop is artificial
```

**Conclusion:** Data issue, not real business decline.

---

## 📊 Data Trust Checklist (Quick Fill)

```
Check        | Status | Notes
-----------------------------------------
Source       |  ✅ / ❌ | Owner, lineage
Freshness    |  ✅ / ❌ | Last update time
Completeness |  ✅ / ❌ | Missing segments
Bias         |  ✅ / ❌ | Who is excluded?
Sanity       |  ✅ / ❌ | Trends & ratios
```

---

## 💬 Language That Works

* "Before acting, let's validate whether this data is trustworthy."
* "What assumptions does this metric rely on?"
* "Which users or events might be missing here?"

---

## 🔑 5-Second Recall

```
Where did this come from?
→ Is it fresh?
→ Is anything missing?
→ Who is over/under counted?
→ Does it pass the smell test?
```

If you want, next we can do **L2 – Scale & Capacity**, or I can compress **L1** into a **30-second interview answer** you can memorize.
