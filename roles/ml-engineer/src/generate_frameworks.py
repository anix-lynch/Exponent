"""
Generate ML Engineer Question Bank with frameworks
"""
import json

with open('data/questions_by_category.json', 'r') as f:
    questions_by_category = json.load(f)

FRAMEWORKS = {
    "Machine Learning": """
Machine Learning
├─ Understand the problem
│  ├─ What type? (Classification/Regression/Clustering)
│  ├─ What's the goal?
│  └─ What data is available?
│
├─ Choose algorithm
│  ├─ Supervised (labeled data)
│  ├─ Unsupervised (no labels)
│  └─ Semi-supervised
│
├─ Feature engineering
│  ├─ Feature selection
│  ├─ Feature extraction
│  └─ Normalization/Scaling
│
├─ Train & evaluate
│  ├─ Train/val/test split
│  ├─ Cross-validation
│  └─ Metrics (accuracy, F1, etc.)
│
└─ Iterate & improve
   ├─ Hyperparameter tuning
   ├─ Feature engineering
   └─ Try different models
""",

    "Deep Learning": """
Deep Learning
├─ Architecture design
│  ├─ Input layer
│  ├─ Hidden layers
│  ├─ Output layer
│  └─ Activation functions
│
├─ Training
│  ├─ Loss function
│  ├─ Optimizer (Adam, SGD)
│  ├─ Learning rate
│  └─ Batch size
│
├─ Regularization
│  ├─ Dropout
│  ├─ Batch normalization
│  ├─ L1/L2 regularization
│  └─ Early stopping
│
└─ Evaluation
   ├─ Validation loss
   ├─ Overfitting check
   └─ Test set performance
""",

    "LLMs": """
LLMs (Large Language Models)
├─ Architecture
│  ├─ Transformer
│  ├─ Attention mechanism
│  ├─ Context window
│  └─ Tokenization
│
├─ Training
│  ├─ Pre-training (unsupervised)
│  ├─ Fine-tuning (supervised)
│  ├─ RLHF (Reinforcement Learning from Human Feedback)
│  └─ Prompt engineering
│
├─ Inference
│  ├─ Temperature
│  ├─ Top-k/Top-p sampling
│  ├─ Context management
│  └─ Latency optimization
│
└─ Evaluation
   ├─ Perplexity
   ├─ Human evaluation
   └─ Task-specific metrics
""",

    "Computer Vision": """
Computer Vision
├─ Problem type
│  ├─ Classification
│  ├─ Object detection
│  ├─ Segmentation
│  └─ Image generation
│
├─ Architecture
│  ├─ CNN (Convolutional Neural Network)
│  ├─ ResNet, VGG, etc.
│  ├─ Vision Transformer
│  └─ Transfer learning
│
├─ Data preprocessing
│  ├─ Normalization
│  ├─ Augmentation
│  └─ Resizing
│
└─ Evaluation
   ├─ Accuracy
   ├─ IoU (Intersection over Union)
   └─ mAP (mean Average Precision)
""",

    "ML System Design": """
ML System Design
├─ Requirements (5 min)
│  ├─ Problem definition
│  ├─ Scale (QPS, users)
│  ├─ Latency requirements
│  └─ Accuracy requirements
│
├─ High-level design (10 min)
│  ├─ Data collection
│  ├─ Feature engineering
│  ├─ Model training
│  ├─ Model serving
│  └─ Monitoring
│
├─ Deep dive (20 min)
│  ├─ Model choice
│  ├─ Training pipeline
│  ├─ Inference optimization
│  ├─ A/B testing
│  └─ Feedback loop
│
└─ Trade-offs
   ├─ Accuracy vs Latency
   ├─ Complexity vs Interpretability
   └─ Cost vs Performance
""",

    "Model Deployment": """
Model Deployment
├─ Serving infrastructure
│  ├─ REST API
│  ├─ gRPC
│  ├─ Batch vs Real-time
│  └─ Load balancing
│
├─ Optimization
│  ├─ Model compression
│  ├─ Quantization
│  ├─ Pruning
│  └─ Caching
│
├─ Monitoring
│  ├─ Latency
│  ├─ Throughput
│  ├─ Model drift
│  └─ Data drift
│
└─ Scaling
   ├─ Horizontal scaling
   ├─ Auto-scaling
   └─ GPU utilization
""",

    "Data Structures & Algorithms": """
Data Structures & Algorithms
├─ Understand problem
│  ├─ Input/output
│  ├─ Constraints
│  └─ Edge cases
│
├─ Choose data structure
│  ├─ Array/List
│  ├─ Hash Map/Set
│  ├─ Tree/Graph
│  └─ Heap/Stack/Queue
│
├─ Design algorithm
│  ├─ Brute force first
│  ├─ Identify pattern
│  └─ Optimize
│
└─ Analyze complexity
   ├─ Time: O(?)
   └─ Space: O(?)
""",

    "Behavioral": """
Behavioral (STAR Method)
├─ Situation
│  ├─ Context
│  └─ Challenge
│
├─ Task
│  ├─ Your role
│  └─ Goal
│
├─ Action
│  ├─ What YOU did
│  └─ Technical decisions
│
└─ Result
   ├─ Impact (quantify!)
   └─ Learnings
""",

    "System Design": """
System Design
├─ Requirements
│  ├─ Functional
│  ├─ Non-functional
│  └─ Scale
│
├─ High-level design
│  ├─ Components
│  ├─ Data flow
│  └─ APIs
│
├─ Deep dive
│  ├─ Database design
│  ├─ Caching
│  ├─ Load balancing
│  └─ Scaling
│
└─ Trade-offs
   ├─ Consistency vs Availability
   └─ Latency vs Throughput
"""
}

