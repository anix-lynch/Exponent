#!/usr/bin/env python3
"""
Generate ACTIONABLE strength zones - one page with frameworks and specific questions
Excludes questions already in overlapped list
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

def get_category_strength(category_name):
    """Determine strength level based on MBA/VC/PE background"""
    category_lower = category_name.lower()
    
    # SKIP categories (don't show these at all)
    if any(k in category_lower for k in ['algorithm', 'data structure', 'coding', 'leetcode', 'tree', 'graph', 'dynamic programming', 'machine learning', 'deep learning', 'neural network']):
        return None
    
    # 95% - Behavioral (but exclude - it's in overlapped)
    if any(k in category_lower for k in ['behavioral', 'experience', 'background', 'motivation', 'career']):
        return None  # Already in overlapped
    
    # 90% - Strategy & Business
    if any(k in category_lower for k in ['strategy', 'business', 'operations', 'planning', 'finance', 'growth']):
        return ('90%', 'MASTER', '💗', 'MBA + VC/PE')
    
    # 85% - Problem Solving & Analysis
    if any(k in category_lower for k in ['problem solving', 'analytical', 'decision', 'prioritization', 'judgment']):
        return ('85%', 'STRONG', '💗', 'Executive experience')
    
    # 80% - Leadership & Communication
    if any(k in category_lower for k in ['leadership', 'management', 'stakeholder', 'communication', 'collaboration', 'influence']):
        return ('80%', 'STRONG', '💗', '20 years leadership')
    
    # 70% - SQL & Data Analysis (FOCUS)
    if any(k in category_lower for k in ['sql', 'data analysis', 'metrics', 'kpi', 'dashboard', 'visualization']):
        return ('70%', 'FOCUS', '🟢', 'Study 10-20 hours')
    
    # 65% - System Design (FOCUS)
    if any(k in category_lower for k in ['system design', 'architecture', 'scalability', 'infrastructure']):
        return ('65%', 'FOCUS', '🟢', 'Study 15-25 hours')
    
    # 60% - Product
    if any(k in category_lower for k in ['product', 'feature', 'user experience', 'design']):
        return ('60%', 'LEARN', '🟡', 'Study 5-10 hours')
    
    return None

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
    
    elif 'system design' in category_lower or 'architecture' in category_lower:
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
    
    elif 'product' in category_lower:
        return """
Product Questions Framework
├─ 1. Clarify the Product
│  ├─ What is it?
│  ├─ Who's the user?
│  └─ What problem does it solve?
│
├─ 2. Define Success
│  ├─ User metrics
│  ├─ Business metrics
│  └─ Technical metrics
│
├─ 3. Analyze Trade-offs
│  ├─ User value vs. effort
│  ├─ Short-term vs. long-term
│  └─ Build vs. buy
│
└─ 4. Recommend
   ├─ Data-driven decision
   ├─ Clear rationale
   └─ Next steps
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

def load_role_questions(role_dir):
    """Load categorized questions for a role"""
    json_path = role_dir / 'data' / 'questions_by_category.json'
    if json_path.exists():
        with open(json_path) as f:
            return json.load(f)
    return {}

