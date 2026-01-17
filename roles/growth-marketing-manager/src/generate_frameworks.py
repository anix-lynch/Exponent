"""
Generate Growth Marketing Manager Interview Framework and Question Bank
"""
import json
import os

def get_framework_for_category(category):
    """Return ASCII framework for each category"""
    
    frameworks = {
        "Behavioral": """
Behavioral (STAR Method)
├─ Situation
│  ├─ Context and background
│  ├─ Business metrics at the time
│  └─ Why growth was needed
│
├─ Task
│  ├─ Your specific responsibility
│  ├─ Growth goals/targets
│  └─ Constraints (budget, time, resources)
│
├─ Action
│  ├─ Strategy you developed
│  ├─ Channels you tested
│  ├─ Experiments you ran
│  └─ How you collaborated
│
└─ Result
   ├─ Growth metrics (users, revenue, etc.)
   ├─ ROI and efficiency gains
   ├─ Learnings and insights
   └─ How you'd scale it
""",
        "Growth Strategy": """
Growth Strategy
├─ Understand current state
│  ├─ Current growth rate
│  ├─ Key metrics (CAC, LTV, etc.)
│  └─ Growth blockers
│
├─ Identify opportunities
│  ├─ User acquisition channels
│  ├─ Activation improvements
│  ├─ Retention levers
│  └─ Monetization potential
│
├─ Prioritize initiatives
│  ├─ Impact vs effort
│  ├─ ICE scoring (Impact, Confidence, Ease)
│  └─ Resource allocation
│
├─ Build growth model
│  ├─ Assumptions
│  ├─ Projections
│  └─ Key drivers
│
└─ Execute and iterate
   ├─ Run experiments
   ├─ Measure results
   └─ Double down on winners
""",
        "Customer Acquisition": """
Customer Acquisition
├─ Define target audience
│  ├─ ICP (Ideal Customer Profile)
│  ├─ User segments
│  └─ Pain points
│
├─ Channel strategy
│  ├─ Paid (SEM, social, display)
│  ├─ Organic (SEO, content, viral)
│  ├─ Partnerships
│  └─ Referrals
│
├─ Optimize funnel
│  ├─ Awareness
│  ├─ Consideration
│  ├─ Conversion
│  └─ Drop-off analysis
│
├─ Measure efficiency
│  ├─ CAC (Customer Acquisition Cost)
│  ├─ LTV (Lifetime Value)
│  ├─ LTV:CAC ratio
│  └─ Payback period
│
└─ Scale what works
   ├─ Increase budget
   ├─ Expand to new channels
   └─ Automate processes
""",
        "Retention & Engagement": """
Retention & Engagement
├─ Understand user journey
│  ├─ Onboarding experience
│  ├─ Aha moment
│  ├─ Core value delivery
│  └─ Habit formation
│
├─ Identify churn drivers
│  ├─ When do users churn?
│  ├─ Why do they churn?
│  └─ Cohort analysis
│
├─ Build retention loops
│  ├─ Email/push campaigns
│  ├─ In-product engagement
│  ├─ Community building
│  └─ Loyalty programs
│
├─ Measure engagement
│  ├─ DAU/MAU ratio
│  ├─ Retention curves
│  ├─ Feature adoption
│  └─ NPS/satisfaction
│
└─ Iterate and improve
   ├─ A/B test improvements
   ├─ Personalization
   └─ Win-back campaigns
""",
        "Analytics & Metrics": """
Analytics & Metrics
├─ Define success metrics
│  ├─ North Star Metric
│  ├─ Leading indicators
│  └─ Lagging indicators
│
├─ Build measurement framework
│  ├─ Funnel metrics
│  ├─ Cohort analysis
│  ├─ Attribution model
│  └─ Dashboards
│
├─ Analyze data
│  ├─ Trends and patterns
│  ├─ Segment performance
│  ├─ Channel effectiveness
│  └─ User behavior
│
├─ Generate insights
│  ├─ What's working?
│  ├─ What's not?
│  └─ Why?
│
└─ Drive action
   ├─ Recommendations
   ├─ Prioritization
   └─ Experimentation roadmap
""",
        "A/B Testing & Experimentation": """
A/B Testing & Experimentation
├─ Formulate hypothesis
│  ├─ What do you believe?
│  ├─ Why do you believe it?
│  └─ Expected impact
│
├─ Design experiment
│  ├─ Control vs variant
│  ├─ Sample size calculation
│  ├─ Duration
│  └─ Success metrics
│
├─ Run test
│  ├─ Ensure proper randomization
│  ├─ Monitor for issues
│  └─ Avoid peeking
│
├─ Analyze results
│  ├─ Statistical significance
│  ├─ Practical significance
│  ├─ Segment analysis
│  └─ Secondary metrics
│
└─ Take action
   ├─ Ship winner
   ├─ Document learnings
   └─ Plan next experiment
""",
        "Channel Strategy": """
Channel Strategy
├─ Evaluate channels
│  ├─ Paid channels (SEM, social, display)
│  ├─ Organic channels (SEO, content, PR)
│  ├─ Referral/viral
│  └─ Partnerships
│
├─ Test and learn
│  ├─ Small budget tests
│  ├─ Measure CAC and LTV
│  ├─ Assess scalability
│  └─ Compare channels
│
├─ Optimize performance
│  ├─ Creative testing
│  ├─ Targeting refinement
│  ├─ Bidding strategy
│  └─ Landing page optimization
│
├─ Allocate budget
│  ├─ ROI by channel
│  ├─ Diminishing returns
│  ├─ Portfolio approach
│  └─ Reserve for testing
│
└─ Scale winners
   ├─ Increase spend
   ├─ Expand geographies
   └─ New audience segments
""",
        "Product-Led Growth": """
Product-Led Growth
├─ Design for virality
│  ├─ Built-in sharing
│  ├─ Network effects
│  ├─ Referral incentives
│  └─ Social proof
│
├─ Optimize onboarding
│  ├─ Time to value
│  ├─ Aha moment
│  ├─ Activation rate
│  └─ Reduce friction
│
├─ Freemium strategy
│  ├─ Free tier value
│  ├─ Upgrade triggers
│  ├─ Conversion rate
│  └─ Monetization balance
│
├─ In-product growth loops
│  ├─ Invite flows
│  ├─ Collaboration features
│  ├─ Content sharing
│  └─ User-generated content
│
└─ Measure PLG metrics
   ├─ Viral coefficient (k-factor)
   ├─ Time to value
   ├─ Free-to-paid conversion
   └─ Expansion revenue
"""
    }
    
    return frameworks.get(category, "Framework coming soon...")

