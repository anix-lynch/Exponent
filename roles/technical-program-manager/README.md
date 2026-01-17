# 🎯 Technical Program Manager Interview Preparation

Complete question bank and mental model frameworks for Technical Program Manager interviews, scraped from [Exponent](https://www.tryexponent.com/questions?page=1&role=tpm).

---

## 📁 File Structure

```
technical-program-manager/
├── Technical_Program_Manager_Question_Bank.md  ← 📚 All 189 questions (GitHub rich text)
├── INTERVIEW_FRAMEWORK.md                      ← 🧠 Mental model frameworks
├── README.md                                   ← 📖 This file
├── data/                                       ← 💾 Supporting JSON files
│   ├── questions_raw.json              
│   ├── questions_categorized.json      
│   └── questions_by_category.json      
└── src/                                        ← 🔧 Scraping scripts
    ├── scrape_tpm.py                    
    └── categorize_questions.py         
```

---

## 🚀 Quick Start

### 1. **Study the Frameworks** 📖
Start with [`INTERVIEW_FRAMEWORK.md`](./INTERVIEW_FRAMEWORK.md) to understand the mental models for each category.

### 2. **Practice Questions** 💪
Use [`Technical_Program_Manager_Question_Bank.md`](./Technical_Program_Manager_Question_Bank.md) - includes ASCII tree frameworks + all questions for each category.

### 3. **Apply the Framework** 🎯
For each question:
1. Identify the category
2. Apply that category's framework
3. Structure your answer

---

## 📊 Question Distribution

**Total: 189 questions across 17 categories**

| Category | Questions |
|----------|-----------|
| Program Management | 75 |
| Behavioral | 54 |
| System Design | 38 |
| Team Leadership | 14 |
| Project Execution | 11 |
| Stakeholder Management | 8 |
| Technical Communication | 8 |
| Conflict Resolution | 8 |
| Metrics & KPIs | 7 |
| Process Improvement | 6 |
| Cross-Functional Leadership | 4 |
| Risk Management | 4 |
| Resource Planning | 4 |
| Prioritization | 4 |
| Roadmapping | 3 |
| Problem Solving | 3 |
| Agile/Scrum | 3 |

---

## 🎯 How to Use in Interviews

When a question comes:

1. **Name the category silently** (e.g., "This is a Program Management question")
2. **Apply that category's framework** (from INTERVIEW_FRAMEWORK.md)
3. **Speak in structured bullets** (Clarify → Plan → Execute → Measure → Scale)

---

## 🔄 Regenerating Data

If you want to re-scrape or update:

```bash
# Scrape fresh questions (takes ~30 seconds for 10 pages)
python3 src/scrape_tpm.py

# Categorize questions
python3 src/categorize_questions.py
```

---

## 📚 Resources

- **Source**: [Exponent TPM Questions](https://www.tryexponent.com/questions?page=1&role=tpm)
- **GitHub Repo**: [Exponent Interview Prep](https://github.com/anix-lynch/Exponent)

---

## 💡 Philosophy

This resource focuses on **mental models and frameworks**, not memorizing answers. 

The goal is to develop a systematic approach to any TPM interview question by:
- Understanding the underlying pattern
- Applying a structured framework
- Communicating clearly and concisely

---

**Happy interviewing! 🚀**
