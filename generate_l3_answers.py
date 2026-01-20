#!/usr/bin/env python3
"""
Generate short answers for L3 questions using the Cost / ROI framework.
Each answer follows: Cost Drivers → Benefits → Breakeven → Decide
with line breaks between sections.
"""

import csv

def generate_l3_short_answer(question_text, notes):
    """Generate a short answer following L3 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_cost = any(word in question_lower for word in ['cost', 'price', 'expense', 'spend', 'break even', 'breakeven'])
    is_revenue = any(word in question_lower for word in ['revenue', 'estimate revenue', 'advertising revenue'])
    is_roi = any(word in question_lower for word in ['roi', 'return', 'worth', 'value', 'acquisition'])
    is_estimation = any(word in question_lower for word in ['estimate', 'calculate', 'how much', 'market size', 'market'])
    is_behavioral = any(word in question_lower for word in ['describe', 'time when', 'identified'])
    
    parts = []
    
    # 1. COST DRIVERS (WHAT do we pay?)
    cost = "Cost Drivers: Identify what we pay. "
    cost += "Build cost: "
    cost += "Eng time: people × weeks (engineering effort). "
    cost += "Opportunity cost: what we don't build (tradeoffs). "
    cost += "One-time infra setup: initial infrastructure investment. "
    cost += "Run cost: "
    cost += "Compute / storage / bandwidth: ongoing infrastructure costs. "
    cost += "Third-party APIs: external service fees. "
    cost += "Support & ops: operational overhead, maintenance. "
    cost += "Risk cost: "
    cost += "Reliability risk: potential downtime, service degradation. "
    cost += "Compliance / legal: regulatory, legal exposure. "
    cost += "Brand damage: reputation risk, user trust impact."
    
    parts.append(cost)
    
    # 2. BENEFITS (WHAT do we gain?)
    benefits = "Benefits: Quantify what we gain. "
    benefits += "Revenue: "
    benefits += "New users: user acquisition, market expansion. "
    benefits += "Higher conversion: improved conversion rates. "
    benefits += "ARPU / LTV lift: average revenue per user, lifetime value increase. "
    benefits += "Cost savings: "
    benefits += "Automation: reduce manual work, operational efficiency. "
    benefits += "Infra reduction: lower infrastructure costs. "
    benefits += "Support deflection: fewer support tickets, self-service. "
    benefits += "Strategic: "
    benefits += "Learning: knowledge, insights, experimentation value. "
    benefits += "Moat / differentiation: competitive advantage. "
    benefits += "Risk reduction: mitigate existing risks."
    
    parts.append(benefits)
    
    # 3. BREAKEVEN (WHEN does it pay back?)
    breakeven = "Breakeven: Calculate when it pays back. "
    breakeven += "Simple math: "
    breakeven += "Monthly benefit: recurring value (revenue or savings). "
    breakeven += "Monthly cost: ongoing operational costs. "
    breakeven += "Payback period: build cost / monthly net benefit. "
    breakeven += "Sensitivity: "
    breakeven += "Best case: optimistic scenario (high adoption, high value). "
    breakeven += "Base case: realistic scenario (expected outcomes). "
    breakeven += "Worst case: pessimistic scenario (low adoption, high costs). "
    breakeven += "Sanity checks: Unit economics (does usage scale cost?), Reversibility (can we undo this?), Fixed vs variable (what grows with scale?)."
    
    parts.append(breakeven)
    
    # 4. DECIDE (WHAT do we do?)
    decide = "Decide: Choose path forward. "
    decide += "Greenlight: "
    decide += "Short payback: < 6-12 months typically acceptable. "
    decide += "Asymmetric upside: high potential reward vs risk. "
    decide += "Scope down: "
    decide += "MVP first: build minimal version to test assumptions. "
    decide += "Cheaper experiment: validate with lower investment. "
    decide += "Kill / Defer: "
    decide += "Long breakeven: payback period too long (> 18-24 months). "
    decide += "High downside: significant risk, low confidence. "
    decide += "Remember: ROI is not 'big upside.' It's 'good outcomes even if we're wrong.'"
    
    parts.append(decide)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l3_csv(input_file, output_file):
    """Process L3 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l3_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/15_L3_cost_roi.csv'
    output_file = 'pattern_bank_answered/15_L3_cost_roi.csv'
    process_l3_csv(input_file, output_file)
