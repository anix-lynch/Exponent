#!/usr/bin/env python3
"""
Generate HIGH QUALITY Red Ignore List
- Same format as Yellow list
- With frameworks and actual questions
- Clean markdown (no === lines)
- SMART question selection: filter junk, pick diverse/useful questions
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# Target roles to KEEP (everything else goes to Red)
TARGET_ROLES = {'Chief of Staff', 'BizOps Strategy', 'Data Engineer'}

# Junk patterns to filter out
JUNK_PATTERNS = [
    r'^share interview',
    r'^i was asked',
    r'^\+ share',
    r'^share your',
    r'^contribute',
    r'^why work at \w+\?$',  # "Why work at X?" - too specific
    r'^why do you want to work at \w+\?$',  # Same
    r'^if i know',
    r'^do you know',
]

# Company-specific patterns (too narrow)
COMPANY_SPECIFIC = [
    r'design \w+ for',  # "Design Uber for X"
    r'as a pm at \w+',
    r'at \w+,',
    r'why did \w+ fail',
]

def is_junk_question(question):
    """Check if question is junk/broken scraped data."""
    q_lower = question.lower().strip()
    
    # Too short (likely broken)
    if len(q_lower) < 10:
        return True
    
    # Check junk patterns
    for pattern in JUNK_PATTERNS:
        if re.search(pattern, q_lower):
            return True
    
    return False

def is_too_specific(question):
    """Check if question is too company/product specific."""
    q_lower = question.lower()
    
    for pattern in COMPANY_SPECIFIC:
        if re.search(pattern, q_lower):
            return True
    
    return False

def calculate_question_value(question, category):
    """
    Calculate value score for a question.
    Higher score = more useful for learning.
    """
    score = 0
    q_lower = question.lower()
    
    # Prefer "how" questions (teach methodology)
    if q_lower.startswith('how'):
        score += 10
    
    # Prefer "what" questions (teach concepts)
    if q_lower.startswith('what'):
        score += 8
    
    # Prefer questions with key learning words
    learning_words = ['explain', 'describe', 'difference between', 'compare', 'analyze', 'calculate']
    for word in learning_words:
        if word in q_lower:
            score += 5
            break
    
    # Penalize overly long questions (usually too specific)
    if len(question) > 150:
        score -= 5
    
    # Penalize overly short questions (usually broken)
    if len(question) < 20:
        score -= 10
    
    # Prefer questions with numbers/metrics (more concrete)
    if any(word in q_lower for word in ['metric', 'kpi', 'measure', 'calculate', 'estimate']):
        score += 3
    
    # Category-specific bonuses
    if 'coding' in category.lower() or 'algorithm' in category.lower():
        # Prefer classic algorithm questions
        if any(word in q_lower for word in ['array', 'tree', 'linked list', 'sort', 'search']):
            score += 5
    
    if 'sql' in category.lower():
        # Prefer SQL with clear operations
        if any(word in q_lower for word in ['join', 'group by', 'window', 'aggregate']):
            score += 5
    
    return score

def select_best_questions(questions, category, max_count=10):
    """
    Select the best N questions from a list.
    Filters junk, ranks by value, ensures diversity.
    """
    # Filter out junk
    clean_questions = []
    for q_data in questions:
        question = q_data['question']
        if not is_junk_question(question) and not is_too_specific(question):
            q_data['value_score'] = calculate_question_value(question, category)
            clean_questions.append(q_data)
    
    # If we filtered everything, return original (better than nothing)
    if not clean_questions:
        return questions[:max_count]
    
    # Sort by value score (highest first), then by frequency, then by length
    clean_questions.sort(key=lambda x: (-x['value_score'], -x['count'], len(x['question'])))
    
    # Take top N
    return clean_questions[:max_count]

def load_overlapped_questions():
    """Load questions from overlapped list."""
    overlapped = set()
    overlapped_file = Path(__file__).parent.parent / 'output' / '⭐️_TRUE_OVERLAPPED_QUESTIONS.md'
    
    if overlapped_file.exists():
        with open(overlapped_file) as f:
            for line in f:
                if line.strip().startswith(('1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ')):
                    parts = line.split('.', 1)
                    if len(parts) > 1:
                        q = parts[1].strip()
                        if '[' in q:
                            q = q.split('[')[0].strip()
                        overlapped.add(q)
    
    return overlapped

def load_yellow_questions():
    """Load questions from yellow list."""
    yellow = set()
    yellow_file = Path(__file__).parent.parent / 'output' / '🟡_LOW_HANGING_FRUIT.md'
    
    if yellow_file.exists():
        with open(yellow_file) as f:
            for line in f:
                if line.strip().startswith(('1. 🟡', '2. 🟡', '3. 🟡', '4. 🟡', '5. 🟡', '6. 🟡', '7. 🟡', '8. 🟡', '9. 🟡')):
                    parts = line.split('🟡', 1)
                    if len(parts) > 1:
                        yellow.add(parts[1].strip())
    
    return yellow

def get_category_framework(category):
    """Get framework for a category."""
    category_lower = category.lower()
    
    # Coding/Algorithms
    if any(kw in category_lower for kw in ['coding', 'algorithm', 'data structure', 'leetcode']):
        return """
