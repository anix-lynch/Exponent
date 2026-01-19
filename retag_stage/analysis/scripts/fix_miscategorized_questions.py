#!/usr/bin/env python3
"""
Fix miscategorized questions across all roles.
Many questions are in wrong categories (e.g., coding in "Data Pipeline Design").
"""

import json
from pathlib import Path
from typing import Dict, List

# Define proper categorization rules
CODING_KEYWORDS = [
    'linked list', 'binary tree', 'array', 'algorithm', 'leetcode',
    'reverse a', 'merge k', 'find the two sum', 'valid parentheses',
    'squares of sorted', 'triplet', 'subarray', 'palindrome',
    'climbing stairs', 'house robber', 'container with', 'n-queens',
    'serialize', 'deserialize', 'lowest common ancestor', 'maximum path sum',
    'candy', 'rotate', 'spiral', 'game of life', 'regex parser'
]

SQL_KEYWORDS = [
    'write a query', 'sql', 'select', 'join', 'group by',
    'write sql', 'query to find', 'consecutive days', 'attendance',
    'fibonacci series', 'stored procedures'
]

BEHAVIORAL_KEYWORDS = [
    'tell me about', 'why do you', 'describe a time', 'how do you',
    'what would you do if', 'share your experience', 'what types of',
    'can you provide an example', 'why did you become'
]

PRODUCT_ANALYTICS_KEYWORDS = [
    'conversion rate', 'missing item', 'wrong item', 'user engagement',
    'how would you measure', 'what metrics', 'a/b test'
]

PIPELINE_KEYWORDS = [
    'design a pipeline', 'design an etl', 'etl pipeline', 'data pipeline',
    'nightly job', 'scheduling dependencies', 'clickstream', 'ingest',
    'batch processing', 'streaming', 'kafka', 'airflow'
]

def categorize_question(question: str) -> str:
    """Properly categorize a question based on its content."""
    q_lower = question.lower()
    
    # Check in priority order
    if any(kw in q_lower for kw in BEHAVIORAL_KEYWORDS):
        return 'Behavioral'
    
    if any(kw in q_lower for kw in CODING_KEYWORDS):
        return 'Coding'
    
    if any(kw in q_lower for kw in SQL_KEYWORDS):
        return 'SQL'
    
    if any(kw in q_lower for kw in PRODUCT_ANALYTICS_KEYWORDS):
        return 'Product Analytics'
    
    if any(kw in q_lower for kw in PIPELINE_KEYWORDS):
        return 'Data Pipeline Design'
    
    # Default: keep original category
    return None

def fix_role_questions(role_dir: Path):
    """Fix categorization for a single role."""
    categorized_file = role_dir / 'data' / 'questions_categorized.json'
    by_category_file = role_dir / 'data' / 'questions_by_category.json'
    
    if not categorized_file.exists():
        return
    
    print(f"\n🔧 Fixing: {role_dir.name}")
    
    # Load categorized questions
    with open(categorized_file) as f:
        questions = json.load(f)
    
    # Recategorize
    changes = 0
    for q in questions:
        question_text = q.get('question', '')
        current_category = q.get('categories', ['Uncategorized'])[0]
        
        new_category = categorize_question(question_text)
        
        if new_category and new_category != current_category:
            print(f"   ✓ '{question_text[:60]}...'")
            print(f"     {current_category} → {new_category}")
            q['categories'] = [new_category]
            changes += 1
    
    if changes > 0:
        # Save updated categorized file
        with open(categorized_file, 'w') as f:
            json.dump(questions, f, indent=2)
        
        # Rebuild by_category file
        by_category = {}
        for q in questions:
            category = q.get('categories', ['Uncategorized'])[0]
            if category not in by_category:
                by_category[category] = []
            by_category[category].append({
                'question': q['question'],
                'url': q.get('url', '')
            })
        
        with open(by_category_file, 'w') as f:
            json.dump(by_category, f, indent=2)
        
        print(f"   ✅ Fixed {changes} questions")
    else:
        print(f"   ✓ No changes needed")

def main():
    print("🎯 Fixing Miscategorized Questions Across All Roles")
    print("=" * 80)
    
    roles_dir = Path(__file__).parent.parent.parent / 'roles'
    
    for role_dir in sorted(roles_dir.iterdir()):
        if role_dir.is_dir():
            fix_role_questions(role_dir)
    
    print("\n" + "=" * 80)
    print("✅ Done! Now regenerate the Yellow list with correct categories.")

if __name__ == "__main__":
    main()
