#!/usr/bin/env python3
"""
Generate 2 simple files:
1. 🟡 LHF (Low Hanging Fruit) - Easy wins after overlapped
2. 🔴 IGNORE - What to skip
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
    
    q = re.sub(r'\s+', ' ', q.strip().lower())
    q = re.sub(r'[^\w\s]', '', q)
    return q

def load_overlapped_questions():
    """Load questions that are already in overlapped list"""
    overlapped = set()
    
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
    
    question_count = defaultdict(int)
    
    for role_slug, role_name in role_names.items():
        role_dir = roles_dir / role_slug
        if not role_dir.exists():
            continue
        
        json_path = role_dir / 'data' / 'questions_by_category.json'
        if json_path.exists():
            with open(json_path) as f:
                questions_by_cat = json.load(f)
                
            for category, questions in questions_by_cat.items():
                for q in questions:
                    if isinstance(q, dict):
                        q_text = q.get('question', '')
                    else:
                        q_text = str(q)
                    
                    normalized = normalize_question(q_text)
                    question_count[normalized] += 1
    
    # Questions in 3+ roles are overlapped
    for q, count in question_count.items():
        if count >= 3:
            overlapped.add(q)
    
    return overlapped

def is_lhf_category(category_name):
    """Check if category is Low Hanging Fruit (easy for MBA/VC/PE background)"""
    category_lower = category_name.lower()
    
    # LHF - Easy wins with your background
    lhf_keywords = [
        'strategy', 'business', 'operations', 'planning', 'finance', 'growth',
        'problem solving', 'analytical', 'decision', 'prioritization',
        'leadership', 'management', 'stakeholder', 'communication', 'collaboration',
        'sql', 'data analysis', 'metrics', 'kpi', 'dashboard'
    ]
    
    for keyword in lhf_keywords:
        if keyword in category_lower:
            return True
    
    return False

def is_ignore_category(category_name):
    """Check if category should be ignored"""
    category_lower = category_name.lower()
    
    # IGNORE - Not worth your time
    ignore_keywords = [
        'algorithm', 'data structure', 'coding', 'leetcode', 'tree', 'graph',
        'dynamic programming', 'machine learning', 'deep learning', 'neural network',
        'model training', 'ml theory', 'array', 'string manipulation', 'recursion',
        'backtracking', 'binary search', 'sorting', 'heap', 'stack', 'queue'
    ]
    
    for keyword in ignore_keywords:
        if keyword in category_lower:
            return True
    
    return False

def load_role_questions(role_dir):
    """Load categorized questions for a role"""
    json_path = role_dir / 'data' / 'questions_by_category.json'
    if json_path.exists():
        with open(json_path) as f:
            return json.load(f)
    return {}

def main():
    """Generate LHF and IGNORE lists"""
    
    print("🎯 Generating LHF and IGNORE lists...")
    print("=" * 80)
    print()
    
    # Load overlapped questions to exclude
    print("📋 Loading overlapped questions to exclude...")
    overlapped_set = load_overlapped_questions()
    print(f"   Found {len(overlapped_set)} overlapped questions")
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
    
    # Collect LHF and IGNORE questions
    lhf_by_category = defaultdict(lambda: {'roles': [], 'questions': []})
    ignore_by_category = defaultdict(lambda: {'roles': [], 'questions': []})
    
    for role_slug, role_name in role_names.items():
        role_dir = roles_dir / role_slug
        if not role_dir.exists():
            continue
        
        questions_by_cat = load_role_questions(role_dir)
        
        for category, questions in questions_by_cat.items():
            # Filter out overlapped questions
            unique_questions = []
            for q in questions:
                if isinstance(q, dict):
                    q_text = q.get('question', '')
                else:
                    q_text = str(q)
                
                normalized = normalize_question(q_text)
                if normalized not in overlapped_set:
                    unique_questions.append(q_text)
            
            if not unique_questions:
                continue
            
            # Categorize as LHF or IGNORE
            if is_lhf_category(category):
                lhf_by_category[category]['roles'].append(role_name)
                lhf_by_category[category]['questions'].extend(unique_questions)
            elif is_ignore_category(category):
                ignore_by_category[category]['roles'].append(role_name)
                ignore_by_category[category]['questions'].extend(unique_questions)
    
    # Sort by number of questions
    lhf_sorted = sorted(lhf_by_category.items(), key=lambda x: len(x[1]['questions']), reverse=True)
    ignore_sorted = sorted(ignore_by_category.items(), key=lambda x: len(x[1]['questions']), reverse=True)
    
    print(f"🟡 LHF Categories: {len(lhf_sorted)}")
    print(f"🔴 IGNORE Categories: {len(ignore_sorted)}")
    print()
    
    # Generate LHF file
    lhf_output = []
    lhf_output.append("# 🟡 LOW HANGING FRUIT (LHF) - Study After Overlapped")
    lhf_output.append("")
    lhf_output.append("**After mastering ⭐️ TRUE OVERLAPPED QUESTIONS, study these next.**")
    lhf_output.append("")
    lhf_output.append("These are easy wins based on your MBA + VC/PE + 20 years experience.")
    lhf_output.append("You're already 70-95% ready for these categories.")
    lhf_output.append("")
    
    total_lhf = sum(len(data['questions']) for _, data in lhf_sorted)
    lhf_output.append(f"**Total Questions:** {total_lhf}")
    lhf_output.append(f"**Study Time:** 30-60 hours")
    lhf_output.append("")
    lhf_output.append("---")
    lhf_output.append("")
    
    for i, (category, data) in enumerate(lhf_sorted, 1):
        lhf_output.append(f"## {i}. {category}")
        lhf_output.append("")
        lhf_output.append(f"**Questions:** {len(data['questions'])}")
        lhf_output.append(f"**Roles:** {', '.join(data['roles'])}")
        lhf_output.append("")
        lhf_output.append("**Questions:**")
        lhf_output.append("")
        for j, q in enumerate(data['questions'], 1):
            lhf_output.append(f"{j}. {q}")
        lhf_output.append("")
        lhf_output.append("---")
        lhf_output.append("")
    
    # Generate IGNORE file
    ignore_output = []
    ignore_output.append("# 🔴 IGNORE LIST - Skip These Entirely")
    ignore_output.append("")
    ignore_output.append("**DO NOT STUDY THESE. Target roles that don't require them.**")
    ignore_output.append("")
    ignore_output.append("These categories would take 200+ hours to get from 30% to 70%.")
    ignore_output.append("Not worth your time. Focus on LHF instead.")
    ignore_output.append("")
    
    total_ignore = sum(len(data['questions']) for _, data in ignore_sorted)
    ignore_output.append(f"**Total Questions:** {total_ignore}")
    ignore_output.append(f"**Time Saved:** 200+ hours")
    ignore_output.append("")
    ignore_output.append("---")
    ignore_output.append("")
    ignore_output.append("## Why Skip These?")
    ignore_output.append("")
    ignore_output.append("1. **Data Structures & Algorithms** - Would take 100+ hours")
    ignore_output.append("2. **Machine Learning Theory** - Not your target roles")
    ignore_output.append("3. **LeetCode Coding** - Better to target non-coding roles")
    ignore_output.append("")
    ignore_output.append("**Instead:** Target roles like BizOps, Business Analyst, Product Analyst, Chief of Staff")
    ignore_output.append("")
    ignore_output.append("---")
    ignore_output.append("")
    
    for i, (category, data) in enumerate(ignore_sorted, 1):
        ignore_output.append(f"## {i}. {category} ❌")
        ignore_output.append("")
        ignore_output.append(f"**Questions:** {len(data['questions'])}")
        ignore_output.append(f"**Roles:** {', '.join(data['roles'])}")
        ignore_output.append("")
        ignore_output.append("**Why skip:** Would take 50+ hours to master, not aligned with your strengths")
        ignore_output.append("")
        ignore_output.append("---")
        ignore_output.append("")
    
    # Save files
    output_dir = Path(__file__).parent.parent / 'output'
    
    lhf_path = output_dir / '🟡_LOW_HANGING_FRUIT.md'
    with open(lhf_path, 'w') as f:
        f.write('\n'.join(lhf_output))
    
    ignore_path = output_dir / '🔴_IGNORE_LIST.md'
    with open(ignore_path, 'w') as f:
        f.write('\n'.join(ignore_output))
    
    print(f"✅ Generated: {lhf_path}")
    print(f"✅ Generated: {ignore_path}")
    print()
    print("📊 Summary:")
    print(f"   🟡 LHF: {len(lhf_sorted)} categories, {total_lhf} questions")
    print(f"   🔴 IGNORE: {len(ignore_sorted)} categories, {total_ignore} questions")
    print()
    print("🎯 Your 3 Files:")
    print("   1. ⭐️_TRUE_OVERLAPPED_QUESTIONS.md (study first)")
    print("   2. 🟡_LOW_HANGING_FRUIT.md (study next)")
    print("   3. 🔴_IGNORE_LIST.md (skip entirely)")

if __name__ == "__main__":
    main()
