#!/usr/bin/env python3
"""
Add priority tags to individual questions in ALL question banks
Updates BOTH the original Question_Bank.md AND the TAGGED version
"""
import re
from pathlib import Path

def add_tags_to_questions(file_path):
    """Add tags to each question based on its category"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all category sections with their tags
    # Pattern: ====\nCATEGORY TAG\n====
    category_pattern = r'={80}\n([A-Z\s\-&/()]+)\s+(💗|🟢|🔴|🟠|🟡|⚪|⚠️[^\n]*)\n={80}'
    
    new_content = []
    current_tag = None
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a category header
        if line == '=' * 80 and i + 2 < len(lines):
            # Get the category line
            category_line = lines[i + 1]
            
            # Extract tag from category line
            tag_match = re.search(r'(💗|🟢|🔴|🟠|🟡|⚪|⚠️[^\s]*)', category_line)
            if tag_match:
                current_tag = tag_match.group(1).split()[0]  # Get just the emoji
            
            # Add the separator and category line
            new_content.append(line)
            new_content.append(lines[i + 1])
            new_content.append(lines[i + 2])  # Bottom separator
            i += 3
            continue
        
        # Check if this is a numbered question
        question_match = re.match(r'^(\d+)\.\s+(.+)$', line)
        if question_match and current_tag:
            number = question_match.group(1)
            question_text = question_match.group(2)
            
            # Check if tag already exists
            if not re.match(r'^(💗|🟢|🔴|🟠|🟡|⚪|⚠️)', question_text):
                # Add tag after the number
                new_line = f"{number}. {current_tag} {question_text}"
                new_content.append(new_line)
            else:
                # Tag already exists, keep as is
                new_content.append(line)
        else:
            # Not a question, keep as is
            new_content.append(line)
        
        i += 1
    
    return '\n'.join(new_content)

def process_role(role_dir):
    """Process both question bank files for a role"""
    role_name = role_dir.name
    
    # Find both question bank files
    original_files = list(role_dir.glob('*Question_Bank.md'))
    original_files = [f for f in original_files if 'TAGGED' not in f.name.upper()]
    
    tagged_files = list(role_dir.glob('*_TAGGED_Question_Bank.md'))
    
    files_to_process = original_files + tagged_files
    
    if not files_to_process:
        return 0
    
    total_tagged = 0
    
    for file_path in files_to_process:
        # Add tags to questions
        new_content = add_tags_to_questions(file_path)
        
        # Save updated file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # Count tagged questions
        tagged_count = len(re.findall(r'^\d+\.\s+(💗|🟢|🔴|🟠|🟡|⚪|⚠️)', new_content, re.MULTILINE))
        
        print(f"   ✅ {file_path.name}: {tagged_count} questions tagged")
        total_tagged += tagged_count
    
    return total_tagged

def main():
    """Add tags to ALL question banks (both original and tagged versions)"""
    
    print("🏷️  Adding emoji tags to ALL question banks...")
    print("=" * 70)
    print()
    
    repo_root = Path('/Users/anixlynch/Downloads/Exponent_DataAnalyst_interview')
    roles_dir = repo_root / 'roles'
    
    total_roles = 0
    total_questions = 0
    
    for role_dir in sorted(roles_dir.iterdir()):
        if not role_dir.is_dir():
            continue
        
        role_name = role_dir.name.replace('-', ' ').title()
        print(f"📝 {role_name}...")
        
        tagged = process_role(role_dir)
        
        if tagged > 0:
            total_roles += 1
            total_questions += tagged
            print()
    
    print("=" * 70)
    print(f"✅ COMPLETE!")
    print(f"   • Updated {total_roles} roles")
    print(f"   • Tagged {total_questions} total questions")
    print()
    print("Now ALL question banks (original + tagged) have emoji tags on each question!")
    print()
    print("Check GitHub to see the updated files:")
    print("https://github.com/anix-lynch/Exponent/tree/master/roles")

if __name__ == "__main__":
    main()
