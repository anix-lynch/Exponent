"""
Categorize Chief of Staff questions into interview categories
"""
import json
import os

# Chief of Staff Categories
CATEGORIES = [
    "Behavioral",
    "Leadership",
    "Strategic Planning",
    "Communication",
    "Cross-Functional Collaboration",
    "Problem Solving"
]

def categorize_question(question_text, url=""):
    """Categorize a Chief of Staff question based on keywords and patterns"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral Questions (STAR format)
    if any(phrase in q_lower for phrase in [
        'tell me about a time', 'describe a time', 'give an example',
        'walk me through a time', 'have you ever'
    ]):
        categories.append("Behavioral")
    
    # Leadership
    if any(keyword in q_lower for keyword in [
        'lead', 'leadership', 'manage', 'team', 'influence',
        'motivate', 'inspire', 'mentor', 'coach'
    ]):
        categories.append("Leadership")
    
    # Communication
    if any(keyword in q_lower for keyword in [
        'feedback', 'communicate', 'present', 'stakeholder',
        'explain', 'persuade', 'negotiate'
    ]):
        categories.append("Communication")
    
    # Cross-Functional Collaboration
    if any(keyword in q_lower for keyword in [
        'cross-functional', 'collaborate', 'partnership',
        'work with others', 'helped someone'
    ]):
        categories.append("Cross-Functional Collaboration")
    
    # Strategic Planning
    if any(keyword in q_lower for keyword in [
        'strategy', 'strategic', 'plan', 'roadmap',
        'vision', 'long-term', 'prioritize'
    ]):
        categories.append("Strategic Planning")
    
    # Problem Solving
    if any(keyword in q_lower for keyword in [
        'problem', 'challenge', 'difficult', 'conflict',
        'resolve', 'solution'
    ]):
        categories.append("Problem Solving")
    
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
    
    print(f"📊 Categorizing {len(questions)} Chief of Staff questions...")
    
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
