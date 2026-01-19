#!/usr/bin/env python3
"""
Generate YOUR_STRENGTH_ZONES.md based on MBA/VC/PE background
"""
import json
from pathlib import Path
from collections import defaultdict

def get_category_strength(category_name):
    """Determine strength level based on MBA/VC/PE background"""
    category_lower = category_name.lower()
    
    # 95% - Behavioral (20 years of stories)
    if any(k in category_lower for k in ['behavioral', 'experience', 'background', 'motivation', 'career']):
        return ('95%', 'MASTER', '💗', 'Your 20 years of STAR stories')
    
    # 90% - Strategy & Business (MBA + VC/PE)
    if any(k in category_lower for k in ['strategy', 'business', 'operations', 'planning', 'finance', 'growth']):
        return ('90%', 'MASTER', '💗', 'MBA + VC/PE background')
    
    # 85% - Problem Solving & Analysis (Executive experience)
    if any(k in category_lower for k in ['problem solving', 'analytical', 'decision', 'prioritization', 'judgment']):
        return ('85%', 'STRONG', '💗', 'Executive judgment & frameworks')
    
    # 80% - Leadership & Communication (20 years)
    if any(k in category_lower for k in ['leadership', 'management', 'stakeholder', 'communication', 'collaboration', 'influence']):
        return ('80%', 'STRONG', '💗', '20 years of leadership')
    
    # 70% - SQL & Data Analysis (Focus area)
    if any(k in category_lower for k in ['sql', 'data analysis', 'metrics', 'kpi', 'dashboard', 'visualization']):
        return ('70%', 'FOCUS', '🟢', 'Study 10-20 hours')
    
    # 65% - System Design & Architecture (Focus area)
    if any(k in category_lower for k in ['system design', 'architecture', 'scalability', 'infrastructure']):
        return ('65%', 'FOCUS', '🟢', 'Study 15-25 hours')
    
    # 60% - Product & Technical (Learnable)
    if any(k in category_lower for k in ['product', 'feature', 'user experience', 'design']):
        return ('60%', 'LEARN', '🟡', 'Study 5-10 hours')
    
    # 30% - Data Structures & Algorithms (SKIP)
    if any(k in category_lower for k in ['algorithm', 'data structure', 'coding', 'leetcode', 'tree', 'graph', 'dynamic programming']):
        return ('30%', 'SKIP', '🔴', 'Not worth your time')
    
    # 25% - Machine Learning Theory (SKIP)
    if any(k in category_lower for k in ['machine learning', 'deep learning', 'neural network', 'model training', 'ml theory']):
        return ('25%', 'SKIP', '🔴', 'Not your target roles')
    
    # Default
    return ('50%', 'NEUTRAL', '⚪', 'Case by case')

def load_role_questions(role_dir):
    """Load categorized questions for a role"""
    json_path = role_dir / 'data' / 'questions_by_category.json'
    if json_path.exists():
        with open(json_path) as f:
            return json.load(f)
    return {}

