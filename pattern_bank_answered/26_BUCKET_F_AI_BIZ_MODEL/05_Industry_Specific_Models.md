# AI Business Models: Industry-Specific

**Category:** AI solutions tailored to specific industries (healthcare, finance, data monetization)

---

## 1. AI Healthcare Model

**Business Model:** AI solutions for diagnostics, treatment planning, and patient care

**Companies:**
- **Tempus** - AI for precision medicine (oncology data analytics)
- **PathAI** - AI-powered pathology tools for disease diagnosis
- **Suki AI** - AI assistant for healthcare documentation
- **Babylon Health** - AI-powered telemedicine and health assessments
- **Butterfly Network** - AI-powered ultrasound devices

---

### Metrics Framework

```
AI Healthcare Model Metrics
│
├─ NSM (North Star Metric)
│   └─ Patient Outcomes Improved
│       └─ Or: Clinical Revenue (for providers)
│
├─ Input KPIs
│   ├─ Revenue drivers
│   │   ├─ New healthcare provider customers
│   │   ├─ Per-patient fees (diagnostics)
│   │   ├─ Subscription/licenses (software)
│   │   └─ Device sales (if hardware)
│   │
│   ├─ Product adoption
│   │   ├─ Cases processed per month
│   │   ├─ Provider utilization rate
│   │   ├─ Feature adoption (diagnostic tools)
│   │   └─ Integration with EMR systems
│   │
│   └─ Customer health
│       ├─ Clinical accuracy rates
│       ├─ Provider satisfaction (NPS)
│       ├─ Regulatory compliance
│       └─ Patient outcomes (if measurable)
│
├─ Leading Indicators
│   ├─ Pilot program conversions
│   ├─ Clinical trial results
│   ├─ Regulatory approvals (FDA, etc.)
│   └─ Provider referrals
│
└─ Guardrails
    ├─ Regulatory compliance (FDA, HIPAA)
    ├─ Clinical accuracy / safety
    ├─ Customer concentration risk
    └─ Liability / malpractice risk
```

---

### Unit Economics

**Key Metrics:**
- **Revenue per case:** Diagnostic fee or subscription / Cases
- **CAC:** Sales cost / New provider customers
- **Clinical accuracy:** True positive rate, false positive rate (critical)
- **Regulatory cost:** FDA approval, compliance overhead

**Example (PathAI-style):**
- **Pricing:** $50-200 per pathology case (varies by complexity)
- **CAC:** $20K-50K (long sales cycle, regulatory)
- **Gross margin:** ~60-70% (after compute + operations)
- **Sales cycle:** 12-24 months (regulatory, clinical validation)

**Example (Tempus-style):**
- **Revenue model:** Data analytics platform (subscription + per-patient)
- **Average contract:** $500K-2M annually (health systems)
- **Value prop:** Better patient outcomes → cost savings
- **Regulatory:** HIPAA compliance, data privacy critical

**Optimization levers:**
- Clinical validation (prove outcomes → higher pricing)
- Regulatory approvals (FDA clearance → market access)
- Integration depth (EMR integration → stickiness)

---

## 2. AI Financial Services Model

**Business Model:** AI for trading, risk assessment, fraud detection, and customer service

**Companies:**
- **JPMorgan Chase** - AI for fraud detection, algorithmic trading
- **Robinhood** - AI-powered financial advice (planned)
- **Zest AI** - AI-driven credit underwriting
- **Palantir Technologies** - Data analytics for financial institutions
- **Kensho** - AI for financial analysis (acquired by S&P)

---

### Metrics Framework

```
AI Financial Services Model Metrics
│
├─ NSM (North Star Metric)
│   └─ Revenue Impact (fraud prevented, trading profits)
│       └─ Or: ARR (for SaaS providers)
│
├─ Input KPIs
│   ├─ Revenue drivers
│   │   ├─ New financial institution customers
│   │   ├─ Trading volume (for trading AI)
│   │   ├─ Fraud prevented (cost savings)
│   │   └─ Credit decisions improved (for underwriting)
│   │
│   ├─ Product adoption
│   │   ├─ Transactions processed
│   │   ├─ Fraud detection rate
│   │   ├─ Trading algorithm performance
│   │   └─ Credit approval accuracy
│   │
│   └─ Customer health
│       ├─ False positive rate (fraud)
│       ├─ Trading returns (alpha)
│       ├─ Regulatory compliance
│       └─ Customer satisfaction
│
├─ Leading Indicators
│   ├─ Pilot program conversions
│   ├─ Regulatory approvals
│   ├─ Performance benchmarks
│   └─ Partnership announcements
│
└─ Guardrails
    ├─ Regulatory compliance (SEC, FINRA, etc.)
    ├─ Model accuracy / risk
    ├─ False positive rates (fraud)
    └─ Customer concentration risk
```

---

### Unit Economics

