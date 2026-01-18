"""
Generate comprehensive Business Analyst frameworks matching Data Analyst quality
"""
import json
import os

def get_framework_for_category(category):
    """Return comprehensive ASCII framework for each BA category"""
    
    frameworks = {
        "Behavioral": """
Behavioral (STAR Method)
├─ Situation
│  ├─ Business context and background
│  ├─ Stakeholders involved
│  ├─ Business metrics at the time
│  └─ Why this was important
│
├─ Task
│  ├─ Your specific responsibility
│  ├─ Business goals and objectives
│  ├─ Constraints (time, resources, data)
│  └─ Success criteria
│
├─ Action
│  ├─ Analysis approach
│  ├─ Tools and methods used
│  ├─ How you collaborated with stakeholders
│  ├─ Challenges you overcame
│  └─ Iterations and refinements
│
└─ Result
   ├─ Quantifiable business outcomes
   ├─ Impact on revenue, cost, or efficiency
   ├─ Stakeholder feedback
   ├─ What you learned
   └─ How you'd apply it again
""",
        "Data Analysis - Business Problem Solving": """
Data Analysis - Business Problem Solving
├─ Understand the business problem
│  ├─ What's the business objective?
│  ├─ Who are the stakeholders?
│  ├─ What's the current state?
│  └─ What does success look like?
│
├─ Identify data sources
│  ├─ What data is available?
│  ├─ What data is needed?
│  ├─ Data quality assessment
│  └─ Gaps and limitations
│
├─ Analyze the data
│  ├─ Exploratory analysis
│  ├─ Segment by key dimensions
│  ├─ Identify patterns and trends
│  ├─ Test hypotheses
│  └─ Quantify the problem
│
├─ Generate insights
│  ├─ What's driving the issue?
│  ├─ What are the opportunities?
│  ├─ What are the risks?
│  └─ What are the tradeoffs?
│
└─ Recommend action
   ├─ Proposed solution
   ├─ Expected business impact
   ├─ Implementation plan
   ├─ Success metrics
   └─ Next steps
""",
        "Data Analysis - Root Cause Analysis": """
Data Analysis - Root Cause Analysis
├─ Define the problem
│  ├─ What metric changed?
│  ├─ When did it change?
│  ├─ How much did it change?
│  ├─ Why does it matter to the business?
│  └─ What's the baseline?
│
├─ Form hypotheses
│  ├─ Internal factors (process changes, system issues)
│  ├─ External factors (market, competition, seasonality)
│  ├─ Customer behavior changes
│  ├─ Data quality issues
│  └─ Prioritize hypotheses
│
├─ Segment and drill down
│  ├─ By time period (hourly, daily, weekly)
│  ├─ By customer segment (new vs returning, demographics)
│  ├─ By product/service line
│  ├─ By geography or channel
│  └─ By business unit
│
├─ Test hypotheses
│  ├─ Gather supporting data
│  ├─ Look for correlations
│  ├─ Rule out alternatives
│  ├─ Validate with stakeholders
│  └─ Identify root cause
│
└─ Recommend solution
   ├─ Fix the immediate issue
   ├─ Prevent recurrence
   ├─ Monitor going forward
   ├─ Expected impact
   └─ Implementation timeline
""",
        "Data Analysis - Trend Analysis": """
Data Analysis - Trend Analysis
├─ Understand the context
│  ├─ Business objective
│  ├─ Time period of interest
│  ├─ Key metrics to track
│  └─ Historical context
│
├─ Prepare the data
│  ├─ Ensure data quality
│  ├─ Handle missing values
│  ├─ Aggregate at appropriate level
│  └─ Normalize if needed
│
├─ Identify patterns
│  ├─ Overall trend (up, down, flat)
│  ├─ Seasonality (daily, weekly, monthly)
│  ├─ Cyclical patterns
│  ├─ Anomalies and outliers
│  └─ Inflection points
│
├─ Analyze drivers
│  ├─ What's causing the trend?
│  ├─ Internal factors
│  ├─ External factors
│  ├─ Correlation with other metrics
│  └─ Segment-level differences
│
└─ Forecast and recommend
   ├─ Project future trends
   ├─ Identify risks and opportunities
   ├─ Recommend actions
   └─ Set targets and goals
""",
        "Data Analysis - Cohort Analysis": """
Data Analysis - Cohort Analysis
├─ Define cohorts
│  ├─ Cohort criteria (signup date, first purchase, etc.)
│  ├─ Time period (daily, weekly, monthly)
│  ├─ Relevant segments
│  └─ Cohort size considerations
│
├─ Choose metrics
│  ├─ Retention rate
│  ├─ Engagement metrics
│  ├─ Revenue per cohort
│  ├─ Conversion rates
│  └─ Lifetime value
│
├─ Analyze patterns
│  ├─ Retention curves by cohort
│  ├─ Compare cohorts over time
│  ├─ Identify improving/declining cohorts
│  ├─ Look for seasonality
│  └─ Benchmark against targets
│
├─ Investigate differences
│  ├─ What changed between cohorts?
│  ├─ Product changes
│  ├─ Marketing campaigns
│  ├─ External factors
│  └─ User behavior shifts
│
└─ Drive action
   ├─ Improve retention
   ├─ Optimize onboarding
   ├─ Target at-risk cohorts
   └─ Forecast future performance
""",
        "SQL - Joins & Aggregation": """
SQL - Joins & Aggregation
├─ Understand requirements
│  ├─ What question are we answering?
│  ├─ What tables are involved?
│  ├─ What's the grain of the output?
│  └─ What aggregations are needed?
│
├─ Plan the query
│  ├─ Identify primary table
│  ├─ Determine join types (INNER, LEFT, RIGHT, FULL)
│  ├─ Join conditions (keys)
│  ├─ Filter criteria (WHERE)
│  └─ Aggregation level (GROUP BY)
│
├─ Write the query
│  ├─ SELECT columns and aggregations (SUM, COUNT, AVG, MAX, MIN)
│  ├─ FROM primary table
│  ├─ JOIN additional tables
│  ├─ WHERE to filter rows
│  ├─ GROUP BY for aggregations
│  ├─ HAVING to filter groups
│  └─ ORDER BY and LIMIT
│
├─ Optimize
│  ├─ Use appropriate indexes
│  ├─ Filter early (WHERE before JOIN)
│  ├─ Avoid SELECT *
│  ├─ Use EXPLAIN to check plan
│  └─ Consider query performance
│
└─ Validate
   ├─ Check for nulls and duplicates
   ├─ Verify row counts
   ├─ Spot check results
   ├─ Test edge cases
   └─ Document assumptions
""",
        "SQL - Window Functions": """
SQL - Window Functions
├─ Understand the use case
│  ├─ Running totals
│  ├─ Moving averages
│  ├─ Ranking (ROW_NUMBER, RANK, DENSE_RANK)
│  ├─ Lead/Lag (previous/next values)
│  └─ Percentiles
│
├─ Define the window
│  ├─ PARTITION BY (groups)
│  ├─ ORDER BY (sequence)
│  ├─ Frame specification (ROWS, RANGE)
│  └─ Window boundaries (PRECEDING, FOLLOWING)
│
├─ Choose function
│  ├─ Aggregate: SUM, AVG, COUNT, MAX, MIN
│  ├─ Ranking: ROW_NUMBER, RANK, DENSE_RANK, NTILE
│  ├─ Value: LAG, LEAD, FIRST_VALUE, LAST_VALUE
│  └─ Distribution: PERCENT_RANK, CUME_DIST
│
├─ Write the query
│  ├─ SELECT with window function
│  ├─ OVER clause with PARTITION and ORDER
│  ├─ Frame specification if needed
│  └─ Combine with other clauses
│
└─ Validate
   ├─ Check partitioning is correct
   ├─ Verify ordering
   ├─ Test edge cases
   └─ Compare with expected results
""",
        "SQL - Query Optimization": """
SQL - Query Optimization
├─ Identify performance issues
│  ├─ Slow query logs
│  ├─ User complaints
│  ├─ Resource monitoring
│  └─ Query execution time
│
├─ Analyze the query
│  ├─ Use EXPLAIN or EXPLAIN ANALYZE
│  ├─ Identify bottlenecks (full table scans, sorts)
│  ├─ Check join order
│  ├─ Look for missing indexes
│  └─ Identify unnecessary operations
│
├─ Optimize
│  ├─ Add appropriate indexes
│  ├─ Rewrite subqueries as JOINs
│  ├─ Filter early (WHERE before JOIN)
│  ├─ Use LIMIT when appropriate
│  ├─ Avoid SELECT * (specify columns)
│  ├─ Use EXISTS instead of IN for large sets
│  └─ Partition large tables
│
├─ Test improvements
│  ├─ Measure execution time
│  ├─ Check resource usage
│  ├─ Verify results are unchanged
│  └─ Test with production data volume
│
└─ Monitor
   ├─ Track query performance over time
   ├─ Watch for regressions
   ├─ Update statistics
   └─ Maintain indexes
""",
        "Business Metrics & KPIs": """
Business Metrics & KPIs
├─ Understand the business
│  ├─ Business model and revenue drivers
│  ├─ Customer journey and lifecycle
│  ├─ Key value propositions
│  ├─ Competitive landscape
│  └─ Strategic objectives
│
├─ Define metrics
│  ├─ North Star Metric (primary success indicator)
│  ├─ Leading indicators (predictive)
│  ├─ Lagging indicators (historical)
│  ├─ Input metrics (controllable)
│  ├─ Output metrics (results)
│  └─ Guardrail metrics (protect against negative impacts)
│
├─ Ensure quality
│  ├─ Specific and measurable
│  ├─ Aligned with business goals
│  ├─ Actionable (can influence)
│  ├─ Timely (updated regularly)
│  └─ Comparable (benchmarks)
│
├─ Track and report
│  ├─ Data sources and calculation
│  ├─ Frequency of measurement
│  ├─ Dashboards and visualizations
│  ├─ Alerts and thresholds
│  └─ Stakeholder communication
│
└─ Drive action
   ├─ Analyze trends and patterns
   ├─ Identify opportunities and risks
   ├─ Set targets and goals
   ├─ Prioritize initiatives
   └─ Measure impact of changes
""",
        "Estimation & Market Sizing": """
Estimation & Market Sizing
├─ Clarify the question
│  ├─ What exactly are we estimating?
│  ├─ Geography (country, region, world)
│  ├─ Time period (annual, monthly)
│  ├─ Units (dollars, customers, transactions)
│  └─ Precision needed
│
├─ Choose approach
│  ├─ Top-down (total market → segments)
│  ├─ Bottom-up (unit economics → total)
│  ├─ Proxy/analogy (similar markets)
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
        "Requirements Gathering": """
Requirements Gathering
├─ Understand the context
│  ├─ Business problem or opportunity
│  ├─ Stakeholders and their roles
│  ├─ Current state and pain points
│  ├─ Desired future state
│  └─ Success criteria
│
├─ Elicit requirements
│  ├─ Stakeholder interviews
│  ├─ Workshops and brainstorming
│  ├─ Process observation
│  ├─ Document analysis
│  └─ Prototyping and feedback
│
├─ Document requirements
│  ├─ Functional requirements (what system should do)
│  ├─ Non-functional requirements (performance, security)
│  ├─ Business rules
│  ├─ User stories or use cases
│  ├─ Data requirements
│  └─ Acceptance criteria
│
├─ Validate and prioritize
│  ├─ Review with stakeholders
│  ├─ Resolve conflicts and ambiguities
│  ├─ Prioritize (MoSCoW: Must, Should, Could, Won't)
│  ├─ Assess feasibility
│  └─ Get sign-off
│
└─ Manage changes
   ├─ Track requirement changes
   ├─ Assess impact of changes
   ├─ Update documentation
   └─ Communicate to team
""",
        "Stakeholder Management": """
Stakeholder Management
├─ Identify stakeholders
│  ├─ Who is impacted?
│  ├─ Who has decision authority?
│  ├─ Who provides input?
│  ├─ Who are the end users?
│  └─ Map influence and interest
│
├─ Understand their needs
│  ├─ Goals and objectives
│  ├─ Pain points and concerns
│  ├─ Success criteria
│  ├─ Communication preferences
│  └─ Level of technical knowledge
│
├─ Communicate effectively
│  ├─ Tailor message to audience
│  ├─ Use appropriate level of detail
│  ├─ Visual aids (charts, dashboards)
│  ├─ Tell a story with data
│  ├─ Focus on business impact
│  └─ Provide recommendations, not just data
│
├─ Build relationships
│  ├─ Regular check-ins
│  ├─ Active listening
│  ├─ Manage expectations
│  ├─ Be transparent about limitations
│  └─ Follow through on commitments
│
└─ Manage conflicts
   ├─ Understand different perspectives
   ├─ Find common ground
   ├─ Use data to inform decisions
   ├─ Escalate when needed
   └─ Document decisions and rationale
""",
        "Process Improvement": """
Process Improvement
├─ Understand current process
│  ├─ Map the current state
│  ├─ Identify inputs and outputs
│  ├─ Document steps and handoffs
│  ├─ Measure current performance
│  └─ Identify pain points
│
├─ Analyze inefficiencies
│  ├─ Bottlenecks and delays
│  ├─ Redundant or unnecessary steps
│  ├─ Manual vs automated tasks
│  ├─ Error rates and rework
│  └─ Resource utilization
│
├─ Design improved process
│  ├─ Eliminate waste
│  ├─ Streamline steps
│  ├─ Automate where possible
│  ├─ Reduce handoffs
│  ├─ Add quality checks
│  └─ Map the future state
│
├─ Quantify impact
│  ├─ Time savings
│  ├─ Cost reduction
│  ├─ Quality improvement
│  ├─ Capacity increase
│  └─ ROI calculation
│
└─ Implement and monitor
   ├─ Change management plan
   ├─ Training and documentation
   ├─ Pilot and iterate
   ├─ Monitor performance
   └─ Continuous improvement
""",
        "Financial Analysis": """
Financial Analysis
├─ Understand the objective
│  ├─ What decision needs to be made?
│  ├─ What financial metrics matter?
│  ├─ Time period of analysis
│  └─ Level of detail needed
│
├─ Gather financial data
│  ├─ Revenue (by product, channel, segment)
│  ├─ Costs (fixed, variable, direct, indirect)
│  ├─ Profitability (gross margin, EBITDA, net income)
│  ├─ Cash flow
│  └─ Balance sheet items
│
├─ Analyze performance
│  ├─ Trend analysis (YoY, MoM, QoQ)
│  ├─ Variance analysis (actual vs budget/forecast)
│  ├─ Ratio analysis (margins, ROI, ROE)
│  ├─ Segment performance
│  └─ Benchmark against industry
│
├─ Identify drivers
│  ├─ Revenue drivers (volume, price, mix)
│  ├─ Cost drivers (efficiency, scale, input costs)
│  ├─ Profitability drivers
│  └─ Working capital drivers
│
└─ Recommend action
   ├─ Opportunities to increase revenue
   ├─ Opportunities to reduce costs
   ├─ Investment decisions (ROI analysis)
   ├─ Pricing strategies
   └─ Financial forecasts
""",
        "Product Strategy": """
Product Strategy
├─ Understand the market
│  ├─ Market size and growth
│  ├─ Customer segments and needs
│  ├─ Competitive landscape
│  ├─ Market trends
│  └─ Regulatory environment
│
├─ Define product vision
│  ├─ Target customers
│  ├─ Value proposition
│  ├─ Differentiation
│  ├─ Strategic fit
│  └─ Success metrics
│
├─ Analyze opportunities
│  ├─ New products or features
│  ├─ Market expansion
│  ├─ Customer segments
│  ├─ Partnerships
│  └─ Business model innovations
│
├─ Evaluate options
│  ├─ Market attractiveness
│  ├─ Competitive advantage
│  ├─ Financial viability (revenue, costs, ROI)
│  ├─ Technical feasibility
│  ├─ Resource requirements
│  └─ Risks and dependencies
│
└─ Recommend strategy
   ├─ Product roadmap
   ├─ Go-to-market approach
   ├─ Pricing strategy
   ├─ Success metrics and targets
   └─ Implementation plan
""",
        "Communication & Presentation": """
Communication & Presentation
├─ Know your audience
│  ├─ Who are they? (executives, technical, operational)
│  ├─ What do they care about?
│  ├─ What's their level of knowledge?
│  ├─ What decision do they need to make?
│  └─ How much time do you have?
│
├─ Structure your message
│  ├─ Start with the conclusion (executive summary)
│  ├─ Provide context and problem statement
│  ├─ Present analysis and insights
│  ├─ Make clear recommendations
│  └─ End with next steps
│
├─ Visualize effectively
│  ├─ Choose right chart type (bar, line, scatter, etc.)
│  ├─ Keep it simple and focused
│  ├─ Use clear labels and titles
│  ├─ Highlight key insights
│  ├─ Use consistent colors and formatting
│  └─ Remove clutter
│
├─ Tell a story with data
│  ├─ Set the scene (context)
│  ├─ Introduce the problem
│  ├─ Show the evidence (data)
│  ├─ Explain the insights
│  └─ Recommend the solution
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
│  ├─ Business goals and strategy
│  ├─ Available resources (time, budget, people)
│  ├─ Constraints and dependencies
│  ├─ Stakeholder needs
│  └─ Timeline and urgency
│
├─ Define criteria
│  ├─ Business impact (revenue, cost savings, efficiency)
│  ├─ Strategic alignment
│  ├─ Customer value
│  ├─ Effort required (time, resources, complexity)
│  ├─ Risk and uncertainty
│  └─ Dependencies
│
├─ Evaluate options
│  ├─ Score each option on criteria
│  ├─ Impact vs Effort matrix
│  ├─ ROI calculation
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
        "Data Visualization": """
Data Visualization
├─ Understand the purpose
│  ├─ What story are you telling?
│  ├─ What decision needs to be made?
│  ├─ Who is the audience?
│  └─ What's the key message?
│
├─ Choose the right chart
│  ├─ Comparison: Bar chart, column chart
│  ├─ Trend over time: Line chart, area chart
│  ├─ Distribution: Histogram, box plot
│  ├─ Relationship: Scatter plot
│  ├─ Composition: Pie chart, stacked bar, treemap
│  └─ Geographic: Map
│
├─ Design effectively
│  ├─ Clear and descriptive title
│  ├─ Labeled axes with units
│  ├─ Appropriate scale (start at zero for bar charts)
│  ├─ Minimal colors (use for emphasis)
│  ├─ Remove chart junk (gridlines, borders)
│  └─ Consistent formatting
│
├─ Highlight insights
│  ├─ Annotate key points
│  ├─ Use color to draw attention
│  ├─ Add reference lines or benchmarks
│  ├─ Show trends or patterns
│  └─ Include context
│
└─ Build dashboards
   ├─ Organize logically (most important first)
   ├─ Use filters and interactivity
   ├─ Consistent layout and style
   ├─ Balance detail and overview
   └─ Optimize for refresh and performance
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
    
    print(f"🚀 Generating comprehensive Business Analyst frameworks...")
    print(f"   Total questions: {total_questions}")
    print(f"   Categories: {len([c for c in category_counts if c[1] > 0])}")
    
    # Generate Question Bank (matching Data Analyst format)
    qb_md = """
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║           BUSINESS ANALYST INTERVIEW PREPARATION FRAMEWORK                     ║
║           Mental Models & Complete Question Bank                               ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

This framework provides mental models for approaching each type of business analyst
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
            "Behavioral": "Can you demonstrate BA skills through past experiences using structured storytelling?",
            "Business Metrics & KPIs": "Can you define and track the right metrics to measure business success?",
            "Data Analysis - Root Cause Analysis": "Can you investigate and diagnose business problems systematically?",
            "Financial Analysis": "Can you analyze financial data to drive business decisions?",
            "Product Strategy": "Can you think strategically about product and market opportunities?",
            "Communication & Presentation": "Can you communicate insights effectively to diverse stakeholders?",
            "Estimation & Market Sizing": "Can you make reasonable estimates using structured thinking?",
            "Stakeholder Management": "Can you work effectively with diverse stakeholders across the organization?",
            "Data Analysis - Cohort Analysis": "Can you analyze user cohorts to understand retention and behavior?",
            "Process Improvement": "Can you identify and implement process improvements?",
            "Data Visualization": "Can you create clear, effective visualizations that drive decisions?",
            "SQL - Query Optimization": "Can you write efficient SQL queries and optimize performance?",
            "Data Analysis - Business Problem Solving": "Can you use data to solve complex business problems?",
            "Data Analysis - Trend Analysis": "Can you identify and analyze trends to inform strategy?",
            "SQL - Joins & Aggregation": "Can you write SQL queries to extract and aggregate data?",
            "SQL - Window Functions": "Can you use advanced SQL for complex analytical queries?",
            "Prioritization": "Can you prioritize competing initiatives based on business impact?",
            "Requirements Gathering": "Can you elicit and document business requirements effectively?"
        }
        
        qb_md += f"🎯 What they're really testing:\n"
        qb_md += f"{testing_desc.get(cat, 'Your business analysis skills.')}\n\n"
        
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
    qb_path = os.path.join(os.path.dirname(__file__), '../Business_Analyst_Question_Bank.md')
    with open(qb_path, 'w') as f:
        f.write(qb_md)
    print(f"✅ Generated Business_Analyst_Question_Bank.md")
    
    # Generate Interview Framework (high-level overview)
    fw_md = f"""# 🧠 Business Analyst Interview Mindmap (Systematic)

## 📚 Resources

**GitHub Repo**: https://github.com/anix-lynch/Exponent

**Source**: https://www.tryexponent.com/questions?role=business-analyst

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

- **Business acumen** - Do you understand the business context?
- **Analytical thinking** - Can you break down complex problems?
- **Communication** - Can you explain insights to non-technical stakeholders?
- **Impact focus** - Do you connect analysis to business outcomes?

So every answer should follow this shape:

```
Understand business context → Analyze data → Generate insights → Recommend action → Measure impact
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

### For All Business Analyst Interviews:

1. **Start with the business** - Understand the business context before diving into analysis
2. **Show your thinking** - Walk through your analytical approach step-by-step
3. **Quantify impact** - Use numbers to show business value
4. **Communicate clearly** - Tailor your message to your audience
5. **Be actionable** - Always end with clear recommendations

### Common Mistakes to Avoid:

- ❌ Jumping to analysis without understanding the business problem
- ❌ Using jargon with non-technical stakeholders
- ❌ Presenting data without insights or recommendations
- ❌ Ignoring stakeholder needs and concerns
- ❌ Forgetting to measure and communicate impact

---

**Check out the [Business_Analyst_Question_Bank.md](./Business_Analyst_Question_Bank.md) for all questions with detailed frameworks!**
"""
    
    # Save Interview Framework
    fw_path = os.path.join(os.path.dirname(__file__), '../INTERVIEW_FRAMEWORK.md')
    with open(fw_path, 'w') as f:
        f.write(fw_md)
    print(f"✅ Generated INTERVIEW_FRAMEWORK.md")
    
    print("="*70)
    print("✅ Business Analyst frameworks complete!")

if __name__ == "__main__":
    main()
