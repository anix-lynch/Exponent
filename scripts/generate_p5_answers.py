#!/usr/bin/env python3
"""
Generate short answers for P5 questions using the Segmentation framework.
Each answer follows: (Persona × Behavior × Value) → Rank → Focus Top Segments
with line breaks between sections.
"""

import csv

def generate_p5_short_answer(question_text, notes):
    """Generate a short answer following P5 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_market = any(word in question_lower for word in ['market', 'geography', 'segment', 'target'])
    is_user = any(word in question_lower for word in ['user', 'customer', 'audience', 'persona'])
    is_churn = any(word in question_lower for word in ['churn', 'retention'])
    is_engagement = any(word in question_lower for word in ['engagement', 'improve'])
    is_ecommerce = any(word in question_lower for word in ['e-commerce', 'ecommerce', 'platform'])
    is_social = any(word in question_lower for word in ['social', 'instagram', 'whatsapp', 'facebook'])
    
    parts = []
    
    # 1. DEFINE PERSONAS (WHO)
    personas = "Define Personas (WHO): Identify distinct user groups. "
    if is_market:
        personas += "Demographics: age, role, company size, geographic region. "
        personas += "Context: job-to-be-done, use case, environment. "
        personas += "Needs and constraints: what they need, what limits them."
    elif is_ecommerce:
        personas += "Demographics: age, income, shopping frequency. "
        personas += "Context: shopping occasion (gift, personal, bulk), device preference. "
        personas += "Needs: price sensitivity, convenience, product discovery."
    elif is_social:
        personas += "Demographics: age, interests, social graph size. "
        personas += "Context: content consumption vs creation, platform usage pattern. "
        personas += "Needs: connection, entertainment, self-expression."
    else:
        personas += "Demographics: age, role, company size, location. "
        personas += "Context: job-to-be-done, environment, use case. "
        personas += "Needs and constraints: what they need, what limits them."
    
    parts.append(personas)
    
    # 2. DEFINE BEHAVIORS (HOW)
    behaviors = "Define Behaviors (HOW): Map how users interact. "
    behaviors += "Frequency: daily vs weekly vs occasional usage patterns. "
    behaviors += "Depth: light users (basic features) vs power users (advanced features). "
    behaviors += "Lifecycle stage: new users vs active users vs mature users. "
    if is_churn:
        behaviors += "Churn indicators: usage decline, feature abandonment, support ticket patterns."
    elif is_engagement:
        behaviors += "Engagement patterns: session frequency, feature adoption, content interaction."
    else:
        behaviors += "Usage patterns: feature adoption, session length, return frequency."
    
    parts.append(behaviors)
    
    # 3. DEFINE VALUE (WHY THEY MATTER)
    value = "Define Value (WHY THEY MATTER): Quantify segment importance. "
    if is_ecommerce:
        value += "Revenue: ARPU (average revenue per user), LTV (lifetime value), purchase frequency. "
        value += "Strategic value: growth potential, referral rate, network effects. "
        value += "Cost/risk: support cost, return rate, churn risk."
    elif is_social:
        value += "Revenue: ad engagement, premium subscription rate, creator revenue share. "
        value += "Strategic value: content creation, network effects, viral growth. "
        value += "Cost/risk: moderation cost, platform abuse, churn risk."
    else:
        value += "Revenue: ARPU, LTV, conversion rate, retention. "
        value += "Strategic value: growth potential, network effects, market position. "
        value += "Cost/risk: support cost, churn risk, acquisition cost."
    
    parts.append(value)
    
    # 4. COMBINE INTO SEGMENTS
    segments = "Combine into Segments: Create Persona × Behavior × Value matrix. "
    segments += "Example: Persona A × Behavior X × High Value = Segment 1. "
    segments += "Persona B × Behavior Y × Medium Value = Segment 2. "
    segments += "Persona C × Behavior Z × Low Value = Segment 3. "
    segments += "Each segment is a unique combination of who they are, how they behave, and why they matter."
    
    parts.append(segments)
    
    # 5. RANK SEGMENTS
    rank = "Rank Segments: Prioritize by impact and feasibility. "
    rank += "Impact on core metric: which segment moves the needle most? "
    rank += "Size and growth potential: current size and future growth trajectory. "
    rank += "Effort to serve: how much work to address this segment's needs? "
    rank += "Score: High Impact × Large Size × Low Effort = Top Priority."
    
    parts.append(rank)
    
    # 6. FOCUS
    focus = "Focus: Choose primary and secondary segments. "
    focus += "Primary segment: default design target, gets most resources. "
    focus += "Secondary segment: nice-to-have, addressed if resources allow. "
    focus += "Deprioritize or ignore: segments that don't rank high enough. "
    focus += "Design decisions should optimize for the primary segment first."
    
    parts.append(focus)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p5_csv(input_file, output_file):
    """Process P5 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_p5_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/05_P5_segmentation.csv'
    output_file = 'pattern_bank_answered/05_P5_segmentation.csv'
    process_p5_csv(input_file, output_file)
