"""
Categorize Business Analyst questions into interview categories
COMPREHENSIVE NESTED CATEGORIZATION for top-tier role
"""
import json
import os

# Business Analyst Categories (with nested subcategories)
CATEGORIES = [
    "Behavioral",
    "Data Analysis - Business Problem Solving",
    "Data Analysis - Root Cause Analysis",
    "Data Analysis - Trend Analysis",
    "Data Analysis - Cohort Analysis",
    "SQL - Joins & Aggregation",
    "SQL - Window Functions",
    "SQL - Query Optimization",
    "Business Metrics & KPIs",
    "Estimation & Market Sizing",
    "Requirements Gathering",
    "Stakeholder Management",
    "Process Improvement",
    "Financial Analysis",
    "Product Strategy",
    "Communication & Presentation",
    "Prioritization",
    "Data Visualization"
]

def categorize_question(question_text, url=""):
    """Categorize a Business Analyst question with nested subcategories"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral
    if any(phrase in q_lower for phrase in [
        'tell me about a time', 'describe a time', 'walk me through a time',
        'have you ever', 'give an example'
    ]):
        categories.append("Behavioral")
    
    # Data Analysis - Business Problem Solving
    if any(keyword in q_lower for keyword in [
        'business problem', 'solve', 'identified', 'data to solve',
        'business challenge', 'opportunity'
    ]):
        categories.append("Data Analysis - Business Problem Solving")
    
    # Data Analysis - Root Cause Analysis
    if any(keyword in q_lower for keyword in [
        'drop', 'decline', 'decrease', 'sudden', 'investigate', 'why',
        'root cause', 'diagnose'
    ]):
        categories.append("Data Analysis - Root Cause Analysis")
    
    # Data Analysis - Trend Analysis
    if any(keyword in q_lower for keyword in [
        'trend', 'pattern', 'over time', 'historical', 'forecast'
    ]):
        categories.append("Data Analysis - Trend Analysis")
    
    # Data Analysis - Cohort Analysis
    if any(keyword in q_lower for keyword in [
        'cohort', 'cohort analysis', 'user segments', 'segment'
    ]):
        categories.append("Data Analysis - Cohort Analysis")
    
    # SQL - Joins & Aggregation
    if any(keyword in q_lower for keyword in [
        'sql', 'query', 'join', 'group by', 'aggregate', 'sum', 'count',
        'average', 'top 10', 'top customers'
    ]):
        categories.append("SQL - Joins & Aggregation")
    
    # SQL - Window Functions
    if any(keyword in q_lower for keyword in [
        'window function', 'rank', 'row_number', 'lag', 'lead',
        'running total', 'moving average'
    ]):
        categories.append("SQL - Window Functions")
    
    # SQL - Query Optimization
    if any(keyword in q_lower for keyword in [
        'optimize', 'performance', 'slow query', 'index', 'query performance'
    ]):
        categories.append("SQL - Query Optimization")
    
    # Business Metrics & KPIs
    if any(keyword in q_lower for keyword in [
        'kpi', 'metric', 'measure success', 'track', 'business metrics',
        'key performance', 'measure', 'success of'
    ]):
        categories.append("Business Metrics & KPIs")
    
    # Estimation & Market Sizing
    if any(keyword in q_lower for keyword in [
        'estimate', 'market size', 'market sizing', 'how many', 'calculate'
    ]):
        categories.append("Estimation & Market Sizing")
    
    # Requirements Gathering
    if any(keyword in q_lower for keyword in [
        'requirements', 'requirement gathering', 'documenting', 'elicit',
        'stakeholder needs', 'business requirements'
    ]):
        categories.append("Requirements Gathering")
    
    # Stakeholder Management
    if any(keyword in q_lower for keyword in [
        'stakeholder', 'present', 'presentation', 'senior leadership',
        'executive', 'communicate with'
    ]):
        categories.append("Stakeholder Management")
    
    # Process Improvement
    if any(keyword in q_lower for keyword in [
        'process', 'improve', 'efficiency', 'streamline', 'optimize process'
    ]):
        categories.append("Process Improvement")
    
    # Financial Analysis
    if any(keyword in q_lower for keyword in [
        'revenue', 'cost', 'profit', 'margin', 'financial', 'roi',
        'return on investment'
    ]):
        categories.append("Financial Analysis")
    
    # Product Strategy
    if any(keyword in q_lower for keyword in [
        'product launch', 'product strategy', 'feature', 'roadmap'
    ]):
        categories.append("Product Strategy")
    
    # Communication & Presentation
    if any(keyword in q_lower for keyword in [
        'present', 'communicate', 'explain', 'insights', 'findings'
    ]):
        categories.append("Communication & Presentation")
    
    # Prioritization
    if any(keyword in q_lower for keyword in [
        'prioritize', 'priority', 'competing', 'limited resources',
        'trade-off'
    ]):
        categories.append("Prioritization")
    
    # Data Visualization
    if any(keyword in q_lower for keyword in [
        'dashboard', 'visualization', 'chart', 'graph', 'visualize'
    ]):
        categories.append("Data Visualization")
    
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
    
    print(f"📊 Categorizing {len(questions)} Business Analyst questions...")
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
