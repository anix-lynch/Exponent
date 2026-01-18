"""
Generate comprehensive Product Analyst frameworks matching Data Analyst quality
"""
import json
import os

def get_framework_for_category(category):
    """Return comprehensive ASCII framework for each PA category"""
    
    frameworks = {
        "Behavioral": """
Behavioral (STAR Method)
├─ Situation
│  ├─ Product context and background
│  ├─ Team and stakeholders involved
│  ├─ Product metrics at the time
│  └─ Why this was important
│
├─ Task
│  ├─ Your specific responsibility
│  ├─ Product goals and objectives
│  ├─ Constraints (time, resources, data)
│  └─ Success criteria
│
├─ Action
│  ├─ Analysis approach
│  ├─ Tools and methods used
│  ├─ How you collaborated with PM/Eng
│  ├─ Challenges you overcame
│  └─ Iterations and refinements
│
└─ Result
   ├─ Quantifiable product outcomes
   ├─ Impact on users and business
   ├─ Stakeholder feedback
   ├─ What you learned
   └─ How you'd apply it again
""",
        "Product Metrics & KPIs": """
Product Metrics & KPIs
├─ Understand the product
│  ├─ Product vision and goals
│  ├─ User journey and lifecycle
│  ├─ Key value propositions
│  ├─ Competitive landscape
│  └─ Business model
│
├─ Define metrics framework
│  ├─ North Star Metric (primary success indicator)
│  ├─ Acquisition metrics (signups, installs, traffic)
│  ├─ Activation metrics (onboarding completion, first action)
│  ├─ Engagement metrics (DAU, MAU, session length, frequency)
│  ├─ Retention metrics (D1, D7, D30 retention, churn)
│  ├─ Revenue metrics (ARPU, LTV, conversion rate)
│  └─ Referral metrics (viral coefficient, NPS)
│
├─ Ensure quality
│  ├─ Aligned with product goals
│  ├─ Actionable (can influence)
│  ├─ Measurable and trackable
│  ├─ Leading vs lagging indicators
│  └─ Guardrail metrics (prevent negative impacts)
│
├─ Track and analyze
│  ├─ Set up tracking and instrumentation
│  ├─ Build dashboards
│  ├─ Monitor trends over time
│  ├─ Segment by user cohorts
│  └─ Benchmark against targets
│
└─ Drive product decisions
   ├─ Identify opportunities
   ├─ Prioritize features
   ├─ Measure experiment impact
   ├─ Inform roadmap
   └─ Communicate to stakeholders
""",
        "Product Analysis - Root Cause": """
Product Analysis - Root Cause
├─ Define the problem
│  ├─ What metric changed? (engagement, conversion, retention)
│  ├─ When did it change? (date, time, event)
│  ├─ How much did it change? (magnitude, percentage)
│  ├─ Why does it matter? (user impact, business impact)
│  └─ What's the baseline?
│
├─ Form hypotheses
│  ├─ Product changes (new feature, UI change, bug)
│  ├─ Technical issues (performance, crashes, errors)
│  ├─ User behavior changes (new cohorts, usage patterns)
│  ├─ External factors (seasonality, competition, market)
│  ├─ Data quality issues (tracking, instrumentation)
│  └─ Prioritize hypotheses
│
├─ Segment and drill down
│  ├─ By time (hourly, daily, weekly)
│  ├─ By user segment (new vs returning, demographics)
│  ├─ By platform (web, iOS, Android)
│  ├─ By feature or flow
│  ├─ By geography or locale
│  └─ By cohort or acquisition channel
│
├─ Test hypotheses
│  ├─ Gather supporting data
│  ├─ Look for correlations
│  ├─ Check logs and events
│  ├─ Validate with qualitative data (user feedback)
│  └─ Identify root cause
│
└─ Recommend solution
   ├─ Fix the immediate issue
   ├─ Prevent recurrence
   ├─ Monitor going forward
   ├─ Expected impact
   └─ Implementation timeline
""",
        "Product Analysis - Feature Impact": """
Product Analysis - Feature Impact
├─ Understand the feature
│  ├─ What problem does it solve?
│  ├─ Who is the target user?
│  ├─ How does it work?
│  ├─ When was it launched?
│  └─ What were the goals?
│
├─ Define success metrics
│  ├─ Primary metrics (feature adoption, usage)
│  ├─ Secondary metrics (engagement, retention)
│  ├─ Business metrics (revenue, conversion)
│  ├─ User satisfaction (NPS, feedback)
│  └─ Guardrail metrics (negative impacts)
│
├─ Analyze adoption
│  ├─ What % of users discovered the feature?
│  ├─ What % of users tried it?
│  ├─ What % of users use it regularly?
│  ├─ Adoption curve over time
│  └─ Compare to expectations
│
├─ Analyze impact
│  ├─ Did it improve target metrics?
│  ├─ Segment by user type (power users, new users)
│  ├─ Compare users who use it vs don't
│  ├─ Look for unintended consequences
│  └─ Qualitative feedback
│
└─ Recommend next steps
   ├─ Should we invest more? (iterate, expand)
   ├─ Should we optimize? (improve adoption, UX)
   ├─ Should we sunset? (low value, high cost)
   ├─ What did we learn?
   └─ Apply learnings to future features
""",
        "Product Analysis - User Behavior": """
Product Analysis - User Behavior
├─ Define the question
│  ├─ What user behavior are we analyzing?
│  ├─ Why does it matter?
│  ├─ What decisions will this inform?
│  └─ What's the scope? (segment, timeframe)
│
├─ Map the user journey
│  ├─ Key touchpoints and actions
│  ├─ Entry points
│  ├─ Critical paths
│  ├─ Exit points
│  └─ Conversion funnels
│
├─ Analyze patterns
│  ├─ Frequency (how often do users engage?)
│  ├─ Recency (when was last engagement?)
│  ├─ Depth (how deeply do they engage?)
│  ├─ Breadth (what features do they use?)
│  ├─ Sequences (what paths do they take?)
│  └─ Cohort analysis (how do cohorts differ?)
│
├─ Segment users
│  ├─ Power users vs casual users
│  ├─ New users vs returning users
│  ├─ By demographics (age, location)
│  ├─ By acquisition channel
│  ├─ By product usage patterns
│  └─ Identify key segments
│
└─ Generate insights
   ├─ What drives engagement?
   ├─ What causes drop-off?
   ├─ What predicts retention?
   ├─ What opportunities exist?
   └─ Recommend product improvements
""",
        "Product Analysis - Funnel Analysis": """
Product Analysis - Funnel Analysis
├─ Define the funnel
│  ├─ What's the goal? (signup, purchase, activation)
│  ├─ What are the steps?
│  ├─ Entry point
│  ├─ Critical milestones
│  └─ Success event
│
├─ Measure conversion
│  ├─ Overall conversion rate
│  ├─ Step-by-step conversion
│  ├─ Drop-off at each step
│  ├─ Time to convert
│  └─ Benchmark against targets
│
├─ Segment the funnel
│  ├─ By user type (new vs returning)
│  ├─ By platform (web, iOS, Android)
│  ├─ By acquisition channel
│  ├─ By geography or locale
│  ├─ By cohort
│  └─ Identify high/low performing segments
│
├─ Identify bottlenecks
│  ├─ Which step has highest drop-off?
│  ├─ Why are users dropping off? (UX, friction, confusion)
│  ├─ What's different about users who convert?
│  ├─ Are there technical issues?
│  └─ Qualitative feedback
│
└─ Optimize the funnel
   ├─ Prioritize steps to improve
   ├─ Hypothesis for improvement
   ├─ Design experiment
   ├─ Expected impact
   └─ Monitor and iterate
""",
        "A/B Testing & Experimentation": """
A/B Testing & Experimentation
├─ Define the experiment
│  ├─ What's the hypothesis?
│  ├─ What are we testing? (feature, design, copy)
│  ├─ What's the control vs treatment?
│  ├─ What's the expected impact?
│  └─ Why does this matter?
│
├─ Choose metrics
│  ├─ Primary metric (what we're optimizing for)
│  ├─ Secondary metrics (additional signals)
│  ├─ Guardrail metrics (prevent negative impacts)
│  ├─ Leading indicators (early signals)
│  └─ Ensure metrics are measurable
│
├─ Design the experiment
│  ├─ Randomization unit (user, session, device)
│  ├─ Sample size calculation (power analysis)
│  ├─ Traffic allocation (50/50, 90/10)
│  ├─ Duration (how long to run?)
│  ├─ Exclusions (bots, internal users)
│  └─ Instrumentation and tracking
│
├─ Analyze results
│  ├─ Check for statistical significance (p-value < 0.05)
│  ├─ Calculate effect size (% lift)
│  ├─ Check secondary and guardrail metrics
│  ├─ Segment analysis (did it work for all users?)
│  ├─ Novelty effect (did effect decay over time?)
│  └─ Validate data quality
│
└─ Make decision
   ├─ Ship (clear win)
   ├─ Don't ship (no impact or negative)
   ├─ Iterate (promising but needs work)
   ├─ Run longer (inconclusive)
   └─ Document learnings
""",
        "SQL - Product Analytics": """
SQL - Product Analytics
├─ Understand the question
│  ├─ What product question are we answering?
│  ├─ What tables are involved? (events, users, sessions)
│  ├─ What's the grain of the output?
│  └─ What time period?
│
├─ Plan the query
│  ├─ Identify event tables (user actions, page views)
│  ├─ Identify dimension tables (users, products)
│  ├─ Join conditions
│  ├─ Filter criteria (WHERE)
│  ├─ Aggregation level (GROUP BY)
│  └─ Window functions if needed
│
├─ Write the query
│  ├─ SELECT metrics (COUNT, COUNT DISTINCT, AVG, SUM)
│  ├─ FROM event table
│  ├─ JOIN user/product tables
│  ├─ WHERE to filter (date range, user segment, event type)
│  ├─ GROUP BY dimensions (date, user_id, product)
│  ├─ HAVING to filter groups
│  └─ ORDER BY and LIMIT
│
├─ Handle product-specific patterns
│  ├─ Funnels (sequential events)
│  ├─ Retention (users who return)
│  ├─ Cohorts (group by signup date)
│  ├─ DAU/MAU (active users)
│  ├─ Session analysis (sessionization)
│  └─ Feature adoption (first use, regular use)
│
└─ Validate
   ├─ Check for nulls and duplicates
   ├─ Verify row counts
   ├─ Spot check results
   ├─ Test edge cases
   └─ Document assumptions
""",
        "SQL - Cohort & Retention": """
SQL - Cohort & Retention
├─ Define cohorts
│  ├─ Cohort criteria (signup date, first purchase, first action)
│  ├─ Time period (daily, weekly, monthly)
│  ├─ Cohort size and distribution
│  └─ Relevant segments
│
├─ Define retention
│  ├─ What action defines "retained"? (login, purchase, engagement)
│  ├─ Time windows (D1, D7, D30, M1, M3, M6)
│  ├─ Rolling vs calendar retention
│  └─ Classic vs unbounded retention
│
├─ Write the query
│  ├─ CTE 1: Define cohorts (first action date)
│  ├─ CTE 2: Get all user activity
│  ├─ CTE 3: Calculate time since cohort start
│  ├─ CTE 4: Aggregate retention by cohort and period
│  ├─ Use window functions for running calculations
│  └─ Format output (cohort, period, retention %)
│
├─ Analyze patterns
│  ├─ Retention curves by cohort
│  ├─ Compare cohorts over time
│  ├─ Identify improving/declining cohorts
│  ├─ Look for seasonality
│  └─ Benchmark against targets
│
└─ Generate insights
   ├─ What's driving retention changes?
   ├─ Which cohorts are healthiest?
   ├─ When do users churn?
   ├─ What can we do to improve retention?
   └─ Forecast future retention
""",
        "Product Strategy": """
Product Strategy
├─ Understand the context
│  ├─ Product vision and mission
│  ├─ Target market and users
│  ├─ Competitive landscape
│  ├─ Market trends
│  └─ Business goals
│
├─ Analyze the opportunity
│  ├─ Market size and growth (TAM, SAM, SOM)
│  ├─ User needs and pain points
│  ├─ Competitive gaps
│  ├─ Technology trends
│  └─ Regulatory environment
│
├─ Define product strategy
│  ├─ Target user segments
│  ├─ Value proposition
│  ├─ Differentiation
│  ├─ Product positioning
│  └─ Success metrics
│
├─ Evaluate options
│  ├─ New features vs new products
│  ├─ Market expansion (new segments, geographies)
│  ├─ Platform vs point solution
│  ├─ Build vs buy vs partner
│  └─ Prioritization (impact, effort, risk)
│
└─ Recommend roadmap
   ├─ Short-term (0-6 months)
   ├─ Medium-term (6-12 months)
   ├─ Long-term (12+ months)
   ├─ Key milestones and metrics
   └─ Resource requirements
""",
        "Product Sense": """
Product Sense
├─ Understand the problem
│  ├─ Who is the user?
│  ├─ What problem are they facing?
│  ├─ Why does this problem matter?
│  ├─ How do they solve it today?
│  └─ What's the opportunity size?
│
├─ Define the solution
│  ├─ What's the core value proposition?
│  ├─ What are the key features?
│  ├─ How does it work? (user flow)
│  ├─ What makes it better than alternatives?
│  └─ What are the constraints?
│
├─ Prioritize features
│  ├─ Must-haves (MVP)
│  ├─ Should-haves (V2)
│  ├─ Nice-to-haves (future)
│  ├─ Impact vs effort
│  └─ User value vs business value
│
├─ Define success
│  ├─ User success (adoption, engagement, satisfaction)
│  ├─ Business success (revenue, growth, efficiency)
│  ├─ Key metrics to track
│  ├─ Short-term vs long-term goals
│  └─ How to measure
│
└─ Consider trade-offs
   ├─ Simplicity vs functionality
   ├─ Speed vs quality
   ├─ User value vs business value
   ├─ Short-term vs long-term
   └─ Build vs buy
""",
        "Data Visualization & Dashboards": """
Data Visualization & Dashboards
├─ Understand the purpose
│  ├─ Who is the audience? (PM, exec, eng, ops)
│  ├─ What decisions will they make?
│  ├─ What questions are they asking?
│  ├─ How often will they use it?
│  └─ What's the key message?
│
├─ Choose the right charts
│  ├─ Trends over time: Line chart, area chart
│  ├─ Comparison: Bar chart, column chart
│  ├─ Distribution: Histogram, box plot
│  ├─ Relationship: Scatter plot
│  ├─ Composition: Pie chart, stacked bar, treemap
│  ├─ Funnel: Funnel chart
│  └─ Cohort: Cohort retention table
│
├─ Design effectively
│  ├─ Clear and descriptive titles
│  ├─ Labeled axes with units
│  ├─ Appropriate scale
│  ├─ Minimal colors (use for emphasis)
│  ├─ Remove clutter (gridlines, borders)
│  ├─ Consistent formatting
│  └─ Mobile-friendly if needed
│
├─ Build the dashboard
│  ├─ Organize logically (most important first)
│  ├─ Use filters (date range, segment, platform)
│  ├─ Add interactivity (drill-down, hover)
│  ├─ Balance detail and overview
│  ├─ Set refresh frequency
│  └─ Optimize for performance
│
└─ Maintain and iterate
   ├─ Monitor usage (who's using it?)
   ├─ Gather feedback
   ├─ Update as product evolves
   ├─ Deprecate unused charts
   └─ Document definitions and calculations
""",
        "Estimation & Market Sizing": """
Estimation & Market Sizing
├─ Clarify the question
│  ├─ What exactly are we estimating?
│  ├─ Geography (country, region, world)
│  ├─ Time period (annual, monthly, daily)
│  ├─ Units (users, revenue, transactions)
│  └─ Precision needed
│
├─ Choose approach
│  ├─ Top-down (total market → segments)
│  ├─ Bottom-up (unit economics → total)
│  ├─ Proxy/analogy (similar products)
│  └─ Combination
│
├─ Make assumptions
│  ├─ State assumptions clearly
│  ├─ Use round numbers
│  ├─ Base on known facts when possible
│  ├─ Be reasonable and logical
│  └─ Document key assumptions
│
├─ Calculate step by step
│  ├─ Break into components
│  ├─ Calculate each piece
│  ├─ Show your work
│  ├─ Use simple math
│  └─ Sanity check along the way
│
└─ Validate and refine
   ├─ Does the answer make sense?
   ├─ Compare to known benchmarks
   ├─ Sensitivity analysis (key assumptions)
   ├─ Discuss limitations
   └─ Provide range if appropriate
""",
        "Communication & Stakeholder Management": """
Communication & Stakeholder Management
├─ Know your audience
│  ├─ Who are they? (PM, eng, exec, design)
│  ├─ What do they care about?
│  ├─ What's their level of technical knowledge?
│  ├─ What decision do they need to make?
│  └─ How much time do you have?
│
├─ Structure your message
│  ├─ Start with the conclusion (TL;DR)
│  ├─ Provide context and problem statement
│  ├─ Present analysis and insights
│  ├─ Make clear recommendations
│  └─ End with next steps
│
├─ Tell a story with data
│  ├─ Set the scene (context)
│  ├─ Introduce the problem
│  ├─ Show the evidence (data)
│  ├─ Explain the insights
│  └─ Recommend the solution
│
├─ Visualize effectively
│  ├─ Choose right chart type
│  ├─ Keep it simple and focused
│  ├─ Use clear labels and titles
│  ├─ Highlight key insights
│  └─ Remove clutter
│
└─ Engage and respond
   ├─ Anticipate questions
   ├─ Listen actively
   ├─ Clarify when needed
   ├─ Acknowledge concerns
   └─ Follow up on action items
""",
        "Prioritization": """
Prioritization
├─ Understand the context
│  ├─ Product goals and strategy
│  ├─ Available resources (eng, design, time)
│  ├─ Constraints and dependencies
│  ├─ Stakeholder needs
│  └─ Timeline and urgency
│
├─ Define criteria
│  ├─ User impact (adoption, engagement, satisfaction)
│  ├─ Business impact (revenue, growth, efficiency)
│  ├─ Strategic alignment
│  ├─ Effort required (eng, design, PM)
│  ├─ Risk and uncertainty
│  └─ Dependencies
│
├─ Evaluate options
│  ├─ Score each option on criteria
│  ├─ Impact vs Effort matrix (RICE, ICE)
│  ├─ User value vs business value
│  ├─ Risk assessment
│  └─ Consider trade-offs
│
├─ Prioritize
│  ├─ High impact, low effort (do first)
│  ├─ High impact, high effort (plan carefully)
│  ├─ Low impact, low effort (quick wins)
│  ├─ Low impact, high effort (deprioritize)
│  └─ Must-haves vs nice-to-haves
│
└─ Communicate and align
   ├─ Share prioritization rationale
   ├─ Get stakeholder buy-in
   ├─ Document decisions
   ├─ Set expectations
   └─ Revisit regularly
""",
        "Technical Concepts": """
Technical Concepts (for Product Analysts)
├─ Data infrastructure
│  ├─ Data warehouse (Snowflake, BigQuery, Redshift)
│  ├─ Data lake (S3, HDFS)
│  ├─ ETL/ELT pipelines
│  ├─ Event tracking (Segment, Amplitude, Mixpanel)
│  └─ Data quality and governance
│
├─ Analytics tools
│  ├─ SQL (querying and analysis)
│  ├─ BI tools (Tableau, Looker, Mode)
│  ├─ Python/R (advanced analysis)
│  ├─ Excel/Sheets (quick analysis)
│  └─ Product analytics (Amplitude, Mixpanel, Heap)
│
├─ Product instrumentation
│  ├─ Event tracking (what to track)
│  ├─ Event schema (properties, naming)
│  ├─ User identification (user_id, device_id)
│  ├─ Session tracking
│  └─ Data validation
│
├─ Statistical concepts
│  ├─ Descriptive statistics (mean, median, mode, std dev)
│  ├─ Hypothesis testing (t-test, chi-square)
│  ├─ Statistical significance (p-value, confidence intervals)
│  ├─ Correlation vs causation
│  └─ Regression analysis
│
└─ Product development
   ├─ Agile/Scrum methodology
   ├─ Product lifecycle (ideation → launch → growth → maturity)
   ├─ Feature flags and rollouts
   ├─ A/B testing infrastructure
   └─ Product roadmap and planning
"""
    }
    
    return frameworks.get(category, "")

