#!/usr/bin/env python3
"""
Extract questions from the most universal 💗 EASIEST categories
These are the highest probability questions across all roles
"""
import json
from pathlib import Path
from collections import defaultdict

def load_role_questions(role_dir):
    """Load categorized questions for a role"""
    json_path = role_dir / 'data' / 'questions_by_category.json'
    if json_path.exists():
        with open(json_path) as f:
            return json.load(f)
    return {}

def get_category_priority(category_name):
    """Determine priority based on category name"""
    category_lower = category_name.lower()
    
    # 💗 EASIEST - Universal skills everyone has
    easiest_keywords = [
        'behavioral', 'experience', 'background', 'motivation', 'career',
        'communication', 'collaboration', 'teamwork', 'leadership',
        'problem solving', 'analytical', 'decision making',
        'stakeholder', 'presentation', 'conflict resolution',
        'time management', 'prioritization', 'project management',
        'data analysis', 'metrics', 'kpi', 'reporting',
        'sql', 'excel', 'visualization', 'dashboard',
        'business', 'strategy', 'planning', 'operations',
        'process improvement', 'efficiency', 'optimization',
        'customer', 'user', 'client', 'stakeholder management',
        'ethics', 'judgment', 'discretion', 'confidential',
        'role understanding', 'responsibilities', 'growth',
        'culture', 'values', 'trust building'
    ]
    
    for keyword in easiest_keywords:
        if keyword in category_lower:
            return '💗'
    
    return None

