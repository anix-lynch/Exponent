"""
Categorize Product Analyst questions into interview categories
COMPREHENSIVE NESTED CATEGORIZATION for top-tier role
"""
import json
import os

# Product Analyst Categories (with nested subcategories)
CATEGORIES = [
    "Behavioral",
    "Product Metrics - Definition",
    "Product Metrics - Tracking",
    "Product Metrics - Interpretation",
    "A/B Testing - Design",
    "A/B Testing - Analysis",
    "A/B Testing - Interpretation",
    "Data Analysis - Feature Impact",
    "Data Analysis - User Behavior",
    "Data Analysis - Funnel Analysis",
    "Data Analysis - Retention & Churn",
    "SQL",
    "Product Strategy",
    "Product Sense",
    "Dashboard & Visualization",
    "Stakeholder Communication",
    "Prioritization",
    "Root Cause Analysis"
]

def categorize_question(question_text, url=""):
    """Categorize a Product Analyst question with nested subcategories"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral
    if any(phrase in q_lower for phrase in [
        'tell me about a time', 'describe a time', 'walk me through a time',
        'have you ever', 'give an example'
    ]):
        categories.append("Behavioral")
    
    # Product Metrics - Definition
    if any(keyword in q_lower for keyword in [
        'what metrics', 'which metrics', 'define metrics', 'kpi',
        'measure success', 'metrics would you track'
    ]):
        categories.append("Product Metrics - Definition")
    
    # Product Metrics - Tracking
    if any(keyword in q_lower for keyword in [
        'track', 'tracking', 'monitor', 'dashboard'
    ]):
        categories.append("Product Metrics - Tracking")
    
    # Product Metrics - Interpretation
    if any(keyword in q_lower for keyword in [
        'interpret', 'what does it mean', 'metric shows'
    ]):
        categories.append("Product Metrics - Interpretation")
    
    # A/B Testing - Design
    if any(keyword in q_lower for keyword in [
        'design an a/b test', 'design a test', 'a/b test design',
        'experiment design', 'how would you test'
    ]):
        categories.append("A/B Testing - Design")
    
    # A/B Testing - Analysis
    if any(keyword in q_lower for keyword in [
        'analyze a/b test', 'test results', 'experiment results'
    ]):
        categories.append("A/B Testing - Analysis")
    
    # A/B Testing - Interpretation
    if any(keyword in q_lower for keyword in [
        'interpret test', 'what would you conclude', 'test shows'
    ]):
        categories.append("A/B Testing - Interpretation")
    
    # Data Analysis - Feature Impact
    if any(keyword in q_lower for keyword in [
        'feature', 'new feature', 'feature success', 'feature impact',
        'measure the success of a new feature'
    ]):
        categories.append("Data Analysis - Feature Impact")
    
    # Data Analysis - User Behavior
    if any(keyword in q_lower for keyword in [
        'user behavior', 'user engagement', 'how users', 'user activity'
    ]):
        categories.append("Data Analysis - User Behavior")
    
    # Data Analysis - Funnel Analysis
    if any(keyword in q_lower for keyword in [
        'funnel', 'conversion', 'checkout flow', 'conversion flow'
    ]):
        categories.append("Data Analysis - Funnel Analysis")
    
    # Data Analysis - Retention & Churn
    if any(keyword in q_lower for keyword in [
        'retention', 'churn', 'drop in user', 'user retention'
    ]):
        categories.append("Data Analysis - Retention & Churn")
    
    # SQL
    if any(keyword in q_lower for keyword in [
        'sql', 'query', 'write a query', 'database'
    ]):
        categories.append("SQL")
    
    # Product Strategy
    if any(keyword in q_lower for keyword in [
        'product strategy', 'product decision', 'influence', 'product roadmap'
    ]):
        categories.append("Product Strategy")
    
    # Product Sense
    if any(keyword in q_lower for keyword in [
        'product sense', 'product thinking', 'user needs', 'product improvement'
    ]):
        categories.append("Product Sense")
    
    # Dashboard & Visualization
    if any(keyword in q_lower for keyword in [
        'dashboard', 'visualization', 'build a dashboard', 'executive dashboard'
    ]):
        categories.append("Dashboard & Visualization")
    
    # Stakeholder Communication
    if any(keyword in q_lower for keyword in [
        'stakeholder', 'communicate', 'present', 'product manager',
        'disagreed with'
    ]):
        categories.append("Stakeholder Communication")
    
    # Prioritization
    if any(keyword in q_lower for keyword in [
        'prioritize', 'priority', 'which features', 'analyze first'
    ]):
        categories.append("Prioritization")
    
    # Root Cause Analysis
    if any(keyword in q_lower for keyword in [
        'investigate', 'drop', 'decline', 'why', 'root cause'
    ]):
        categories.append("Root Cause Analysis")
    
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
    
    print(f"📊 Categorizing {len(questions)} Product Analyst questions...")
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