def main():
    """Generate actionable strength zones"""
    
    print("💪 Generating ACTIONABLE Strength Zones...")
    print("=" * 80)
    print()
    
    # Load overlapped questions to exclude
    print("📋 Loading overlapped questions to exclude...")
    overlapped_set = load_overlapped_questions()
    print(f"   Found {len(overlapped_set)} overlapped questions (will exclude)")
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
    
    # Collect categories
    category_data = defaultdict(lambda: {
        'strength': '',
        'level': '',
        'emoji': '',
        'reason': '',
        'roles': [],
        'questions': [],
        'framework': ''
    })
    
    for role_slug, role_name in role_names.items():
        role_dir = roles_dir / role_slug
        if not role_dir.exists():
            continue
        
        questions_by_cat = load_role_questions(role_dir)
        
        for category, questions in questions_by_cat.items():
            strength_info = get_category_strength(category)
            if not strength_info:
                continue  # Skip behavioral, DSA, ML
            
            strength, level, emoji, reason = strength_info
            
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
                continue  # Skip if all questions are overlapped
            
            category_data[category]['strength'] = strength
            category_data[category]['level'] = level
            category_data[category]['emoji'] = emoji
            category_data[category]['reason'] = reason
            category_data[category]['roles'].append(role_name)
            category_data[category]['questions'].extend(unique_questions)
            category_data[category]['framework'] = get_category_framework(category)
    
    # Group by level and sort
    by_level = defaultdict(list)
    for category, data in category_data.items():
        by_level[data['level']].append((category, data))
    
    for level in by_level:
        by_level[level].sort(key=lambda x: len(x[1]['questions']), reverse=True)
    
    # Generate ONE-PAGE output
    output = []
    output.append("# 💪 YOUR STRENGTH ZONES - ACTIONABLE STUDY GUIDE")
    output.append("")
    output.append("**After mastering [⭐️ TRUE OVERLAPPED QUESTIONS](⭐️_TRUE_OVERLAPPED_QUESTIONS.md), study these next.**")
    output.append("")
    output.append("Each category shows:")
    output.append("- 🎯 ASCII framework (mental model)")
    output.append("- 📝 Specific questions (not in overlapped list)")
    output.append("- 🎭 All roles that use this (no +3 more)")
    output.append("")
    output.append("---")
    output.append("")
    
    # Summary table
    master_q = sum(len(data['questions']) for _, data in by_level.get('MASTER', []))
    strong_q = sum(len(data['questions']) for _, data in by_level.get('STRONG', []))
    focus_q = sum(len(data['questions']) for _, data in by_level.get('FOCUS', []))
    learn_q = sum(len(data['questions']) for _, data in by_level.get('LEARN', []))
    
    output.append("## 📊 What to Study Tonight")
    output.append("")
    output.append("| Priority | Categories | Questions | Study Time | Action |")
    output.append("|----------|------------|-----------|------------|--------|")
    output.append(f"| 🟢 FOCUS | {len(by_level.get('FOCUS', []))} | {focus_q} | 25-45h | **START HERE** |")
    output.append(f"| 💗 STRONG | {len(by_level.get('STRONG', []))} | {strong_q} | 2-5h | Light review |")
    output.append(f"| 💗 MASTER | {len(by_level.get('MASTER', []))} | {master_q} | 0h | You got this |")
    output.append(f"| 🟡 LEARN | {len(by_level.get('LEARN', []))} | {learn_q} | 5-10h | If time |")
    output.append("")
    output.append("---")
    output.append("")
    
    # Show categories in priority order
    levels_order = [
        ('FOCUS', '🟢 FOCUS ZONE - Start Here (70% → 90%)'),
        ('STRONG', '💗 STRONG ZONE - Light Review (80-85%)'),
        ('MASTER', '💗 MASTER ZONE - You Got This (90-95%)'),
        ('LEARN', '🟡 LEARN ZONE - If Time (60%)')
    ]
    
    for level_key, level_title in levels_order:
        if level_key not in by_level:
            continue
        
        categories = by_level[level_key]
        
        output.append(f"## {level_title}")
        output.append("")
        
        for i, (category, data) in enumerate(categories, 1):
            # Category header
            output.append(f"### {i}. {category} {data['emoji']}")
            output.append("")
            output.append(f"**Strength:** {data['strength']} | **Why:** {data['reason']}")
            output.append(f"**Questions:** {len(data['questions'])} (not in overlapped)")
            output.append(f"**Roles:** {', '.join(data['roles'])}")
            output.append("")
            
            # Framework
            output.append("**🎯 Mental Model:**")
            output.append("```")
            output.append(data['framework'].strip())
            output.append("```")
            output.append("")
            
            # Show top 5 questions + link to full list
            output.append(f"**📝 Sample Questions (showing 5 of {len(data['questions'])}):**")
            output.append("")
            for j, q in enumerate(data['questions'][:5], 1):
                output.append(f"{j}. {q}")
            output.append("")
            
            if len(data['questions']) > 5:
                # Create detail file
                detail_filename = f"details/{category.replace('/', '-').replace(' ', '_')}.md"
                output.append(f"[📋 See all {len(data['questions'])} questions]({detail_filename})")
                output.append("")
                
                # Create detail file
                detail_output = []
                detail_output.append(f"# {category} - All Questions")
                detail_output.append("")
                detail_output.append(f"**Strength:** {data['strength']} {data['emoji']}")
                detail_output.append(f"**Roles:** {', '.join(data['roles'])}")
                detail_output.append("")
                detail_output.append("**🎯 Mental Model:**")
                detail_output.append("```")
                detail_output.append(data['framework'].strip())
                detail_output.append("```")
                detail_output.append("")
                detail_output.append(f"## All {len(data['questions'])} Questions:")
                detail_output.append("")
                for j, q in enumerate(data['questions'], 1):
                    detail_output.append(f"{j}. {q}")
                detail_output.append("")
                
                # Save detail file
                detail_dir = Path(__file__).parent.parent / 'output' / 'details'
                detail_dir.mkdir(exist_ok=True)
                detail_path = detail_dir / f"{category.replace('/', '-').replace(' ', '_')}.md"
                with open(detail_path, 'w') as f:
                    f.write('\n'.join(detail_output))
            
            output.append("---")
            output.append("")
        
        output.append("")
    
    # Save main file
    output_dir = Path(__file__).parent.parent / 'output'
    output_path = output_dir / 'YOUR_STRENGTH_ZONES.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(output))
    
    print(f"✅ Generated: {output_path}")
    print()
    print("📊 Actionable Categories:")
    print(f"   🟢 FOCUS: {len(by_level.get('FOCUS', []))} categories, {focus_q} questions")
    print(f"   💗 STRONG: {len(by_level.get('STRONG', []))} categories, {strong_q} questions")
    print(f"   💗 MASTER: {len(by_level.get('MASTER', []))} categories, {master_q} questions")
    print(f"   🟡 LEARN: {len(by_level.get('LEARN', []))} categories, {learn_q} questions")
    print()
    print(f"📁 Created {sum(len(cats) for cats in by_level.values())} detail files")
    print()
    print("✅ Excluded overlapped questions (they're in ⭐️ file)")
    print("✅ All roles listed (no +3 more)")
    print("✅ ASCII frameworks for each category")
    print("✅ Specific questions to practice")

if __name__ == "__main__":
    main()
