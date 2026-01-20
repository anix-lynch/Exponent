#!/usr/bin/env python3
"""
Generate short answers for L12 questions using the Metrics Interpretation framework.
Each answer follows: Metric Moved → Proxy Validity → Gaming Risk → Decide
with line breaks between sections.
"""

import csv

def generate_l12_short_answer(question_text, notes):
    """Generate a short answer following L12 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_simpson = 'simpson' in notes_lower or 'paradox' in notes_lower
    is_aggregation = any(word in question_lower for word in ['overall', 'aggregate', 'total', 'combined'])
    is_segmentation = any(word in question_lower for word in ['segment', 'group', 'department', 'category'])
    is_rate = any(word in question_lower for word in ['rate', 'percentage', 'ratio', 'acceptance'])
    
    parts = []
    
    # 1. METRIC MOVED (WHAT exactly changed?) - 5 bullets max
    metric_lines = []
    metric_lines.append("📊 Metric Moved: Identify what exactly changed")
    metric_lines.append("  📈 Direction: up / down / flat, which direction did the metric move?")
    metric_lines.append("  📏 Magnitude: small blip vs step-change, how significant is the change?")
    metric_lines.append("  🎯 Scope: which segment, surface, cohort, where is the change happening?")
    metric_lines.append("  ⏰ Time: one day spike vs sustained trend, is this temporary or ongoing?")
    if is_aggregation and is_segmentation:
        metric_lines.append("  🔀 Aggregation level: overall metric vs segment-level metrics, check for Simpson's paradox")
    metric_lines.append("  ⚠️ Rule: Never react to a single datapoint")
    parts.append("\n".join(metric_lines))
    
    # 2. PROXY VALIDITY (DOES this metric mean what we think?) - 5 bullets max
    proxy_lines = []
    proxy_lines.append("🔍 Proxy Validity: Verify if this metric means what we think it means")
    proxy_lines.append("  🎯 Is it a proxy or the real goal? Is this metric a stand-in for something else, or the actual outcome?")
    proxy_lines.append("  📈 How tightly correlated to value? Does this metric actually predict business value or user satisfaction?")
    proxy_lines.append("  ⏭️ Leading vs lagging? Is this a leading indicator (predicts future) or lagging indicator (reflects past)?")
    proxy_lines.append("  👁️ Any known blind spots? Are there scenarios where this metric is misleading or incomplete?")
    proxy_lines.append("  ⚠️ Example: CTR ↑ but satisfaction ↓ → weak proxy")
    parts.append("\n".join(proxy_lines))
    
    # 3. GAMING & INCENTIVES (CAN it be manipulated?) - 5 bullets max
    gaming_lines = []
    gaming_lines.append("🎮 Gaming & Incentives: Assess if the metric can be manipulated")
    gaming_lines.append("  👥 By users? Spam, bots, churn masking, are users gaming the system?")
    gaming_lines.append("  👔 By teams? Optimize metric, hurt product, are teams optimizing for the metric at the expense of real value?")
    gaming_lines.append("  🎨 By design? Dark patterns, forced clicks, is the product design encouraging manipulation?")
    gaming_lines.append("  📊 By reporting? Definition drift, are we changing how we measure this over time?")
    gaming_lines.append("  ⚠️ Rule: If it's tied to goals/bonuses, it WILL be gamed")
    parts.append("\n".join(gaming_lines))
    
    # 4. CONTEXT CHECKS (IS this causal?) - 5 bullets max
    context_lines = []
    context_lines.append("🔍 Context Checks: Determine if this change is causal or coincidental")
    context_lines.append("  📅 Seasonality? Is this a seasonal pattern we've seen before?")
    context_lines.append("  🚀 Launches / experiments? Did we recently launch a feature or run an experiment?")
    context_lines.append("  🌍 External events? Are there external factors (news, holidays, market changes) affecting this?")
    context_lines.append("  🔧 Data pipeline issues? Could this be a data quality problem or reporting error?")
    if is_simpson:
        context_lines.append("  🔀 Aggregation bias? Is the overall metric hiding important segment-level differences (Simpson's paradox)?")
    context_lines.append("  ⚠️ Correlation vs causation: is this change actually caused by what we think, or just correlated?")
    parts.append("\n".join(context_lines))
    
    # 5. DECIDE (NOW what?) - 5 bullets max
    decide_lines = []
    decide_lines.append("✅ Decide: Determine the appropriate action based on the analysis")
    decide_lines.append("  🚫 Ignore → noise or bad proxy: if the metric is misleading or the change is insignificant, ignore it")
    decide_lines.append("  👀 Monitor → unclear, need more data: if we're not sure, set up monitoring and wait for more information")
    decide_lines.append("  🔍 Investigate → signal but ambiguous: if there's a potential signal, dig deeper to understand what's happening")
    decide_lines.append("  ⚡ Act → strong signal + aligned proxy: if the metric is a good proxy and the change is significant, take action")
    decide_lines.append("  💡 Output: 'We believe X changed because Y, so we will Z.'")
    parts.append("\n".join(decide_lines))
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l12_csv(input_file, output_file):
    """Process L12 CSV and add/update short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # Get original fieldnames and remove duplicates
        original_fieldnames = list(reader.fieldnames)
        seen = set()
        fieldnames = []
        for field in original_fieldnames:
            if field not in seen:
                fieldnames.append(field)
                seen.add(field)
        
        # Add short_answer if it doesn't exist
        if 'short_answer' not in fieldnames:
            fieldnames.append('short_answer')
        
        for row in reader:
            short_answer = generate_l12_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/23_L12_metrics_interpretation.csv'
    output_file = 'pattern_bank_answered/23_L12_metrics_interpretation.csv'
    process_l12_csv(input_file, output_file)