def main():
    """Generate comprehensive frameworks"""
    
    # Load data
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    with open(os.path.join(data_dir, 'questions_by_category.json'), 'r') as f:
        by_category = json.load(f)
    
    # Count totals
    total_questions = sum(len(qs) for qs in by_category.values())
    category_counts = [(cat, len(by_category[cat])) for cat in by_category.keys()]
    category_counts.sort(key=lambda x: x[1], reverse=True)
    
    print(f"🚀 Generating comprehensive Product Analyst frameworks...")
    print(f"   Total questions: {total_questions}")
    print(f"   Categories: {len([c for c in category_counts if c[1] > 0])}")
    
    # Generate Question Bank (matching Data Analyst format)
    qb_md = """
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║           PRODUCT ANALYST INTERVIEW PREPARATION FRAMEWORK                      ║
║           Mental Models & Complete Question Bank                               ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

This framework provides mental models for approaching each type of product analyst
interview question. Focus on understanding the PATTERN and FRAMEWORK, not 
memorizing answers.

Total Questions: {} across {} categories


""".format(total_questions, len([c for c in category_counts if c[1] > 0]))
    
    # Add each category with framework
    for cat, count in category_counts:
        if count == 0:
            continue
        
        questions = by_category[cat]
        
        qb_md += "=" * 80 + "\n"
        qb_md += f"{cat.upper()}\n"
        qb_md += "=" * 80 + "\n\n"
        qb_md += f"📊 Total Questions: {count}\n\n"
        
        # Add "What they're really testing"
        testing_desc = {
            "Behavioral": "Can you demonstrate product analytics skills through past experiences using structured storytelling?",
            "Product Metrics & KPIs": "Can you define and track the right metrics to measure product success?",
            "Product Analysis - Root Cause": "Can you investigate and diagnose product issues systematically?",
            "Product Analysis - Feature Impact": "Can you measure and evaluate the impact of product features?",
            "Product Analysis - User Behavior": "Can you analyze user behavior to drive product decisions?",
            "Product Analysis - Funnel Analysis": "Can you analyze and optimize conversion funnels?",
            "A/B Testing & Experimentation": "Can you design, run, and analyze product experiments?",
            "SQL - Product Analytics": "Can you write SQL queries to answer product questions?",
            "SQL - Cohort & Retention": "Can you use SQL to analyze cohorts and retention?",
            "Product Strategy": "Can you think strategically about product direction and opportunities?",
            "Product Sense": "Can you design products that solve real user problems?",
            "Data Visualization & Dashboards": "Can you create dashboards that drive product decisions?",
            "Estimation & Market Sizing": "Can you make reasonable estimates using structured thinking?",
            "Communication & Stakeholder Management": "Can you communicate insights effectively to product teams?",
            "Prioritization": "Can you prioritize product initiatives based on data and impact?",
            "Technical Concepts": "Do you understand the technical foundations of product analytics?"
        }
        
        qb_md += f"🎯 What they're really testing:\n"
        qb_md += f"{testing_desc.get(cat, 'Your product analytics skills.')}\n\n"
        
        # Add framework
        framework = get_framework_for_category(cat)
        if framework:
            qb_md += "🗺️  Mental Model Framework:\n```\n"
            qb_md += framework.strip() + "\n```\n\n"
        
        # Add questions
        qb_md += f"📝 All {count} Questions:\n\n"
        for i, q in enumerate(questions, 1):
            qb_md += f"{i}. {q['question']}\n"
        
        qb_md += "\n"
    
    # Save Question Bank
    qb_path = os.path.join(os.path.dirname(__file__), '../Product_Analyst_Question_Bank.md')
    with open(qb_path, 'w') as f:
        f.write(qb_md)
    print(f"✅ Generated Product_Analyst_Question_Bank.md")
    
    # Generate Interview Framework (high-level overview)
    fw_md = f"""# 🧠 Product Analyst Interview Mindmap (Systematic)

## 📚 Resources

**GitHub Repo**: https://github.com/anix-lynch/Exponent

**Source**: https://www.tryexponent.com/questions?role=product-analyst

---

## 📊 Question Distribution

```
"""
    
    for cat, count in category_counts:
        if count > 0:
            fw_md += f"{cat.ljust(50)} {count:>3} questions\n"
    
    fw_md += f"""```

**Total: {total_questions} questions across {len([c for c in category_counts if c[1] > 0])} categories**

---

## 🎯 How to USE this in interviews

When a question comes:

1. **Name the category silently**
2. **Apply that category's framework**
3. Speak in **structured bullets**

---

## 0️⃣ Core Interview Meta-Structure (applies to EVERYTHING)

No matter the category, interviewers are testing:

- **Product thinking** - Do you understand how products work and what makes them successful?
- **Analytical rigor** - Can you use data to answer product questions?
- **User empathy** - Do you understand user needs and behavior?
- **Business impact** - Do you connect analysis to product and business outcomes?

So every answer should follow this shape:

```
Understand the product → Analyze the data → Generate insights → Recommend action → Measure impact
```

---

"""
    
    # Add key frameworks
    fw_md += "## Key Categories\n\n"
    for cat, count in category_counts[:10]:  # Top 10 categories
        if count > 0:
            fw_md += f"### {cat}\n\n"
            framework = get_framework_for_category(cat)
            if framework:
                fw_md += "```\n" + framework.strip() + "\n```\n\n"
            fw_md += "---\n\n"
    
    fw_md += """
## 💡 Final Tips

### For All Product Analyst Interviews:

1. **Start with the product** - Understand the product, users, and goals before diving into data
2. **Show your thinking** - Walk through your analytical approach step-by-step
3. **Quantify impact** - Use metrics to show product value
4. **Think like a PM** - Connect analysis to product decisions and user outcomes
5. **Be actionable** - Always end with clear recommendations

### Common Mistakes to Avoid:

- ❌ Jumping to analysis without understanding the product context
- ❌ Using metrics without explaining why they matter
- ❌ Presenting data without insights or recommendations
- ❌ Ignoring user experience and behavior
- ❌ Forgetting to measure and communicate impact

---

**Check out the [Product_Analyst_Question_Bank.md](./Product_Analyst_Question_Bank.md) for all questions with detailed frameworks!**
"""
    
    # Save Interview Framework
    fw_path = os.path.join(os.path.dirname(__file__), '../INTERVIEW_FRAMEWORK.md')
    with open(fw_path, 'w') as f:
        f.write(fw_md)
    print(f"✅ Generated INTERVIEW_FRAMEWORK.md")
    
    print("="*70)
    print("✅ Product Analyst frameworks complete!")

if __name__ == "__main__":
    main()
