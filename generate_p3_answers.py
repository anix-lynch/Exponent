#!/usr/bin/env python3
"""
Generate short answers for P3 questions using the Funnel Analysis framework.
Each answer follows: Define Funnel Steps → Measure Drop-off → Identify Friction → Hypothesize Fix → Test
with line breaks between sections.
"""

import csv

def generate_p3_short_answer(question_text, notes):
    """Generate a short answer following P3 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine funnel type
    is_signup = any(word in question_lower for word in ['sign-up', 'signup', 'sign up', 'registration', 'register'])
    is_checkout = any(word in question_lower for word in ['checkout', 'purchase', 'buy', 'payment', 'conversion'])
    is_application = any(word in question_lower for word in ['application', 'apply', 'submission', 'submit'])
    is_engagement = any(word in question_lower for word in ['engagement', 'engage', 'active', 'usage', 'session'])
    is_retention = any(word in question_lower for word in ['retention', 'retain', 'churn', 'come back'])
    is_hiring = any(word in question_lower for word in ['hiring', 'hire', 'recruit', 'application to offer'])
    is_booking = any(word in question_lower for word in ['booking', 'book', 'reservation'])
    
    parts = []
    
    # 1. DEFINE FUNNEL STEPS
    if is_signup:
        funnel = "Define Funnel Steps: Map the exact user journey. "
        funnel += "Step 1: Entry (landing page / app open). "
        funnel += "Step 2: Start sign-up (click sign-up button). "
        funnel += "Step 3: Fill form (email, password, verification). "
        funnel += "Step 4: Complete sign-up (submit, verify email). "
        funnel += "Step 5: Activation (first action / onboarding complete). "
        funnel += "Guardrail: Steps must be USER actions, not internal events."
    elif is_checkout:
        funnel = "Define Funnel Steps: Map the exact user journey. "
        funnel += "Step 1: Product view / add to cart. "
        funnel += "Step 2: View cart / proceed to checkout. "
        funnel += "Step 3: Enter shipping / payment info. "
        funnel += "Step 4: Review order / confirm purchase. "
        funnel += "Step 5: Purchase complete / confirmation. "
        funnel += "Guardrail: Steps must be USER actions, not internal events."
    elif is_application:
        funnel = "Define Funnel Steps: Map the exact user journey. "
        funnel += "Step 1: View application page / start application. "
        funnel += "Step 2: Fill required fields (personal info, experience). "
        funnel += "Step 3: Review / upload documents. "
        funnel += "Step 4: Submit application. "
        funnel += "Step 5: Confirmation / next steps. "
        funnel += "Guardrail: Steps must be USER actions, not internal events."
    elif is_engagement:
        funnel = "Define Funnel Steps: Map the exact user journey. "
        funnel += "Step 1: Entry (visit / app open). "
        funnel += "Step 2: Discovery (browse / search / explore). "
        funnel += "Step 3: Interaction (click / view / listen). "
        funnel += "Step 4: Core action (like / share / save / comment). "
        funnel += "Step 5: Return / repeat usage. "
        funnel += "Guardrail: Steps must be USER actions, not internal events."
    elif is_retention:
        funnel = "Define Funnel Steps: Map the exact user journey. "
        funnel += "Step 1: First use / activation. "
        funnel += "Step 2: Core value experience (complete key action). "
        funnel += "Step 3: Return within 7 days. "
        funnel += "Step 4: Return within 30 days. "
        funnel += "Step 5: Habit formation (weekly active). "
        funnel += "Guardrail: Steps must be USER actions, not internal events."
    elif is_hiring:
        funnel = "Define Funnel Steps: Map the exact user journey. "
        funnel += "Step 1: Application received. "
        funnel += "Step 2: Resume review / screening. "
        funnel += "Step 3: Interview (phone / on-site). "
        funnel += "Step 4: Decision / offer extended. "
        funnel += "Step 5: Offer accepted / onboarding. "
        funnel += "Guardrail: Steps must be USER actions, not internal events."
    elif is_booking:
        funnel = "Define Funnel Steps: Map the exact user journey. "
        funnel += "Step 1: Search / browse listings. "
        funnel += "Step 2: View details / select option. "
        funnel += "Step 3: Enter booking info (dates, guests). "
        funnel += "Step 4: Review / payment. "
        funnel += "Step 5: Booking confirmed. "
        funnel += "Guardrail: Steps must be USER actions, not internal events."
    else:
        funnel = "Define Funnel Steps: Map the exact user journey from entry to success. "
        funnel += "Identify 4-5 key steps: Entry → Activation → Core Action → Conversion → Success. "
        funnel += "Guardrail: Steps must be USER actions (not internal events or system metrics)."
    
    parts.append(funnel)
    
    # 2. MEASURE DROP-OFF
    measure = "Measure Drop-off: Compute conversion rate between each step. "
    measure += "Calculate: Step 1 → 2: X%, Step 2 → 3: Y%, Step 3 → 4: Z%. "
    measure += "Identify the largest % drop - this is the bottleneck that needs attention."
    
    parts.append(measure)
    
    # 3. IDENTIFY FRICTION
    friction = "Identify Friction: Ask WHY users fail at the bottleneck step. "
    if is_signup:
        friction += "UX friction: too many fields, confusing flow, slow load time. "
        friction += "Trust friction: privacy concerns, unclear value. "
        friction += "Technical friction: bugs, errors, mobile issues. "
        friction += "Use session replays, funnel by segment (new vs returning), and qual research."
    elif is_checkout:
        friction += "UX friction: unexpected costs, forced account creation, complex forms. "
        friction += "Trust friction: payment security, price shock, shipping delays. "
        friction += "Technical friction: payment errors, mobile issues, slow checkout. "
        friction += "Use session replays, funnel by device/platform, and error logs."
    elif is_application:
        friction += "UX friction: too many required fields, unclear instructions, time-consuming. "
        friction += "Trust friction: unclear process, privacy concerns. "
        friction += "Technical friction: form errors, save issues, upload problems. "
        friction += "Use session replays, funnel by segment, and form analytics."
    elif is_engagement or is_retention:
        friction += "UX friction: unclear value, confusing interface, slow performance. "
        friction += "Value friction: not seeing benefit, lack of personalization. "
        friction += "Technical friction: bugs, crashes, latency. "
        friction += "Use session replays, cohort analysis, and user surveys."
    else:
        friction += "UX friction: confusing flow, too many steps, slow load time. "
        friction += "Trust friction: unclear value, privacy concerns. "
        friction += "Value friction: benefit not clear. "
        friction += "Technical friction: bugs, latency, errors. "
        friction += "Use session replays, funnel by segment, and qual research."
    
    parts.append(friction)
    
    # 4. HYPOTHESIZE FIX
    hypothesize = "Hypothesize Fix: Generate 1-2 clear hypotheses. "
    hypothesize += "Format: If we reduce friction X, then conversion at step Y increases. "
    hypothesize += "Prioritize: High impact × Low effort, isolated to one step. "
    hypothesize += "Examples: simplify form, show value earlier, fix technical issues, improve mobile UX."
    
    parts.append(hypothesize)
    
    # 5. TEST
    test = "Test: Run A/B test or staged rollout. "
    test += "Primary metric: conversion rate at the bottleneck step. "
    test += "Guardrails: monitor downstream impact (retention, quality, revenue). "
    test += "Decide: ship winner, iterate, or rollback based on results."
    
    parts.append(test)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_p3_csv(input_file, output_file):
    """Process P3 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_p3_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/03_P3_funnel_analysis.csv'
    output_file = 'pattern_bank_answered/03_P3_funnel_analysis.csv'
    process_p3_csv(input_file, output_file)
