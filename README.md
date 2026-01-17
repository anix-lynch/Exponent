# 🎯 Exponent Interview Prep Framework

**Multi-Role Interview Question Bank with Mental Model Frameworks**

A comprehensive collection of interview questions and systematic thinking frameworks for various tech roles, automatically extracted from Exponent.

---

## 📊 Repository Structure

This repo is organized by **role branches**:

```
main (master)
├── roles/
│   ├── bizops-strategy/              # BizOps & Strategy questions & frameworks
│   ├── chief-of-staff/               # Chief of Staff questions & frameworks
│   ├── data-analyst/                 # Data Analyst questions & frameworks
│   ├── data-engineer/                # Data Engineer questions & frameworks 🎯 #1 GOAL
│   ├── finance-strategy/             # Finance & Strategy questions & frameworks
│   ├── growth-marketing-manager/     # Growth Marketing Manager questions & frameworks
│   ├── ml-engineer/                  # ML Engineer questions & frameworks
│   ├── product-manager/              # Product Manager questions & frameworks
│   ├── product-marketing-manager/    # Product Marketing Manager questions & frameworks
│   ├── program-manager/              # Program Manager questions & frameworks
│   ├── software-engineer/            # Software Engineer questions & frameworks
│   └── technical-program-manager/    # Technical Program Manager questions & frameworks
│
├── README.md                         # This file
└── .gitignore
```

### Branch Strategy

- **`master`** - Main branch with overall documentation
- **`data-analyst`** - Complete Data Analyst prep (118 questions) ✅
- **`data-engineer`** - Complete Data Engineer prep (151 questions) ✅ 🎯 **#1 GOAL ROLE**
- **`product-manager`** - Complete Product Manager prep (1,710 questions) ✅
- **`software-engineer`** - Complete Software Engineer prep (575 questions) ✅
- **`technical-program-manager`** - Complete TPM prep (189 questions) ✅

---

## 🎓 Available Roles

### ✅ Data Analyst (Complete)
- **118 questions** across 20 categories
- Mental model frameworks for each category
- Source: https://www.tryexponent.com/questions?role=data-analyst

**View**: Switch to `data-analyst` branch or check `roles/data-analyst/`

### ✅ 🎯 Data Engineer (Complete) - **YOUR #1 GOAL ROLE**
- **151 questions** across 19 categories
- **Comprehensive frameworks** with extra detail for your primary target
- **Priority levels**: Critical (76 pipeline), High (52 algo/system), Important (34)
- Source: https://www.tryexponent.com/questions?page=1&role=data-engineer

**View**: Switch to `data-engineer` branch or check `roles/data-engineer/`

**🔥 Focus Areas**:
- Data Pipeline Design (76 questions) - CRITICAL
- Data Structures & Algorithms (32 questions) - HIGH  
- System Design (20 questions) - HIGH

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

### ✅ Technical Program Manager (Complete)
- **189 questions** across 17 categories
- Mental model frameworks for TPM-specific categories
- Source: https://www.tryexponent.com/questions?page=1&role=tpm

**View**: Switch to `technical-program-manager` branch or check `roles/technical-program-manager/`

### ✅ Machine Learning Engineer (Complete)
- **137 questions** across 15 categories
- Mental model frameworks for ML-specific categories
- Source: https://www.tryexponent.com/questions?page=1&role=ml-engineer

**View**: Check `roles/ml-engineer/`

### ✅ BizOps & Strategy (Complete)
- **97 questions** across 14 categories
- Mental model frameworks for BizOps-specific categories
- Source: https://www.tryexponent.com/questions?page=1&role=bizops

**View**: Check `roles/bizops-strategy/`

### ✅ Program Manager (Complete)
- **11 questions** across 4 categories
- Mental model frameworks for Program Management
- Source: https://www.tryexponent.com/questions?page=1&role=program-manager

**View**: Check `roles/program-manager/`

### ✅ Finance & Strategy (Complete)
- **7 questions** across 6 categories
- Mental model frameworks for Finance & Strategy
- Source: https://www.tryexponent.com/questions?role=finance-strategy

**View**: Check `roles/finance-strategy/`

### ✅ Chief of Staff (Complete)
- **2 questions** across 3 categories
- Mental model frameworks for Chief of Staff
- Source: https://www.tryexponent.com/questions?page=1&role=chief-of-staff

**View**: Check `roles/chief-of-staff/`

### ✅ Growth Marketing Manager (Complete)
- **2 questions** across 1 category
- Mental model frameworks for Growth Marketing
- Source: https://www.tryexponent.com/questions?role=growth-marketing-manager

**View**: Check `roles/growth-marketing-manager/`

### ✅ Product Marketing Manager (Complete)
- **5 questions** (sample) across 5 categories
- Mental model frameworks for Product Marketing
- Source: https://www.tryexponent.com/questions?role=pmm

**View**: Check `roles/product-marketing-manager/`

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

- [x] Data Analyst role complete (118 questions)
- [x] Product Manager role complete (1,710 questions)
- [x] Software Engineer role complete (575 questions)
- [x] Technical Program Manager role complete (189 questions)
- [x] Data Engineer role complete (151 questions) 🎯 **#1 GOAL**
- [x] Machine Learning Engineer role complete (137 questions)
- [x] BizOps & Strategy role complete (97 questions)
- [x] Program Manager role complete (11 questions)
- [x] Finance & Strategy role complete (7 questions)
- [x] Chief of Staff role complete (2 questions)
- [x] Growth Marketing Manager role complete (2 questions)
- [x] Product Marketing Manager role complete (5 questions sample)
- [ ] Data Scientist role
- [ ] Engineering Manager role

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
