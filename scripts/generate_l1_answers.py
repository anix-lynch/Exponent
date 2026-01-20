#!/usr/bin/env python3
"""
Generate short answers for L1 questions using the Data Trust framework.
Each answer follows: Source → Freshness → Completeness → Bias → Sanity Checks
with line breaks between sections.
"""

import csv

def generate_l1_short_answer(question_text, notes):
    """Generate a short answer following L1 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_debug = any(word in question_lower for word in ['debug', 'off', 'wrong', 'anomaly', 'issue'])
    is_quality = any(word in question_lower for word in ['quality', 'clean', 'governance', 'curation', 'messy'])
    is_bias = any(word in question_lower for word in ['bias', 'bias'])
    is_integration = any(word in question_lower for word in ['join', 'integrate', 'inconsistent', 'different sources'])
    is_behavioral = any(word in question_lower for word in ['describe', 'tell me', 'experience', 'project'])
    
    parts = []
    
    # 1. SOURCE (WHERE did this come from?)
    source = "Source: Identify origin and validate ownership. "
    source += "Identify origin: "
    source += "Primary: product logs, first-party events, direct user actions. "
    source += "Secondary: internal pipelines, transformations, aggregated data. "
    source += "External: vendors, partners, scraped data, third-party APIs. "
    source += "Validate ownership: "
    source += "Who maintains it? Who is on-call when it breaks? "
    source += "Is there documentation / lineage? Can we trace the data flow?"
    
    parts.append(source)
    
    # 2. FRESHNESS (IS it up to date?)
    freshness = "Freshness: Check if data is up to date. "
    freshness += "Expected latency: "
    freshness += "Real-time: should update immediately. "
    freshness += "Hourly: should update within the hour. "
    freshness += "Daily / Batch: should update on schedule. "
    freshness += "Check gaps: "
    freshness += "Last updated timestamp: when was it last refreshed? "
    freshness += "Delays vs SLA: is it meeting expected update frequency? "
    freshness += "Silent failures: no alerts but stale data (check for missing updates)."
    
    parts.append(freshness)
    
    # 3. COMPLETENESS (IS anything missing?)
    completeness = "Completeness: Verify nothing is missing. "
    completeness += "Coverage checks: "
    completeness += "Missing rows / days: are there gaps in the time series? "
    completeness += "Null or default-heavy fields: are key fields populated? "
    completeness += "Partial segments dropped: are all user segments / platforms included? "
    completeness += "Join loss: "
    completeness += "Inner joins removing data: are we losing records in joins? "
    completeness += "Key mismatches: do join keys align correctly? "
    completeness += "Upstream schema changes: did schema changes break data collection?"
    
    parts.append(completeness)
    
    # 4. BIAS (WHO is over- or under-represented?)
    bias = "Bias: Check who is over- or under-represented. "
    bias += "Sampling bias: "
    bias += "Logged-in only: are we missing anonymous users? "
    bias += "Power users: are we over-representing heavy users? "
    bias += "Specific regions / platforms: are all geos and devices included? "
    bias += "Measurement bias: "
    bias += "Proxy ≠ true behavior: is our metric a good proxy for what we care about? "
    bias += "Instrumentation gaps: are we tracking all relevant events? "
    bias += "Incentives to game metrics: could users or teams be gaming the measurement?"
    
    parts.append(bias)
    
    # 5. SANITY CHECKS (DO numbers pass smell test?)
    sanity = "Sanity Checks: Verify numbers pass the smell test. "
    sanity += "Trend checks: sharp jumps/drops that don't align with known changes. "
    sanity += "Ratio checks: conversion > 100%? Negative values where impossible? "
    sanity += "Cross-metric consistency: do related metrics move together logically? "
    sanity += "Compare to historical baselines: is this within expected range? "
    sanity += "Remember: No decision is better than a confident decision on bad data. "
    sanity += "If trust is low → slow down, qualify, or re-measure."
    
    parts.append(sanity)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l1_csv(input_file, output_file):
    """Process L1 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l1_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/13_L1_data_trust.csv'
    output_file = 'pattern_bank_answered/13_L1_data_trust.csv'
    process_l1_csv(input_file, output_file)
