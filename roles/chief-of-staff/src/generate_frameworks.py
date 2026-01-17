"""
Generate Chief of Staff Interview Framework and Question Bank
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
│  ├─ Key stakeholders involved
│  └─ Why this was important
│
├─ Task
│  ├─ Your specific responsibility
│  ├─ Goals and objectives
│  └─ Constraints you faced
│
├─ Action
│  ├─ Steps you took
│  ├─ How you approached it
│  ├─ Tools/methods used
│  └─ How you collaborated
│
└─ Result
   ├─ Quantifiable outcomes
   ├─ Business/team impact
   ├─ What you learned
   └─ How you'd apply it again
""",
        "Leadership": """
Leadership
├─ Understand the need
│  ├─ Team/individual challenges
│  └─ Business context
│
├─ Set vision and direction
│  ├─ Clear goals
│  ├─ Success criteria
│  └─ Align with company objectives
│
├─ Enable and empower
│  ├─ Remove blockers
│  ├─ Provide resources
│  └─ Delegate effectively
│
├─ Motivate and inspire
│  ├─ Recognize contributions
│  ├─ Build trust
│  └─ Lead by example
│
└─ Measure and iterate
   ├─ Track progress
   ├─ Provide feedback
   └─ Adjust approach
""",
        "Communication": """
Communication
├─ Understand your audience
│  ├─ Who are they?
│  ├─ What do they care about?
│  └─ What's their context?
│
├─ Clarify your message
│  ├─ What's the key point?
│  ├─ Why does it matter?
│  └─ What action do you want?
│
├─ Choose the right medium
│  ├─ Written vs verbal
│  ├─ Formal vs informal
│  └─ 1:1 vs group
│
├─ Deliver effectively
│  ├─ Clear and concise
│  ├─ Use examples/data
│  └─ Check for understanding
│
└─ Follow up
   ├─ Confirm next steps
   ├─ Document decisions
   └─ Close the loop
""",
        "Cross-Functional Collaboration": """
Cross-Functional Collaboration
├─ Identify stakeholders
│  ├─ Who needs to be involved?
│  ├─ What are their goals?
│  └─ What are their constraints?
│
├─ Align on objectives
│  ├─ Shared goals
│  ├─ Success metrics
│  └─ Trade-offs
│
├─ Establish communication
│  ├─ Regular check-ins
│  ├─ Clear ownership
│  └─ Escalation paths
│
├─ Navigate conflicts
│  ├─ Listen actively
│  ├─ Find common ground
│  └─ Propose solutions
│
└─ Drive to outcomes
   ├─ Track progress
   ├─ Unblock teams
   └─ Celebrate wins
""",
        "Strategic Planning": """
Strategic Planning
├─ Assess current state
│  ├─ Business performance
│  ├─ Market position
│  └─ Internal capabilities
│
├─ Define vision
│  ├─ Long-term goals (3-5 years)
│  ├─ Success criteria
│  └─ Key priorities
│
├─ Identify initiatives
│  ├─ Growth opportunities
│  ├─ Efficiency improvements
│  └─ New capabilities needed
│
├─ Prioritize ruthlessly
│  ├─ Impact vs effort
│  ├─ Resource constraints
│  ├─ Dependencies
│  └─ Risk assessment
│
├─ Build roadmap
│  ├─ Milestones and timelines
│  ├─ Resource allocation
│  └─ Key metrics
│
└─ Execute and adapt
   ├─ Track progress
   ├─ Course correct
   └─ Communicate updates
""",
        "Problem Solving": """
Problem Solving
├─ Define the problem
│  ├─ What's the real issue?
│  ├─ Who's impacted?
│  └─ Why does it matter?
│
├─ Gather information
│  ├─ Data and facts
│  ├─ Stakeholder input
│  └─ Root cause analysis
│
├─ Generate solutions
│  ├─ Brainstorm options
│  ├─ Evaluate trade-offs
│  └─ Consider constraints
│
├─ Make a decision
│  ├─ Criteria for success
│  ├─ Risk assessment
│  └─ Get buy-in
│
├─ Execute
│  ├─ Action plan
│  ├─ Assign ownership
│  └─ Set timeline
│
└─ Monitor and learn
   ├─ Track outcomes
   ├─ Adjust as needed
   └─ Document learnings
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
    md = f"""# Chief of Staff Interview Question Bank

## 📚 Resources

**{total_questions} Chief of Staff questions** from [Exponent](https://www.tryexponent.com/questions?page=1&role=chief-of-staff)

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
            "Behavioral": "Can you communicate past experiences clearly using structured storytelling (STAR method)?",
            "Leadership": "Can you influence, motivate, and guide teams without direct authority?",
            "Communication": "Can you deliver feedback and communicate effectively across all levels?",
            "Cross-Functional Collaboration": "Can you work effectively with diverse teams and stakeholders?",
            "Strategic Planning": "Can you think long-term and align initiatives with business goals?",
            "Problem Solving": "Can you identify root causes and drive solutions to complex problems?"
        }
        
        md += f"🎯 **What they're really testing:**\n"
        md += f"{testing_descriptions.get(cat, 'Your ability to operate as a strategic partner to leadership.')}\n\n"
        
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
    output_path = os.path.join(os.path.dirname(__file__), '../Chief_of_Staff_Question_Bank.md')
    with open(output_path, 'w') as f:
        f.write(md)
    
    print(f"✅ Generated {output_path}")

