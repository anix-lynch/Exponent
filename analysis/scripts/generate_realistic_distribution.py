#!/usr/bin/env python3
"""
Generate REALISTIC distribution:
- Star: 18 questions (5+ roles)
- Green: 172 questions (3-4 roles) 
- Yellow: 200-300 questions (top 3 roles only)
- Red: 800+ questions (ignore)
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

# Top 3 target roles
TARGET_ROLES = {'Chief of Staff', 'BizOps Strategy', 'Data Engineer'}

def is_must_ignore_category(category_name):
    """Categories to ALWAYS ignore"""
    category_lower = category_name.lower()
    
    must_ignore = [
        # Coding & Algorithms
        'algorithm', 'data structure', 'coding', 'leetcode', 'tree', 'graph',
        'dynamic programming', 'recursion', 'backtracking', 'binary search',
        'sorting', 'heap', 'stack', 'queue', 'array', 'string manipulation',
        
        # ML/Deep Learning Theory
        'machine learning', 'deep learning', 'neural network', 'model training',
        'ml theory', 'supervised', 'unsupervised', 'reinforcement learning',
        
        # Software Engineer specific
        'object-oriented design', 'design patterns', 'concurrency',
        'multithreading', 'memory management'
    ]
    
    for keyword in must_ignore:
        if keyword in category_lower:
            return True
    
    return False

def is_target_role_category(category_name, roles):
    """Check if category is relevant for top 3 target roles"""
    # If any of the roles using this category is in our target, keep it
    for role in roles:
        if role in TARGET_ROLES:
            return True
    return False

def load_all_questions():
    """Load all questions with role and category info"""
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
    
    # Map: normalized_question -> {text, roles, categories, count}
    question_map = defaultdict(lambda: {
        'text': '',
        'roles': set(),
        'categories': set(),
        'count': 0
    })
    
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
                    
                    if not q_text or len(q_text) < 10:
                        continue
                    
                    normalized = normalize_question(q_text)
                    
                    if not question_map[normalized]['text']:
                        question_map[normalized]['text'] = q_text
                    
                    question_map[normalized]['roles'].add(role_name)
                    question_map[normalized]['categories'].add(category)
                    question_map[normalized]['count'] = len(question_map[normalized]['roles'])
    
    return question_map

def main():
    """Generate realistic distribution"""
    
    print("🎯 Generating REALISTIC Distribution...")
    print("=" * 80)
    print()
    print(f"Target Roles: {', '.join(TARGET_ROLES)}")
    print()
    
    # Load all questions
    question_map = load_all_questions()
    
    # Categorize questions
    star_questions = []      # 5+ roles
    green_questions = []     # 3-4 roles
    yellow_questions = []    # 1-2 roles BUT in target roles
    red_questions = []       # Ignore
    
    for normalized, data in question_map.items():
        count = data['count']
        roles = data['roles']
        categories = data['categories']
        text = data['text']
        
        # Check if must ignore
        must_ignore = any(is_must_ignore_category(cat) for cat in categories)
        
        if must_ignore:
            red_questions.append((text, count, list(roles), list(categories)))
        elif count >= 5:
            star_questions.append((text, count, list(roles), list(categories)))
        elif count >= 3:
            green_questions.append((text, count, list(roles), list(categories)))
        elif any(role in TARGET_ROLES for role in roles):
            # Only keep if relevant to target roles
            yellow_questions.append((text, count, list(roles), list(categories)))
        else:
            # Not in target roles, ignore
            red_questions.append((text, count, list(roles), list(categories)))
    
    # Sort
    star_questions.sort(key=lambda x: x[1], reverse=True)
    green_questions.sort(key=lambda x: x[1], reverse=True)
    yellow_questions.sort(key=lambda x: x[1], reverse=True)
    
    print(f"⭐️ STAR (5+ roles): {len(star_questions)} questions")
    print(f"🟢 GREEN (3-4 roles): {len(green_questions)} questions")
    print(f"🟡 YELLOW (target roles): {len(yellow_questions)} questions")
    print(f"🔴 RED (ignore): {len(red_questions)} questions")
    print()
    
    total = len(star_questions) + len(green_questions) + len(yellow_questions) + len(red_questions)
    
    print(f"📊 Total: {total} questions")
    print()
    print(f"Study load: {len(star_questions) + len(green_questions) + len(yellow_questions)} questions")
    print(f"Ignore: {len(red_questions)} questions ({len(red_questions)/total*100:.1f}%)")
    print()
    
    # Generate output files
    output_dir = Path(__file__).parent.parent / 'output'
    
    # 1. STAR file (already exists, just update if needed)
    
    # 2. GREEN file
    green_output = []
    green_output.append("# 🟢 GREEN - HIGH PRIORITY (3-4 Roles)")
    green_output.append("")
    green_output.append(f"**{len(green_questions)} questions that appear in 3-4 roles**")
    green_output.append("")
    green_output.append("Study these AFTER the Star questions.")
    green_output.append("These still have high ROI but slightly less universal.")
    green_output.append("")
    green_output.append(f"**Study Time:** 50-70 hours")
    green_output.append("")
    green_output.append("---")
    green_output.append("")
    
    for i, (text, count, roles, categories) in enumerate(green_questions, 1):
        green_output.append(f"## {i}. {text}")
        green_output.append("")
        green_output.append(f"**Appears in {count} roles:** {', '.join(sorted(roles))}")
        green_output.append(f"**Categories:** {', '.join(sorted(set(categories)))}")
        green_output.append("")
        green_output.append("---")
        green_output.append("")
    
    green_path = output_dir / '🟢_GREEN_HIGH_PRIORITY.md'
    with open(green_path, 'w') as f:
        f.write('\n'.join(green_output))
    
    # 3. YELLOW file
    yellow_output = []
    yellow_output.append("# 🟡 YELLOW - TARGET ROLES ONLY")
    yellow_output.append("")
    yellow_output.append(f"**{len(yellow_questions)} questions for your top 3 target roles**")
    yellow_output.append("")
    yellow_output.append(f"**Target Roles:** {', '.join(TARGET_ROLES)}")
    yellow_output.append("")
    yellow_output.append("Study these AFTER Star and Green.")
    yellow_output.append("These are specific to your target roles.")
    yellow_output.append("")
    yellow_output.append(f"**Study Time:** 60-90 hours")
    yellow_output.append("")
    yellow_output.append("---")
    yellow_output.append("")
    
    for i, (text, count, roles, categories) in enumerate(yellow_questions, 1):
        yellow_output.append(f"## {i}. {text}")
        yellow_output.append("")
        yellow_output.append(f"**Appears in {count} role(s):** {', '.join(sorted(roles))}")
        yellow_output.append(f"**Categories:** {', '.join(sorted(set(categories)))}")
        yellow_output.append("")
        yellow_output.append("---")
        yellow_output.append("")
    
    yellow_path = output_dir / '🟡_YELLOW_TARGET_ROLES.md'
    with open(yellow_path, 'w') as f:
        f.write('\n'.join(yellow_output))
    
    # 4. Update RED file
    red_output = []
    red_output.append("# 🔴 RED - IGNORE LIST")
    red_output.append("")
    red_output.append(f"**{len(red_questions)} questions to SKIP ENTIRELY**")
    red_output.append("")
    red_output.append("**Why ignore:**")
    red_output.append("1. Not relevant to your top 3 target roles")
    red_output.append("2. Would take 200+ hours to master")
    red_output.append("3. Low ROI for your background")
    red_output.append("")
    red_output.append(f"**Time Saved:** 200+ hours")
    red_output.append("")
    red_output.append("---")
    red_output.append("")
    red_output.append("## Categories to Ignore:")
    red_output.append("")
    
    # Group by category
    by_category = defaultdict(list)
    for text, count, roles, categories in red_questions:
        for cat in categories:
            by_category[cat].append(text)
    
    for category in sorted(by_category.keys()):
        questions = by_category[category]
        red_output.append(f"### {category} ({len(questions)} questions)")
        red_output.append("")
        red_output.append("**Why skip:** Not aligned with Chief of Staff / BizOps / Data Engineer roles")
        red_output.append("")
        red_output.append("---")
        red_output.append("")
    
    red_path = output_dir / '🔴_RED_IGNORE_LIST.md'
    with open(red_path, 'w') as f:
        f.write('\n'.join(red_output))
    
    # 5. Summary pie chart
    pie_output = []
    pie_output.append("# 📊 REALISTIC QUESTION DISTRIBUTION")
    pie_output.append("")
    pie_output.append("## Summary Table")
    pie_output.append("")
    pie_output.append("| Priority | Questions | Percentage | Study Time | Action |")
    pie_output.append("|----------|-----------|------------|------------|--------|")
    pie_output.append(f"| ⭐️ STAR | {len(star_questions)} | {len(star_questions)/total*100:.1f}% | 2-3h | Study first |")
    pie_output.append(f"| 🟢 GREEN | {len(green_questions)} | {len(green_questions)/total*100:.1f}% | 50-70h | Study next |")
    pie_output.append(f"| 🟡 YELLOW | {len(yellow_questions)} | {len(yellow_questions)/total*100:.1f}% | 60-90h | If time |")
    pie_output.append(f"| 🔴 RED | {len(red_questions)} | {len(red_questions)/total*100:.1f}% | 0h | SKIP |")
    pie_output.append(f"| **TOTAL** | **{total}** | **100%** | | |")
    pie_output.append("")
    pie_output.append("---")
    pie_output.append("")
    pie_output.append("## ASCII Pie Chart")
    pie_output.append("")
    pie_output.append("```")
    
    star_pct = len(star_questions) / total * 100
    green_pct = len(green_questions) / total * 100
    yellow_pct = len(yellow_questions) / total * 100
    red_pct = len(red_questions) / total * 100
    
    star_bars = int(star_pct / 2)
    green_bars = int(green_pct / 2)
    yellow_bars = int(yellow_pct / 2)
    red_bars = int(red_pct / 2)
    
    pie_output.append("         Question Distribution")
    pie_output.append("")
    pie_output.append(f"  ⭐️ STAR (5+ roles) - {star_pct:.1f}%")
    pie_output.append(f"  {'█' * star_bars}")
    pie_output.append("")
    pie_output.append(f"  🟢 GREEN (3-4 roles) - {green_pct:.1f}%")
    pie_output.append(f"  {'█' * green_bars}")
    pie_output.append("")
    pie_output.append(f"  🟡 YELLOW (target roles) - {yellow_pct:.1f}%")
    pie_output.append(f"  {'█' * yellow_bars}")
    pie_output.append("")
    pie_output.append(f"  🔴 RED (ignore) - {red_pct:.1f}%")
    pie_output.append(f"  {'█' * red_bars}")
    pie_output.append("")
    pie_output.append("```")
    pie_output.append("")
    pie_output.append("---")
    pie_output.append("")
    pie_output.append("## Your Study Plan")
    pie_output.append("")
    pie_output.append(f"**Week 1:** ⭐️ STAR ({len(star_questions)} questions)")
    pie_output.append(f"**Week 2-3:** 🟢 GREEN ({len(green_questions)} questions)")
    pie_output.append(f"**Week 4-6:** 🟡 YELLOW ({len(yellow_questions)} questions)")
    pie_output.append(f"**Forever:** 🔴 RED - Skip {len(red_questions)} questions")
    pie_output.append("")
    pie_output.append(f"**Total Study Load:** {len(star_questions) + len(green_questions) + len(yellow_questions)} questions")
    pie_output.append(f"**Total Time:** 110-160 hours (much more realistic!)")
    
    pie_path = output_dir / 'QUESTION_DISTRIBUTION_PIE_CHART.md'
    with open(pie_path, 'w') as f:
        f.write('\n'.join(pie_output))
    
    print(f"✅ Generated: {green_path}")
    print(f"✅ Generated: {yellow_path}")
    print(f"✅ Updated: {red_path}")
    print(f"✅ Updated: {pie_path}")
    print()
    print("🎯 Your 4 Files:")
    print(f"   1. ⭐️_TRUE_OVERLAPPED_QUESTIONS.md ({len(star_questions)} questions)")
    print(f"   2. 🟢_GREEN_HIGH_PRIORITY.md ({len(green_questions)} questions)")
    print(f"   3. 🟡_YELLOW_TARGET_ROLES.md ({len(yellow_questions)} questions)")
    print(f"   4. 🔴_RED_IGNORE_LIST.md ({len(red_questions)} questions)")
    print()
    print(f"📚 Study: {len(star_questions) + len(green_questions) + len(yellow_questions)} questions (110-160 hours)")
    print(f"🚫 Ignore: {len(red_questions)} questions (save 200+ hours)")

if __name__ == "__main__":
    main()
