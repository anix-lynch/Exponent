#!/usr/bin/env python3
"""
Generate short answers for P2 questions using the NSM + KPI Ladder framework.
Each answer follows: NSM → Input KPIs → Leading Indicators → Guardrails → Dashboard
with line breaks between sections.
"""

import csv

def generate_p2_short_answer(question_text, notes):
    """Generate a short answer following P2 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine product/feature context
    is_design = 'design' in question_lower
    is_metrics = any(word in question_lower for word in ['metric', 'measure', 'success', 'kpi', 'track'])
    is_feature = any(word in question_lower for word in ['feature', 'product', 'launch', 'new'])
    
    # Extract product type hints
    product_type = None
    if 'homepage' in question_lower or 'home page' in question_lower:
        product_type = 'homepage'
    elif 'video' in question_lower or 'conference' in question_lower:
        product_type = 'video'
    elif 'booking' in question_lower or 'reservation' in question_lower:
        product_type = 'booking'
    elif 'chat' in question_lower or 'messaging' in question_lower:
        product_type = 'communication'
    elif 'support' in question_lower or 'customer' in question_lower:
        product_type = 'support'
    elif 'gaming' in question_lower or 'console' in question_lower:
        product_type = 'gaming'
    elif 'education' in question_lower or 'learning' in question_lower:
        product_type = 'education'
    elif 'financial' in question_lower or 'money' in question_lower:
        product_type = 'financial'
    
    parts = []
    
    # 1. NSM (North Star Metric)
    if is_design or is_feature:
        nsm = "NSM: Define one North Star metric that best represents user + business value. "
        if product_type == 'homepage':
            nsm += "Example: Weekly Engaged Users or Time to Value."
        elif product_type == 'video':
            nsm += "Example: Weekly Active Video Viewers or Watch Time per User."
        elif product_type == 'booking':
            nsm += "Example: Weekly Successful Bookings or Booking Completion Rate."
        elif product_type == 'communication':
            nsm += "Example: Daily Active Conversations or Messages per User."
        elif product_type == 'support':
            nsm += "Example: Issue Resolution Rate or Customer Satisfaction Score."
        elif product_type == 'gaming':
            nsm += "Example: Monthly Active Players or Engagement Hours per User."
        elif product_type == 'education':
            nsm += "Example: Weekly Active Learners or Course Completion Rate."
        elif product_type == 'financial':
            nsm += "Example: Monthly Active Users with Transactions or Financial Health Score."
        else:
            nsm += "Choose a single metric that captures both user value and business outcomes."
    else:
        nsm = "NSM: Identify the single most important metric that represents success. "
        nsm += "This should be the one number that best captures user value + business value combined."
    
    parts.append(nsm)
    
    # 2. INPUT KPIs (What drives the NSM)
    input_kpis = "Input KPIs: Break NSM into 3-5 controllable drivers. "
    if product_type == 'homepage':
        input_kpis += "User behavior: sessions per user, click-through rate, time on page. "
        input_kpis += "Content quality: relevance score, engagement depth. "
        input_kpis += "Monetization: conversion rate, revenue per session."
    elif product_type == 'video':
        input_kpis += "Content: video quality, relevance, diversity. "
        input_kpis += "Engagement: watch time, completion rate, shares. "
        input_kpis += "Platform: load time, buffering, playback quality."
    elif product_type == 'booking':
        input_kpis += "Discovery: search relevance, listing quality, availability. "
        input_kpis += "Conversion: booking completion rate, payment success. "
        input_kpis += "Supply: inventory quality, partner reliability."
    elif product_type == 'communication':
        input_kpis += "Adoption: active conversations, message volume. "
        input_kpis += "Quality: response time, message relevance. "
        input_kpis += "Engagement: daily active users, conversation depth."
    elif product_type == 'support':
        input_kpis += "Resolution: first-contact resolution, time to resolve. "
        input_kpis += "Quality: customer satisfaction, issue recurrence. "
        input_kpis += "Efficiency: tickets per agent, automation rate."
    else:
        input_kpis += "User behavior drivers (engagement, activation). "
        input_kpis += "Supply/quality drivers (content, inventory, features). "
        input_kpis += "Monetization drivers (conversion, retention, LTV)."
    
    parts.append(input_kpis)
    
    # 3. LEADING INDICATORS (Early signals)
    leading = "Leading Indicators: Add early signals that predict NSM movement. "
    leading += "Short-term behaviors: first-session actions, early engagement patterns. "
    leading += "Funnel entry signals: activation rate, feature discovery. "
    leading += "Quality proxies: user satisfaction, retention hooks, content signals."
    
    parts.append(leading)
    
    # 4. GUARDRAILS (What must NOT break)
    guardrails = "Guardrails: Define what must NOT break while optimizing NSM. "
    if 'accessibility' in question_lower or 'disability' in question_lower:
        guardrails += "Accessibility compliance, user trust, inclusive design. "
    elif 'content' in question_lower or 'moderation' in question_lower:
        guardrails += "Content quality, user safety, community guidelines compliance. "
    elif 'financial' in question_lower or 'money' in question_lower:
        guardrails += "User financial safety, regulatory compliance, fraud prevention. "
    else:
        guardrails += "User trust, long-term health, cost/abuse prevention, compliance. "
    guardrails += "Set thresholds that trigger alerts if breached."
    
    parts.append(guardrails)
    
    # 5. DASHBOARD (How you monitor)
    dashboard = "Dashboard: Design simple monitoring structure. "
    dashboard += "NSM at top (always visible, weekly trend). "
    dashboard += "Input KPIs (weekly review, track drivers). "
    dashboard += "Leading indicators (daily monitoring, early signals). "
    dashboard += "Guardrails (alerts only, no daily noise)."
    
    parts.append(dashboard)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p2_csv(input_file, output_file):
    """Process P2 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_p2_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/02_P2_nsm_kpi_ladder.csv'
    output_file = 'pattern_bank_answered/02_P2_nsm_kpi_ladder.csv'
    process_p2_csv(input_file, output_file)
