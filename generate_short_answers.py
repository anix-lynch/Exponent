#!/usr/bin/env python3
"""
Generate short answers for P1 questions using the formula library framework.
Each answer follows: Clarify → Data Check → Segment → Hypothesize → Validate → Action
with line breaks between sections.
"""

import csv
import re

def generate_short_answer(question_text, notes):
    """Generate a short answer following P1 framework with line breaks."""
    
    # Extract key context from question and notes
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine if it's a drop, increase, or improvement question
    is_drop = any(word in question_lower for word in ['down', 'drop', 'decline', 'decrease', 'decreasing', 'dip', 'fall'])
    is_increase = any(word in question_lower for word in ['increase', 'improve', 'grow', 'up', 'rise', 'enhance'])
    is_diagnosis = any(word in question_lower for word in ['investigate', 'diagnose', 'why', 'what happened', 'root cause', 'analyze'])
    
    # Extract metric mentions
    metric_keywords = ['orders', 'revenue', 'conversion', 'engagement', 'bookings', 'transactions', 
                       'watch time', 'signups', 'DAU', 'MAU', 'traffic', 'rating', 'market share',
                       'usage', 'drop-off', 'NPS', 'installs', 'deliveries', 'tickets', 'cancellations']
    
    mentioned_metric = None
    for metric in metric_keywords:
        if metric in question_lower:
            mentioned_metric = metric
            break
    
    # Build answer following P1 framework
    parts = []
    
    # 1. CLARIFY
    if is_drop:
        clarify = f"Clarify: Define the metric (numerator/denominator), baseline, and scope. "
        if mentioned_metric:
            clarify += f"Specify: {mentioned_metric} = what exactly? "
        clarify += "Time window: when did it start? Magnitude: how significant?"
    elif is_increase:
        clarify = f"Clarify: Define success metric and target. "
        if mentioned_metric:
            clarify += f"Current {mentioned_metric} rate? Target growth? "
        clarify += "Scope: which segments, surfaces, or user types?"
    else:
        clarify = "Clarify: Define the key metric(s) and success criteria. What exactly needs to change? Baseline and target?"
    
    parts.append(clarify)
    
    # 2. DATA CHECK
    data_check = "Data Check: Rule out instrumentation changes, pipeline delays, or denominator shifts. "
    if is_drop:
        data_check += "Verify tracking accuracy, ETL lag, or event schema changes."
    elif is_increase:
        data_check += "Confirm measurement is accurate and not inflated by bots or data quality issues."
    else:
        data_check += "Ensure data quality and measurement consistency."
    
    parts.append(data_check)
    
    # 3. SEGMENT
    segment = "Segment: Slice by platform (iOS/Android/Web), geography, user cohort (new vs returning), "
    if 'booking' in question_lower or 'reservation' in question_lower:
        segment += "listing type, and booking window to find highest-leverage opportunities."
    elif 'transaction' in question_lower or 'purchase' in question_lower:
        segment += "product category, discovery surface, and payment method to identify friction points."
    elif 'engagement' in question_lower or 'usage' in question_lower:
        segment += "content type, feature usage, and time of day to find engagement drivers."
    elif 'delivery' in question_lower or 'logistics' in question_lower:
        segment += "city, partner type, and order characteristics to isolate the issue."
    else:
        segment += "funnel step, acquisition channel, and user segment to find the hot spot."
    
    parts.append(segment)
    
    # 4. HYPOTHESIZE
    if is_drop:
        hypothesize = "Hypothesize: Product changes (UI, pricing, policy), external factors (competitor, seasonality), "
        hypothesize += "performance issues (latency, crashes), or supply-side changes (if marketplace)."
    elif is_increase:
        hypothesize = "Hypothesize: Search relevance, pricing optimization, trust signals, supply quality, "
        hypothesize += "feature adoption, or user experience improvements."
    else:
        hypothesize = "Hypothesize: Top 3-5 potential causes ranked by likelihood × impact. "
        hypothesize += "Consider product, user, market, and technical factors."
    
    parts.append(hypothesize)
    
    # 5. VALIDATE
    validate = "Validate: Check correlation with launches, counter-metrics, funnel drop-offs, "
    if is_drop:
        validate += "and compare to control segments. Look for crash rates, error codes, or performance degradation."
    elif is_increase:
        validate += "and test hypotheses with A/B tests or targeted experiments. Compare conversion rates by segment."
    else:
        validate += "and analyze user behavior patterns. Use session replays, surveys, or log analysis."
    
    parts.append(validate)
    
    # 6. ACTION
    if is_drop:
        action = "Action: If severe + clear cause → rollback/hotfix immediately. "
        action += "If unclear → add logging, run targeted experiments, or fix segment-specific issues. "
        action += "Communicate findings and mitigation plan."
    elif is_increase:
        action = "Action: Focus on highest-impact segments. "
        action += "Implement fixes: improve search/ranking, optimize pricing, add trust signals, or enhance UX. "
        action += "Measure impact and iterate."
    else:
        action = "Action: Prioritize fixes by impact × confidence. "
        action += "Start with data issues, then high-impact hypotheses. "
        action += "Run experiments, monitor results, and communicate plan."
    
    parts.append(action)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_csv(input_file, output_file):
    """Process CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/01_P1_metric_drop.csv'
    output_file = 'pattern_bank_answered/01_P1_metric_drop.csv'
    process_csv(input_file, output_file)
