# Executive Study Plan: L11 - Risk Mitigation
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~10 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L11 (RISK MITIGATION) QUESTIONS

**Even when "risk" isn't mentioned, look for these keywords/phrases:**

### Explicit Risk Keywords:
- "risk", "risks", "risk mitigation", "what could go wrong", "potential issues"
- "prevent", "protect", "safety", "security", "compliance", "privacy"
- "adversarial attacks", "data leakage", "PII exposure", "age verification"

### Implicit L11 Indicators:
- **Risk questions:** "What risks would you consider?", "What could go wrong?", "How do you prevent X?"
- **Safety questions:** "How do you keep data safe?", "How do you prevent users from X?", "Security concerns"
- **Compliance questions:** "How do you ensure compliance?", "Privacy concerns", "Regulatory risks"

### L11 vs P12 Distinction:
- **L11 (Risk Mitigation):** "What risks would you consider?" → Focus: Enumerate risks, assess blast radius, mitigate
- **P12 (Operational Excellence):** "How do you ensure system reliability?" → Focus: Operational process

### L11 vs L4 Distinction:
- **L11 (Risk Mitigation):** "What risks would you consider?" → Focus: Risk identification and mitigation
- **L4 (Constraints):** "What are the constraints?" → Focus: Legal, technical, organizational, timeline constraints

### Red Flags (NOT L11):
- "What are the constraints?" → L4 (Constraints)
- "How do you ensure system reliability?" → P12 (Operational Excellence)
- "How do you monitor a system?" → L5 (Observability)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Risk Mitigation Framework** (HIGHEST PRIORITY)
2. ✅ **Risk Types & Mitigations** (HIGH PRIORITY)

**For Data Engineer:**
1. ✅ **Risk Mitigation Framework** (HIGHEST) - Core framework
2. ✅ **Risk Types & Mitigations** (HIGH) - Practical application

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Risk Mitigation Framework
**Questions:** ~8 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "What risks would you consider?" or "What could go wrong?" - core risk mitigation framework
- **Framework:** Enumerate Risks → Blast Radius → Mitigations → Monitor
- **Enumerate Risks:** List all potential risks before judging (Technical: bugs, downtime, data loss, Data: quality, drift, leakage, bias, Operational: on-call load, handoffs, Legal/Compliance: PII, regulations, Business: revenue, trust, reputation), Rule: If you can't name it, you can't manage it
- **Assess Blast Radius:** How bad is it? (Users affected: 1% vs 100%, Duration: minutes vs weeks, Reversibility: easy rollback vs permanent, Visibility: internal vs public), Output: Risk = Probability × Impact
- **Prioritize:** NOT all risks deserve fixes (High impact + high probability → ACT, High impact + low probability → PLAN, Low impact + high probability → AUTOMATE, Low impact + low probability → ACCEPT)
- **Mitigate:** Reduce impact or probability (Prevent: guardrails, validation, limits, Detect: monitoring, alerts, Contain: rate limits, feature flags, Recover: rollback, backups, runbooks)
- **Monitor:** Assume failure will happen (Early warning metrics, Alert thresholds, Clear owner + escalation path), Output: "If X happens, we detect in Y mins and recover in Z."

**Concrete Examples:**
- "ML model launch risks: Enumerate (Prediction drift, biased outcomes, latency regression), Blast Radius (Affects all users, high visibility), Mitigation (Shadow deploy, canary rollout, drift alerts), Monitor (Auto-rollback on threshold breach)"
- "Risk mitigation: List risks, assess impact, prioritize, mitigate, monitor"

