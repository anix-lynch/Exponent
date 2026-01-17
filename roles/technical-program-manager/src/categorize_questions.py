"""
Categorize TPM questions into interview categories
"""
import json
import os

# TPM Categories
CATEGORIES = [
    "Program Management",
    "Cross-Functional Leadership",
    "Technical Strategy",
    "System Design",
    "Behavioral",
    "Stakeholder Management",
    "Risk Management",
    "Project Execution",
    "Roadmapping",
    "Resource Planning",
    "Technical Communication",
    "Metrics & KPIs",
    "Problem Solving",
    "Conflict Resolution",
    "Process Improvement",
    "Agile/Scrum",
    "Architecture",
    "Prioritization",
    "Team Leadership"
]

def categorize_question(question_text, url=""):
    """Categorize a TPM question based on keywords and patterns"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral Questions
    if any(phrase in q_lower for phrase in ['tell me about a time', 'describe a time', 'have you ever', 'walk me through', 'past projects', 'made a mistake', 'faced challenges', 'conflict', 'disagreement', 'failure', 'difficult decision']):
        categories.append("Behavioral")
    
    # Program Management
    if any(keyword in q_lower for keyword in ['program', 'initiate', 'launch', 'deliver', 'multiple projects', 'portfolio', 'program manager', 'end-to-end']):
        categories.append("Program Management")
    
    # Cross-Functional Leadership
    if any(keyword in q_lower for keyword in ['cross-functional', 'engineering team', 'work with', 'collaborate', 'coordinate', 'align teams', 'multiple teams']):
        categories.append("Cross-Functional Leadership")
    
    # Technical Strategy
    if any(keyword in q_lower for keyword in ['technical strategy', 'technology decision', 'technical direction', 'architecture decision', 'technical roadmap', 'tech stack']):
        categories.append("Technical Strategy")
    
    # System Design
    if any(keyword in q_lower for keyword in ['design', 'system design', 'architecture', 'design twitter', 'design facebook', 'build a system', 'scalability']):
        categories.append("System Design")
    
    # Stakeholder Management
    if any(keyword in q_lower for keyword in ['stakeholder', 'executive', 'leadership', 'communicate with', 'present to', 'buy-in', 'alignment']):
        categories.append("Stakeholder Management")
    
    # Risk Management
    if any(keyword in q_lower for keyword in ['risk', 'failure', 'mitigation', 'contingency', 'backup plan', 'what if']):
        categories.append("Risk Management")
    
    # Project Execution
    if any(keyword in q_lower for keyword in ['execute', 'deliver', 'implementation', 'rollout', 'deploy', 'launch', 'ship']):
        categories.append("Project Execution")
    
    # Roadmapping
    if any(keyword in q_lower for keyword in ['roadmap', 'planning', 'timeline', 'milestone', 'phases', 'quarters']):
        categories.append("Roadmapping")
    
    # Resource Planning
    if any(keyword in q_lower for keyword in ['resource', 'capacity', 'allocation', 'staffing', 'budget', 'cost']):
        categories.append("Resource Planning")
    
    # Technical Communication
    if any(keyword in q_lower for keyword in ['explain', 'communicate', 'technical concept', 'non-technical', 'present', 'articulate']):
        categories.append("Technical Communication")
    
    # Metrics & KPIs
    if any(keyword in q_lower for keyword in ['metric', 'kpi', 'measure', 'track', 'success criteria', 'performance indicator']):
        categories.append("Metrics & KPIs")
    
    # Prioritization
    if any(keyword in q_lower for keyword in ['prioritize', 'priority', 'rank', 'choose between', 'limited resources', 'trade-off']):
        categories.append("Prioritization")
    
    # Conflict Resolution
    if any(keyword in q_lower for keyword in ['conflict', 'disagreement', 'dispute', 'resolve', 'mediate', 'tension']):
        categories.append("Conflict Resolution")
    
    # Process Improvement
    if any(keyword in q_lower for keyword in ['process', 'improve', 'optimize', 'efficiency', 'streamline', 'workflow']):
        categories.append("Process Improvement")
    
    # Agile/Scrum
    if any(keyword in q_lower for keyword in ['agile', 'scrum', 'sprint', 'kanban', 'backlog', 'standup', 'retrospective']):
        categories.append("Agile/Scrum")
    
    # Architecture
    if any(keyword in q_lower for keyword in ['architecture', 'architectural', 'infrastructure', 'platform', 'framework']):
        if "System Design" not in categories:
            categories.append("Architecture")
    
    # Team Leadership
    if any(keyword in q_lower for keyword in ['lead', 'leadership', 'mentor', 'coach', 'team', 'manage', 'motivate']):
        if "Behavioral" not in categories and "Cross-Functional Leadership" not in categories:
            categories.append("Team Leadership")
    
    # Problem Solving
    if any(keyword in q_lower for keyword in ['problem', 'solve', 'challenge', 'issue', 'troubleshoot', 'blockers']):
        if not categories:
            categories.append("Problem Solving")
    
    # Default to Program Management if no categories found
    if not categories:
        categories.append("Program Management")
    
    return list(set(categories))

def main():
    """Load raw questions, categorize them, and save results"""
    
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
            print(f"  {cat.ljust(35)} {count:>3}")
    
    print(f"\n📊 Total questions: {len(categorized)}")

if __name__ == "__main__":
    main()
