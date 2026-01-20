#!/usr/bin/env python3
"""
Generate short answers for L4 questions using the Constraints framework.
Each answer follows: Legal → Technical → Organizational → Timeline → Prioritize
with line breaks between sections.
"""

import csv

def generate_l4_short_answer(question_text, notes):
    """Generate a short answer following L4 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_legal = any(word in question_lower for word in ['gdpr', 'compliance', 'legal', 'regulatory', 'privacy', 'ccpa', 'hipaa'])
    is_technical = any(word in question_lower for word in ['technical', 'system', 'architecture', 'migration', 'pipeline', 'infrastructure'])
    is_organizational = any(word in question_lower for word in ['team', 'organization', 'stakeholder', 'approval', 'process'])
    is_timeline = any(word in question_lower for word in ['deadline', 'timeline', 'schedule', 'launch', 'migration'])
    
    parts = []
    
    # 1. LEGAL / REGULATORY (WHAT are we not allowed to do?)
    legal = "Legal / Regulatory: Identify what we're not allowed to do. "
    legal += "Compliance: "
    legal += "GDPR / CCPA / HIPAA: data privacy regulations, consent requirements. "
    legal += "Data residency: where data can be stored, processed. "
    legal += "Consent requirements: explicit user consent for data usage. "
    legal += "Contracts: "
    legal += "Vendor terms: third-party service agreements, limitations. "
    legal += "Partner SLAs: service level agreements, commitments. "
    legal += "Licensing limits: software licenses, usage restrictions. "
    legal += "Risk exposure: "
    legal += "Fines / penalties: regulatory fines for non-compliance. "
    legal += "Lawsuits: legal action, liability. "
    legal += "Regulatory scrutiny: increased oversight, audits."
    
    parts.append(legal)
    
    # 2. TECHNICAL (WHAT can't the system do today?)
    technical = "Technical: Identify what the system can't do today. "
    technical += "Architecture: "
    technical += "Legacy systems: old systems that are hard to change. "
    technical += "Tight coupling: dependencies that limit flexibility. "
    technical += "Data quality gaps: missing, incomplete, or unreliable data. "
    technical += "Scale limits: "
    technical += "Latency: response time constraints. "
    technical += "Throughput: processing capacity limits. "
    technical += "Reliability: uptime, error rate constraints. "
    technical += "Dependencies: "
    technical += "External APIs: third-party service availability, rate limits. "
    technical += "Data availability: when data is available, freshness. "
    technical += "Infra readiness: infrastructure capacity, capabilities."
    
    parts.append(technical)
    
    # 3. ORGANIZATIONAL (WHO blocks or enables this?)
    organizational = "Organizational: Identify who blocks or enables this. "
    organizational += "People: "
    organizational += "Hiring gaps: missing skills, headcount constraints. "
    organizational += "Specialized expertise: domain knowledge, technical skills. "
    organizational += "On-call ownership: who maintains and supports this. "
    organizational += "Incentives: "
    organizational += "Team OKRs misaligned: different priorities across teams. "
    organizational += "Competing priorities: other work takes precedence. "
    organizational += "Political resistance: organizational pushback. "
    organizational += "Process: "
    organizational += "Review cycles: approval processes, gate reviews. "
    organizational += "Approval chains: multiple stakeholders, sign-offs. "
    organizational += "Cross-team coordination: dependencies on other teams."
    
    parts.append(organizational)
    
    # 4. TIMELINE (WHEN does this break?)
    timeline = "Timeline: Identify when this breaks. "
    timeline += "Fixed deadlines: "
    timeline += "Launch dates: product launch, feature release dates. "
    timeline += "Regulatory deadlines: compliance requirements, legal dates. "
    timeline += "Contract renewals: vendor contracts, partnership agreements. "
    timeline += "Sequencing: "
    timeline += "Must-do-first work: prerequisites, dependencies. "
    timeline += "Long-lead items: things that take time to prepare. "
    timeline += "Critical path: work that blocks everything else. "
    timeline += "Opportunity cost: "
    timeline += "What slips if this ships? Other work that gets delayed. "
    timeline += "What breaks if it's late? Consequences of delay."
    
    parts.append(timeline)
    
    # 5. PRIORITIZE (WHAT do we do about it?)
    prioritize = "Prioritize: Decide what to do about constraints. "
    prioritize += "Hard constraints (NON-NEGOTIABLE): "
    prioritize += "Legal / safety: must comply, cannot compromise. "
    prioritize += "External deadlines: fixed dates we can't change. "
    prioritize += "Soft constraints (NEGOTIABLE): "
    prioritize += "Scope: can reduce features, simplify. "
    prioritize += "UX polish: can defer nice-to-haves. "
    prioritize += "Internal tooling: can use workarounds. "
    prioritize += "Strategy: "
    prioritize += "Redesign to avoid constraint: change approach to work around limitation. "
    prioritize += "Phase rollout: launch in stages, address constraints incrementally. "
    prioritize += "Explicitly accept risk: acknowledge constraint and proceed with mitigation. "
    prioritize += "Remember: Constraints are not excuses. They are design inputs. "
    prioritize += "Good answers say what you'll trade, not just what you can't do."
    
    parts.append(prioritize)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l4_csv(input_file, output_file):
    """Process L4 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l4_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/16_L4_constraints.csv'
    output_file = 'pattern_bank_answered/16_L4_constraints.csv'
    process_l4_csv(input_file, output_file)
