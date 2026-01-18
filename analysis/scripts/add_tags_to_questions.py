#!/usr/bin/env python3
"""
Add priority tags to individual questions in question banks
Example: "1. Question text" → "1. 💗 Question text"
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

def main():
    """Add tags to Data Analyst question bank first (test)"""
    
    print("🏷️  Adding tags to individual questions...")
    print()
    
    # Start with Data Analyst
    role_dir = Path('/Users/anixlynch/Downloads/Exponent_DataAnalyst_interview/roles/data-analyst')
    tagged_file = role_dir / 'DATA-ANALYST_TAGGED_Question_Bank.md'
    
    if not tagged_file.exists():
        print(f"❌ File not found: {tagged_file}")
        return
    
    print(f"📝 Processing Data Analyst...")
    
    # Add tags to questions
    new_content = add_tags_to_questions(tagged_file)
    
    # Save updated file
    with open(tagged_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"   ✅ Updated: {tagged_file.name}")
    
    # Count tagged questions
    tagged_count = len(re.findall(r'^\d+\.\s+(💗|🟢|🔴|🟠|🟡|⚪|⚠️)', new_content, re.MULTILINE))
    print(f"   📊 Tagged {tagged_count} questions")
    
    print()
    print("✅ Data Analyst question bank updated!")
    print()
    print("Check the file to see if you like the format.")
    print("If yes, I'll apply to all 15 roles.")

if __name__ == "__main__":
    main()
