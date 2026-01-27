# DATA ANALYST HEALTH TREE
## (Wrong Numbers = Wrong Decisions)

```
                                      [ANALYSIS]
                                         |
                                         |
        -------------------------------------------------------------------------
        |                          |                          |                 |
        |                          |                          |                 |
   [1] METRIC MISMATCH         [2] MISSING CONTEXT       [3] CORRELATION TRAP   [4] STORYTELLING FAIL
   ตัวเลขไม่ตรงกัน              บริบทหายไป              สาเหตุผิด            บอกเรื่องไม่ชัด
   เพราะ definition ผิด        เพราะไม่รู้ business     เพราะ correlation    เพราะไม่เชื่อมโยง
                                context                  ≠ causation          insight → action

        |                          |                          |                 |
        |                          |                          |                 |

   Metric Definition Gap      Business Context Score     Correlation vs Causation  Actionability Score
   (revenue SQL mismatch)     (understands business)     (spurious relationships)   (insight → decision)

        |                          |                          |                 |
        |                          |                          |                 |

   = 1       HEAVEN          > 80%    UNDERSTANDS      Causal     TRUTH       > 80%    ACTIONABLE
   = 2       WARNING        60–80%    PARTIAL          Correlation WARNING     60–80%   NEEDS WORK
   ≥ 3       CIVIL WAR       < 60%    CLUELESS         Spurious   LIES        < 60%    USELESS

        |                          |                          |                 |
        |                          |                          |                 |

   Impact:                   Impact:                    Impact:             Impact:
   Teams fight over numbers   Wrong interpretation       Wrong fixes          No action taken
   Nobody trusts data         Wrong recommendations      Problem persists     Wasted analysis
   Metrics drift              Business ignores you       Time wasted          You become invisible

        |                          |                          |                 |
        -------------------------------------------------------------------------
                                         |
                                         |
                               ANALYSIS RELIABILITY SCORE

                         If ANY pillar is RED:
                         → Analysis is wrong
                         → Business ignores you
                         → You become "analyst who never helps"
```

---

## 🎯 INTENT BEHIND DATA ANALYST QUESTIONS

### [1] METRIC MISMATCH - "Why does metric definition matter?"

**Intent**: Test if you understand single source of truth

**What they're really testing:**
- Do you know metric definitions?
- Can you prevent metric conflicts?
- Do you understand why teams fight over numbers?

**Questions map to:**
- "How do you ensure metric consistency?" → Tests definition awareness
- "What's your approach to data modeling?" → Tests single source of truth
- "How do you handle metric versioning?" → Tests governance

**Why it matters:**
- Marketing says "revenue = $1M"
- Finance says "revenue = $1.2M"
- → Teams fight, nobody trusts data
- → Execs lose confidence in analytics

**Your portfolio shows:**
- Cocktailverse: "Walk me through your star schema design" → Single source of truth
- Marketing Analytics: CTR, CPC, ROAS definitions → Metric clarity

---

### [2] MISSING CONTEXT - "Why does business understanding matter?"

**Intent**: Test if you understand business, not just data

**What they're really testing:**
- Do you understand business context?
- Can you interpret data correctly?
- Do you know why metrics matter?

**Questions map to:**
- "How do you explain insights to stakeholders?" → Tests business communication
- "What's your approach to root cause analysis?" → Tests business understanding
- "How do you prioritize analysis requests?" → Tests business acumen

**Why it matters:**
- "Revenue dropped 10%" → Without context = Panic
- "Revenue dropped 10% because we stopped unprofitable products" → With context = Good decision
- Missing context = Wrong interpretation = Wrong decisions

**Your portfolio shows:**
- Finance/VC background = Business context strength
- Marketing Analytics: Business metrics (CTR, ROAS) → Business understanding

---

### [3] CORRELATION TRAP - "Why does causation matter?"

**Intent**: Test if you understand correlation vs causation

**What they're really testing:**
- Do you know correlation ≠ causation?
- Can you identify spurious relationships?
- Do you understand root cause analysis?

**Questions map to:**
- "How do you identify root causes?" → Tests causal thinking
- "How do you distinguish correlation from causation?" → Tests rigor
- "What's your approach to root cause analysis?" → Tests methodology

**Why it matters:**
- "Ice cream sales correlate with drownings" → Correlation, not causation
- Business fixes wrong thing → Problem persists
- "Users who click ads convert more" → Maybe they were going to convert anyway
- Wrong fixes = Wasted time and resources

**Your portfolio shows:**
- AI BI Agent: "Automated EDA" → Could emphasize root cause analysis
- Marketing Analytics: Could add root cause analysis for campaign performance

---

### [4] STORYTELLING FAIL - "Why does actionability matter?"

**Intent**: Test if you can drive decisions, not just report numbers

**What they're really testing:**
- Can you connect insights to actions?
- Do you understand business impact?
- Can you communicate value?

