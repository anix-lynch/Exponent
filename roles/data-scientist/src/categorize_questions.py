"""
Categorize Data Scientist questions into interview categories
COMPREHENSIVE NESTED CATEGORIZATION for top-tier role
"""
import json
import os

# Data Scientist Categories (with nested subcategories)
CATEGORIES = [
    "Behavioral",
    "Machine Learning - Supervised",
    "Machine Learning - Unsupervised", 
    "Machine Learning - Model Evaluation",
    "Machine Learning - Feature Engineering",
    "Statistics & Experimentation - A/B Testing",
    "Statistics & Experimentation - Hypothesis Testing",
    "Statistics & Experimentation - Probability",
    "Data Analysis - Exploratory",
    "Data Analysis - Root Cause",
    "Data Analysis - Business Metrics",
    "SQL",
    "Coding",
    "Model Deployment & Production",
    "Deep Learning",
    "Time Series",
    "NLP",
    "Computer Vision",
    "Recommendation Systems",
    "Data Cleaning & Preprocessing"
]

def categorize_question(question_text, url=""):
    """Categorize a Data Scientist question with nested subcategories"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral
    if any(phrase in q_lower for phrase in [
        'tell me about a time', 'describe a time', 'walk me through a time',
        'have you ever', 'give an example'
    ]):
        categories.append("Behavioral")
    
    # Machine Learning - Supervised
    if any(keyword in q_lower for keyword in [
        'regression', 'classification', 'supervised', 'predict', 'prediction',
        'linear regression', 'logistic regression', 'random forest', 'gradient boosting',
        'xgboost', 'decision tree', 'svm', 'support vector'
    ]):
        categories.append("Machine Learning - Supervised")
    
    # Machine Learning - Unsupervised
    if any(keyword in q_lower for keyword in [
        'clustering', 'unsupervised', 'k-means', 'hierarchical clustering',
        'dimensionality reduction', 'pca', 'principal component', 't-sne'
    ]):
        categories.append("Machine Learning - Unsupervised")
    
    # Machine Learning - Model Evaluation
    if any(keyword in q_lower for keyword in [
        'evaluate', 'evaluation', 'metrics', 'accuracy', 'precision', 'recall',
        'f1 score', 'roc', 'auc', 'confusion matrix', 'cross-validation',
        'overfitting', 'underfitting', 'bias-variance', 'model performance'
    ]):
        categories.append("Machine Learning - Model Evaluation")
    
    # Machine Learning - Feature Engineering
    if any(keyword in q_lower for keyword in [
        'feature engineering', 'feature selection', 'feature extraction',
        'feature importance', 'create features'
    ]):
        categories.append("Machine Learning - Feature Engineering")
    
    # Statistics & Experimentation - A/B Testing
    if any(keyword in q_lower for keyword in [
        'a/b test', 'ab test', 'experiment', 'test design', 'control group',
        'treatment group', 'randomization'
    ]):
        categories.append("Statistics & Experimentation - A/B Testing")
    
    # Statistics & Experimentation - Hypothesis Testing
    if any(keyword in q_lower for keyword in [
        'hypothesis test', 'statistical significance', 'p-value', 't-test',
        'z-test', 'chi-square', 'anova', 'confidence interval'
    ]):
        categories.append("Statistics & Experimentation - Hypothesis Testing")
    
    # Statistics & Experimentation - Probability
    if any(keyword in q_lower for keyword in [
        'probability', 'distribution', 'normal distribution', 'binomial',
        'poisson', 'expected value', 'variance', 'standard deviation'
    ]):
        categories.append("Statistics & Experimentation - Probability")
    
    # Data Analysis - Exploratory
    if any(keyword in q_lower for keyword in [
        'explore', 'exploratory', 'eda', 'data exploration', 'visualize',
        'visualization', 'understand data'
    ]):
        categories.append("Data Analysis - Exploratory")
    
    # Data Analysis - Root Cause
    if any(keyword in q_lower for keyword in [
        'drop', 'decline', 'decrease', 'investigate', 'why', 'root cause',
        'diagnose', 'sudden change'
    ]):
        categories.append("Data Analysis - Root Cause")
    
    # Data Analysis - Business Metrics
    if any(keyword in q_lower for keyword in [
        'metric', 'kpi', 'measure success', 'business impact', 'roi'
    ]):
        categories.append("Data Analysis - Business Metrics")
    
    # SQL
    if any(keyword in q_lower for keyword in [
        'sql', 'query', 'select', 'join', 'database'
    ]):
        categories.append("SQL")
    
    # Coding
    if any(keyword in q_lower for keyword in [
        'code', 'implement', 'write a function', 'algorithm', 'python'
    ]):
        categories.append("Coding")
    
    # Model Deployment & Production
    if any(keyword in q_lower for keyword in [
        'production', 'deploy', 'deployment', 'model in production',
        'serve model', 'ml ops', 'mlops', 'monitoring'
    ]):
        categories.append("Model Deployment & Production")
    
    # Deep Learning
    if any(keyword in q_lower for keyword in [
        'deep learning', 'neural network', 'cnn', 'rnn', 'lstm', 'transformer',
        'pytorch', 'tensorflow', 'keras'
    ]):
        categories.append("Deep Learning")
    
    # Time Series
    if any(keyword in q_lower for keyword in [
        'time series', 'forecasting', 'forecast', 'arima', 'seasonality',
        'trend', 'temporal'
    ]):
        categories.append("Time Series")
    
    # NLP
    if any(keyword in q_lower for keyword in [
        'nlp', 'natural language', 'text', 'sentiment', 'tokenization',
        'word embedding', 'bert', 'gpt'
    ]):
        categories.append("NLP")
    
    # Computer Vision
    if any(keyword in q_lower for keyword in [
        'computer vision', 'image', 'object detection', 'image classification',
        'segmentation', 'opencv'
    ]):
        categories.append("Computer Vision")
    
    # Recommendation Systems
    if any(keyword in q_lower for keyword in [
        'recommendation', 'recommender', 'collaborative filtering',
        'content-based filtering'
    ]):
        categories.append("Recommendation Systems")
    
    # Data Cleaning & Preprocessing
    if any(keyword in q_lower for keyword in [
        'outlier', 'missing data', 'data cleaning', 'preprocessing',
        'imputation', 'handle missing', 'data quality', 'imbalanced'
    ]):
        categories.append("Data Cleaning & Preprocessing")
    
    # Default to Behavioral if no categories found
    if not categories:
        categories.append("Behavioral")
    
    return list(set(categories))

def main():
    """Load raw questions, categorize them, and save results"""
    
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    raw_path = os.path.join(data_dir, 'questions_raw.json')
    
    with open(raw_path, 'r') as f:
        questions = json.load(f)
    
    print(f"📊 Categorizing {len(questions)} Data Scientist questions...")
    print("🎯 Using COMPREHENSIVE NESTED categorization for top-tier role!")
    
    categorized = []
    by_category = {cat: [] for cat in CATEGORIES}
    
    for q in questions:
        q_text = q['question']
        q_url = q.get('url', '')
        
        cats = categorize_question(q_text, q_url)
        q['categories'] = cats
        categorized.append(q)
        
        for cat in cats:
            if cat in by_category:
                by_category[cat].append({
                    'question': q_text,
                    'url': q_url
                })
    
    categorized_path = os.path.join(data_dir, 'questions_categorized.json')
    with open(categorized_path, 'w') as f:
        json.dump(categorized, f, indent=2)
    print(f"✅ Saved to {categorized_path}")
    
    by_category_path = os.path.join(data_dir, 'questions_by_category.json')
    with open(by_category_path, 'w') as f:
        json.dump(by_category, f, indent=2)
    print(f"✅ Saved to {by_category_path}")
    
    print("\n" + "="*70)
    print("📋 Questions per category:")
    print("="*70)
    
    category_counts = [(cat, len(by_category[cat])) for cat in CATEGORIES]
    category_counts.sort(key=lambda x: x[1], reverse=True)
    
    for cat, count in category_counts:
        if count > 0:
            print(f"  {cat.ljust(45)} {count:>3}")
    
    print(f"\n📊 Total questions: {len(categorized)}")
    print("🎯 Nested categorization complete!")

if __name__ == "__main__":
    main()
