"""
Categorize Product Marketing Manager questions into interview categories
"""
import json
import os

# Product Marketing Manager Categories
CATEGORIES = [
    "Behavioral",
    "Go-To-Market Strategy",
    "Product Positioning",
    "Product Launch",
    "Messaging & Communication",
    "Market Research",
    "Competitive Analysis",
    "Cross-Functional Collaboration",
    "Sales Enablement",
    "Customer Insights"
]

def categorize_question(question_text, url=""):
    """Categorize a Product Marketing Manager question based on keywords and patterns"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral Questions
    if any(phrase in q_lower for phrase in [
        'tell me about a time', 'describe a time', 'give an example',
        'walk me through a time', 'have you ever', 'tell me how you'
    ]):
        categories.append("Behavioral")
    
    # Go-To-Market Strategy
    if any(keyword in q_lower for keyword in [
        'gtm', 'go-to-market', 'market entry', 'launch strategy',
        'design a gtm', 'gtm strategy', 'taking', 'brick-and-mortar'
    ]):
        categories.append("Go-To-Market Strategy")
    
    # Product Positioning
    if any(keyword in q_lower for keyword in [
        'positioning', 'position', 'differentiate', 'value proposition',
        'positioning was effective'
    ]):
        categories.append("Product Positioning")
    
    # Product Launch
    if any(keyword in q_lower for keyword in [
        'launch', 'brought a product to market', 'new feature launch',
        'product release', 'launch plan', 'waitlist appointment feature'
    ]):
        categories.append("Product Launch")
    
    # Messaging & Communication
    if any(keyword in q_lower for keyword in [
        'messaging', 'message', 'communicate', 'storytelling',
        'narrative', 'pitch', 'presentation'
    ]):
        categories.append("Messaging & Communication")
    
    # Market Research
    if any(keyword in q_lower for keyword in [
        'market research', 'customer research', 'user research',
        'market analysis', 'market size', 'tam'
    ]):
        categories.append("Market Research")
    
    # Competitive Analysis
    if any(keyword in q_lower for keyword in [
        'competitive', 'competitor', 'competition', 'competitive landscape',
        'competitive analysis'
    ]):
        categories.append("Competitive Analysis")
    
    # Cross-Functional Collaboration
    if any(keyword in q_lower for keyword in [
        'team is not motivated', 'collaborate', 'cross-functional',
        'work with', 'partnership', 'stakeholder'
    ]):
        categories.append("Cross-Functional Collaboration")
    
    # Sales Enablement
    if any(keyword in q_lower for keyword in [
        'sales enablement', 'sales team', 'sales materials',
        'sales support', 'sales training'
    ]):
        categories.append("Sales Enablement")
    
    # Customer Insights
    if any(keyword in q_lower for keyword in [
        'customer insight', 'customer feedback', 'user feedback',
        'customer pain', 'customer need'
    ]):
        categories.append("Customer Insights")
    
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
    
    print(f"📊 Categorizing {len(questions)} Product Marketing Manager questions...")
    
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
