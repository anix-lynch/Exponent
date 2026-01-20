#!/usr/bin/env python3
"""
Generate short answers for P10 questions using the Executive Communication framework.
Each answer follows: Context → Insight → Recommendation → Next Steps
with line breaks between sections.
"""

import csv

def generate_p10_short_answer(question_text, notes):
    """Generate a short answer following P10 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_technical = any(word in question_lower for word in ['technical', 'explain', 'non-technical', 'layman', 'grandmother', 'five-year-old'])
    is_presentation = any(word in question_lower for word in ['present', 'sell', 'pitch', 'slide', 'communicate'])
    is_explanation = any(word in question_lower for word in ['explain', 'describe', 'convey', 'demonstrate'])
    is_executive = any(word in question_lower for word in ['executive', 'c-suite', 'leadership', 'senior management', 'board'])
    is_insight = any(word in question_lower for word in ['insight', 'drop', 'revenue', 'success', 'results'])
    
    parts = []
    
    # 1. CONTEXT (WHY this matters)
    context = "Context: Set the frame with one-sentence situation. "
    if is_technical:
        context += "What needs to be explained? Why does the audience need to understand this? "
        context += "What's at stake? (decision-making, alignment, buy-in). "
        context += "Set the frame: business goal (decision support, alignment, education). "
        context += "Decision owner / timeline: who needs to understand and by when?"
    elif is_presentation:
        context += "What decision needs to be made? Why now? "
        context += "What's at stake? (revenue, growth, risk, efficiency). "
        context += "Set the frame: business goal and decision owner / timeline."
    elif is_insight:
        context += "What changed? Why now? What's at stake? "
        context += "Set the frame: business goal (revenue, growth, risk, efficiency). "
        context += "Decision owner / timeline: who needs to act and when?"
    else:
        context += "One-sentence situation: what changed, why now, what's at stake? "
        context += "Set the frame: business goal (revenue, growth, risk, efficiency). "
        context += "Decision owner / timeline."
    
    parts.append(context)
    
    # 2. INSIGHT (WHAT we learned)
    insight = "Insight: Share 2-3 facts only (no analysis dump). "
    if is_technical:
        insight += "Data signal: what the concept is, why it matters. "
        insight += "User / market signal: how it applies to business context. "
        insight += "Constraint or risk: what limitations or considerations exist. "
        insight += "Translate data → meaning: 'This means...' 'The implication is...'"
    elif is_presentation:
        insight += "Data signal: key metrics, trends, or findings. "
        insight += "User / market signal: user feedback, market dynamics. "
        insight += "Constraint or risk: limitations, dependencies, risks. "
        insight += "Translate data → meaning: 'This means...' 'The implication is...'"
    elif is_insight:
        insight += "Data signal: what the numbers show, key trends. "
        insight += "User / market signal: user behavior, market changes. "
        insight += "Constraint or risk: what's limiting or risky. "
        insight += "Translate data → meaning: 'This means...' 'The implication is...'"
    else:
        insight += "2-3 facts only: data signal, user/market signal, constraint or risk. "
        insight += "Translate data → meaning: 'This means...' 'The implication is...'"
    
    parts.append(insight)
    
    # 3. RECOMMENDATION (WHAT to do)
    recommendation = "Recommendation: Clear decision with rationale. "
    if is_technical:
        recommendation += "Clear decision: how to explain the concept (analogy, simple terms, visual). "
        recommendation += "Why this is right: connects to audience's context, builds understanding. "
        recommendation += "Upside: enables decision-making, alignment, buy-in. "
        recommendation += "Risk: acknowledge complexity, potential misunderstandings. "
        recommendation += "Why alternatives are worse: too technical, too abstract, missing context."
    elif is_presentation:
        recommendation += "Clear decision: do X, do X over Y (explicit tradeoff), do X now not later. "
        recommendation += "Why this is right: upside, risk (acknowledged not hidden), why alternatives are worse."
    elif is_insight:
        recommendation += "Clear decision: what action to take based on insights. "
        recommendation += "Why this is right: upside, risk (acknowledged), why alternatives are worse."
    else:
        recommendation += "Clear decision: do X, do X over Y, do X now. "
        recommendation += "Why this is right: upside, risk (acknowledged), why alternatives are worse."
    
    parts.append(recommendation)
    
    # 4. NEXT STEPS (HOW it happens)
    next_steps = "Next Steps: Immediate actions with ownership and metrics. "
    next_steps += "Immediate actions: 30-60-90 day plan. "
    next_steps += "Owner(s): who is responsible. "
    next_steps += "Success metric: how we measure success. "
    next_steps += "Decision checkpoints / update cadence: when we review progress."
    
    parts.append(next_steps)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p10_csv(input_file, output_file):
    """Process P10 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_p10_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/10_P10_executive_communication.csv'
    output_file = 'pattern_bank_answered/10_P10_executive_communication.csv'
    process_p10_csv(input_file, output_file)
