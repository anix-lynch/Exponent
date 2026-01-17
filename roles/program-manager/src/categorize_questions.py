"""
Categorize Program Manager questions
"""
import json
import os

CATEGORIES = [
    "Behavioral",
    "Program Management",
    "Data Analysis",
    "Stakeholder Management",
    "Project Planning",
    "Risk Management"
]

def categorize_question(question_text):
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral (highest priority)
    behavioral_phrases = [
        'tell me about a time', 'describe a time', 'have you ever',
        'why do you want to work at', 'what experience do you have',
        'how do you prioritize', 'faced significant', 'led a project',
        'felt inspired', 'suggestion that', 'discovered an opportunity'
    ]
    if any(phrase in q_lower for phrase in behavioral_phrases):
        categories.append("Behavioral")
    
    # Data Analysis
    if 'data' in q_lower:
        categories.append("Data Analysis")
    
    # Stakeholder Management
    if any(kw in q_lower for kw in ['stakeholder', 'team', 'global teams']):
        categories.append("Stakeholder Management")
    
    # Program Management
    if any(kw in q_lower for kw in ['program', 'project', 'prioritize', 'manage']):
        categories.append("Program Management")
    
    # Default
    if not categories:
        categories.append("Behavioral")
    
    return list(set(categories))

def main():
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    raw_path = os.path.join(data_dir, 'questions_raw.json')
    
    with open(raw_path, 'r') as f:
        questions = json.load(f)
    
    print(f"📊 Categorizing {len(questions)} Program Manager questions...")
    
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
