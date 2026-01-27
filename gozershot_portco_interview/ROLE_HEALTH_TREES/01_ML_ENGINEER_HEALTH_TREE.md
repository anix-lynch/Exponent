# ML ENGINEERING HEALTH TREE
## (Models Break in Production)

```
                                      [MODEL]
                                         |
                                         |
        -------------------------------------------------------------------------
        |                          |                          |                 |
        |                          |                          |                 |
   [1] DATA LEAKAGE           [2] MODEL DRIFT           [3] PREDICTION LATENCY  [4] FEATURE STALENESS
   อนาคตรั่วไหล                โมเดลลืม                ทำนายช้าเกินไป          ฟีเจอร์เก่า
   เพราะใช้ข้อมูลอนาคต        เพราะโลกเปลี่ยน          เพราะ compute ช้า        เพราะ update ช้า

        |                          |                          |                 |
        |                          |                          |                 |

   Future Info Leak         Drift Score               P95 Latency            Feature Freshness
   (test has future data)   (prod vs train)          (request → prediction)  (feature → model)

        |                          |                          |                 |
        |                          |                          |                 |

   = 0%       CLEAN          < 5%     STABLE          < 100ms   REAL-TIME    < 1 min    FRESH
   0–2%       WARNING        5–10%    DRIFTING        100–500ms  ACCEPTABLE   1–5 min    STALE
   > 2%       CHEATING       > 10%    BROKEN          > 500ms    TOO SLOW     > 5 min    ROTTEN

        |                          |                          |                 |
        |                          |                          |                 |

   Impact:                   Impact:                    Impact:             Impact:
   Fake accuracy             Wrong predictions          User experience      Model accuracy drops
   Production fails          Business decisions wrong    Revenue loss         Predictions useless
   Model useless             Customer churn             System timeout       Features outdated

        |                          |                          |                 |
        -------------------------------------------------------------------------
                                         |
                                         |
                               MODEL RELIABILITY SCORE

                         If ANY pillar is RED:
                         → Model is broken
                         → Predictions are wrong
                         → Business loses money
```

---

## 🎯 INTENT BEHIND ML ENGINEER QUESTIONS

### [1] DATA LEAKAGE - "Why does time-aware splitting matter?"

**Intent**: Test if you understand temporal data correctly

**What they're really testing:**
- Do you know not to use future data to predict past?
- Can you prevent data leakage?
- Do you understand why random split fails for time-series?

**Questions map to:**
- "How did you prevent data leakage in your time-aware train/test split?" → Tests temporal awareness
- "Why time-aware splitting?" → Tests understanding of leakage
- "How do you handle temporal validation?" → Tests proper methodology

**Why it matters:**
- Using future data = fake accuracy
- Model looks great in test, fails in production
- Business makes wrong decisions based on fake metrics

**Your portfolio shows:**
- Churn ML Pipeline: "How did you prevent data leakage in your time-aware train/test split?"
- This is THE critical question for ML Engineer roles

---

### [2] MODEL DRIFT - "Why does production monitoring matter?"

**Intent**: Test if you understand model lifecycle

**What they're really testing:**
- Do you know models degrade over time?
- Can you detect when model breaks?
- Do you understand retraining triggers?

**Questions map to:**
- "How do you handle model drift over time?" → Tests monitoring
- "How do you monitor model performance in production?" → Tests observability
- "What's your approach to model retraining?" → Tests lifecycle

**Why it matters:**
- Model trained on 2023 data, world changed in 2024
- Predictions become wrong
- Business loses money on bad decisions
- Customer churn increases

**Your portfolio shows:**
- Churn ML Pipeline: "How do you handle model drift over time?"
- Fraud Detection: "How do you handle concept drift in fraud patterns?"

---

### [3] PREDICTION LATENCY - "Why does speed matter?"

**Intent**: Test if you understand production constraints

**What they're really testing:**
- Do you know latency requirements?
- Can you optimize for speed?
- Do you understand trade-offs (accuracy vs speed)?

**Questions map to:**
- "How did you achieve < 100ms latency?" → Tests optimization
- "How do you handle feature computation in sub-100ms?" → Tests real-time design
- "Why statistical methods over ML for real-time?" → Tests trade-off understanding

**Why it matters:**
- User clicks "predict" → waits 5 seconds → leaves
- Real-time fraud detection → 500ms delay → transaction already processed
- Revenue loss from slow predictions

**Your portfolio shows:**
- Fraud Detection: "How did you achieve less than 100ms latency?"
- This shows you understand production ML constraints

---

### [4] FEATURE STALENESS - "Why does feature freshness matter?"

**Intent**: Test if you understand feature engineering in production

**What they're really testing:**
- Do you know features need to be fresh?
- Can you design feature pipelines?
- Do you understand feature store concepts?

**Questions map to:**
- "How do you handle real-time feature engineering?" → Tests freshness
- "What's your approach to feature computation?" → Tests pipeline design
- "How do you ensure feature consistency?" → Tests feature store

**Why it matters:**
- Model uses "last 30 days transactions" → feature updated 1 hour ago
- Predictions based on stale features = wrong predictions
- Model accuracy drops over time

**Your portfolio shows:**
- Fraud Detection: "Walk me through your real-time feature engineering approach"
- Churn ML Pipeline: "Walk me through your feature engineering process"

---

## 🔥 FAILURE MODES

### If DATA LEAKAGE > 2%:
- Model accuracy is fake
- Production performance much worse
- Business makes wrong decisions
- **You get fired when model fails in production**

### If MODEL DRIFT > 10%:
- Predictions become wrong
- Business loses money
- Customer experience degrades
- **You get fired when revenue drops**

### If PREDICTION LATENCY > 500ms:
- User experience is bad
- Real-time systems break
- Revenue loss from slow predictions
- **You get fired when users complain**

### If FEATURE STALENESS > 5 min:
- Features are outdated
- Model accuracy drops
- Predictions become useless
- **You get fired when predictions are wrong**

---

## ✅ YOUR PORTFOLIO CONNECTION

### Churn ML Pipeline shows:
- ✅ Time-aware splitting (no leakage)
- ✅ Feature engineering
- ✅ Model monitoring
- ✅ Model drift handling

### Fraud Detection shows:
- ✅ Real-time latency (< 100ms)
- ✅ Real-time feature engineering
- ✅ Statistical methods (fast predictions)
- ✅ Concept drift handling

**Every ML question maps to these 4 pillars.**
