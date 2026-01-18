#!/usr/bin/env python3
"""
Generate HIGH QUALITY Yellow list with:
- ASCII frameworks for each category
- "What they're testing" explanations
- All questions listed cleanly
- Focus on top 3 target roles
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

TARGET_ROLES = {'Chief of Staff', 'BizOps Strategy', 'Data Engineer'}

def is_coding_question(question_text, category):
    """Detect coding questions to exclude"""
    text_lower = question_text.lower()
    category_lower = category.lower()
    
    # Exclude Behavioral (should only be in overlapped)
    if 'behavioral' in category_lower:
        return True
    
    # Exclude coding categories
    if any(k in category_lower for k in ['algorithm', 'data structure', 'coding', 'leetcode', 'machine learning', 'deep learning']):
        return True
    
    # Exclude coding keywords
    coding_keywords = [
        'write a function', 'implement', 'write code',
        'linked list', 'binary tree', 'binary search tree',
        'valid parentheses', 'two sum', 'reverse linked list',
        'merge sorted', 'search in rotated', 'lru cache',
        'given an array', 'split an array', 'return the pairs',
        'sorting algorithm', 'divide and conquer', 'n-queens'
    ]
    
    for keyword in coding_keywords:
        if keyword in text_lower:
            return True
    
    return False

def load_overlapped_questions():
    """Load overlapped questions to exclude"""
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
    return {q for q, count in question_count.items() if count >= 3}

def get_category_framework(category_name):
    """Get ASCII framework for category"""
    category_lower = category_name.lower()
    
    if 'sql' in category_lower:
        return """
SQL Problem Framework
├─ 1. Understand Requirements
│  ├─ What tables are involved?
│  ├─ What's the expected output?
│  └─ Any edge cases?
│
├─ 2. Identify Query Type
│  ├─ Simple SELECT?
│  ├─ JOIN required?
│  ├─ Aggregation needed?
│  └─ Window function?
│
├─ 3. Build Step-by-Step
│  ├─ Start with FROM/JOIN
│  ├─ Add WHERE filters
│  ├─ Add GROUP BY if needed
│  └─ Add SELECT columns
│
└─ 4. Optimize
   ├─ Use indexes
   ├─ Avoid subqueries if possible
   └─ Test with EXPLAIN
"""
    
    elif 'strategy' in category_lower or 'business' in category_lower:
        return """
Strategy/Business Framework
├─ 1. Clarify the Goal
│  ├─ What's the business objective?
│  ├─ What metrics matter?
│  └─ What's the timeline?
│
├─ 2. Analyze Current State
│  ├─ Market position
│  ├─ Competitive landscape
│  └─ Internal capabilities
│
├─ 3. Identify Options
│  ├─ Brainstorm 3-5 options
│  ├─ Pros/cons of each
│  └─ Resource requirements
│
└─ 4. Recommend & Execute
   ├─ Pick best option (with data)
   ├─ Define success metrics
   └─ Create action plan
"""
    
    elif 'stakeholder' in category_lower or 'communication' in category_lower:
        return """
Stakeholder Management Framework
├─ 1. Identify Stakeholders
│  ├─ Who's impacted?
│  ├─ Who has decision power?
│  └─ Who are influencers?
│
├─ 2. Understand Motivations
│  ├─ What do they care about?
│  ├─ What are their concerns?
│  └─ What's their communication style?
│
├─ 3. Align & Engage
│  ├─ Find common ground
│  ├─ Address concerns early
│  └─ Regular updates
│
└─ 4. Manage Conflicts
   ├─ Listen actively
   ├─ Find win-win solutions
   └─ Escalate if needed
"""
    
    elif 'problem solving' in category_lower or 'analytical' in category_lower:
        return """
Problem Solving Framework
├─ 1. Define the Problem
│  ├─ What's the symptom?
│  ├─ What's the root cause?
│  └─ What's the impact?
│
├─ 2. Gather Data
│  ├─ What data do we have?
│  ├─ What's missing?
│  └─ What assumptions are we making?
│
├─ 3. Analyze & Hypothesize
│  ├─ Break down into components
│  ├─ Test hypotheses
│  └─ Identify patterns
│
└─ 4. Solve & Validate
   ├─ Propose solution
   ├─ Test with data
   └─ Monitor results
