#!/usr/bin/env python3
"""
Generate short answers for L8 questions using the Market / Competitive Analysis framework.
Each answer follows: Competitors → Differentiation → Market Conditions → Strategy
with line breaks between sections.
"""

import csv

def generate_l8_short_answer(question_text, notes):
    """Generate a short answer following L8 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_competitor = any(word in question_lower for word in ['competitor', 'alternative', 'compete', 'rival'])
    is_market = any(word in question_lower for word in ['market', 'industry', 'sizing', 'demand', 'potential'])
    is_strategy = any(word in question_lower for word in ['strategy', 'position', 'differentiate', 'launch'])
    
    parts = []
    
    # 1. COMPETITORS (WHO are the alternatives?)
    competitors = "Competitors: Identify who the alternatives are. "
    competitors += "Direct: same user, same job (direct substitutes). "
    competitors += "Indirect: different product, same job (alternative solutions). "
    competitors += "Status quo: Excel, email, manual work, doing nothing. "
    competitors += "Remember: The real competitor is often the status quo. "
    competitors += "Map all options users have to solve their problem."
    
    parts.append(competitors)
    
    # 2. DIFFERENTIATION (WHY do users pick each?)
    differentiation = "Differentiation: Understand why users choose each option. "
    differentiation += "Price: cost, value proposition, pricing model. "
    differentiation += "Quality / Performance: features, speed, accuracy, reliability. "
    differentiation += "Convenience / UX: ease of use, time to value, user experience. "
    differentiation += "Trust / Brand: reputation, security, established presence. "
    differentiation += "Ecosystem / Lock-in: integrations, network effects, switching costs. "
    differentiation += "Rule: Features don't differentiate — reasons do. "
    differentiation += "People don't buy features — they buy outcomes. "
    differentiation += "Create a table: Option | Who uses it | Why they choose it | Weakness."
    
    parts.append(differentiation)
    
    # 3. MARKET CONDITIONS (WHAT environment are we in?)
    market = "Market Conditions: Assess the market environment. "
    market += "Market size & growth: TAM, SAM, growth rate, maturity. "
    market += "Buyer vs seller power: who has leverage, pricing dynamics. "
    market += "Switching costs: how easy/hard to switch, lock-in factors. "
    market += "Regulation / risk: compliance, legal constraints, regulatory environment. "
    market += "Network effects: yes/no, how strong, winner-take-all dynamics. "
    market += "Competitive intensity: number of players, barriers to entry, differentiation."
    
    parts.append(market)
    
    # 4. STRATEGY (SO WHAT do we do?)
    strategy = "Strategy: Define clear positioning and tradeoffs. "
    strategy += "Compete head-on: match competitors feature-for-feature, price-for-price. "
    strategy += "Focus on niche: target specific segment, underserved market. "
    strategy += "Undercut on cost: lower price, better value proposition. "
    strategy += "Differentiate on UX / trust: better experience, stronger brand. "
    strategy += "Bundle / unbundle: combine features or focus on core. "
    strategy += "Remember: Strategy is choosing what not to compete on. "
    strategy += "If there's no tradeoff, there's no strategy. "
    strategy += "Output: Clear positioning + tradeoffs. "
    strategy += "What's our sharp bet? What are we explicitly not doing?"
    
    parts.append(strategy)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l8_csv(input_file, output_file):
    """Process L8 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l8_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/19_L8_market_analysis.csv'
    output_file = 'pattern_bank_answered/19_L8_market_analysis.csv'
    process_l8_csv(input_file, output_file)
