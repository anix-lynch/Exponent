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
    
    # Behavioral Questions
    if any(phrase in q_lower for phrase in ['tell me about a time', 'describe a time', 'have you ever', 'walk me through', 'past projects', 'made a mistake', 'faced challenges', 'conflict', 'disagreement', 'failure', 'difficult decision', 'skill you learned', 'difficult to work with']):
        categories.append("Behavioral")
    
    # Data Pipeline Design
    if any(keyword in q_lower for keyword in ['pipeline', 'data pipeline', 'build a pipeline', 'design a pipeline', 'data flow', 'ingestion', 'orchestration', 'airflow', 'workflow']):
        categories.append("Data Pipeline Design")
    
    # ETL/ELT
    if any(keyword in q_lower for keyword in ['etl', 'elt', 'extract', 'transform', 'load', 'data integration', 'data migration']):
        categories.append("ETL/ELT")
    
    # Data Modeling
    if any(keyword in q_lower for keyword in ['data model', 'schema', 'database schema', 'design a database', 'star schema', 'snowflake schema', 'dimensional model', 'fact table', 'dimension table', 'fitness app', 'e-commerce']):
        categories.append("Data Modeling")
    
    # SQL
    if any(keyword in q_lower for keyword in ['sql', 'query', 'select', 'join', 'group by', 'window function', 'cte', 'subquery']):
        categories.append("SQL")
    
    # Data Structures & Algorithms
    if any(keyword in q_lower for keyword in ['array', 'linked list', 'tree', 'graph', 'hash', 'heap', 'stack', 'queue', 'binary search', 'sorting', 'dynamic programming', 'lru cache', 'merge intervals', 'two sum', 'robber', 'container with most water']):
        categories.append("Data Structures & Algorithms")
    
    # Coding (general)
    if any(keyword in q_lower for keyword in ['implement', 'write a function', 'code', 'algorithm', 'solution']):
        if "Data Structures & Algorithms" not in categories:
            categories.append("Coding")
    
    # System Design
    if any(keyword in q_lower for keyword in ['design a', 'design an', 'system design', 'architecture', 'how would you build', 'scalability', 'design twitter', 'design uber', 'design netflix']):
        categories.append("System Design")
    
    # Distributed Systems
    if any(keyword in q_lower for keyword in ['distributed', 'sharding', 'replication', 'consistency', 'partition', 'consensus', 'distributed system', 'distributed database']):
        categories.append("Distributed Systems")
    
    # Data Warehousing
    if any(keyword in q_lower for keyword in ['data warehouse', 'warehouse', 'redshift', 'snowflake', 'bigquery', 'olap', 'data mart', 'dimensional']):
        categories.append("Data Warehousing")
    
    # Streaming Data
    if any(keyword in q_lower for keyword in ['stream', 'streaming', 'kafka', 'kinesis', 'real-time', 'realtime', 'event', 'message queue']):
        categories.append("Streaming Data")
    
    # Batch Processing
    if any(keyword in q_lower for keyword in ['batch', 'batch processing', 'scheduled', 'cron', 'daily load']):
        categories.append("Batch Processing")
    
    # Cloud Platforms
    if any(keyword in q_lower for keyword in ['aws', 's3', 'ec2', 'lambda', 'glue', 'emr', 'azure', 'gcp', 'cloud', 'databricks']):
        categories.append("Cloud Platforms")
    
    # Spark/Big Data
    if any(keyword in q_lower for keyword in ['spark', 'pyspark', 'hadoop', 'mapreduce', 'hive', 'presto', 'big data']):
        categories.append("Spark/Big Data")
    
    # Database Design
    if any(keyword in q_lower for keyword in ['database', 'db', 'mysql', 'postgresql', 'nosql', 'mongodb', 'cassandra', 'dynamodb', 'redis']):
        if "Data Modeling" not in categories:
            categories.append("Database Design")
    
    # Schema Design
    if any(keyword in q_lower for keyword in ['schema', 'table design', 'index', 'primary key', 'foreign key', 'normalization', 'denormalization']):
        if "Data Modeling" not in categories:
            categories.append("Schema Design")
    
    # Performance Optimization
    if any(keyword in q_lower for keyword in ['optimize', 'optimization', 'performance', 'speed up', 'improve', 'efficiency', 'bottleneck', 'slow query']):
        categories.append("Performance Optimization")
    
    # Data Quality
    if any(keyword in q_lower for keyword in ['data quality', 'data validation', 'data integrity', 'data cleansing', 'data accuracy', 'missing data', 'duplicate']):
        categories.append("Data Quality")
    
    # Data Governance
    if any(keyword in q_lower for keyword in ['governance', 'compliance', 'gdpr', 'privacy', 'security', 'access control', 'audit']):
        categories.append("Data Governance")
    
    # Monitoring & Observability
    if any(keyword in q_lower for keyword in ['monitor', 'monitoring', 'observability', 'logging', 'alerting', 'metrics', 'dashboard']):
        categories.append("Monitoring & Observability")
    
    # Default to Data Pipeline Design if no categories found (most common DE question type)
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
