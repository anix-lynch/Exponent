# 🧠 ML Engineer Interview Mindmap (Systematic)

## 📚 Resources

**GitHub Repo**: https://github.com/anix-lynch/Exponent

**Source**: https://www.tryexponent.com/questions?page=1&role=ml-engineer

---

## 📊 Question Distribution

```
Machine Learning........................  103 questions
Data Structures & Algorithms............   39 questions
System Design...........................   20 questions
Behavioral..............................   20 questions
Computer Vision.........................   11 questions
ML System Design........................   11 questions
Model Evaluation........................   10 questions
Coding..................................    9 questions
Deep Learning...........................    8 questions
Model Deployment........................    8 questions
LLMs....................................    7 questions
Reinforcement Learning..................    6 questions
Generative AI...........................    6 questions
Natural Language Processing.............    5 questions
SQL.....................................    4 questions
Statistics & Probability................    3 questions
MLOps...................................    2 questions
Optimization............................    1 question
```

**Total: 250 questions across 18 categories**

---

## 🔟 How to USE this in interviews

When a question comes:

1. **Name the category silently**
2. **Apply that category's framework**
3. **Speak in structured bullets**

---

## 0️⃣ Core ML Engineering Meta-Structure

Every ML interview tests:

- **ML fundamentals** (algorithms, evaluation, optimization)
- **System thinking** (end-to-end ML systems)
- **Coding ability** (implement algorithms, process data)
- **Production mindset** (deployment, monitoring, scaling)

So every answer should follow:

```
Clarify → Design → Implement → Evaluate → Deploy → Monitor
```

---

## 1️⃣ Machine Learning (CRITICAL - 103 questions)

**What they're really testing:**
Do you understand ML fundamentals and when to apply different algorithms?

**Mindmap**

```
Machine Learning
├─ 1. Problem Understanding
│  ├─ Classification vs Regression vs Clustering
│  ├─ Supervised vs Unsupervised vs Semi-supervised
│  ├─ Available data (labeled/unlabeled)
│  └─ Success metrics
│
├─ 2. Algorithm Selection
│  ├─ Linear models (LR, Lasso, Ridge)
│  ├─ Tree-based (Decision Tree, Random Forest, XGBoost)
│  ├─ SVM (Support Vector Machine)
│  ├─ Neural Networks
│  └─ Ensemble methods
│
├─ 3. Feature Engineering
│  ├─ Feature selection (filter, wrapper, embedded)
│  ├─ Feature extraction (PCA, t-SNE)
│  ├─ Encoding (one-hot, label, target)
│  ├─ Scaling (standardization, normalization)
│  └─ Handling missing values
│
├─ 4. Training
│  ├─ Train/val/test split (70/15/15 or 80/10/10)
│  ├─ Cross-validation (k-fold)
│  ├─ Hyperparameter tuning (grid search, random search)
│  └─ Regularization (L1, L2, dropout)
│
├─ 5. Evaluation
│  ├─ Classification metrics (accuracy, precision, recall, F1, AUC-ROC)
│  ├─ Regression metrics (MSE, RMSE, MAE, R²)
│  ├─ Clustering metrics (silhouette, Davies-Bouldin)
│  └─ Confusion matrix analysis
│
└─ 6. Model Improvement
   ├─ Address overfitting (more data, regularization, simpler model)
   ├─ Address underfitting (more features, complex model)
   ├─ Feature engineering iteration
   └─ Ensemble methods
```

📌 **Always start with**: What type of problem? What data? What metric?

---

## 2️⃣ Data Structures & Algorithms (HIGH - 39 questions)

**What they're really testing:**
Can you write efficient code to solve problems?

**Mindmap**

