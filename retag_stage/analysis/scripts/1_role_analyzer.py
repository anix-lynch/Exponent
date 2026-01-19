#!/usr/bin/env python3
"""
SCRIPT 1: ROLE ANALYZER
Parses all question banks and extracts category statistics
"""
import os
import re
import json
from pathlib import Path
from collections import defaultdict

def parse_question_bank(filepath):
    """Parse a Question Bank markdown file and extract categories"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    role_data = {
        'total_questions': 0,
        'categories': {},
        'file_path': str(filepath)
    }
    
    # Extract total questions from header
    total_match = re.search(r'Total Questions:\s*(\d+)', content)
    if total_match:
        role_data['total_questions'] = int(total_match.group(1))
    
    # Find all category sections
    # Pattern: ===== CATEGORY NAME ===== followed by 📊 Total Questions: X
    category_pattern = r'={80}\n([A-Z\s\-&/]+)\n={80}\n\n📊 Total Questions:\s*(\d+)'
    
    for match in re.finditer(category_pattern, content):
        category_name = match.group(1).strip()
        question_count = int(match.group(2))
        role_data['categories'][category_name] = question_count
    
    return role_data

def analyze_all_roles(base_dir='roles'):
    """Walk through all role directories and analyze question banks"""
    
    roles_dir = Path(base_dir)
    all_roles = {}
    
    print("🔍 Analyzing all role question banks...\n")
    
    for role_dir in sorted(roles_dir.iterdir()):
        if not role_dir.is_dir():
            continue
        
        role_name = role_dir.name
        
        # Look for Question Bank markdown file
        question_bank_files = list(role_dir.glob('*Question_Bank.md'))
        
        if not question_bank_files:
            print(f"⚠️  {role_name}: No Question Bank found")
            continue
        
        qb_file = question_bank_files[0]
        
        try:
            role_data = parse_question_bank(qb_file)
            all_roles[role_name] = role_data
            
            print(f"✅ {role_name}")
            print(f"   Total: {role_data['total_questions']} questions")
            print(f"   Categories: {len(role_data['categories'])}")
            print()
            
        except Exception as e:
            print(f"❌ {role_name}: Error - {e}")
    
    return all_roles

def identify_universal_categories(all_roles):
    """Identify categories that appear across multiple roles"""
    
    category_frequency = defaultdict(lambda: {'count': 0, 'total_questions': 0, 'roles': []})
    
    for role_name, role_data in all_roles.items():
        for category, question_count in role_data['categories'].items():
            category_frequency[category]['count'] += 1
            category_frequency[category]['total_questions'] += question_count
            category_frequency[category]['roles'].append(role_name)
    
    # Sort by frequency
    universal_categories = []
    for category, data in sorted(category_frequency.items(), key=lambda x: x[1]['count'], reverse=True):
        universal_categories.append({
            'category': category,
            'appears_in_roles': data['count'],
            'total_questions': data['total_questions'],
            'roles': data['roles'],
            'frequency_percent': round(data['count'] / len(all_roles) * 100, 1)
        })
    
    return universal_categories

def generate_summary_report(all_roles, universal_categories):
    """Generate a human-readable summary report"""
    
    report = []
    report.append("=" * 80)
    report.append("ROLE INVENTORY ANALYSIS SUMMARY")
    report.append("=" * 80)
    report.append("")
    
    # Total stats
    total_questions = sum(role['total_questions'] for role in all_roles.values())
    total_roles = len(all_roles)
    
    report.append(f"📊 Total Roles Analyzed: {total_roles}")
    report.append(f"📊 Total Questions Across All Roles: {total_questions}")
    report.append("")
    
    # Role breakdown
    report.append("=" * 80)
    report.append("ROLES BY QUESTION COUNT")
    report.append("=" * 80)
    report.append("")
    
    sorted_roles = sorted(all_roles.items(), key=lambda x: x[1]['total_questions'], reverse=True)
    for role_name, role_data in sorted_roles:
        report.append(f"{role_name.ljust(35)} {role_data['total_questions']:>4} questions  ({len(role_data['categories'])} categories)")
    
    report.append("")
    report.append("=" * 80)
    report.append("UNIVERSAL CATEGORIES (Appear in 50%+ of roles)")
    report.append("=" * 80)
    report.append("")
    
    for cat_data in universal_categories:
        if cat_data['frequency_percent'] >= 50:
            report.append(f"{cat_data['category'].ljust(40)} {cat_data['appears_in_roles']:>2}/{total_roles} roles ({cat_data['frequency_percent']:>5.1f}%)  {cat_data['total_questions']:>4} total questions")
    
    report.append("")
    report.append("=" * 80)
    report.append("ROLE-SPECIFIC CATEGORIES (Appear in <50% of roles)")
    report.append("=" * 80)
    report.append("")
    
    for cat_data in universal_categories:
        if cat_data['frequency_percent'] < 50:
            report.append(f"{cat_data['category'].ljust(40)} {cat_data['appears_in_roles']:>2}/{total_roles} roles ({cat_data['frequency_percent']:>5.1f}%)")
    
    return "\n".join(report)

def main():
    """Main execution"""
    
    print("🚀 Starting Role Analyzer...\n")
    
    # Change to repo root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    os.chdir(repo_root)
    
    # Analyze all roles
    all_roles = analyze_all_roles('roles')
    
    # Identify universal categories
    universal_categories = identify_universal_categories(all_roles)
    
    # Save JSON output
    output_data = {
        'roles': all_roles,
        'universal_categories': universal_categories,
        'summary': {
            'total_roles': len(all_roles),
            'total_questions': sum(role['total_questions'] for role in all_roles.values())
        }
    }
    
    output_path = 'analysis/data/role_inventory.json'
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"\n✅ Saved detailed data to: {output_path}")
    
    # Generate and save summary report
    summary_report = generate_summary_report(all_roles, universal_categories)
    
    summary_path = 'analysis/output/ROLE_INVENTORY_SUMMARY.md'
    with open(summary_path, 'w') as f:
        f.write(summary_report)
    
    print(f"✅ Saved summary report to: {summary_path}")
    
    # Print summary to console
    print("\n" + summary_report)
    
    print("\n🎉 Role analysis complete!")
    print("\n📋 Next step: Run 2_comfort_scorer.py to assess your comfort level")

if __name__ == "__main__":
    main()
