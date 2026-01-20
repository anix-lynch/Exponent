#!/usr/bin/env python3
"""
Generate short answers for P11 questions using the Stakeholder Alignment framework.
Each answer follows: Understand Incentives → Address Concerns → Build Coalition → Decide
with line breaks between sections.
"""

import csv

def generate_p11_short_answer(question_text, notes):
    """Generate a short answer following P11 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_conflict = any(word in question_lower for word in ['conflict', 'disagree', 'resistance', 'stuck', 'disagreement'])
    is_cross_functional = any(word in question_lower for word in ['cross-functional', 'team', 'department', 'engineering', 'stakeholder'])
    is_influence = any(word in question_lower for word in ['influence', 'without authority', 'negotiate', 'win-win'])
    is_collaboration = any(word in question_lower for word in ['work with', 'collaborate', 'together', 'partnership'])
    is_behavioral = any(word in question_lower for word in ['describe', 'situation', 'time when', 'example'])
    
    parts = []
    
    # 1. UNDERSTAND INCENTIVES (WHY each group cares)
    incentives = "Understand Incentives: Identify why each stakeholder cares. "
    incentives += "Identify stakeholders: Exec, Product, Engineering, Legal/Ops/Sales, Users. "
    incentives += "For each stakeholder: "
    incentives += "Goal: what success looks like for them. "
    incentives += "Fear: what they're protecting against. "
    incentives += "Power: can they block, influence, or approve? "
    incentives += "Map their incentives to understand motivations and constraints."
    
    parts.append(incentives)
    
    # 2. ADDRESS CONCERNS (REMOVE blockers)
    concerns = "Address Concerns: Remove blockers with specifics. "
    concerns += "Map objections: risk, cost, timeline, ownership. "
    concerns += "Respond with specifics: "
    concerns += "Data: where possible, use evidence to address concerns. "
    concerns += "Guardrails: what we won't do, boundaries we'll respect. "
    concerns += "Mitigations: how risk is contained, fallback plans. "
    concerns += "Language that works: 'Here's what I heard you're worried about...' "
    concerns += "'What would make this safe enough to try?'"
    
    parts.append(concerns)
    
    # 3. BUILD COALITION (CREATE momentum)
    coalition = "Build Coalition: Create momentum through strategic alignment. "
    coalition += "Secure early allies: "
    coalition += "Influential but reasonable stakeholders. "
    coalition += "Cross-functional credibility (people who can speak across teams). "
    coalition += "Sequence alignment: "
    coalition += "1:1s before group meetings (address concerns privately first). "
    coalition += "Incorporate feedback visibly (show you're listening). "
    coalition += "Let allies advocate publicly (they champion the idea)."
    
    parts.append(coalition)
    
    # 4. DECIDE (MOVE forward)
    decide = "Decide: Move forward with alignment (not consensus). "
    decide += "Restate shared goal: remind everyone what we're trying to achieve. "
    decide += "Present aligned proposal: show how concerns were addressed. "
    decide += "Call decision explicitly: make the decision clear, don't assume. "
    decide += "Document + communicate outcome: ensure no one is surprised. "
    decide += "Remember: Alignment ≠ consensus. Alignment = no one is surprised, and no one blocks."
    
    parts.append(decide)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p11_csv(input_file, output_file):
    """Process P11 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_p11_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/11_P11_stakeholder_alignment.csv'
    output_file = 'pattern_bank_answered/11_P11_stakeholder_alignment.csv'
    process_p11_csv(input_file, output_file)
