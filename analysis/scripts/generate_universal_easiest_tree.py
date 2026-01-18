#!/usr/bin/env python3
"""
Generate ASCII tree of all 💗 EASIEST categories across all roles
These are universal priorities to memorize
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
    """Generate universal EASIEST categories tree"""
    
    print("🌳 Generating Universal 💗 EASIEST Categories Tree...")
    print("=" * 80)
    print()
    
    roles_dir = Path(__file__).parent.parent.parent / 'roles'
    
    # Collect all EASIEST categories across all roles
    easiest_categories = defaultdict(lambda: {'count': 0, 'roles': set(), 'questions': 0})
    
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
                easiest_categories[category]['roles'].add(role_name)
                easiest_categories[category]['questions'] += len(questions)
    
    # Group categories by theme
    themes = {
        'Behavioral & Experience': [],
        'Communication & Collaboration': [],
        'Problem Solving & Analysis': [],
        'Data & Technical Skills': [],
        'Business & Strategy': [],
        'Leadership & Management': [],
        'Ethics & Professionalism': []
    }
    
    for category, data in easiest_categories.items():
        cat_lower = category.lower()
        
        if any(k in cat_lower for k in ['behavioral', 'experience', 'background', 'motivation', 'career']):
            themes['Behavioral & Experience'].append((category, data))
        elif any(k in cat_lower for k in ['communication', 'collaboration', 'teamwork', 'stakeholder management', 'presentation']):
            themes['Communication & Collaboration'].append((category, data))
        elif any(k in cat_lower for k in ['problem solving', 'analytical', 'decision', 'conflict', 'crisis']):
            themes['Problem Solving & Analysis'].append((category, data))
        elif any(k in cat_lower for k in ['sql', 'data', 'excel', 'visualization', 'dashboard', 'metrics', 'kpi', 'reporting']):
            themes['Data & Technical Skills'].append((category, data))
        elif any(k in cat_lower for k in ['business', 'strategy', 'planning', 'operations', 'process', 'efficiency']):
            themes['Business & Strategy'].append((category, data))
        elif any(k in cat_lower for k in ['leadership', 'management', 'prioritization', 'time management', 'project']):
            themes['Leadership & Management'].append((category, data))
        elif any(k in cat_lower for k in ['ethics', 'judgment', 'discretion', 'confidential', 'trust', 'culture']):
            themes['Ethics & Professionalism'].append((category, data))
    
    # Sort by number of roles (most universal first)
    for theme in themes:
        themes[theme].sort(key=lambda x: (x[1]['count'], x[1]['questions']), reverse=True)
    
    # Generate ASCII tree
    output = []
    output.append("# 💗 UNIVERSAL EASIEST CATEGORIES - MEMORIZE THIS TREE!")
    output.append("")
    output.append("**These are your universal strengths across ALL roles.**")
    output.append("**Master these topics and you'll ace 60-100% of any interview!**")
    output.append("")
    output.append("```")
    output.append("💗 EASIEST CATEGORIES (Your Universal Strengths)")
    output.append("│")
    
    theme_count = len([t for t in themes.values() if t])
    current_theme = 0
    
    for theme_name, categories in themes.items():
        if not categories:
            continue
        
        current_theme += 1
        is_last_theme = (current_theme == theme_count)
        
        theme_prefix = "└─" if is_last_theme else "├─"
        output.append(f"│")
        output.append(f"{theme_prefix} {theme_name}")
        
        for i, (category, data) in enumerate(categories):
            is_last_cat = (i == len(categories) - 1)
            
            if is_last_theme:
                cat_prefix = "   └─" if is_last_cat else "   ├─"
                detail_prefix = "      " if is_last_cat else "   │  "
            else:
                cat_prefix = "│  └─" if is_last_cat else "│  ├─"
                detail_prefix = "│     " if is_last_cat else "│  │  "
            
            output.append(f"{cat_prefix} {category}")
            output.append(f"{detail_prefix}├─ 📊 {data['questions']} questions")
            output.append(f"{detail_prefix}├─ 🎯 {data['count']} roles")
            
            # Show top 3 roles
            top_roles = sorted(list(data['roles']))[:3]
            roles_str = ", ".join(top_roles)
            if len(data['roles']) > 3:
                roles_str += f" +{len(data['roles'])-3} more"
            output.append(f"{detail_prefix}└─ 📝 {roles_str}")
    
    output.append("```")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 📊 Summary Statistics")
    output.append("")
    
    total_questions = sum(data['questions'] for cats in themes.values() for _, data in cats)
    total_categories = sum(len(cats) for cats in themes.values())
    
    output.append(f"- **Total 💗 EASIEST Categories:** {total_categories}")
    output.append(f"- **Total Questions:** {total_questions}")
    output.append(f"- **Coverage:** These appear in {len(role_names)} roles")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 🎯 Why These Are EASIEST")
    output.append("")
    output.append("1. **Behavioral & Experience** - You have 20 years of stories!")
    output.append("2. **Communication & Collaboration** - Executive-level skills")
    output.append("3. **Problem Solving & Analysis** - MBA + VC/PE background")
    output.append("4. **Data & Technical Skills** - SQL, Excel, dashboards")
    output.append("5. **Business & Strategy** - Your core expertise")
    output.append("6. **Leadership & Management** - 20 years of leadership")
    output.append("7. **Ethics & Professionalism** - Executive maturity")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 💡 How to Use This Tree")
    output.append("")
    output.append("### Step 1: Memorize the 7 Themes")
    output.append("```")
    output.append("1. Behavioral & Experience")
    output.append("2. Communication & Collaboration")
    output.append("3. Problem Solving & Analysis")
    output.append("4. Data & Technical Skills")
    output.append("5. Business & Strategy")
    output.append("6. Leadership & Management")
    output.append("7. Ethics & Professionalism")
    output.append("```")
    output.append("")
    output.append("### Step 2: Prepare 2-3 STAR Stories Per Theme")
    output.append("- Each story should cover multiple categories in that theme")
    output.append("- Use your 20 years of experience")
    output.append("- Focus on measurable results")
    output.append("")
    output.append("### Step 3: Practice Adapting Stories")
    output.append("- Same story can answer 5-10 different questions")
    output.append("- Adjust emphasis based on the question")
    output.append("- Always tie back to business impact")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 🚀 Quick Win Strategy")
    output.append("")
    output.append("**Master these 💗 EASIEST categories and you'll be:**")
    output.append("")
    output.append("- ✅ 100% ready for Growth Marketing Manager")
    output.append("- ✅ 99% ready for BizOps Strategy")
    output.append("- ✅ 96% ready for Business Analyst")
    output.append("- ✅ 85% ready for Product Analyst")
    output.append("- ✅ 77% ready for Data Scientist")
    output.append("- ✅ 67% ready for Program Manager")
    output.append("- ✅ 64% ready for Data Analyst")
    output.append("- ✅ 64% ready for Finance Strategy")
    output.append("- ✅ 62% ready for Chief of Staff")
    output.append("- ✅ 59% ready for Product Manager")
    output.append("")
    output.append("**These categories are your competitive advantage!**")
    
    # Save output
    output_dir = Path(__file__).parent.parent / 'output'
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / 'UNIVERSAL_EASIEST_TREE.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(output))
    
    print(f"✅ Generated: {output_path}")
    print()
    print(f"📊 Found {total_categories} EASIEST categories")
    print(f"📝 Covering {total_questions} questions")
    print(f"🎯 Across {len(role_names)} roles")
    print()
    print("🌳 Tree organized into 7 themes:")
    for theme_name, categories in themes.items():
        if categories:
            print(f"   • {theme_name}: {len(categories)} categories")

if __name__ == "__main__":
    main()
