# Portfolio to Pillars Mapping

**How YOUR projects demonstrate the 4 pillars for each role**

---

## 🏗️ DATA ENGINEER - Your Portfolio Mapping

### [1] DUPLICATION
**Your Projects:**
- ✅ **Coffeeverse**: "How do you handle duplicate records in your pipeline?"
- ✅ **Cocktailverse**: "What was your approach to deduplication?"
- ✅ **Marketing Analytics**: "What's your deduplication strategy for ad campaigns?"

**What to say:**
> "In Coffeeverse, I implemented idempotency checks to prevent duplicates, ensuring duplicate rate stays < 2%. This prevents revenue inflation and fake growth metrics."

### [2] LATENESS
**Your Projects:**
- ✅ **Cocktailverse**: "How did you achieve less than 5 minute data latency?"
- ✅ **Coffeeverse**: "What was your strategy for handling late-arriving data?"

**What to say:**
> "In Cocktailverse, I optimized the BigQuery pipeline to achieve < 5 minute latency from API ingestion to dashboard, ensuring data freshness SLAs are met and preventing dashboard rewrites."

### [3] TIME TRAVEL
**Your Projects:**
- ✅ **Cocktailverse**: "How do you handle schema changes without breaking downstream?"
- ✅ **Coffeeverse**: "How do you handle schema evolution in your Azure pipeline?"

**What to say:**
> "In Cocktailverse, I designed a star schema with proper SCD handling, ensuring historical accuracy is preserved and preventing attribution lies when data changes."

### [4] CANONICAL
**Your Projects:**
- ✅ **Cocktailverse**: "Walk me through your star schema design" → Single source of truth
- ✅ **Coffeeverse**: "How do you ensure data consistency across different systems?"

**What to say:**
> "In Cocktailverse, I implemented a star schema as the single source of truth, ensuring all teams use the same metric definitions and preventing civil wars over conflicting numbers."

---

## 🤖 ML ENGINEER - Your Portfolio Mapping

### [1] DATA LEAKAGE
**Your Projects:**
- ✅ **Churn ML Pipeline**: "How did you prevent data leakage in your time-aware train/test split?"

**What to say:**
> "In my Churn ML Pipeline, I implemented time-aware splitting to prevent data leakage, ensuring test data never contains future information. This prevents fake accuracy and ensures production performance matches training."

### [2] MODEL DRIFT
**Your Projects:**
- ✅ **Churn ML Pipeline**: "How do you handle model drift over time?"
- ✅ **Fraud Detection**: "How do you handle concept drift in fraud patterns?"

**What to say:**
> "In my Churn ML Pipeline, I monitor model performance in production and have retraining triggers when drift exceeds 5%, ensuring predictions remain accurate as customer behavior changes."

### [3] PREDICTION LATENCY
**Your Projects:**
- ✅ **Fraud Detection**: "How did you achieve less than 100ms latency?"

**What to say:**
> "In my Real-time Fraud Detection system, I optimized feature computation to achieve < 100ms latency, ensuring real-time fraud detection without blocking transactions."

### [4] FEATURE STALENESS
**Your Projects:**
- ✅ **Fraud Detection**: "Walk me through your real-time feature engineering approach"

**What to say:**
> "In my Fraud Detection system, I implemented real-time feature engineering with < 1 minute freshness, ensuring features are always current and model accuracy doesn't degrade."

---

## 🎨 GENAI ENGINEER - Your Portfolio Mapping

### [1] HALLUCINATION
**Your Projects:**
- ✅ **Mocktailverse**: "How do you measure the quality of retrieved documents?"
- ✅ **AI BI Agent**: "How do you implement RAG in your BI agent?"

**What to say:**
> "In Mocktailverse, I implemented RAG with quality checks to ensure retrieved documents are relevant, keeping hallucination rate < 5% and ensuring AI responses are grounded in real data."

### [2] RETRIEVAL QUALITY
**Your Projects:**
- ✅ **Mocktailverse**: "How did you optimize vector search performance?"
- ✅ **AI Agent Job Intelligence**: "How do you implement semantic job matching?"

**What to say:**
> "In Mocktailverse, I optimized vector search to achieve > 80% retrieval precision, ensuring relevant documents are found and preventing model confusion from irrelevant context."

### [3] CONTEXT WINDOW
**Your Projects:**
- ✅ **Mocktailverse**: "How did you decide on chunk size for document processing?"

**What to say:**
> "In Mocktailverse, I designed a chunking strategy that keeps context window usage < 80%, preventing truncation and ensuring complete information is available for generation."

### [4] COST PER QUERY
**Your Projects:**
- ✅ **Mocktailverse**: "How did you handle costs for embedding generation at scale?"
- ✅ **Mocktailverse**: "You mention the system costs $1-2/month. How did you achieve that?"

