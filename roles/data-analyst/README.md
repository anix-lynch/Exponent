# 🎯 Data Analyst Interview Preparation

Complete question bank and mental model frameworks for Data Analyst interviews, scraped from [Exponent](https://www.tryexponent.com/questions?role=data-analyst&src=nav).

---

## 📁 File Structure

```
data-analyst/
├── Data_Analyst_Question_Bank.md      ← 📚 All 118 questions (GitHub rich text)
├── INTERVIEW_FRAMEWORK.md             ← 🧠 Mental model frameworks
├── README.md                          ← 📖 This file
├── data/                              ← 💾 Supporting JSON files
│   ├── questions_raw.json              
│   ├── questions_categorized.json      
│   ├── questions_by_category.json
│   ├── frameworks_master.txt
│   └── frameworks_master.md
└── src/                               ← 🔧 Scraping scripts
    ├── simple_scraper.py                    
    ├── categorize_questions.py         
    └── generate_frameworks.py          
```

---

## 🚀 Quick Start

### 1. **Study the Frameworks** 📖
Start with [`INTERVIEW_FRAMEWORK.md`](./INTERVIEW_FRAMEWORK.md) to understand the mental models for each category.

### 2. **Practice Questions** 💪
Use [`Data_Analyst_Question_Bank.md`](./Data_Analyst_Question_Bank.md) to practice questions by category.

### 3. **Apply the Framework** 🎯
For each question:
1. Identify the category
2. Apply that category's framework
3. Structure your answer

---

## 📊 Question Distribution

**Total: 118 questions across 20 categories**

| Category | Questions |
|----------|-----------|
| Data Analysis | 39 |
| Analytical | 39 |
| SQL | 24 |
| Coding | 20 |
| Product Strategy | 16 |
| Product Design | 16 |
| Artificial Intelligence | 16 |
| Behavioral | 12 |
| Execution | 8 |
| Cross-Functional | 8 |
| Project Management | 7 |
| Customer Interaction | 6 |
| Concept | 5 |
| Technical | 4 |
| Statistics & Experimentation | 4 |
| Estimation | 4 |
| Data Structures & Algorithms | 3 |
| Data Modeling | 2 |
| System Design | 1 |
| Data Pipeline Design | 1 |

---

## 🎯 How to Use in Interviews

When a question comes:

1. **Name the category silently** (e.g., "This is a Data Analysis question")
2. **Apply that category's framework** (from INTERVIEW_FRAMEWORK.md)
3. **Speak in structured bullets** (Clarify → Break down → Analyze → Decide → Impact)

---

## 🔄 Regenerating Data

If you want to re-scrape or update:

```bash
# Scrape fresh questions (takes ~30 seconds for 6 pages)
python3 src/simple_scraper.py

# Categorize questions
python3 src/categorize_questions.py

# Generate frameworks
python3 src/generate_frameworks.py
```

---

## 📚 Resources

- **Source**: [Exponent DA Questions](https://www.tryexponent.com/questions?role=data-analyst&src=nav)
- **GitHub Repo**: [Exponent Interview Prep](https://github.com/anix-lynch/Exponent_DataAnalyst_interview)

---

## 💡 Philosophy

This resource focuses on **mental models and frameworks**, not memorizing answers. 

The goal is to develop a systematic approach to any DA interview question by:
- Understanding the underlying pattern
- Applying a structured framework
- Communicating clearly and concisely

---

**Happy interviewing! 🚀**
