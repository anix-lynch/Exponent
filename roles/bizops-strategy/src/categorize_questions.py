"""
Categorize BizOps & Strategy questions
"""
import json
import os

CATEGORIES = [
    "Strategy",
    "Business Analysis",
    "Operations",
    "Behavioral",
    "Data Analysis",
    "Product Strategy",
    "Market Analysis",
    "Financial Analysis",
    "Process Improvement",
    "Stakeholder Management",
    "Problem Solving",
    "Case Study",
    "Analytical",
    "System Design",
    "SQL"
]

def categorize_question(question_text):
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral (highest priority)
    behavioral_phrases = [
        'tell me about a time', 'describe a time', 'have you ever', 'walk me through',
        'tell me about yourself', 'why do you want to work at', 'greatest success',
        'made a mistake', 'disagreed', 'conflict', 'gained trust', 'break a complex problem'
    ]
    if any(phrase in q_lower for phrase in behavioral_phrases):
        return ["Behavioral"]
    
    # Strategy
    if any(kw in q_lower for kw in ['strategy', 'strategic', 'market entry', 'competitive advantage', 'business model', 'go-to-market', 'expansion']):
        categories.append("Strategy")
    
    # Product Strategy
    if any(kw in q_lower for kw in ['product strategy', 'product roadmap', 'product launch', 'product market fit']):
        categories.append("Product Strategy")
    
    # Market Analysis
    if any(kw in q_lower for kw in ['market', 'competition', 'competitive', 'industry', 'emerging markets', 'market size', 'tam']):
        categories.append("Market Analysis")
    
    # Business Analysis
    if any(kw in q_lower for kw in ['business', 'revenue', 'profit', 'growth', 'metrics', 'kpi', 'roi', 'business case']):
        categories.append("Business Analysis")
    
    # Financial Analysis
    if any(kw in q_lower for kw in ['financial', 'finance', 'budget', 'cost', 'pricing', 'valuation', 'investment']):
        categories.append("Financial Analysis")
    
    # Operations
    if any(kw in q_lower for kw in ['operations', 'operational', 'efficiency', 'process', 'workflow', 'supply chain', 'logistics']):
        categories.append("Operations")
    
    # Process Improvement
    if any(kw in q_lower for kw in ['improve', 'optimization', 'optimize', 'reduce', 'increase', 'attrition', 'retention']):
        categories.append("Process Improvement")
    
    # Data Analysis
    if any(kw in q_lower for kw in ['data', 'analyze', 'analysis', 'metric', 'dashboard', 'report', 'insight']):
        categories.append("Data Analysis")
    
    # Analytical (root cause, investigation)
    if any(kw in q_lower for kw in ['why', 'investigate', 'root cause', 'diagnose', 'decline', 'drop', 'increase']):
        categories.append("Analytical")
    
    # Case Study
    if any(kw in q_lower for kw in ['case study', 'scenario', 'situation', 'problem', 'challenge']):
        categories.append("Case Study")
    
    # Problem Solving
    if any(kw in q_lower for kw in ['solve', 'solution', 'approach', 'how would you', 'what would you do']):
        if not categories:
            categories.append("Problem Solving")
    
    # Stakeholder Management
    if any(kw in q_lower for kw in ['stakeholder', 'cross-functional', 'partner', 'alignment', 'communication']):
        categories.append("Stakeholder Management")
    
    # System Design
    if 'design' in q_lower and any(kw in q_lower for kw in ['system', 'application', 'platform', 'architecture']):
        categories.append("System Design")
    
    # SQL
    if any(kw in q_lower for kw in ['sql', 'query', 'database']):
        categories.append("SQL")
    
    # Default
    if not categories:
        categories.append("Strategy")
    
    return list(set(categories))

def main():
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    raw_path = os.path.join(data_dir, 'questions_raw.json')
    
    with open(raw_path, 'r') as f:
        questions = json.load(f)
    
    print(f"📊 Categorizing {len(questions)} BizOps & Strategy questions...")
    
    categorized = []
    by_category = {cat: [] for cat in CATEGORIES}
    
    for q in questions:
        cats = categorize_question(q['question'])
        q['categories'] = cats
        categorized.append(q)
        
        for cat in cats:
            if cat in by_category:
                by_category[cat].append({
                    'question': q['question'],
                    'url': q.get('url', '')
                })
    
    # Save
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
            print(f"  {cat.ljust(40)} {count:>3}")
    
    print(f"\n📊 Total questions: {len(categorized)}")

if __name__ == "__main__":
    main()
