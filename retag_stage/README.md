# 🎯 RETAG STAGE - Clean Workspace

**Purpose:** Tag 2,849 questions into 30 master patterns (🟢 Northstar + 🟡 LHF)

**Goal:** Squeeze 3,000 questions → 30 patterns to master on autopilot

---

## 📁 File Structure

```
retag_stage/
├── README.md                          # This file
├── rules/                             # Classification rules
│   ├── RULEBOOK_LLM.md               # Intent-based tagging algorithm (for LLM)
│   └── CHEATSHEET_HUMAN.md           # Pattern matching guide (for B)
├── input/                             # Source data
│   ├── questions_raw.md              # 2,853 questions (pre-normalized)
│   └── questions_normalized.md       # 2,849 questions (cleaned, ready)
└── output/                            # Results (to be generated)
    ├── 🟢_NORTHSTAR_12_PATTERNS.md   # 12 universal patterns + questions
    ├── 🟡_LHF_14_PATTERNS.md         # 14 low-hanging fruit + questions
    └── 🔴_SAFE_TO_IGNORE.md          # Everything else

```

---

## 📋 The 6 Essential Files

### **1️⃣ RULEBOOK_LLM.md** (rules/RULEBOOK_LLM.md)
- **Original:** `🤖_TAGGING_ALGORITHM_LLM.md`
- **Purpose:** Intent-based classification engine
- **For:** LLM tagging (deterministic, auditable)
- **Features:**
  - 5-second decision guide
  - Two-layer intent detection (keywords + semantic)
  - Boundary examples
  - 50 worked examples

### **2️⃣ CHEATSHEET_HUMAN.md** (rules/CHEATSHEET_HUMAN.md)
- **Original:** `🟢🟡🔴_PATTERN_MATCHING_CHEATSHEET.md [FOR B'S EYES ONLY]`
- **Purpose:** Human-friendly study guide
- **For:** B's interview prep
- **Features:**
  - 12 Northstar patterns with frameworks
  - 14 LHF patterns
  - Quick pattern matching guide

### **3️⃣ questions_raw.md** (input/questions_raw.md)
- **Original:** `ALL_QUESTIONS_RAW.md`
- **Purpose:** Pre-normalized source (2,853 questions)
- **Status:** Contains 4 junk questions, 34 truncated

### **4️⃣ questions_normalized.md** (input/questions_normalized.md)
- **Original:** `ALL_QUESTIONS_NORMALIZED.md`
- **Purpose:** Clean, ready-to-tag data (2,849 questions)
- **Status:** 98.8% complete, ready for tagging

### **5️⃣ 🟢_NORTHSTAR_12_PATTERNS.md** (output/ - TO BE GENERATED)
- **Purpose:** 12 universal patterns + all matching questions
- **Expected:** ~200-300 questions
- **For:** B's top priority study list

### **6️⃣ 🟡_LHF_14_PATTERNS.md** (output/ - TO BE GENERATED)
- **Purpose:** 14 low-hanging fruit patterns + questions
- **Expected:** ~400-600 questions
- **For:** B's secondary study list

### **BONUS: 🔴_SAFE_TO_IGNORE.md** (output/ - TO BE GENERATED)
- **Purpose:** All questions that don't fit 🟢 or 🟡
- **Expected:** ~1,800-2,200 questions
- **For:** Strategic ignore list

---

## 🎯 The 30 Patterns to Master

### 🟢 **NORTHSTAR (12 patterns)**

1. Metric Drop Diagnosis Tree
2. North Star Metric + KPI Ladder
3. Funnel Decomposition + Conversion Fix
4. Cohort / Retention / Churn Reasoning
5. Segmentation (Who / Where / Why) + Targeting
6. Prioritization Framework (RICE / Impact-Effort)
7. Tradeoff Framing + Guardrails
8. Experiment Design & Causal Reasoning
9. Decision-Making Under Uncertainty
10. Executive Communication (1-Pager / Narrative)
11. Stakeholder Alignment + Influence Without Authority
12. Operational Excellence (Risk / Monitoring / Escalation)

### 🟡 **LOW-HANGING FRUIT (14 patterns)**

1. Data Readiness & Trust Pattern
2. Scale & Capacity Reasoning
3. Cost / ROI Framing
4. System Constraints Mapping
5. Instrumentation & Observability
6. Operational Tradeoffs (Ops-level)
7. Data Modeling for Decision-Making
8. Market & Competitive Snapshot
9. Financial Sensitivity Analysis
10. Process & Workflow Optimization
11. Risk Enumeration & Mitigation
12. Advanced Metrics Interpretation
13. SQL-for-Reasoning (Conceptual)
14. System Design (Conceptual Scale)

**Total: 26 patterns (12 + 14)**

---

## 🚀 Next Steps

### **Step 1: Dry Run (Manual Validation)**
- Tag 50-100 sample questions manually
- Validate intent detection works
- Adjust thresholds if needed

### **Step 2: Full Tagging**
- Run RULEBOOK_LLM.md on questions_normalized.md
- Generate 3 output files

### **Step 3: Quality Check**
- Review boundary cases
- Ensure 🟢 questions are truly universal
- Verify 🔴 questions are safe to ignore

### **Step 4: Study Mode**
- B uses CHEATSHEET_HUMAN.md for frameworks
- B studies questions from 🟢 (priority) then 🟡 (secondary)
- B ignores 🔴 entirely

---

## ✅ Success Metrics

**Goal achieved when:**
- ✅ 2,849 questions bucketed into 🟢🟡🔴
- ✅ ~600-900 questions in 🟢 + 🟡 (manageable study load)
- ✅ ~1,800-2,200 questions in 🔴 (strategic ignore)
- ✅ B can recognize any question's pattern in 5 seconds
- ✅ Both B and LLM can classify on autopilot

---

## 📊 Expected Distribution

```
🟢 NORTHSTAR (12 patterns)
├─ ~200-300 questions
├─ ~60-90 hours study time
└─ MUST MASTER (universal across roles)

🟡 LOW-HANGING FRUIT (14 patterns)
├─ ~400-600 questions
├─ ~120-180 hours study time
└─ SHOULD STUDY (high ROI)

🔴 SAFE TO IGNORE
├─ ~1,800-2,200 questions
├─ ~0 hours study time
└─ SKIP (low ROI, coding/ML theory, niche)
```

**Total study time: ~180-270 hours (manageable for 3-day sprint if focused)**

---

## 🎯 Why This Works

1. **Intent-based detection** → Catches "LeetCode by shape" not just keywords
2. **Two-layer filtering** → Fast path (keywords) + semantic path (intent)
3. **Deterministic rules** → Consistent, auditable, no black box
4. **Pattern-focused** → Learn 26 frameworks, answer 900 questions
5. **Strategic ignore** → Don't waste time on low-ROI questions

**This is not fine-tuning. This is prompt-programming + deterministic policy.**

**Ready for production tagging.** 🎯