```
DSA for ML Engineers
├─ 1. Problem Understanding
│  ├─ Input format
│  ├─ Output format
│  ├─ Constraints
│  └─ Edge cases
│
├─ 2. Data Structure Choice
│  ├─ Array/List (sequential access)
│  ├─ Hash Map/Set (O(1) lookup)
│  ├─ Tree (hierarchical data)
│  ├─ Graph (relationships)
│  ├─ Heap (priority queue)
│  └─ Stack/Queue (LIFO/FIFO)
│
├─ 3. Algorithm Patterns
│  ├─ Two pointers
│  ├─ Sliding window
│  ├─ BFS/DFS
│  ├─ Dynamic programming
│  ├─ Binary search
│  └─ Divide and conquer
│
├─ 4. Implementation
│  ├─ Write clean code
│  ├─ Handle edge cases
│  ├─ Test with examples
│  └─ Optimize
│
└─ 5. Complexity Analysis
   ├─ Time complexity: O(?)
   ├─ Space complexity: O(?)
   └─ Can we do better?
```

📌 **Think in terms of**: Time/space complexity, common patterns, edge cases

---

## 3️⃣ ML System Design (HIGH - 11 questions)

**What they're really testing:**
Can you design end-to-end ML systems at scale?

**Mindmap**

```
ML System Design
├─ 1. Requirements (5 min)
│  ├─ Problem definition
│  │  ├─ What are we predicting?
│  │  ├─ What's the business goal?
│  │  └─ Success metrics
│  ├─ Scale
│  │  ├─ QPS (queries per second)
│  │  ├─ Number of users
│  │  └─ Data volume
│  ├─ Latency requirements
│  │  ├─ Real-time (< 100ms)
│  │  ├─ Near real-time (< 1s)
│  │  └─ Batch (minutes/hours)
│  └─ Accuracy requirements
│
├─ 2. High-Level Design (10 min)
│  ├─ Data collection
│  │  ├─ User events
│  │  ├─ Logs
│  │  └─ External APIs
│  ├─ Feature engineering
│  │  ├─ Online features (real-time)
│  │  └─ Offline features (batch)
│  ├─ Model training
│  │  ├─ Training pipeline
│  │  ├─ Model selection
│  │  └─ Hyperparameter tuning
│  ├─ Model serving
│  │  ├─ Prediction API
│  │  ├─ Caching
│  │  └─ Load balancing
│  └─ Monitoring & feedback
│     ├─ Model performance
│     ├─ Data drift
│     └─ A/B testing
│
├─ 3. Deep Dive (20 min)
│  ├─ Model choice & architecture
│  │  ├─ Why this model?
│  │  ├─ Alternatives considered
│  │  └─ Trade-offs
│  ├─ Training pipeline
│  │  ├─ Data preprocessing
│  │  ├─ Feature store
│  │  ├─ Training frequency
│  │  └─ Experiment tracking
│  ├─ Inference optimization
│  │  ├─ Model compression
│  │  ├─ Quantization
│  │  ├─ Batching
│  │  └─ GPU utilization
│  ├─ A/B testing
│  │  ├─ Control vs treatment
│  │  ├─ Metrics to track
│  │  └─ Statistical significance
│  └─ Feedback loop
│     ├─ Collect predictions
│     ├─ Collect ground truth
│     └─ Retrain model
│
└─ 4. Trade-offs
   ├─ Accuracy vs Latency
   ├─ Complexity vs Interpretability
   ├─ Cost vs Performance
   └─ Online vs Offline learning
```

📌 **Always discuss**: Scale, latency, accuracy, trade-offs

---

## 4️⃣ System Design (20 questions)

**What they're really testing:**
Can you design scalable distributed systems?

**Mindmap**

```
System Design
├─ 1. Requirements (5 min)
│  ├─ Functional requirements
│  │  ├─ What features?
│  │  └─ What APIs?
│  ├─ Non-functional requirements
│  │  ├─ Scale (QPS, users, data)
│  │  ├─ Latency (ms, seconds)
│  │  ├─ Availability (99.9%?)
│  │  └─ Consistency
│  └─ Constraints
│
├─ 2. High-Level Design (10 min)
│  ├─ Draw architecture
│  ├─ Main components
│  ├─ Data flow
│  └─ APIs
│
├─ 3. Deep Dive (20 min)
│  ├─ Database design
│  │  ├─ SQL vs NoSQL
│  │  ├─ Schema design
│  │  └─ Indexing
│  ├─ Caching
│  │  ├─ Redis, Memcached
│  │  ├─ Cache invalidation
│  │  └─ TTL strategy
│  ├─ Load balancing
│  │  ├─ Round robin
│  │  ├─ Least connections
│  │  └─ Consistent hashing
│  └─ Scaling
│     ├─ Horizontal scaling
│     ├─ Vertical scaling
│     ├─ Sharding
│     └─ Replication
│
└─ 4. Trade-offs
   ├─ Consistency vs Availability (CAP theorem)
   ├─ Latency vs Throughput
   └─ Cost vs Performance
```

