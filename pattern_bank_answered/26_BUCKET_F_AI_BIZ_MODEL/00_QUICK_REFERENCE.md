# AI Business Models - Quick Reference

**Purpose:** Quick scan of AI business models, metrics, and unit economics

---

## Model Categories Overview

| Category | Models | Key Companies | Primary Revenue |
|----------|--------|---------------|----------------|
| **API/Infrastructure** | API Access, Platforms, Hardware, Open-Source Freemium | OpenAI, AWS, Nvidia, Hugging Face | Per-request, compute, hardware sales, enterprise subscriptions |
| **SaaS/Enterprise** | AI SaaS, Consulting, Licensing | DataRobot, Fractal, Landing AI | Subscription, projects, licenses |
| **Consumer/Product** | Creative Tools, Enhanced Products, Content | Runway, Tesla, TikTok | Subscriptions, product sales, ads |
| **Token/Crypto** | Token Marketplace, Decentralized Network | SingularityNET, Bittensor, Ocean | Token transactions, staking |
| **Industry-Specific** | Healthcare, Finance, Data | Tempus, Zest AI, Palantir | Per-case, SaaS, platform usage |

---

## Metrics Framework (Universal)

```
SaaS / Enterprise Metrics
│
├─ NSM (North Star Metric)
│   └─ ARR (Annual Recurring Revenue)
│       └─ Or: NRR (Net Revenue Retention)
│
├─ Input KPIs
│   ├─ Revenue drivers
│   │   ├─ New customer acquisition
│   │   ├─ Expansion revenue
│   │   └─ Contract renewals
│   │
│   ├─ Product adoption
│   │   ├─ Feature usage
│   │   ├─ Seat utilization
│   │   └─ Integration adoption
│   │
│   └─ Customer health
│       ├─ Product engagement
│       ├─ Support ticket volume
│       └─ Customer satisfaction (NPS)
│
├─ Leading Indicators
│   ├─ Time to value
│   ├─ Feature adoption rate
│   └─ Expansion signal strength
│
└─ Guardrails
    ├─ Churn rate
    ├─ CAC payback period
    └─ Customer concentration risk
```

---

## Unit Economics Cheat Sheet

### SaaS Models
- **LTV:CAC ratio:** Target 3:1+
- **CAC payback:** 12-18 months
- **Gross margin:** 75-80%
- **Churn:** 5-10% annually

### API Models
- **Revenue per request:** Price per token/request
- **Cost per request:** Compute cost (GPU/inference)
- **Gross margin:** 50-70% (after compute)
- **Volume driver:** Developer adoption

### Hardware Models
- **Gross margin:** 65-70%
- **ASP:** Varies by product ($30K+ for high-end GPUs)
- **Volume driver:** AI training demand

### Consulting Models
- **Project margin:** 25-35%
- **Utilization:** 75-85% target
- **Billable rate:** $200-400/hour

### Consumer Models
- **MRR per user:** $10-35/month
- **CAC:** $20-40
- **Churn:** 5-8% monthly
- **LTV:** $200-400

---

## Key Patterns Across Models

1. **Freemium → Paid:** Free tier drives adoption
2. **Land and Expand:** Pilot → full deployment
3. **Network Effects:** More users → better AI → more value
4. **Data Flywheel:** More usage → better AI → more engagement
5. **Ecosystem Lock-in:** Software/tools increase switching costs

---

## Model-Specific Considerations

### API Access
- **Focus:** Cost per API call, volume growth
- **Key metric:** API calls/requests
- **Optimization:** Model efficiency, infrastructure scale

### SaaS
- **Focus:** ARR, NRR, churn
- **Key metric:** ARR, customer count
- **Optimization:** Product-led growth, expansion revenue

### Enterprise Consulting
- **Focus:** Project margin, utilization
- **Key metric:** TCV, billable hours
- **Optimization:** Productization, outcome-based pricing

### Consumer Products
- **Focus:** MAU, engagement, virality
- **Key metric:** DAU, time spent
- **Optimization:** Freemium conversion, network effects

### Token/Crypto
- **Focus:** TVL, transaction volume
- **Key metric:** Token transactions, staking
- **Optimization:** Token utility, network effects

### Industry-Specific
- **Focus:** Regulatory compliance, outcomes
- **Key metric:** Patient outcomes, fraud prevented, platform ARR
- **Optimization:** Clinical validation, regulatory approvals

---

## Quick Company Reference

| Company | Model | Key Metric | Revenue Model |
|---------|-------|------------|---------------|
| **OpenAI** | API Access | API calls | Per-token pricing |
| **Hugging Face** | Open-Source Freemium | Community engagement, Enterprise ARR | Enterprise subscriptions |
| **DataRobot** | AI SaaS | ARR | Subscription |
| **Nvidia** | Hardware | Units × ASP | Hardware sales |
| **Runway ML** | Creative Tools | MRR | Subscription |
| **Tesla** | Enhanced Product | Product revenue | FSD subscription |
| **TikTok** | Content Creation | DAU | Ads + subscriptions |
| **SingularityNET** | Token Marketplace | TVL | Token transactions |
| **Tempus** | Healthcare | Patient outcomes | Per-case + subscription |
| **Zest AI** | Finance | ARR | SaaS subscription |
| **Palantir** | Data Monetization | Platform ARR | Enterprise contracts |

---

## Files in This Folder

1. **01_API_Infrastructure_Models.md** - API access, platforms, hardware
2. **02_SaaS_Enterprise_Models.md** - AI SaaS, consulting, licensing
3. **03_Consumer_Product_Models.md** - Creative tools, enhanced products, content
4. **04_Token_Crypto_Models.md** - Token-based, decentralized AI
5. **05_Industry_Specific_Models.md** - Healthcare, finance, data monetization

Each file includes:
- Business model description
- Metrics framework (NSM, ARR, KPIs, Leading Indicators, Guardrails)
- Unit economics
- ASCII tree visualization
- Company examples
