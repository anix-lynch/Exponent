"""
Categorize Data Engineer questions into interview categories
COMPREHENSIVE categorization for #1 goal role
"""
import json
import os

# Data Engineer Categories (comprehensive for your #1 goal)
CATEGORIES = [
    "Data Pipeline Design",
    "ETL/ELT",
    "Data Modeling",
    "SQL",
    "Data Structures & Algorithms",
    "System Design",
    "Distributed Systems",
    "Data Warehousing",
    "Streaming Data",
    "Batch Processing",
    "Cloud Platforms",
    "Performance Optimization",
    "Data Quality",
    "Behavioral",
    "Coding",
    "Spark/Big Data",
    "Database Design",
    "Schema Design",
    "Data Governance",
    "Monitoring & Observability"
]

def categorize_question(question_text, url=""):
    """Categorize a Data Engineer question based on keywords and patterns"""
    q_lower = question_text.lower()
    categories = []
    
    # Company-specific behavioral (Why do you want to work at X?)
    if 'why do you want to work at' in q_lower or 'why did you become' in q_lower or 'what other companies' in q_lower or 'why do you think we should not hire' in q_lower or 'why should we hire' in q_lower or 'why shouldn\'t we hire' in q_lower:
        categories.append("Behavioral")
        return categories  # Early return for these
    
    # Behavioral Questions (MUST come before other checks)
    behavioral_phrases = [
        'tell me about a time', 'describe a time', 'have you ever', 'walk me through',
        'made a mistake', 'tell me about a mistake', 'faced challenges', 'conflict', 'disagreement', 'failure',
        'difficult decision', 'skill you learned', 'difficult to work with',
        'tell me about yourself', 'project you are most proud', 'influence without authority',
        'encourage collaboration', 'approach personal growth', 'develop yourself professionally',
        'what parts of', 'mission statement resonate', 'tell me about a relevant complex program'
    ]
    if any(phrase in q_lower for phrase in behavioral_phrases):
        categories.append("Behavioral")
        return categories  # Early return for behavioral
    
    # Classic LeetCode/DSA problems (MUST come before general coding)
    dsa_patterns = [
        'palindrome', 'container with most water', 'two sum', 'merge two sorted',
        'valid parentheses', 'climbing stairs', 'roman to integer', 'islands',
        'spiral order', 'set matrix zeroes', 'game of life', 'rotating the box',
        'generate parentheses', 'top k frequent', 'sliding window maximum',
        'course schedule', 'reverse a sentence', 'print all combinations',
        'stock prices', 'maximize your profit', 'regex parser', 'calculator'
    ]
    if any(pattern in q_lower for pattern in dsa_patterns):
        categories.append("Data Structures & Algorithms")
        return categories  # Early return for DSA
    
    # SQL-specific questions (table names, SQL operations)
    sql_indicators = [
        'employee', 'earnings', 'salaries', 'department', 'hierarchy',
        'transaction', 'instagram likes', 'lyft ride', 'duolingo leaderboard',
        'test scores', 'post success', 'session data analysis', 'high volume low success',
        'marketing channel attribution', 'campaign purchases', 'fraudulent transactions',
        'customer lifetime value', 'monthly customer transactions'
    ]
    if any(indicator in q_lower for indicator in sql_indicators):
        categories.append("SQL")
        # Don't return, might also be data analysis
    
    # ETL/ELT (specific design questions)
    if 'etl pipeline' in q_lower or 'elt pipeline' in q_lower:
        categories.append("ETL/ELT")
        categories.append("Data Pipeline Design")
        categories.append("System Design")
        return categories
    
    # Data Pipeline Design (specific pipeline questions)
    pipeline_keywords = [
        'clickstream data pipeline', 'data pipeline that updates', 'data pipeline that complies',
        'document processing pipeline', 'design a pipeline', 'build a pipeline'
    ]
    if any(keyword in q_lower for keyword in pipeline_keywords):
        categories.append("Data Pipeline Design")
        if 'design' in q_lower:
            categories.append("System Design")
        return categories
    
    # Spark/Big Data specific
    spark_keywords = ['delta live tables', 'spark', 'delta lake', 'job cluster', 'all-purpose cluster', 'parquet', 'avro']
    if any(keyword in q_lower for keyword in spark_keywords):
        categories.append("Spark/Big Data")
        return categories
    
    # Data Warehousing
    if any(keyword in q_lower for keyword in ['data warehouse', 'warehouse', 'redshift', 'snowflake', 'bigquery', 'olap', 'data mart', 'dimensional']):
        categories.append("Data Warehousing")
    
    # Streaming Data
    if any(keyword in q_lower for keyword in ['stream', 'streaming', 'kafka', 'kinesis', 'real-time', 'realtime', 'clickstream']):
        categories.append("Streaming Data")
    
    # Cloud Platforms
    if any(keyword in q_lower for keyword in ['aws', 's3', 'ec2', 'lambda', 'glue', 'emr', 'azure', 'gcp', 'cloud', 'databricks', 'alexa']):
        categories.append("Cloud Platforms")
    
    # System Design (broader design questions)
    if any(keyword in q_lower for keyword in ['design a', 'design an', 'system design', 'architecture', 'how would you build', 'scalability']):
        if "Data Structures & Algorithms" not in categories:  # Don't double-categorize DSA
            categories.append("System Design")
    
    # Data Modeling
    if any(keyword in q_lower for keyword in ['data model', 'schema', 'database schema', 'design a database', 'star schema', 'snowflake schema', 'dimensional model', 'fact table', 'dimension table']):
        categories.append("Data Modeling")
    
    # Data Quality
    if any(keyword in q_lower for keyword in ['data quality', 'data validation', 'data integrity', 'missing data', 'duplicate', 'missing item', 'wrong item']):
        categories.append("Data Quality")
    
    # Data Governance
    if any(keyword in q_lower for keyword in ['governance', 'compliance', 'gdpr', 'privacy', 'security', 'access control', 'audit']):
        categories.append("Data Governance")
    
    # Monitoring & Observability
    if any(keyword in q_lower for keyword in ['monitor', 'monitoring', 'observability', 'logging', 'alerting', 'metrics', 'dashboard']):
        categories.append("Monitoring & Observability")
    
    # Performance Optimization
    if any(keyword in q_lower for keyword in ['optimize', 'optimization', 'performance', 'speed up', 'efficiency', 'bottleneck', 'slow query', 'multithreading', 'multiprocessing']):
        categories.append("Performance Optimization")
    
    # Database Design
    if any(keyword in q_lower for keyword in ['database', 'db', 'mysql', 'postgresql', 'nosql', 'mongodb', 'cassandra', 'dynamodb', 'redis']):
        if "Data Modeling" not in categories:
            categories.append("Database Design")
    
    # Coding (general, for questions that don't fit elsewhere)
    coding_keywords = ['implement', 'write a function', 'build a', 'create a']
    if any(keyword in q_lower for keyword in coding_keywords):
        if not categories:  # Only if nothing else matched
            categories.append("Coding")
    
    # Data tools question
    if 'data tools have you worked with' in q_lower:
        categories.append("Behavioral")
        return categories
    
    # Analysis questions (PM-style but for DE)
    if any(keyword in q_lower for keyword in ['how would you investigate', 'how would you analyze', 'conversion rates', 'declined']):
        categories.append("Data Pipeline Design")  # DE perspective on analysis
    
    # Default: if still no categories, mark as Data Pipeline Design
    if not categories:
        categories.append("Data Pipeline Design")
    
    return list(set(categories))

