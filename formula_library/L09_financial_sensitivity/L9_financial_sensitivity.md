# L9 - Financial Sensitivity

**Formula:** `Levers (Price, Volume, Churn) → Impact → Prioritize`

---

## 🧠 Mental Model (ASCII Tree)

```
START: "What actually moves the business outcome?"
│
├─ 1) Identify Levers (WHAT can move?)
│   │
│   ├─ Price
│   │   └─ ARPU, fees, discounting
│   │
│   ├─ Volume
│   │   └─ Users, orders, sessions
│   │
│   └─ Churn
│       └─ Retention, repeat rate
│
├─ 2) Sensitivity Test (HOW sensitive is outcome?)
│   │
│   ├─ +1% Price → Δ Revenue?
│   ├─ +1% Volume → Δ Revenue?
│   └─ -1% Churn → Δ LTV?
│
│   ⚠ Rule: Use direction + relative size, not exact math
│
├─ 3) Constraints (WHAT limits each lever?)
│   │
│   ├─ Price elasticity
│   ├─ Supply / ops limits
│   ├─ Market saturation
│   └─ Competitive response
│
├─ 4) Prioritize (WHERE do we focus?)
│   │
│   ├─ High impact × low risk first
│   ├─ Short-term vs long-term split
│   └─ One primary lever (not all)
│
└─ OUTPUT: "We focus on X because it moves Y the most"
```

---

## 📊 Quick Sensitivity Grid

```
| Lever  | Impact | Risk | Control | Verdict |
|-------|--------|------|---------|---------|
| Price | High   | High | Medium  | Careful |
| Volume| Medium | Med  | Low     | Secondary |
| Churn | High   | Low  | High    | Primary |
```

---

## 🚨 Anti-Patterns (Red Flags)

```
✗ Optimizing all levers at once
✗ Ignoring elasticity / user behavior
✗ Precision math with fake numbers
✗ Confusing growth with profitability
✗ No clear "primary lever"
```

---

## 📌 Interview Example: Subscription App Profitability

**Question:**
"What moves profitability most for a subscription app?"

```
Levers
├─ Price: +5% risks churn
├─ Volume: CAC rising
└─ Churn: 1% ↓ churn = big LTV gain

Constraints
├─ Competitive pricing pressure
└─ High switching costs

Decision
└─ Focus on retention first
```

---

## 💬 One-Liners You Can Drop

* "Small churn changes compound more than price hikes."
* "Not all growth is profitable growth."
* "Sensitivity beats precision early on."
* "Pick one lever to lead, others to support."

---

## 🔑 5-Second Recall

```
Which lever moves outcome most?
→ How sensitive is it?
→ What constrains it?
→ Focus there.
```

Next if you want: **L10 – Process Optimization**, **L11 – Risk Mitigation**, or a **rapid drill: L1–L9 lightning round**.
