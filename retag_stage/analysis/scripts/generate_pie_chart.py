#!/usr/bin/env python3
"""
Generate pie chart showing question distribution across 3 files
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
    """Count overlapped questions"""
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
    
    # Count overlapped (3+ roles)
    overlapped = sum(1 for count in question_count.values() if count >= 3)
    
    return overlapped

def is_lhf_category(category_name):
    """Check if category is Low Hanging Fruit"""
    category_lower = category_name.lower()
    
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
    """Generate pie chart data"""
    
    print("📊 Generating Pie Chart Data...")
    print("=" * 80)
    print()
    
    # Count overlapped
    overlapped_count = load_overlapped_questions()
    
    # Load overlapped set for exclusion
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
    
    question_count_map = defaultdict(int)
    
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
                    question_count_map[normalized] += 1
    
    overlapped_set = {q for q, count in question_count_map.items() if count >= 3}
    
    # Count LHF and IGNORE
    lhf_count = 0
    ignore_count = 0
    
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
                
                normalized = normalize_question(q_text)
                if normalized in overlapped_set:
                    continue  # Skip overlapped
                
                if is_lhf_category(category):
                    lhf_count += 1
                elif is_ignore_category(category):
                    ignore_count += 1
    
    total = overlapped_count + lhf_count + ignore_count
    
    # Calculate percentages
    overlapped_pct = (overlapped_count / total * 100) if total > 0 else 0
    lhf_pct = (lhf_count / total * 100) if total > 0 else 0
    ignore_pct = (ignore_count / total * 100) if total > 0 else 0
    
    print(f"⭐️ Overlapped: {overlapped_count} questions ({overlapped_pct:.1f}%)")
    print(f"🟡 LHF: {lhf_count} questions ({lhf_pct:.1f}%)")
    print(f"🔴 Ignore: {ignore_count} questions ({ignore_pct:.1f}%)")
    print(f"📊 Total: {total} questions")
    print()
    
    # Generate ASCII pie chart
    output = []
    output.append("# 📊 QUESTION DISTRIBUTION - PIE CHART")
    output.append("")
    output.append("## Summary Table")
    output.append("")
    output.append("| Category | Questions | Percentage | Priority |")
    output.append("|----------|-----------|------------|----------|")
    output.append(f"| ⭐️ Overlapped | {overlapped_count} | {overlapped_pct:.1f}% | Study First |")
    output.append(f"| 🟡 Low Hanging Fruit | {lhf_count} | {lhf_pct:.1f}% | Study Next |")
    output.append(f"| 🔴 Ignore | {ignore_count} | {ignore_pct:.1f}% | Skip |")
    output.append(f"| **TOTAL** | **{total}** | **100%** | |")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## ASCII Pie Chart")
    output.append("")
    output.append("```")
    
    # Create ASCII pie chart
    overlapped_bars = int(overlapped_pct / 2)
    lhf_bars = int(lhf_pct / 2)
    ignore_bars = int(ignore_pct / 2)
    
    output.append("         Question Distribution")
    output.append("")
    output.append(f"  ⭐️ Overlapped ({overlapped_pct:.1f}%)")
    output.append(f"  {'█' * overlapped_bars}")
    output.append("")
    output.append(f"  🟡 Low Hanging Fruit ({lhf_pct:.1f}%)")
    output.append(f"  {'█' * lhf_bars}")
    output.append("")
    output.append(f"  🔴 Ignore ({ignore_pct:.1f}%)")
    output.append(f"  {'█' * ignore_bars}")
    output.append("")
    output.append("```")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## What This Means")
    output.append("")
    output.append(f"**{overlapped_pct:.1f}% of questions** appear across multiple roles")
    output.append("- These are your highest ROI")
    output.append("- Study these first")
    output.append("")
    output.append(f"**{lhf_pct:.1f}% of questions** are low hanging fruit")
    output.append("- You're already 70-95% ready")
    output.append("- Easy wins with 30-60 hours study")
    output.append("")
    output.append(f"**{ignore_pct:.1f}% of questions** should be ignored")
    output.append("- Would take 200+ hours to master")
    output.append("- Target roles that don't need these")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## Your Study Strategy")
    output.append("")
    output.append(f"**Focus on {overlapped_pct + lhf_pct:.1f}% of questions** (Overlapped + LHF)")
    output.append("")
    output.append(f"**Skip {ignore_pct:.1f}% of questions** (Ignore list)")
    output.append("")
    output.append("**Result:** Study 30-60 hours instead of 200+ hours")
    
    # Save output
    output_dir = Path(__file__).parent.parent / 'output'
    output_path = output_dir / 'QUESTION_DISTRIBUTION_PIE_CHART.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(output))
    
    print(f"✅ Generated: {output_path}")

if __name__ == "__main__":
    main()