def main():
    """Load raw questions, categorize them, and save results"""
    
    # Load raw questions
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    raw_path = os.path.join(data_dir, 'questions_raw.json')
    
    with open(raw_path, 'r') as f:
        questions = json.load(f)
    
    print(f"📊 Categorizing {len(questions)} Data Engineer questions...")
    print("🎯 Using comprehensive categorization for your #1 goal role!")
    
    # Categorize each question
    categorized = []
    by_category = {cat: [] for cat in CATEGORIES}
    
    for q in questions:
        q_text = q['question']
        q_url = q.get('url', '')
        
        # Get categories
        cats = categorize_question(q_text, q_url)
        
        # Update question
        q['categories'] = cats
        categorized.append(q)
        
        # Add to by_category
        for cat in cats:
            if cat in by_category:
                by_category[cat].append({
                    'question': q_text,
                    'url': q_url
                })
    
    # Save categorized questions
    categorized_path = os.path.join(data_dir, 'questions_categorized.json')
    with open(categorized_path, 'w') as f:
        json.dump(categorized, f, indent=2)
    print(f"✅ Saved to {categorized_path}")
    
    # Save by category
    by_category_path = os.path.join(data_dir, 'questions_by_category.json')
    with open(by_category_path, 'w') as f:
        json.dump(by_category, f, indent=2)
    print(f"✅ Saved to {by_category_path}")
    
    # Print summary
    print("\n" + "="*70)
    print("📋 Questions per category:")
    print("="*70)
    
    # Sort by count
    category_counts = [(cat, len(by_category[cat])) for cat in CATEGORIES]
    category_counts.sort(key=lambda x: x[1], reverse=True)
    
    for cat, count in category_counts:
        if count > 0:
            print(f"  {cat.ljust(35)} {count:>3}")
    
    print(f"\n📊 Total questions: {len(categorized)}")
    print("🎯 Ready to ace your Data Engineer interviews!")

if __name__ == "__main__":
    main()