**Representative Questions (Do 5 only):**
- Q61: As a PM for Instacart, what potential issues do you foresee after a customer places an order? (risk enumeration angle)
- Q796: Explain how LLMs might be susceptible to adversarial attacks. (security/risk angle)
- Q1026: How can we prevent users under 18 years old from lying about their age during signup? (compliance/risk angle)
- Q1116: How do you identify and account for risks in a program? (risk management angle)
- Q1120: How do you keep users' data safe and private when building AI systems? (data privacy/risk angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When identifying and mitigating risks, I use Enumerate Risks → Blast Radius → Mitigations → Monitor. First, I Enumerate Risks: List all potential risks before judging. Technical (Bugs, downtime, data loss, performance degradation, system failures), Data (Quality issues, drift, leakage, bias, completeness, freshness), Operational (On-call load, handoffs, manual processes, capacity limits), Legal/Compliance (PII exposure, regulatory violations, privacy breaches), Business (Revenue loss, user trust erosion, reputation damage, competitive disadvantage). Rule: If you can't name it, you can't manage it. Be comprehensive - don't skip categories. Second, I assess Blast Radius: How bad is each risk? Users affected (1% vs 100%, specific segments vs all users), Duration (Minutes vs hours vs weeks, temporary vs permanent), Reversibility (Easy rollback vs permanent damage, recoverable vs irreversible), Visibility (Internal vs public, contained vs widespread). Output: Risk = Probability × Impact. I prioritize: High impact + high probability → ACT (Critical - fix immediately), High impact + low probability → PLAN (Plan for - prepare response), Low impact + high probability → AUTOMATE (Automate handling - reduce manual work), Low impact + low probability → ACCEPT (Accept - not worth fixing). Third, I Mitigate: Reduce impact or probability. Prevent (Guardrails, validation, limits, access controls - stop it from happening), Detect (Monitoring, alerts, anomaly detection, early warning systems - know when it happens), Contain (Rate limits, feature flags, circuit breakers, isolation - limit damage), Recover (Rollback procedures, backups, runbooks, incident response - fix when it happens). Layered approach: Multiple mitigations for high-risk items. Remember: You don't eliminate risk — you bound it. Finally, I Monitor: Assume failure will happen and prepare detection. Early warning metrics (Leading indicators that predict problems), Alert thresholds (When to trigger alerts, escalation criteria), Clear owner + escalation path (Who responds, how to escalate). Detection speed matters more than perfection. Output: 'If X happens, we detect in Y mins and recover in Z.' Test monitoring: Verify alerts work, runbooks are current, owners are reachable."

**How to Adapt This Narrative for Each Question:**

- **Q61 (Instacart order issues):** Focus on post-order risks → "To identify potential issues after an Instacart order, I'd: Enumerate Risks (Technical: Order processing failures, payment issues, app crashes, Data: Order data loss, incorrect items, pricing errors, Operational: Shopper availability, delivery delays, capacity limits, Legal/Compliance: PII exposure, payment security, Business: Customer dissatisfaction, refunds, reputation damage), Assess Blast Radius (Users affected: Single order vs all orders, Duration: Minutes vs hours, Reversibility: Can fix order vs permanent damage, Visibility: Customer-facing vs internal), Prioritize (High impact + high probability: Order failures, payment issues → ACT, High impact + low probability: Data breach → PLAN, Low impact + high probability: Minor delays → AUTOMATE, Low impact + low probability: Edge cases → ACCEPT), Mitigate (Prevent: Order validation, payment verification, guardrails, Detect: Order monitoring, payment alerts, delivery tracking, Contain: Feature flags, rate limits, circuit breakers, Recover: Order cancellation, refunds, customer support, runbooks), Monitor (Early warning: Order failure rate, payment errors, delivery delays, Alert thresholds: >1% order failures, >5% payment errors, Clear owner: On-call rotation, escalation path). I'd prioritize: Order processing (Critical - affects all orders), Payment security (High impact - trust issue), Delivery reliability (High impact - customer experience)."

- **Q1120 (AI data privacy):** Emphasize data privacy risks → "To keep users' data safe and private in AI systems, I'd: Enumerate Risks (Technical: Data breaches, model attacks, system vulnerabilities, Data: PII exposure, data leakage, bias, quality issues, Operational: Access control failures, manual errors, Legal/Compliance: GDPR violations, privacy breaches, regulatory fines, Business: User trust erosion, reputation damage, competitive disadvantage, AI-specific: Model drift, adversarial attacks, hallucination, misuse), Assess Blast Radius (Users affected: All users if breach, Duration: Permanent if data leaked, Reversibility: Irreversible if PII exposed, Visibility: Public if breach, high visibility), Prioritize (High impact + high probability: PII exposure, data breaches → ACT, High impact + low probability: Regulatory violations → PLAN, Low impact + high probability: Access control issues → AUTOMATE, Low impact + low probability: Edge cases → ACCEPT), Mitigate (Prevent: Encryption, access controls, data minimization, anonymization, guardrails, Detect: Access monitoring, anomaly detection, data quality checks, Contain: Rate limits, feature flags, isolation, Recover: Incident response, data deletion, notifications, runbooks), Monitor (Early warning: Unusual access patterns, data quality anomalies, Alert thresholds: Unauthorized access, data quality issues, Clear owner: Security team, DPO, escalation path). I'd prioritize: Data encryption (Critical - protect at rest and in transit), Access controls (High impact - limit who can access), Anonymization (High impact - reduce PII exposure), Monitoring (High impact - detect breaches early)."

---

### BUCKET 2: Risk Types & Mitigations
**Questions:** ~2 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "How do you prevent X?" or "Security concerns" - same framework, with focus on specific risk types
- **Approach:** Same risk mitigation framework, with focus on risk types and their mitigations
- **Risk Types:** Data risks, Model risks, Infra risks, Product risks, Legal risks
- **Typical Mitigations:** Data (Validation + sanity checks), Model (Drift monitoring), Infra (Rate limits + autoscaling), Product (Feature flags + phased rollout), Legal (Access control + audits)

