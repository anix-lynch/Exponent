"""
Categorize Finance & Strategy questions into interview categories
"""
import json
import os

# Finance & Strategy Categories
CATEGORIES = [
    "Behavioral",
    "Financial Analysis",
    "Financial Modeling",
    "Product Strategy",
    "Strategic Planning",
    "Cost Management",
    "Business Metrics"
]

def categorize_question(question_text, url=""):
    """Categorize a Finance & Strategy question based on keywords and patterns"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral Questions
    if any(phrase in q_lower for phrase in [
        'tell me about a time', 'describe a time', 'walk me through a time',
        'have you ever', 'give an example'
    ]):
        categories.append("Behavioral")
    
    # Financial Analysis
    if any(keyword in q_lower for keyword in [
        'financial results', 'financial analysis', 'analyze', 'evaluate',
        'financially successful', 'financial performance', 'roi', 'return on investment'
    ]):
        categories.append("Financial Analysis")
    
    # Financial Modeling
    if any(keyword in q_lower for keyword in [
        'financial model', 'build a model', 'forecast', 'projection',
        'subscription business', 'revenue model', 'unit economics'
    ]):
        categories.append("Financial Modeling")
    
    # Product Strategy
    if any(keyword in q_lower for keyword in [
        'product launch', 'new product', 'product strategy', 'product decision'
    ]):
        categories.append("Product Strategy")
    
    # Strategic Planning
    if any(keyword in q_lower for keyword in [
        'strategic plan', 'strategic initiatives', 'strategy', 'prioritize',
        'business unit', 'long-term', '3-year', 'roadmap'
    ]):
        categories.append("Strategic Planning")
    
    # Cost Management
    if any(keyword in q_lower for keyword in [
        'cost-saving', 'cost reduction', 'efficiency', 'optimize costs',
        'budget', 'expense'
    ]):
        categories.append("Cost Management")
    
    # Business Metrics
    if any(keyword in q_lower for keyword in [
        'metrics', 'kpi', 'measure', 'track performance'
    ]):
        categories.append("Business Metrics")
    
    # Default to Strategic Planning if no categories found
    if not categories:
        categories.append("Strategic Planning")
    
    return list(set(categories))

def main():
    """Load raw questions, categorize them, and save results"""
    
    # Load raw questions
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    raw_path = os.path.join(data_dir, 'questions_raw.json')
    
    with open(raw_path, 'r') as f:
        questions = json.load(f)
    
    print(f"📊 Categorizing {len(questions)} Finance & Strategy questions...")
    
    # Categorize each question
    categorized = []
    by_category = {cat: [] for cat in CATEGORIES}
    
    for q in questions:
        q_text = q['question']
        q_url = q.get('url', '')
        
        # Get categories
        cats = categorize_question(q_text, q_url)
        
        # Update question
        q['categories'] = cats
        categorized.append(q)
        
        # Add to by_category
        for cat in cats:
            if cat in by_category:
                by_category[cat].append({
                    'question': q_text,
                    'url': q_url
                })
    
    # Save categorized questions
    categorized_path = os.path.join(data_dir, 'questions_categorized.json')
    with open(categorized_path, 'w') as f:
        json.dump(categorized, f, indent=2)
    print(f"✅ Saved to {categorized_path}")
    
    # Save by category
    by_category_path = os.path.join(data_dir, 'questions_by_category.json')
    with open(by_category_path, 'w') as f:
        json.dump(by_category, f, indent=2)
    print(f"✅ Saved to {by_category_path}")
    
    # Print summary
    print("\n" + "="*70)
    print("📋 Questions per category:")
    print("="*70)
    
    # Sort by count
    category_counts = [(cat, len(by_category[cat])) for cat in CATEGORIES]
    category_counts.sort(key=lambda x: x[1], reverse=True)
    
    for cat, count in category_counts:
        if count > 0:
            print(f"  {cat.ljust(35)} {count:>3}")
    
    print(f"\n📊 Total questions: {len(categorized)}")

if __name__ == "__main__":
    main()
