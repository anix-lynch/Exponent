# Executive Study Plan: L4 - Constraints
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~10 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L4 (CONSTRAINTS) QUESTIONS

**Even when "constraints" isn't mentioned, look for these keywords/phrases:**

### Explicit Constraint Keywords:
- "constraints", "limitations", "blockers", "can't do", "not allowed"
- "GDPR", "compliance", "legal", "regulatory", "migration", "design with constraints"
- "why can't we", "what limits us", "blocked from", "restrictions"

### Implicit L4 Indicators:
- **Compliance questions:** "Design system that complies with GDPR", "How do you handle compliance?", "Legal constraints"
- **Migration questions:** "Design plan to migrate X", "System migration", "How do you handle legacy systems?"
- **Constraint questions:** "Why can't we launch globally?", "What are the constraints?", "What blocks this?"

### L4 vs P12 Distinction:
- **L4 (Constraints):** "Why can't we launch globally?" → Focus: Identify constraints (Legal, technical, organizational, timeline)
- **P12 (Operational Excellence):** "How do you ensure system reliability?" → Focus: Operational process

### L4 vs P7 Distinction:
- **L4 (Constraints):** "What are the constraints?" → Focus: Identify and prioritize constraints
- **P7 (Tradeoff Framing):** "How do you make tradeoffs?" → Focus: Tradeoff analysis framework

### Red Flags (NOT L4):
- "How do you make tradeoffs?" → P7 (Tradeoff Framing)
- "How do you prioritize features?" → P6 (Prioritization)
- "How do you ensure system reliability?" → P12 (Operational Excellence)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Constraints Framework** (HIGHEST PRIORITY)
2. ⚠️ **Compliance & Migration** (MEDIUM)