📌 **Draw diagrams**: Visual communication is key

---

## 5️⃣ Behavioral (20 questions)

**What they're really testing:**
Can you work effectively in a team?

**Mindmap (STAR Method)**

```
Behavioral
├─ Situation
│  ├─ Context
│  ├─ Challenge
│  └─ Stakeholders
│
├─ Task
│  ├─ Your role
│  ├─ Goal
│  └─ Constraints
│
├─ Action
│  ├─ What YOU did
│  ├─ Technical decisions
│  ├─ Trade-offs considered
│  └─ Collaboration
│
└─ Result
   ├─ Quantifiable impact
   ├─ What you learned
   └─ What you'd do differently
```

📌 **Common themes**: Project ownership, technical challenges, collaboration, learning from failure

---

## 6️⃣ Computer Vision (11 questions)

**What they're really testing:**
Can you build and deploy computer vision models?

**Mindmap**

```
Computer Vision
├─ 1. Problem Type
│  ├─ Image classification
│  ├─ Object detection (YOLO, R-CNN)
│  ├─ Semantic segmentation
│  ├─ Instance segmentation
│  └─ Image generation
│
├─ 2. Architecture
│  ├─ CNN (Convolutional Neural Network)
│  │  ├─ Conv layers
│  │  ├─ Pooling layers
│  │  └─ Fully connected layers
│  ├─ Pre-trained models
│  │  ├─ ResNet
│  │  ├─ VGG
│  │  ├─ EfficientNet
│  │  └─ Vision Transformer (ViT)
│  └─ Transfer learning
│
├─ 3. Data Preprocessing
│  ├─ Normalization
│  ├─ Augmentation (flip, rotate, crop)
│  ├─ Resizing
│  └─ Color space conversion
│
├─ 4. Training
│  ├─ Loss function (cross-entropy, focal loss)
│  ├─ Optimizer (Adam, SGD)
│  ├─ Learning rate schedule
│  └─ Data augmentation
│
└─ 5. Evaluation
   ├─ Accuracy
   ├─ IoU (Intersection over Union)
   ├─ mAP (mean Average Precision)
   └─ Confusion matrix
```

📌 **Transfer learning first**: Start with pre-trained models, fine-tune on your data

---

## 7️⃣ Model Evaluation (10 questions)

**What they're really testing:**
Do you know how to evaluate and improve ML models?

**Mindmap**

```
Model Evaluation
├─ 1. Classification Metrics
│  ├─ Accuracy (when balanced)
│  ├─ Precision (minimize false positives)
│  ├─ Recall (minimize false negatives)
│  ├─ F1 score (harmonic mean)
│  ├─ AUC-ROC (threshold-independent)
│  └─ Confusion matrix
│
├─ 2. Regression Metrics
│  ├─ MSE (Mean Squared Error)
│  ├─ RMSE (Root MSE)
│  ├─ MAE (Mean Absolute Error)
│  └─ R² (coefficient of determination)
│
├─ 3. Overfitting vs Underfitting
│  ├─ Overfitting
│  │  ├─ High train accuracy, low val accuracy
│  │  ├─ Solutions: regularization, more data, simpler model
│  │  └─ Dropout, early stopping
│  └─ Underfitting
│     ├─ Low train and val accuracy
│     ├─ Solutions: more features, complex model
│     └─ Feature engineering
│
├─ 4. Bias-Variance Trade-off
│  ├─ High bias = underfitting
│  ├─ High variance = overfitting
│  └─ Balance through regularization
│
└─ 5. Cross-Validation
   ├─ K-fold CV
   ├─ Stratified K-fold
   └─ Time series CV
```

📌 **Choose metric based on problem**: Imbalanced data? Use F1/AUC. Outliers matter? Use MAE.

---

## 8️⃣ Coding (9 questions)

