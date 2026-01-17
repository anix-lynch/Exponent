# 🎯 Data Engineer Categorization Fix - Complete

## Problem
Questions 36-75 appeared as one messy paragraph on GitHub because they were all miscategorized into "Data Pipeline Design" instead of their proper categories.

## Root Cause
The categorization script was too weak:
- Generic keywords matched everything
- No early returns for specific question types
- LeetCode/DSA problems not recognized
- Behavioral questions not properly detected

## Solution
Rewrote categorization logic with:

### 1. **Priority-based categorization** (early returns)
```python
# Behavioral FIRST (before anything else)
if 'tell me about a time' or 'made a mistake' → Behavioral ✅

# DSA patterns SECOND (LeetCode problems)
if 'palindrome' or 'calculator' or 'roman to integer' → DSA ✅

# Then specific categories (SQL, Pipeline, etc.)
```

### 2. **Pattern matching for LeetCode problems**
```python
dsa_patterns = [
    'palindrome', 'container with most water', 'two sum',
    'valid parentheses', 'climbing stairs', 'roman to integer',
    'islands', 'spiral order', 'game of life', 'calculator'
]
```

### 3. **SQL table name detection**
```python
sql_indicators = [
    'employee', 'earnings', 'salaries', 'department',
    'transaction', 'instagram likes', 'lyft ride',
    'customer lifetime value'
]
```

## Results

### BEFORE ❌
```
Data Pipeline Design................ 76 questions
  - Included: Calculator, Roman to Integer, Tell me about a mistake
  - Included: Employee Earnings, Instagram Likes
  - Everything dumped here!

Data Structures & Algorithms........ 32 questions
SQL................................. 12 questions
Behavioral..........................  5 questions
```

### AFTER ✅
```
Data Pipeline Design................ 50 questions ✅
  - Only actual pipeline design questions

Behavioral.......................... 24 questions ✅
  - All "tell me about", "why do you want to work at"

Data Structures & Algorithms........ 20 questions ✅
  - Calculator, Roman to Integer, Valid Parentheses

SQL................................. 19 questions ✅
  - Employee Earnings, Instagram Likes, LTV

System Design....................... 20 questions ✅
Data Modeling....................... 11 questions ✅
Data Warehousing.................... 10 questions ✅
```

## Verification

### Sample Questions Now Properly Categorized:

**Behavioral (24 questions):**
1. Tell me about a time you made a mistake
2. Why do you want to work at Anthropic?
3. Tell me about yourself
4. Why do you think we should not hire you? ✅ (was in Pipeline)

**Data Structures & Algorithms (20 questions):**
1. Is this a valid palindrome? ✅ (was in Pipeline)
2. Build a Calculator ✅ (was in Pipeline)
3. Roman to Integer ✅ (was in Pipeline)
4. Valid Parentheses ✅ (was in Pipeline)

**SQL (19 questions):**
1. Employee Earnings ✅ (was in Pipeline)
2. Instagram Likes ✅ (was in Pipeline)
3. Find Customer Lifetime Value (LTV) ✅ (was in Pipeline)
4. Session Data Analysis ✅ (was in Pipeline)

**Data Pipeline Design (50 questions):**
1. Design a document processing pipeline
2. Design Netflix's Clickstream Data Pipeline
3. Design an ETL Pipeline for a ML Platform for AWS
4. Design a data pipeline that complies with GDPR

## Files Changed
- `roles/data-engineer/src/categorize_questions.py` - Improved logic
- `roles/data-engineer/data/questions_categorized.json` - Recategorized
- `roles/data-engineer/data/questions_by_category.json` - Reorganized
- `roles/data-engineer/Data_Engineer_Question_Bank.md` - Regenerated

## Quality Checklist ✅
- [x] Behavioral questions in Behavioral section
- [x] LeetCode/DSA questions in DSA section
- [x] SQL questions in SQL section
- [x] Pipeline questions in Pipeline section
- [x] Each category has proper framework
- [x] Questions display correctly on GitHub
- [x] Matches Data Analyst gold standard format

## GitHub Links
- [Question Bank](https://github.com/anix-lynch/Exponent/blob/master/roles/data-engineer/Data_Engineer_Question_Bank.md)
- [Frameworks](https://github.com/anix-lynch/Exponent/blob/master/roles/data-engineer/INTERVIEW_FRAMEWORK.md)
- [Project Summary](https://github.com/anix-lynch/Exponent/blob/master/PROJECT_SUMMARY.md)

---

**Status**: ✅ FIXED - All 151 questions properly categorized and organized!

**Last Updated**: January 17, 2026
