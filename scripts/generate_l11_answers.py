#!/usr/bin/env python3
"""
Generate short answers for L11 questions using the Risk Mitigation framework.
Each answer follows: Enumerate Risks → Blast Radius → Mitigations → Monitor
with line breaks between sections.
"""

import csv

def generate_l11_short_answer(question_text, notes):
    """Generate a short answer following L11 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_ai = any(word in question_lower for word in ['ai', 'llm', 'model', 'generative', 'agentic'])
    is_data = any(word in question_lower for word in ['data', 'privacy', 'gdpr', 'pii', 'leakage'])
    is_security = any(word in question_lower for word in ['security', 'attack', 'adversarial', 'safe', 'protect'])
    is_content = any(word in question_lower for word in ['content', 'upload', 'moderation', 'harmful', 'unsafe'])
    is_operational = any(word in question_lower for word in ['bug', 'downtime', 'migration', 'decommission', 'production'])
    is_compliance = any(word in question_lower for word in ['compliance', 'regulatory', 'legal', 'ethical', 'responsible'])
    
    parts = []
    
    # 1. ENUMERATE RISKS (LIST before judging)
    risks = "Enumerate Risks: List all potential risks before judging. "
    risks += "Technical: bugs, downtime, data loss, performance degradation, system failures. "
    risks += "Data: quality issues, drift, leakage, bias, completeness, freshness. "
    risks += "Operational: on-call load, handoffs, manual processes, capacity limits. "
    risks += "Legal / Compliance: PII exposure, regulatory violations, privacy breaches. "
    risks += "Business: revenue loss, user trust erosion, reputation damage, competitive disadvantage. "
    if is_ai:
        risks += "AI-specific: model drift, bias, adversarial attacks, hallucination, misuse. "
    if is_content:
        risks += "Content-specific: harmful content, spam, abuse, copyright violations. "
    risks += "Rule: If you can't name it, you can't manage it. "
    risks += "Be comprehensive: don't skip categories."
    
    parts.append(risks)
    
    # 2. ASSESS BLAST RADIUS (HOW bad is it?)
    blast = "Assess Blast Radius: Evaluate how bad each risk is. "
    blast += "Users affected: 1% vs 100%, specific segments vs all users. "
    blast += "Duration: minutes vs hours vs weeks, temporary vs permanent. "
    blast += "Reversibility: easy rollback vs permanent damage, recoverable vs irreversible. "
    blast += "Visibility: internal vs public, contained vs widespread. "
    blast += "Output: Risk = Probability × Impact. "
    blast += "Rank risks: High impact + high probability → critical. "
    blast += "High impact + low probability → plan for. "
    blast += "Low impact + high probability → automate handling. "
    blast += "Low impact + low probability → accept."
    
    parts.append(blast)
    
    # 3. MITIGATE (REDUCE impact or probability)
    mitigate = "Mitigate: Reduce impact or probability of risks. "
    mitigate += "Prevent: guardrails, validation, limits, access controls. "
    mitigate += "Detect: monitoring, alerts, anomaly detection, early warning systems. "
    mitigate += "Contain: rate limits, feature flags, circuit breakers, isolation. "
    mitigate += "Recover: rollback procedures, backups, runbooks, incident response. "
    if is_ai:
        mitigate += "AI-specific: shadow deploys, canary rollouts, drift monitoring, bias testing, output filtering. "
    if is_data:
        mitigate += "Data-specific: encryption, access controls, audit logs, data minimization, anonymization. "
    if is_content:
        mitigate += "Content-specific: pre-moderation, post-moderation, automated filters, human review, user reporting. "
    mitigate += "Layered approach: multiple mitigations for high-risk items. "
    mitigate += "Remember: You don't eliminate risk — you bound it."
    
    parts.append(mitigate)
    
    # 4. MONITOR (ASSUME failure will happen)
    monitor = "Monitor: Assume failure will happen and prepare detection. "
    monitor += "Early warning metrics: leading indicators that predict problems. "
    monitor += "Alert thresholds: when to trigger alerts, escalation criteria. "
    monitor += "Clear owner + escalation path: who responds, how to escalate. "
    monitor += "Detection speed matters more than perfection. "
    monitor += "Output: 'If X happens, we detect in Y mins and recover in Z.' "
    monitor += "Test monitoring: verify alerts work, runbooks are current, owners are reachable."
    
    parts.append(monitor)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l11_csv(input_file, output_file):
    """Process L11 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l11_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/22_L11_risk_mitigation.csv'
    output_file = 'pattern_bank_answered/22_L11_risk_mitigation.csv'
    process_l11_csv(input_file, output_file)
