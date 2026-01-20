#!/usr/bin/env python3
"""
Generate short answers for L6 questions using the Ops Tradeoffs framework.
Each answer follows: Speed vs Quality vs Reliability → SLAs → Error Budget → Decide
with line breaks between sections.
"""

import csv

def generate_l6_short_answer(question_text, notes):
    """Generate a short answer following L6 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_speed = any(word in question_lower for word in ['speed', 'fast', 'quick', 'rapid', 'deploy', 'release'])
    is_quality = any(word in question_lower for word in ['quality', 'bug', 'correctness', 'test', 'polish'])
    is_reliability = any(word in question_lower for word in ['reliability', 'uptime', 'stability', 'available', 'downtime'])
    is_sla = any(word in question_lower for word in ['sla', 'slo', 'error budget', 'service level'])
    
    parts = []
    
    # 1. SPEED VS QUALITY VS RELIABILITY (pick the tension)
    tradeoff = "Speed vs Quality vs Reliability: Identify the tension. "
    tradeoff += "Speed: "
    tradeoff += "Fast deploys: rapid iteration, quick releases. "
    tradeoff += "Rapid iteration: fast feedback loops, quick experiments. "
    tradeoff += "Short time-to-market: get features to users quickly. "
    tradeoff += "Quality: "
    tradeoff += "Fewer bugs: thorough testing, code review. "
    tradeoff += "Correctness: accuracy, data integrity. "
    tradeoff += "User trust: reliable experience, consistent behavior. "
    tradeoff += "Reliability: "
    tradeoff += "Uptime: high availability, minimal downtime. "
    tradeoff += "Consistency: predictable performance, stable behavior. "
    tradeoff += "Predictability: users know what to expect. "
    tradeoff += "Rule: You can maximize 2, never all 3. "
    tradeoff += "Make the tradeoff explicit: which two are we optimizing for?"
    
    parts.append(tradeoff)
    
    # 2. SLAs / SLOs (WHAT do we promise?)
    sla = "SLAs / SLOs: Define what we promise. "
    sla += "SLI (signal): "
    sla += "Availability: uptime percentage, service availability. "
    sla += "Latency: response time, p50/p95/p99. "
    sla += "Success rate: percentage of successful requests. "
    sla += "SLO (target): "
    sla += "99.9% uptime: availability target. "
    sla += "p95 < 300ms: latency target. "
    sla += "<0.1% errors: error rate target. "
    sla += "SLA (external promise): "
    sla += "What customers can hold you to: contractual commitments, penalties for violations."
    
    parts.append(sla)
    
    # 3. ERROR BUDGET (HOW much can we break?)
    budget = "Error Budget: Define how much we can break. "
    budget += "Error Budget = 1 − SLO. "
    budget += "99.9% SLO → 0.1% budget (permission to move fast). "
    budget += "Budget = permission to ship, experiment, take risks. "
    budget += "Budget healthy? "
    budget += "YES → Ship faster, experiment more, iterate quickly. "
    budget += "NO → Freeze launches, fix reliability, slow down. "
    budget += "Shared contract: "
    budget += "Product wants speed: features, iterations. "
    budget += "Ops wants stability: reliability, uptime. "
    budget += "Error budget aligns both: speed allowed until budget is gone."
    
    parts.append(budget)
    
    # 4. DECIDE + COMMUNICATE
    decide = "Decide + Communicate: Make tradeoff explicit and align stakeholders. "
    decide += "Make tradeoff explicit: clearly state which two we're optimizing for. "
    decide += "Align stakeholders: get agreement on priorities, SLAs, error budget. "
    decide += "Revisit when conditions change: startup vs mature product, incident vs normal operations. "
    decide += "When to bias each side: "
    decide += "Early startup → Speed. "
    decide += "Regulated / payments system → Reliability. "
    decide += "Core user-facing feature → Quality. "
    decide += "Incident ongoing → Reliability. "
    decide += "Innovation window open → Speed. "
    decide += "Remember: If tradeoffs are implicit, someone is silently paying the cost (usually users or on-call)."
    
    parts.append(decide)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l6_csv(input_file, output_file):
    """Process L6 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l6_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/17_L6_ops_tradeoffs.csv'
    output_file = 'pattern_bank_answered/17_L6_ops_tradeoffs.csv'
    process_l6_csv(input_file, output_file)