**What they're really testing:**
Can you implement ML algorithms from scratch?

**Mindmap**

```
Coding
├─ 1. Understand requirements
│  ├─ Input format
│  ├─ Output format
│  ├─ Constraints
│  └─ Edge cases
│
├─ 2. Design approach
│  ├─ Algorithm choice
│  ├─ Data structures
│  └─ Pseudocode
│
├─ 3. Implement
│  ├─ Clean code
│  ├─ Meaningful names
│  ├─ Comments
│  └─ Error handling
│
├─ 4. Test
│  ├─ Normal cases
│  ├─ Edge cases
│  └─ Performance
│
└─ 5. Optimize
   ├─ Time complexity
   ├─ Space complexity
   └─ Code readability
```

📌 **Common tasks**: Implement gradient descent, backpropagation, k-means, decision tree

---

## 9️⃣ Deep Learning (8 questions)

**What they're really testing:**
Can you design and train neural networks effectively?

**Mindmap**

```
Deep Learning
├─ 1. Architecture Design
│  ├─ Input layer (match data dimensions)
│  ├─ Hidden layers
│  │  ├─ Number of layers (depth)
│  │  ├─ Number of neurons (width)
│  │  └─ Activation functions (ReLU, tanh, sigmoid)
│  └─ Output layer (match task)
│
├─ 2. Training
│  ├─ Loss function
│  │  ├─ Classification: Cross-entropy
│  │  ├─ Regression: MSE
│  │  └─ Custom losses
│  ├─ Optimizer
│  │  ├─ SGD (simple, stable)
│  │  ├─ Adam (adaptive, fast)
│  │  └─ RMSprop
│  ├─ Learning rate
│  │  ├─ Initial value
│  │  ├─ Schedule (decay, warmup)
│  │  └─ Learning rate finder
│  └─ Batch size
│     ├─ Small batch: noisy gradients, regularization
│     └─ Large batch: stable, faster training
│
├─ 3. Regularization
│  ├─ Dropout (randomly drop neurons)
│  ├─ Batch normalization (normalize activations)
│  ├─ L1/L2 regularization (weight penalty)
│  ├─ Early stopping (stop when val loss increases)
│  └─ Data augmentation
│
├─ 4. Optimization Techniques
│  ├─ Gradient descent variants
│  ├─ Momentum
│  ├─ Gradient clipping
│  └─ Batch normalization
│
└─ 5. Evaluation
   ├─ Training loss
   ├─ Validation loss
   ├─ Test accuracy
   └─ Learning curves
```

📌 **Start simple**: Shallow network first, then add complexity if needed

---

## 🔟 Model Deployment (8 questions)

**What they're really testing:**
Can you deploy and serve ML models in production?

**Mindmap**

```
Model Deployment
├─ 1. Serving Infrastructure
│  ├─ REST API (Flask, FastAPI)
│  ├─ gRPC (low latency)
│  ├─ Batch prediction
│  ├─ Real-time prediction
│  └─ Load balancing
│
├─ 2. Model Optimization
│  ├─ Model compression
│  │  ├─ Pruning (remove weights)
│  │  ├─ Quantization (reduce precision)
│  │  └─ Knowledge distillation
│  ├─ Inference optimization
│  │  ├─ Batching requests
│  │  ├─ Caching predictions
│  │  └─ GPU utilization
│  └─ Model formats
│     ├─ ONNX
│     ├─ TensorFlow Lite
│     └─ TorchScript
│
├─ 3. Monitoring
│  ├─ Latency (p50, p95, p99)
│  ├─ Throughput (QPS)
│  ├─ Error rate
│  ├─ Model drift
│  │  ├─ Data drift (input distribution changes)
│  │  └─ Concept drift (relationship changes)
│  └─ Resource utilization (CPU, GPU, memory)
│
├─ 4. Scaling
│  ├─ Horizontal scaling (add more servers)
│  ├─ Vertical scaling (bigger servers)
│  ├─ Auto-scaling
│  └─ GPU sharing
│
└─ 5. A/B Testing
   ├─ Control vs treatment
   ├─ Metrics to track
   ├─ Statistical significance
   └─ Gradual rollout
```

