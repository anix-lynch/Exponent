"""
Generate comprehensive Data Scientist frameworks matching Data Analyst quality
"""
import json
import os

def get_framework_for_category(category):
    """Return comprehensive ASCII framework for each DS category"""
    
    frameworks = {
        "Behavioral": """
Behavioral (STAR Method)
├─ Situation
│  ├─ Context and background
│  ├─ Business metrics at the time
│  ├─ Team and stakeholders
│  └─ Why this was important
│
├─ Task
│  ├─ Your specific responsibility
│  ├─ Goals and objectives
│  ├─ Constraints (time, resources, data)
│  └─ Success criteria
│
├─ Action
│  ├─ Approach and methodology
│  ├─ Models/techniques used
│  ├─ How you collaborated
│  ├─ Challenges you overcame
│  └─ Iterations and improvements
│
└─ Result
   ├─ Quantifiable outcomes
   ├─ Business impact (revenue, efficiency, etc.)
   ├─ Model performance metrics
   ├─ What you learned
   └─ How you'd apply it again
""",
        "Machine Learning - Supervised": """
Machine Learning - Supervised
├─ Understand the problem
│  ├─ Business objective
│  ├─ Prediction task (regression/classification)
│  ├─ Success metrics
│  └─ Constraints
│
├─ Data preparation
│  ├─ Feature engineering
│  ├─ Handle missing data
│  ├─ Encode categorical variables
│  └─ Train/validation/test split
│
├─ Model selection
│  ├─ Linear models (regression, logistic)
│  ├─ Tree-based (RF, XGBoost, etc.)
│  ├─ Neural networks
│  └─ Consider complexity vs interpretability
│
├─ Training and tuning
│  ├─ Hyperparameter optimization
│  ├─ Cross-validation
│  ├─ Regularization (L1/L2)
│  └─ Monitor for overfitting
│
└─ Evaluation
   ├─ Appropriate metrics (accuracy, precision, recall, RMSE, etc.)
   ├─ Confusion matrix / ROC curve
   ├─ Feature importance
   └─ Business impact
""",
        "Machine Learning - Unsupervised": """
Machine Learning - Unsupervised
├─ Define objective
│  ├─ What patterns to discover?
│  ├─ Clustering or dimensionality reduction?
│  └─ How will results be used?
│
├─ Data preparation
│  ├─ Feature scaling/normalization
│  ├─ Handle missing values
│  ├─ Remove outliers (if appropriate)
│  └─ Feature selection
│
├─ Algorithm selection
│  ├─ Clustering: K-means, hierarchical, DBSCAN
│  ├─ Dimensionality reduction: PCA, t-SNE, UMAP
│  └─ Consider data characteristics
│
├─ Model training
│  ├─ Choose number of clusters/components
│  ├─ Initialize properly
│  ├─ Iterate and refine
│  └─ Validate stability
│
└─ Evaluation and interpretation
   ├─ Silhouette score, elbow method
   ├─ Visualize results
   ├─ Interpret clusters/components
   └─ Validate with domain knowledge
""",
        "Machine Learning - Model Evaluation": """
Machine Learning - Model Evaluation
├─ Choose appropriate metrics
│  ├─ Classification: accuracy, precision, recall, F1, AUC-ROC
│  ├─ Regression: RMSE, MAE, R², MAPE
│  ├─ Consider business context
│  └─ Class imbalance considerations
│
├─ Cross-validation
│  ├─ K-fold cross-validation
│  ├─ Stratified for imbalanced data
│  ├─ Time series: forward chaining
│  └─ Report mean and std of metrics
│
├─ Bias-variance tradeoff
│  ├─ Underfitting (high bias)
│  ├─ Overfitting (high variance)
│  ├─ Learning curves
│  └─ Regularization strategies
│
├─ Error analysis
│  ├─ Confusion matrix
│  ├─ Analyze misclassifications
│  ├─ Feature importance
│  └─ Identify systematic errors
│
└─ Production considerations
   ├─ Model robustness
   ├─ Inference latency
   ├─ Model size
   └─ Monitoring and retraining
""",
        "Machine Learning - Feature Engineering": """
Machine Learning - Feature Engineering
├─ Understand the data
│  ├─ Domain knowledge
│  ├─ Data types and distributions
│  ├─ Missing values and outliers
│  └─ Correlations
│
├─ Create new features
│  ├─ Interactions (A * B, A / B)
│  ├─ Aggregations (sum, mean, count)
│  ├─ Time-based (day of week, hour, lag)
│  ├─ Text features (TF-IDF, embeddings)
│  └─ Domain-specific transformations
│
├─ Transform existing features
│  ├─ Scaling (standardization, normalization)
│  ├─ Encoding (one-hot, label, target)
│  ├─ Binning/discretization
│  └─ Log/power transformations
│
├─ Feature selection
│  ├─ Remove low variance features
│  ├─ Remove highly correlated features
│  ├─ Feature importance from models
│  ├─ Recursive feature elimination
│  └─ L1 regularization
│
└─ Validate
   ├─ Check for data leakage
   ├─ Validate on holdout set
   ├─ Monitor feature drift
   └─ Document feature definitions
""",
        "Statistics & Experimentation - A/B Testing": """
Statistics & Experimentation - A/B Testing
├─ Design the experiment
│  ├─ Define hypothesis (null and alternative)
│  ├─ Choose primary metric
│  ├─ Secondary and guardrail metrics
│  ├─ Determine sample size (power analysis)
│  └─ Randomization strategy
│
├─ Run the test
│  ├─ Ensure proper randomization
│  ├─ Monitor for issues (SRM, bugs)
│  ├─ Avoid peeking
│  └─ Collect sufficient data
│
├─ Analyze results
│  ├─ Calculate statistical significance (p-value)
│  ├─ Calculate confidence intervals
│  ├─ Check for practical significance
│  ├─ Segment analysis
│  └─ Check guardrail metrics
│
├─ Interpret findings
│  ├─ Can we reject null hypothesis?
│  ├─ Effect size and business impact
│  ├─ Consider external factors
│  └─ Long-term vs short-term effects
│
└─ Make decision
   ├─ Ship, iterate, or kill
   ├─ Document learnings
   └─ Plan next experiments
""",
        "Statistics & Experimentation - Hypothesis Testing": """
Statistics & Experimentation - Hypothesis Testing
├─ Formulate hypotheses
│  ├─ Null hypothesis (H0)
│  ├─ Alternative hypothesis (H1)
│  └─ One-tailed vs two-tailed
│
├─ Choose test
│  ├─ t-test (means, small samples)
│  ├─ z-test (means, large samples)
│  ├─ Chi-square (categorical)
│  ├─ ANOVA (multiple groups)
│  └─ Non-parametric alternatives
│
├─ Set significance level
│  ├─ Alpha (typically 0.05)
│  ├─ Type I error (false positive)
│  ├─ Type II error (false negative)
│  └─ Power (1 - Type II error)
│
├─ Calculate test statistic
│  ├─ Compute from sample data
│  ├─ Compare to null distribution
│  └─ Calculate p-value
│
└─ Make decision
   ├─ Reject or fail to reject H0
   ├─ Confidence interval
   ├─ Practical significance
   └─ Communicate findings
""",
        "Statistics & Experimentation - Probability": """
Statistics & Experimentation - Probability
├─ Understand the problem
│  ├─ What are we trying to find?
│  ├─ What information is given?
│  └─ What assumptions can we make?
│
├─ Identify distribution
│  ├─ Discrete: binomial, Poisson, geometric
│  ├─ Continuous: normal, exponential, uniform
│  ├─ Parameters (mean, variance, etc.)
│  └─ Assumptions and conditions
│
├─ Apply probability rules
│  ├─ Addition rule (OR)
│  ├─ Multiplication rule (AND)
│  ├─ Conditional probability
│  ├─ Bayes' theorem
│  └─ Independence
│
├─ Calculate
│  ├─ Expected value
│  ├─ Variance and standard deviation
│  ├─ Confidence intervals
│  └─ Percentiles
│
└─ Interpret
   ├─ What does the result mean?
   ├─ Practical implications
   └─ Uncertainty and assumptions
""",
        "Data Analysis - Root Cause": """
Data Analysis - Root Cause
├─ Define the problem
│  ├─ What metric changed?
│  ├─ When did it change?
│  ├─ How much did it change?
│  └─ Why does it matter?
│
├─ Form hypotheses
│  ├─ Internal factors (product changes, bugs)
│  ├─ External factors (seasonality, competition)
│  ├─ User behavior changes
│  └─ Data quality issues
│
├─ Segment and drill down
│  ├─ By time (hourly, daily, weekly)
│  ├─ By user cohort (new vs returning)
│  ├─ By platform (iOS, Android, web)
│  ├─ By geography
│  └─ By feature usage
│
├─ Test hypotheses
│  ├─ Gather supporting data
│  ├─ Rule out alternatives
│  ├─ Look for correlations
│  └─ Identify root cause
│
└─ Recommend action
   ├─ Fix the issue
   ├─ Prevent recurrence
   ├─ Monitor going forward
   └─ Expected impact
""",
        "Data Analysis - Business Metrics": """
Data Analysis - Business Metrics
├─ Understand the business
│  ├─ Business model
│  ├─ Key value drivers
│  ├─ User journey
│  └─ Competitive landscape
│
├─ Define metrics
│  ├─ North Star Metric
│  ├─ Leading indicators
│  ├─ Lagging indicators
│  ├─ Input vs output metrics
│  └─ Guardrail metrics
│
├─ Measure and track
│  ├─ Data sources
│  ├─ Calculation methodology
│  ├─ Frequency of measurement
│  ├─ Dashboards and reports
│  └─ Alerts and thresholds
│
├─ Analyze trends
│  ├─ Historical patterns
│  ├─ Seasonality
│  ├─ Growth rates
│  ├─ Cohort analysis
│  └─ Segment comparisons
│
└─ Drive action
   ├─ Insights and recommendations
   ├─ Prioritize initiatives
   ├─ Set targets and goals
   └─ Measure impact
""",
        "SQL": """
SQL
├─ Understand requirements
│  ├─ What question are we answering?
│  ├─ What tables are involved?
│  ├─ What's the grain of the output?
│  └─ Performance considerations
│
├─ Write the query
│  ├─ SELECT appropriate columns
│  ├─ FROM and JOIN tables
│  ├─ WHERE to filter rows
│  ├─ GROUP BY for aggregations
│  ├─ HAVING to filter groups
│  └─ ORDER BY and LIMIT
│
├─ Use advanced features
│  ├─ Window functions (ROW_NUMBER, RANK, LAG, LEAD)
│  ├─ CTEs (WITH clause) for readability
│  ├─ Subqueries
│  ├─ CASE statements
│  └─ Date functions
│
├─ Optimize
│  ├─ Use indexes effectively
│  ├─ Avoid SELECT *
│  ├─ Filter early (WHERE before JOIN)
│  ├─ Limit result set
│  └─ Explain plan
│
└─ Validate
   ├─ Check for nulls
   ├─ Verify row counts
   ├─ Spot check results
   └─ Test edge cases
""",
        "Coding": """
Coding
├─ Understand the problem
│  ├─ Read carefully
│  ├─ Ask clarifying questions
│  ├─ Identify inputs and outputs
│  ├─ Constraints and edge cases
│  └─ Examples
│
├─ Plan the approach
│  ├─ Brute force first
│  ├─ Identify patterns
│  ├─ Choose data structures
│  ├─ Consider time/space complexity
│  └─ Outline algorithm
│
├─ Implement
│  ├─ Write clean, readable code
│  ├─ Use meaningful variable names
│  ├─ Handle edge cases
│  ├─ Add comments for clarity
│  └─ Test as you go
│
├─ Test
│  ├─ Normal cases
│  ├─ Edge cases (empty, single element)
│  ├─ Large inputs
│  └─ Invalid inputs
│
└─ Optimize
   ├─ Time complexity
   ├─ Space complexity
   ├─ Code readability
   └─ Discuss tradeoffs
""",
        "Model Deployment & Production": """
Model Deployment & Production
├─ Prepare for deployment
│  ├─ Model serialization (pickle, joblib, ONNX)
│  ├─ Dependency management
│  ├─ Version control
│  └─ Documentation
│
├─ Deploy
│  ├─ Batch vs real-time
│  ├─ API endpoint (REST, gRPC)
│  ├─ Containerization (Docker)
│  ├─ Orchestration (Kubernetes)
│  └─ A/B testing framework
│
├─ Monitor
│  ├─ Model performance metrics
│  ├─ Prediction latency
│  ├─ Data drift
│  ├─ Concept drift
│  ├─ Error rates
│  └─ Resource usage
│
├─ Maintain
│  ├─ Retrain schedule
│  ├─ Feature store
│  ├─ Model registry
│  ├─ Rollback strategy
│  └─ Incident response
│
└─ Iterate
   ├─ Collect feedback
   ├─ Analyze failures
   ├─ Improve features
   └─ Update model
""",
        "Deep Learning": """
Deep Learning
├─ Problem formulation
│  ├─ Task type (classification, regression, generation)
│  ├─ Data availability
│  ├─ Computational resources
│  └─ Interpretability needs
│
├─ Architecture design
│  ├─ Input layer (shape, preprocessing)
│  ├─ Hidden layers (CNN, RNN, Transformer)
│  ├─ Activation functions (ReLU, tanh, sigmoid)
│  ├─ Output layer (softmax, linear)
│  └─ Number of parameters
│
├─ Training
│  ├─ Loss function
│  ├─ Optimizer (Adam, SGD)
│  ├─ Learning rate schedule
│  ├─ Batch size
│  ├─ Regularization (dropout, batch norm)
│  └─ Early stopping
│
├─ Evaluation
│  ├─ Validation metrics
│  ├─ Learning curves
│  ├─ Overfitting/underfitting
│  └─ Generalization
│
└─ Optimization
   ├─ Hyperparameter tuning
   ├─ Data augmentation
   ├─ Transfer learning
   └─ Model compression
""",
        "Time Series": """
Time Series
├─ Understand the data
│  ├─ Trend
│  ├─ Seasonality
│  ├─ Cyclical patterns
│  ├─ Irregularities/outliers
│  └─ Stationarity
│
├─ Preprocessing
│  ├─ Handle missing values
│  ├─ Detrending
│  ├─ Deseasonalizing
│  ├─ Differencing
│  └─ Scaling
│
├─ Model selection
│  ├─ Classical: ARIMA, SARIMA, Exponential Smoothing
│  ├─ ML: Random Forest, XGBoost with lag features
│  ├─ DL: LSTM, GRU, Transformer
│  └─ Consider forecast horizon
│
├─ Feature engineering
│  ├─ Lag features
│  ├─ Rolling statistics
│  ├─ Time-based features (day of week, month)
│  └─ External variables
│
└─ Evaluation
   ├─ Train/validation/test split (time-based)
   ├─ Metrics: MAE, RMSE, MAPE
   ├─ Forecast vs actual plots
   └─ Residual analysis
""",
        "NLP": """
Natural Language Processing
├─ Text preprocessing
│  ├─ Tokenization
│  ├─ Lowercasing
│  ├─ Remove stopwords
│  ├─ Stemming/lemmatization
│  └─ Handle special characters
│
├─ Feature extraction
│  ├─ Bag of words
│  ├─ TF-IDF
│  ├─ Word embeddings (Word2Vec, GloVe)
│  ├─ Contextual embeddings (BERT, GPT)
│  └─ Character-level features
│
├─ Model selection
│  ├─ Classical: Naive Bayes, SVM, Logistic Regression
│  ├─ Deep learning: RNN, LSTM, Transformer
│  ├─ Pre-trained models: BERT, RoBERTa, GPT
│  └─ Task-specific architectures
│
├─ Training
│  ├─ Handle class imbalance
│  ├─ Sequence padding/truncation
│  ├─ Fine-tuning strategies
│  └─ Regularization
│
└─ Evaluation
   ├─ Accuracy, precision, recall, F1
   ├─ Confusion matrix
   ├─ Error analysis
   └─ Qualitative review
""",
        "Computer Vision": """
Computer Vision
├─ Problem definition
│  ├─ Classification, detection, segmentation
│  ├─ Data availability
│  ├─ Real-time requirements
│  └─ Accuracy needs
│
├─ Data preparation
│  ├─ Image preprocessing (resize, normalize)
│  ├─ Data augmentation (flip, rotate, crop)
│  ├─ Handle class imbalance
│  └─ Train/val/test split
│
├─ Model architecture
│  ├─ CNN basics (conv, pool, FC)
│  ├─ Pre-trained models (ResNet, VGG, EfficientNet)
│  ├─ Transfer learning
│  ├─ Object detection (YOLO, R-CNN)
│  └─ Segmentation (U-Net, Mask R-CNN)
│
├─ Training
│  ├─ Loss function (cross-entropy, focal loss)
│  ├─ Optimizer and learning rate
│  ├─ Batch size
│  └─ Monitor overfitting
│
└─ Evaluation
   ├─ Accuracy, precision, recall
   ├─ IoU for detection/segmentation
   ├─ Confusion matrix
   └─ Visual inspection
""",
        "Recommendation Systems": """
Recommendation Systems
├─ Understand the problem
│  ├─ User-item interactions
│  ├─ Cold start problem
│  ├─ Implicit vs explicit feedback
│  └─ Business objectives
│
├─ Approach selection
│  ├─ Collaborative filtering (user-based, item-based)
│  ├─ Content-based filtering
│  ├─ Hybrid approaches
│  ├─ Matrix factorization
│  └─ Deep learning (neural collaborative filtering)
│
├─ Feature engineering
│  ├─ User features (demographics, behavior)
│  ├─ Item features (attributes, popularity)
│  ├─ Context features (time, location)
│  └─ Interaction features
│
├─ Model training
│  ├─ Handle sparsity
│  ├─ Negative sampling
│  ├─ Regularization
│  └─ Optimize for ranking
│
└─ Evaluation
   ├─ Offline: Precision@K, Recall@K, NDCG, MAP
   ├─ Online: CTR, conversion rate
   ├─ A/B testing
   └─ Diversity and serendipity
""",
        "Data Cleaning & Preprocessing": """
Data Cleaning & Preprocessing
├─ Understand the data
│  ├─ Data types and schema
│  ├─ Data distributions
│  ├─ Summary statistics
│  └─ Data quality issues
│
├─ Handle missing data
│  ├─ Identify patterns (MCAR, MAR, MNAR)
│  ├─ Remove rows/columns
│  ├─ Imputation (mean, median, mode, model-based)
│  └─ Create missing indicator
│
├─ Handle outliers
│  ├─ Identify (IQR, z-score, visualization)
│  ├─ Investigate cause
│  ├─ Remove, cap, or transform
│  └─ Robust methods
│
├─ Handle imbalanced data
│  ├─ Resampling (oversample minority, undersample majority)
│  ├─ SMOTE
│  ├─ Class weights
│  └─ Anomaly detection approaches
│
└─ Transform and scale
   ├─ Normalization (min-max)
   ├─ Standardization (z-score)
   ├─ Log/power transformations
   └─ Encoding (one-hot, label, target)
"""
    }
    
    return frameworks.get(category, "")

