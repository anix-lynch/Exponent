"""
Categorize ML Engineer questions
"""
import json
import os

CATEGORIES = [
    "Machine Learning",
    "Deep Learning",
    "Natural Language Processing",
    "Computer Vision",
    "Model Deployment",
    "Data Structures & Algorithms",
    "System Design",
    "ML System Design",
    "Behavioral",
    "Coding",
    "Statistics & Probability",
    "Model Evaluation",
    "Feature Engineering",
    "Optimization",
    "Reinforcement Learning",
    "Generative AI",
    "LLMs",
    "MLOps",
    "Data Processing",
    "SQL"
]

def categorize_question(question_text):
    q_lower = question_text.lower()
    categories = []
    
    # Behavioral (highest priority)
    behavioral_phrases = [
        'tell me about a time', 'describe a time', 'have you ever', 'walk me through',
        'tell me about yourself', 'why do you want to work at', 'past projects',
        'made a mistake', 'disagreed', 'conflict', 'difficult decision'
    ]
    if any(phrase in q_lower for phrase in behavioral_phrases):
        return ["Behavioral"]
    
    # LLMs & Generative AI
    if any(kw in q_lower for kw in ['llm', 'large language model', 'gpt', 'bert', 'transformer', 'attention mechanism', 'context window']):
        categories.append("LLMs")
    if any(kw in q_lower for kw in ['generative', 'gen ai', 'diffusion', 'gan', 'vae', 'stable diffusion']):
        categories.append("Generative AI")
    
    # NLP
    if any(kw in q_lower for kw in ['nlp', 'natural language', 'text', 'tokenization', 'embedding', 'sentiment', 'named entity']):
        categories.append("Natural Language Processing")
    
    # Computer Vision
    if any(kw in q_lower for kw in ['computer vision', 'image', 'cnn', 'convolutional', 'object detection', 'segmentation', 'yolo', 'resnet']):
        categories.append("Computer Vision")
    
    # Reinforcement Learning
    if any(kw in q_lower for kw in ['reinforcement learning', 'rl', 'q-learning', 'policy', 'reward', 'agent', 'markov']):
        categories.append("Reinforcement Learning")
    
    # Deep Learning
    if any(kw in q_lower for kw in ['deep learning', 'neural network', 'backpropagation', 'gradient descent', 'activation function', 'dropout', 'batch normalization']):
        categories.append("Deep Learning")
    
    # Machine Learning (general)
    if any(kw in q_lower for kw in ['machine learning', 'supervised', 'unsupervised', 'classification', 'regression', 'clustering', 'random forest', 'svm', 'decision tree']):
        categories.append("Machine Learning")
    
    # Model Evaluation
    if any(kw in q_lower for kw in ['accuracy', 'precision', 'recall', 'f1', 'auc', 'roc', 'confusion matrix', 'overfitting', 'underfitting', 'bias-variance']):
        categories.append("Model Evaluation")
    
    # Model Deployment & MLOps
    if any(kw in q_lower for kw in ['deploy', 'production', 'serving', 'inference', 'latency', 'throughput', 'model monitoring']):
        categories.append("Model Deployment")
    if any(kw in q_lower for kw in ['mlops', 'ml pipeline', 'model versioning', 'experiment tracking', 'mlflow']):
        categories.append("MLOps")
    
    # Feature Engineering
    if any(kw in q_lower for kw in ['feature engineering', 'feature selection', 'feature extraction', 'dimensionality reduction', 'pca']):
        categories.append("Feature Engineering")
    
    # Statistics & Probability
    if any(kw in q_lower for kw in ['statistics', 'probability', 'distribution', 'hypothesis test', 'p-value', 'confidence interval', 'bayesian']):
        categories.append("Statistics & Probability")
    
    # Optimization
    if any(kw in q_lower for kw in ['optimization', 'gradient descent', 'adam', 'sgd', 'learning rate', 'hyperparameter']):
        categories.append("Optimization")
    
    # DSA
    dsa_patterns = [
        'array', 'linked list', 'tree', 'graph', 'hash', 'sorting', 'binary search',
        'dynamic programming', 'two pointers', 'sliding window'
    ]
    if any(pattern in q_lower for pattern in dsa_patterns):
        return ["Data Structures & Algorithms"]
    
    # Coding
    if any(kw in q_lower for kw in ['implement', 'write a function', 'code', 'algorithm']) and not categories:
        categories.append("Coding")
    
    # System Design
    if 'design a' in q_lower or 'design an' in q_lower:
        if any(kw in q_lower for kw in ['ml', 'model', 'recommendation', 'search', 'ranking']):
            categories.append("ML System Design")
        else:
            categories.append("System Design")
    
    # Data Processing
    if any(kw in q_lower for kw in ['data processing', 'data pipeline', 'etl', 'spark', 'hadoop']):
        categories.append("Data Processing")
    
    # SQL
    if any(kw in q_lower for kw in ['sql', 'query', 'database', 'select', 'join']):
        categories.append("SQL")
    
    # Default
    if not categories:
        categories.append("Machine Learning")
    
    return list(set(categories))

def main():
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    raw_path = os.path.join(data_dir, 'questions_raw.json')
    
    with open(raw_path, 'r') as f:
        questions = json.load(f)
    
    print(f"📊 Categorizing {len(questions)} ML Engineer questions...")
    
    categorized = []
    by_category = {cat: [] for cat in CATEGORIES}
    
    for q in questions:
        cats = categorize_question(q['question'])
        q['categories'] = cats
        categorized.append(q)
        
        for cat in cats:
            if cat in by_category:
                by_category[cat].append({
                    'question': q['question'],
                    'url': q.get('url', '')
                })
    
    # Save
    categorized_path = os.path.join(data_dir, 'questions_categorized.json')
    with open(categorized_path, 'w') as f:
        json.dump(categorized, f, indent=2)
    print(f"✅ Saved to {categorized_path}")
    
    by_category_path = os.path.join(data_dir, 'questions_by_category.json')
    with open(by_category_path, 'w') as f:
        json.dump(by_category, f, indent=2)
    print(f"✅ Saved to {by_category_path}")
    
    print("\n" + "="*70)
    print("📋 Questions per category:")
    print("="*70)
    
    category_counts = [(cat, len(by_category[cat])) for cat in CATEGORIES]
    category_counts.sort(key=lambda x: x[1], reverse=True)
    
    for cat, count in category_counts:
        if count > 0:
            print(f"  {cat.ljust(40)} {count:>3}")
    
    print(f"\n📊 Total questions: {len(categorized)}")

if __name__ == "__main__":
    main()