def generate_question_bank():
    """Generate the combined Question Bank with frameworks"""
    
    # Load categorized questions
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    by_category_path = os.path.join(data_dir, 'questions_by_category.json')
    
    with open(by_category_path, 'r') as f:
        by_category = json.load(f)
    
    # Count total questions
    total_questions = sum(len(questions) for questions in by_category.values())
    
    # Start building markdown
    md = f"""# Growth Marketing Manager Interview Question Bank

## 📚 Resources

**{total_questions} Growth Marketing Manager questions** from [Exponent](https://www.tryexponent.com/questions?role=growth-marketing-manager)

**GitHub**: [Exponent Interview Prep](https://github.com/anix-lynch/Exponent)

⚠️ **Note**: Very limited dataset (only 2 questions available on Exponent)

---

## 📊 Question Distribution

"""
    
    # Add question counts
    category_counts = [(cat, len(by_category[cat])) for cat in by_category.keys()]
    category_counts.sort(key=lambda x: x[1], reverse=True)
    
    for cat, count in category_counts:
        if count > 0:
            md += f"- **{cat}**: {count} question{'s' if count != 1 else ''}\n"
    
    md += f"\n**Total: {total_questions} questions**\n\n"
    md += "---\n\n"
    
    # Add each category with framework and questions
    for cat, count in category_counts:
        if count == 0:
            continue
        
        questions = by_category[cat]
        
        md += "=" * 80 + "\n"
        md += f"{cat.upper()}\n"
        md += "=" * 80 + "\n\n"
        md += f"📊 **Total Questions**: {count}\n\n"
        
        # Add "What they're really testing"
        testing_descriptions = {
            "Behavioral": "Can you demonstrate growth mindset and data-driven decision making through past experiences?",
            "Growth Strategy": "Can you develop comprehensive growth strategies that drive sustainable user and revenue growth?",
            "Customer Acquisition": "Can you efficiently acquire customers across multiple channels?",
            "Retention & Engagement": "Can you keep users engaged and reduce churn?",
            "Analytics & Metrics": "Can you define, track, and act on the right growth metrics?",
            "A/B Testing & Experimentation": "Can you design and execute rigorous experiments to drive growth?",
            "Channel Strategy": "Can you identify, test, and scale the most effective marketing channels?",
            "Product-Led Growth": "Can you leverage the product itself as the primary growth driver?"
        }
        
        md += f"🎯 **What they're really testing:**\n"
        md += f"{testing_descriptions.get(cat, 'Your ability to drive measurable growth.')}\n\n"
        
        # Add framework
        md += "🗺️  **Mental Model Framework:**\n\n"
        md += "```\n"
        md += get_framework_for_category(cat).strip()
        md += "\n```\n\n"
        
        # Add questions
        md += f"📝 **All {count} Question{'s' if count != 1 else ''}:**\n\n"
        for i, q in enumerate(questions, 1):
            md += f"{i}. {q['question']}\n"
        
        md += "\n"
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), '../Growth_Marketing_Manager_Question_Bank.md')
    with open(output_path, 'w') as f:
        f.write(md)
    
    print(f"✅ Generated {output_path}")

