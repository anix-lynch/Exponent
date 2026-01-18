#!/usr/bin/env python3
"""
Analyze tag distribution across ALL 15 roles
Shows which roles have the most 💗, 🟢, 🔴 tags
"""
import re
from pathlib import Path
from collections import defaultdict

def analyze_role_tags(role_dir):
    """Count tags in a role's tagged question bank"""
    
    # Find tagged question bank
    tagged_files = list(role_dir.glob('*_TAGGED_Question_Bank.md'))
    if not tagged_files:
        return None
    
    with open(tagged_files[0], 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count tags
    tags = {
        '💗': 0,  # EASIEST
        '🟢': 0,  # EASY
        '🔴': 0,  # STUDY
        '🟠': 0,  # PRACTICE
        '🟡': 0,  # OPTIONAL
        '⚪': 0,  # LOW
        '⚠️': 0,  # SKIP
    }
    
    # Find all category headers with tags
    # Pattern handles multiple formats:
    # - "📊 Total Questions: 55"
    # - "📊 **Total Questions**: 55"
    # - "Total Questions: 101 across 13 categories"
    # - "Total Questions: 1,710" (with commas)
    category_pattern = r'={80}\n([A-Z\s\-&/()]+)\s+(💗|🟢|🔴|🟠|🟡|⚪|⚠️.*?)\n={80}\n\n📊\s+\*?\*?Total Questions\*?\*?:\s*([\d,]+)'
    
    for match in re.finditer(category_pattern, content):
        category = match.group(1).strip()
        tag = match.group(2).strip()
        question_count_str = match.group(3).replace(',', '')
        question_count = int(question_count_str)
        
        # Get base tag (handle "⚠️ SKIP" format)
        base_tag = tag.split()[0] if ' ' in tag else tag
        
        if base_tag in tags:
            tags[base_tag] += question_count
    
    # Get total questions (handle multiple formats, including commas like "1,710")
    total_match = re.search(r'\*?\*?Total Questions?\*?\*?:\s*([\d,]+)', content)
    if total_match:
        total_str = total_match.group(1).replace(',', '')
        total_questions = int(total_str)
    else:
        total_questions = sum(tags.values())
    
    # If no categories found but file has content, try alternate format
    if sum(tags.values()) == 0 and len(content) > 1000:
        # Try without the 📊 emoji
        alt_pattern = r'={80}\n([A-Z\s\-&/()]+)\s+(💗|🟢|🔴|🟠|🟡|⚪|⚠️.*?)\n={80}'
        for match in re.finditer(alt_pattern, content):
            # Find the question count after this category
            category_end = match.end()
            next_section = content[category_end:category_end+500]
            count_match = re.search(r'\*?\*?Total Questions?\*?\*?:\s*([\d,]+)', next_section)
            if count_match:
                tag = match.group(2).strip().split()[0]
                if tag in tags:
                    count_str = count_match.group(1).replace(',', '')
                    tags[tag] += int(count_str)
    
    return {
        'tags': tags,
        'total': total_questions
    }

def main():
    """Analyze all roles and create summary"""
    
    print("🔍 Analyzing tag distribution across ALL 15 roles...\n")
    
    # Change to repo root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    roles_dir = repo_root / 'roles'
    
    # Analyze all roles
    role_data = {}
    for role_dir in sorted(roles_dir.iterdir()):
        if not role_dir.is_dir():
            continue
        
        role_name = role_dir.name
        data = analyze_role_tags(role_dir)
        
        if data:
            role_data[role_name] = data
            print(f"✅ {role_name}: {data['total']} questions")
    
    # Create summary report
    summary = []
    summary.append("=" * 100)
    summary.append("📊 TAG DISTRIBUTION ACROSS ALL 15 ROLES")
    summary.append("=" * 100)
    summary.append("")
    summary.append("Which roles have the most 💗 EASIEST, 🟢 EASY, and 🔴 STUDY questions?")
    summary.append("Use this to decide which roles to apply to first!")
    summary.append("")
    summary.append("=" * 100)
    summary.append("")
    
    # Sort roles by "easiest" score (💗 + 🟢)
    role_scores = []
    for role_name, data in role_data.items():
        easiest = data['tags']['💗']
        easy = data['tags']['🟢']
        study = data['tags']['🔴']
        practice = data['tags']['🟠']
        skip = data['tags']['⚠️']
        total = data['total']
        
        easiest_score = easiest + easy
        easiest_pct = (easiest_score / total * 100) if total > 0 else 0
        
        role_scores.append({
            'name': role_name,
            'total': total,
            'easiest': easiest,
            'easy': easy,
            'study': study,
            'practice': practice,
            'skip': skip,
            'easiest_score': easiest_score,
            'easiest_pct': easiest_pct
        })
    
    # Sort by easiest percentage (highest first)
    role_scores.sort(key=lambda x: x['easiest_pct'], reverse=True)
    
    # Print summary table
    summary.append(f"{'ROLE'.ljust(35)} {'TOTAL'.rjust(5)} │ {'💗'.rjust(4)} {'🟢'.rjust(4)} {'🔴'.rjust(4)} {'🟠'.rjust(4)} {'⚠️'.rjust(4)} │ {'READY'.rjust(6)}")
    summary.append("─" * 100)
    
    for role in role_scores:
        name = role['name'].replace('-', ' ').title()
        total = role['total']
        easiest = role['easiest']
        easy = role['easy']
        study = role['study']
        practice = role['practice']
        skip = role['skip']
        ready_pct = role['easiest_pct']
        
        # Add indicator for top roles
        if ready_pct >= 70:
            indicator = "🎯"
        elif ready_pct >= 50:
            indicator = "🟡"
        else:
            indicator = "  "
        
        summary.append(
            f"{indicator} {name.ljust(32)} {total:>5} │ "
            f"{easiest:>4} {easy:>4} {study:>4} {practice:>4} {skip:>4} │ "
            f"{ready_pct:>5.0f}%"
        )
    
    summary.append("")
    summary.append("=" * 100)
    summary.append("LEGEND:")
    summary.append("💗 EASIEST  - Universal, master once use everywhere")
    summary.append("🟢 EASY     - Your strength (MBA/VC/PE), just review")
    summary.append("🔴 STUDY    - Need focused study")
    summary.append("🟠 PRACTICE - Need some practice")
    summary.append("⚠️ SKIP     - Strategic ignore")
    summary.append("")
    summary.append("READY % = (💗 + 🟢) / Total")
    summary.append("🎯 = 70%+ ready (apply immediately)")
    summary.append("🟡 = 50-70% ready (study then apply)")
    summary.append("")
    summary.append("=" * 100)
    summary.append("")
    summary.append("🎯 RECOMMENDATION:")
    summary.append("")
    summary.append("Apply to roles with:")
    summary.append("1. Highest 💗 + 🟢 count (you're most ready)")
    summary.append("2. Lowest 🔴 count (less study needed)")
    summary.append("3. Lowest ⚠️ count (less to skip)")
    summary.append("")
    summary.append("Start with roles marked 🎯 (70%+ ready)!")
    summary.append("")
    
    # Save summary
    output_path = repo_root / 'analysis' / 'output' / 'ALL_ROLES_TAG_SUMMARY.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(summary))
    
    print(f"\n✅ Summary saved to: {output_path}")
    
    # Print to console
    print("\n" + '\n'.join(summary))
    
    # Print top 5 recommendations
    print("\n" + "=" * 100)
    print("🎯 TOP 5 ROLES TO APPLY TO (Most 💗 + 🟢):")
    print("=" * 100)
    for i, role in enumerate(role_scores[:5], 1):
        name = role['name'].replace('-', ' ').title()
        ready_pct = role['easiest_pct']
        easiest = role['easiest']
        easy = role['easy']
        print(f"{i}. {name.ljust(35)} {ready_pct:>5.0f}% ready (💗 {easiest} + 🟢 {easy})")

if __name__ == "__main__":
    main()
