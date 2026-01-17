# 💻 Software Engineer Interview Preparation

Complete question bank and mental model frameworks for Software Engineer interviews, scraped from [Exponent](https://www.tryexponent.com/questions?page=1&role=swe).

---

## 📁 File Structure

```
software-engineer/
├── Software_Engineer_Question_Bank.md  ← 📚 All 575 questions (GitHub rich text)
├── INTERVIEW_FRAMEWORK.md              ← 🧠 Mental model frameworks
├── README.md                           ← 📖 This file
├── data/                               ← 💾 Supporting JSON files
│   ├── questions_raw.json              
│   ├── questions_categorized.json      
│   └── questions_by_category.json      
└── src/                                ← 🔧 Scraping scripts
    ├── scrape_swe.py                    
    └── categorize_questions.py         
```

---

## 🚀 Quick Start

### 1. **Study the Frameworks** 📖
Start with [`INTERVIEW_FRAMEWORK.md`](./INTERVIEW_FRAMEWORK.md) to understand the mental models for each category.

### 2. **Practice Questions** 💪
Use [`Software_Engineer_Question_Bank.md`](./Software_Engineer_Question_Bank.md) to practice questions by category.

### 3. **Apply the Framework** 🎯
For each question:
1. Identify the category
2. Apply that category's framework
3. Structure your answer

---

## 📊 Question Distribution

**Total: 575 questions across 19 categories**

| Category | Questions |
|----------|-----------|
| Problem Solving | 158 |
| Data Structures & Algorithms | 102 |
| Coding | 102 |
| System Design | 88 |
| Behavioral | 72 |
| Technical Communication | 29 |
| APIs | 25 |
| Project Management | 19 |
| Leadership | 16 |
| Databases | 12 |
| Testing | 11 |
| Object-Oriented Design | 10 |
| Distributed Systems | 9 |
| Code Review | 7 |
| Debugging | 6 |
| Concurrency | 5 |
| Security | 4 |
| Performance Optimization | 4 |
| Scalability | 2 |

---

## 🎯 How to Use in Interviews

When a question comes:

1. **Name the category silently** (e.g., "This is a System Design question")
2. **Apply that category's framework** (from INTERVIEW_FRAMEWORK.md)
3. **Speak in structured bullets** (Clarify → Plan → Implement → Test → Optimize)

---

## 🔄 Regenerating Data

If you want to re-scrape or update:

```bash
# Scrape fresh questions (takes ~1 minute for 30 pages)
python3 src/scrape_swe.py

# Categorize questions
python3 src/categorize_questions.py
```

---

## 📚 Resources

- **Source**: [Exponent SWE Questions](https://www.tryexponent.com/questions?page=1&role=swe)
- **GitHub Repo**: [Exponent Interview Prep](https://github.com/anix-lynch/Exponent)

---

## 💡 Philosophy

This resource focuses on **mental models and frameworks**, not memorizing answers. 

The goal is to develop a systematic approach to any SWE interview question by:
- Understanding the underlying pattern
- Applying a structured framework
- Communicating clearly and concisely

---

**Happy interviewing! 🚀**
