# L12 - Metrics Interpretation

**Formula:** `Metric Moved → Proxy Validity → Gaming Risk → Decide`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "This metric changed — should we care?"
│
├─ 1) Metric Moved (WHAT exactly changed?)
│   │
│   ├─ Direction: up / down / flat
│   ├─ Magnitude: small blip vs step-change
│   ├─ Scope: which segment, surface, cohort
│   └─ Time: one day spike vs sustained trend
│
│   ⚠ Rule: Never react to a single datapoint
│
├─ 2) Proxy Validity (DOES this metric mean what we think?)
│   │
│   ├─ Is it a proxy or the real goal?
│   ├─ How tightly is it correlated to value?
│   ├─ Leading vs lagging?
│   └─ Any known blind spots?
│
│   Example:
│   ├─ CTR ↑ but satisfaction ↓ → weak proxy
│   └─ DAU ↑ via spam → misleading
│
├─ 3) Gaming & Incentives (CAN it be manipulated?)
│   │
│   ├─ By users? (spam, bots, churn masking)
│   ├─ By teams? (optimize metric, hurt product)
│   ├─ By design? (dark patterns, forced clicks)
│   └─ By reporting? (definition drift)
│
│   ⚠ Rule: If it's tied to goals/bonuses, it WILL be gamed
│
├─ 4) Context Checks (IS this causal?)
│   │
│   ├─ Seasonality?
│   ├─ Launches / experiments?
│   ├─ External events?
│   └─ Data pipeline issues?
│
├─ 5) Decide (NOW what?)
│   │
│   ├─ Ignore → noise or bad proxy
│   ├─ Monitor → unclear, need more data
│   ├─ Investigate → signal but ambiguous
│   └─ Act → strong signal + aligned proxy
│
└─ OUTPUT: "We believe X changed because Y, so we will Z."
```

---

## 📊 Common Metric Traps

```
| Trap                    | Example                                  |
|-------------------------|------------------------------------------|
| Vanity metric           | Pageviews with no engagement              |
| Proxy drift             | CTR no longer predicts retention          |
| Metric cannibalization  | Time spent ↑ but content quality ↓        |
| Local optimization      | Team wins, company loses                  |
| Dashboard blindness     | Green metrics, red user experience        |
```

---

## 📌 Interview Example: Signup Conversion Increase

**Question:**
"Signup conversion increased 10%. Is that good?"

```
Metric
├─ Signup conversion ↑ 10%

Proxy Check
├─ Does signup → activation? Weak link

Gaming Risk
├─ Forced signup wall introduced

Context
├─ Marketing campaign changed traffic mix

Decision
└─ Investigate activation + retention before celebrating
```

---

## 💬 Power One-Liners

* "A metric moving is not the same as progress."
* "Proxies decay over time."
* "If a metric becomes a target, it stops being a metric."
* "Context beats dashboards."

---

## 🔑 5-Second Recall

```
Moved → Meaning → Gaming → Act?
```

If you want, next we can do:

* **L13 – SQL Reasoning**
* **Full L1–L12 lightning drill**
* **Map L1–L12 to real interview questions**
