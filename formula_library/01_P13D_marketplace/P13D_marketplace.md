# P13D - Marketplace / Two-Sided Platforms

**Formula:** `Sides → Value Exchange → Liquidity Risks → MVP → Balancing Levers`

**Intent:** Airbnb-style, bike sharing, mentorship, job matching. Focus on supply/demand balance, liquidity, and trust.

---

## 🧠 Mental Model (ASCII Tree)

```
Marketplace / Two-Sided Platform Design
│
├─ 1) Sides
│   ├─ Supply side
│   │   ├─ Who are suppliers?
│   │   ├─ What do they provide?
│   │   └─ What are their incentives?
│   │
│   └─ Demand side
│       ├─ Who are buyers/users?
│       ├─ What do they need?
│       └─ What are their incentives?
│
├─ 2) Value Exchange
│   ├─ What is the value exchange?
│   │   ├─ Supply → Demand value
│   │   ├─ Demand → Supply value
│   │   └─ Platform value
│   │
│   └─ How is value created?
│       ├─ Matching efficiency
│       ├─ Trust & safety
│       └─ Network effects
│
├─ 3) Liquidity Risks
│   ├─ Cold start problem
│   │   ├─ No supply → no demand
│   │   └─ No demand → no supply
│   │
│   └─ Liquidity strategies
│       ├─ Seed supply/demand
│       ├─ Incentivize early adopters
│       └─ Phased launch
│
├─ 4) MVP
│   ├─ Minimum viable marketplace
│   │   ├─ Core matching
│   │   ├─ Basic trust mechanisms
│   │   └─ Payment/transaction
│   │
│   └─ Launch strategy
│       ├─ Geographic focus
│       ├─ Category focus
│       └─ Supply-first or demand-first
│
└─ 5) Balancing Levers
    ├─ Supply/demand balance
    │   ├─ Pricing
    │   ├─ Incentives
    │   └─ Matching algorithms
    │
    └─ Success metrics
        ├─ Match rate
        ├─ Liquidity
        ├─ GMV
        └─ Take rate
```

---

## 📌 Sample Questions

- "Design a bike-sharing system for your city"
- "Design a product for making restaurant reservations"
- "Design a mentorship platform"

---

## 🎯 Key Principles

- **Two-sided focus**: Design for both supply and demand
- **Liquidity first**: Solve cold start problem
- **Trust & safety**: Critical for marketplace success
- **Balancing act**: Keep supply/demand balanced
- **Network effects**: Leverage when possible

---

## 🔗 Related Patterns

- **P2B3 (Marketplace Metrics)**: Use for marketplace metrics
- **P13A-P13C, P13E**: Other product design subcategories
