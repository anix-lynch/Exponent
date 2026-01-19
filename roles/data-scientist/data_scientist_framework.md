# 🧠 Data Scientist Interview Mindmap (Systematic)

## 📚 Resources

**GitHub Repo**: https://github.com/anix-lynch/Exponent

**Source**: https://www.tryexponent.com/questions?role=data-science

---

## 📊 Question Distribution

```
Behavioral                                         100 questions
Data Analysis - Root Cause                          20 questions
Machine Learning - Model Evaluation                 11 questions
Coding                                              10 questions
Data Analysis - Business Metrics                     7 questions
SQL                                                  6 questions
Machine Learning - Supervised                        4 questions
Statistics & Experimentation - A/B Testing           4 questions
Statistics & Experimentation - Probability           4 questions
Deep Learning                                        3 questions
Machine Learning - Unsupervised                      1 questions
Statistics & Experimentation - Hypothesis Testing    1 questions
Computer Vision                                      1 questions
Recommendation Systems                               1 questions
```

**Total: 173 questions across 14 categories**

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

## Key Categories

### Behavioral

```
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
```

---

### Data Analysis - Root Cause

```
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
```

---

### Machine Learning - Model Evaluation

```
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
```

---

### Coding

```
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
```

---

### Data Analysis - Business Metrics

```
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
```

---

### SQL

```
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
```

---

### Machine Learning - Supervised

```
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
```

---

### Statistics & Experimentation - A/B Testing

```
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
```

---

### Statistics & Experimentation - Probability

```
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
```

---

### Deep Learning

```
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
```

---


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
