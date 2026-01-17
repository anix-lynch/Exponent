"""
Categorize SWE questions into interview categories
"""
import json
import os

# SWE Categories
CATEGORIES = [
    "Data Structures & Algorithms",
    "System Design",
    "Behavioral",
    "Coding",
    "Object-Oriented Design",
    "Debugging",
    "Testing",
    "Architecture",
    "Scalability",
    "Databases",
    "APIs",
    "Security",
    "Performance Optimization",
    "Concurrency",
    "Distributed Systems",
    "Problem Solving",
    "Technical Communication",
    "Code Review",
    "Leadership",
    "Project Management"
]

def categorize_question(question_text, url=""):
    """Categorize a SWE question based on keywords and patterns"""
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral Questions
    if any(phrase in q_lower for phrase in ['tell me about a time', 'describe a time', 'have you ever', 'walk me through', 'made a mistake', 'faced challenges', 'conflict', 'disagreement', 'failure', 'difficult decision', 'worked on a project', 'tight deadline']):
        categories.append("Behavioral")
    
    # Data Structures & Algorithms
    if any(keyword in q_lower for keyword in ['array', 'linked list', 'tree', 'graph', 'hash', 'heap', 'stack', 'queue', 'binary search', 'sorting', 'dynamic programming', 'recursion', 'backtracking', 'greedy', 'two pointer', 'sliding window', 'bfs', 'dfs', 'dijkstra', 'topological']):
        categories.append("Data Structures & Algorithms")
    
    # Coding (general)
    if any(keyword in q_lower for keyword in ['write a function', 'implement', 'code', 'algorithm', 'solution', 'fibonacci', 'palindrome', 'reverse', 'merge', 'find', 'calculate', 'return']):
        if "Data Structures & Algorithms" not in categories:
            categories.append("Coding")
    
    # Check URL for coding problems
    if any(term in url.lower() for term in ['earnings', 'salaries', 'employees', 'merge-intervals', 'fibonacci', 'palindrome', 'reverse', 'two-sum', 'three-sum']):
        if "Coding" not in categories:
            categories.append("Coding")
    
    # System Design
    if any(keyword in q_lower for keyword in ['design a', 'design an', 'system design', 'architecture', 'how would you build', 'design twitter', 'design facebook', 'design instagram', 'design uber', 'design netflix', 'url shortener', 'rate limiter', 'load balancer', 'cache', 'cdn']):
        categories.append("System Design")
    
    # Object-Oriented Design
    if any(keyword in q_lower for keyword in ['oop', 'object-oriented', 'class', 'inheritance', 'polymorphism', 'encapsulation', 'design pattern', 'singleton', 'factory', 'observer', 'decorator']):
        categories.append("Object-Oriented Design")
    
    # Distributed Systems
    if any(keyword in q_lower for keyword in ['distributed', 'microservices', 'sharding', 'replication', 'consistency', 'partition', 'consensus', 'raft', 'paxos', 'cap theorem']):
        categories.append("Distributed Systems")
    
    # Scalability
    if any(keyword in q_lower for keyword in ['scale', 'scalability', 'horizontal scaling', 'vertical scaling', 'load balancing', 'high availability', 'throughput', 'latency']):
        categories.append("Scalability")
    
    # Databases
    if any(keyword in q_lower for keyword in ['database', 'sql', 'nosql', 'mysql', 'postgresql', 'mongodb', 'redis', 'cassandra', 'query', 'index', 'transaction', 'acid', 'normalization']):
        categories.append("Databases")
    
    # APIs
    if any(keyword in q_lower for keyword in ['api', 'rest', 'restful', 'graphql', 'endpoint', 'http', 'request', 'response', 'json', 'xml']):
        categories.append("APIs")
    
    # Security
    if any(keyword in q_lower for keyword in ['security', 'authentication', 'authorization', 'encryption', 'hashing', 'oauth', 'jwt', 'xss', 'csrf', 'sql injection', 'vulnerability']):
        categories.append("Security")
    
    # Performance Optimization
    if any(keyword in q_lower for keyword in ['optimize', 'optimization', 'performance', 'speed up', 'improve', 'efficiency', 'bottleneck', 'profiling']):
        categories.append("Performance Optimization")
    
    # Concurrency
    if any(keyword in q_lower for keyword in ['thread', 'concurrency', 'parallel', 'mutex', 'lock', 'semaphore', 'deadlock', 'race condition', 'synchronization']):
        categories.append("Concurrency")
    
    # Debugging
    if any(keyword in q_lower for keyword in ['debug', 'debugging', 'bug', 'error', 'issue', 'troubleshoot', 'fix']):
        categories.append("Debugging")
    
    # Testing
    if any(keyword in q_lower for keyword in ['test', 'testing', 'unit test', 'integration test', 'tdd', 'test-driven', 'qa', 'quality assurance']):
        categories.append("Testing")
    
    # Architecture
    if any(keyword in q_lower for keyword in ['architecture', 'architectural', 'design decision', 'trade-off', 'tradeoff']):
        if "System Design" not in categories:
            categories.append("Architecture")
    
    # Problem Solving
    if any(keyword in q_lower for keyword in ['approach', 'solve', 'solution', 'strategy', 'how would you']):
        if not categories:
            categories.append("Problem Solving")
    
    # Technical Communication
    if any(keyword in q_lower for keyword in ['explain', 'describe', 'communicate', 'technical concept', 'non-technical']):
        categories.append("Technical Communication")
    
    # Code Review
    if any(keyword in q_lower for keyword in ['code review', 'review code', 'feedback', 'best practices', 'coding standards']):
        categories.append("Code Review")
    
    # Leadership
    if any(keyword in q_lower for keyword in ['lead', 'leadership', 'mentor', 'team', 'manage', 'influence']):
        if "Behavioral" not in categories:
            categories.append("Leadership")
    
    # Project Management
    if any(keyword in q_lower for keyword in ['project', 'deadline', 'prioritize', 'planning', 'estimate']):
        if "Behavioral" not in categories:
            categories.append("Project Management")
    
    # Default to Problem Solving if no categories found
    if not categories:
        categories.append("Problem Solving")
    
    return list(set(categories))

def main():
    """Load raw questions, categorize them, and save results"""
    
    # Load raw questions
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    raw_path = os.path.join(data_dir, 'questions_raw.json')
    
    with open(raw_path, 'r') as f:
        questions = json.load(f)
    
    print(f"📊 Categorizing {len(questions)} questions...")
    
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

if __name__ == "__main__":
    main()
