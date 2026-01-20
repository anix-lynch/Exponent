#!/usr/bin/env python3
"""
TEST: Generate short answers for L14 questions using ASCII tree format.
This is a test version to see if ASCII trees are more readable.
"""

import csv

def generate_l14_short_answer_ascii(question_text, notes):
    """Generate a short answer following L14 framework with ASCII tree format."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_ml = any(word in question_lower for word in ['ml', 'machine learning', 'model', 'ai', 'llm', 'rag', 'gen ai', 'generative'])
    is_data = any(word in question_lower for word in ['data', 'pipeline', 'etl', 'warehouse', 'lake', 'database'])
    is_realtime = any(word in question_lower for word in ['real-time', 'live', 'streaming', 'messaging', 'chat'])
    
    # Build ASCII tree
    tree = []
    tree.append("START: Design System Architecture")
    tree.append("│")
    tree.append("├─ 1) Define the GOAL")
    tree.append("│  │")
    tree.append("│  ├─ Primary user goal: what is the main user need or business objective?")
    tree.append("│  ├─ Success metric: latency, reliability, accuracy, cost, what defines success?")
    tree.append("│  └─ Non-goals: explicitly say what's out of scope, what we're NOT building")
    tree.append("│")
    tree.append("│  ⚠ Rule: If the goal isn't clear, architecture will be wrong")
    tree.append("│")
    tree.append("├─ 2) Identify CORE COMPONENTS")
    tree.append("│  │")
    tree.append("│  ├─ Clients: web, mobile, internal tools, what are the entry points?")
    tree.append("│  ├─ Ingestion layer: APIs, SDKs, event collectors, how does data enter?")
    tree.append("│  ├─ Processing layer: sync vs async, how is data processed?")
    tree.append("│  ├─ Storage: hot / warm / cold, where is data stored?")
    tree.append("│  ├─ Compute: stateless vs stateful, how is computation handled?")
    tree.append("│  ├─ Orchestration / queues: how are tasks coordinated and queued?")
    tree.append("│  ├─ Observability: metrics, logs, alerts, how do we monitor?")
    tree.append("│  └─ Admin / control plane: how is the system managed?")
    
    if is_ml:
        tree.append("│  │")
        tree.append("│  └─ ML-specific: model serving, feature store, training pipeline, inference endpoints")
    if is_data:
        tree.append("│  │")
        tree.append("│  └─ Data-specific: ETL pipelines, data warehouse, data lake, transformation layers")
    if is_realtime:
        tree.append("│  │")
        tree.append("│  └─ Real-time specific: message queues, stream processing, pub/sub systems")
    
    tree.append("│")
    tree.append("│  ⚠ Rule: Name boxes before wiring arrows")
    tree.append("│")
    tree.append("├─ 3) Data FLOW")
    tree.append("│  │")
    tree.append("│  ├─ Request path (read): how do read requests flow through the system?")
    tree.append("│  ├─ Write path (create/update): how do write requests flow through?")
    tree.append("│  ├─ Async paths: queues, streams, retries, how are async operations handled?")
    tree.append("│  ├─ Failure paths: timeouts, backpressure, how are failures handled?")
    tree.append("│  └─ Control vs data plane: how are control operations separated from data?")
    tree.append("│")
    tree.append("│  ⚠ Rule: Always describe the happy path first")
    tree.append("│")
    tree.append("├─ 4) Boundaries & CONSTRAINTS")
    tree.append("│  │")
    tree.append("│  ├─ Latency SLOs: what are the latency requirements?")
    tree.append("│  ├─ Consistency: strong consistency vs eventual consistency?")
    tree.append("│  ├─ Throughput limits: how many requests per second must we handle?")
    tree.append("│  ├─ Regulatory / privacy: GDPR, HIPAA, data residency requirements?")
    tree.append("│  ├─ Team ownership: which teams own which components?")
    tree.append("│  └─ Cost ceilings: what are the budget constraints?")
    tree.append("│")
    tree.append("│  ⚠ Rule: Constraints shape architecture more than features")
    tree.append("│")
    tree.append("└─ 5) Scale & FAILURE MODES")
    tree.append("   │")
    tree.append("   ├─ Bottlenecks: DB, network, fan-out, where will the system slow down?")
    tree.append("   ├─ Single points of failure: what components have no redundancy?")
    tree.append("   ├─ Backpressure strategy: how do we handle overload?")
    tree.append("   ├─ Caching layers: where can we cache to reduce load?")
    tree.append("   ├─ Sharding / partitioning: how do we distribute data across instances?")
    tree.append("   └─ Graceful degradation: how does the system degrade when overloaded?")
    tree.append("   │")
    tree.append("   ⚠ Rule: Talk about failure BEFORE optimization")
    tree.append("   │")
    tree.append("   └─ OUTPUT: System of boxes + arrows, bounded by constraints,")
    tree.append("              designed to scale and fail safely.")
    
    return "\n".join(tree)


def process_l14_csv_test(input_file, output_file):
    """Process L14 CSV and add short_answer column with ASCII tree format."""
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
            short_answer = generate_l14_short_answer_ascii(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    # Write to test file
    test_output_file = output_file.replace('.csv', '_ASCII_TEST.csv')
    with open(test_output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} ASCII tree short answers in {test_output_file}")
    print(f"\nSample question preview:")
    if rows:
        print(f"Question: {rows[0]['question_text'][:80]}...")
        print(f"\nASCII Tree Answer (first 500 chars):")
        print(rows[0]['short_answer'][:500])


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/25_L14_system_design_conceptual.csv'
    output_file = 'pattern_bank_answered/25_L14_system_design_conceptual.csv'
    process_l14_csv_test(input_file, output_file)
