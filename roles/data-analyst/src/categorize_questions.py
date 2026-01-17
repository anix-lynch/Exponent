"""
Categorize questions into the 24 Data Analyst interview categories
"""
import json
import re

# 24 Categories for Data Analyst questions
CATEGORIES = [
    "Data Analysis",
    "SQL",
    "Coding",
    "Behavioral",
    "Technical",
    "Statistics & Experimentation",
    "Concept",
    "Analytical",
    "Data Structures & Algorithms",
    "Project Management",
    "Program Sense",
    "Execution",
    "System Design",
    "Product Design",
    "Estimation",
    "Product Strategy",
    "Artificial Intelligence",
    "Machine Learning",
    "People Management",
    "Cross-Functional",
    "Customer Interaction",
    "App Critique",
    "Data Pipeline Design",
    "Data Modeling"
]

def categorize_question(question_text, url=""):
    """Categorize a question based on keywords and patterns"""
    q_lower = question_text.lower()
    categories = []
    
    # SQL Questions
    if any(keyword in q_lower for keyword in ['sql', 'query', 'select', 'join', 'database', 'table', 'between', 'having']):
        categories.append("SQL")
    
    # Check URL for SQL coding problems
    if any(term in url.lower() for term in ['earnings', 'salaries', 'employees', 'transactions', 'hierarchy', 'lyft', 'instagram', 'duolingo', 'fraudulent', 'revenue', 'marketing-channel', 'ltv', 'campaign', 'product-lines', 'overstretched']):
        if "SQL" not in categories:
            categories.append("SQL")
        categories.append("Coding")
    
    # Behavioral Questions
    if any(phrase in q_lower for phrase in ['tell me about a time', 'describe a time', 'have you ever', 'walk me through a time', 'past projects', 'made a mistake', 'built a dashboard', 'faced challenges']):
        categories.append("Behavioral")
    
    # Data Analysis
    if any(keyword in q_lower for keyword in ['analyze', 'analysis', 'investigate', 'drop in', 'decline', 'metric', 'kpi', 'measure', 'data project', 'dataset', 'insights', 'trend']):
        categories.append("Data Analysis")
    
    # Analytical (Root cause, diagnosis, investigation)
    if any(keyword in q_lower for keyword in ['why', 'how would you investigate', 'diagnose', 'identify', 'determine', 'assess', 'evaluate', 'what caused']):
        if "Analytical" not in categories:
            categories.append("Analytical")
    
    # Product Strategy
    if any(keyword in q_lower for keyword in ['should introduce', 'should we', 'launch', 'expansion', 'new market', 'new region', 'new city', 'competitor', 'market share', 'pricing']):
        categories.append("Product Strategy")
    
    # Estimation
    if any(keyword in q_lower for keyword in ['estimate', 'market size', 'tam', 'total addressable market', 'how many', 'size the opportunity']):
        categories.append("Estimation")
    
    # Product Design
    if any(keyword in q_lower for keyword in ['north star metric', 'product', 'feature', 'user engagement', 'adoption', 'retention']):
        if "Product Strategy" not in categories:
            categories.append("Product Design")
    
    # Statistics & Experimentation
    if any(keyword in q_lower for keyword in ['a/b test', 'experiment', 'test the impact', 'test the viability', 'beta launch', 'cohort', 'statistical']):
        categories.append("Statistics & Experimentation")
    
    # System Design
    if any(keyword in q_lower for keyword in ['design', 'architecture', 'pipeline', 'data flow', 'etl', 'system']):
        categories.append("System Design")
    
    # Data Modeling
    if any(keyword in q_lower for keyword in ['model', 'schema', 'data structure', 'nosql', 'connect databases']):
        categories.append("Data Modeling")
    
    # Technical
    if any(keyword in q_lower for keyword in ['technical', 'code', 'algorithm', 'complexity', 'optimize']):
        categories.append("Technical")
    
    # Coding (algorithms, data structures)
    if any(keyword in q_lower or term in url.lower() for keyword in ['merge intervals', 'fibonacci', 'algorithm', 'biased coin'] for term in ['merge-intervals', 'fibonacci', 'biased-coin']):
        categories.append("Coding")
        categories.append("Data Structures & Algorithms")
    
    # Cross-Functional
    if any(keyword in q_lower for keyword in ['stakeholder', 'non-technical', 'business user', 'leadership', 'communicate', 'present insights', 'convey']):
        categories.append("Cross-Functional")
    
    # Execution
    if any(keyword in q_lower for keyword in ['prioritize', 'limited resources', 'decision', 'actionable', 'turn analysis into action']):
        categories.append("Execution")
    
    # Project Management
    if any(keyword in q_lower for keyword in ['project', 'workflow', 'process', 'inefficiencies', 'team']):
        if "Behavioral" not in categories:
            categories.append("Project Management")
    
    # Customer Interaction
    if any(keyword in q_lower for keyword in ['customer', 'user segment', 'high-value customers']):
        categories.append("Customer Interaction")
    
    # Concept Questions (Why questions about fundamentals)
    if q_lower.startswith('why do you want') or q_lower.startswith('what is') or 'difference between' in q_lower:
        categories.append("Concept")
    
    # Data Pipeline Design
    if any(keyword in q_lower for keyword in ['pipeline', 'data flow', 'etl', 'data sources', 'inconsistent ids', 'joining data']):
        categories.append("Data Pipeline Design")
    
    # AI/ML
    if any(keyword in q_lower for keyword in ['ai', 'artificial intelligence', 'machine learning', 'ml', 'recommendation engine', 'anomaly', 'detect']):
        categories.append("Artificial Intelligence")
        if 'machine learning' in q_lower or 'ml' in q_lower:
            categories.append("Machine Learning")
    
    # Visualization
    if any(keyword in q_lower for keyword in ['visualize', 'visualization', 'dashboard', 'chart']):
        if "Data Analysis" not in categories:
            categories.append("Data Analysis")
    
    # If no categories found, mark as Analytical (most questions are analytical in nature)
    if not categories:
        categories.append("Analytical")
    
    return categories

