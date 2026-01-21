# P2B6 - Advertising Metrics

**Formula:** `Define NSM → Input KPIs → Leading Indicators → Guardrails`

**Key Metrics:** CTR, CPC, ROAS, conversion rate, ad quality, targeting accuracy

---

## 🧠 Mental Model (ASCII Tree)

```
Advertising Metrics
│
├─ NSM (North Star Metric)                         [Platform KPI ↔ Advertiser Outcome]
│   └─ Advertiser Revenue / ROAS                   [Advertiser KPI]
│       └─ Or: Advertiser ROI                      [Advertiser KPI]
│
├─ Input KPIs
│   ├─ Performance metrics                         [Advertiser KPIs]
│   │   ├─ CTR (Click-Through Rate)                [Advertiser KPI]
│   │   ├─ CPC (Cost Per Click)                    [Advertiser KPI]
│   │   └─ Conversion rate                          [Advertiser KPI]
│   │
│   ├─ Ad quality                                  [Platform Optimization KPIs]
│   │   ├─ Ad relevance score                      [Platform KPI]
│   │   ├─ Targeting accuracy                      [Platform KPI]
│   │   └─ Ad fatigue                              [Platform KPI / UX Guardrail]
│   │
│   └─ Inventory                                   [Platform Supply-Side KPIs]
│       ├─ Ad impressions                          [Platform KPI → reported to Advertiser]
│       ├─ Fill rate                               [Platform KPI]
│       └─ CPM (Cost Per Mille)                    [Platform Revenue KPI]
│
├─ Leading Indicators
│   ├─ Ad engagement rate                           [Platform KPI → early Advertiser signal]
│   ├─ View-through rate                            [Platform KPI]
│   └─ Advertiser satisfaction                     [Platform KPI]
│
└─ Guardrails                                      [Platform Protection KPIs]
    ├─ User experience (ad load)                   [Platform KPI]
    ├─ Ad quality standards                        [Platform KPI]
    └─ Click fraud prevention                      [Platform KPI]
```

---

## 📌 Key Metrics for Advertising

- **CTR**: Click-Through Rate (% of impressions that get clicks)
- **CPC**: Cost Per Click
- **ROAS**: Return on Ad Spend
- **Conversion Rate**: % of clicks that convert
- **Ad Quality**: Relevance score, targeting accuracy
- **CPM**: Cost Per Mille (cost per 1000 impressions)

---

## 🔗 Related Patterns

- **P2A**: North Star Metric (single metric focus)
- **P2B1-P2B5, P2B7-P2B9**: Other business model metrics
