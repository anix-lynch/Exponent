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
        "Root Cause Analysis": """
Root Cause Analysis
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
        "Product Metrics - Tracking": """
Product Metrics - Tracking
├─ Understand the product
│  ├─ Product vision and goals
│  ├─ User journey and lifecycle
│  ├─ Key value propositions
│  └─ Business model
│
├─ Define what to track
│  ├─ User actions (clicks, views, purchases)
│  ├─ Product events (feature usage, errors)
│  ├─ User properties (demographics, cohort)
│  ├─ Session data (duration, frequency)
│  └─ Business outcomes (revenue, retention)
│
├─ Set up tracking
│  ├─ Event schema design
│  ├─ Naming conventions
│  ├─ User identification (user_id, device_id)
│  ├─ Data validation and QA
│  └─ Documentation
│
├─ Build dashboards
│  ├─ Key metrics and KPIs
│  ├─ Trends over time
│  ├─ Segmentation and filters
│  ├─ Alerts and thresholds
│  └─ Refresh frequency
│
└─ Monitor and iterate
   ├─ Data quality checks
   ├─ Track coverage and adoption
   ├─ Gather feedback from stakeholders
   ├─ Update as product evolves
   └─ Deprecate unused metrics
""",
        "Product Metrics - Definition": """
Product Metrics - Definition
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
        "Data Analysis - Feature Impact": """
Data Analysis - Feature Impact
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
        "Data Analysis - Retention & Churn": """
Data Analysis - Retention & Churn
├─ Define retention
│  ├─ What action defines "retained"? (login, purchase, engagement)
│  ├─ Time windows (D1, D7, D30, M1, M3, M6)
│  ├─ Rolling vs calendar retention
│  └─ Classic vs unbounded retention
│
├─ Measure retention
│  ├─ Overall retention rate
│  ├─ Retention curves by cohort
│  ├─ Compare cohorts over time
│  ├─ Identify improving/declining cohorts
│  └─ Benchmark against targets
│
├─ Analyze churn
│  ├─ When do users churn? (time to churn)
│  ├─ Why do users churn? (exit surveys, feedback)
│  ├─ Churn rate by segment (new vs power users)
│  ├─ Predictive churn modeling
│  └─ Reactivation opportunities
│
├─ Segment and drill down
│  ├─ By user type (new, casual, power)
│  ├─ By acquisition channel
│  ├─ By platform (web, iOS, Android)
│  ├─ By geography or locale
│  └─ By product usage patterns
│
└─ Recommend actions
   ├─ Improve onboarding (activation)
   ├─ Increase engagement (habit formation)
   ├─ Target at-risk users (churn prevention)
   ├─ Win-back campaigns (reactivation)
   └─ Measure impact of interventions
""",
        "Stakeholder Communication": """
Stakeholder Communication
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
        "Dashboard & Visualization": """
Dashboard & Visualization
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
        "A/B Testing - Design": """
A/B Testing - Design
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
        "Data Analysis - User Behavior": """
Data Analysis - User Behavior
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
        "Data Analysis - Funnel Analysis": """
Data Analysis - Funnel Analysis
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
            "Root Cause Analysis": "Can you investigate and diagnose product issues systematically?",
            "Product Metrics - Tracking": "Can you set up tracking and build dashboards for product metrics?",
            "Product Metrics - Definition": "Can you define the right metrics to measure product success?",
            "Data Analysis - Feature Impact": "Can you measure and evaluate the impact of product features?",
            "Data Analysis - Retention & Churn": "Can you analyze retention patterns and identify churn drivers?",
            "Stakeholder Communication": "Can you communicate insights effectively to product teams and leadership?",
            "Dashboard & Visualization": "Can you create dashboards that drive product decisions?",
            "A/B Testing - Design": "Can you design rigorous product experiments?",
            "Data Analysis - User Behavior": "Can you analyze user behavior to drive product decisions?",
            "Data Analysis - Funnel Analysis": "Can you analyze and optimize conversion funnels?",
            "Product Strategy": "Can you think strategically about product direction and opportunities?",
            "Prioritization": "Can you prioritize product initiatives based on data and impact?"
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
    print(f"✅ Generated Product_Analyst_Question_Bank.md with ALL frameworks")
    
    print("="*70)
    print("✅ Product Analyst frameworks complete - ALL categories now have ASCII trees!")

if __name__ == "__main__":
    main()
