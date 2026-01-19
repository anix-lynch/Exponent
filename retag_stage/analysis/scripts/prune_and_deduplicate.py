#!/usr/bin/env python3
"""
Prune and deduplicate questions:
1. Reclassify hidden coding questions
2. Deduplicate similar questions
3. Remove role-specific questions
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

def is_hidden_coding_question(question_text):
    """Detect coding questions miscategorized as analytical"""
    text_lower = question_text.lower()
    
    coding_keywords = [
        'write a function', 'implement', 'write code', 'code a',
        'linked list', 'binary tree', 'binary search tree',
        'array', 'string manipulation', 'hash table', 'hash map',
        'valid parentheses', 'two sum', 'three sum',
        'reverse linked list', 'merge sorted', 'merge k sorted',
        'search in rotated', 'find peak', 'find duplicate',
        'longest substring', 'palindrome', 'anagram',
        'depth first', 'breadth first', 'dfs', 'bfs',
        'dynamic programming', 'recursion', 'backtracking',
        'merge intervals', 'linked list cycle', 'lru cache',
        'return all prime', 'fibonacci', 'factorial',
        'sort algorithm', 'quicksort', 'mergesort',
        'time complexity', 'space complexity', 'big o'
    ]
    
    for keyword in coding_keywords:
        if keyword in text_lower:
            return True
    
    return False

def get_question_pattern(question_text):
    """Get the core pattern of a question for deduplication"""
    text_lower = question_text.lower()
    
    # Company-specific questions
    if 'why do you want to work at' in text_lower or 'why are you interested in' in text_lower:
        return 'PATTERN: Why Company X?'
    
    if 'why do you want to join' in text_lower:
        return 'PATTERN: Why Company X?'
    
    # Tell me about yourself variations
    if 'tell me about yourself' in text_lower or 'walk me through your resume' in text_lower:
        return 'PATTERN: Tell me about yourself'
    
    if 'tell me about your experience' in text_lower or 'tell me about your background' in text_lower:
        return 'PATTERN: Tell me about yourself'
    
    # Conflict/disagreement
    if any(k in text_lower for k in ['conflict', 'disagreement', 'difficult stakeholder', 'challenging stakeholder']):
        return 'PATTERN: Conflict resolution'
    
    # Failure/mistake
    if any(k in text_lower for k in ['tell me about a time you failed', 'biggest mistake', 'time you were wrong']):
        return 'PATTERN: Failure/learning'
    
    # Leadership
    if 'led a team' in text_lower or 'leadership experience' in text_lower:
        return 'PATTERN: Leadership'
    
    # Data-driven decision
    if 'used data' in text_lower or 'data-driven decision' in text_lower:
        return 'PATTERN: Data-driven decision'
    
    # Complex problem
    if 'complex problem' in text_lower or 'difficult problem' in text_lower:
        return 'PATTERN: Problem solving'
    
    # Prioritization
    if 'prioritize' in text_lower and 'how do you' in text_lower:
        return 'PATTERN: Prioritization'
    
    # No pattern - keep as unique
    return None

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
    """Prune and deduplicate questions"""
    
    print("🔍 Pruning and Deduplicating Questions...")
    print("=" * 80)
    print()
    
    # Load all questions
    question_map = load_all_questions()
    
    print(f"📊 Total unique questions before pruning: {len(question_map)}")
    print()
    
    # Step 1: Reclassify hidden coding questions
    print("Step 1: Reclassifying hidden coding questions...")
    hidden_coding = 0
    
    # Step 2: Deduplicate by pattern
    print("Step 2: Deduplicating similar questions...")
    pattern_map = defaultdict(list)
    unique_questions = []
    
    for normalized, data in question_map.items():
        text = data['text']
        count = data['count']
        roles = data['roles']
        
        # Check if hidden coding
        if is_hidden_coding_question(text):
            hidden_coding += 1
            continue  # Skip coding questions
        
        # Check if target role
        if count < 3 and not any(role in TARGET_ROLES for role in roles):
            continue  # Skip non-target role questions
        
        # Get pattern
        pattern = get_question_pattern(text)
        
        if pattern:
            pattern_map[pattern].append((text, count, list(roles)))
        else:
            unique_questions.append((text, count, list(roles)))
    
    print(f"   Found {hidden_coding} hidden coding questions → Moved to Red")
    print(f"   Found {len(pattern_map)} question patterns")
    print()
    
    # Step 3: Create final lists
    star_questions = []      # 5+ roles
    green_questions = []     # 3-4 roles
    yellow_questions = []    # 1-2 roles in target
    
    # Add pattern representatives
    for pattern, questions in pattern_map.items():
        # Sort by count (most roles first)
        questions.sort(key=lambda x: x[1], reverse=True)
        best_example = questions[0]
        text, count, roles = best_example
        
        if count >= 5:
            star_questions.append((pattern, text, count, roles, len(questions)))
        elif count >= 3:
            green_questions.append((pattern, text, count, roles, len(questions)))
        else:
            yellow_questions.append((pattern, text, count, roles, len(questions)))
    
    # Add unique questions
    for text, count, roles in unique_questions:
        if count >= 5:
            star_questions.append((None, text, count, roles, 1))
        elif count >= 3:
            green_questions.append((None, text, count, roles, 1))
        else:
            yellow_questions.append((None, text, count, roles, 1))
    
    # Sort
    star_questions.sort(key=lambda x: x[2], reverse=True)
    green_questions.sort(key=lambda x: x[2], reverse=True)
    yellow_questions.sort(key=lambda x: x[2], reverse=True)
    
    print("📊 After Pruning:")
    print(f"   ⭐️ STAR: {len(star_questions)} questions")
    print(f"   🟢 GREEN: {len(green_questions)} questions")
    print(f"   🟡 YELLOW: {len(yellow_questions)} questions")
    print(f"   🔴 RED: {hidden_coding + (len(question_map) - len(star_questions) - len(green_questions) - len(yellow_questions))} questions")
    print()
    
    total_study = len(star_questions) + len(green_questions) + len(yellow_questions)
    print(f"✅ Study load reduced to: {total_study} questions")
    print()
    
    # Generate output files
    output_dir = Path(__file__).parent.parent / 'output'
    
    # STAR file
    star_output = []
    star_output.append("# ⭐️ STAR - MUST STUDY (5+ Roles)")
    star_output.append("")
    star_output.append(f"**{len(star_questions)} core question patterns**")
    star_output.append("")
    star_output.append("These are the HIGHEST ROI questions. Master these first.")
    star_output.append("")
    star_output.append(f"**Study Time:** 4-6 hours")
    star_output.append("")
    star_output.append("---")
    star_output.append("")
    
    for i, item in enumerate(star_questions, 1):
        if len(item) == 5:
            pattern, text, count, roles, variations = item
            if pattern:
                star_output.append(f"## {i}. {pattern}")
                star_output.append("")
                star_output.append(f"**Example:** {text}")
                star_output.append(f"**Appears in {count} roles:** {', '.join(sorted(roles))}")
                star_output.append(f"**Variations:** {variations} similar questions")
                star_output.append("")
                star_output.append(f"💡 **Tip:** Prepare ONE answer that works for all {variations} variations")
            else:
                star_output.append(f"## {i}. {text}")
                star_output.append("")
                star_output.append(f"**Appears in {count} roles:** {', '.join(sorted(roles))}")
        star_output.append("")
        star_output.append("---")
        star_output.append("")
    
    star_path = output_dir / '⭐️_STAR_MUST_STUDY.md'
    with open(star_path, 'w') as f:
        f.write('\n'.join(star_output))
    
    # GREEN file
    green_output = []
    green_output.append("# 🟢 GREEN - HIGH PRIORITY (3-4 Roles)")
    green_output.append("")
    green_output.append(f"**{len(green_questions)} questions**")
    green_output.append("")
    green_output.append("Study these AFTER Star questions.")
    green_output.append("")
    green_output.append(f"**Study Time:** 30-50 hours")
    green_output.append("")
    green_output.append("---")
    green_output.append("")
    
    for i, item in enumerate(green_questions, 1):
        if len(item) == 5:
            pattern, text, count, roles, variations = item
            if pattern:
                green_output.append(f"## {i}. {pattern}")
                green_output.append("")
                green_output.append(f"**Example:** {text}")
                green_output.append(f"**Appears in {count} roles:** {', '.join(sorted(roles))}")
                if variations > 1:
                    green_output.append(f"**Variations:** {variations} similar questions")
            else:
                green_output.append(f"## {i}. {text}")
                green_output.append("")
                green_output.append(f"**Appears in {count} roles:** {', '.join(sorted(roles))}")
        green_output.append("")
        green_output.append("---")
        green_output.append("")
    
    green_path = output_dir / '🟢_GREEN_HIGH_PRIORITY.md'
    with open(green_path, 'w') as f:
        f.write('\n'.join(green_output))
    
    # YELLOW file
    yellow_output = []
    yellow_output.append("# 🟡 YELLOW - TARGET ROLES")
    yellow_output.append("")
    yellow_output.append(f"**{len(yellow_questions)} questions for Chief of Staff / BizOps / Data Engineer**")
    yellow_output.append("")
    yellow_output.append("Study these AFTER Star and Green.")
    yellow_output.append("")
    yellow_output.append(f"**Study Time:** 40-60 hours")
    yellow_output.append("")
    yellow_output.append("---")
    yellow_output.append("")
    
    for i, item in enumerate(yellow_questions, 1):
        if len(item) == 5:
            pattern, text, count, roles, variations = item
            if pattern:
                yellow_output.append(f"## {i}. {pattern}")
                yellow_output.append("")
                yellow_output.append(f"**Example:** {text}")
                yellow_output.append(f"**Roles:** {', '.join(sorted(roles))}")
                if variations > 1:
                    yellow_output.append(f"**Variations:** {variations} similar questions")
            else:
                yellow_output.append(f"## {i}. {text}")
                yellow_output.append("")
                yellow_output.append(f"**Roles:** {', '.join(sorted(roles))}")
        yellow_output.append("")
        yellow_output.append("---")
        yellow_output.append("")
    
    yellow_path = output_dir / '🟡_YELLOW_TARGET_ROLES.md'
    with open(yellow_path, 'w') as f:
        f.write('\n'.join(yellow_output))
    
    print(f"✅ Generated: {star_path}")
    print(f"✅ Generated: {green_path}")
    print(f"✅ Generated: {yellow_path}")
    print()
    print("🎯 Summary:")
    print(f"   Before: 1,947 questions")
    print(f"   After: {total_study} questions")
    print(f"   Reduction: {1947 - total_study} questions ({(1947-total_study)/1947*100:.1f}%)")
    print()
    print(f"   Hidden coding removed: {hidden_coding}")
    print(f"   Patterns identified: {len(pattern_map)}")

if __name__ == "__main__":
    main()
