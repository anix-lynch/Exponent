#!/usr/bin/env python3
"""
Generate short answers for L9 questions using the Financial Sensitivity framework.
Each answer follows: Levers (Price, Volume, Churn) → Impact → Prioritize
with line breaks between sections.
"""

import csv

def generate_l9_short_answer(question_text, notes):
    """Generate a short answer following L9 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_revenue = any(word in question_lower for word in ['revenue', 'monetize', 'profit', 'ltv', 'lifetime value'])
    is_pricing = any(word in question_lower for word in ['price', 'pricing', 'payment', 'cost', 'aov', 'order value'])
    is_growth = any(word in question_lower for word in ['increase', 'grow', 'triple', 'double', 'maximize'])
    is_subscription = any(word in question_lower for word in ['subscription', 'retention', 'churn'])
    
    parts = []
    
    # 1. IDENTIFY LEVERS (WHAT can move?)
    levers = "Identify Levers: Determine what can move the business outcome. "
    levers += "Price: "
    levers += "ARPU (average revenue per user), fees, discounting, pricing tiers. "
    levers += "Volume: "
    levers += "Users, orders, sessions, transactions, engagement. "
    levers += "Churn: "
    levers += "Retention, repeat rate, lifetime value, customer lifetime. "
    levers += "Each lever can impact revenue/profitability, but with different sensitivity and constraints."
    
    parts.append(levers)
    
    # 2. SENSITIVITY TEST (HOW sensitive is outcome?)
    sensitivity = "Sensitivity Test: Assess how sensitive the outcome is to each lever. "
    sensitivity += "+1% Price → Δ Revenue? (price elasticity, churn risk). "
    sensitivity += "+1% Volume → Δ Revenue? (scalability, marginal cost). "
    sensitivity += "-1% Churn → Δ LTV? (lifetime value impact, compounding effect). "
    sensitivity += "Rule: Use direction + relative size, not exact math. "
    sensitivity += "Sensitivity beats precision early on. "
    sensitivity += "Small churn changes compound more than price hikes. "
    sensitivity += "Not all growth is profitable growth."
    
    parts.append(sensitivity)
    
    # 3. CONSTRAINTS (WHAT limits each lever?)
    constraints = "Constraints: Identify what limits each lever. "
    constraints += "Price elasticity: how much demand drops with price increase. "
    constraints += "Supply / ops limits: capacity constraints, operational bottlenecks. "
    constraints += "Market saturation: addressable market size, growth ceiling. "
    constraints += "Competitive response: how competitors react to changes. "
    constraints += "Switching costs: how easy/hard for users to leave. "
    constraints += "Regulatory / legal: pricing regulations, compliance limits."
    
    parts.append(constraints)
    
    # 4. PRIORITIZE (WHERE do we focus?)
    prioritize = "Prioritize: Focus on highest-impact lever. "
    prioritize += "High impact × low risk first: maximize outcome while minimizing downside. "
    prioritize += "Short-term vs long-term split: balance immediate gains with sustainable growth. "
    prioritize += "One primary lever (not all): pick one lever to lead, others to support. "
    prioritize += "Quick sensitivity grid: "
    prioritize += "Price: High impact, High risk, Medium control → Careful. "
    prioritize += "Volume: Medium impact, Medium risk, Low control → Secondary. "
    prioritize += "Churn: High impact, Low risk, High control → Primary (often). "
    prioritize += "Output: 'We focus on X because it moves Y the most.' "
    prioritize += "Remember: Pick one lever to lead, others to support."
    
    parts.append(prioritize)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l9_csv(input_file, output_file):
    """Process L9 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l9_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/20_L9_financial_sensitivity.csv'
    output_file = 'pattern_bank_answered/20_L9_financial_sensitivity.csv'
    process_l9_csv(input_file, output_file)
