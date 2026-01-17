"""
Categorize PM questions into interview categories
"""
import json
import re

# PM Categories
CATEGORIES = [
    "Product Design",
    "Product Strategy",
    "Analytical",
    "Behavioral",
    "Technical",
    "Estimation",
    "Metrics",
    "Execution",
    "Leadership",
    "Communication",
    "System Design",
    "Prioritization",
    "User Research",
    "Go-to-Market",
    "Roadmapping",
    "Stakeholder Management",
    "Trade-offs",
    "Root Cause Analysis",
    "A/B Testing",
    "Pricing",
    "Growth",
    "Product Sense",
    "Case Study",
    "Concept"
]

def categorize_question(question_text, url=""):
    """Categorize a PM question based on keywords and patterns"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral Questions
    if any(phrase in q_lower for phrase in ['tell me about a time', 'describe a time', 'have you ever', 'walk me through', 'made a mistake', 'faced challenges', 'conflict', 'disagreement', 'failure', 'difficult decision']):
        categories.append("Behavioral")
    
    # Product Design
    if any(keyword in q_lower for keyword in ['design a', 'design an', 'improve', 'feature', 'user experience', 'ux', 'interface', 'app for', 'product for', 'how would you design']):
        categories.append("Product Design")
    
    # Product Strategy
    if any(keyword in q_lower for keyword in ['should we', 'should introduce', 'launch', 'expansion', 'new market', 'enter', 'competitor', 'market share', 'strategic', 'vision', 'direction']):
        categories.append("Product Strategy")
    
    # Analytical / Root Cause Analysis
    if any(keyword in q_lower for keyword in ['why', 'investigate', 'diagnose', 'drop in', 'decline', 'decreased', 'increased', 'what caused', 'analyze', 'data shows']):
        if 'why' in q_lower and any(word in q_lower for word in ['drop', 'decline', 'decrease', 'increase', 'change']):
            categories.append("Root Cause Analysis")
        categories.append("Analytical")
    
    # Metrics
    if any(keyword in q_lower for keyword in ['metric', 'kpi', 'measure success', 'track', 'north star', 'key performance', 'success metric']):
        categories.append("Metrics")
    
    # Estimation
    if any(keyword in q_lower for keyword in ['estimate', 'market size', 'tam', 'how many', 'size the', 'revenue opportunity']):
        categories.append("Estimation")
    
    # A/B Testing
    if any(keyword in q_lower for keyword in ['a/b test', 'experiment', 'test the', 'hypothesis', 'control group', 'variant']):
        categories.append("A/B Testing")
    
    # Prioritization
    if any(keyword in q_lower for keyword in ['prioritize', 'priority', 'rank', 'choose between', 'which feature', 'limited resources', 'roadmap']):
        categories.append("Prioritization")
    
    # Execution
    if any(keyword in q_lower for keyword in ['execute', 'implement', 'deliver', 'ship', 'launch plan', 'go-to-market', 'rollout']):
        categories.append("Execution")
    
    # Go-to-Market
    if any(keyword in q_lower for keyword in ['go-to-market', 'gtm', 'launch strategy', 'market entry', 'positioning', 'messaging']):
        categories.append("Go-to-Market")
    
    # Pricing
    if any(keyword in q_lower for keyword in ['pricing', 'price', 'monetize', 'monetization', 'subscription', 'freemium']):
        categories.append("Pricing")
    
    # Growth
    if any(keyword in q_lower for keyword in ['growth', 'grow', 'acquisition', 'retention', 'engagement', 'viral', 'user growth']):
        categories.append("Growth")
    
    # User Research
    if any(keyword in q_lower for keyword in ['user research', 'customer feedback', 'user interview', 'survey', 'user needs', 'customer pain']):
        categories.append("User Research")
    
    # Stakeholder Management
    if any(keyword in q_lower for keyword in ['stakeholder', 'convince', 'persuade', 'alignment', 'buy-in', 'executive']):
        categories.append("Stakeholder Management")
    
    # Leadership
    if any(keyword in q_lower for keyword in ['lead', 'leadership', 'team', 'mentor', 'coach', 'influence', 'motivate']):
        if "Behavioral" not in categories:
            categories.append("Leadership")
    
    # Communication
    if any(keyword in q_lower for keyword in ['communicate', 'present', 'explain', 'convey', 'articulate']):
        categories.append("Communication")
    
    # Trade-offs
    if any(keyword in q_lower for keyword in ['trade-off', 'tradeoff', 'balance', 'compromise', 'pros and cons']):
        categories.append("Trade-offs")
    
    # Technical
    if any(keyword in q_lower for keyword in ['technical', 'api', 'database', 'architecture', 'scalability', 'performance', 'latency']):
        categories.append("Technical")
    
    # System Design
    if any(keyword in q_lower for keyword in ['design a system', 'architecture', 'scale', 'infrastructure', 'backend']):
        categories.append("System Design")
    
    # Roadmapping
    if any(keyword in q_lower for keyword in ['roadmap', 'planning', 'timeline', 'milestones', 'phases']):
        categories.append("Roadmapping")
    
    # Product Sense
    if any(keyword in q_lower for keyword in ['favorite product', 'product you love', 'critique', 'improve a product']):
        categories.append("Product Sense")
    
    # Case Study
    if any(keyword in q_lower for keyword in ['case study', 'case interview', 'business case']):
        categories.append("Case Study")
    
    # Concept Questions
    if q_lower.startswith('what is') or q_lower.startswith('define') or 'difference between' in q_lower:
        categories.append("Concept")
    
    # Default to Analytical if no categories found
    if not categories:
        categories.append("Analytical")
    
    return list(set(categories))  # Remove duplicates

def main():
    """Load raw questions, categorize them, and save results"""
    import os
    
    # Load raw questions
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    raw_path = os.path.join(data_dir, 'questions_raw.json')
    
    with open(raw_path, 'r') as f:
        questions = json.load(f)
    
    print(f"📊 Categorizing {len(questions)} questions...")
    
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
            print(f"  {cat.ljust(30)} {count:>3}")
    
    print(f"\n📊 Total questions: {len(categorized)}")

if __name__ == "__main__":
    main()