"""
    
    elif 'data' in category_lower and 'analysis' in category_lower:
        return """
Data Analysis Framework
├─ 1. Clarify the Question
│  ├─ What metric/outcome?
│  ├─ Time period?
│  └─ Success criteria?
│
├─ 2. Identify Data Sources
│  ├─ What tables/datasets?
│  ├─ Data quality check
│  └─ Missing data?
│
├─ 3. Explore & Segment
│  ├─ By time (trends)
│  ├─ By cohort (user groups)
│  └─ By dimension (geo, device, etc)
│
├─ 4. Diagnose Root Cause
│  ├─ External factors
│  ├─ Internal changes
│  └─ User behavior shifts
│
└─ 5. Recommend Action
   ├─ What to do
   ├─ Expected impact
   └─ How to measure
"""
    
    elif 'system design' in category_lower or 'pipeline' in category_lower:
        return """
System Design Framework
├─ 1. Requirements
│  ├─ Functional (what it does)
│  ├─ Non-functional (scale, latency)
│  └─ Constraints (budget, time)
│
├─ 2. High-Level Design
│  ├─ Client → API → Database
│  ├─ Key components
│  └─ Data flow
│
├─ 3. Deep Dive
│  ├─ Database schema
│  ├─ API design
│  ├─ Caching strategy
│  └─ Load balancing
│
└─ 4. Scale & Optimize
   ├─ Bottlenecks
   ├─ Sharding/replication
   └─ Monitoring
"""
    
    elif 'leadership' in category_lower or 'management' in category_lower:
        return """
Leadership Framework
├─ 1. Set Vision & Goals
│  ├─ Where are we going?
│  ├─ Why does it matter?
│  └─ What success looks like?
│
├─ 2. Build the Team
│  ├─ Right people in right roles
│  ├─ Clear responsibilities
│  └─ Psychological safety
│
├─ 3. Enable & Empower
│  ├─ Remove blockers
│  ├─ Provide resources
│  └─ Delegate authority
│
└─ 4. Monitor & Adapt
   ├─ Track progress
   ├─ Give feedback
   └─ Adjust course
"""
    
    elif 'prioritization' in category_lower:
        return """
Prioritization Framework
├─ 1. List All Options
│  ├─ What needs to be done?
│  ├─ What are the constraints?
│  └─ What are dependencies?
│
├─ 2. Score Each Option
│  ├─ Impact (1-10)
│  ├─ Effort (1-10)
│  └─ Urgency (1-10)
│
├─ 3. Apply Framework
│  ├─ Impact/Effort matrix
│  ├─ RICE scoring
│  └─ MoSCoW method
│
└─ 4. Decide & Communicate
   ├─ Explain the rationale
   ├─ Get buy-in
   └─ Revisit regularly
"""
    
    elif 'metrics' in category_lower or 'kpi' in category_lower:
        return """
Metrics/KPI Framework
├─ 1. Define Success
│  ├─ What's the goal?
│  ├─ What behavior to drive?
│  └─ What's the baseline?
│
├─ 2. Choose Metrics
│  ├─ Leading indicators
│  ├─ Lagging indicators
│  └─ Counter metrics
│
├─ 3. Set Targets
│  ├─ Ambitious but achievable
│  ├─ Time-bound
│  └─ Aligned with business goals
│
└─ 4. Track & Act
   ├─ Dashboard/reporting
   ├─ Regular reviews
   └─ Adjust based on data
"""
    
    else:
        return """
General Framework
├─ 1. Clarify
│  └─ Understand the question
│
├─ 2. Structure
│  └─ Break into components
│
├─ 3. Analyze
│  └─ Use data & logic
│
└─ 4. Conclude
   └─ Clear recommendation
"""

def get_what_testing(category_name):
    """Get 'what they're testing' explanation"""
    category_lower = category_name.lower()
    
    if 'sql' in category_lower:
        return "Can you write efficient SQL queries and understand database concepts?"
    elif 'strategy' in category_lower:
        return "Can you think strategically and make data-driven business decisions?"
    elif 'stakeholder' in category_lower:
        return "Can you influence and manage relationships with senior leaders?"
    elif 'problem solving' in category_lower:
        return "Can you break down complex problems and find solutions?"
    elif 'data analysis' in category_lower:
        return "Can you extract insights from data and drive business decisions?"
    elif 'system design' in category_lower:
        return "Can you design scalable systems and data pipelines?"
    elif 'leadership' in category_lower:
        return "Can you lead teams and drive results?"
    elif 'prioritization' in category_lower:
        return "Can you make trade-offs and prioritize effectively?"
    elif 'metrics' in category_lower:
        return "Can you define and track the right metrics?"
    else:
        return "Can you demonstrate competence in this area?"

