# DATA SCIENTIST HEALTH TREE
## (Wrong Insights = Wrong Decisions)

```
                                      [INSIGHTS]
                                         |
                                         |
        -------------------------------------------------------------------------
        |                          |                          |                 |
        |                          |                          |                 |
   [1] STATISTICAL SIGNIFICANCE  [2] BUSINESS IMPACT      [3] EXPERIMENT DESIGN  [4] ROOT CAUSE
   สถิติไม่น่าเชื่อถือ            ผลกระทบไม่ชัดเจน        ทดลองผิดวิธี          หาสาเหตุผิด
   เพราะ p-value ผิด            เพราะไม่เชื่อมโยง      เพราะ bias            เพราะ correlation ≠ causation

        |                          |                          |                 |
        |                          |                          |                 |

   P-value Threshold         Business Metric Link       Experiment Bias        Correlation vs Causation
   (statistical rigor)       (insight → revenue)        (selection bias)       (spurious relationships)

        |                          |                          |                 |
        |                          |                          |                 |

   p < 0.01   RIGOROUS       Direct $ link   ACTIONABLE   No bias     CLEAN     Causal     TRUTH
   p < 0.05   ACCEPTABLE     Indirect link   USEFUL       Some bias   RISKY     Correlation WARNING
   p > 0.05   NOT SIGNIFICANT No link        USELESS      High bias   BROKEN    Spurious   LIES

        |                          |                          |                 |
        |                          |                          |                 |

   Impact:                   Impact:                    Impact:             Impact:
   Wrong conclusions         No action taken             Wrong decisions      Wrong fixes
   False discoveries         Wasted effort               Wasted resources     Problem persists
   Wasted experiments        Business ignores you        Revenue loss          Time wasted

        |                          |                          |                 |
        -------------------------------------------------------------------------
                                         |
                                         |
                               INSIGHT RELIABILITY SCORE

                         If ANY pillar is RED:
                         → Insights are wrong
                         → Business ignores you
                         → You become "data person who never helps"
```

---

## 🎯 INTENT BEHIND DATA SCIENTIST QUESTIONS

### [1] STATISTICAL SIGNIFICANCE - "Why does p-value matter?"

**Intent**: Test if you understand statistical rigor

**What they're really testing:**
- Do you know when results are significant?
- Can you interpret p-values correctly?
- Do you understand false discovery rate?

**Questions map to:**
- "What's your approach to statistical significance testing?" → Tests p-value understanding
- "How do you interpret confidence intervals?" → Tests statistical rigor
- "What's your threshold for statistical significance?" → Tests decision-making

**Why it matters:**
- p > 0.05 = Not significant = Could be random chance
- Business makes decisions on noise
- Wasted resources on false discoveries
- Multiple testing = False discovery rate explosion

**Your portfolio shows:**
- Marketing Analytics: Could add A/B testing with p-values
- AI BI Agent: "What's your approach to statistical analysis automation?"
- This is THE core Data Scientist skill

---

### [2] BUSINESS IMPACT - "Why does revenue connection matter?"

**Intent**: Test if you understand business value

**What they're really testing:**
- Can you connect insights to business metrics?
- Do you understand ROI?
- Can you communicate value?

**Questions map to:**
- "How do you measure business value of your work?" → Tests impact thinking
- "What metrics do you use to show impact?" → Tests business connection
- "How do you explain insights to stakeholders?" → Tests communication

**Why it matters:**
- "CTR improved 5%" → So what? → Business ignores you
- "CTR improved 5% → $50K additional revenue" → Business listens
- No business link = Wasted analysis

**Your portfolio shows:**
- Marketing Analytics: CTR, CPC, ROAS (business metrics)
- Churn ML Pipeline: Could emphasize "reduced churn by X% → saved $Y"
- This is what separates DS from analysts

---

### [3] EXPERIMENT DESIGN - "Why does bias matter?"

**Intent**: Test if you understand proper experimentation

**What they're really testing:**
- Do you know selection bias?
- Can you design controlled experiments?
- Do you understand randomization?

**Questions map to:**
- "How do you design A/B tests?" → Tests experiment design
- "How do you prevent selection bias?" → Tests bias awareness
- "What's your approach to randomization?" → Tests rigor

**Why it matters:**
- Selection bias = Wrong conclusions
- "New feature works!" → Actually just better users selected
- Business makes wrong decisions
- Wasted resources

**Your portfolio shows:**
- Marketing Analytics: Could add A/B testing module
- This is THE gap in your portfolio for DS roles

---

### [4] ROOT CAUSE - "Why does causation matter?"

**Intent**: Test if you understand correlation vs causation

**What they're really testing:**
- Do you know correlation ≠ causation?
- Can you identify spurious relationships?
- Do you understand causal inference?

**Questions map to:**
- "How do you identify root causes?" → Tests causal thinking
- "How do you distinguish correlation from causation?" → Tests rigor
- "What's your approach to root cause analysis?" → Tests methodology

**Why it matters:**
- "Ice cream sales correlate with drownings" → Correlation, not causation
- Business fixes wrong thing → Problem persists
- Wasted time and resources

**Your portfolio shows:**
- AI BI Agent: "Automated EDA" → Could emphasize root cause analysis
- Marketing Analytics: Could add root cause analysis for campaign performance

---

## 🔥 FAILURE MODES

### If STATISTICAL SIGNIFICANCE > 0.05:
- Results not significant
- Could be random chance
- Business makes decisions on noise
- **You get fired when decisions are wrong**

### If BUSINESS IMPACT = No link:
- Insights don't connect to revenue
- Business ignores you
- Wasted analysis time
- **You get fired when you don't add value**

### If EXPERIMENT DESIGN = Biased:
- Wrong conclusions
- Business makes bad decisions
- Wasted resources
- **You get fired when experiments fail**

### If ROOT CAUSE = Correlation:
- Fix wrong problem
- Issue persists
- Time wasted
- **You get fired when problems don't get solved**

---

## ✅ YOUR PORTFOLIO CONNECTION

### Marketing Analytics shows:
- ✅ Business metrics (CTR, ROAS)
- ⚠️ Could add: Statistical significance testing
- ⚠️ Could add: A/B testing (experiment design)

### AI BI Agent shows:
- ✅ Automated EDA
- ✅ Statistical analysis
- ⚠️ Could emphasize: Root cause analysis

### Churn ML Pipeline shows:
- ✅ Model evaluation
- ⚠️ Could emphasize: Business impact ($ saved from churn reduction)

**Your portfolio is strong but needs A/B testing extension for full DS coverage.**

---

## 🎯 WHAT TO ADD FOR DATA SCIENTIST ROLES

### Extend Marketing Analytics with:
1. **A/B Testing Module**
   - Statistical significance (p-values)
   - Confidence intervals
   - Experiment design

2. **Root Cause Analysis**
   - "Why did campaign A outperform B?"
   - Causal analysis, not just correlation

3. **Business Impact Emphasis**
   - "Improved CTR by 15% → $50K additional revenue"
   - Connect every insight to $$$

**This makes your portfolio DS-ready.**
