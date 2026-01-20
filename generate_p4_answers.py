#!/usr/bin/env python3
"""
Generate short answers for P4 questions using the Cohort / Retention / Churn framework.
Each answer follows: Define Cohorts → Measure Retention → Identify Churn Drivers → Hypothesize → Fix
with line breaks between sections.
"""

import csv

def generate_p4_short_answer(question_text, notes):
    """Generate a short answer following P4 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_retention = any(word in question_lower for word in ['retention', 'retain', 'return', 'come back', 'return rate'])
    is_churn = any(word in question_lower for word in ['churn', 'leave', 'drop', 'inactive', 'not logging', 'not using'])
    is_cohort = any(word in question_lower for word in ['cohort', 'segment'])
    is_new_user = any(word in question_lower for word in ['new user', 'new users', 'sign-up', 'signup'])
    is_paying = any(word in question_lower for word in ['paying', 'subscriber', 'subscription'])
    
    parts = []
    
    # 1. DEFINE COHORTS
    cohorts = "Define Cohorts: Group users by meaningful dimensions. "
    cohorts += "By signup time: week/month cohorts to track lifecycle. "
    cohorts += "By acquisition source: ads vs organic vs referral to identify quality differences. "
    cohorts += "By persona: power users vs casual users vs new users. "
    cohorts += "By behavior: activated vs not activated, feature adopters vs non-adopters."
    
    parts.append(cohorts)
    
    # 2. MEASURE RETENTION
    retention = "Measure Retention: Build retention curve and compare cohorts. "
    retention += "Track: D1 (day 1), D7 (week 1), D30 (month 1), W4 (week 4), M3 (month 3) retention. "
    retention += "Compare cohorts side-by-side to spot differences. "
    retention += "Assess: absolute level (how low is retention?) and shape (early cliff vs slow decay)."
    
    parts.append(retention)
    
    # 3. IDENTIFY CHURN DRIVERS
    churn = "Identify Churn Drivers: Understand WHEN, WHO, and WHAT. "
    
    if is_new_user:
        churn += "WHEN: Day 0-1 churn → onboarding/activation problem. "
        churn += "Week 1 churn → value not clear. "
        churn += "Month 1+ churn → habit/competition issue. "
    else:
        churn += "WHEN: Day 0-1 → onboarding/activation gap. "
        churn += "Week 1 → value not clear. "
        churn += "Month 1+ → habit formation or competition. "
    
    churn += "WHO: Which segments leave more? Specific cohorts, channels, or user types? "
    churn += "WHAT: What changes before churn? Drop in key actions, fewer sessions, feature not used, or usage pattern shift."
    
    parts.append(churn)
    
    # 4. HYPOTHESIZE
    hypothesize = "Hypothesize: Generate hypotheses based on churn timing and patterns. "
    if is_new_user:
        hypothesize += "If users churn early (Day 0-1) → activation gap, onboarding friction. "
        hypothesize += "If one cohort worse → acquisition mismatch, targeting issue. "
        hypothesize += "If usage drops first → value erosion, core loop not engaging. "
        hypothesize += "If late churn (Month 1+) → lack of habit, missing retention hooks."
    elif is_paying:
        hypothesize += "If paying but inactive → value not delivered, product-market fit gap. "
        hypothesize += "If specific cohort churns → acquisition quality issue. "
        hypothesize += "If gradual decline → habit not formed, engagement loop broken."
    else:
        hypothesize += "If early drop → activation problem. "
        hypothesize += "If one cohort worse → acquisition mismatch. "
        hypothesize += "If usage drops first → value erosion. "
        hypothesize += "If late churn → lack of habit/reminders."
    
    parts.append(hypothesize)
    
    # 5. FIX
    fix = "Fix: Implement targeted solutions based on hypotheses. "
    if is_new_user:
        fix += "Improve onboarding/activation: simplify first experience, show value faster, reduce friction. "
        fix += "Tighten targeting: improve acquisition quality, align messaging with product value. "
        fix += "Reinforce core value loop: ensure users complete key action early. "
        fix += "Add retention hooks: email, push notifications, content recommendations. "
        fix += "Measure cohort again: track if retention curve improved for next cohort."
    else:
        fix += "Improve onboarding/activation for early churn. "
        fix += "Tighten targeting if specific cohorts underperform. "
        fix += "Reinforce core value loop if usage drops. "
        fix += "Add retention hooks (email, push, content) for late churn. "
        fix += "Measure cohort again to validate improvements."
    
    parts.append(fix)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p4_csv(input_file, output_file):
    """Process P4 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            # Process all rows with pattern_id = P4
            if row.get('pattern_id') == 'P4':
                short_answer = generate_p4_short_answer(row['question_text'], row.get('notes', ''))
                row['short_answer'] = short_answer
            else:
                # For rows that aren't P4, leave short_answer empty
                row['short_answer'] = ''
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    p4_count = sum(1 for row in rows if row.get('pattern_id') == 'P4')
    print(f"Generated {p4_count} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/04_P4_cohort_retention_churn.csv'
    output_file = 'pattern_bank_answered/04_P4_cohort_retention_churn.csv'
    process_p4_csv(input_file, output_file)