def main():
    """Generate strength zones analysis"""
    
    print("💪 Generating YOUR Strength Zones...")
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
    
    # Collect categories and their strengths
    category_analysis = defaultdict(lambda: {
        'strength': '',
        'level': '',
        'emoji': '',
        'reason': '',
        'roles': set(),
        'questions': 0
    })
    
    for role_slug, role_name in role_names.items():
        role_dir = roles_dir / role_slug
        if not role_dir.exists():
            continue
        
        questions_by_cat = load_role_questions(role_dir)
        
        for category, questions in questions_by_cat.items():
            strength, level, emoji, reason = get_category_strength(category)
            
            category_analysis[category]['strength'] = strength
            category_analysis[category]['level'] = level
            category_analysis[category]['emoji'] = emoji
            category_analysis[category]['reason'] = reason
            category_analysis[category]['roles'].add(role_name)
            category_analysis[category]['questions'] += len(questions)
    
    # Group by strength level
    by_level = defaultdict(list)
    for category, data in category_analysis.items():
        by_level[data['level']].append((category, data))
    
    # Sort each level by number of questions
    for level in by_level:
        by_level[level].sort(key=lambda x: x[1]['questions'], reverse=True)
    
    # Generate output
    output = []
    output.append("# 💪 YOUR STRENGTH ZONES")
    output.append("")
    output.append("**Based on your MBA + VC/PE + 20 years executive experience**")
    output.append("")
    output.append("This analysis maps every category to YOUR specific strengths and weaknesses.")
    output.append("Focus your study time on 🟢 FOCUS areas. Skip 🔴 SKIP areas entirely.")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 📊 Quick Summary")
    output.append("")
    
    master_q = sum(data['questions'] for _, data in by_level.get('MASTER', []))
    strong_q = sum(data['questions'] for _, data in by_level.get('STRONG', []))
    focus_q = sum(data['questions'] for _, data in by_level.get('FOCUS', []))
    learn_q = sum(data['questions'] for _, data in by_level.get('LEARN', []))
    skip_q = sum(data['questions'] for _, data in by_level.get('SKIP', []))
    
    output.append(f"| Level | Strength | Categories | Questions | Study Time |")
    output.append(f"|-------|----------|------------|-----------|------------|")
    output.append(f"| 💗 MASTER | 90-95% | {len(by_level.get('MASTER', []))} | {master_q} | 0 hours (you got this!) |")
    output.append(f"| 💗 STRONG | 80-85% | {len(by_level.get('STRONG', []))} | {strong_q} | 2-5 hours (light review) |")
    output.append(f"| 🟢 FOCUS | 65-70% | {len(by_level.get('FOCUS', []))} | {focus_q} | 25-45 hours (main study) |")
    output.append(f"| 🟡 LEARN | 60% | {len(by_level.get('LEARN', []))} | {learn_q} | 5-10 hours (if time) |")
    output.append(f"| 🔴 SKIP | 25-30% | {len(by_level.get('SKIP', []))} | {skip_q} | 0 hours (ignore) |")
    output.append("")
    output.append("**Total Study Time Needed: 30-60 hours** (mostly SQL + System Design)")
    output.append("")
    output.append("---")
    output.append("")
    
    # Detailed breakdown
    levels_order = [
        ('MASTER', '💗 MASTER ZONE (90-95% Ready)', 'These are your superpowers. You already have this from 20 years of experience.'),
        ('STRONG', '💗 STRONG ZONE (80-85% Ready)', 'You have strong foundations here. Light review only.'),
        ('FOCUS', '🟢 FOCUS ZONE (65-70% Ready)', 'This is where you should spend 80% of your study time.'),
        ('LEARN', '🟡 LEARN ZONE (60% Ready)', 'Study these if you have extra time after FOCUS areas.'),
        ('SKIP', '🔴 SKIP ZONE (25-30% Ready)', 'Not worth your time. Target roles that don\'t require these.')
    ]
    
    for level_key, level_title, level_desc in levels_order:
        if level_key not in by_level:
            continue
        
        categories = by_level[level_key]
        total_q = sum(data['questions'] for _, data in categories)
        
        output.append("=" * 80)
        output.append(f"## {level_title}")
        output.append("=" * 80)
        output.append("")
        output.append(f"**{level_desc}**")
        output.append("")
        output.append(f"**Total Categories:** {len(categories)}")
        output.append(f"**Total Questions:** {total_q}")
        output.append("")
        output.append("---")
        output.append("")
        
        for i, (category, data) in enumerate(categories, 1):
            output.append(f"### {i}. {category}")
            output.append("")
            output.append(f"**Strength:** {data['strength']} {data['emoji']}")
            output.append(f"**Why:** {data['reason']}")
            output.append(f"**Questions:** {data['questions']}")
            output.append(f"**Appears in:** {len(data['roles'])} roles")
            output.append("")
            
            # Show top 3 roles
            top_roles = sorted(list(data['roles']))[:3]
            roles_str = ", ".join(top_roles)
            if len(data['roles']) > 3:
                roles_str += f" +{len(data['roles'])-3} more"
            output.append(f"**Roles:** {roles_str}")
            output.append("")
            output.append("---")
            output.append("")
        
        output.append("")
    
    # Study recommendations
    output.append("=" * 80)
    output.append("## 🎯 YOUR PERSONALIZED STUDY PLAN")
    output.append("=" * 80)
    output.append("")
    output.append("### Week 1: Focus on SQL (20-30 hours)")
    output.append("")
    output.append("**Why:** SQL appears in 6 roles and you're at 70%. Biggest ROI.")
    output.append("")
    output.append("**Topics:**")
    output.append("- JOINs (INNER, LEFT, RIGHT, FULL)")
    output.append("- Aggregations (GROUP BY, HAVING, COUNT, SUM, AVG)")
    output.append("- Window Functions (ROW_NUMBER, RANK, LAG, LEAD)")
    output.append("- Subqueries & CTEs")
    output.append("- Query Optimization")
    output.append("")
    output.append("**Resources:**")
    output.append("- LeetCode SQL (Easy + Medium)")
    output.append("- Mode Analytics SQL Tutorial")
    output.append("- Practice on your actual data")
    output.append("")
    output.append("### Week 2: System Design Basics (10-15 hours)")
    output.append("")
    output.append("**Why:** You're at 65% and this appears in Data Engineer/Technical roles.")
    output.append("")
    output.append("**Topics:**")
    output.append("- Load balancing")
    output.append("- Caching strategies")
    output.append("- Database sharding")
    output.append("- API design")
    output.append("- Scalability patterns")
    output.append("")
    output.append("**Resources:**")
    output.append("- Grokking System Design Interview")
    output.append("- System Design Primer (GitHub)")
    output.append("- Watch YouTube system design walkthroughs")
    output.append("")
    output.append("### Week 3: Light Review (5-10 hours)")
    output.append("")
    output.append("**Focus:**")
    output.append("- Review your STAR stories (2 hours)")
    output.append("- Practice SQL questions (3 hours)")
    output.append("- Mock interviews (3 hours)")
    output.append("- Product questions if time (2 hours)")
    output.append("")
    output.append("### What to SKIP:")
    output.append("")
    output.append("❌ **Data Structures & Algorithms** (30% ready)")
    output.append("   - Not worth 100+ hours to get to 70%")
    output.append("   - Target roles that don't require LeetCode")
    output.append("")
    output.append("❌ **Machine Learning Theory** (25% ready)")
    output.append("   - You're targeting analyst/strategy roles, not ML Engineer")
    output.append("   - Focus on ML business applications instead")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 💡 Key Insights")
    output.append("")
    output.append("1. **You're 80-95% ready for most categories** (your experience is powerful!)")
    output.append("2. **30-60 hours of focused study** gets you to 90%+ across the board")
    output.append("3. **SQL is your #1 priority** (20-30 hours = 70% → 90%)")
    output.append("4. **Skip DSA & ML Theory** (not worth 200+ hours for your target roles)")
    output.append("5. **Target roles that value your strengths:** BizOps, Business Analyst, Product Analyst, Chief of Staff")
    output.append("")
    output.append("---")
    output.append("")
    output.append(f"**Total Categories Analyzed:** {len(category_analysis)}")
    output.append(f"**Your Sweet Spot:** Strategy, Business, Leadership, Problem Solving")
    output.append(f"**Your Focus Area:** SQL + System Design (30-45 hours)")
    output.append(f"**Strategic Skip:** DSA + ML Theory (save 200+ hours)")
    
    # Save output
    output_dir = Path(__file__).parent.parent / 'output'
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / 'YOUR_STRENGTH_ZONES.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(output))
    
    print(f"✅ Generated: {output_path}")
    print()
    print("💪 Your Strength Distribution:")
    print(f"   💗 MASTER (90-95%): {len(by_level.get('MASTER', []))} categories, {master_q} questions")
    print(f"   💗 STRONG (80-85%): {len(by_level.get('STRONG', []))} categories, {strong_q} questions")
    print(f"   🟢 FOCUS (65-70%): {len(by_level.get('FOCUS', []))} categories, {focus_q} questions")
    print(f"   🟡 LEARN (60%): {len(by_level.get('LEARN', []))} categories, {learn_q} questions")
    print(f"   🔴 SKIP (25-30%): {len(by_level.get('SKIP', []))} categories, {skip_q} questions")
    print()
    print(f"🎯 Study Time Needed: 30-60 hours (mainly SQL + System Design)")

if __name__ == "__main__":
    main()
