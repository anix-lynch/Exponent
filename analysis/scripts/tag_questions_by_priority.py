#!/usr/bin/env python3
"""
Tag questions with priority markers based on:
1. Universal categories (appear in 80%+ of roles)
2. Role-specific importance
3. Your background fit
"""
import json
import re
from pathlib import Path

# Universal categories (study first - appear in 80%+ roles)
# 💗 = UNIVERSAL (appears in ALL or nearly all roles - LOW HANGING FRUIT)
UNIVERSAL_CATEGORIES = {
    'BEHAVIORAL': '💗',  # UNIVERSAL - ALL 15 roles (100%)
    'SQL': '💗',  # UNIVERSAL - 12/15 roles (80%)
    'PROBLEM SOLVING': '💗',  # UNIVERSAL - 13/15 roles (87%)
    'STRATEGIC THINKING': '🟢',  # Medium - 10/15 roles (67%)
    'STRATEGY': '🟢',
    'BUSINESS ANALYSIS': '🟢',
}

# Data Engineer specific priorities (for your #1 goal)
# Don't override UNIVERSAL categories here - let them show 💗
DE_PRIORITIES = {
    'DATA PIPELINE DESIGN': '🔴',  # Critical for DE - 50 questions
    'SYSTEM DESIGN': '🟠',  # High for DE - 20 questions
    'DATA MODELING': '🟡',  # Medium for DE - 11 questions
    'DATABASE DESIGN': '🟡',  # Medium for DE
    'ETL/ELT': '🟡',  # Medium for DE
    'DATA WAREHOUSING': '🟡',  # Medium for DE
    'DATA STRUCTURES & ALGORITHMS': '⚪',  # Skip - 32 questions
    'CODING': '⚪',  # Skip - 4 questions
}

# Your background strengths
YOUR_STRENGTHS = {
    'BEHAVIORAL': '✅',  # 90% fit - 20 years experience
    'STRATEGY': '✅',  # 95% fit - MBA/VC/PE
    'STRATEGIC THINKING': '✅',
    'BUSINESS ANALYSIS': '✅',  # 85% fit
    'FINANCIAL ANALYSIS': '✅',  # 90% fit - VC/PE
    'MARKET ANALYSIS': '✅',  # 90% fit
    'PROBLEM SOLVING': '✅',  # 85% fit
}

# Categories to skip (low ROI for your goals)
SKIP_CATEGORIES = {
    'DATA STRUCTURES & ALGORITHMS': '⚠️ SKIP',
    'CODING': '⚠️ SKIP',
    'MACHINE LEARNING': '⚠️ DEFER',
    'DEEP LEARNING': '⚠️ DEFER',
}

def get_priority_tag(category, role='data-engineer'):
    """Get priority tag for a category - ONE TAG ONLY"""
    category_upper = category.upper()
    
    # Check if should skip
    if category_upper in SKIP_CATEGORIES:
        return SKIP_CATEGORIES[category_upper]
    
    # PRIORITY 1: Universal + Your Strength = EASIEST (pink heart)
    if category_upper in UNIVERSAL_CATEGORIES and category_upper in YOUR_STRENGTHS:
        return '💗'  # Universal + Strength = EASIEST WIN
    
    # PRIORITY 2: Universal (need practice) = LOW HANGING FRUIT (pink heart)
    elif category_upper in UNIVERSAL_CATEGORIES:
        return '💗'  # Universal = Master once, use everywhere
    
    # PRIORITY 3: Your strength (but not universal) = EASY (green)
    elif category_upper in YOUR_STRENGTHS:
        return '🟢'  # Your strength = Easy
    
    # PRIORITY 4: DE Critical = STUDY (red)
    elif role == 'data-engineer' and category_upper in DE_PRIORITIES:
        return DE_PRIORITIES[category_upper]
    
    # PRIORITY 5: Low priority
    else:
        return '⚪'  # Low priority