Coding Problem Framework
├─ 1. Clarify
│  ├─ Input/output format
│  ├─ Edge cases
│  └─ Constraints
│
├─ 2. Plan
│  ├─ Brute force approach
│  ├─ Optimal approach
│  └─ Time/space complexity
│
├─ 3. Code
│  ├─ Write clean code
│  ├─ Handle edge cases
│  └─ Test with examples
│
└─ 4. Optimize
   ├─ Review complexity
   ├─ Refactor if needed
   └─ Explain trade-offs
"""
    
    # ML/AI
    elif any(kw in category_lower for kw in ['machine learning', 'ml', 'deep learning', 'ai', 'neural']):
        return """
ML Problem Framework
├─ 1. Problem Definition
│  ├─ Classification/Regression/Clustering?
│  ├─ Supervised/Unsupervised?
│  └─ Success metrics
│
├─ 2. Data
│  ├─ Features available
│  ├─ Data quality
│  └─ Train/test split
│
├─ 3. Model Selection
│  ├─ Baseline model
│  ├─ Advanced models
│  └─ Ensemble methods
│
└─ 4. Evaluation
   ├─ Metrics (accuracy, F1, etc.)
   ├─ Cross-validation
   └─ Production monitoring
"""
    
    # Product/PM
    elif any(kw in category_lower for kw in ['product', 'feature', 'user', 'design']):
        return """
Product Framework
├─ 1. Clarify
│  ├─ Who is the user?
│  ├─ What problem are we solving?
│  └─ Success criteria
│
├─ 2. Users & Needs
│  ├─ User segments
│  ├─ Pain points
│  └─ Use cases
│
├─ 3. Solution
│  ├─ Feature ideas
│  ├─ Prioritization
│  └─ MVP scope
│
└─ 4. Metrics
   ├─ North star metric
   ├─ Supporting metrics
   └─ Trade-offs
"""
    
    # System Design
    elif 'system' in category_lower or 'architecture' in category_lower:
        return """
System Design Framework
├─ 1. Requirements
│  ├─ Functional
│  ├─ Non-functional
│  └─ Constraints
│
├─ 2. High-Level Design
│  ├─ Components
│  ├─ Data flow
│  └─ APIs
│
├─ 3. Deep Dive
│  ├─ Database design
│  ├─ Caching
│  └─ Load balancing
│
└─ 4. Scale
   ├─ Bottlenecks
   ├─ Optimization
   └─ Monitoring
"""
    
    # Default
    else:
        return """
General Problem Framework
├─ 1. Understand
│  ├─ What is being asked?
│  ├─ Key constraints
│  └─ Success criteria
│
├─ 2. Structure
│  ├─ Break into components
│  ├─ Identify dependencies
│  └─ Prioritize
│
├─ 3. Solve
│  ├─ Propose solution
│  ├─ Walk through example
│  └─ Handle edge cases
│
└─ 4. Validate
   ├─ Check assumptions
   ├─ Consider alternatives
   └─ Summarize
