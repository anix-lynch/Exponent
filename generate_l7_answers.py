#!/usr/bin/env python3
"""
Generate short answers for L7 questions using the Data Modeling framework.
Each answer follows: Entities → Relationships → Metrics → Grain → Validate
with line breaks between sections.
"""

import csv

def generate_l7_short_answer(question_text, notes):
    """Generate a short answer following L7 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_warehouse = any(word in question_lower for word in ['warehouse', 'data warehouse', 'schema'])
    is_database = any(word in question_lower for word in ['database', 'schema', 'model'])
    is_ecommerce = any(word in question_lower for word in ['amazon', 'e-commerce', 'ecommerce', 'order', 'product'])
    is_social = any(word in question_lower for word in ['instagram', 'linkedin', 'social', 'post', 'user'])
    is_ride_sharing = any(word in question_lower for word in ['ride', 'uber', 'lyft', 'driver', 'trip'])
    is_ml = any(word in question_lower for word in ['model', 'propensity', 'ml', 'machine learning'])
    
    parts = []
    
    # 1. ENTITIES (WHAT things exist?)
    entities = "Entities: Identify core nouns in the business. "
    if is_ecommerce:
        entities += "Core entities: User, Product, Order, Order_Item, Session, Payment. "
        entities += "Rule: If it has its own lifecycle → entity. "
        entities += "Each entity represents a distinct business concept with its own attributes and lifecycle."
    elif is_social:
        entities += "Core entities: User, Post, Comment, Like, Follow, Session. "
        entities += "Rule: If it has its own lifecycle → entity. "
        entities += "Each entity represents a distinct business concept with its own attributes and lifecycle."
    elif is_ride_sharing:
        entities += "Core entities: User (rider), Driver, Trip, Vehicle, Payment. "
        entities += "Rule: If it has its own lifecycle → entity. "
        entities += "Each entity represents a distinct business concept with its own attributes and lifecycle."
    elif is_warehouse:
        entities += "Core entities: Identify main business objects (Users, Transactions, Events, Products, etc.). "
        entities += "Rule: If it has its own lifecycle → entity. "
        entities += "Each entity represents a distinct business concept with its own attributes and lifecycle."
    else:
        entities += "Core entities: Identify main business objects. "
        entities += "Rule: If it has its own lifecycle → entity. "
        entities += "Each entity represents a distinct business concept with its own attributes and lifecycle."
    
    parts.append(entities)
    
    # 2. RELATIONSHIPS (HOW do they connect?)
    relationships = "Relationships: Define how entities connect. "
    relationships += "One-to-one: single relationship (e.g., User → Profile). "
    relationships += "One-to-many: parent-child (e.g., User → Orders, User → Sessions). "
    relationships += "Many-to-many: requires junction table (e.g., Order ↔ Products via Order_Items). "
    if is_ecommerce:
        relationships += "Examples: User → Orders (1:N), Order → Order_Items (1:N), Order_Items → Product (M:N via Order_Items). "
    elif is_social:
        relationships += "Examples: User → Posts (1:N), User → Likes (M:N via Likes table), User → Follows (M:N via Follows table). "
    elif is_ride_sharing:
        relationships += "Examples: User → Trips (1:N), Driver → Trips (1:N), Trip → Payment (1:1). "
    relationships += "Design relationships to support efficient queries and avoid data redundancy."
    
    parts.append(relationships)
    
    # 3. METRICS (WHAT do we measure?)
    metrics = "Metrics: Define what we measure. "
    metrics += "Counts: # orders, # sessions, # users, # events. "
    metrics += "Sums: Revenue, Spend, Total amount. "
    metrics += "Ratios: Conversion rate, Retention rate, Average order value. "
    metrics += "Rule: Metrics live on facts (fact tables), not dimensions. "
    metrics += "Facts store metrics; dimensions store context. "
    if is_ecommerce:
        metrics += "Example metrics: Revenue (sum of order amounts), Order count, Conversion rate (orders/sessions). "
    elif is_social:
        metrics += "Example metrics: Post count, Engagement rate (likes/posts), Active users. "
    elif is_ride_sharing:
        metrics += "Example metrics: Trip count, Revenue (sum of trip fares), Average trip distance. "
    
    parts.append(metrics)
    
    # 4. GRAIN (WHAT does one row represent?)
    grain = "Grain: Define what one row represents. "
    grain += "One row per: Event, Session, Order, User-day, Transaction. "
    grain += "Rule: Never mix grains in one table. "
    grain += "Grain is the most important decision - it determines what questions you can answer. "
    if is_ecommerce:
        grain += "Example: fact_orders table = 1 row per order. fact_sessions table = 1 row per session. "
    elif is_social:
        grain += "Example: fact_posts table = 1 row per post. fact_events table = 1 row per user action (like, comment). "
    elif is_ride_sharing:
        grain += "Example: fact_trips table = 1 row per trip. fact_events table = 1 row per event (request, accept, complete). "
    grain += "Model for questions, not for storage."
    
    parts.append(grain)
    
    # 5. VALIDATE (CAN we answer the question?)
    validate = "Validate: Verify the model can answer key questions. "
    validate += "Can we compute metrics without double-counting? Check aggregation logic. "
    validate += "Do joins stay clean? Verify relationships support efficient queries. "
    validate += "Does aggregation feel natural? Can we easily roll up by time, user, product, etc.? "
    validate += "Do edge cases break it? Test with nulls, duplicates, orphaned records. "
    validate += "Output: Clean Fact + Dimension model. "
    validate += "FACT tables: things that happen (events, orders, sessions). "
    validate += "DIM tables: descriptions (users, products, time). "
    validate += "If joins feel painful, the model is wrong."
    
    parts.append(validate)
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l7_csv(input_file, output_file):
    """Process L7 CSV and add short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['short_answer']
        
        for row in reader:
            short_answer = generate_l7_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/18_L7_data_modeling.csv'
    output_file = 'pattern_bank_answered/18_L7_data_modeling.csv'
    process_l7_csv(input_file, output_file)