def tag_question_bank(role_name, role_dir):
    """Add priority tags to a question bank"""
    
    # Find question bank file
    qb_files = list(role_dir.glob('*Question_Bank.md'))
    if not qb_files:
        return None
    
    qb_file = qb_files[0]
    
    with open(qb_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all category sections (with or without existing tags)
    # This pattern matches category names that may already have tags
    category_pattern = r'(={80}\n)([A-Z\s\-&/()]+?)(?:\s+(?:💗|🟢|🔴|🟠|🟡|⚪|⚠️).*?)?(\n={80})'
    
    def add_tag(match):
        separator1 = match.group(1)
        category_name = match.group(2).strip()
        separator2 = match.group(3)
        
        # Get priority tag
        tag = get_priority_tag(category_name, role_name)
        
        # Add tag to category name
        tagged_name = f"{category_name} {tag}"
        
        return f"{separator1}{tagged_name}{separator2}"
    
    # Add tags to categories (replacing any existing tags)
    tagged_content = re.sub(category_pattern, add_tag, content)
    
    # Save tagged version
    tagged_file = role_dir / f"{role_name.upper()}_TAGGED_Question_Bank.md"
    with open(tagged_file, 'w', encoding='utf-8') as f:
        f.write(tagged_content)
    
    return tagged_file

def create_legend():
    """Create a legend explaining the tags"""
    legend = """
# 🏷️ QUESTION PRIORITY LEGEND

## Priority Tags (Study Order) - ONE TAG PER CATEGORY

💗 **EASIEST** - Universal (80%+ roles) - Master once, use everywhere!
   - Includes categories you're already strong in
   - Behavioral (15/15 roles, you're 90% ready)
   - SQL (12/15 roles, need practice)
   - Problem Solving (13/15 roles, you're 85% ready)

🟢 **EASY** - Your strength (85%+ fit from MBA/VC/PE)
   - Strategy, Business Analysis, Financial Analysis
   - Just review, you're already ready

🔴 **STUDY** - Critical for Data Engineer (your #1 goal)
   - Data Pipeline Design (50q - 28% of DE role)
   - Focused study needed

🟠 **PRACTICE** - Important for DE or multiple roles
   - System Design, Data Modeling
   - Need some practice

🟡 **OPTIONAL** - Medium priority, if time permits
   - Nice to have, not critical

⚪ **LOW** - Lower priority
   - Study last if time

⚠️ **SKIP** - Strategic ignore, low ROI
   - Data Structures & Algorithms (32q = 18% of DE)
   - Coding (4q = 2% of DE)
   - Save 6+ hours by skipping these!

---

## How to Use This

### For Data Engineer (Your #1 Goal):

**Study in this order:**

1. **💗 EASIEST** (Universal - master once, use everywhere!)
   - Behavioral (15/15 roles, you're 90% ready - just review)
   - SQL (12/15 roles - practice 15 problems)
   - Problem Solving (13/15 roles, you're 85% ready - just review)

2. **🔴 STUDY** (Critical for DE, need focused study)
   - Data Pipeline Design (50 questions - 28% of DE role)

3. **🟠 PRACTICE** (Important for DE)
   - System Design (20 questions)
   - Data Modeling (11 questions)

3. **🟠 Categories** (High priority)
   - Data Modeling
   - Database Design

4. **🟡 Categories** (Medium priority, if time permits)
   - ETL/ELT
   - Data Warehousing

5. **⚠️ SKIP** (Strategic ignore)
   - Data Structures & Algorithms (32 questions - 18%)
   - Coding (4 questions - 2%)

### For Quick Win Roles (Chief of Staff, BizOps):

**Focus on:**
- 💗 Behavioral (easiest - just review)
- 💗 Problem Solving (easiest - just review)
- 🟢 Strategy (easy - your strength)
- 🟢 Business Analysis (easy - your strength)

You're 85%+ ready for these roles NOW!

**Bonus**: Master 💗 categories (8 hours) = ready for 12+ roles!

---

## Time Allocation (20 hours total)

Based on ONE TAG per category:
- 💗 EASIEST: 8 hours (universal - master once, use everywhere)
  - Behavioral (2 hours review)
  - SQL (6 hours practice)
  
- 🔴 STUDY: 8 hours (DE critical - focused study)
  - Data Pipeline Design (6 hours)
  - Other critical categories (2 hours)
  
- 🟠 PRACTICE: 3 hours (important for DE)
  - System Design, Data Modeling
  
- 🟡 OPTIONAL: 1 hour (if time permits)

- ⚠️ SKIP: 0 hours (strategic ignore - save 6+ hours!)

**KEY INSIGHT**: 
- 8 hours on 💗 = ready for 12+ roles!
- 8 hours on 🔴 = ready for Data Engineer!
- Total: 16 hours to be competitive everywhere!

---

**Use the tagged question banks to prioritize your study time!**
"""
    return legend

def main():
    """Tag all question banks"""
    
    print("🏷️  Tagging questions with priority markers...\n")
    
    # Change to repo root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    
    roles_dir = repo_root / 'roles'
    
    tagged_files = []
    
    # Tag Data Engineer first (priority)
    de_dir = roles_dir / 'data-engineer'
    if de_dir.exists():
        print("🎯 Tagging Data Engineer (YOUR #1 GOAL)...")
        tagged_file = tag_question_bank('data-engineer', de_dir)
        if tagged_file:
            tagged_files.append(('Data Engineer', tagged_file))
            print(f"   ✅ Created: {tagged_file.name}\n")
    
    # Tag other roles
    for role_dir in sorted(roles_dir.iterdir()):
        if not role_dir.is_dir() or role_dir.name == 'data-engineer':
            continue
        
        role_name = role_dir.name
        print(f"📝 Tagging {role_name}...")
        
        tagged_file = tag_question_bank(role_name, role_dir)
        if tagged_file:
            tagged_files.append((role_name, tagged_file))
            print(f"   ✅ Created: {tagged_file.name}")
    
    # Create legend
    legend_path = repo_root / 'analysis' / 'output' / 'PRIORITY_LEGEND.md'
    with open(legend_path, 'w') as f:
        f.write(create_legend())
    
    print(f"\n✅ Created priority legend: {legend_path}")
    
    # Summary
    print("\n" + "="*70)
    print("📊 SUMMARY")
    print("="*70)
    print(f"Tagged {len(tagged_files)} role question banks")
    print(f"\nTagged files created in each role's directory:")
    for role, file in tagged_files:
        print(f"  • {role}: {file.name}")
    
    print(f"\n📖 See PRIORITY_LEGEND.md for tag explanations")
    print("\n🎯 Start with Data Engineer tagged questions!")
    print("   Focus on: 🔴 and 🟠 tags, skip ⚠️ tags")

if __name__ == "__main__":
    main()