def main():
    """Generate comprehensive frameworks"""
    
    # Load data
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    with open(os.path.join(data_dir, 'questions_by_category.json'), 'r') as f:
        by_category = json.load(f)
    
    # Count totals
    total_questions = sum(len(qs) for qs in by_category.values())
    category_counts = [(cat, len(by_category[cat])) for cat in by_category.keys()]
    category_counts.sort(key=lambda x: x[1], reverse=True)
    
    print(f"🚀 Generating comprehensive Data Scientist frameworks...")
    print(f"   Total questions: {total_questions}")
    print(f"   Categories: {len([c for c in category_counts if c[1] > 0])}")
    
    # Generate Question Bank (matching Data Analyst format)
    qb_md = """
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║           DATA SCIENTIST INTERVIEW PREPARATION FRAMEWORK                       ║
║           Mental Models & Complete Question Bank                               ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

This framework provides mental models for approaching each type of data scientist
interview question. Focus on understanding the PATTERN and FRAMEWORK, not 
memorizing answers.

Total Questions: {} across {} categories


""".format(total_questions, len([c for c in category_counts if c[1] > 0]))
    
    # Add each category with framework
    for cat, count in category_counts:
        if count == 0:
            continue
        
        questions = by_category[cat]
        
        qb_md += "=" * 80 + "\n"
        qb_md += f"{cat.upper()}\n"
        qb_md += "=" * 80 + "\n\n"
        qb_md += f"📊 Total Questions: {count}\n\n"
        
        # Add "What they're really testing"
        testing_desc = {
            "Behavioral": "Can you demonstrate DS skills through past experiences using structured storytelling?",
            "Machine Learning - Supervised": "Can you build and evaluate supervised learning models effectively?",
            "Machine Learning - Unsupervised": "Can you discover patterns in unlabeled data?",
            "Machine Learning - Model Evaluation": "Can you properly evaluate and improve model performance?",
            "Machine Learning - Feature Engineering": "Can you create and select features that improve model performance?",
            "Statistics & Experimentation - A/B Testing": "Can you design, run, and analyze experiments rigorously?",
            "Statistics & Experimentation - Hypothesis Testing": "Can you test hypotheses using appropriate statistical methods?",
            "Statistics & Experimentation - Probability": "Can you apply probability theory to solve problems?",
            "Data Analysis - Root Cause": "Can you investigate and diagnose drops or changes in metrics?",
            "Data Analysis - Business Metrics": "Can you define and track the right business metrics?",
            "SQL": "Can you write efficient queries to extract insights from data?",
            "Coding": "Can you implement algorithms and solve coding problems?",
            "Model Deployment & Production": "Can you deploy and maintain models in production?",
            "Deep Learning": "Can you design and train deep neural networks?",
            "Time Series": "Can you forecast and analyze time-dependent data?",
            "NLP": "Can you process and analyze text data?",
            "Computer Vision": "Can you build models to understand images?",
            "Recommendation Systems": "Can you build systems that recommend relevant items?",
            "Data Cleaning & Preprocessing": "Can you prepare messy data for analysis and modeling?"
        }
        
        qb_md += f"🎯 What they're really testing:\n"
        qb_md += f"{testing_desc.get(cat, 'Your data science skills.')}\n\n"
        
        # Add framework
        framework = get_framework_for_category(cat)
        if framework:
            qb_md += "🗺️  Mental Model Framework:\n```\n"
            qb_md += framework.strip() + "\n```\n\n"
        
        # Add questions
        qb_md += f"📝 All {count} Questions:\n\n"
        for i, q in enumerate(questions, 1):
            qb_md += f"{i}. {q['question']}\n"
        
        qb_md += "\n"
    
    # Save Question Bank
    qb_path = os.path.join(os.path.dirname(__file__), '../Data_Scientist_Question_Bank.md')
    with open(qb_path, 'w') as f:
        f.write(qb_md)
    print(f"✅ Generated Data_Scientist_Question_Bank.md")
    
    # Generate Interview Framework (high-level overview)
    fw_md = f"""# 🧠 Data Scientist Interview Mindmap (Systematic)

## 📚 Resources

**GitHub Repo**: https://github.com/anix-lynch/Exponent

**Source**: https://www.tryexponent.com/questions?role=data-science

---

## 📊 Question Distribution

```
"""
    
    for cat, count in category_counts:
        if count > 0:
            fw_md += f"{cat.ljust(50)} {count:>3} questions\n"
    
    fw_md += f"""```

**Total: {total_questions} questions across {len([c for c in category_counts if c[1] > 0])} categories**

---

## 🎯 How to USE this in interviews

When a question comes:

1. **Name the category silently**
2. **Apply that category's framework**
3. Speak in **structured bullets**

---

## 0️⃣ Core Interview Meta-Structure (applies to EVERYTHING)

No matter the category, interviewers are testing:

- **Technical depth** - Do you understand the fundamentals?
- **Practical application** - Can you apply theory to real problems?
- **Communication** - Can you explain complex concepts clearly?
- **Business impact** - Do you connect models to business value?

So every answer should follow this shape:

```
Understand → Plan → Implement → Evaluate → Communicate impact
```

---

"""
    
    # Add key frameworks
    fw_md += "## Key Categories\n\n"
    for cat, count in category_counts[:10]:  # Top 10 categories
        if count > 0:
            fw_md += f"### {cat}\n\n"
            framework = get_framework_for_category(cat)
            if framework:
                fw_md += "```\n" + framework.strip() + "\n```\n\n"
            fw_md += "---\n\n"
    
    fw_md += """
## 💡 Final Tips

### For All Data Scientist Interviews:

1. **Start with the problem** - Understand business context before jumping to solutions
2. **Show your thinking** - Walk through your approach step-by-step
3. **Quantify everything** - Use metrics to evaluate success
4. **Consider tradeoffs** - Accuracy vs speed, complexity vs interpretability
5. **Connect to business** - How does this model drive value?

### Common Mistakes to Avoid:

- ❌ Jumping to complex models without understanding the problem
- ❌ Ignoring data quality and preprocessing
- ❌ Overfitting to training data
- ❌ Not considering production constraints
- ❌ Forgetting to communicate business impact

---

**Check out the [Data_Scientist_Question_Bank.md](./Data_Scientist_Question_Bank.md) for all questions with detailed frameworks!**
"""
    
    # Save Interview Framework
    fw_path = os.path.join(os.path.dirname(__file__), '../INTERVIEW_FRAMEWORK.md')
    with open(fw_path, 'w') as f:
        f.write(fw_md)
    print(f"✅ Generated INTERVIEW_FRAMEWORK.md")
    
    print("="*70)
    print("✅ Data Scientist frameworks complete!")

if __name__ == "__main__":
    main()