def main():
    import os
    # Load questions
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    input_file = os.path.join(data_dir, 'questions_raw.json')
    
    with open(input_file, 'r') as f:
        questions = json.load(f)
    
    # Filter out junk questions
    filtered_questions = []
    for q in questions:
        text = q['question']
        # Skip non-questions
        if len(text) < 15 or text in ['+ Share interview', 'Share interview', 'I was asked this', '+ Share interview experience']:
            continue
        filtered_questions.append(q)
    
    print(f"📊 Categorizing {len(filtered_questions)} questions...")
    
    # Categorize each question
    categorized = []
    for q in filtered_questions:
        cats = categorize_question(q['question'], q['url'])
        categorized.append({
            'question': q['question'],
            'categories': cats,
            'url': q['url']
        })
    
    # Save categorized questions
    output_file1 = os.path.join(data_dir, 'questions_categorized.json')
    with open(output_file1, 'w') as f:
        json.dump(categorized, f, indent=2)
    
    print(f"✅ Saved to {output_file1}")
    
    # Organize by category
    by_category = {cat: [] for cat in CATEGORIES}
    
    for q in categorized:
        for cat in q['categories']:
            by_category[cat].append({
                'question': q['question'],
                'url': q['url']
            })
    
    # Save by category
    output_file2 = os.path.join(data_dir, 'questions_by_category.json')
    with open(output_file2, 'w') as f:
        json.dump(by_category, f, indent=2)
    
    print(f"✅ Saved to {output_file2}")
    
    # Print summary
    print(f"\n{'='*70}")
    print("📋 Questions per category:")
    print(f"{'='*70}")
    for cat in CATEGORIES:
        count = len(by_category[cat])
        if count > 0:
            print(f"  {cat:.<45} {count:>3}")
    
    print(f"\n📊 Total questions: {len(filtered_questions)}")

if __name__ == "__main__":
    main()
