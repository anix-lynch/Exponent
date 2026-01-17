"""
Categorize Growth Marketing Manager questions into interview categories
"""
import json
import os

# Growth Marketing Manager Categories
CATEGORIES = [
    "Behavioral",
    "Growth Strategy",
    "Customer Acquisition",
    "Retention & Engagement",
    "Analytics & Metrics",
    "A/B Testing & Experimentation",
    "Channel Strategy",
    "Product-Led Growth"
]

def categorize_question(question_text, url=""):
    """Categorize a Growth Marketing Manager question based on keywords and patterns"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral Questions
    if any(phrase in q_lower for phrase in [
        'tell me about a time', 'describe a time', 'give an example',
        'walk me through a time', 'have you ever', 'encountered obstacles',
        'used customer feedback'
    ]):
        categories.append("Behavioral")
    
    # Growth Strategy
    if any(keyword in q_lower for keyword in [
        'growth strategy', 'scale', 'growth plan', 'user growth',
        'acquisition strategy', 'growth opportunity'
    ]):
        categories.append("Growth Strategy")
    
    # Customer Acquisition
    if any(keyword in q_lower for keyword in [
        'acquire', 'acquisition', 'new users', 'user acquisition',
        'customer acquisition', 'cac', 'cost per acquisition'
    ]):
        categories.append("Customer Acquisition")
    
    # Retention & Engagement
    if any(keyword in q_lower for keyword in [
        'retention', 'churn', 'engagement', 'activate', 'activation',
        'keep users', 'user retention'
    ]):
        categories.append("Retention & Engagement")
    
    # Analytics & Metrics
    if any(keyword in q_lower for keyword in [
        'metric', 'kpi', 'measure', 'track', 'analytics',
        'data', 'funnel', 'conversion'
    ]):
        categories.append("Analytics & Metrics")
    
    # A/B Testing & Experimentation
    if any(keyword in q_lower for keyword in [
        'a/b test', 'experiment', 'test', 'hypothesis',
        'experimentation', 'variant'
    ]):
        categories.append("A/B Testing & Experimentation")
    
    # Channel Strategy
    if any(keyword in q_lower for keyword in [
        'channel', 'marketing channel', 'paid', 'organic',
        'seo', 'sem', 'social media', 'email', 'content marketing'
    ]):
        categories.append("Channel Strategy")
    
    # Product-Led Growth
    if any(keyword in q_lower for keyword in [
        'product-led', 'plg', 'product growth', 'viral',
        'referral', 'freemium'
    ]):
        categories.append("Product-Led Growth")
    
    # Default to Behavioral if no categories found
    if not categories:
        categories.append("Behavioral")
    
    return list(set(categories))

def main():
    """Load raw questions, categorize them, and save results"""
    
    # Load raw questions
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    raw_path = os.path.join(data_dir, 'questions_raw.json')
    
    with open(raw_path, 'r') as f:
        questions = json.load(f)
    
    print(f"📊 Categorizing {len(questions)} Growth Marketing Manager questions...")
    
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
