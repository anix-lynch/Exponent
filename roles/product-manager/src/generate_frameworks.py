"""
Generate mental model frameworks for each category
"""
import json
import os

FRAMEWORKS = {
    "Data Analysis": """
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
""",

    "SQL": """
SQL
├─ Understand requirements
│  ├─ What output format?
│  ├─ Aggregation needed?
│  └─ Filters/conditions?
│
├─ Identify tables & joins
│  ├─ Which tables?
│  ├─ Join keys
│  └─ Join type (INNER/LEFT/etc)
│
├─ Write query structure
│  ├─ SELECT (what columns)
│  ├─ FROM & JOIN
│  ├─ WHERE (filters)
│  ├─ GROUP BY (aggregation)
│  ├─ HAVING (post-agg filter)
│  └─ ORDER BY + LIMIT
│
├─ Optimize
│  ├─ Use indexes
│  ├─ Avoid subqueries if possible
│  └─ Window functions for ranking
│
└─ Validate
   ├─ Check edge cases
   ├─ NULL handling
   └─ Test with sample data
""",

    "Coding": """
Coding
├─ Clarify requirements
│  ├─ Input format
│  ├─ Output format
│  └─ Constraints
│
├─ Think through approach
│  ├─ Brute force first
│  ├─ Optimize
│  └─ Edge cases
│
├─ Write pseudocode
│  ├─ Break into steps
│  └─ Identify data structures
│
├─ Implement
│  ├─ Start simple
│  ├─ Test as you go
│  └─ Handle edge cases
│
└─ Analyze complexity
   ├─ Time: O(?)
   └─ Space: O(?)
""",

    "Behavioral": """
Behavioral (STAR Method)
├─ Situation
│  ├─ Context
│  ├─ Challenge
│  └─ Stakeholders
│
├─ Task
│  ├─ Your role
│  ├─ Goal
│  └─ Constraints
│
├─ Action
│  ├─ What YOU did
│  ├─ Why that approach
│  └─ How you executed
│
└─ Result
   ├─ Outcome (quantify!)
   ├─ Impact
   └─ Learnings
""",

    "Analytical": """
Analytical
├─ Define the problem
│  ├─ What changed?
│  ├─ When?
│  └─ How much?
│
├─ Form hypotheses
│  ├─ Internal causes
│  ├─ External causes
│  └─ User behavior
│
├─ Gather evidence
│  ├─ Segment data
│  ├─ Compare periods
│  └─ Look for patterns
│
├─ Test hypotheses
│  ├─ Validate with data
│  ├─ Rule out alternatives
│  └─ Identify root cause
│
└─ Recommend solution
   ├─ Fix the issue
   ├─ Prevent recurrence
   └─ Monitor going forward
""",

    "Product Strategy": """
Product Strategy
├─ Understand goal
│  ├─ Company objective
│  ├─ User need
│  └─ Market opportunity
│
├─ Assess landscape
│  ├─ Competitors
│  ├─ Market trends
│  └─ User behavior
│
├─ Evaluate options
│  ├─ Build vs buy
│  ├─ Prioritization
│  └─ Tradeoffs
│
├─ Define success
│  ├─ North star metric
│  ├─ Supporting metrics
│  └─ Timeline
│
└─ Make recommendation
   ├─ Why this option
   ├─ Expected impact
   └─ Risks & mitigation
""",

    "Estimation": """
Estimation
├─ Clarify scope
│  ├─ Geography
│  ├─ Time period
│  └─ Target segment
│
├─ Break down problem
│  ├─ Top-down approach
│  └─ Bottom-up approach
│
├─ Make assumptions
│  ├─ State clearly
│  ├─ Use round numbers
│  └─ Be reasonable
│
├─ Calculate step by step
│  ├─ Show your work
│  ├─ Explain logic
│  └─ Adjust as needed
│
└─ Sanity check
   ├─ Does it make sense?
   ├─ Compare to known data
   └─ Sensitivity analysis
""",

    "Product Design": """
Product Design
├─ Understand user problem
│  ├─ Who is the user?
│  ├─ What's the pain point?
│  └─ Why does it matter?
│
├─ Define success
│  ├─ User value
│  ├─ Business value
│  └─ Key metrics
│
├─ Ideate solutions
│  ├─ Brainstorm features
│  ├─ Consider alternatives
│  └─ Prioritize
│
├─ Design experience
│  ├─ User journey
│  ├─ Key interactions
│  └─ Edge cases
│
└─ Measure & iterate
   ├─ Launch metrics
   ├─ User feedback
   └─ Continuous improvement
""",

    "Statistics & Experimentation": """
Statistics & Experimentation
├─ Define hypothesis
│  ├─ What are we testing?
│  ├─ Expected outcome
│  └─ Success criteria
│
├─ Design experiment
│  ├─ Control vs treatment
│  ├─ Sample size
│  ├─ Duration
│  └─ Randomization
│
├─ Choose metrics
│  ├─ Primary metric
│  ├─ Secondary metrics
│  └─ Guardrail metrics
│
├─ Analyze results
│  ├─ Statistical significance
│  ├─ Practical significance
│  └─ Confidence interval
│
└─ Make decision
   ├─ Ship or don't ship
   ├─ Why?
   └─ Next steps
""",

    "Cross-Functional": """
Cross-Functional
├─ Understand partner goals
│  ├─ What do they care about?
│  ├─ Their constraints
│  └─ Their language
│
├─ Translate data to context
│  ├─ Simplify technical details
│  ├─ Use analogies
│  └─ Visual aids
│
├─ Align on metrics
│  ├─ Shared KPIs
│  ├─ Trade-offs
│  └─ Success criteria
│
├─ Manage expectations
│  ├─ What's possible
│  ├─ Timeline
│  └─ Limitations
│
└─ Communicate clearly
   ├─ Executive summary
   ├─ Key insights
   └─ Actionable recommendations
""",

    "Execution": """
Execution
├─ Prioritize tasks
│  ├─ Impact vs effort
│  ├─ Dependencies
│  └─ Urgency
│
├─ Break into actions
│  ├─ Concrete steps
│  ├─ Owners
│  └─ Timeline
│
├─ Deliver incrementally
│  ├─ Quick wins
│  ├─ Iterate
│  └─ Show progress
│
├─ Adapt to changes
│  ├─ New information
│  ├─ Blockers
│  └─ Pivot if needed
│
└─ Close the loop
   ├─ Results
   ├─ Learnings
   └─ Next steps
""",

    "Project Management": """
Project Management
├─ Define objective
│  ├─ Business goal
│  ├─ Success criteria
│  └─ Stakeholders
│
├─ Scope work
│  ├─ Must-haves
│  ├─ Nice-to-haves
│  └─ Out of scope
│
├─ Plan execution
│  ├─ Timeline
│  ├─ Resources
│  └─ Milestones
│
├─ Manage risks
│  ├─ Dependencies
│  ├─ Blockers
│  └─ Mitigation plan
│
└─ Communicate status
   ├─ Regular updates
   ├─ Escalations
   └─ Lessons learned
""",

    "System Design": """
System Design
├─ Define use case
│  ├─ What problem?
│  ├─ Scale requirements
│  └─ Constraints
│
├─ Identify data sources
│  ├─ Where does data come from?
│  ├─ Format
│  └─ Volume
│
├─ Data flow
│  ├─ Ingest (how data enters)
│  ├─ Store (database/warehouse)
│  ├─ Transform (ETL/ELT)
│  └─ Serve (APIs/dashboards)
│
├─ Scalability considerations
│  ├─ Can it handle growth?
│  ├─ Performance
│  └─ Reliability
│
└─ Tradeoffs
   ├─ Cost
   ├─ Complexity
   └─ Maintenance
""",

    "Customer Interaction": """
Customer Interaction
├─ Understand customer need
│  ├─ What are they asking?
│  ├─ Why do they need it?
│  └─ Context
│
├─ Ask clarifying questions
│  ├─ Scope
│  ├─ Timeline
│  └─ Format
│
├─ Present insights simply
│  ├─ Non-technical language
│  ├─ Visual aids
│  └─ Key takeaways
│
├─ Handle feedback
│  ├─ Listen actively
│  ├─ Address concerns
│  └─ Iterate
│
└─ Drive action
   ├─ Clear recommendations
   ├─ Next steps
   └─ Follow-up
""",

    "Data Pipeline Design": """
Data Pipeline Design
├─ Data sources
│  ├─ Where is data?
│  ├─ Format (JSON, CSV, DB)
│  └─ Update frequency
│
├─ Ingestion
│  ├─ Batch vs streaming
│  ├─ API vs file upload
│  └─ Error handling
│
├─ Transformation
│  ├─ Clean
│  ├─ Enrich
│  └─ Aggregate
│
├─ Storage
│  ├─ Data warehouse
│  ├─ Data lake
│  └─ Schema design
│
└─ Consumption
   ├─ Dashboards
   ├─ Reports
   └─ ML models
""",

    "Data Modeling": """
Data Modeling
├─ Identify entities
│  ├─ What objects?
│  ├─ Attributes
│  └─ Business rules
│
├─ Define relationships
│  ├─ One-to-one
│  ├─ One-to-many
│  └─ Many-to-many
│
├─ Keys
│  ├─ Primary key
│  ├─ Foreign key
│  └─ Composite key
│
├─ Granularity
│  ├─ Level of detail
│  ├─ Aggregation
│  └─ Time dimension
│
└─ Use cases
   ├─ Queries to support
   ├─ Performance
   └─ Maintainability
""",

    "Concept": """
Concept
├─ Define the term
│  ├─ What is it?
│  ├─ Core purpose
│  └─ When to use
│
├─ Key characteristics
│  ├─ Properties
│  ├─ Constraints
│  └─ Behavior
│
├─ Compare & contrast
│  ├─ Similar concepts
│  ├─ Differences
│  └─ Tradeoffs
│
├─ Real-world example
│  ├─ Use case
│  ├─ Benefits
│  └─ Limitations
│
└─ Best practices
   ├─ When to use
   ├─ When NOT to use
   └─ Common pitfalls
""",

    "Artificial Intelligence": """
Artificial Intelligence
├─ Problem suitability
│  ├─ Is AI needed?
│  ├─ Alternative approaches
│  └─ Expected benefit
│
├─ Data requirements
│  ├─ Volume
│  ├─ Quality
│  └─ Labels
│
├─ Model output usage
│  ├─ How will it be used?
│  ├─ Real-time vs batch
│  └─ Accuracy requirements
│
├─ Risks
│  ├─ Bias
│  ├─ Errors (false positives/negatives)
│  └─ Explainability
│
└─ Business impact
   ├─ Value created
   ├─ Cost
   └─ Maintenance
""",

    "Machine Learning": """
Machine Learning
├─ Define prediction task
│  ├─ Classification
│  ├─ Regression
│  └─ Clustering
│
├─ Features
│  ├─ What inputs?
│  ├─ Feature engineering
│  └─ Feature selection
│
├─ Labels
│  ├─ What are we predicting?
│  ├─ How to get labels
│  └─ Label quality
│
├─ Evaluation metrics
│  ├─ Accuracy, precision, recall
│  ├─ Business metric
│  └─ Baseline comparison
│
└─ Limitations
   ├─ Data limitations
   ├─ Model limitations
   └─ Deployment considerations
""",

    "Technical": """
Technical
├─ Understand the concept
│  ├─ What is it?
│  ├─ How does it work?
│  └─ Why is it used?
│
├─ Key components
│  ├─ Architecture
│  ├─ Dependencies
│  └─ Configuration
│
├─ Implementation
│  ├─ Setup
│  ├─ Code structure
│  └─ Testing
│
├─ Optimization
│  ├─ Performance
│  ├─ Scalability
│  └─ Maintainability
│
└─ Troubleshooting
   ├─ Common issues
   ├─ Debugging approach
   └─ Best practices
""",

    "Data Structures & Algorithms": """
Data Structures & Algorithms
├─ Understand problem
│  ├─ Input/output
│  ├─ Constraints
│  └─ Edge cases
│
├─ Choose data structure
│  ├─ Array, list, set
│  ├─ Hash map, tree
│  └─ Stack, queue
│
├─ Design algorithm
│  ├─ Brute force
│  ├─ Optimize
│  └─ Pseudocode
│
├─ Implement
│  ├─ Write code
│  ├─ Test
│  └─ Handle edge cases
│
└─ Analyze complexity
   ├─ Time: O(?)
   ├─ Space: O(?)
   └─ Can we do better?
"""
}