def generate_interview_framework():
    """Generate the high-level Interview Framework"""
    
    md = """# Chief of Staff Interview Framework

## 📚 Resources

**GitHub**: [Exponent Interview Prep](https://github.com/anix-lynch/Exponent)

**Source**: [Exponent Chief of Staff Questions](https://www.tryexponent.com/questions?page=1&role=chief-of-staff)

⚠️ **Note**: Very limited dataset (only 2 questions available on Exponent)

---

## 📊 Question Distribution

- **Behavioral**: 2 questions
- **Communication**: 1 question
- **Cross-Functional Collaboration**: 1 question

**Total: 2 questions**

---

## 🎯 How to Use This Framework

1. **Identify the question type** (Behavioral, Leadership, etc.)
2. **Apply the relevant framework** (see below)
3. **Structure your answer** using the mental model

---

## 0️⃣ Core Meta-Structure

### Universal Principles for Chief of Staff Interviews

1. **Think like a CEO's right hand** - You're the strategic partner to leadership
2. **Show executive presence** - Communicate clearly, confidently, and concisely
3. **Demonstrate business acumen** - Understand the big picture and business impact
4. **Highlight influence without authority** - You lead through persuasion, not power
5. **Be the connector** - Bridge gaps between teams, functions, and leadership

### Universal Answer Framework

```
Chief of Staff Answer Structure
├─ Context
│  ├─ Business situation
│  └─ Key stakeholders
│
├─ Challenge
│  ├─ What needed to be done
│  └─ Why it mattered
│
├─ Approach
│  ├─ How you tackled it
│  ├─ Who you worked with
│  └─ What frameworks you used
│
├─ Impact
│  ├─ Quantifiable results
│  └─ Business outcomes
│
└─ Learnings
   └─ What you'd do differently
```

---

## 1️⃣ Behavioral Questions

**What they're really testing:**
Can you communicate past experiences clearly using structured storytelling?

**Framework: STAR Method**

```
Behavioral (STAR Method)
├─ Situation
│  ├─ Context and background
│  ├─ Key stakeholders involved
│  └─ Why this was important
│
├─ Task
│  ├─ Your specific responsibility
│  ├─ Goals and objectives
│  └─ Constraints you faced
│
├─ Action
│  ├─ Steps you took
│  ├─ How you approached it
│  ├─ Tools/methods used
│  └─ How you collaborated
│
└─ Result
   ├─ Quantifiable outcomes
   ├─ Business/team impact
   ├─ What you learned
   └─ How you'd apply it again
```

📌 **Key tip**: Chief of Staff roles require executive-level storytelling - be concise, focus on impact, and demonstrate strategic thinking

---

## 2️⃣ Communication

**What they're really testing:**
Can you deliver feedback and communicate effectively across all levels?

**Framework:**

```
Communication
├─ Understand your audience
│  ├─ Who are they?
│  ├─ What do they care about?
│  └─ What's their context?
│
├─ Clarify your message
│  ├─ What's the key point?
│  ├─ Why does it matter?
│  └─ What action do you want?
│
├─ Choose the right medium
│  ├─ Written vs verbal
│  ├─ Formal vs informal
│  └─ 1:1 vs group
│
├─ Deliver effectively
│  ├─ Clear and concise
│  ├─ Use examples/data
│  └─ Check for understanding
│
└─ Follow up
   ├─ Confirm next steps
   ├─ Document decisions
   └─ Close the loop
```

📌 **Key tip**: Chiefs of Staff communicate with everyone from interns to the CEO - show you can adapt your style

---

## 3️⃣ Cross-Functional Collaboration

**What they're really testing:**
Can you work effectively with diverse teams and stakeholders?

**Framework:**

```
Cross-Functional Collaboration
├─ Identify stakeholders
│  ├─ Who needs to be involved?
│  ├─ What are their goals?
│  └─ What are their constraints?
│
├─ Align on objectives
│  ├─ Shared goals
│  ├─ Success metrics
│  └─ Trade-offs
│
├─ Establish communication
│  ├─ Regular check-ins
│  ├─ Clear ownership
│  └─ Escalation paths
│
├─ Navigate conflicts
│  ├─ Listen actively
│  ├─ Find common ground
│  └─ Propose solutions
│
└─ Drive to outcomes
   ├─ Track progress
   ├─ Unblock teams
   └─ Celebrate wins
```

📌 **Key tip**: Show how you build relationships and influence without authority

---

## 4️⃣ Leadership

**What they're really testing:**
Can you influence, motivate, and guide teams without direct authority?

**Framework:**

```
Leadership
├─ Understand the need
│  ├─ Team/individual challenges
│  └─ Business context
│
├─ Set vision and direction
│  ├─ Clear goals
│  ├─ Success criteria
│  └─ Align with company objectives
│
├─ Enable and empower
│  ├─ Remove blockers
│  ├─ Provide resources
│  └─ Delegate effectively
│
├─ Motivate and inspire
│  ├─ Recognize contributions
│  ├─ Build trust
│  └─ Lead by example
│
└─ Measure and iterate
   ├─ Track progress
   ├─ Provide feedback
   └─ Adjust approach
```

📌 **Key tip**: Chiefs of Staff lead through influence - demonstrate how you get things done without direct reports

---

## 5️⃣ Strategic Planning

**What they're really testing:**
Can you think long-term and align initiatives with business goals?

**Framework:**

```
Strategic Planning
├─ Assess current state
│  ├─ Business performance
│  ├─ Market position
│  └─ Internal capabilities
│
├─ Define vision
│  ├─ Long-term goals (3-5 years)
│  ├─ Success criteria
│  └─ Key priorities
│
├─ Identify initiatives
│  ├─ Growth opportunities
│  ├─ Efficiency improvements
│  └─ New capabilities needed
│
├─ Prioritize ruthlessly
│  ├─ Impact vs effort
│  ├─ Resource constraints
│  ├─ Dependencies
│  └─ Risk assessment
│
├─ Build roadmap
│  ├─ Milestones and timelines
│  ├─ Resource allocation
│  └─ Key metrics
│
└─ Execute and adapt
   ├─ Track progress
   ├─ Course correct
   └─ Communicate updates
```

📌 **Key tip**: Show you can translate CEO vision into executable plans

---

## 6️⃣ Problem Solving

**What they're really testing:**
Can you identify root causes and drive solutions to complex problems?

**Framework:**

```
Problem Solving
├─ Define the problem
│  ├─ What's the real issue?
│  ├─ Who's impacted?
│  └─ Why does it matter?
│
├─ Gather information
│  ├─ Data and facts
│  ├─ Stakeholder input
│  └─ Root cause analysis
│
├─ Generate solutions
│  ├─ Brainstorm options
│  ├─ Evaluate trade-offs
│  └─ Consider constraints
│
├─ Make a decision
│  ├─ Criteria for success
│  ├─ Risk assessment
│  └─ Get buy-in
│
├─ Execute
│  ├─ Action plan
│  ├─ Assign ownership
│  └─ Set timeline
│
└─ Monitor and learn
   ├─ Track outcomes
   ├─ Adjust as needed
   └─ Document learnings
```

📌 **Key tip**: Chiefs of Staff solve the CEO's hardest problems - show structured thinking and business judgment

---

## 💡 Final Tips

### For All Chief of Staff Interviews:

1. **Think like an owner** - Show you care about the business, not just your function
2. **Be a force multiplier** - Demonstrate how you amplify the CEO's impact
3. **Show executive judgment** - Make decisions with incomplete information
4. **Communicate like a leader** - Clear, concise, and action-oriented
5. **Build trust quickly** - You'll work with everyone from interns to the board

### Common Mistakes to Avoid:

- ❌ Being too tactical - Chiefs of Staff are strategic partners
- ❌ Waiting for permission - Show initiative and ownership
- ❌ Ignoring stakeholders - This role is all about relationships
- ❌ Overcomplicating - Executives value clarity and simplicity

### What Makes a Great Chief of Staff:

- ✅ **Strategic thinker** - See the big picture
- ✅ **Excellent communicator** - Bridge gaps between teams
- ✅ **Trusted advisor** - Build relationships at all levels
- ✅ **Execution-focused** - Turn strategy into results
- ✅ **Adaptable** - Wear many hats and context-switch quickly

---

## 🎯 Ready to Practice?

Check out the [Chief_of_Staff_Question_Bank.md](./Chief_of_Staff_Question_Bank.md) for all questions organized by category with frameworks!

---

**Good luck with your Chief of Staff interviews!** 🚀
"""
    
    output_path = os.path.join(os.path.dirname(__file__), '../INTERVIEW_FRAMEWORK.md')
    with open(output_path, 'w') as f:
        f.write(md)
    
    print(f"✅ Generated {output_path}")

def main():
    """Generate both markdown files"""
    print("🚀 Generating Chief of Staff frameworks...")
    print("="*70)
    
    generate_interview_framework()
    generate_question_bank()
    
    print("="*70)
    print("✅ Chief of Staff frameworks complete!")
    print("\nGenerated files:")
    print("  1. INTERVIEW_FRAMEWORK.md")
    print("  2. Chief_of_Staff_Question_Bank.md")

if __name__ == "__main__":
    main()
