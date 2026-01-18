# 🎯 TAGGING STRATEGY - 2,849 Questions at Scale

**Goal:** Tag all questions with speed + quality, zero hallucination

**Reference:** DRY_RUN_FINAL.csv (validated format)

---

## 📊 The Challenge

- **Volume:** 2,849 questions
- **Output:** 8 columns per question
- **Quality bar:** DRY_RUN_FINAL.csv
- **Risk:** Hallucination, drift, inconsistency

---

## ✅ RECOMMENDED APPROACH: Chunked Batch Processing

### **Strategy: 100 questions per batch**

**Why 100?**
- ✅ Fits in context window comfortably
- ✅ Maintains quality (no drift)
- ✅ Easy to validate/spot-check
- ✅ Can resume if interrupted

**Total batches:** 2,849 ÷ 100 = ~29 batches

---

## 🔄 Batch Processing Workflow

### **Batch N (100 questions):**

**Input:**
- questions_normalized.md (lines X to Y)
- RULEBOOK_LLM.md (intent detection rules)
- DRY_RUN_FINAL.csv (reference format)

**Process:**
1. Load 100 questions
2. For each question:
   - Apply STEP 1 (reject triggers)
   - Apply STEP 2 (Northstar matching)
   - Apply STEP 3 (LHF matching)
   - Generate: pattern_id, pattern_name, formula, notes, short_answer
3. Output: batch_N.csv

**Validation:**
- Spot-check 5 random rows
- Verify format matches DRY_RUN_FINAL.csv
- Check for hallucination (nonsense answers)

**Merge:**
- Append batch_N.csv to master file

---

## 🎯 Quality Controls (Anti-Hallucination)

### **1. Deterministic Pattern Matching**
- Use exact keywords from RULEBOOK_LLM.md
- No "creative interpretation"
- If uncertain → default to 🔴

### **2. Formula Library (Pre-defined)**
- Lock 26 canonical formulas (12 🟢 + 14 🟡)
- No ad-hoc formulas
- Copy from library, don't generate

### **3. Short Answer Template**
- Follow DRY_RUN_FINAL.csv style
- 2-3 sentences max
- Must reference the formula steps
- No generic fluff

### **4. Spot-Check Every Batch**
- Random sample 5 questions
- Verify pattern match is correct
- Verify formula is from library
- Verify short answer makes sense

---

## 📋 Pre-Work: Lock the 26 Canonical Formulas

**Before tagging, create:**

`FORMULA_LIBRARY.md`

```
🟢 NORTHSTAR FORMULAS (12)

P1 - Metric Drop Diagnosis
Formula: Clarify Metric → Segment → Hypothesize → Data Check → Action

P2 - NSM + KPI Ladder
Formula: Define NSM → Input KPIs → Leading Indicators → Guardrails → Dashboard

P3 - Funnel Analysis
Formula: Define Funnel Steps → Measure Drop-off → Identify Friction → Hypothesize Fix → Test

P4 - Cohort / Retention / Churn
Formula: Define Cohorts → Measure Retention → Identify Churn Drivers → Hypothesize → Fix

P5 - Segmentation
Formula: (Persona × Behavior × Value) → Rank → Focus Top Segments

P6 - Prioritization
Formula: Impact × Confidence × Ease → RICE Score → Decide + Communicate

P7 - Tradeoff Framing
Formula: Define Options → Winners/Losers → Guardrails → Decide + Communicate

P8 - Experiment Design
Formula: Hypothesis → Metric → Design → Run → Validate → Decide

P9 - Decision Under Uncertainty
Formula: Clarify Assumptions → Identify Risks → Validation Plan → Decide

P10 - Executive Communication
Formula: Context → Insight → Recommendation → Next Steps

P11 - Stakeholder Alignment
Formula: Understand Incentives → Address Concerns → Build Coalition → Decide

P12 - Operational Excellence
Formula: Assess Current State → Identify Risks → Prioritize Fixes → Communicate Plan → Monitor

🟡 LHF FORMULAS (14)

L1 - Data Trust
Formula: Source → Freshness → Completeness → Bias → Sanity Checks

L2 - Scale & Capacity
Formula: Current Load → 10× Projection → Bottlenecks → Mitigation

L3 - Cost / ROI
Formula: Cost Drivers → Benefits → Breakeven → Decide

L4 - Constraints
Formula: Legal → Technical → Organizational → Timeline → Prioritize

L5 - Observability
Formula: Key Metrics → Alerts → Dashboards → Escalation

L6 - Ops Tradeoffs
Formula: Speed vs Quality vs Reliability → SLAs → Error Budget → Decide

L7 - Data Modeling
Formula: Entities → Relationships → Metrics → Grain → Validate

L8 - Market Analysis
Formula: Competitors → Differentiation → Market Conditions → Strategy

L9 - Financial Sensitivity
Formula: Levers (Price, Volume, Churn) → Impact → Prioritize

L10 - Process Optimization
Formula: Map Workflow → Identify Bottlenecks → Optimize → Measure

L11 - Risk Mitigation
Formula: Enumerate Risks → Blast Radius → Mitigations → Monitor

L12 - Metrics Interpretation
Formula: Metric Moved → Proxy Validity → Gaming Risk → Decide

L13 - SQL Reasoning
Formula: Conceptual Join → Aggregation Logic → Filter Logic → Output

L14 - System Design (Conceptual)
Formula: Components → Data Flow → Boundaries → Scale Considerations
```

**This prevents hallucination.** Copy formula from library, don't generate.

---

## 🚀 Execution Plan

### **Phase 1: Lock Formulas (30 min)**
- Create FORMULA_LIBRARY.md
- Validate against DRY_RUN_FINAL.csv
- Commit to repo

### **Phase 2: Batch Tagging (4-6 hours)**
- Process 100 questions per batch
- 29 batches total
- Spot-check every batch
- Merge into master CSV

### **Phase 3: Quality Check (1 hour)**
- Random sample 50 questions across all batches
- Verify pattern matching
- Check for hallucination
- Fix any drift

### **Phase 4: Split into 3 Files**
- 🟢_NORTHSTAR_12_PATTERNS.csv
- 🟡_LHF_14_PATTERNS.csv
- 🔴_SAFE_TO_IGNORE.csv

**Total time: 5-8 hours**

---

## ⚠️ Failure Modes & Mitigations

### **Problem 1: Hallucinated Formulas**
- **Symptom:** Formula not in library
- **Fix:** Pre-lock 26 formulas, copy only

### **Problem 2: Wrong Pattern Match**
- **Symptom:** Question doesn't fit pattern
- **Fix:** Strict keyword matching from RULEBOOK_LLM.md

### **Problem 3: Generic Short Answers**
- **Symptom:** "I would analyze the data and make a decision"
- **Fix:** Must reference formula steps explicitly

### **Problem 4: Drift Across Batches**
- **Symptom:** Batch 1 style ≠ Batch 29 style
- **Fix:** Spot-check every batch, reference DRY_RUN_FINAL.csv

---

## 🎯 Success Criteria

✅ All 2,849 questions tagged  
✅ Format matches DRY_RUN_FINAL.csv  
✅ Zero hallucinated formulas (all from library)  
✅ Pattern matches are correct (validated)  
✅ Short answers reference formula steps  
✅ 3 output files generated (🟢🟡🔴)

---

## 🔑 The Key: Deterministic + Templated

**Not:** "Generate creative answers"  
**Yes:** "Apply rules + copy from library"

**This is not AI creativity.**  
**This is AI as a deterministic compiler.**

Speed + Quality + Zero Hallucination. 🎯