📌 **Production = monitoring + optimization + reliability**

---

## 1️⃣1️⃣ LLMs (7 questions)

**What they're really testing:**
Do you understand how large language models work?

**Mindmap**

```
LLMs (Large Language Models)
├─ 1. Architecture
│  ├─ Transformer
│  │  ├─ Self-attention mechanism
│  │  ├─ Multi-head attention
│  │  └─ Positional encoding
│  ├─ Context window
│  │  ├─ Token limit (e.g., 4K, 8K, 128K)
│  │  ├─ Lost in the middle problem
│  │  └─ Context management
│  └─ Tokenization
│     ├─ BPE (Byte Pair Encoding)
│     ├─ WordPiece
│     └─ SentencePiece
│
├─ 2. Training
│  ├─ Pre-training (unsupervised)
│  │  ├─ Next token prediction
│  │  ├─ Masked language modeling
│  │  └─ Large corpus
│  ├─ Fine-tuning (supervised)
│  │  ├─ Task-specific data
│  │  ├─ Instruction tuning
│  │  └─ Few-shot learning
│  └─ RLHF (Reinforcement Learning from Human Feedback)
│     ├─ Reward model
│     ├─ PPO (Proximal Policy Optimization)
│     └─ Human preferences
│
├─ 3. Inference
│  ├─ Sampling strategies
│  │  ├─ Greedy (deterministic)
│  │  ├─ Temperature (randomness)
│  │  ├─ Top-k sampling
│  │  └─ Top-p (nucleus) sampling
│  ├─ Prompt engineering
│  │  ├─ Zero-shot
│  │  ├─ Few-shot
│  │  └─ Chain-of-thought
│  └─ Context management
│     ├─ Sliding window
│     ├─ Summarization
│     └─ Retrieval augmentation (RAG)
│
└─ 4. Evaluation
   ├─ Perplexity
   ├─ BLEU, ROUGE (text generation)
   ├─ Human evaluation
   └─ Task-specific metrics
```

📌 **Context window is key**: Longer context = more information but higher cost and latency

---

## 1️⃣2️⃣ Reinforcement Learning (6 questions)

**What they're really testing:**
Do you understand RL concepts and algorithms?

**Mindmap**

```
Reinforcement Learning
├─ 1. Core Concepts
│  ├─ Agent (learner)
│  ├─ Environment (world)
│  ├─ State (current situation)
│  ├─ Action (what agent can do)
│  ├─ Reward (feedback)
│  └─ Policy (strategy)
│
├─ 2. MDP (Markov Decision Process)
│  ├─ States S
│  ├─ Actions A
│  ├─ Transition probabilities P
│  ├─ Rewards R
│  └─ Discount factor γ
│
├─ 3. Algorithms
│  ├─ Value-based
│  │  ├─ Q-Learning
│  │  ├─ DQN (Deep Q-Network)
│  │  └─ Double DQN
│  ├─ Policy-based
│  │  ├─ Policy Gradient
│  │  ├─ REINFORCE
│  │  └─ Actor-Critic
│  └─ Model-based
│     ├─ Planning
│     └─ Monte Carlo Tree Search
│
├─ 4. Exploration vs Exploitation
│  ├─ ε-greedy
│  ├─ Softmax
│  └─ UCB (Upper Confidence Bound)
│
└─ 5. Applications
   ├─ Game playing
   ├─ Robotics
   ├─ Recommendation systems
   └─ Resource allocation
```

📌 **Key trade-off**: Exploration (try new things) vs Exploitation (use what works)

---

## 1️⃣3️⃣ Generative AI (6 questions)

**What they're really testing:**
Can you work with generative models?

**Mindmap**

