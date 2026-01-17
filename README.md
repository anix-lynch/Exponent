# 🎯 Exponent Data Analyst Interview Prep Framework

**First Major Web Scraping Success! 🚀**

A complete mental model framework for Data Analyst interviews with 118 real questions from Exponent, automatically extracted and categorized.

---

## 📊 What's Inside

- **118 Interview Questions** - All questions from Exponent's Data Analyst question bank
- **20 Categories** - Organized into key interview categories
- **Mental Model Frameworks** - Thinking frameworks for each category type
- **No Answers** - Focus on patterns and frameworks, not memorization

---

## 🎉 Project Success Story

### Challenge
Extract all Data Analyst interview questions from Exponent's paginated website (6 pages, 120 questions) and organize them by category with mental model frameworks.

### Solution
**Simple Python Web Scraping** (No browser automation needed!)
- Used `requests` + `BeautifulSoup` for HTTP scraping
- Handled pagination across 6 pages
- Intelligent categorization into 24 categories using keyword matching
- Generated mental model frameworks for each category

### Tools Used
- ✅ **Python** - `requests`, `BeautifulSoup`, `json`
- ✅ **Simple HTTP scraping** - No Selenium, Puppeteer, or browser automation
- ❌ **NOT used**: Cursor native browser, MCP servers (attempted but not needed)

### Why It Worked
The Exponent pages render server-side HTML, so simple HTTP requests were sufficient. No JavaScript rendering needed!

---

## 📁 Project Structure

```
.
├── data/
│   ├── questions_raw.json              # All 118 extracted questions
│   ├── questions_categorized.json      # Questions with categories
│   ├── questions_by_category.json      # Organized by category
│   └── frameworks_master.txt           # 🎯 MAIN OUTPUT - Mental models + all questions
│
├── src/
│   ├── simple_scraper.py              # Web scraper (requests + BeautifulSoup)
│   ├── categorize_questions.py        # Intelligent categorization
│   └── generate_frameworks.py         # Framework generator
│
└── README.md
```

---

## 📈 Results

### Questions by Category

```
Data Analysis........................  39 questions
Analytical...........................  39 questions
SQL..................................  24 questions
Coding...............................  20 questions
Product Strategy.....................  16 questions
Product Design.......................  16 questions
Artificial Intelligence..............  16 questions
Behavioral...........................  12 questions
Execution............................   8 questions
Cross-Functional.....................   8 questions
Project Management...................   7 questions
Customer Interaction.................   6 questions
Concept..............................   5 questions
Technical............................   4 questions
Statistics & Experimentation.........   4 questions
Estimation...........................   4 questions
Data Structures & Algorithms.........   3 questions
Data Modeling........................   2 questions
System Design........................   1 question
Data Pipeline Design.................   1 question
```

**Total: 118 questions across 20 categories**

---

## 🚀 How to Use

### 1. View the Complete Framework
Open `data/frameworks_master.txt` - this contains:
- Mental model frameworks for each category
- ALL 118 questions organized by category
- Ready to import into Notion

### 2. Run the Scraper (if you want fresh data)
```bash
cd src
python3 simple_scraper.py
```

### 3. Categorize Questions
```bash
python3 categorize_questions.py
```

### 4. Generate Frameworks
```bash
python3 generate_frameworks.py
```

---

## 💡 Mental Model Approach

Instead of memorizing answers, this framework teaches you **how to think** about each question type:

**Example: Data Analysis Framework**
```
Data Analysis
├─ Clarify the question
│  ├─ What metric/outcome?
│  ├─ Time period?
│  └─ Success criteria?
│
├─ Identify data sources
│  ├─ What tables/datasets?
│  ├─ Data quality check
│  └─ Missing data?
│
├─ Explore & segment
│  ├─ By time (trends)
│  ├─ By cohort (user groups)
│  └─ By dimension (geo, device, etc)
│
├─ Diagnose root cause
│  ├─ External factors
│  ├─ Internal changes
│  └─ User behavior shifts
│
└─ Recommend action
   ├─ What to do
   ├─ Expected impact
   └─ How to measure
```

---

## 🎓 Key Learnings

1. **Start Simple** - Tried MCP/browser automation first, but simple HTTP scraping worked better
2. **Server-side rendering** - Many modern sites still render HTML server-side
3. **Pattern recognition** - Categorization through keyword matching is surprisingly effective
4. **Focus on frameworks** - Mental models > memorized answers

---

## 🔧 Technical Notes

### Attempted Approaches
1. ❌ Cursor native browser agent - Configuration issues
2. ❌ MCP servers (Puppeteer, BrowserBase) - Overcomplicated
3. ✅ Simple Python HTTP scraping - **Winner!**

### Why Simple Won
- Exponent renders questions in server-side HTML
- No JavaScript required to access content
- Pagination is URL-based (`?page=1`, `?page=2`, etc.)
- Fast, reliable, no browser overhead

---

## 📝 Next Steps

- [ ] Add more question sources (LeetCode, Glassdoor, etc.)
- [ ] Create practice schedule generator
- [ ] Add company-specific question filters
- [ ] Build flashcard system from frameworks

---

## 🙏 Credits

- **Source**: [Exponent.com](https://www.tryexponent.com/questions?role=data-analyst)
- **Tool**: Cursor AI + Claude Sonnet 4.5
- **Approach**: Simple Python web scraping

---

## ⚖️ License & Usage

This is for **personal interview preparation only**. Questions are sourced from Exponent's public question bank. Please support Exponent by signing up for their platform if you find this useful.

---

**Built with 🚀 by learning to keep it simple!**
