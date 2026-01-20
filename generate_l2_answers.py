#!/usr/bin/env python3
"""
Generate short answers for L2 questions using the Scale & Capacity framework.
Each answer follows: Current Load → 10× Projection → Bottlenecks → Mitigation
with line breaks between sections.
"""

import csv

def generate_l2_short_answer(question_text, notes):
    """Generate a short answer following L2 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_estimation = any(word in question_lower for word in ['estimate', 'calculate', 'how many', 'how much', 'bandwidth', 'storage'])
    is_system_design = any(word in question_lower for word in ['design', 'scalable', 'system', 'service', 'handle'])
    is_capacity = any(word in question_lower for word in ['capacity', 'scale', 'traffic', 'requests', 'load'])
    is_forecast = any(word in question_lower for word in ['forecast', 'headcount', 'needs'])
    
    parts = []
    
    # 1. CURRENT LOAD (WHAT do we run today?)
    current = "Current Load: Understand what we run today. "
    current += "Traffic: "
    current += "QPS / RPS: queries/requests per second. "
    current += "Concurrent users: how many users active simultaneously. "
    current += "Peak vs average: understand traffic patterns. "
    current += "Data: "
    current += "Rows/day: data ingestion rate. "
    current += "Storage size: current data volume. "
    current += "Read/write ratio: access patterns. "
    current += "Resources: "
    current += "CPU / Memory: compute utilization. "
    current += "Network: bandwidth usage. "
    current += "Third-party quotas: external service limits."
    
    parts.append(current)
    
    # 2. 10× PROJECTION (WHAT changes at 10×?)
    projection = "10× Projection: Model what changes at 10× scale. "
    projection += "Linear growth assumptions: "
    projection += "Traffic ×10: requests, users, sessions. "
    projection += "Data ×10: storage, ingestion, processing. "
    projection += "Cost ×10: infrastructure, services, operations. "
    projection += "Non-linear risks: "
    projection += "Lock contention: database locks become bottleneck. "
    projection += "Hot keys / hot shards: uneven distribution causes hotspots. "
    projection += "Fan-out explosions: one request triggers many downstream calls. "
    projection += "Tail latency: p99/p999 latency degrades faster than average."
    
    parts.append(projection)
    
    # 3. BOTTLENECKS (WHAT fails first?)
    bottlenecks = "Bottlenecks: Identify what fails first. "
    bottlenecks += "Compute: "
    bottlenecks += "Single-threaded services: can't parallelize. "
    bottlenecks += "GC pressure: garbage collection overhead. "
    bottlenecks += "Cold starts: latency spikes from initialization. "
    bottlenecks += "Storage: "
    bottlenecks += "Index bloat: indexes grow, queries slow. "
    bottlenecks += "Write amplification: writes trigger more I/O. "
    bottlenecks += "Slow scans: full table scans become expensive. "
    bottlenecks += "Network: "
    bottlenecks += "Chatty services: too many small requests. "
    bottlenecks += "Cross-AZ traffic: inter-region latency and cost. "
    bottlenecks += "External deps: "
    bottlenecks += "Rate limits: third-party API throttling. "
    bottlenecks += "SLA violations: external service degradation. "
    bottlenecks += "Vendor outages: dependency failures."
    
    parts.append(bottlenecks)
    
    # 4. MITIGATION (HOW do we survive?)
    mitigation = "Mitigation: Design solutions to survive 10× growth. "
    mitigation += "Architectural: "
    mitigation += "Caching: reduce load on backend systems. "
    mitigation += "Async / queues: decouple and buffer requests. "
    mitigation += "Sharding / partitioning: distribute load across nodes. "
    mitigation += "Backpressure: slow down producers when consumers are overwhelmed. "
    mitigation += "Operational: "
    mitigation += "Load shedding: drop low-priority requests during overload. "
    mitigation += "Graceful degradation: reduce features to maintain core functionality. "
    mitigation += "Feature flags: disable non-critical features under load. "
    mitigation += "Economic: "
    mitigation += "Cost caps: limit spending to prevent runaway costs. "
    mitigation += "Tiered SLAs: different service levels for different users. "
    mitigation += "Kill switches: emergency shutdowns for cost control. "
    mitigation += "Remember: Scaling isn't 'can it run?' It's 'what fails first, and is that acceptable?'"
    
    parts.append(mitigation)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l2_csv(input_file, output_file):
    """Process L2 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l2_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/14_L2_scale_capacity.csv'
    output_file = 'pattern_bank_answered/14_L2_scale_capacity.csv'
    process_l2_csv(input_file, output_file)
