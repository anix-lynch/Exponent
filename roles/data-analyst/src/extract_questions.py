"""
Extract Exponent Data Analyst Interview Questions
Goal: Extract questions with categories (no answers) to build mental models
"""

import json
from typing import List, Dict

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

def organize_by_category(questions: List[Dict]) -> Dict[str, List[str]]:
    """Organize questions by category"""
    organized = {cat: [] for cat in CATEGORIES}
    
    for q in questions:
        category = q.get('category', 'Uncategorized')
        question_text = q.get('question', '')
        if category in organized:
            organized[category].append(question_text)
    
    return organized

def save_questions(questions: List[Dict], filepath: str = '../data/questions.json'):
    """Save extracted questions to JSON"""
    with open(filepath, 'w') as f:
        json.dump(questions, f, indent=2)
    print(f"Saved {len(questions)} questions to {filepath}")

def load_questions(filepath: str = '../data/questions.json') -> List[Dict]:
    """Load questions from JSON"""
    with open(filepath, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    print("Categories to extract:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")