"""

def get_why_skip(category):
    """Get reason why this category should be skipped."""
    category_lower = category.lower()
    
    if any(kw in category_lower for kw in ['coding', 'algorithm', 'data structure', 'leetcode']):
        return "Heavy coding/algorithms - not required for Chief of Staff, BizOps Strategy, or Data Engineer roles. Would take 100+ hours to master with low ROI."
    
    elif any(kw in category_lower for kw in ['machine learning', 'ml', 'deep learning', 'neural', 'nlp', 'computer vision']):
        return "ML/AI theory - only relevant for ML Engineer/Data Scientist roles. Your target roles focus on business strategy and data infrastructure, not ML modeling."
    
    elif any(kw in category_lower for kw in ['product', 'feature', 'user experience', 'ux', 'ui']):
        return "Product Management focus - not aligned with Chief of Staff (executive support), BizOps (business operations), or Data Engineer (data infrastructure) roles."
    
    elif any(kw in category_lower for kw in ['mobile', 'ios', 'android', 'frontend', 'react', 'javascript']):
        return "Frontend/mobile development - not relevant for your target roles which focus on business strategy and backend data systems."
    
    elif 'behavioral' in category_lower:
        return "Already covered in ⭐️ Overlapped list. These behavioral questions are specific to non-target roles (PM, Software Engineer, etc.)."
    
    else:
        return "Not aligned with your top 3 target roles (Chief of Staff, BizOps Strategy, Data Engineer). Low ROI for your interview prep."

def main():
    print("🎯 Generating HIGH QUALITY Red Ignore List...")
    print("=" * 80)
    
    # Load overlapped and yellow questions
    overlapped_questions = load_overlapped_questions()
    yellow_questions = load_yellow_questions()
    print(f"📋 Excluding {len(overlapped_questions)} overlapped questions")
    print(f"📋 Excluding {len(yellow_questions)} yellow questions")
    print()
    
    # Load all questions from all roles
    # Track: category -> question -> {count, roles}
    roles_dir = Path(__file__).parent.parent.parent / 'roles'
    all_questions = defaultdict(lambda: {'questions': defaultdict(lambda: {'count': 0, 'roles': set()}), 'roles': set()})
    
    for role_dir in sorted(roles_dir.iterdir()):
        if not role_dir.is_dir():
            continue
        
        role_name = role_dir.name.replace('-', ' ').title()
        by_category_file = role_dir / 'data' / 'questions_by_category.json'
        
        if not by_category_file.exists():
            continue
        
        with open(by_category_file) as f:
            data = json.load(f)
        
        for category, questions in data.items():
            for q_data in questions:
                question = q_data.get('question', '').strip()
                
                if not question or question in overlapped_questions or question in yellow_questions:
                    continue
                
                # Check if question contains overlapped/yellow text
                skip = False
                for oq in overlapped_questions:
                    if oq in question or question in oq:
                        skip = True
                        break
                if not skip:
                    for yq in yellow_questions:
                        if yq in question or question in yq:
                            skip = True
                            break
                
                if not skip:
                    all_questions[category]['questions'][question]['count'] += 1
                    all_questions[category]['questions'][question]['roles'].add(role_name)
                    all_questions[category]['roles'].add(role_name)
    
    # Convert to list format
    for category in all_questions:
        questions_list = []
        for q, data in all_questions[category]['questions'].items():
            questions_list.append({
                'question': q,
                'count': data['count'],
                'roles': data['roles']
            })
        all_questions[category]['questions'] = questions_list
    
    # Sort by question count
    sorted_categories = sorted(
        all_questions.items(),
        key=lambda x: len(x[1]['questions']),
        reverse=True
    )
    
    total_questions = sum(len(data['questions']) for _, data in sorted_categories)
    
    print(f"📊 Found {len(sorted_categories)} categories")
    print(f"📝 Total questions: {total_questions}")
    print()
    
    # Generate output
    output = []
    output.append("# 🔴 RED - IGNORE LIST")
    output.append("")
    output.append(f"**{total_questions:,} questions to SKIP**")
    output.append("")
    output.append("**Why ignore:**")
    output.append("1. Not relevant to your top 3 target roles (Chief of Staff, BizOps Strategy, Data Engineer)")
    output.append("2. Would take 800+ hours to master")
    output.append("3. Low ROI for your background (MBA, VC/PE, family office)")
    output.append("")
    output.append(f"**Time Saved:** 800+ hours")
    output.append("")
    output.append(f"**Your Focus:** Study only ⭐️ Overlapped (190q) + 🟡 Yellow (116q) = 306 questions")
    output.append("")
    output.append("")
    
    # Add each category
    for category, data in sorted_categories:
        roles = sorted(list(data['roles']))
        questions = data['questions']
        
        # Select BEST 10 questions (not just first 10)
        display_questions = select_best_questions(questions, category, max_count=10)
        
        output.append("---")
        output.append("")
        output.append(f"## {category.upper()} 🔴")
        output.append("")
        output.append(f"📊 Total Questions: {len(questions)}")
        output.append(f"🎯 Roles: {', '.join(roles)}")
        output.append("")
        output.append("❌ Why skip:")
        output.append(get_why_skip(category))
        output.append("")
        output.append("🗺️  Framework (if you must study):")
        output.append("```")
        output.append(get_category_framework(category).strip())
        output.append("```")
        output.append("")
        output.append(f"📝 Top 10 High-Value Questions (filtered for quality & relevance):")
        output.append("")
        
        for i, q_data in enumerate(display_questions, 1):
            question_text = q_data['question']
            clean_q = question_text.replace('\n', ' ').replace('  ', ' ').strip()
            role_count = q_data['count']
            output.append(f"{i}. 🔴 {clean_q} [{role_count} roles]")
        
        if len(questions) > 10:
            output.append("")
            output.append(f"*...and {len(questions) - 10} more questions in this category*")
        
        output.append("")
        output.append("")
    
    # Save output
    output_dir = Path(__file__).parent.parent / 'output'
    output_path = output_dir / '🔴_RED_IGNORE_LIST.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(output))
    
    print(f"✅ Generated: {output_path}")
    print()
    print("📋 Top 5 Ignore Categories:")
    for i, (category, data) in enumerate(sorted_categories[:5], 1):
        print(f"   {i}. {category}: {len(data['questions'])} questions")

if __name__ == "__main__":
    main()
