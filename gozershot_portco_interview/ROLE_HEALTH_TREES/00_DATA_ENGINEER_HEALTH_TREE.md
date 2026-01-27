# DATA ENGINEERING HEALTH TREE
## (You Get Fired Here)

```
                                      [DATA]
                                         |
                                         |
        -------------------------------------------------------------------------
        |                          |                          |                 |
        |                          |                          |                 |
   [1] DUPLICATION             [2] LATENESS              [3] TIME TRAVEL   [4] CANONICAL
   ตัวเลขพอง                  ตัวเลขย้อน                เขียนอดีตใหม่      ความจริงไม่กลาง
   เพราะความซ้ำ              เพราะมาช้า              เพราะ SCD พัง        เพราะใช้หลายแหล่ง

        |                          |                          |                 |
        |                          |                          |                 |

   Duplicate Rate           Late Arrival P90           SCD Violation        Metric Versions
   (raw vs canonical)       (event → ingest)           (join > 1 row)       (revenue SQL)

        |                          |                          |                 |
        |                          |                          |                 |

   < 2%      SAFE           < 1 hr     GOD               = 0        CLEAN     = 1       HEAVEN
   2–5%      WARNING        1–12 hr    NORMAL            > 0        LYING      = 2       WARNING
   > 5%      FUCKED         > 24 hr    SNAPSHOT NOW                      ≥ 3       CIVIL WAR

        |                          |                          |                 |
        |                          |                          |                 |

   Impact:                   Impact:                    Impact:             Impact:
   Revenue inflation         Dashboard rewrites         History rewrite     Teams fight
   Fake growth               CFO rage                   Attribution lies    Nobody trusts data
   Marketing hallucination   Exec loses trust           Legal exposure      Metrics drift

        |                          |                          |                 |
        -------------------------------------------------------------------------
                                         |
                                         |
                               COMPANY REALITY SCORE

                         If ANY pillar is RED:
                         → Stop shipping features
                         → Fix data first
                         → Or enjoy post-mortems
```

---

## 🎯 INTENT BEHIND DATA ENGINEER QUESTIONS

### [1] DUPLICATION - "Why do we care about duplicates?"

**Intent**: Test if you understand data quality fundamentals

**What they're really testing:**
- Do you know garbage in = garbage out?
- Can you detect and prevent duplicates?
- Do you understand business impact of bad data?

**Questions map to:**
- "How do you handle duplicate records?" → Tests deduplication strategy
- "What's your approach to data quality validation?" → Tests prevention
- "How do you ensure idempotency?" → Tests duplicate prevention

**Why it matters:**
- Duplicate orders = fake revenue
- Duplicate users = inflated metrics
- Duplicate events = wrong attribution

**Your portfolio shows:**
- Coffeeverse: "How do you handle duplicate records in your pipeline?"
- Cocktailverse: "What was your approach to deduplication?"

---

### [2] LATENESS - "Why does data freshness matter?"

**Intent**: Test if you understand SLAs and business impact

**What they're really testing:**
- Do you understand data freshness requirements?
- Can you design for latency SLAs?
- Do you know when data is "too late"?

**Questions map to:**
- "How did you achieve < 5 minute data latency?" → Tests optimization
- "What's your strategy for handling late-arriving data?" → Tests design
- "How do you handle data freshness SLAs?" → Tests SLA awareness

**Why it matters:**
- Late data = wrong decisions
- Dashboard shows yesterday's numbers = execs lose trust
- Real-time systems need real-time data

**Your portfolio shows:**
- Cocktailverse: "How did you achieve less than 5 minute data latency?"
- Coffeeverse: "What was your strategy for handling late-arriving data?"

---

### [3] TIME TRAVEL - "Why does SCD matter?"

**Intent**: Test if you understand historical accuracy

**What they're really testing:**
- Do you understand slowly changing dimensions?
- Can you preserve historical accuracy?
- Do you know when history gets rewritten?

**Questions map to:**
- "How do you handle schema evolution?" → Tests SCD awareness
- "What's your approach to dimensional modeling?" → Tests SCD design
- "How do you handle slowly changing dimensions?" → Tests SCD implementation

**Why it matters:**
- Rewritten history = wrong attribution
- "Customer was in Segment A" → "Customer was in Segment B" = lies
- Legal/compliance needs accurate history

**Your portfolio shows:**
- Cocktailverse: "How do you handle schema changes without breaking downstream?"
- Coffeeverse: "How do you handle schema evolution in your Azure pipeline?"

---

### [4] CANONICAL - "Why does single source of truth matter?"

**Intent**: Test if you understand data governance

**What they're really testing:**
- Do you understand metric definitions?
- Can you prevent metric conflicts?
- Do you know when teams fight over numbers?

**Questions map to:**
- "How do you ensure data consistency across different systems?" → Tests canonical design
- "What's your approach to data modeling?" → Tests single source of truth
- "How do you handle data governance?" → Tests metric versioning

**Why it matters:**
- Marketing says revenue = $1M
- Finance says revenue = $1.2M
- → Teams fight, nobody trusts data
- → Execs lose confidence

**Your portfolio shows:**
- Cocktailverse: "Walk me through your star schema design" → Single source of truth
- Coffeeverse: "How do you ensure data consistency?" → Canonical design

---

## 🔥 FAILURE MODES

### If DUPLICATION > 5%:
- Revenue looks inflated
- Growth metrics are fake
- Marketing thinks campaigns work (they don't)
- **You get fired when CFO finds out**

### If LATENESS > 24 hours:
- Dashboards show yesterday's data
- Execs make decisions on stale data
- Real-time systems break
- **You get fired when exec loses trust**

### If TIME TRAVEL breaks:
- Historical reports change
- Attribution is wrong
- Legal/compliance issues
- **You get fired when audit finds lies**

### If CANONICAL breaks:
- Multiple versions of truth
- Teams fight over numbers
- Nobody trusts data
- **You get fired when metrics drift**

---

## ✅ YOUR PORTFOLIO CONNECTION

### Coffeeverse shows:
- ✅ Deduplication strategy
- ✅ Late-arriving data handling
- ✅ Schema evolution
- ✅ Data consistency

### Cocktailverse shows:
- ✅ Data latency optimization
- ✅ Star schema (canonical)
- ✅ Schema change handling
- ✅ Data quality validation

**Every question in your portfolio maps to these 4 pillars.**
