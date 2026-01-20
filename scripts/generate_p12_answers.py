#!/usr/bin/env python3
"""
Generate short answers for P12 questions using the Operational Excellence framework.
Each answer follows: Assess Current State → Identify Risks → Prioritize Fixes → Communicate Plan → Monitor
with line breaks between sections.
"""

import csv

def generate_p12_short_answer(question_text, notes):
    """Generate a short answer following P12 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_crisis = any(word in question_lower for word in ['fail', 'failure', 'broken', 'crisis', 'emergency', 'release day'])
    is_launch = any(word in question_lower for word in ['launch', 'go-to-market', 'gtm', 'release', 'ship'])
    is_operational = any(word in question_lower for word in ['operational', 'reliability', 'system', 'scale', 'monitor'])
    is_process = any(word in question_lower for word in ['process', 'inefficiency', 'improve', 'optimize'])
    is_behavioral = any(word in question_lower for word in ['describe', 'situation', 'time when', 'project'])
    
    parts = []
    
    # 1. ASSESS CURRENT STATE (WHAT is actually happening)
    assess = "Assess Current State: Understand what's actually happening. "
    assess += "Define scope: "
    assess += "Product / system boundaries: what's in scope, what's out. "
    assess += "Owners: who's on-call / accountable. "
    assess += "SLAs / expectations: what are the performance targets? "
    assess += "Baseline health: "
    assess += "Availability: uptime, error rates. "
    assess += "Performance: latency, throughput. "
    assess += "Quality: bugs, data correctness. "
    assess += "Operations: on-call load, manual work."
    
    parts.append(assess)
    
    # 2. IDENTIFY RISKS (WHAT could break)
    risks = "Identify Risks: Enumerate what could break. "
    risks += "Enumerate failure modes: "
    risks += "Technical: scaling issues, dependencies, infrastructure. "
    risks += "Data: freshness, correctness, completeness. "
    risks += "Process: handoffs, approvals, manual steps. "
    risks += "People: bus factor, burnout, knowledge gaps. "
    risks += "For each risk: "
    risks += "Likelihood: how probable is this failure? "
    risks += "Impact: blast radius (how many users/features affected). "
    risks += "Detection difficulty: how fast would we notice?"
    
    parts.append(risks)
    
    # 3. PRIORITIZE FIXES (WHAT to fix first)
    prioritize = "Prioritize Fixes: Rank and choose actions. "
    prioritize += "Rank risks by: "
    prioritize += "Impact × Likelihood (high priority = high impact × high likelihood). "
    prioritize += "Time-to-detect × Time-to-recover (faster detection/recovery = better). "
    prioritize += "Choose actions: "
    prioritize += "Prevent: design changes, architecture improvements, automation. "
    prioritize += "Detect: metrics, alerts, monitoring, dashboards. "
    prioritize += "Respond: runbooks, automation, clear ownership, escalation paths."
    
    parts.append(prioritize)
    
    # 4. COMMUNICATE PLAN (ALIGN execution)
    communicate = "Communicate Plan: Align execution with stakeholders. "
    communicate += "What we're fixing now vs later: prioritize by impact and urgency. "
    communicate += "Owners and timelines: who owns what, when will it be done. "
    communicate += "Tradeoffs accepted: what risks are we explicitly accepting. "
    communicate += "Escalation paths: who to contact if things go wrong. "
    communicate += "Language that works: 'What's the blast radius if this fails?' "
    communicate += "'How would we know this is broken at 3am?' 'What's our fastest safe rollback?'"
    
    parts.append(communicate)
    
    # 5. MONITOR (KEEP it healthy)
    monitor = "Monitor: Keep system healthy over time. "
    monitor += "Track leading indicators: metrics that predict problems before they happen. "
    monitor += "Review incidents + near-misses: learn from failures, update processes. "
    monitor += "Update runbooks: keep documentation current as system evolves. "
    monitor += "Revisit risks regularly: quarterly risk review, update mitigation plans. "
    monitor += "Remember: Operational excellence ≠ zero failures. "
    monitor += "Operational excellence = fail small, detect fast, recover predictably."
    
    parts.append(monitor)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p12_csv(input_file, output_file):
    """Process P12 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_p12_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/12_P12_operational_excellence.csv'
    output_file = 'pattern_bank_answered/12_P12_operational_excellence.csv'
    process_p12_csv(input_file, output_file)
