#!/usr/bin/env python3
"""
Generate short answers for P6 questions using the Prioritization (RICE) framework.
Each answer follows: Impact × Confidence × Ease → RICE Score → Decide + Communicate
with line breaks between sections.
"""

import csv

def generate_p6_short_answer(question_text, notes):
    """Generate a short answer following P6 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_feature = any(word in question_lower for word in ['feature', 'build', 'develop', 'functionality'])
    is_task = any(word in question_lower for word in ['task', 'prioritize', 'roadmap', 'initiative'])
    is_resource = any(word in question_lower for word in ['resource', 'time', 'deadline', 'budget', 'cut'])
    is_conflict = any(word in question_lower for word in ['conflict', 'competing', 'conflicting', 'balance'])
    is_delegation = any(word in question_lower for word in ['delegate', 'handle personally', 'delegation'])
    
    parts = []
    
    # 1. LIST CANDIDATES
    candidates = "List Candidates: Identify all options to prioritize. "
    if is_feature:
        candidates += "List all features, improvements, or initiatives under consideration. "
        candidates += "Include: new features, improvements to existing features, technical debt, and foundational work."
    elif is_task:
        candidates += "List all tasks, projects, or initiatives competing for resources. "
        candidates += "Include: product roadmap items, engineering tasks, bugs, and leadership requests."
    elif is_resource:
        candidates += "List all options given the resource constraint. "
        candidates += "Consider: what can be cut, what must stay, and what can be delayed."
    else:
        candidates += "List all options, features, or initiatives that need prioritization. "
        candidates += "Be comprehensive: include all stakeholders' requests and internal initiatives."
    
    parts.append(candidates)
    
    # 2. SCORE EACH CANDIDATE
    score = "Score Each Candidate: Evaluate using RICE framework (Impact × Confidence × Ease). "
    score += "Impact (How big is the upside?): "
    score += "3 = massive user/business impact, 2 = meaningful but local, 1 = minor improvement. "
    score += "Confidence (How sure are we?): "
    score += "1.0 = strong data/past proof, 0.7 = some data/informed guess, 0.4 = mostly hypothesis. "
    score += "Ease (How hard is it?): "
    score += "3 = very easy/quick win, 2 = medium effort, 1 = hard/long-term. "
    score += "For each candidate, assign scores for Impact, Confidence, and Ease."
    
    parts.append(score)
    
    # 3. COMPUTE RICE
    compute = "Compute RICE: Calculate score for each candidate. "
    compute += "RICE = Impact × Confidence × Ease. "
    compute += "Example: Impact 3 × Confidence 0.9 × Ease 3 = RICE 8.1. "
    compute += "Higher RICE score = higher priority. "
    compute += "Calculate RICE for all candidates to enable objective comparison."
    
    parts.append(compute)
    
    # 4. RANK BY RICE SCORE
    rank = "Rank by RICE Score: Sort candidates from highest to lowest RICE. "
    rank += "Top candidates: highest RICE scores get priority. "
    rank += "Review the ranking: does it align with strategic goals? "
    rank += "Consider adjustments: if strategic importance differs from RICE, note why."
    
    parts.append(rank)
    
    # 5. DECIDE + COMMUNICATE
    decide = "Decide + Communicate: Make clear decisions and explain tradeoffs. "
    if is_resource:
        decide += "What we do first: highest RICE items that fit within constraints. "
        decide += "What we delay: lower RICE items that can wait. "
        decide += "What we cut: lowest RICE items or items that don't fit constraints. "
        decide += "Why: explain the RICE rationale and resource limitations clearly to stakeholders."
    elif is_conflict:
        decide += "What we prioritize: highest RICE items that align with core goals. "
        decide += "What we deprioritize: lower RICE items or conflicting requests. "
        decide += "Why: explain RICE scores and how they resolve the conflict. "
        decide += "Communicate tradeoffs: what we're saying yes to and what we're saying no to."
    elif is_delegation:
        decide += "What I handle: high-impact, high-confidence items that need my expertise. "
        decide += "What I delegate: lower-impact items or items where others have more expertise. "
        decide += "Why: explain based on impact, my unique value, and team capacity."
    else:
        decide += "What we do first: highest RICE items that maximize impact. "
        decide += "What we delay: lower RICE items that can wait for next cycle. "
        decide += "Why: explain RICE scores and strategic rationale to stakeholders."
    
    parts.append(decide)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p6_csv(input_file, output_file):
    """Process P6 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_p6_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/06_P6_prioritization.csv'
    output_file = 'pattern_bank_answered/06_P6_prioritization.csv'
    process_p6_csv(input_file, output_file)
