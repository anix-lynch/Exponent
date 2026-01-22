# Executive Study Plan: L10 - Process Optimization
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~15 questions → 2 concept buckets → 2 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY L10 (PROCESS OPTIMIZATION) QUESTIONS

**Even when "process optimization" isn't mentioned, look for these keywords/phrases:**

### Explicit Process Keywords:
- "process optimization", "process improvement", "workflow", "bottleneck", "optimize process"
- "queue", "wait time", "cycle time", "throughput", "efficiency", "streamline"
- "how would you improve", "how would you optimize", "fix slow process"

### Implicit L10 Indicators:
- **Process questions:** "How would you optimize X process?", "How do you improve workflow?", "What's the bottleneck?"
- **Queue questions:** "Long queue", "wait time", "how to reduce wait", "capacity issues"
- **Efficiency questions:** "How to improve efficiency?", "Streamline process", "Reduce cycle time"
- **Workflow questions:** "Design workflow", "Map process", "Define flow"

### L10 vs P12 Distinction:
- **L10 (Process Optimization):** "How would you optimize a process?" → Focus: Map workflow, identify bottlenecks, optimize
- **P12 (Operational Excellence):** "How do you ensure system reliability?" → Focus: Operational process, reliability

### L10 vs L2 Distinction:
- **L10 (Process Optimization):** "How would you optimize a process?" → Focus: Process bottlenecks, workflow optimization
- **L2 (Scale & Capacity):** "What breaks if traffic grows 10x?" → Focus: System bottlenecks, technical scaling

### Red Flags (NOT L10):
- "What breaks if traffic grows 10x?" → L2 (Scale & Capacity)
- "How do you ensure system reliability?" → P12 (Operational Excellence)
- "How do you monitor a system?" → L5 (Observability)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Process Optimization Framework** (HIGHEST PRIORITY)
2. ✅ **Workflow Design** (HIGH PRIORITY)

**For Data Engineer:**
1. ✅ **Process Optimization Framework** (HIGHEST) - Core framework
2. ✅ **Workflow Design** (HIGH) - Practical application

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Process Optimization Framework
**Questions:** ~10 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "How would you optimize X process?" or "What's the bottleneck?" - core process optimization framework
- **Framework:** Map Workflow → Identify Bottlenecks → Optimize → Measure
- **Map Workflow:** Document current process end-to-end (Identify all steps: from start to finish, map every stage, Sequence: order of operations, dependencies between steps, Stakeholders: who is involved at each step, Time: how long each step takes, total cycle time, Handoffs: where work transfers between people/systems, Create visual flow: step 1 → step 2 → step 3 → completion)
- **Identify Bottlenecks:** Find where process slows down (Time analysis: which step takes longest?, Wait time: where is work waiting - queues, approvals, dependencies?, Resource constraints: limited capacity, single-threaded steps, Rework: steps that require repetition, errors, corrections, Manual steps: human-dependent processes that could be automated, Dependencies: steps blocked by other processes or approvals, Focus on: highest time impact, most frequent delays, biggest pain points)
- **Optimize:** Design improvements to eliminate bottlenecks (Increase capacity: add resources, parallel processing, Reduce demand: batch processing, off-peak scheduling, Optimize flow: reduce wait time, improve routing, Eliminate waste: remove unnecessary steps, streamline, Prioritize: focus on highest-impact bottlenecks first)
- **Measure:** Track impact of optimizations (Before metrics: baseline cycle time, throughput, error rate, After metrics: improved cycle time, throughput, error rate, Key metrics: time saved, capacity increase, quality improvement, Continuous monitoring: track metrics over time, identify new bottlenecks, Iterate: if optimization didn't work, try different approach, Document learnings: what worked, what didn't, why)

**Concrete Examples:**
- "Amusement park queue: Map workflow (Enter → Wait → Ride → Exit), Bottlenecks (Wait time - long queue, single ride capacity), Optimize (Increase capacity - more rides, Reduce demand - off-peak scheduling, Optimize flow - better queue management), Measure (Wait time, throughput, satisfaction)"
- "Process optimization: Map workflow, identify bottlenecks, optimize, measure impact"

