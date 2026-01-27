# 🧠 Quick Reference - Memorize the 4 Pillars

**Memorize these. They're what gets you fired. Know them cold.**

---

## 📊 DATA ENGINEER - 4 Pillars

```
[1] DUPLICATION - ตัวเลขพอง เพราะความซ้ำ
   → Duplicate Rate < 2% = SAFE | > 5% = FUCKED
   → Impact: Revenue inflation, fake growth

[2] LATENESS - ตัวเลขย้อน เพราะมาช้า
   → < 1 hr = GOD | > 24 hr = SNAPSHOT NOW
   → Impact: Dashboard rewrites, CFO rage

[3] TIME TRAVEL - เขียนอดีตใหม่ เพราะ SCD พัง
   → = 0 = CLEAN | > 0 = LYING
   → Impact: History rewrite, attribution lies

[4] CANONICAL - ความจริงไม่กลาง เพราะใช้หลายแหล่ง
   → = 1 = HEAVEN | ≥ 3 = CIVIL WAR
   → Impact: Teams fight, nobody trusts data
```

**Memory trick**: "DLTC" - Data Late Time Canonical
- **D**uplication (numbers inflate)
- **L**ateness (data late)
- **T**ime Travel (SCD breaks)
- **C**anonical (multiple truths)

---

## 🤖 ML ENGINEER - 4 Pillars

```
[1] DATA LEAKAGE - อนาคตรั่วไหล เพราะใช้ข้อมูลอนาคต
   → = 0% = CLEAN | > 2% = CHEATING
   → Impact: Fake accuracy, production fails

[2] MODEL DRIFT - โมเดลลืม เพราะโลกเปลี่ยน
   → < 5% = STABLE | > 10% = BROKEN
   → Impact: Wrong predictions, revenue loss

[3] PREDICTION LATENCY - ทำนายช้าเกินไป เพราะ compute ช้า
   → < 100ms = REAL-TIME | > 500ms = TOO SLOW
   → Impact: User experience, revenue loss

[4] FEATURE STALENESS - ฟีเจอร์เก่า เพราะ update ช้า
   → < 1 min = FRESH | > 5 min = ROTTEN
   → Impact: Model accuracy drops, predictions useless
```

**Memory trick**: "DLPF" - Data Leakage, Latency, Feature Freshness
- **D**ata Leakage (future leaks)
- **L**atency (too slow)
- **P**rediction (model drift)
- **F**eature (stale features)

---

## 🎨 GENAI ENGINEER - 4 Pillars

```
[1] HALLUCINATION - AI พูดโกหก เพราะไม่มี grounding
   → < 5% = GROUNDED | > 15% = LYING
   → Impact: Wrong answers, user loses trust

[2] RETRIEVAL QUALITY - หาข้อมูลผิด เพราะ vector search พัง
   → > 80% = EXCELLENT | < 60% = BROKEN
   → Impact: Irrelevant context, bad recommendations

[3] CONTEXT WINDOW - ใส่ข้อมูลมากเกิน เพราะ token limit
   → < 80% = SAFE | > 95% = OVERFLOW
   → Impact: Truncated responses, lost information

[4] COST PER QUERY - ใช้เงินมากเกิน เพราะ API ราคาแพง
   → < $0.01 = CHEAP | > $0.05 = EXPENSIVE
   → Impact: Budget overrun, project cancelled
```

**Memory trick**: "HRCC" - Hallucination, Retrieval, Context, Cost
- **H**allucination (AI lies)
- **R**etrieval (wrong docs)
- **C**ontext (too much)
- **C**ost (too expensive)

---

## 📈 DATA SCIENTIST - 4 Pillars

```
[1] STATISTICAL SIGNIFICANCE - สถิติไม่น่าเชื่อถือ เพราะ p-value ผิด
   → p < 0.01 = RIGOROUS | p > 0.05 = NOT SIGNIFICANT
   → Impact: Wrong conclusions, false discoveries

[2] BUSINESS IMPACT - ผลกระทบไม่ชัดเจน เพราะไม่เชื่อมโยง
   → Direct $ link = ACTIONABLE | No link = USELESS
   → Impact: No action taken, business ignores you

[3] EXPERIMENT DESIGN - ทดลองผิดวิธี เพราะ bias
   → No bias = CLEAN | High bias = BROKEN
   → Impact: Wrong decisions, wasted resources

[4] ROOT CAUSE - หาสาเหตุผิด เพราะ correlation ≠ causation
   → Causal = TRUTH | Spurious = LIES
   → Impact: Wrong fixes, problem persists
```

**Memory trick**: "SBER" - Significance, Business, Experiment, Root
- **S**tatistical (p-value)
- **B**usiness (impact)
- **E**xperiment (bias)
- **R**oot (causation)

---

## 📊 DATA ANALYST - 4 Pillars

```
[1] METRIC MISMATCH - ตัวเลขไม่ตรงกัน เพราะ definition ผิด
   → = 1 = HEAVEN | ≥ 3 = CIVIL WAR
   → Impact: Teams fight, nobody trusts data

[2] MISSING CONTEXT - บริบทหายไป เพราะไม่รู้ business context
   → > 80% = UNDERSTANDS | < 60% = CLUELESS
   → Impact: Wrong interpretation, business ignores you

[3] CORRELATION TRAP - สาเหตุผิด เพราะ correlation ≠ causation
   → Causal = TRUTH | Spurious = LIES
   → Impact: Wrong fixes, problem persists

[4] STORYTELLING FAIL - บอกเรื่องไม่ชัด เพราะไม่เชื่อมโยง insight → action
   → > 80% = ACTIONABLE | < 60% = USELESS
   → Impact: No action taken, wasted analysis
```

**Memory trick**: "MMCS" - Metric Mismatch, Missing Context, Correlation, Storytelling
- **M**etric (mismatch)
- **M**issing (context)
- **C**orrelation (trap)
- **S**torytelling (fail)

---

## 🎯 ONE-LINER MEMORY AIDS

### Data Engineer: "DLTC"
- **D**uplication → Numbers inflate
- **L**ateness → Data late
- **T**ime Travel → SCD breaks
- **C**anonical → Multiple truths

### ML Engineer: "DLPF"
- **D**ata Leakage → Future leaks
- **L**atency → Too slow
- **P**rediction → Model drifts
- **F**eature → Stale features

### GenAI Engineer: "HRCC"
- **H**allucination → AI lies
- **R**etrieval → Wrong docs
- **C**ontext → Too much
- **C**ost → Too expensive

### Data Scientist: "SBER"
- **S**tatistical → p-value
- **B**usiness → Impact
- **E**xperiment → Bias
- **R**oot → Causation

### Data Analyst: "MMCS"
- **M**etric → Mismatch
- **M**issing → Context
- **C**orrelation → Trap
- **S**torytelling → Fail

---

## 🔥 THE PATTERN

**Every role = 4 pillars. If ANY breaks = You get fired.**

**Memorize:**
1. The 4 pillar names
2. The thresholds (Safe/Warning/Fucked)
3. The impact (what happens when it breaks)

**Then in interviews:**
- Map questions to pillars
- Show you understand thresholds
- Demonstrate you prevent failures

---

**Practice saying these out loud. Know them cold.**
