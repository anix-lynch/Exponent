#!/usr/bin/env python3
"""
Generate short answers for L5 questions using the Observability framework.
Each answer follows: Key Metrics → Alerts → Dashboards → Escalation
with line breaks between sections.
"""

import csv

def generate_l5_short_answer(question_text, notes):
    """Generate a short answer following L5 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_dashboard = any(word in question_lower for word in ['dashboard', 'monitor', 'track', 'analytics'])
    is_monitoring = any(word in question_lower for word in ['monitoring', 'observability', 'health', 'metrics service'])
    is_alert = any(word in question_lower for word in ['alert', 'alarm', 'notification'])
    is_ml = any(word in question_lower for word in ['ml', 'machine learning', 'model', 'drift'])
    is_performance = any(word in question_lower for word in ['latency', 'performance', 'slow', 'profiler'])
    
    parts = []
    
    # 1. KEY METRICS (WHAT do we measure?)
    metrics = "Key Metrics: Define what we measure. "
    metrics += "Golden signals: "
    metrics += "Latency: p50 / p95 / p99 response times. "
    metrics += "Error rate: percentage of failed requests, errors per second. "
    metrics += "Throughput / volume: requests per second, transactions per minute. "
    metrics += "Saturation: CPU, memory, queue depth, resource utilization. "
    metrics += "Business metrics: "
    metrics += "Conversions / success rate: business outcome metrics. "
    metrics += "Drops / failures: user-facing failures, drop-off rates. "
    metrics += "Revenue-impacting events: payment failures, checkout issues. "
    if is_ml:
        metrics += "Data quality (for ML systems): "
        metrics += "Freshness: data recency, model staleness. "
        metrics += "Completeness: missing features, null rates. "
        metrics += "Anomalies: drift detection, outlier rates."
    elif is_dashboard:
        metrics += "Data quality (if data system): "
        metrics += "Freshness: data update frequency, latency. "
        metrics += "Completeness: missing records, coverage. "
        metrics += "Anomalies: unexpected patterns, outliers."
    
    parts.append(metrics)
    
    # 2. ALERTS (WHEN do we wake someone?)
    alerts = "Alerts: Define when to wake someone. "
    alerts += "Symptom-based (preferred): "
    alerts += "User-visible errors: alerts on issues users experience. "
    alerts += "SLO burn rate: alert when SLO error budget is being consumed. "
    alerts += "Missed business outcomes: conversion drops, revenue impact. "
    alerts += "Thresholds: "
    alerts += "Static: known limits (e.g., error rate > 1%). "
    alerts += "Dynamic: baseline deviation (e.g., 3-sigma from normal). "
    alerts += "Alert hygiene: "
    alerts += "Actionable: alert tells us what to do. "
    alerts += "Low noise: only alerts on real issues, not false positives. "
    alerts += "Clear owner: who responds to this alert."
    
    parts.append(alerts)
    
    # 3. DASHBOARDS (HOW do we debug fast?)
    dashboards = "Dashboards: Enable fast debugging. "
    dashboards += "Overview: "
    dashboards += "Health at a glance: red / yellow / green status. "
    dashboards += "Key metrics visible immediately. "
    dashboards += "Drill-down: "
    dashboards += "By service: isolate which service has issues. "
    dashboards += "By region / segment: geographic or user segment breakdown. "
    dashboards += "By time: historical trends, time-series analysis. "
    dashboards += "Correlation: "
    dashboards += "Deploys: link metrics to deployment events. "
    dashboards += "Traffic spikes: correlate with traffic patterns. "
    dashboards += "Feature flags: see impact of feature toggles. "
    dashboards += "Remember: Dashboards are for debugging, alerts are for action."
    
    parts.append(dashboards)
    
    # 4. ESCALATION (WHAT happens next?)
    escalation = "Escalation: Define response and learning. "
    escalation += "Ownership: "
    escalation += "On-call rotation: clear ownership, rotation schedule. "
    escalation += "Clear runbooks: documented response procedures. "
    escalation += "Response: "
    escalation += "Mitigate first: stop the bleeding, restore service. "
    escalation += "Roll back / degrade: revert changes or disable features. "
    escalation += "Learning: "
    escalation += "Postmortem: document what happened, why, and how to prevent. "
    escalation += "Fix root cause: address underlying issue, not just symptoms. "
    escalation += "Improve signals: update metrics, alerts, dashboards based on learnings. "
    escalation += "Remember: If you can't answer 'Are users hurting right now?' in 10 seconds, your observability is broken."
    
    parts.append(escalation)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l5_csv(input_file, output_file):
    """Process L5 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l5_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/17_L5_observability.csv'
    output_file = 'pattern_bank_answered/17_L5_observability.csv'
    process_l5_csv(input_file, output_file)