def main():
    """Extract overlapped questions from most universal categories"""
    
    print("🔍 Extracting Overlapped Questions (Highest Probability)...")
    print("=" * 80)
    print()
    
    roles_dir = Path(__file__).parent.parent.parent / 'roles'
    
    # Collect all EASIEST categories across all roles
    easiest_categories = defaultdict(lambda: {'count': 0, 'roles': {}, 'questions': []})
    
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
    
    for role_slug, role_name in role_names.items():
        role_dir = roles_dir / role_slug
        if not role_dir.exists():
            continue
        
        questions_by_cat = load_role_questions(role_dir)
        
        for category, questions in questions_by_cat.items():
            priority = get_category_priority(category)
            if priority == '💗':
                easiest_categories[category]['count'] += 1
                easiest_categories[category]['roles'][role_name] = len(questions)
                
                # Add questions with role info
                for q in questions:
                    easiest_categories[category]['questions'].append({
                        'question': q,
                        'role': role_name,
                        'category': category
                    })
    
    # Find top 6 most universal categories (appear in most roles)
    sorted_categories = sorted(
        easiest_categories.items(),
        key=lambda x: (x[1]['count'], len(x[1]['questions'])),
        reverse=True
    )
    
    top_6_categories = sorted_categories[:6]
    
    print("📊 Top 6 Most Universal 💗 EASIEST Categories:")
    print()
    for i, (category, data) in enumerate(top_6_categories, 1):
        print(f"{i}. {category}")
        print(f"   • Appears in {data['count']} roles")
        print(f"   • {len(data['questions'])} total questions")
        print(f"   • Roles: {', '.join(sorted(data['roles'].keys())[:3])}...")
        print()
    
    # Generate markdown output
    output = []
    output.append("# 🎯 OVERLAPPED QUESTIONS - Highest Probability Across All Roles")
    output.append("")
    output.append("**These are the questions you're MOST LIKELY to face in ANY interview.**")
    output.append("")
    output.append("These 6 categories appear in the most roles and cover the most questions.")
    output.append("Master these and you'll be prepared for 60-100% of any interview!")
    output.append("")
    output.append("---")
    output.append("")
    
    # Summary table
    output.append("## 📊 Quick Summary")
    output.append("")
    output.append("| Category | Roles | Questions | Your Advantage |")
    output.append("|----------|-------|-----------|----------------|")
    
    for category, data in top_6_categories:
        roles_count = data['count']
        questions_count = len(data['questions'])
        advantage = "20 years of stories!" if 'behavioral' in category.lower() else \
                   "6 roles use this!" if 'sql' in category.lower() else \
                   "MBA + VC/PE background" if 'strategy' in category.lower() else \
                   "Executive experience" if 'stakeholder' in category.lower() else \
                   "3 roles, core skill" if 'analytical' in category.lower() else \
                   "Your daily work"
        output.append(f"| {category} | {roles_count} | {questions_count} | {advantage} |")
    
    total_questions = sum(len(data['questions']) for _, data in top_6_categories)
    output.append(f"| **TOTAL** | **All 15** | **{total_questions}** | **Your sweet spot!** |")
    output.append("")
    output.append("---")
    output.append("")
    
    # Detailed questions by category
    for i, (category, data) in enumerate(top_6_categories, 1):
        output.append("=" * 80)
        output.append(f"## {i}. {category.upper()}")
        output.append("=" * 80)
        output.append("")
        output.append(f"**📊 Appears in:** {data['count']} roles")
        output.append(f"**📝 Total Questions:** {len(data['questions'])}")
        output.append("")
        
        # Show which roles use this category
        output.append("**🎯 Used by these roles:**")
        for role, count in sorted(data['roles'].items(), key=lambda x: x[1], reverse=True):
            output.append(f"- {role} ({count} questions)")
        output.append("")
        
        # Add "why this matters"
        if 'behavioral' in category.lower():
            output.append("**💡 Why this matters:**")
            output.append("Every single role asks behavioral questions. These are your STAR stories from 20 years of experience.")
            output.append("Prepare 10-15 strong STAR stories and you can answer ANY behavioral question.")
        elif 'sql' in category.lower():
            output.append("**💡 Why this matters:**")
            output.append("SQL appears in 6 different roles! Master SQL and you unlock multiple career paths.")
            output.append("Focus on: JOINs, aggregations, window functions, query optimization.")
        elif 'stakeholder' in category.lower():
            output.append("**💡 Why this matters:**")
            output.append("Executive-level communication is your superpower with 20 years of experience.")
            output.append("These questions let you showcase your ability to influence and align teams.")
        elif 'analytical' in category.lower():
            output.append("**💡 Why this matters:**")
            output.append("Your MBA + VC/PE background gives you strong analytical frameworks.")
            output.append("Use frameworks like: MECE, 5 Whys, Root Cause Analysis, Cost-Benefit.")
        elif 'strategy' in category.lower():
            output.append("**💡 Why this matters:**")
            output.append("Strategy questions appear in 6 roles! Your VC/PE experience is perfect here.")
            output.append("Use frameworks like: Porter's 5 Forces, SWOT, Business Model Canvas.")
        elif 'problem solving' in category.lower():
            output.append("**💡 Why this matters:**")
            output.append("Problem solving appears in 4 roles and tests your executive judgment.")
            output.append("Use structured approaches: Define → Analyze → Options → Decide → Execute.")
        
        output.append("")
        output.append("---")
        output.append("")
        
        # Group questions by role
        questions_by_role = defaultdict(list)
        for q_data in data['questions']:
            questions_by_role[q_data['role']].append(q_data['question'])
        
        output.append("### 📝 All Questions:")
        output.append("")
        
        for role in sorted(questions_by_role.keys()):
            questions = questions_by_role[role]
            output.append(f"#### {role} ({len(questions)} questions)")
            output.append("")
            for j, question in enumerate(questions, 1):
                output.append(f"{j}. {question}")
            output.append("")
        
        output.append("")
    
    # Add study guide at the end
    output.append("=" * 80)
    output.append("## 🎓 HOW TO MASTER THESE OVERLAPPED QUESTIONS")
    output.append("=" * 80)
    output.append("")
    output.append("### Step 1: Prepare STAR Stories (2-3 hours)")
    output.append("")
    output.append("For **Behavioral** questions, prepare 10-15 STAR stories covering:")
    output.append("- Leadership & influence")
    output.append("- Problem solving & crisis management")
    output.append("- Stakeholder management & communication")
    output.append("- Data-driven decision making")
    output.append("- Strategic thinking & planning")
    output.append("- Failure & learning")
    output.append("- Team collaboration")
    output.append("")
    output.append("### Step 2: Practice SQL (1-2 hours)")
    output.append("")
    output.append("Focus on these SQL topics:")
    output.append("- JOINs (INNER, LEFT, RIGHT, FULL)")
    output.append("- Aggregations (GROUP BY, HAVING)")
    output.append("- Window functions (ROW_NUMBER, RANK, LAG, LEAD)")
    output.append("- Subqueries & CTEs")
    output.append("- Query optimization")
    output.append("")
    output.append("### Step 3: Review Frameworks (1 hour)")
    output.append("")
    output.append("Memorize these frameworks:")
    output.append("- **Analytical:** MECE, 5 Whys, Root Cause Analysis")
    output.append("- **Strategy:** Porter's 5 Forces, SWOT, Business Model Canvas")
    output.append("- **Problem Solving:** Define → Analyze → Options → Decide → Execute")
    output.append("- **Stakeholder:** Identify → Prioritize → Engage → Align → Monitor")
    output.append("")
    output.append("### Step 4: Practice Adapting (ongoing)")
    output.append("")
    output.append("- Use the same STAR story for multiple questions")
    output.append("- Adjust emphasis based on what they're testing")
    output.append("- Always tie back to business impact")
    output.append("- Quantify results when possible")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 🚀 Why These Questions Matter")
    output.append("")
    output.append("**These 6 categories represent the CORE of what every interviewer wants to know:**")
    output.append("")
    output.append("1. **Behavioral** - Can you do the job? (past performance)")
    output.append("2. **SQL** - Do you have technical skills? (hands-on ability)")
    output.append("3. **Strategy** - Can you think big picture? (strategic thinking)")
    output.append("4. **Stakeholder Management** - Can you influence? (soft skills)")
    output.append("5. **Analytical** - Can you solve problems? (frameworks)")
    output.append("6. **Problem Solving** - How do you approach challenges? (process)")
    output.append("")
    output.append("**Master these 6 and you're 60-100% ready for ANY role!**")
    output.append("")
    output.append("---")
    output.append("")
    output.append(f"**Total Questions:** {total_questions}")
    output.append(f"**Coverage:** All 15 roles")
    output.append(f"**Your Readiness:** These are ALL 💗 EASIEST for you!")
    
    # Save output
    output_dir = Path(__file__).parent.parent / 'output'
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / 'OVERLAPPED_QUESTIONS.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(output))
    
    print("=" * 80)
    print(f"✅ Generated: {output_path}")
    print()
    print(f"📊 Top 6 Most Universal Categories:")
    for i, (category, data) in enumerate(top_6_categories, 1):
        print(f"   {i}. {category}: {data['count']} roles, {len(data['questions'])} questions")
    print()
    print(f"📝 Total Questions: {total_questions}")
    print(f"🎯 Coverage: All 15 roles")
    print()
    print("💡 These are the HIGHEST PROBABILITY questions you'll face!")

if __name__ == "__main__":
    main()