```
Generative AI
├─ 1. Model Types
│  ├─ GANs (Generative Adversarial Networks)
│  │  ├─ Generator (creates fake data)
│  │  ├─ Discriminator (detects fake)
│  │  └─ Adversarial training
│  ├─ VAE (Variational Autoencoder)
│  │  ├─ Encoder (compress to latent)
│  │  ├─ Decoder (reconstruct)
│  │  └─ Probabilistic
│  ├─ Diffusion Models
│  │  ├─ Forward process (add noise)
│  │  ├─ Reverse process (denoise)
│  │  └─ Stable Diffusion, DALL-E
│  └─ Transformers (GPT, etc.)
│
├─ 2. Training
│  ├─ Loss functions
│  ├─ Mode collapse (GANs)
│  ├─ Convergence issues
│  └─ Regularization
│
├─ 3. Evaluation
│  ├─ Inception Score
│  ├─ FID (Fréchet Inception Distance)
│  ├─ Human evaluation
│  └─ Diversity metrics
│
└─ 4. Applications
   ├─ Image generation
   ├─ Text generation
   ├─ Audio synthesis
   └─ Video generation
```

📌 **Diffusion models > GANs** for image generation (more stable training)

---

## 1️⃣4️⃣ Natural Language Processing (5 questions)

**What they're really testing:**
Do you understand NLP techniques?

**Mindmap**

```
Natural Language Processing
├─ 1. Text Preprocessing
│  ├─ Tokenization
│  ├─ Lowercasing
│  ├─ Stop word removal
│  ├─ Stemming/Lemmatization
│  └─ Handling special characters
│
├─ 2. Text Representation
│  ├─ Bag of Words
│  ├─ TF-IDF
│  ├─ Word embeddings (Word2Vec, GloVe)
│  ├─ Contextual embeddings (BERT, GPT)
│  └─ Sentence embeddings
│
├─ 3. Common Tasks
│  ├─ Classification (sentiment, topic)
│  ├─ Named Entity Recognition (NER)
│  ├─ Question Answering
│  ├─ Machine Translation
│  └─ Text Summarization
│
├─ 4. Models
│  ├─ Traditional (Naive Bayes, SVM)
│  ├─ RNN/LSTM
│  ├─ Transformer (BERT, GPT)
│  └─ Fine-tuning pre-trained models
│
└─ 5. Evaluation
   ├─ Accuracy, F1
   ├─ BLEU (translation)
   ├─ ROUGE (summarization)
   └─ Perplexity (language modeling)
```

📌 **Start with pre-trained models**: BERT for understanding, GPT for generation

---

## 1️⃣5️⃣ SQL (4 questions)

**What they're really testing:**
Can you query and manipulate data?

**Mindmap**

```
SQL
├─ SELECT / WHERE
├─ JOIN (INNER, LEFT, RIGHT)
├─ GROUP BY / HAVING
├─ Aggregations (COUNT, SUM, AVG)
├─ Window functions
└─ CTEs (WITH clause)
```

📌 **For ML**: Use SQL to prepare training data

---

## 1️⃣6️⃣ Statistics & Probability (3 questions)

**What they're really testing:**
Do you have strong statistical foundations?

**Mindmap**

```
Statistics & Probability
├─ Distributions (Normal, Binomial, Poisson)
├─ Hypothesis testing
├─ P-value, confidence intervals
├─ Bayesian vs Frequentist
└─ Central Limit Theorem
```

📌 **Foundation for ML**: Understanding uncertainty and inference

---

## 1️⃣7️⃣ MLOps (2 questions)

**What they're really testing:**
Do you understand ML operations?

**Mindmap**

```
MLOps
├─ Experiment tracking (MLflow, Weights & Biases)
├─ Model versioning
├─ CI/CD for ML
├─ Feature store
└─ Model registry
```

📌 **Production ML = MLOps**

---

## 🎯 Study Strategy

### Week 1-2: ML Fundamentals (103 questions)
- Review algorithms, evaluation metrics
- Practice on Kaggle datasets
- Implement algorithms from scratch

### Week 3-4: DSA (39 questions)
- Daily LeetCode (Medium level)
- Focus on: Arrays, Trees, DP
- ML-specific problems (matrix operations)

### Week 5-6: ML System Design (11 questions)
- Practice designing: Recommendation, Search, Ranking systems
- Study: Feature stores, model serving, A/B testing
- Draw architecture diagrams

### Ongoing:
- Behavioral (STAR method)
- Deep Learning, Computer Vision, NLP
- Stay updated on LLMs and Generative AI

---

**See [`ML_Engineer_Question_Bank.md`](./ML_Engineer_Question_Bank.md) for all questions with frameworks.**
