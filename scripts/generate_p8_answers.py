#!/usr/bin/env python3
"""
Generate short answers for P8 questions using the Experiment Design framework.
Each answer follows: Hypothesis → Metric → Design → Run → Validate → Decide
with line breaks between sections.
"""

import csv

def generate_p8_short_answer(question_text, notes):
    """Generate a short answer following P8 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_ab_test = any(word in question_lower for word in ['a/b', 'ab test', 'experiment', 'test'])
    is_feature = any(word in question_lower for word in ['feature', 'new feature', 'rollout', 'ship'])
    is_algorithm = any(word in question_lower for word in ['algorithm', 'ranking', 'recommendation'])
    is_pilot = any(word in question_lower for word in ['pilot', 'validate', 'mvp', 'market fit'])
    is_campaign = any(word in question_lower for word in ['campaign', 'promotion', 'marketing'])
    
    parts = []
    
    # 0. FRAME (30 sec)
    frame = "Frame: Clarify decision and constraints. "
    frame += "What decision are we making? (launch feature, change algorithm, run campaign, etc.) "
    frame += "What constraints matter? (time, risk, traffic volume, legal, UX impact). "
    frame += "Define success criteria upfront."
    
    parts.append(frame)
    
    # 1. HYPOTHESIS
    hypothesis = "Hypothesis: State clear if-then-because. "
    hypothesis += "Format: If we change X for users Y, then outcome Z will change because R. "
    hypothesis += "X = treatment (what changes). "
    hypothesis += "Y = target population (who gets the change). "
    hypothesis += "Z = expected direction + size (if possible). "
    hypothesis += "R = mechanism (why it should work)."
    
    parts.append(hypothesis)
    
    # 2. METRIC (success + safety)
    metric = "Metric: Define primary, guardrails, and diagnostics. "
    metric += "Primary metric: the 'one number' for decision. "
    metric += "Must map to goal (revenue, retention, activation, conversion, engagement). "
    metric += "Guardrails: prevent self-own (quality, user harm, churn, latency, errors, complaints). "
    metric += "Diagnostics: help explain why (step metrics, funnel steps, latency breakdown, CTR vs CVR)."
    
    parts.append(metric)
    
    # 3. DESIGN (make it valid)
    design = "Design: Make experiment valid and reliable. "
    design += "Unit of randomization: user vs session vs account vs geo vs device. "
    design += "Avoid spillover (users affecting each other). "
    design += "Population / eligibility: new users? returning? specific segment? "
    design += "Variants: Control vs Treatment (or A/B/C). Keep everything else constant. "
    design += "Duration & sample sizing: run full cycles (weekday/weekend). "
    design += "Ensure enough power for expected effect size. "
    design += "Instrumentation: event tracking, logging, exposure definition. "
    design += "'Who saw treatment?' must be unambiguous."
    
    parts.append(design)
    
    # 4. RUN (execution plan)
    run = "Run: Execute with careful ramp and monitoring. "
    run += "Ramp: 1% → 10% → 50% → 100% (if safe). "
    run += "Monitor guardrails daily. "
    run += "Freeze conflicting changes during test window. "
    run += "Track exposure and outcomes consistently."
    
    parts.append(run)
    
    # 5. VALIDATE (trust the result?)
    validate = "Validate: Check result trustworthiness. "
    validate += "A/A or sanity checks (if available). "
    validate += "SRM check (sample ratio mismatch - traffic split correct?). "
    validate += "Balance check (are groups comparable?). "
    validate += "Correct attribution (exposure vs outcome window). "
    validate += "Novelty / seasonality / logging changes. "
    validate += "Multiple testing / peeking risk."
    
    parts.append(validate)
    
    # 6. DECIDE
    decide = "Decide: Ship, iterate, or rollback. "
    decide += "If primary metric up and guardrails stable → ship with gradual rollout. "
    decide += "If mixed results → iterate (refine treatment) and re-test. "
    decide += "If guardrails worsen → rollback + root-cause analysis. "
    decide += "Learnings: mechanism confirmed? which segment moved? "
    decide += "Follow-up monitoring plan."
    
    parts.append(decide)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p8_csv(input_file, output_file):
    """Process P8 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_p8_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/08_P8_experiment_design.csv'
    output_file = 'pattern_bank_answered/08_P8_experiment_design.csv'
    process_p8_csv(input_file, output_file)