**For Data Engineer:**
1. ✅ **Constraints Framework** (HIGHEST) - Core framework
2. ✅ **Compliance & Migration** (HIGH) - Practical application

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Constraints Framework
**Questions:** ~8 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Why can't we launch globally?" or "What are the constraints?" - core constraints framework
- **Framework:** Legal → Technical → Organizational → Timeline → Prioritize
- **Legal/Regulatory:** Compliance (GDPR/CCPA/HIPAA, Data residency, Consent requirements), Contracts (Vendor terms, Partner SLAs, Licensing limits), Risk exposure (Fines/penalties, Lawsuits, Regulatory scrutiny)
- **Technical:** Architecture (Legacy systems, Tight coupling, Data quality gaps), Scale limits (Latency, Throughput, Reliability), Dependencies (External APIs, Data availability, Infra readiness)
- **Organizational:** People (Hiring gaps, Specialized expertise, On-call ownership), Incentives (Team OKRs misaligned, Competing priorities, Political resistance), Process (Review cycles, Approval chains, Cross-team coordination)
- **Timeline:** Fixed deadlines (Launch dates, Regulatory deadlines, Contract renewals), Sequencing (Must-do-first work, Long-lead items, Critical path), Opportunity cost (What slips if this ships? What breaks if it's late?)
- **Prioritize:** Hard constraints (NON-NEGOTIABLE: Legal/safety, External deadlines), Soft constraints (NEGOTIABLE: Scope, UX polish, Internal tooling), Strategy (Redesign to avoid constraint, Phase rollout, Explicitly accept risk)

**Concrete Examples:**
- "Global launch constraints: Legal (GDPR requires consent, EU data not isolated), Technical (Legacy systems, tight coupling), Organizational (Legal review 4-6 weeks), Timeline (Marketing launch in 2 weeks), Decision (Launch US-only, EU in Phase 2)"
- "Constraints: Identify legal, technical, organizational, timeline constraints, prioritize hard vs soft, design around them"

**Representative Questions (Do 5 only):**
- Q286: Design a data pipeline that complies with GDPR. (GDPR compliance angle)
- Q392: Design a plan to migrate an existing authentication system to a new one. (system migration angle)
- Q2670: You are in charge of building a national park system in a newly formed country; how would you measure success? (constraints in design angle)
- Q2840: You're called in by the government of India to design the Cowin portal. What top features would you integrate for partner personas? What key metrics would indicate the platform's success and how would you measure them? (constraints in design angle)
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (operational constraints angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When identifying constraints, I use Legal → Technical → Organizational → Timeline → Prioritize. First, I check Legal/Regulatory: Compliance (GDPR/CCPA/HIPAA: data privacy regulations, consent requirements, Data residency: where data can be stored, processed, Consent requirements: explicit user consent for data usage), Contracts (Vendor terms: third-party service agreements, limitations, Partner SLAs: service level agreements, commitments, Licensing limits: software licenses, usage restrictions), Risk exposure (Fines/penalties: regulatory fines for non-compliance, Lawsuits: legal action, liability, Regulatory scrutiny: increased oversight, audits). Second, I check Technical: Architecture (Legacy systems: old systems that are hard to change, Tight coupling: dependencies that limit flexibility, Data quality gaps: missing, incomplete, or unreliable data), Scale limits (Latency: response time constraints, Throughput: processing capacity limits, Reliability: uptime, error rate constraints), Dependencies (External APIs: third-party service availability, rate limits, Data availability: when data is available, freshness, Infra readiness: infrastructure capacity, capabilities). Third, I check Organizational: People (Hiring gaps: missing skills, headcount constraints, Specialized expertise: domain knowledge, technical skills, On-call ownership: who maintains and supports this), Incentives (Team OKRs misaligned: different priorities across teams, Competing priorities: other work takes precedence, Political resistance: organizational pushback), Process (Review cycles: approval processes, gate reviews, Approval chains: multiple stakeholders, sign-offs, Cross-team coordination: dependencies on other teams). Fourth, I check Timeline: Fixed deadlines (Launch dates: product launch, feature release dates, Regulatory deadlines: compliance requirements, legal dates, Contract renewals: vendor contracts, partnership agreements), Sequencing (Must-do-first work: prerequisites, dependencies, Long-lead items: things that take time to prepare, Critical path: work that blocks everything else), Opportunity cost (What slips if this ships? Other work that gets delayed, What breaks if it's late? Consequences of delay). Finally, I Prioritize: Hard constraints (NON-NEGOTIABLE: Legal/safety - must comply, cannot compromise, External deadlines - fixed dates we can't change), Soft constraints (NEGOTIABLE: Scope - can reduce features, simplify, UX polish - can defer nice-to-haves, Internal tooling - can use workarounds), Strategy (Redesign to avoid constraint: change approach to work around limitation, Phase rollout: launch in stages, address constraints incrementally, Explicitly accept risk: acknowledge constraint and proceed with mitigation). The key principle: Constraints are not excuses. They are design inputs. Good answers say what you'll trade, not just what you can't do."

**How to Adapt This Narrative for Each Question:**

- **Q286 (GDPR-compliant data pipeline):** Focus on GDPR compliance → "To design a GDPR-compliant data pipeline, I'd: Legal/Regulatory (Compliance: GDPR requirements - consent, right to access, right to deletion, data residency - EU data must stay in EU, Consent requirements - explicit consent for data usage, Risk exposure: Fines up to 4% revenue, lawsuits), Technical (Architecture: Design for GDPR - data minimization, purpose limitation, encryption, Scale limits: Handle deletion requests, data portability, Dependencies: EU-compliant infrastructure, data residency), Organizational (People: Legal team review, DPO (Data Protection Officer), Technical expertise, Incentives: Compliance is priority, Process: Review cycles, approval chains), Timeline (Fixed deadlines: GDPR compliance deadline, Regulatory deadlines, Sequencing: Legal review first, then technical implementation, Opportunity cost: Other features delayed), Prioritize (Hard constraints: GDPR compliance is non-negotiable, Soft constraints: Scope - can phase features, UX polish - can defer, Strategy: Design pipeline with GDPR in mind from start, Phase rollout - start with core compliance, then add features). I'd design: Data minimization (Only collect necessary data), Consent management (Track and manage consent), Right to deletion (Ability to delete user data), Data residency (EU data in EU), Encryption (Data at rest and in transit), Audit trail (Log all data access)."

- **Q392 (Authentication system migration):** Emphasize migration constraints → "To migrate an authentication system, I'd: Legal/Regulatory (Compliance: Security requirements, data privacy, Contracts: Vendor contracts, SLAs, Risk exposure: Security breaches, downtime), Technical (Architecture: Legacy system constraints, tight coupling, data migration, Scale limits: Zero downtime migration, user impact, Dependencies: External auth providers, user data, Infra readiness: New system capacity), Organizational (People: Migration team, expertise, on-call, Incentives: Team priorities, competing work, Process: Review cycles, approval, coordination), Timeline (Fixed deadlines: Contract renewals, security deadlines, Sequencing: Must migrate users gradually, long-lead items, Critical path: Data migration blocks everything, Opportunity cost: Other features delayed), Prioritize (Hard constraints: Security, zero downtime, Soft constraints: Scope - can phase features, UX polish, Strategy: Dual-write approach, gradual migration, rollback plan). I'd design: Dual-write (Write to both old and new systems), Gradual migration (Migrate users in batches), Rollback plan (Can revert if issues), Monitoring (Track migration progress, errors), Communication (Notify users, support team)."

---

### BUCKET 2: Compliance & Migration
**Questions:** ~2 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Design system that complies with X" or "Migrate system" - same framework, with focus on compliance/migration
- **Approach:** Same constraints framework, with focus on compliance and migration
- **Compliance:** Legal requirements, Technical implementation, Organizational process, Timeline
- **Migration:** Legacy constraints, Technical migration, Organizational coordination, Timeline

**Concrete Examples:**
- "GDPR compliance: Legal (GDPR requirements), Technical (Data residency, encryption), Organizational (Legal review, DPO), Timeline (Compliance deadline), Prioritize (Hard constraint, design around it)"
- "System migration: Identify constraints, design migration plan, phase rollout, mitigate risks"

**Representative Questions (Do 5 only):**
- Q286: Design a data pipeline that complies with GDPR. (GDPR compliance angle)
- Q392: Design a plan to migrate an existing authentication system to a new one. (system migration angle)
- Q2670: You are in charge of building a national park system in a newly formed country; how would you measure success? (constraints in design angle)
- Q2840: You're called in by the government of India to design the Cowin portal. What top features would you integrate for partner personas? What key metrics would indicate the platform's success and how would you measure them? (constraints in design angle)
- Q110: As the owner of a gas station observing a sudden surge in customers, reaching four times the usual capacity during peak times, how would you investigate, diagnose, and resolve this issue? (operational constraints angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When dealing with compliance or migration, I use the same constraints framework but focus on specific constraints. For Compliance: Legal (Regulatory requirements, consent, data residency), Technical (Implementation - encryption, access controls, audit trails), Organizational (Legal review, DPO, processes), Timeline (Compliance deadlines), Prioritize (Hard constraint - must comply, design around it). For Migration: Legal (Security, contracts), Technical (Legacy constraints, zero downtime, data migration), Organizational (Migration team, coordination), Timeline (Gradual migration, critical path), Prioritize (Hard constraints - security, zero downtime, Soft - scope, Strategy - dual-write, gradual migration, rollback). The key is identifying all constraints and designing around them."

**How to Adapt This Narrative for Each Question:**

- **Q286 (GDPR pipeline):** Already covered in Bucket 1.

- **Q392 (Auth migration):** Already covered in Bucket 1.

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Constraints Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Compliance & Migration** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through constraints framework in 2 minutes (Legal → Technical → Organizational → Timeline → Prioritize)
- [ ] Identify constraints (Legal, technical, organizational, timeline)
- [ ] Prioritize constraints (Hard vs soft, negotiable vs non-negotiable)
- [ ] Design around constraints (Redesign, phase rollout, accept risk)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the constraints framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Legal → Technical → Organizational → Timeline → Prioritize framework**, not memorizing answers

**Remember:** L4 is about constraints. The framework: Legal → Technical → Organizational → Timeline → Prioritize. Key principle: Constraints are not excuses. They are design inputs. Good answers say what you'll trade, not just what you can't do.