**What to say:**
> "In Mocktailverse, I optimized Bedrock API calls and implemented caching strategies to keep cost per query < $0.01, ensuring the system runs for $1-2/month while maintaining quality."

---

## 📈 DATA SCIENTIST - Your Portfolio Mapping

### [1] STATISTICAL SIGNIFICANCE
**Your Projects:**
- ⚠️ **Marketing Analytics**: Could add A/B testing with p-values
- ✅ **AI BI Agent**: "What's your approach to statistical analysis automation?"

**What to say:**
> "In my Marketing Analytics project, I'm extending it with A/B testing capabilities using statistical significance testing (p < 0.05) to ensure results are reliable and not random chance."

### [2] BUSINESS IMPACT
**Your Projects:**
- ✅ **Marketing Analytics**: CTR, CPC, ROAS metrics
- ✅ **Churn ML Pipeline**: Could emphasize business impact

**What to say:**
> "In my Marketing Analytics dashboard, I compute business metrics like ROAS and connect insights directly to revenue impact, ensuring every analysis has actionable business value."

### [3] EXPERIMENT DESIGN
**Your Projects:**
- ⚠️ **Marketing Analytics**: Could add A/B testing module

**What to say:**
> "I'm extending my Marketing Analytics project with A/B testing capabilities, designing controlled experiments to prevent selection bias and ensure valid conclusions."

### [4] ROOT CAUSE
**Your Projects:**
- ✅ **AI BI Agent**: Automated EDA
- ⚠️ **Marketing Analytics**: Could add root cause analysis

**What to say:**
> "In my AI BI Agent, I implemented automated EDA with root cause analysis capabilities, distinguishing correlation from causation to ensure we fix the right problems."

---

## 📊 DATA ANALYST - Your Portfolio Mapping

### [1] METRIC MISMATCH
**Your Projects:**
- ✅ **Cocktailverse**: Star schema (single source of truth)
- ✅ **Marketing Analytics**: Clear metric definitions (CTR, CPC, ROAS)

**What to say:**
> "In Cocktailverse, I designed a star schema as the single source of truth, ensuring all teams use consistent metric definitions and preventing conflicts over numbers."

### [2] MISSING CONTEXT
**Your Projects:**
- ✅ **Finance/VC Background**: Business context understanding
- ✅ **Marketing Analytics**: Business metrics

**What to say:**
> "With my finance/VC background, I understand business context deeply. In Marketing Analytics, I ensure every metric is interpreted with business context, not just raw numbers."

### [3] CORRELATION TRAP
**Your Projects:**
- ✅ **AI BI Agent**: Automated EDA
- ⚠️ **Marketing Analytics**: Could add root cause analysis

**What to say:**
> "In my AI BI Agent, I implemented root cause analysis to distinguish correlation from causation, ensuring we identify true causes, not spurious relationships."

### [4] STORYTELLING FAIL
**Your Projects:**
- ✅ **Marketing Analytics**: Dashboard with KPIs
- ✅ **Finance/VC Background**: Stakeholder communication

**What to say:**
> "In Marketing Analytics, I built dashboards that connect insights to actionable recommendations, ensuring every analysis drives business decisions, not just reports numbers."

---

## 🎯 Quick Reference: Project → Pillar

### Coffeeverse → DE Pillars
- Duplication: Deduplication strategy
- Lateness: Late-arriving data handling
- Time Travel: Schema evolution
- Canonical: Data consistency

### Cocktailverse → DE Pillars
- Duplication: Deduplication approach
- Lateness: < 5 min latency achievement
- Time Travel: Schema change handling
- Canonical: Star schema design

### Churn ML Pipeline → ML Pillars
- Data Leakage: Time-aware splitting
- Model Drift: Drift monitoring
- Prediction Latency: FastAPI serving
- Feature Staleness: Feature engineering

### Fraud Detection → ML Pillars
- Data Leakage: Statistical methods (no future data)
- Model Drift: Concept drift handling
- Prediction Latency: < 100ms achievement
- Feature Staleness: Real-time feature engineering

### Mocktailverse → GenAI Pillars
- Hallucination: RAG implementation
- Retrieval Quality: Vector search optimization
- Context Window: Chunking strategy
- Cost Per Query: $1-2/month optimization

### AI Agent Job Intelligence → GenAI Pillars
- Hallucination: RAG grounding
- Retrieval Quality: Semantic search
- Context Window: Embedding management
- Cost Per Query: Cost optimization

### Marketing Analytics → DS/DA Pillars
- Statistical Significance: (Could add A/B testing)
- Business Impact: CTR, ROAS metrics
- Experiment Design: (Could add A/B testing)
- Root Cause: (Could add analysis)

---

**Memorize: Which project shows which pillar. Connect them in interviews.**
