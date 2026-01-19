#!/usr/bin/env python3
"""
Strikethrough incomplete questions (coding problem titles without context)
These are questions that are just titles like "Employee Earnings" or "Merge Intervals"
"""
import re
from pathlib import Path

# Patterns that indicate an incomplete question (just a title)
INCOMPLETE_PATTERNS = [
    r'^[A-Z][a-z]+ [A-Z][a-z]+\.?$',  # "Employee Earnings" or "Instagram Likes"
    r'^[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+\.?$',  # "Top Earning Employees"
    r'^[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+\.?$',  # "Top Salaries by Department"
    r'^[A-Z][a-z]+ [A-Z][a-z]+s\.?$',  # "Merge Intervals"
    r'^[A-Z][A-Z]+ [A-Z][a-z]+\.?$',  # "SQL Query"
]

# Known incomplete questions (coding problems without descriptions)
KNOWN_INCOMPLETE = {
    'Employee Earnings',
    'Instagram Likes',
    'Top Earning Employees',
    'Top Salaries by Department',
    'Merge Intervals',
    'Most Recent Transaction',
    'High Volume Low Success',
    'Calculate Test Scores',
    'Post Success By Age Group',
    'Session Data Analysis',
    'Monthly Post Success Analysis',
    'Analyze Monthly Customer Transactions',
    'Find Campaign Purchases',
    'Fraudulent Transactions',
    'Convert Biased Coin to Fair Coin',
    'Rotating the Box',
    'Generate Parentheses',
    'Roman to Integer',
    'Sliding Window Maximum',
    'Set Matrix Zeroes',
    'Squares of sorted array',
    'Search in rotated sorted array',
    'Serialize and deserialize binary tree',
    'Linked List Cycle',
}

def is_incomplete_question(question_text):
    """Check if a question is just a title without context"""
    
    # Remove leading emoji if present
    clean_text = re.sub(r'^[💗🟢🔴🟠🟡⚪⚠️]\s+', '', question_text).strip()
    
    # Check if it's in known incomplete list
    if clean_text.rstrip('.') in KNOWN_INCOMPLETE:
        return True
    
    # Check if it matches incomplete patterns
    for pattern in INCOMPLETE_PATTERNS:
        if re.match(pattern, clean_text):
            # Additional check: if it's very short (< 4 words) and has no question mark or "how/what/why"
            words = clean_text.split()
            if len(words) <= 4 and '?' not in clean_text:
                if not any(word.lower() in ['how', 'what', 'why', 'when', 'where', 'should', 'would', 'could'] for word in words):
                    return True
    
    return False

def strikethrough_incomplete_questions(file_path):
    """Add strikethrough to incomplete questions"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    incomplete_count = 0
    
    for line in lines:
        # Check if this is a numbered question
        question_match = re.match(r'^(\d+)\.\s+(💗|🟢|🔴|🟠|🟡|⚪|⚠️)?\s*(.+)$', line)
        
        if question_match:
            number = question_match.group(1)
            emoji = question_match.group(2) or ''
            question_text = question_match.group(3)
            
            # Check if incomplete
            if is_incomplete_question(question_text):
                # Add strikethrough
                if emoji:
                    new_line = f"{number}. {emoji} ~~{question_text}~~ *(incomplete - coding problem title only)*"
                else:
                    new_line = f"{number}. ~~{question_text}~~ *(incomplete - coding problem title only)*"
                
                new_lines.append(new_line)
                incomplete_count += 1
            else:
                # Keep as is
                new_lines.append(line)
        else:
            # Not a question, keep as is
            new_lines.append(line)
    
    return '\n'.join(new_lines), incomplete_count

def main():
    """Strikethrough incomplete questions in all question banks"""
    
    print("🔍 Finding and striking through incomplete questions...")
    print("=" * 70)
    print()
    
    repo_root = Path('/Users/anixlynch/Downloads/Exponent_DataAnalyst_interview')
    roles_dir = repo_root / 'roles'
    
    total_roles = 0
    total_incomplete = 0
    
    for role_dir in sorted(roles_dir.iterdir()):
        if not role_dir.is_dir():
            continue
        
        role_name = role_dir.name.replace('-', ' ').title()
        
        # Process both original and tagged files
        files_to_process = []
        files_to_process.extend(role_dir.glob('*Question_Bank.md'))
        
        if not files_to_process:
            continue
        
        role_incomplete = 0
        
        for file_path in files_to_process:
            if 'TAGGED' in file_path.name.upper():
                continue  # Skip tagged files for now
            
            new_content, incomplete_count = strikethrough_incomplete_questions(file_path)
            
            if incomplete_count > 0:
                # Save updated file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                role_incomplete += incomplete_count
        
        if role_incomplete > 0:
            print(f"📝 {role_name}: {role_incomplete} incomplete questions marked")
            total_roles += 1
            total_incomplete += role_incomplete
    
    print()
    print("=" * 70)
    print(f"✅ COMPLETE!")
    print(f"   • Updated {total_roles} roles")
    print(f"   • Marked {total_incomplete} incomplete questions")
    print()
    print("Incomplete questions now show:")
    print("  ~~Employee Earnings~~ *(incomplete - coding problem title only)*")
    print()
    print("These are coding problems that need full problem descriptions.")

if __name__ == "__main__":
    main()