**Representative Questions (Do 5 only):**
- Q24: An amusement park has a ride with a long queue that is a growing concern. How would you address this issue? (queue/bottleneck angle)
- Q76: As a PM, how would you name conference rooms for a new office so newcomers can easily navigate? (wayfinding/process design angle)
- Q147: Can you explain the Agile methodology and its key principles? (methodology/process angle)
- Q182: Debug a build/CI system for a particular scenario or slow builds. (CI/CD optimization angle)
- Q196: Define the flow from order booking to delivery, including installation, for a customized drinking water purifier. (process definition angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When optimizing a process, I use Map Workflow → Identify Bottlenecks → Optimize → Measure. First, I Map Workflow: Document current process end-to-end. Identify all steps (From start to finish, map every stage - what happens at each step?), Sequence (Order of operations, dependencies between steps - what must happen before what?), Stakeholders (Who is involved at each step - who does what?), Time (How long each step takes, total cycle time - where does time go?), Handoffs (Where work transfers between people/systems - where are the handoffs?). Create a visual flow: step 1 → step 2 → step 3 → completion. Second, I Identify Bottlenecks: Find where process slows down. Time analysis (Which step takes longest? Where is most time spent?), Wait time (Where is work waiting? Queues, approvals, dependencies - where does work get stuck?), Resource constraints (Limited capacity, single-threaded steps - what's the constraint?), Rework (Steps that require repetition, errors, corrections - where do we redo work?), Manual steps (Human-dependent processes that could be automated - where is manual work?), Dependencies (Steps blocked by other processes or approvals - what blocks progress?). Focus on: highest time impact, most frequent delays, biggest pain points. Third, I Optimize: Design improvements to eliminate bottlenecks. Increase capacity (Add resources, parallel processing - can we do more?), Reduce demand (Batch processing, off-peak scheduling - can we reduce load?), Optimize flow (Reduce wait time, improve routing - can we flow faster?), Eliminate waste (Remove unnecessary steps, streamline - can we remove steps?), Prioritize (Focus on highest-impact bottlenecks first - what moves the needle most?). Finally, I Measure: Track impact of optimizations. Before metrics (Baseline cycle time, throughput, error rate - what was it before?), After metrics (Improved cycle time, throughput, error rate - what is it after?), Key metrics (Time saved, capacity increase, quality improvement - what improved?), Continuous monitoring (Track metrics over time, identify new bottlenecks - are we maintaining improvement?), Iterate (If optimization didn't work, try different approach - what did we learn?), Document learnings (What worked, what didn't, why - what can we apply next time?)."

**How to Adapt This Narrative for Each Question:**

- **Q24 (Amusement park queue):** Focus on queue bottleneck → "To address a long queue at an amusement park ride, I'd: Map Workflow (Steps: Enter park → Walk to ride → Join queue → Wait in queue → Board ride → Ride → Exit, Sequence: Must wait in queue before boarding, Stakeholders: Visitors, ride operators, Time: Queue wait time is longest step, Handoffs: Queue to ride operators), Identify Bottlenecks (Time analysis: Queue wait time is longest step - 30+ minutes, Wait time: Visitors waiting in queue, Resource constraints: Single ride, limited capacity per cycle, Rework: None, Manual steps: Manual boarding, Dependencies: Must wait for previous cycle to finish, Focus: Queue wait time is the bottleneck - highest time impact, biggest pain point), Optimize (Increase capacity: Add more rides, increase ride capacity, parallel processing, Reduce demand: Off-peak scheduling, reservations, timed entry, Optimize flow: Better queue management, virtual queue, express passes, Eliminate waste: Remove unnecessary steps, streamline boarding, Prioritize: Focus on queue wait time - highest impact), Measure (Before metrics: Average wait time 30+ min, throughput X riders/hour, satisfaction low, After metrics: Target wait time < 10 min, increased throughput, higher satisfaction, Key metrics: Time saved per visitor, capacity increase, satisfaction improvement, Continuous monitoring: Track wait times, identify new bottlenecks, Iterate: If virtual queue works, expand, if not, try other approaches, Document learnings: What worked - virtual queue, what didn't - express passes caused issues, why). I'd prioritize: Virtual queue system (Visitors get time slot, can do other things, reduces perceived wait), Increase capacity (Add more rides if possible, increase ride capacity), Optimize flow (Better queue routing, faster boarding process)."

- **Q182 (CI/CD slow builds):** Emphasize build optimization → "To debug and optimize slow CI/CD builds, I'd: Map Workflow (Steps: Code commit → Trigger build → Install dependencies → Run tests → Build artifacts → Deploy, Sequence: Sequential steps, dependencies, Stakeholders: Developers, CI system, Time: Each step takes time, total build time, Handoffs: Code to CI system, CI to deployment), Identify Bottlenecks (Time analysis: Which step takes longest? Tests? Build? Dependencies?, Wait time: Where is work waiting? Queue for CI runners?, Resource constraints: Limited CI runners, single-threaded steps, Rework: Failed builds require re-running, Manual steps: Manual deployments?, Dependencies: Steps blocked by other processes, Focus: Longest step, most frequent delays), Optimize (Increase capacity: More CI runners, parallel test execution, Reduce demand: Batch builds, off-peak scheduling, Optimize flow: Cache dependencies, parallel steps, Eliminate waste: Remove unnecessary steps, skip tests when possible, Prioritize: Focus on longest step first), Measure (Before metrics: Build time 30 min, throughput X builds/hour, error rate, After metrics: Target build time < 5 min, increased throughput, lower error rate, Key metrics: Time saved, capacity increase, quality improvement, Continuous monitoring: Track build times, identify new bottlenecks, Iterate: If caching works, expand, if not, try other approaches, Document learnings: What worked, what didn't, why). I'd prioritize: Parallel test execution (Run tests in parallel, reduce test time), Cache dependencies (Cache npm/pip packages, reduce install time), Optimize slowest step (Identify and optimize the longest step)."

---

### BUCKET 2: Workflow Design
**Questions:** ~5 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Design workflow for X" or "Define flow for X" - same framework, with focus on workflow design
- **Approach:** Same process optimization framework, with focus on designing new workflows
- **Workflow Design:** Map desired workflow, Identify potential bottlenecks, Design to avoid bottlenecks, Measure and iterate
- **Design Principles:** Clear steps, Efficient flow, Minimal handoffs, Automated where possible

**Concrete Examples:**
- "Order-to-delivery workflow: Map (Order → Payment → Manufacturing → Shipping → Delivery → Installation), Bottlenecks (Manufacturing time, shipping delays), Design (Optimize manufacturing, faster shipping, clear communication), Measure (Cycle time, customer satisfaction)"
- "Workflow design: Map desired flow, identify potential bottlenecks, design to avoid them, measure and iterate"

**Representative Questions (Do 5 only):**
- Q196: Define the flow from order booking to delivery, including installation, for a customized drinking water purifier. (workflow design angle)
- Q76: As a PM, how would you name conference rooms for a new office so newcomers can easily navigate? (wayfinding/workflow design angle)
- Q24: An amusement park has a ride with a long queue that is a growing concern. How would you address this issue? (workflow optimization angle)
- Q182: Debug a build/CI system for a particular scenario or slow builds. (workflow optimization angle)
- Q147: Can you explain the Agile methodology and its key principles? (methodology/workflow angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**
> "When designing workflows, I use the same process optimization framework but focus on designing new workflows. I Map Desired Workflow: Define the ideal process (Steps: What should happen?, Sequence: What order?, Stakeholders: Who's involved?, Time: How long should it take?, Handoffs: Where are transfers?). I Identify Potential Bottlenecks: Anticipate where issues might occur (Time: Which steps might be slow?, Wait time: Where might work wait?, Resource constraints: What might be limited?, Dependencies: What might block progress?). I Design to Avoid Bottlenecks: Build in optimizations from start (Increase capacity: Design for scale, Reduce demand: Design for efficiency, Optimize flow: Design for speed, Eliminate waste: Design for simplicity). I Measure and Iterate: Track and improve (Before: Baseline, After: Improved, Monitor: Continuous, Iterate: Learn and improve). The key is designing for efficiency from the start."

**How to Adapt This Narrative for Each Question:**

- **Q196 (Order-to-delivery flow):** Focus on workflow design → "To define the flow from order booking to delivery for a water purifier, I'd: Map Desired Workflow (Steps: Order booking → Payment → Manufacturing → Quality check → Shipping → Delivery → Installation → Service, Sequence: Must complete each step before next, Stakeholders: Customer, sales, manufacturing, shipping, installation, service, Time: Total cycle time, Handoffs: Order to manufacturing, manufacturing to shipping, shipping to installation), Identify Potential Bottlenecks (Time: Manufacturing might be slow, Wait time: Waiting for parts, approvals, Resource constraints: Limited manufacturing capacity, single installation team, Dependencies: Parts availability, shipping schedules, Focus: Manufacturing time, installation scheduling), Design to Avoid Bottlenecks (Increase capacity: Multiple manufacturing lines, parallel installation teams, Reduce demand: Batch manufacturing, scheduled installations, Optimize flow: Pre-order parts, optimize routing, Eliminate waste: Streamline steps, reduce handoffs, Prioritize: Focus on manufacturing and installation - longest steps), Measure (Before metrics: Cycle time X days, customer satisfaction, After metrics: Target cycle time Y days, higher satisfaction, Key metrics: Time saved, capacity increase, satisfaction improvement, Continuous monitoring: Track cycle time, identify new bottlenecks, Iterate: If pre-ordering works, expand, if not, try other approaches, Document learnings: What worked, what didn't, why). I'd design: Order booking (Online/phone, immediate confirmation), Payment (Multiple options, instant processing), Manufacturing (Pre-order parts, optimize production, quality check), Shipping (Fast shipping, tracking, communication), Delivery (Scheduled delivery, clear communication), Installation (Scheduled installation, trained technicians, quick setup), Service (Follow-up, warranty, support)."

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Process Optimization Framework** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Workflow Design** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through process optimization framework in 2 minutes (Map Workflow → Identify Bottlenecks → Optimize → Measure)
- [ ] Map workflow (Steps, sequence, stakeholders, time, handoffs)
- [ ] Identify bottlenecks (Time, wait time, resource constraints, rework, manual steps, dependencies)
- [ ] Optimize (Increase capacity, reduce demand, optimize flow, eliminate waste)
- [ ] Measure (Before/after metrics, continuous monitoring, iterate)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the process optimization framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Map Workflow → Identify Bottlenecks → Optimize → Measure framework**, not memorizing answers

**Remember:** L10 is about process optimization. The framework: Map Workflow → Identify Bottlenecks → Optimize → Measure. Key principle: Focus on highest-impact bottlenecks first. Measure and iterate continuously.
