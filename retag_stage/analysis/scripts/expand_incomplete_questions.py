#!/usr/bin/env python3
"""
Expand incomplete questions with full problem descriptions
"""
import re
from pathlib import Path

# Known SQL/coding problems with their full descriptions
QUESTION_EXPANSIONS = {
    'Employee Earnings': 'Write a SQL query to find the employees who earn more than their managers.',
    
    'Instagram Likes': 'Write a SQL query to find the number of likes for each Instagram post in the last 30 days.',
    
    'Top Earning Employees': 'Write a SQL query to find the top 3 highest-earning employees in each department.',
    
    'Top Salaries by Department': 'Write a SQL query to find the employee with the highest salary in each department.',
    
    'Most Recent Transaction': 'Write a SQL query to find the most recent transaction for each customer.',
    
    'High Volume Low Success': 'Write a SQL query to identify products with high order volume but low success rate (< 50% fulfillment).',
    
    'Calculate Test Scores': 'Write a SQL query to calculate the average test score for each student, excluding their lowest score.',
    
    'Post Success By Age Group': 'Write a SQL query to analyze post engagement metrics (likes, comments, shares) grouped by user age ranges (18-24, 25-34, 35-44, 45+).',
    
    'Session Data Analysis': 'Write a SQL query to analyze user session data: calculate average session duration, pages per session, and bounce rate by traffic source.',
    
    'Monthly Post Success Analysis': 'Write a SQL query to calculate monthly post engagement metrics: total posts, average likes per post, engagement rate, and month-over-month growth.',
    
    'Analyze Monthly Customer Transactions': 'Write a SQL query to analyze customer transaction patterns: monthly revenue, average order value, customer retention rate, and identify top 10% customers by spend.',
    
    'Find Campaign Purchases': 'Write a SQL query to find all purchases made within 7 days of a marketing campaign click, grouped by campaign.',
    
    'Fraudulent Transactions': 'Write a SQL query to identify potentially fraudulent transactions: multiple transactions from same card in different cities within 1 hour, or transactions above $10,000.',
    
    'Merge Intervals': 'Given a collection of intervals, merge all overlapping intervals. Example: [[1,3],[2,6],[8,10]] → [[1,6],[8,10]]',
    
    'Convert Biased Coin to Fair Coin': 'Given a function that returns 0 with probability p and 1 with probability (1-p), write a function that returns 0 or 1 with equal probability.',
    
    'Rotating the Box': 'Given an m x n matrix representing a box with obstacles and stones, rotate the box 90 degrees clockwise and let stones fall due to gravity.',
    
    'Generate Parentheses': 'Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. Example: n=3 → ["((()))","(()())","(())()","()(())","()()()"]',
    
    'Roman to Integer': 'Given a Roman numeral string (e.g., "MCMXCIV"), convert it to an integer (e.g., 1994).',
    
    'Sliding Window Maximum': 'Given an array of integers and a window size k, find the maximum value in each sliding window as it moves from left to right.',
    
    'Set Matrix Zeroes': 'Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.',
    
    'Squares of sorted array': 'Given a sorted array of integers (may include negatives), return an array of the squares of each number, also sorted.',
    
    'Search in rotated sorted array': 'Given a rotated sorted array (e.g., [4,5,6,7,0,1,2]), search for a target value in O(log n) time.',
    
    'Serialize and deserialize binary tree': 'Design an algorithm to serialize a binary tree to a string and deserialize the string back to the tree structure.',
    
    'Linked List Cycle': 'Given a linked list, determine if it has a cycle. If yes, return the node where the cycle begins.',
}

def expand_incomplete_question(question_title):
    """Get the full question description for an incomplete title"""
    # Clean the title
    clean_title = question_title.rstrip('.')
    
    # Look up in expansions
    if clean_title in QUESTION_EXPANSIONS:
        return QUESTION_EXPANSIONS[clean_title]
    
    return None

def expand_questions_in_file(file_path):
    """Expand incomplete questions in a file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    expanded_count = 0
    
    for line in lines:
        # Check if this is a strikethrough question
        strikethrough_match = re.match(
            r'^(\d+)\.\s+(💗|🟢|🔴|🟠|🟡|⚪|⚠️)?\s*~~(.+?)~~\s*\*?\(incomplete.*\)\*?$',
            line
        )
        
        if strikethrough_match:
            number = strikethrough_match.group(1)
            emoji = strikethrough_match.group(2) or ''
            question_title = strikethrough_match.group(3).strip()
            
            # Try to expand
            expanded = expand_incomplete_question(question_title)
            
            if expanded:
                # Replace strikethrough with expanded question
                if emoji:
                    new_line = f"{number}. {emoji} {expanded}"
                else:
                    new_line = f"{number}. {expanded}"
                
                new_lines.append(new_line)
                expanded_count += 1
            else:
                # Keep strikethrough if we can't expand
                new_lines.append(line)
        else:
            # Not a strikethrough question, keep as is
            new_lines.append(line)
    
    return '\n'.join(new_lines), expanded_count

def main():
    """Expand incomplete questions in all question banks"""
    
    print("📝 Expanding incomplete questions with full descriptions...")
    print("=" * 70)
    print()
    
    repo_root = Path('/Users/anixlynch/Downloads/Exponent_DataAnalyst_interview')
    roles_dir = repo_root / 'roles'
    
    total_roles = 0
    total_expanded = 0
    
    for role_dir in sorted(roles_dir.iterdir()):
        if not role_dir.is_dir():
            continue
        
        role_name = role_dir.name.replace('-', ' ').title()
        
        # Process original question bank files
        qb_files = list(role_dir.glob('*Question_Bank.md'))
        qb_files = [f for f in qb_files if 'TAGGED' not in f.name.upper()]
        
        if not qb_files:
            continue
        
        role_expanded = 0
        
        for file_path in qb_files:
            new_content, expanded_count = expand_questions_in_file(file_path)
            
            if expanded_count > 0:
                # Save updated file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                role_expanded += expanded_count
        
        if role_expanded > 0:
            print(f"✅ {role_name}: {role_expanded} questions expanded")
            total_roles += 1
            total_expanded += role_expanded
    
    print()
    print("=" * 70)
    print(f"✅ COMPLETE!")
    print(f"   • Updated {total_roles} roles")
    print(f"   • Expanded {total_expanded} questions")
    print()
    print("Example expansions:")
    print("  BEFORE: ~~Employee Earnings~~ *(incomplete)*")
    print("  AFTER:  Write a SQL query to find employees earning more than their managers.")
    print()
    print("Now questions have full context and are actionable!")

if __name__ == "__main__":
    main()
