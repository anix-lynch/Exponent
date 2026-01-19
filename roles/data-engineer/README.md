# 🎯 Data Engineer Interview Preparation

**YOUR #1 GOAL ROLE** - Complete question bank and comprehensive mental model frameworks for Data Engineer interviews, scraped from [Exponent](https://www.tryexponent.com/questions?page=1&role=data-engineer).

---

## 📁 File Structure

```
data-engineer/
├── Data_Engineer_Question_Bank.md     ← 📚 All 151 questions (GitHub rich text)
├── data_engineer_framework.md             ← 🧠 Mental model frameworks
├── README.md                          ← 📖 This file
├── data/                              ← 💾 Supporting JSON files
│   ├── questions_raw.json              
│   ├── questions_categorized.json      
│   └── questions_by_category.json      
└── src/                               ← 🔧 Scraping scripts
    ├── scrape_de.py                    
    └── categorize_questions.py         
```

---

## 🚀 Quick Start

### 1. **Study the Frameworks** 📖
Start with [`data_engineer_framework.md`](./data_engineer_framework.md) to understand the mental models.

### 2. **Practice Questions** 💪
Use [`Data_Engineer_Question_Bank.md`](./Data_Engineer_Question_Bank.md) - includes comprehensive ASCII tree frameworks + all questions for each category.

### 3. **Apply the Framework** 🎯
For each question:
1. Identify the category
2. Apply that category's framework
3. Structure your answer: Source → Ingest → Transform → Store → Serve → Monitor

---

## 📊 Question Distribution

**Total: 151 questions across 19 categories**

| Category | Questions | Priority |
|----------|-----------|----------|
| **Data Pipeline Design** | 76 | 🔥 CRITICAL |
| **Data Structures & Algorithms** | 32 | 🔥 HIGH |
| **System Design** | 20 | 🔥 HIGH |
| Data Modeling | 12 | Important |
| SQL | 12 | Important |
| Data Warehousing | 10 | Important |
| Behavioral | 5 | Important |
| ETL/ELT | 4 | Medium |
| Data Quality | 4 | Medium |
| Spark/Big Data | 4 | Medium |
| Cloud Platforms | 3 | Medium |
| Coding | 3 | Medium |
| Database Design | 3 | Medium |
| Others | 9 | Low |

---

## 🎯 How to Use in Interviews

When a question comes:

1. **Name the category silently** (e.g., "This is a Data Pipeline Design question")
2. **Apply that category's framework** (from Data_Engineer_Question_Bank.md)
3. **Speak in structured bullets** (Source → Ingest → Transform → Store → Serve)

---

## 🔄 Regenerating Data

If you want to re-scrape or update:

```bash
# Scrape fresh questions (takes ~30 seconds for 8 pages)
python3 src/scrape_de.py

# Categorize questions (comprehensive DE-specific categories)
python3 src/categorize_questions.py
```

---

## 📚 Resources

- **Source**: [Exponent DE Questions](https://www.tryexponent.com/questions?page=1&role=data-engineer)
- **GitHub Repo**: [Exponent Interview Prep](https://github.com/anix-lynch/Exponent)

---

## 💡 Philosophy

This resource focuses on **mental models and frameworks**, not memorizing answers. 

The goal is to develop a systematic approach to any DE interview question by:
- Understanding the underlying pattern
- Applying a structured framework
- Thinking about scale, performance, and data quality
- Communicating clearly and concisely

---

## 🎯 Your #1 Goal Role

This is your primary target role - master these patterns:
- **Data Pipeline Design** (76 questions) - Most important!
- **Data Structures & Algorithms** (32 questions) - Practice daily
- **System Design** (20 questions) - Think at scale

**You've got this! 🚀**