def generate_category_summary(category, questions):
    """Generate summary for a category with ALL questions"""
    framework = FRAMEWORKS.get(category, "Framework not defined")
    
    summary = f"""
{'='*80}
{category.upper()}
{'='*80}

📊 Total Questions: {len(questions)}

🎯 What they're really testing:
{get_testing_description(category)}

🗺️  Mental Model Framework:
```
{framework}
```

📝 All {len(questions)} Questions:

"""
    
    # Add ALL questions
    for i, q in enumerate(questions, 1):
        summary += f"{i}. {q['question']}\n"
    
    summary += "\n"
    return summary

def get_testing_description(category):
    """Get what interviewers are really testing for each category"""
    descriptions = {
        "Data Analysis": "Can you extract insights from data and drive business decisions?",
        "SQL": "Can you write efficient queries to extract and manipulate data?",
        "Coding": "Can you write clean, efficient code to solve problems?",
        "Behavioral": "Do you have relevant experience and learn from it?",
        "Analytical": "Can you break down complex problems and find root causes?",
        "Product Strategy": "Do you understand business strategy and market dynamics?",
        "Estimation": "Can you make reasonable assumptions and think quantitatively?",
        "Product Design": "Do you think from the user's perspective?",
        "Statistics & Experimentation": "Do you understand how to design and analyze experiments?",
        "Cross-Functional": "Can you work effectively with non-analysts?",
        "Execution": "Can you turn plans into results?",
        "Project Management": "Can you plan, prioritize, and deliver with constraints?",
        "System Design": "Do you understand data systems at a high level?",
        "Customer Interaction": "Can you represent data insights to external users?",
        "Data Pipeline Design": "Do you understand how data moves end to end?",
        "Data Modeling": "Can you structure data correctly?",
        "Concept": "Do you understand fundamental concepts?",
        "Artificial Intelligence": "Do you understand AI at a practical level (not just theory)?",
        "Machine Learning": "Do you understand ML workflows and evaluation?",
        "Technical": "Do you have the technical depth needed?",
        "Data Structures & Algorithms": "Can you solve algorithmic problems efficiently?",
    }
    return descriptions.get(category, "General problem-solving ability")