TESTING_EXPLANATIONS = {
    "Machine Learning": "Do you understand ML fundamentals and when to apply different algorithms?",
    "Deep Learning": "Can you design and train neural networks effectively?",
    "LLMs": "Do you understand how large language models work and how to use them?",
    "Computer Vision": "Can you build and deploy computer vision models?",
    "ML System Design": "Can you design end-to-end ML systems at scale?",
    "Model Deployment": "Can you deploy and serve ML models in production?",
    "Data Structures & Algorithms": "Can you write efficient code to solve problems?",
    "Behavioral": "Can you work effectively in a team?",
    "System Design": "Can you design scalable systems?",
    "Natural Language Processing": "Do you understand NLP techniques and applications?",
    "Reinforcement Learning": "Do you understand RL concepts and algorithms?",
    "Generative AI": "Can you work with generative models like GANs and diffusion models?",
    "Model Evaluation": "Do you know how to evaluate and improve ML models?",
    "Coding": "Can you implement ML algorithms from scratch?",
    "MLOps": "Do you understand ML operations and best practices?",
    "Statistics & Probability": "Do you have strong statistical foundations?",
    "SQL": "Can you query and manipulate data?",
    "Optimization": "Do you understand optimization techniques for ML?",
    "Feature Engineering": "Can you create effective features for ML models?",
    "Data Processing": "Can you process and prepare data for ML?"
}

# Generate Question Bank
output = []
output.append("")
output.append("╔════════════════════════════════════════════════════════════════════════════════╗")
output.append("║                                                                                ║")
output.append("║          ML ENGINEER INTERVIEW PREPARATION FRAMEWORK                           ║")
output.append("║          Mental Models & Complete Question Bank                                ║")
output.append("║                                                                                ║")
output.append("╚════════════════════════════════════════════════════════════════════════════════╝")
output.append("")
output.append("This framework provides comprehensive mental models for ML Engineer interviews.")
output.append("")
output.append("Focus on understanding the PATTERN and FRAMEWORK, not memorizing answers.")
output.append("")
output.append(f"Total Questions: {sum(len(qs) for qs in questions_by_category.values())} across {len([c for c in questions_by_category if questions_by_category[c]])} categories")
output.append("")
output.append("")

sorted_categories = sorted(questions_by_category.items(), key=lambda x: len(x[1]), reverse=True)

for category, questions in sorted_categories:
    if not questions:
        continue
        
    output.append("=" * 80)
    output.append(category.upper())
    output.append("=" * 80)
    output.append("")
    output.append(f"📊 Total Questions: {len(questions)}")
    output.append("")
    output.append("🎯 What they're really testing:")
    output.append(TESTING_EXPLANATIONS.get(category, "Can you handle this type of question effectively?"))
    output.append("")
    output.append("🗺️  Mental Model Framework:")
    output.append("```")
    output.append(FRAMEWORKS.get(category, "Framework coming soon..."))
    output.append("```")
    output.append("")
    output.append(f"📝 All {len(questions)} Questions:")
    output.append("")
    
    for i, q in enumerate(questions, 1):
        output.append(f"{i}. {q['question']}")
    
    output.append("")
    output.append("")

output_file = 'ML_Engineer_Question_Bank.md'
with open(output_file, 'w') as f:
    f.write('\n'.join(output))

print(f"✅ Generated {output_file}")
print(f"📊 Total: {sum(len(qs) for qs in questions_by_category.values())} questions")