**Concrete Examples:**
- "Data risk: Bad input → Mitigation: Validation + sanity checks"
- "Model risk: Drift → Mitigation: Drift monitoring"
- "Infra risk: Traffic spike → Mitigation: Rate limits + autoscaling"

**Representative Questions (Do 5 only):**
- Q796: Explain how LLMs might be susceptible to adversarial attacks. (security/risk angle)
- Q1026: How can we prevent users under 18 years old from lying about their age during signup? (compliance/risk angle)
- Q1120: How do you keep users' data safe and private when building AI systems? (data privacy/risk angle)
- Q61: As a PM for Instacart, what potential issues do you foresee after a customer places an order? (risk enumeration angle)
- Q1116: How do you identify and account for risks in a program? (risk management angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When dealing with specific risk types, I use the same risk mitigation framework but focus on risk-specific mitigations. For Data risks (Bad input, quality issues, leakage): Prevent (Validation, sanity checks, data quality rules), Detect (Data quality monitoring, anomaly detection), Contain (Data access controls, isolation), Recover (Data correction, deletion, notifications). For Model risks (Drift, bias, adversarial attacks): Prevent (Shadow deploys, canary rollouts, bias testing), Detect (Drift monitoring, performance alerts, bias detection), Contain (Feature flags, model versioning, isolation), Recover (Model rollback, retraining, output filtering). For Infra risks (Traffic spikes, downtime, capacity): Prevent (Autoscaling, rate limits, capacity planning), Detect (Traffic monitoring, health checks, alerts), Contain (Rate limits, circuit breakers, load shedding), Recover (Auto-scaling, rollback, failover). For Product risks (Bad launch, user impact): Prevent (Feature flags, phased rollout, testing), Detect (User monitoring, metrics, alerts), Contain (Feature flags, kill switches), Recover (Rollback, disable feature, communication). For Legal risks (PII exposure, compliance): Prevent (Access control, encryption, audits), Detect (Access monitoring, compliance checks), Contain (Access revocation, data isolation), Recover (Incident response, notifications, remediation). The key is layered mitigations for high-risk items."

**How to Adapt This Narrative for Each Question:**

- **Q796 (LLM adversarial attacks):** Focus on AI security risks → "To explain LLM adversarial attacks, I'd: Enumerate Risks (AI-specific: Adversarial attacks (prompt injection, jailbreaking, data poisoning), Model drift, bias, hallucination, misuse, Technical: System vulnerabilities, Data: Training data poisoning, leakage, Operational: Access control failures, Legal/Compliance: Misuse, harmful outputs, Business: User trust, reputation), Assess Blast Radius (Users affected: All users if model compromised, Duration: Permanent if model poisoned, Reversibility: Hard to fix if model trained on bad data, Visibility: Public if attack successful), Prioritize (High impact + high probability: Adversarial attacks, misuse → ACT, High impact + low probability: Model poisoning → PLAN, Low impact + high probability: Minor prompt issues → AUTOMATE, Low impact + low probability: Edge cases → ACCEPT), Mitigate (Prevent: Input validation, prompt filtering, access controls, guardrails, Detect: Anomaly detection, output monitoring, attack detection, Contain: Rate limits, feature flags, output filtering, Recover: Model rollback, retraining, incident response), Monitor (Early warning: Unusual prompts, output anomalies, Alert thresholds: Attack patterns, harmful outputs, Clear owner: Security team, escalation path). I'd prioritize: Input validation (Critical - prevent attacks), Output filtering (High impact - prevent harmful outputs), Monitoring (High impact - detect attacks early)."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Risk Mitigation Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Risk Types & Mitigations** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through risk mitigation framework in 2 minutes (Enumerate Risks → Blast Radius → Mitigations → Monitor)
- [ ] Enumerate risks (Technical, data, operational, legal, business)
- [ ] Assess blast radius (Users affected, duration, reversibility, visibility)
- [ ] Prioritize risks (High/medium/low impact × probability)
- [ ] Mitigate (Prevent, detect, contain, recover)
- [ ] Monitor (Early warning, alerts, escalation)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the risk mitigation framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Enumerate Risks → Blast Radius → Mitigations → Monitor framework**, not memorizing answers

**Remember:** L11 is about risk mitigation. The framework: Enumerate Risks → Blast Radius → Mitigations → Monitor. Key principles: Risk = probability × blast radius. You don't eliminate risk — you bound it. Detection speed matters more than perfection. Assume failure will happen.