def generate_interview_framework():
    """Generate the high-level Interview Framework"""
    
    md = """# Growth Marketing Manager Interview Framework

## 📚 Resources

**GitHub**: [Exponent Interview Prep](https://github.com/anix-lynch/Exponent)

**Source**: [Exponent Growth Marketing Manager Questions](https://www.tryexponent.com/questions?role=growth-marketing-manager)

⚠️ **Note**: Very limited dataset (only 2 questions available on Exponent)

---

## 📊 Question Distribution

- **Behavioral**: 2 questions

**Total: 2 questions**

---

## 🎯 How to Use This Framework

1. **Identify the question type** (Behavioral, Growth Strategy, etc.)
2. **Apply the relevant framework** (see below)
3. **Structure your answer** using the mental model

---

## 0️⃣ Core Meta-Structure

### Universal Principles for Growth Marketing Manager Interviews

1. **Think in metrics** - Everything should be measurable and data-driven
2. **Focus on ROI** - Show you understand CAC, LTV, and payback periods
3. **Experiment constantly** - Growth is about rapid testing and iteration
4. **Scale what works** - Identify winners and double down
5. **Cross-functional mindset** - Growth requires product, eng, and marketing alignment

### Universal Answer Framework

```
Growth Marketing Answer Structure
├─ Current state
│  ├─ Key metrics
│  └─ Growth challenges
│
├─ Opportunity
│  ├─ What could be improved?
│  └─ Expected impact
│
├─ Strategy
│  ├─ Hypothesis
│  ├─ Approach
│  └─ Channels/tactics
│
├─ Execution
│  ├─ Experiments to run
│  ├─ Success metrics
│  └─ Timeline
│
└─ Results
   ├─ Quantifiable outcomes
   ├─ Learnings
   └─ Next steps
```

---

## 1️⃣ Behavioral Questions

**What they're really testing:**
Can you demonstrate growth mindset and data-driven decision making through past experiences?

**Framework: STAR Method (Growth-Focused)**

```
Behavioral (STAR Method)
├─ Situation
│  ├─ Context and background
│  ├─ Business metrics at the time
│  └─ Why growth was needed
│
├─ Task
│  ├─ Your specific responsibility
│  ├─ Growth goals/targets
│  └─ Constraints (budget, time, resources)
│
├─ Action
│  ├─ Strategy you developed
│  ├─ Channels you tested
│  ├─ Experiments you ran
│  └─ How you collaborated
│
└─ Result
   ├─ Growth metrics (users, revenue, etc.)
   ├─ ROI and efficiency gains
   ├─ Learnings and insights
   └─ How you'd scale it
```

📌 **Key tip**: Always quantify your impact - growth marketers live and die by numbers

---

## 2️⃣ Growth Strategy

**What they're really testing:**
Can you develop comprehensive growth strategies that drive sustainable user and revenue growth?

**Framework:**

```
Growth Strategy
├─ Understand current state
│  ├─ Current growth rate
│  ├─ Key metrics (CAC, LTV, etc.)
│  └─ Growth blockers
│
├─ Identify opportunities
│  ├─ User acquisition channels
│  ├─ Activation improvements
│  ├─ Retention levers
│  └─ Monetization potential
│
├─ Prioritize initiatives
│  ├─ Impact vs effort
│  ├─ ICE scoring (Impact, Confidence, Ease)
│  └─ Resource allocation
│
├─ Build growth model
│  ├─ Assumptions
│  ├─ Projections
│  └─ Key drivers
│
└─ Execute and iterate
   ├─ Run experiments
   ├─ Measure results
   └─ Double down on winners
```

📌 **Key tip**: Use frameworks like AARRR (Acquisition, Activation, Retention, Revenue, Referral) to structure your thinking

---

## 3️⃣ Customer Acquisition

**What they're really testing:**
Can you efficiently acquire customers across multiple channels?

**Framework:**

```
Customer Acquisition
├─ Define target audience
│  ├─ ICP (Ideal Customer Profile)
│  ├─ User segments
│  └─ Pain points
│
├─ Channel strategy
│  ├─ Paid (SEM, social, display)
│  ├─ Organic (SEO, content, viral)
│  ├─ Partnerships
│  └─ Referrals
│
├─ Optimize funnel
│  ├─ Awareness
│  ├─ Consideration
│  ├─ Conversion
│  └─ Drop-off analysis
│
├─ Measure efficiency
│  ├─ CAC (Customer Acquisition Cost)
│  ├─ LTV (Lifetime Value)
│  ├─ LTV:CAC ratio
│  └─ Payback period
│
└─ Scale what works
   ├─ Increase budget
   ├─ Expand to new channels
   └─ Automate processes
```

📌 **Key tip**: Always know your unit economics - CAC, LTV, and payback period

---

## 4️⃣ Retention & Engagement

**What they're really testing:**
Can you keep users engaged and reduce churn?

**Framework:**

```
Retention & Engagement
├─ Understand user journey
│  ├─ Onboarding experience
│  ├─ Aha moment
│  ├─ Core value delivery
│  └─ Habit formation
│
├─ Identify churn drivers
│  ├─ When do users churn?
│  ├─ Why do they churn?
│  └─ Cohort analysis
│
├─ Build retention loops
│  ├─ Email/push campaigns
│  ├─ In-product engagement
│  ├─ Community building
│  └─ Loyalty programs
│
├─ Measure engagement
│  ├─ DAU/MAU ratio
│  ├─ Retention curves
│  ├─ Feature adoption
│  └─ NPS/satisfaction
│
└─ Iterate and improve
   ├─ A/B test improvements
   ├─ Personalization
   └─ Win-back campaigns
```

📌 **Key tip**: Retention is often more valuable than acquisition - focus on the "aha moment"

---

## 5️⃣ Analytics & Metrics

**What they're really testing:**
Can you define, track, and act on the right growth metrics?

**Framework:**

```
Analytics & Metrics
├─ Define success metrics
│  ├─ North Star Metric
│  ├─ Leading indicators
│  └─ Lagging indicators
│
├─ Build measurement framework
│  ├─ Funnel metrics
│  ├─ Cohort analysis
│  ├─ Attribution model
│  └─ Dashboards
│
├─ Analyze data
│  ├─ Trends and patterns
│  ├─ Segment performance
│  ├─ Channel effectiveness
│  └─ User behavior
│
├─ Generate insights
│  ├─ What's working?
│  ├─ What's not?
│  └─ Why?
│
└─ Drive action
   ├─ Recommendations
   ├─ Prioritization
   └─ Experimentation roadmap
```

📌 **Key tip**: Choose a North Star Metric that reflects true value delivery

---

## 6️⃣ A/B Testing & Experimentation

**What they're really testing:**
Can you design and execute rigorous experiments to drive growth?

**Framework:**

```
A/B Testing & Experimentation
├─ Formulate hypothesis
│  ├─ What do you believe?
│  ├─ Why do you believe it?
│  └─ Expected impact
│
├─ Design experiment
│  ├─ Control vs variant
│  ├─ Sample size calculation
│  ├─ Duration
│  └─ Success metrics
│
├─ Run test
│  ├─ Ensure proper randomization
│  ├─ Monitor for issues
│  └─ Avoid peeking
│
├─ Analyze results
│  ├─ Statistical significance
│  ├─ Practical significance
│  ├─ Segment analysis
│  └─ Secondary metrics
│
└─ Take action
   ├─ Ship winner
   ├─ Document learnings
   └─ Plan next experiment
```

📌 **Key tip**: Always start with a clear hypothesis and define success metrics upfront

---

## 7️⃣ Channel Strategy

**What they're really testing:**
Can you identify, test, and scale the most effective marketing channels?

**Framework:**

```
Channel Strategy
├─ Evaluate channels
│  ├─ Paid channels (SEM, social, display)
│  ├─ Organic channels (SEO, content, PR)
│  ├─ Referral/viral
│  └─ Partnerships
│
├─ Test and learn
│  ├─ Small budget tests
│  ├─ Measure CAC and LTV
│  ├─ Assess scalability
│  └─ Compare channels
│
├─ Optimize performance
│  ├─ Creative testing
│  ├─ Targeting refinement
│  ├─ Bidding strategy
│  └─ Landing page optimization
│
├─ Allocate budget
│  ├─ ROI by channel
│  ├─ Diminishing returns
│  ├─ Portfolio approach
│  └─ Reserve for testing
│
└─ Scale winners
   ├─ Increase spend
   ├─ Expand geographies
   └─ New audience segments
```

📌 **Key tip**: Build a portfolio of channels - don't rely on just one

---

## 8️⃣ Product-Led Growth

**What they're really testing:**
Can you leverage the product itself as the primary growth driver?

**Framework:**

```
Product-Led Growth
├─ Design for virality
│  ├─ Built-in sharing
│  ├─ Network effects
│  ├─ Referral incentives
│  └─ Social proof
│
├─ Optimize onboarding
│  ├─ Time to value
│  ├─ Aha moment
│  ├─ Activation rate
│  └─ Reduce friction
│
├─ Freemium strategy
│  ├─ Free tier value
│  ├─ Upgrade triggers
│  ├─ Conversion rate
│  └─ Monetization balance
│
├─ In-product growth loops
│  ├─ Invite flows
│  ├─ Collaboration features
│  ├─ Content sharing
│  └─ User-generated content
│
└─ Measure PLG metrics
   ├─ Viral coefficient (k-factor)
   ├─ Time to value
   ├─ Free-to-paid conversion
   └─ Expansion revenue
```

📌 **Key tip**: The best growth loop is one where users invite other users as part of getting value

---

## 💡 Final Tips

### For All Growth Marketing Manager Interviews:

1. **Be hypothesis-driven** - Start with a clear hypothesis, test it, learn
2. **Know your metrics** - CAC, LTV, payback period, retention curves, viral coefficient
3. **Think in experiments** - Growth is about rapid iteration and learning
4. **Show cross-functional skills** - Growth requires product, eng, data, and marketing
5. **Focus on scalability** - What works at 100 users won't work at 1M users

### Common Mistakes to Avoid:

- ❌ Being vague about metrics - always quantify
- ❌ Ignoring unit economics - CAC and LTV matter
- ❌ Over-relying on one channel - diversify
- ❌ Forgetting about retention - acquisition without retention is a leaky bucket

### Key Growth Frameworks to Know:

- ✅ **AARRR (Pirate Metrics)** - Acquisition, Activation, Retention, Revenue, Referral
- ✅ **ICE Scoring** - Impact, Confidence, Ease
- ✅ **North Star Metric** - The one metric that matters most
- ✅ **Growth Loops** - Sustainable, compounding growth mechanisms

---

## 🎯 Ready to Practice?

Check out the [Growth_Marketing_Manager_Question_Bank.md](./Growth_Marketing_Manager_Question_Bank.md) for all questions organized by category with frameworks!

---

**Good luck with your Growth Marketing Manager interviews!** 🚀
"""
    
    output_path = os.path.join(os.path.dirname(__file__), '../INTERVIEW_FRAMEWORK.md')
    with open(output_path, 'w') as f:
        f.write(md)
    
    print(f"✅ Generated {output_path}")

def main():
    """Generate both markdown files"""
    print("🚀 Generating Growth Marketing Manager frameworks...")
    print("="*70)
    
    generate_interview_framework()
    generate_question_bank()
    
    print("="*70)
    print("✅ Growth Marketing Manager frameworks complete!")
    print("\nGenerated files:")
    print("  1. INTERVIEW_FRAMEWORK.md")
    print("  2. Growth_Marketing_Manager_Question_Bank.md")

if __name__ == "__main__":
    main()
