#!/usr/bin/env python3
"""
Generate short answers for P9 questions using either:
- Decision Under Uncertainty: Clarify Assumptions → Identify Risks → Validation Plan → Decide
- Revenue Optimization: Levers (Price, Volume, Mix) → Test → Measure → Iterate
with line breaks between sections.
"""

import csv

def generate_revenue_optimization_answer(question_text, notes):
    """Generate a short answer following Revenue Optimization framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    parts = []
    
    # 1. LEVERS (Price, Volume, Mix)
    levers = "Levers: Identify revenue optimization opportunities. "
    levers += "Price: "
    levers += "Pricing strategy: increase price, optimize pricing tiers, dynamic pricing. "
    levers += "Price elasticity: test price sensitivity, find optimal price point. "
    levers += "Volume: "
    levers += "User acquisition: increase new users, improve conversion funnel. "
    levers += "Engagement: increase usage frequency, session depth, feature adoption. "
    levers += "Retention: reduce churn, improve lifetime value. "
    levers += "Mix: "
    levers += "Product mix: optimize product portfolio, cross-sell, upsell. "
    levers += "Customer mix: focus on high-value segments, improve ARPU. "
    levers += "Channel mix: optimize acquisition channels, improve CAC efficiency."
    
    parts.append(levers)
    
    # 2. TEST
    test = "Test: Run experiments to validate levers. "
    test += "Design experiments: A/B tests, phased rollouts, market tests. "
    test += "Test one lever at a time: isolate impact of each change. "
    test += "Control for external factors: seasonality, market conditions. "
    test += "Sample size: ensure statistical significance."
    
    parts.append(test)
    
    # 3. MEASURE
    measure = "Measure: Track impact on revenue and key metrics. "
    measure += "Primary metric: revenue impact (total revenue, ARPU, LTV). "
    measure += "Secondary metrics: conversion rate, retention, engagement. "
    measure += "Guardrails: monitor churn, user satisfaction, brand impact. "
    measure += "Time horizon: short-term vs long-term revenue impact."
    
    parts.append(measure)
    
    # 4. ITERATE
    iterate = "Iterate: Refine and optimize based on results. "
    iterate += "If successful: scale the change, expand to more segments. "
    iterate += "If mixed: refine the lever, test variations. "
    iterate += "If unsuccessful: try different lever, pivot strategy. "
    iterate += "Continuous optimization: revenue is not one-time, keep testing and improving."
    
    parts.append(iterate)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def generate_p9_short_answer(question_text, notes):
    """Generate a short answer following P9 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_market_entry = any(word in question_lower for word in ['market', 'enter', 'open', 'expand', 'launch'])
    is_feature = any(word in question_lower for word in ['feature', 'ship', 'deliver', 'build'])
    is_commitment = any(word in question_lower for word in ['guarantee', 'commit', 'promise', 'deadline'])
    is_go_nogo = any(word in question_lower for word in ['go/no-go', 'go no go', 'should we', 'decide'])
    is_pmf = any(word in question_lower for word in ['product-market fit', 'pmf', 'fit'])
    
    parts = []
    
    # 1. CLARIFY ASSUMPTIONS
    assumptions = "Clarify Assumptions: Identify what we believe is true. "
    assumptions += "User behavior assumptions: how will users react, what do they need? "
    assumptions += "Market / demand assumptions: is there demand, what's the market size? "
    assumptions += "Technical feasibility assumptions: can we build it, what are the constraints? "
    assumptions += "Timing / dependency assumptions: when can we deliver, what dependencies exist? "
    assumptions += "Classify assumptions: Critical (decision breaks if wrong) vs Non-critical (nice to know)."
    
    parts.append(assumptions)
    
    # 2. IDENTIFY RISKS
    risks = "Identify Risks: Assess what happens if assumptions are wrong. "
    risks += "If assumption is wrong, what happens? "
    risks += "Revenue risk: financial impact, opportunity cost. "
    risks += "User trust / UX risk: experience degradation, brand damage. "
    risks += "Technical / scalability risk: performance, reliability issues. "
    risks += "Legal / compliance risk: regulatory, legal exposure. "
    risks += "Rank risks: High impact × high likelihood → MUST address. "
    risks += "Low impact or low likelihood → monitor."
    
    parts.append(risks)
    
    # 3. VALIDATION PLAN
    validation = "Validation Plan: Find cheapest signal to reduce uncertainty. "
    validation += "What is the cheapest signal to reduce uncertainty? "
    validation += "Qualitative: user interviews, expert review, stakeholder feedback. "
    validation += "Quantitative: logs, metrics, small experiments, data analysis. "
    validation += "Proxies: analogous products, historical data, competitor analysis. "
    validation += "Time-boxed spike / prototype: build minimal version to test. "
    validation += "Decide upfront: What result would change the decision? "
    validation += "What result is 'good enough' to proceed?"
    
    parts.append(validation)
    
    # 4. DECIDE
    decide = "Decide: Choose path forward with guardrails. "
    decide += "Option A: Proceed now. "
    decide += "If upside >> downside and risks are bounded. "
    decide += "Option B: Delay and validate. "
    decide += "If one critical unknown dominates. "
    decide += "Option C: Kill / pivot. "
    decide += "If downside is irreversible or catastrophic. "
    decide += "Set clear criteria: what would make us change our decision?"
    
    parts.append(decide)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p9_csv(input_file, output_file):
    """Process P9 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            # Process all P9 rows based on their pattern_name
            if row.get('pattern_id') == 'P9':
                pattern_name = row.get('pattern_name', '')
                if 'Decision Under Uncertainty' in pattern_name:
                    short_answer = generate_p9_short_answer(row['question_text'], row.get('notes', ''))
                elif 'Revenue Optimization' in pattern_name:
                    short_answer = generate_revenue_optimization_answer(row['question_text'], row.get('notes', ''))
                else:
                    # Default to Decision Under Uncertainty if pattern not recognized
                    short_answer = generate_p9_short_answer(row['question_text'], row.get('notes', ''))
                row['short_answer'] = short_answer
            else:
                # For rows that aren't P9, leave short_answer empty
                row['short_answer'] = ''
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    p9_count = sum(1 for row in rows if row.get('pattern_id') == 'P9')
    print(f"Generated {p9_count} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/09_P9_decision_uncertainty.csv'
    output_file = 'pattern_bank_answered/09_P9_decision_uncertainty.csv'
    process_p9_csv(input_file, output_file)
