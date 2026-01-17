# 🎯 Exponent Interview Prep Framework

**Multi-Role Interview Question Bank with Mental Model Frameworks**

A comprehensive collection of interview questions and systematic thinking frameworks for various tech roles, automatically extracted from Exponent.

---

## 📊 Repository Structure

This repo is organized by **role branches**:

```
main (master)
├── roles/
│   ├── data-analyst/      # Data Analyst questions & frameworks
│   ├── product-manager/   # Product Manager questions & frameworks
│   └── software-engineer/ # Software Engineer questions & frameworks
│
├── README.md              # This file
└── .gitignore
```

### Branch Strategy

- **`master`** - Main branch with overall documentation
- **`data-analyst`** - Complete Data Analyst prep (118 questions) ✅
- **`product-manager`** - Complete Product Manager prep (1,710 questions) ✅
- **`software-engineer`** - Complete Software Engineer prep (575 questions) ✅

---

## 🎓 Available Roles

### ✅ Data Analyst (Complete)
- **118 questions** across 20 categories
- Mental model frameworks for each category
- Source: https://www.tryexponent.com/questions?role=data-analyst

**View**: Switch to `data-analyst` branch or check `roles/data-analyst/`

### ✅ Product Manager (Complete)
- **1,710 questions** across 23 categories
- Mental model frameworks for PM-specific categories
- Source: https://www.tryexponent.com/questions?page=1&role=pm

**View**: Switch to `product-manager` branch or check `roles/product-manager/`

### ✅ Software Engineer (Complete)
- **575 questions** across 19 categories
- Mental model frameworks for SWE-specific categories
- Source: https://www.tryexponent.com/questions?page=1&role=swe

**View**: Switch to `software-engineer` branch or check `roles/software-engineer/`

---

## 🚀 Quick Start

### View Data Analyst Materials
```bash
git checkout data-analyst
cd roles/data-analyst
```

### View Product Manager Materials
```bash
git checkout product-manager
cd roles/product-manager
```

---

## 📁 Each Role Contains

```
roles/{role-name}/
├── data/
│   ├── questions_raw.json              # All extracted questions
│   ├── questions_categorized.json      # Questions with categories
│   ├── questions_by_category.json      # Organized by category
│   ├── frameworks_master.txt           # Complete framework (Notion import)
│   └── frameworks_master.md            # Rich formatted version (GitHub)
│
├── src/
│   ├── scrape_*.py                     # Web scraper
│   ├── categorize_questions.py         # Categorization logic
│   └── generate_frameworks.py          # Framework generator
│
└── INTERVIEW_FRAMEWORK.md              # Structured mindmaps
```

---

## 🎯 How to Use

1. **Choose your role** - Switch to the appropriate branch
2. **Review frameworks** - Study the mental models for each category
3. **Practice questions** - Use the categorized questions for practice
4. **Import to Notion** - Use `frameworks_master.txt` for Notion import

---

## 🔧 Technical Approach

### Web Scraping
- **Simple Python HTTP scraping** using `requests` + `BeautifulSoup`
- No browser automation needed (server-side rendered HTML)
- Handles pagination automatically
- Respectful rate limiting (1 second between requests)

### Categorization
- Intelligent keyword matching
- Context-aware category assignment
- Multiple categories per question when appropriate

### Framework Generation
- Mental model mindmaps for systematic thinking
- Focus on patterns, not memorization
- Practical tips for each category type

---

## 📊 Success Metrics

### Data Analyst (Completed)
- ✅ 118 questions extracted
- ✅ 20 active categories
- ✅ Mental model frameworks created
- ✅ Ready for Notion import

### Product Manager (In Progress)
- 🚧 Extracting questions
- 🚧 Categorizing by PM frameworks
- 🚧 Generating mental models

---

## 🌟 Key Features

- **No Answers** - Focus on frameworks and thinking patterns
- **Categorized** - Questions organized by interview type
- **Mental Models** - Systematic approaches for each category
- **Notion-Ready** - Easy import into your note-taking system
- **GitHub-Formatted** - Beautiful markdown rendering

---

## 🔮 Roadmap

- [x] Data Analyst role complete
- [ ] Product Manager role
- [ ] Software Engineer role
- [ ] Data Scientist role
- [ ] Engineering Manager role
- [ ] System Design role

---

## 📚 Resources

- **Source**: [Exponent.com](https://www.tryexponent.com/questions)
- **GitHub**: https://github.com/anix-lynch/Exponent

---

## ⚖️ License & Usage

This is for **personal interview preparation only**. Questions are sourced from Exponent's public question bank. Please support Exponent by signing up for their platform if you find this useful.

---

## 🙏 Credits

- **Tool**: Cursor AI + Claude Sonnet 4.5
- **Approach**: Simple Python web scraping (keeping it simple!)
- **First Major Success**: Data Analyst role extraction

---

**Built with 🚀 - One role at a time!**
