#!/usr/bin/env python3
"""
Generate short answers for L13 questions using the SQL Reasoning framework.
Each answer follows: Conceptual Join → Aggregation Logic → Filter Logic → Output
with line breaks between sections.
"""

import csv

def generate_l13_short_answer(question_text, notes):
    """Generate a short answer following L13 framework with line breaks."""
    
    question_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Determine context
    is_join = any(word in question_lower for word in ['join', 'hierarchy', 'relationship', 'related'])
    is_aggregation = any(word in question_lower for word in ['count', 'sum', 'average', 'top', 'total', 'number'])
    is_filter = any(word in question_lower for word in ['filter', 'where', 'last week', 'last month', 'consecutive', 'three or more'])
    is_time = any(word in question_lower for word in ['week', 'month', 'day', 'date', 'time', 'recent'])
    is_ranking = any(word in question_lower for word in ['top', 'highest', 'lowest', 'least', 'most'])
    
    parts = []
    
    # 1. DEFINE THE OUTPUT (WHAT is the final table?) - 5 bullets max
    output_lines = []
    output_lines.append("📊 Define the OUTPUT: Specify what the final table should look like")
    output_lines.append("  🎯 Grain: one row per what? (user / order / day / experiment / cohort / department / zip code)")
    output_lines.append("  📋 Columns: metrics + dimensions, what metrics do we need? What dimensions to group by?")
    output_lines.append("  📅 Time window: last 7d, 30d, all-time, what time period are we analyzing?")
    if is_ranking:
        output_lines.append("  🏆 Ranking: top N, highest/lowest, how are we ranking results?")
    output_lines.append("  ⚠️ Rule: If you can't say the grain, you don't understand the query")
    parts.append("\n".join(output_lines))
    
    # 2. CONCEPTUAL JOIN (WHAT data must come together?) - 5 bullets max
    join_lines = []
    join_lines.append("🔗 Conceptual JOIN: Identify what data must come together")
    join_lines.append("  📊 Fact table: events, orders, transactions, what is the base table with the metrics?")
    join_lines.append("  🏷️ Dimension tables: users, products, dates, what tables provide context or attributes?")
    join_lines.append("  🔑 Join keys: user_id, order_id, product_id, what columns link the tables together?")
    join_lines.append("  🔀 Join type: INNER → only matched rows, LEFT → keep base table intact")
    if is_join:
        join_lines.append("  🔗 Multiple joins: ensure join keys are correct and understand relationships")
    join_lines.append("  ⚠️ Rule: Pick the BASE table first, then join outward")
    parts.append("\n".join(join_lines))
    
    # 3. FILTER LOGIC (WHICH rows count?) - 5 bullets max
    filter_lines = []
    filter_lines.append("🔍 Filter Logic: Determine which rows count")
    filter_lines.append("  📅 Time filters: event_date BETWEEN …, date >= …, what time period are we filtering?")
    filter_lines.append("  ✅ Status filters: completed, paid, active, what status or state conditions?")
    filter_lines.append("  👥 Segment filters: country, platform, plan, what demographic or segment filters?")
    filter_lines.append("  🚫 Exclusions: test users, refunds, bots, what should we exclude?")
    if is_time:
        filter_lines.append("  ⏰ Time-based: filter to the specified time window (last week, last month, etc.)")
    if 'three or more' in question_lower or 'consecutive' in question_lower:
        filter_lines.append("  🔢 Conditional filters: use HAVING or subqueries for conditions on aggregated results")
    filter_lines.append("  ⚠️ Rule: Filters change meaning — say them explicitly")
    parts.append("\n".join(filter_lines))
    
    # 4. AGGREGATION LOGIC (HOW are numbers computed?) - 5 bullets max
    aggregation_lines = []
    aggregation_lines.append("🧮 Aggregation Logic: Determine how numbers are computed")
    aggregation_lines.append("  🔢 Count vs count distinct: COUNT(*) counts all rows, COUNT(DISTINCT column) counts unique values")
    aggregation_lines.append("  ➕ Sum vs average: SUM for totals, AVG for averages, what aggregation function is appropriate?")
    aggregation_lines.append("  📊 Group by: which dimensions? What columns determine the grain of the output?")
    if is_ranking:
        aggregation_lines.append("  🏆 Ranking: use window functions (ROW_NUMBER, RANK, DENSE_RANK) or ORDER BY + LIMIT for top N")
    if 'consecutive' in question_lower:
        aggregation_lines.append("  🔄 Consecutive logic: use window functions (LAG, LEAD) or self-joins to identify consecutive patterns")
    aggregation_lines.append("  ⚠️ Rule: Aggregation happens at the grain, not before")
    parts.append("\n".join(aggregation_lines))
    
    # 5. EDGE CASES & VALIDATION - 5 bullets max
    validation_lines = []
    validation_lines.append("✅ Edge Cases & Validation: Check for potential issues")
    validation_lines.append("  🔄 Duplicates after joins? Do joins create duplicate rows that will inflate counts?")
    validation_lines.append("  ❓ Missing data? Are there NULL values that need handling?")
    validation_lines.append("  🔍 Sanity checks: back-of-envelope validation, do the numbers make sense?")
    validation_lines.append("  📈 Performance: for large datasets, consider if the query will be efficient (indexes, filtering early)")
    validation_lines.append("  🧪 Test edge cases: empty results, single row, all NULLs, what happens in edge cases?")
    parts.append("\n".join(validation_lines))
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l13_csv(input_file, output_file):
    """Process L13 CSV and add/update short_answer column."""
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
            short_answer = generate_l13_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/24_L13_sql_reasoning.csv'
    output_file = 'pattern_bank_answered/24_L13_sql_reasoning.csv'
    process_l13_csv(input_file, output_file)
