#!/usr/bin/env python3
"""
Find TRUE overlapped questions - exact same questions across multiple roles
"""
import json
from pathlib import Path
from collections import defaultdict
import re

def normalize_question(question):
    """Normalize question text for comparison"""
    if isinstance(question, dict):
        q = question.get('question', '')
    else:
        q = str(question)
    
    # Remove extra whitespace, lowercase, remove punctuation
    q = re.sub(r'\s+', ' ', q.strip().lower())
    q = re.sub(r'[^\w\s]', '', q)
    return q

def load_role_questions(role_dir):
    """Load categorized questions for a role"""
    json_path = role_dir / 'data' / 'questions_by_category.json'
    if json_path.exists():
        with open(json_path) as f:
            return json.load(f)
    return {}

def main():
    """Find questions that appear in multiple roles"""
    
    print("🔍 Finding TRUE Overlapped Questions...")
    print("=" * 80)
    print()
    
    roles_dir = Path(__file__).parent.parent.parent / 'roles'
    
    role_names = {
        'data-analyst': 'Data Analyst',
        'data-scientist': 'Data Scientist',
        'data-engineer': 'Data Engineer',
        'ml-engineer': 'ML Engineer',
        'product-analyst': 'Product Analyst',
        'business-analyst': 'Business Analyst',
        'product-manager': 'Product Manager',
        'product-marketing-manager': 'Product Marketing Manager',
        'growth-marketing-manager': 'Growth Marketing Manager',
        'software-engineer': 'Software Engineer',
        'technical-program-manager': 'Technical Program Manager',
        'program-manager': 'Program Manager',
        'chief-of-staff': 'Chief of Staff',
        'bizops-strategy': 'BizOps Strategy',
        'finance-strategy': 'Finance & Strategy'
    }
    
    # Map: normalized_question -> {original_text, roles: [role_name], categories: {role: category}}
    question_map = defaultdict(lambda: {
        'original': '',
        'roles': set(),
        'categories': {},
        'count': 0
    })
    
    # Collect all questions
    for role_slug, role_name in role_names.items():
        role_dir = roles_dir / role_slug
        if not role_dir.exists():
            continue
        
        questions_by_cat = load_role_questions(role_dir)
        
        for category, questions in questions_by_cat.items():
            for q in questions:
                if isinstance(q, dict):
                    q_text = q.get('question', '')
                else:
                    q_text = str(q)
                
                if not q_text or len(q_text) < 10:
                    continue
                
                normalized = normalize_question(q_text)
                
                # Store original text (first occurrence)
                if not question_map[normalized]['original']:
                    question_map[normalized]['original'] = q_text
                
                question_map[normalized]['roles'].add(role_name)
                question_map[normalized]['categories'][role_name] = category
                question_map[normalized]['count'] = len(question_map[normalized]['roles'])
    
    # Filter to questions appearing in 3+ roles (TRUE overlap)
    overlapped_3plus = {
        q: data for q, data in question_map.items()
        if data['count'] >= 3
    }
    
    # Filter to questions appearing in 5+ roles (SUPER overlap)
    overlapped_5plus = {
        q: data for q, data in question_map.items()
        if data['count'] >= 5
    }
    
    # Sort by number of roles
    sorted_3plus = sorted(
        overlapped_3plus.items(),
        key=lambda x: (x[1]['count'], x[0]),
        reverse=True
    )
    
    sorted_5plus = sorted(
        overlapped_5plus.items(),
        key=lambda x: (x[1]['count'], x[0]),
        reverse=True
    )
    
    print(f"📊 Found {len(sorted_3plus)} questions appearing in 3+ roles")
    print(f"📊 Found {len(sorted_5plus)} questions appearing in 5+ roles")
    print()
    
    # Generate output
    output = []
    output.append("# 🎯 TRUE OVERLAPPED QUESTIONS")
    output.append("")
    output.append("**These are the EXACT SAME questions that appear across multiple roles.**")
    output.append("")
    output.append("This is what you actually wanted - questions with the highest probability")
    output.append("of appearing in ANY interview because they're literally asked across roles.")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 📊 Quick Summary")
    output.append("")
    output.append(f"- **Questions in 5+ roles:** {len(sorted_5plus)} (SUPER HIGH PRIORITY)")
    output.append(f"- **Questions in 3-4 roles:** {len(sorted_3plus) - len(sorted_5plus)} (HIGH PRIORITY)")
    output.append(f"- **Total overlapped questions:** {len(sorted_3plus)}")
    output.append("")
    output.append("**Study Strategy:**")
    output.append("1. Master the 5+ role questions first (highest ROI)")
    output.append("2. Then study 3-4 role questions")
    output.append("3. These cover 60-80% of what you'll be asked")
    output.append("")
    output.append("---")
    output.append("")
    
    # SUPER HIGH PRIORITY - 5+ roles
    output.append("=" * 80)
    output.append("## 🔥 SUPER HIGH PRIORITY - Questions in 5+ Roles")
    output.append("=" * 80)
    output.append("")
    output.append(f"**Total:** {len(sorted_5plus)} questions")
    output.append("")
    output.append("**💡 Why these matter:**")
    output.append("These questions appear in 5 or more different roles. If you master these,")
    output.append("you'll be prepared for the most common questions across ALL your target roles.")
    output.append("")
    output.append("---")
    output.append("")
    
    for i, (normalized, data) in enumerate(sorted_5plus, 1):
        output.append(f"### {i}. {data['original']}")
        output.append("")
        output.append(f"**Appears in {data['count']} roles:**")
        for role in sorted(data['roles']):
            category = data['categories'].get(role, 'Unknown')
            output.append(f"- {role} ({category})")
        output.append("")
        output.append("---")
        output.append("")
    
    # HIGH PRIORITY - 3-4 roles
    output.append("")
    output.append("=" * 80)
    output.append("## 🎯 HIGH PRIORITY - Questions in 3-4 Roles")
    output.append("=" * 80)
    output.append("")
    output.append(f"**Total:** {len(sorted_3plus) - len(sorted_5plus)} questions")
    output.append("")
    output.append("**💡 Why these matter:**")
    output.append("These questions appear in 3-4 roles. Still high probability, study after")
    output.append("you've mastered the 5+ role questions.")
    output.append("")
    output.append("---")
    output.append("")
    
    for i, (normalized, data) in enumerate(sorted_3plus, 1):
        if data['count'] < 5:  # Only 3-4 role questions
            output.append(f"### {i}. {data['original']}")
            output.append("")
            output.append(f"**Appears in {data['count']} roles:**")
            for role in sorted(data['roles']):
                category = data['categories'].get(role, 'Unknown')
                output.append(f"- {role} ({category})")
            output.append("")
            output.append("---")
            output.append("")
    
    # Save output
    output_dir = Path(__file__).parent.parent / 'output'
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / 'TRUE_OVERLAPPED_QUESTIONS.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(output))
    
    print(f"✅ Generated: {output_path}")
    print()
    print("📋 Top 10 Most Overlapped Questions:")
    for i, (normalized, data) in enumerate(sorted_5plus[:10], 1):
        print(f"   {i}. ({data['count']} roles) {data['original'][:60]}...")

if __name__ == "__main__":
    main()