**Key Metrics:**
- **Revenue per transaction:** Fee per trade or fraud check
- **Value created:** Fraud prevented ($) or trading alpha (%)
- **Model accuracy:** Precision, recall (critical for financial decisions)
- **Regulatory cost:** Compliance, audit overhead

**Example (Zest AI-style):**
- **Pricing:** $X per credit decision or subscription
- **Value prop:** Better credit decisions → lower defaults, more approvals
- **CAC:** $50K-100K (enterprise financial institutions)
- **Sales cycle:** 12-18 months (regulatory, risk assessment)

**Example (JPMorgan internal AI):**
- **Revenue impact:** Fraud prevented (millions $)
- **Cost:** Internal development + compute
- **Value:** Risk reduction, operational efficiency
- **ROI:** Measured in fraud prevented, not direct revenue

**Optimization levers:**
- Model performance (better accuracy → more value)
- Regulatory compliance (enable market access)
- Real-time processing (low latency for trading)

---

## 3. Data Monetization Model

**Business Model:** Collect and analyze data to offer insights or improve services

**Companies:**
- **Palantir Technologies** - Data analytics platforms (government/commercial)
- **Experian** - AI for credit data analysis and scoring
- **Equifax** - Credit data and analytics
- **Snowflake** - Data cloud platform (enables AI on data)
- **Databricks** - Data + AI platform

---

### Metrics Framework

```
Data Monetization Model Metrics
│
├─ NSM (North Star Metric)
│   └─ Data Platform Revenue (ARR)
│       └─ Or: Insights Revenue (for analytics)
│
├─ Input KPIs
│   ├─ Revenue drivers
│   │   ├─ New enterprise customers
│   │   ├─ Data storage/processing volume
│   │   ├─ Query/compute consumption
│   │   └─ Premium features (AI/ML)
│   │
│   ├─ Product adoption
│   │   ├─ Active users/queries
│   │   ├─ Data volume stored
│   │   ├─ AI/ML workloads
│   │   └─ Integration depth
│   │
│   └─ Customer health
│       ├─ Data platform uptime
│       ├─ Query performance
│       ├─ Customer satisfaction
│       └─ Expansion revenue
│
├─ Leading Indicators
│   ├─ Trial signups
│   ├─ Data migration projects
│   ├─ Developer engagement
│   └─ Partnership pipeline
│
└─ Guardrails
    ├─ Data privacy / compliance (GDPR, CCPA)
    ├─ Customer concentration risk
    ├─ Infrastructure costs (storage/compute)
    └─ Competitive switching
```

---

### Unit Economics

**Key Metrics:**
- **Revenue per customer:** Storage + compute + features
- **Cost per TB:** Infrastructure cost / Data stored
- **Gross margin:** Revenue - infrastructure costs
- **CAC payback:** Sales cost / Monthly platform spend

**Example (Snowflake-style):**
- **Pricing:** Pay-per-use (storage + compute credits)
- **Average customer:** $50K-500K annually (varies by usage)
- **Infrastructure cost:** ~30-40% of revenue (cloud margins)
- **Gross margin:** ~60-70% (after infrastructure)

**Example (Palantir-style):**
- **Pricing:** Enterprise contracts ($1M-10M+ annually)
- **Value prop:** Data integration + analytics + AI
- **CAC:** $200K-500K (enterprise sales)
- **Gross margin:** ~70-80% (software + services)

**Optimization levers:**
- Consumption-based pricing (align with customer value)
- AI/ML features (premium pricing)
- Data marketplace (monetize third-party data)

---

## Key Differences

| Model | Primary Revenue | Unit Economics Focus | Key Metric |
|-------|----------------|---------------------|------------|
| **Healthcare** | Per-case or subscription | Clinical accuracy, outcomes | Patient outcomes |
| **Financial Services** | SaaS or value share | Model accuracy, risk | Revenue impact |
| **Data Monetization** | Platform usage | Infrastructure margin | Platform ARR |

---

## Common Patterns

1. **Regulatory moat:** Compliance requirements create barriers to entry
2. **Data network effects:** More data → better AI → more value
3. **Outcome-based pricing:** Share in value created (fraud prevented, better outcomes)
4. **Integration depth:** EMR, trading systems, data platforms → stickiness

---

## Industry-Specific Considerations

### Healthcare
- **Regulatory:** FDA approval, HIPAA compliance
- **Liability:** Malpractice risk, clinical accuracy critical
- **Sales cycle:** Long (12-24 months, clinical validation)
- **Value prop:** Patient outcomes, cost savings

### Financial Services
- **Regulatory:** SEC, FINRA, banking regulations
- **Risk:** Model accuracy critical (false positives costly)
- **Sales cycle:** 12-18 months (risk assessment, compliance)
- **Value prop:** Risk reduction, trading alpha, fraud prevention

### Data Monetization
- **Regulatory:** GDPR, CCPA, data privacy
- **Infrastructure:** Scale matters (storage/compute costs)
- **Sales cycle:** 6-12 months (enterprise)
- **Value prop:** Data insights, AI/ML capabilities, platform efficiency
