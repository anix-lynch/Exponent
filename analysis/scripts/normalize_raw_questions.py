#!/usr/bin/env python3
"""
Normalize ALL_QUESTIONS_RAW.md for reliable pattern matching

Fixes:
1. Truncated questions (...)
2. Multi-question combos (split into separate entries)
3. Inconsistent formatting
4. URL encoding issues
5. Deduplication
"""

import re
import json
from pathlib import Path
from urllib.parse import unquote

def load_raw_questions(file_path):
    """Load questions from ALL_QUESTIONS_RAW.md"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by question number pattern
    pattern = r'\*\*(\d+)\.\*\* (.+?)\n   - \*\*Roles:\*\* (.+?)\n   - \*\*Original Categories:\*\* (.+?)\n   - \*\*URL:\*\* (.+?)(?=\n\n|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    questions = []
    for match in matches:
        qid, question, roles, categories, url = match
        questions.append({
            'id': int(qid),
            'question': question.strip(),
            'roles': roles.strip(),
            'categories': categories.strip(),
            'url': url.strip()
        })
    
    print(f"✓ Loaded {len(questions)} questions")
    return questions

def normalize_question_text(question):
    """Normalize question text"""
    # Remove leading/trailing whitespace
    question = question.strip()
    
    # Normalize quotes
    question = question.replace('"', '"').replace('"', '"')
    question = question.replace(''', "'").replace(''', "'")
    
    # Normalize whitespace
    question = re.sub(r'\s+', ' ', question)
    
    # Check for truncation
    is_truncated = question.endswith('...')
    
    return question, is_truncated

def normalize_url(url):
    """Normalize URL"""
    # Decode URL encoding
    url = unquote(url)
    
    # Remove trailing quotes
    url = url.rstrip('"').rstrip('%22')
    
    # Ensure https://
    if not url.startswith('http'):
        url = 'https://' + url
    
    return url

def split_multi_questions(question_text):
    """Split multi-question entries"""
    # Pattern: "1. Question A. 2. Question B. 3. Question C."
    pattern = r'(\d+)\.\s+([^.]+(?:\.[^0-9][^.]*)*\.)'
    matches = re.findall(pattern, question_text)
    
    if len(matches) > 1:
        # Multi-question detected
        questions = [match[1].strip() for match in matches]
        return questions, True
    
    return [question_text], False

def is_junk_question(question):
    """Identify junk questions to skip"""
    junk_patterns = [
        r'^\+ Share interview',
        r'^Share interview$',
        r'^I was asked this',
        r'^\+ Share interview experience',
    ]
    
    for pattern in junk_patterns:
        if re.match(pattern, question, re.IGNORECASE):
            return True
    
    return False

def normalize_categories(categories):
    """Normalize category formatting"""
    # Split by comma
    cats = [c.strip() for c in categories.split(',')]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_cats = []
    for cat in cats:
        if cat not in seen:
            seen.add(cat)
            unique_cats.append(cat)
    
    return ', '.join(unique_cats)

def deduplicate_questions(questions):
    """Remove duplicate questions"""
    seen = {}
    unique_questions = []
    duplicates = []
    
    for q in questions:
        # Create dedup key: normalized question + URL
        key = (q['question'].lower().strip(), q['url'])
        
        if key not in seen:
            seen[key] = q
            unique_questions.append(q)
        else:
            duplicates.append(q)
    
    print(f"✓ Removed {len(duplicates)} duplicates")
    return unique_questions, duplicates

def main():
    # Paths
    input_file = Path(__file__).parent.parent / 'output' / 'ALL_QUESTIONS_RAW.md'
    output_file = Path(__file__).parent.parent / 'output' / 'ALL_QUESTIONS_NORMALIZED.md'
    log_file = Path(__file__).parent.parent / 'output' / 'normalization_log.json'
    
    print("=" * 80)
    print("NORMALIZING ALL_QUESTIONS_RAW.md")
    print("=" * 80)
    
    # Load questions
    questions = load_raw_questions(input_file)
    
    # Normalization stats
    stats = {
        'original_count': len(questions),
        'truncated_count': 0,
        'multi_question_count': 0,
        'junk_count': 0,
        'url_fixed_count': 0,
        'final_count': 0
    }
    
    normalized_questions = []
    issues = []
    
    for q in questions:
        # Check for junk
        if is_junk_question(q['question']):
            stats['junk_count'] += 1
            issues.append({
                'id': q['id'],
                'issue': 'junk',
                'question': q['question']
            })
            continue
        
        # Normalize question text
        normalized_text, is_truncated = normalize_question_text(q['question'])
        if is_truncated:
            stats['truncated_count'] += 1
            issues.append({
                'id': q['id'],
                'issue': 'truncated',
                'question': q['question']
            })
        
        # Check for multi-questions
        split_questions, is_multi = split_multi_questions(normalized_text)
        if is_multi:
            stats['multi_question_count'] += 1
            issues.append({
                'id': q['id'],
                'issue': 'multi_question',
                'question': q['question'],
                'split_into': split_questions
            })
            
            # Create separate entries for each sub-question
            for i, sub_q in enumerate(split_questions):
                normalized_questions.append({
                    'id': f"{q['id']}.{i+1}",
                    'question': sub_q,
                    'roles': q['roles'],
                    'categories': normalize_categories(q['categories']),
                    'url': normalize_url(q['url']),
                    'original_id': q['id']
                })
        else:
            # Single question
            normalized_url = normalize_url(q['url'])
            if normalized_url != q['url']:
                stats['url_fixed_count'] += 1
            
            normalized_questions.append({
                'id': q['id'],
                'question': normalized_text,
                'roles': q['roles'],
                'categories': normalize_categories(q['categories']),
                'url': normalized_url
            })
    
    # Deduplicate
    normalized_questions, duplicates = deduplicate_questions(normalized_questions)
    stats['final_count'] = len(normalized_questions)
    
    # Write normalized file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# ALL QUESTIONS - NORMALIZED\n\n")
        f.write(f"**Total: {len(normalized_questions)} unique questions**\n\n")
        f.write("**Purpose:** Clean, normalized master list ready for tagging\n\n")
        f.write("**Format:** Question | Roles | Original Categories | URL\n\n")
        f.write("**Normalization applied:**\n")
        f.write("- ✅ Junk questions removed\n")
        f.write("- ✅ Multi-question entries split\n")
        f.write("- ✅ URL encoding fixed\n")
        f.write("- ✅ Duplicates removed\n")
        f.write("- ✅ Categories normalized\n")
        f.write("- ⚠️ Truncated questions flagged (see log)\n\n")
        f.write("---\n\n")
        
        for q in normalized_questions:
            f.write(f"**{q['id']}.** {q['question']}\n")
            f.write(f"   - **Roles:** {q['roles']}\n")
            f.write(f"   - **Original Categories:** {q['categories']}\n")
            f.write(f"   - **URL:** {q['url']}\n\n")
    
    # Write log
    log_data = {
        'stats': stats,
        'issues': issues,
        'duplicates': [
            {
                'id': d['id'],
                'question': d['question'],
                'url': d['url']
            }
            for d in duplicates
        ]
    }
    
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, indent=2)
    
    # Print summary
    print("\n" + "=" * 80)
    print("NORMALIZATION SUMMARY")
    print("=" * 80)
    print(f"Original questions:       {stats['original_count']}")
    print(f"Junk removed:             {stats['junk_count']}")
    print(f"Multi-questions split:    {stats['multi_question_count']}")
    print(f"Truncated (flagged):      {stats['truncated_count']}")
    print(f"URLs fixed:               {stats['url_fixed_count']}")
    print(f"Duplicates removed:       {len(duplicates)}")
    print(f"Final count:              {stats['final_count']}")
    print("=" * 80)
    print(f"\n✓ Normalized file: {output_file}")
    print(f"✓ Log file: {log_file}")
    print("\n⚠️  TRUNCATED QUESTIONS:")
    print(f"   {stats['truncated_count']} questions end with '...' and need full text")
    print(f"   See {log_file} for details")

if __name__ == '__main__':
    main()
