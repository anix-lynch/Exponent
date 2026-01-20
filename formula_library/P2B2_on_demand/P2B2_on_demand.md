# P2B2 - On-Demand Metrics

**Formula:** `Define NSM → Input KPIs → Leading Indicators → Guardrails`

**Key Metrics:** Time to match, driver utilization, delivery time, ETA accuracy, supply/demand balance

---

## 🧠 Mental Model (ASCII Tree)

```
On-Demand Metrics
│
├─ NSM (North Star Metric)
│   └─ Time to Match / Delivery Time
│       └─ Or: Supply/Demand Balance
│
├─ Input KPIs
│   ├─ Supply side
│   │   ├─ Driver utilization
│   │   ├─ Active drivers online
│   │   └─ Driver earnings
│   │
│   ├─ Demand side
│   │   ├─ Request volume
│   │   ├─ Peak hour coverage
│   │   └─ User wait time
│   │
│   └─ Matching efficiency
│       ├─ Match rate
│       ├─ ETA accuracy
│       └─ Cancellation rate
│
├─ Leading Indicators
│   ├─ Driver sign-up rate
│   ├─ Request acceptance rate
│   └─ Peak hour availability
│
└─ Guardrails
    ├─ Driver satisfaction
    ├─ User safety
    └─ Cost per transaction
```

---

## 📌 Key Metrics for On-Demand

- **Time to Match**: How quickly requests are fulfilled
- **Driver Utilization**: % of time drivers are active
- **Delivery Time**: End-to-end fulfillment time
- **ETA Accuracy**: Predicted vs actual time
- **Supply/Demand Balance**: Ratio of available supply to demand
- **Match Rate**: % of requests successfully matched

---

## 🔗 Related Patterns

- **P2A**: North Star Metric (single metric focus)
- **P2B1, P2B3-P2B9**: Other business model metrics