**Questions map to:**
- "How do you communicate insights to stakeholders?" → Tests storytelling
- "How do you measure business impact?" → Tests actionability
- "What's your approach to data visualization?" → Tests communication

**Why it matters:**
- "CTR is 2.5%" → So what? → Business ignores you
- "CTR is 2.5%, below industry 3.5%, recommend testing new creatives to improve by 0.5% → $50K additional revenue" → Business acts
- No actionability = Wasted analysis = You become invisible

**Your portfolio shows:**
- Marketing Analytics: Dashboard with KPIs → Visualization
- Could emphasize: "Insights → Recommendations → Actions"

---

## 🔥 FAILURE MODES

### If METRIC MISMATCH ≥ 3:
- Multiple versions of truth
- Teams fight over numbers
- Nobody trusts data
- **You get fired when execs lose confidence**

### If MISSING CONTEXT < 60%:
- Wrong interpretation
- Wrong recommendations
- Business ignores you
- **You get fired when decisions are wrong**

### If CORRELATION TRAP = Spurious:
- Fix wrong problem
- Issue persists
- Time wasted
- **You get fired when problems don't get solved**

### If STORYTELLING FAIL < 60%:
- No action taken
- Wasted analysis
- You become invisible
- **You get fired when you don't add value**

---

## ✅ YOUR PORTFOLIO CONNECTION

### Marketing Analytics shows:
- ✅ Metric definitions (CTR, CPC, ROAS)
- ✅ Business metrics
- ✅ Data visualization
- ⚠️ Could add: Root cause analysis
- ⚠️ Could emphasize: Actionability (insights → recommendations)

### Cocktailverse shows:
- ✅ Star schema (single source of truth)
- ✅ Data modeling
- ✅ Metric consistency

### AI BI Agent shows:
- ✅ Automated EDA
- ✅ Statistical analysis
- ⚠️ Could emphasize: Business context in analysis

### Your Finance/VC Background:
- ✅ Business context understanding
- ✅ Metric interpretation
- ✅ Business acumen
- **This is your STRENGTH for Data Analyst roles**

---

## 🎯 KEY DIFFERENCES: Data Analyst vs Data Engineer

### Data Engineer focuses on:
- **Pipeline reliability** (data gets there, on time, correct)
- **Infrastructure** (systems, scale, cost)
- **Technical depth** (how data flows)

### Data Analyst focuses on:
- **Metric accuracy** (numbers are right, definitions clear)
- **Business context** (what numbers mean)
- **Actionability** (insights → decisions)

**Same data, different lens:**
- DE: "How do we get data there reliably?"
- DA: "What does this data mean for the business?"

---

## 📊 DATA ANALYST QUESTION MAPPING

### Metric Mismatch Questions:
- "How do you ensure metric consistency?"
- "What's your approach to data modeling?"
- "How do you handle metric versioning?"
- "How do you prevent metric conflicts?"

### Missing Context Questions:
- "How do you explain insights to stakeholders?"
- "What's your approach to root cause analysis?"
- "How do you prioritize analysis requests?"
- "How do you understand business requirements?"

### Correlation Trap Questions:
- "How do you identify root causes?"
- "How do you distinguish correlation from causation?"
- "What's your approach to hypothesis testing?"
- "How do you validate your analysis?"

### Storytelling Fail Questions:
- "How do you communicate insights?"
- "How do you measure business impact?"
- "What's your approach to data visualization?"
- "How do you drive action from analysis?"

---

## 💡 YOUR STRENGTHS FOR DATA ANALYST

### From Finance/VC Background:
- ✅ **Business context** - You understand metrics in business context
- ✅ **Metric interpretation** - You know what numbers mean
- ✅ **Stakeholder communication** - You've explained to execs
- ✅ **Business acumen** - You understand ROI, unit economics

### From Portfolio:
- ✅ **Technical skills** - You can query, analyze, visualize
- ✅ **Data quality** - You understand data pipelines
- ✅ **Tool proficiency** - SQL, Python, visualization

**You're actually STRONG for Data Analyst roles because of your business background!**

---

## 🎯 WHAT TO EMPHASIZE IN INTERVIEWS

### For Data Analyst roles, emphasize:

1. **Business Context** (Your strength!)
   - "In my VC background, I analyzed metrics in business context..."
   - "I understand how metrics connect to business outcomes..."

2. **Actionability**
   - "I don't just report numbers, I provide recommendations..."
   - "Every analysis connects to actionable insights..."

3. **Communication**
   - "I've explained complex data to non-technical stakeholders..."
   - "I use visualizations to tell stories, not just show numbers..."

4. **Metric Rigor**
   - "I ensure metric definitions are clear and consistent..."
   - "I understand the importance of single source of truth..."

---

**Your portfolio + finance background = Strong Data Analyst candidate!**