def load_role_questions(role_dir):
    """Load categorized questions for a role"""
    json_path = role_dir / 'data' / 'questions_by_category.json'
    if json_path.exists():
        with open(json_path) as f:
            return json.load(f)
    return {}

def main():
    """Generate high quality Yellow list"""
    
    print("🎯 Generating HIGH QUALITY Yellow List...")
    print("=" * 80)
    print()
    
    # Load overlapped to exclude
    overlapped_set = load_overlapped_questions()
    print(f"📋 Excluding {len(overlapped_set)} overlapped questions")
    print()
    
    roles_dir = Path(__file__).parent.parent.parent / 'roles'
    
    role_names = {
        'data-engineer': 'Data Engineer',
        'bizops-strategy': 'BizOps Strategy',
        'chief-of-staff': 'Chief of Staff'
    }
    
    # Collect questions by category for target roles
    category_questions = defaultdict(lambda: {'roles': set(), 'questions': []})
    
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
                
                # Skip coding questions
                if is_coding_question(q_text, category):
                    continue
                
                # Skip overlapped
                normalized = normalize_question(q_text)
                if normalized in overlapped_set:
                    continue
                
                category_questions[category]['roles'].add(role_name)
                category_questions[category]['questions'].append(q_text)
    
    # Sort categories by number of questions
    sorted_categories = sorted(
        category_questions.items(),
        key=lambda x: len(x[1]['questions']),
        reverse=True
    )
    
    print(f"📊 Found {len(sorted_categories)} categories")
    total_questions = sum(len(data['questions']) for _, data in sorted_categories)
    print(f"📝 Total questions: {total_questions}")
    print()
    
    # Generate output
    output = []
    output.append("")
    output.append("╔════════════════════════════════════════════════════════════════════════════════╗")
    output.append("║                                                                                ║")
    output.append("║           🟡 LOW HANGING FRUIT - TARGET ROLES ONLY                             ║")
    output.append("║           Chief of Staff | BizOps Strategy | Data Engineer                     ║")
    output.append("║                                                                                ║")
    output.append("╚════════════════════════════════════════════════════════════════════════════════╝")
    output.append("")
    output.append("This list contains questions specific to your top 3 target roles.")
    output.append("Study these AFTER mastering ⭐️ TRUE OVERLAPPED QUESTIONS.")
    output.append("")
    output.append(f"Total Questions: {total_questions} across {len(sorted_categories)} categories")
    output.append(f"Study Time: 60-90 hours")
    output.append("")
    output.append("")
    
    for category, data in sorted_categories:
        roles = sorted(list(data['roles']))
        questions = data['questions']
        
        output.append("=" * 80)
        output.append(f"{category.upper()} 🟡")
        output.append("=" * 80)
        output.append("")
        output.append(f"📊 Total Questions: {len(questions)}")
        output.append(f"🎯 Roles: {', '.join(roles)}")
        output.append("")
        output.append("🎯 What they're really testing:")
        output.append(get_what_testing(category))
        output.append("")
        output.append("🗺️  Mental Model Framework:")
        output.append("```")
        output.append(get_category_framework(category).strip())
        output.append("```")
        output.append("")
        output.append(f"📝 All {len(questions)} Questions:")
        output.append("")
        
        for i, q in enumerate(questions, 1):
            output.append(f"{i}. 🟡 {q}")
        
        output.append("")
        output.append("")
    
    # Save output
    output_dir = Path(__file__).parent.parent / 'output'
    output_path = output_dir / '🟡_LOW_HANGING_FRUIT.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(output))
    
    print(f"✅ Generated: {output_path}")
    print()
    print("📋 Top 5 Categories:")
    for i, (category, data) in enumerate(sorted_categories[:5], 1):
        print(f"   {i}. {category}: {len(data['questions'])} questions")

if __name__ == "__main__":
    main()
