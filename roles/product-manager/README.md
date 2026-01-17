# 🎯 Product Manager Interview Preparation

Complete question bank and mental model frameworks for Product Manager interviews, scraped from [Exponent](https://www.tryexponent.com/questions?page=1&role=pm).

---

## 📁 File Structure

```
product-manager/
├── Product_Manager_Question_Bank.md    ← 📚 All 1,710 questions (GitHub rich text)
├── INTERVIEW_FRAMEWORK.md              ← 🧠 Mental model frameworks
├── README.md                           ← 📖 This file
├── data/                               ← 💾 Supporting JSON files
│   ├── questions_raw.json              
│   ├── questions_categorized.json      
│   └── questions_by_category.json      
└── src/                                ← 🔧 Scraping scripts
    ├── scrape_pm.py                    
    ├── categorize_questions.py         
    └── generate_frameworks.py          
```

---

## 🚀 Quick Start

### 1. **Study the Frameworks** 📖
Start with [`INTERVIEW_FRAMEWORK.md`](./INTERVIEW_FRAMEWORK.md) to understand the mental models for each category.

### 2. **Practice Questions** 💪
Use [`Product_Manager_Question_Bank.md`](./Product_Manager_Question_Bank.md) to practice questions by category.

### 3. **Apply the Framework** 🎯
For each question:
1. Identify the category
2. Apply that category's framework
3. Structure your answer

---

## 📊 Question Distribution

**Total: 1,710 questions across 23 categories**

| Category | Questions |
|----------|-----------|
| Analytical | 598 |
| Product Design | 524 |
| Product Strategy | 134 |
| Metrics | 128 |
| Behavioral | 117 |
| Estimation | 82 |
| Execution | 77 |
| Leadership | 64 |
| Technical | 61 |
| Concept | 61 |
| Prioritization | 53 |
| Growth | 50 |
| Communication | 35 |
| Pricing | 27 |
| Roadmapping | 26 |
| Stakeholder Management | 26 |
| Product Sense | 17 |
| A/B Testing | 15 |
| System Design | 11 |
| Go-to-Market | 8 |
| Trade-offs | 8 |
| User Research | 4 |
| Root Cause Analysis | 1 |

---

## 🎯 How to Use in Interviews

When a question comes:

1. **Name the category silently** (e.g., "This is a Product Design question")
2. **Apply that category's framework** (from INTERVIEW_FRAMEWORK.md)
3. **Speak in structured bullets** (Clarify → Break down → Analyze → Decide → Impact)

---

## 🔄 Regenerating Data

If you want to re-scrape or update:

```bash
# Scrape fresh questions (takes ~2 minutes for 86 pages)
python3 src/scrape_pm.py

# Categorize questions
python3 src/categorize_questions.py

# Generate frameworks
python3 src/generate_frameworks.py
```

---

## 📚 Resources

- **Source**: [Exponent PM Questions](https://www.tryexponent.com/questions?page=1&role=pm)
- **GitHub Repo**: [Exponent Interview Prep](https://github.com/anix-lynch/Exponent)

---

## 💡 Philosophy

This resource focuses on **mental models and frameworks**, not memorizing answers. 

The goal is to develop a systematic approach to any PM interview question by:
- Understanding the underlying pattern
- Applying a structured framework
- Communicating clearly and concisely

---

**Happy interviewing! 🚀**
