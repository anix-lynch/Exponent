#!/usr/bin/env python3
"""
Generate short answers for L10 questions using the Process Optimization framework.
Each answer follows: Map Workflow → Identify Bottlenecks → Optimize → Measure
with line breaks between sections.
"""

import csv

def generate_l10_short_answer(question_text, notes):
    """Generate a short answer following L10 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_queue = any(word in question_lower for word in ['queue', 'wait', 'line', 'bottleneck'])
    is_delivery = any(word in question_lower for word in ['delivery', 'fulfillment', 'package', 'driver'])
    is_build = any(word in question_lower for word in ['build', 'ci', 'cd', 'compile', 'deploy'])
    is_hiring = any(word in question_lower for word in ['hiring', 'recruit', 'interview', 'onboard'])
    is_automation = any(word in question_lower for word in ['automate', 'manual', 'automation'])
    is_process = any(word in question_lower for word in ['process', 'workflow', 'flow', 'optimize'])
    
    parts = []
    
    # 1. MAP WORKFLOW (WHAT is the current process?)
    workflow = "Map Workflow: Document the current process end-to-end. "
    workflow += "Identify all steps: from start to finish, map every stage. "
    workflow += "Sequence: order of operations, dependencies between steps. "
    workflow += "Stakeholders: who is involved at each step. "
    workflow += "Time: how long each step takes, total cycle time. "
    workflow += "Handoffs: where work transfers between people/systems. "
    workflow += "Create a visual flow: step 1 → step 2 → step 3 → completion."
    
    parts.append(workflow)
    
    # 2. IDENTIFY BOTTLENECKS (WHERE does it slow down?)
    bottlenecks = "Identify Bottlenecks: Find where the process slows down. "
    bottlenecks += "Time analysis: which step takes longest? "
    bottlenecks += "Wait time: where is work waiting (queues, approvals, dependencies)? "
    bottlenecks += "Resource constraints: limited capacity, single-threaded steps. "
    bottlenecks += "Rework: steps that require repetition, errors, corrections. "
    bottlenecks += "Manual steps: human-dependent processes that could be automated. "
    bottlenecks += "Dependencies: steps blocked by other processes or approvals. "
    bottlenecks += "Focus on: highest time impact, most frequent delays, biggest pain points."
    
    parts.append(bottlenecks)
    
    # 3. OPTIMIZE (HOW do we improve?)
    optimize = "Optimize: Design improvements to eliminate bottlenecks. "
    if is_automation:
        optimize += "Automate: replace manual steps with automated systems. "
        optimize += "Parallelize: run steps concurrently instead of sequentially. "
        optimize += "Eliminate: remove unnecessary steps, reduce handoffs. "
        optimize += "Standardize: create consistent processes, reduce variability. "
    elif is_queue:
        optimize += "Increase capacity: add resources, parallel processing. "
        optimize += "Reduce demand: batch processing, off-peak scheduling. "
        optimize += "Optimize flow: reduce wait time, improve routing. "
        optimize += "Eliminate waste: remove unnecessary steps, streamline. "
    elif is_delivery:
        optimize += "Route optimization: efficient paths, minimize travel time. "
        optimize += "Batch processing: group deliveries, optimize stops. "
        optimize += "Resource allocation: right capacity at right time. "
        optimize += "Automation: reduce manual work, improve accuracy. "
    else:
        optimize += "Eliminate waste: remove unnecessary steps, reduce handoffs. "
        optimize += "Automate: replace manual work with systems. "
        optimize += "Parallelize: run steps concurrently. "
        optimize += "Standardize: create consistent processes. "
        optimize += "Increase capacity: add resources where bottlenecked. "
    optimize += "Prioritize: focus on highest-impact bottlenecks first."
    
    parts.append(optimize)
    
    # 4. MEASURE (DID it work?)
    measure = "Measure: Track impact of optimizations. "
    measure += "Before metrics: baseline cycle time, throughput, error rate. "
    measure += "After metrics: improved cycle time, throughput, error rate. "
    measure += "Key metrics: time saved, capacity increase, quality improvement. "
    measure += "Continuous monitoring: track metrics over time, identify new bottlenecks. "
    measure += "Iterate: if optimization didn't work, try different approach. "
    measure += "Document learnings: what worked, what didn't, why."
    
    parts.append(measure)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l10_csv(input_file, output_file):
    """Process L10 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l10_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/21_L10_process_optimization.csv'
    output_file = 'pattern_bank_answered/21_L10_process_optimization.csv'
    process_l10_csv(input_file, output_file)
