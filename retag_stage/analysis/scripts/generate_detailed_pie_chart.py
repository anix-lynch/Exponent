#!/usr/bin/env python3
"""
Generate detailed pie chart showing categories within each section
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
    """Load overlapped questions and their categories"""
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
    
    question_map = defaultdict(lambda: {'count': 0, 'categories': set()})
    
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
                    question_map[normalized]['count'] += 1
                    question_map[normalized]['categories'].add(category)
    
    # Get overlapped questions by category
    overlapped_by_category = defaultdict(int)
    for q, data in question_map.items():
        if data['count'] >= 3:
            # Use the first category (most common)
            category = list(data['categories'])[0]
            overlapped_by_category[category] += 1
    
    return overlapped_by_category, {q for q, data in question_map.items() if data['count'] >= 3}

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
    """Generate detailed pie chart with categories"""
    
    print("📊 Generating Detailed Pie Chart...")
    print("=" * 80)
    print()
    
    # Get overlapped by category
    overlapped_by_category, overlapped_set = load_overlapped_questions()
    
    # Count LHF and IGNORE by category
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
    
    lhf_by_category = defaultdict(int)
    ignore_by_category = defaultdict(int)
    
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
                    lhf_by_category[category] += 1
                elif is_ignore_category(category):
                    ignore_by_category[category] += 1
    
    # Sort by count
    overlapped_sorted = sorted(overlapped_by_category.items(), key=lambda x: x[1], reverse=True)
    lhf_sorted = sorted(lhf_by_category.items(), key=lambda x: x[1], reverse=True)
    ignore_sorted = sorted(ignore_by_category.items(), key=lambda x: x[1], reverse=True)
    
    overlapped_total = sum(overlapped_by_category.values())
    lhf_total = sum(lhf_by_category.values())
    ignore_total = sum(ignore_by_category.values())
    grand_total = overlapped_total + lhf_total + ignore_total
    
    # Generate output
    output = []
    output.append("# 📊 QUESTION DISTRIBUTION BY CATEGORY")
    output.append("")
    output.append("## Overall Summary")
    output.append("")
    output.append("| Section | Questions | Percentage |")
    output.append("|---------|-----------|------------|")
    output.append(f"| ⭐️ Overlapped | {overlapped_total} | {overlapped_total/grand_total*100:.1f}% |")
    output.append(f"| 🟡 Low Hanging Fruit | {lhf_total} | {lhf_total/grand_total*100:.1f}% |")
    output.append(f"| 🔴 Ignore | {ignore_total} | {ignore_total/grand_total*100:.1f}% |")
    output.append(f"| **TOTAL** | **{grand_total}** | **100%** |")
    output.append("")
    output.append("---")
    output.append("")
    
    # Overlapped section
    output.append("## ⭐️ OVERLAPPED QUESTIONS (17.8%)")
    output.append("")
    output.append("```")
    output.append(f"Total: {overlapped_total} questions")
    output.append("")
    for category, count in overlapped_sorted[:10]:  # Top 10
        pct = count / overlapped_total * 100
        bars = int(pct / 2)
        output.append(f"{category:30} {count:4} ({pct:4.1f}%) {'█' * bars}")
    output.append("```")
    output.append("")
    
    # LHF section
    output.append("## 🟡 LOW HANGING FRUIT (67.3%)")
    output.append("")
    output.append("```")
    output.append(f"Total: {lhf_total} questions")
    output.append("")
    for category, count in lhf_sorted[:15]:  # Top 15
        pct = count / lhf_total * 100
        bars = int(pct / 2)
        output.append(f"{category:30} {count:4} ({pct:4.1f}%) {'█' * bars}")
    output.append("```")
    output.append("")
    
    # Ignore section
    output.append("## 🔴 IGNORE LIST (14.8%)")
    output.append("")
    output.append("```")
    output.append(f"Total: {ignore_total} questions")
    output.append("")
    for category, count in ignore_sorted:
        pct = count / ignore_total * 100
        bars = int(pct / 2)
        output.append(f"{category:30} {count:4} ({pct:4.1f}%) {'█' * bars}")
    output.append("```")
    output.append("")
    output.append("---")
    output.append("")
    
    # Key insights
    output.append("## 🎯 Key Insights")
    output.append("")
    output.append("### Overlapped (Study First)")
    if overlapped_sorted:
        top_3 = overlapped_sorted[:3]
        for i, (cat, count) in enumerate(top_3, 1):
            output.append(f"{i}. **{cat}**: {count} questions")
    output.append("")
    
    output.append("### Low Hanging Fruit (Study Next)")
    if lhf_sorted:
        top_3 = lhf_sorted[:3]
        for i, (cat, count) in enumerate(top_3, 1):
            output.append(f"{i}. **{cat}**: {count} questions")
    output.append("")
    
    output.append("### Ignore (Skip)")
    if ignore_sorted:
        for i, (cat, count) in enumerate(ignore_sorted, 1):
            output.append(f"{i}. **{cat}**: {count} questions - Skip entirely")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 📚 Study Plan")
    output.append("")
    output.append("**Week 1:** Focus on top 3 Overlapped categories")
    output.append("**Week 2-4:** Focus on top 5 LHF categories")
    output.append("**Forever:** Ignore the red categories")
    
    # Save output
    output_dir = Path(__file__).parent.parent / 'output'
    output_path = output_dir / 'QUESTION_DISTRIBUTION_PIE_CHART.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(output))
    
    print(f"✅ Generated: {output_path}")
    print()
    print("📊 Top Categories:")
    print()
    print("⭐️ Overlapped:")
    for cat, count in overlapped_sorted[:3]:
        print(f"   - {cat}: {count}")
    print()
    print("🟡 LHF:")
    for cat, count in lhf_sorted[:3]:
        print(f"   - {cat}: {count}")
    print()
    print("🔴 Ignore:")
    for cat, count in ignore_sorted:
        print(f"   - {cat}: {count}")

if __name__ == "__main__":
    main()