def main():
    # Load categorized questions
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    input_file = os.path.join(data_dir, 'questions_by_category.json')
    
    with open(input_file, 'r') as f:
        by_category = json.load(f)
    
    # Generate master framework document
    output = """
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║           DATA ANALYST INTERVIEW PREPARATION FRAMEWORK                         ║
║           Mental Models & Complete Question Bank                               ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

This framework provides mental models for approaching each type of data analyst
interview question. Focus on understanding the PATTERN and FRAMEWORK, not 
memorizing answers.

Total Questions: 118 across 20 categories

"""
    
    # Categories in order of importance (by question count)
    category_order = [
        "Data Analysis",
        "Analytical", 
        "SQL",
        "Coding",
        "Product Strategy",
        "Product Design",
        "Artificial Intelligence",
        "Behavioral",
        "Execution",
        "Cross-Functional",
        "Project Management",
        "Customer Interaction",
        "Concept",
        "Technical",
        "Statistics & Experimentation",
        "Estimation",
        "Data Structures & Algorithms",
        "Data Modeling",
        "System Design",
        "Data Pipeline Design"
    ]
    
    # Generate summary for each category with questions
    for category in category_order:
        if category in by_category and len(by_category[category]) > 0:
            output += generate_category_summary(category, by_category[category])
    
    # Save to file
    output_file = os.path.join(data_dir, 'frameworks_master.txt')
    with open(output_file, 'w') as f:
        f.write(output)
    
    print(f"✅ Generated mental model frameworks with ALL questions")
    print(f"📄 Saved to: {output_file}")
    print(f"\n🎯 Frameworks created for {len(category_order)} categories")
    print(f"📊 Total questions: 118")

if __name__ == "__main__":
    main()
