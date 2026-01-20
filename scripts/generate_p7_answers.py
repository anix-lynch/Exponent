#!/usr/bin/env python3
"""
Generate short answers for P7 questions using the Tradeoff Framing framework.
Each answer follows: Define Options → Winners/Losers → Guardrails → Decide + Communicate
with line breaks between sections.
"""

import csv

def generate_p7_short_answer(question_text, notes):
    """Generate a short answer following P7 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_market_entry = any(word in question_lower for word in ['enter', 'market', 'expand', 'launch'])
    is_feature = any(word in question_lower for word in ['feature', 'introduce', 'add', 'implement'])
    is_pricing = any(word in question_lower for word in ['pricing', 'monetize', 'revenue', 'ads'])
    is_build_buy = any(word in question_lower for word in ['build', 'buy', 'partner', 'partnership'])
    is_strategic = any(word in question_lower for word in ['strategy', 'decision', 'should', 'whether'])
    
    parts = []
    
    # 1. DEFINE OPTIONS
    options = "Define Options: Clearly state the choices. "
    if is_market_entry:
        options += "Option A: Enter the market / expand. "
        options += "Option B: Stay focused / don't enter. "
        options += "Consider: timing, resources, competitive landscape."
    elif is_feature:
        options += "Option A: Launch / implement the feature. "
        options += "Option B: Don't launch / delay. "
        options += "Consider: user need, effort, strategic fit."
    elif is_pricing:
        options += "Option A: Introduce monetization (ads, premium, etc.). "
        options += "Option B: Keep free / current model. "
        options += "Consider: user experience, revenue potential, market position."
    elif is_build_buy:
        options += "Option A: Build internally. "
        options += "Option B: Buy / acquire. "
        options += "Option C: Partner / integrate. "
        options += "Consider: time, cost, control, expertise."
    else:
        options += "Option A: First choice / approach. "
        options += "Option B: Alternative choice / approach. "
        options += "Option C: Third option if applicable. "
        options += "Clearly define what each option entails."
    
    parts.append(options)
    
    # 2. WINNERS / LOSERS (by option)
    winners = "Winners / Losers: Analyze impact by stakeholder for each option. "
    winners += "For each option, evaluate: "
    winners += "Users: who benefits, who loses, experience impact. "
    winners += "Business: revenue impact, cost impact, strategic value. "
    winners += "Engineering / Ops: effort, complexity, maintenance burden. "
    winners += "Long-term Strategy: competitive position, market dynamics, future flexibility. "
    winners += "Be explicit about tradeoffs: what each option gains and gives up."
    
    parts.append(winners)
    
    # 3. GUARDRAILS (non-negotiables)
    guardrails = "Guardrails: Define non-negotiables and constraints. "
    if is_pricing:
        guardrails += "Must not break: user trust, core experience, brand integrity. "
        guardrails += "Must stay within: acceptable UX degradation, user expectations. "
        guardrails += "Must protect: user privacy, data security, long-term relationship."
    elif is_feature:
        guardrails += "Must not break: core product experience, user trust, performance. "
        guardrails += "Must stay within: technical constraints, resource limits. "
        guardrails += "Must protect: user data, platform stability, strategic goals."
    elif is_market_entry:
        guardrails += "Must not break: brand reputation, core business, financial health. "
        guardrails += "Must stay within: budget, resource capacity, risk tolerance. "
        guardrails += "Must protect: existing customers, competitive position, long-term viability."
    else:
        guardrails += "Must not break: core user experience, business fundamentals, trust. "
        guardrails += "Must stay within: resource constraints, risk tolerance, strategic boundaries. "
        guardrails += "Must protect: key stakeholders, long-term goals, competitive position."
    
    parts.append(guardrails)
    
    # 4. DECIDE + COMMUNICATE
    decide = "Decide + Communicate: Make clear decision and explain rationale. "
    decide += "Pick option: choose based on winners/losers analysis and guardrails. "
    decide += "Why this option: explain primary rationale (revenue, user value, strategic fit). "
    decide += "What we're giving up: acknowledge tradeoffs explicitly. "
    decide += "How we'll monitor risk: define metrics to track guardrails and success. "
    decide += "Communicate clearly: explain decision, tradeoffs, and monitoring plan to stakeholders."
    
    parts.append(decide)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p7_csv(input_file, output_file):
    """Process P7 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_p7_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/07_P7_tradeoff_framing.csv'
    output_file = 'pattern_bank_answered/07_P7_tradeoff_framing.csv'
    process_p7_csv(input_file, output_file)
