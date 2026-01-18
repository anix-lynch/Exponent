#!/usr/bin/env python3
"""
Expand truncated questions by using the URL slug as a guide

Since we can't scrape, we'll use the URL to infer the full question
or mark them for manual review.
"""

import json
from pathlib import Path
import re

def load_log():
    """Load normalization log"""
    log_file = Path(__file__).parent.parent / 'output' / 'normalization_log.json'
    with open(log_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_normalized_questions():
    """Load normalized questions"""
    file_path = Path(__file__).parent.parent / 'output' / 'ALL_QUESTIONS_NORMALIZED.md'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'\*\*(\d+)\.\*\* (.+?)\n   - \*\*Roles:\*\* (.+?)\n   - \*\*Original Categories:\*\* (.+?)\n   - \*\*URL:\*\* (.+?)(?=\n\n|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    questions = {}
    for match in matches:
        qid, question, roles, categories, url = match
        questions[int(qid)] = {
            'id': int(qid),
            'question': question.strip(),
            'roles': roles.strip(),
            'categories': categories.strip(),
            'url': url.strip()
        }
    
    return questions

def extract_question_from_url(url):
    """Extract question hint from URL slug"""
    # Get the last part of URL
    slug = url.split('/')[-1]
    
    # Remove question ID prefix (e.g., "2186/")
    slug = re.sub(r'^\d+/', '', slug)
    
    # Convert dashes to spaces
    slug = slug.replace('-', ' ')
    
    # Capitalize first letter
    slug = slug.capitalize()
    
    return slug

def main():
    print("=" * 80)
    print("EXPANDING TRUNCATED QUESTIONS")
    print("=" * 80)
    
    # Load data
    log = load_log()
    questions = load_normalized_questions()
    
    # Find truncated questions
    truncated = [issue for issue in log['issues'] if issue['issue'] == 'truncated']
    
    print(f"\n✓ Found {len(truncated)} truncated questions")
    print("\nTruncated questions (URL slugs as hints):\n")
    
    for item in truncated:
        qid = item['id']
        q = questions.get(qid)
        
        if q:
            url_hint = extract_question_from_url(q['url'])
            print(f"ID {qid}:")
            print(f"  Truncated: {item['question'][:80]}...")
            print(f"  URL hint:  {url_hint}")
            print(f"  Full URL:  {q['url']}")
            print()
    
    print("=" * 80)
    print("RECOMMENDATION")
    print("=" * 80)
    print("\n34 truncated questions out of 2,849 = 1.2%")
    print("\nOptions:")
    print("1. ✅ PROCEED WITH TAGGING - 98.8% of questions are complete")
    print("   - Truncated questions will likely auto-tag to 🔴 (incomplete info)")
    print("   - Can manually review the 34 later if needed")
    print("\n2. ⚠️  MANUAL EXPANSION - Visit each URL and copy full question")
    print("   - Time-consuming (34 URLs)")
    print("   - Only needed if these are high-value questions")
    print("\n3. 🤖 SMART EXPANSION - Use URL slug + context to infer full question")
    print("   - Example: 'facebook-video-for-individuals-with-hearing-disabilities'")
    print("   - Can reconstruct: 'Design improvements for Facebook videos for hearing disabilities'")
    print("\nRECOMMENDATION: Option 1 (proceed with tagging)")
    print("The truncated questions are edge cases and won't block your goal.")

if __name__ == '__main__':
    main()
