# Executive Study Plan: P13B - Design Travel/Transportation Platforms
**Approach:** GM-style, concept-level, not per-question  
**Time:** 2-3 hours total across 3 passes  
**Source:** ~25 questions → 3 concept buckets → 2-3 high-impact buckets

**❤️ = "Hedgehog Answer"** - Your fallback narrative if you know nothing. Master these first!

---

## 🔍 HOW TO IDENTIFY P13B_TRAVEL (DESIGN TRAVEL/TRANSPORTATION PLATFORMS) QUESTIONS

**Even when "travel" or "transportation" isn't mentioned, look for these keywords/phrases:**

### Explicit Travel Keywords:
- "travel", "transportation", "navigation", "maps", "parking", "trip planning"
- "Google Maps", "Uber", "Lyft", "travel app", "navigation app"
- "route", "directions", "commute", "parking", "airport", "trip"

### Implicit P13B_TRAVEL Indicators:
- **Travel focus:** "Design a travel app", "Design for Google Maps", "Design navigation"
- **Transportation focus:** "Design parking solution", "Design transportation app", "Design commute app"
- **Trip planning:** "Design trip planning", "Design for travelers", "Design travel experience"
- **Location-based:** "Design location-based", "Design mapping", "Design navigation"

### P13B_TRAVEL vs P13B_CONTENT Distinction:
- **P13B_TRAVEL (Travel/Transportation):** "Design a travel app" → Focus: Trip planning, navigation, transportation
- **P13B_CONTENT (Content/Media):** "Design a video streaming app" → Focus: Content consumption, discovery

### P13B_TRAVEL vs P13D Distinction:
- **P13B_TRAVEL (Travel/Transportation):** "Design a travel app" → Focus: Single-sided platform, user journey
- **P13D (Marketplace):** "Design a bike-sharing system" → Focus: Two-sided platform, supply/demand

### Red Flags (NOT P13B_TRAVEL):
- "Design a bike-sharing system" → P13D (Marketplace) - if two-sided
- "Design a video streaming app" → P13B_CONTENT (Content/Media)
- "Design a social media app" → P13B_SOCIAL (Social/Community)

---

## 🎯 EXECUTIVE SCOPE (15-20 min)

### Your 2-3 High-Impact Buckets (Pick Based on Role)

**For Product Manager:**
1. ✅ **Travel Platform Design** (HIGHEST PRIORITY)
2. ✅ **Navigation & Trip Planning** (HIGH PRIORITY)
3. ⚠️ **Transportation Features** (MEDIUM)

**For Data Engineer:**
1. ✅ **Travel Platform Design** (HIGHEST) - Understand location systems, mapping, routing
2. ✅ **Navigation & Trip Planning** (HIGH) - Technical implementation, algorithms
3. ⚠️ **Transportation Features** (MEDIUM) - Real-time data, integration

---

## 📊 CONCEPT BUCKET BREAKDOWN

### BUCKET 1: Travel Platform Design
**Questions:** ~15 | **Priority:** 🟢 GREEN (Master this)

**Board Slide Bullets:**
- **What:** "Design a travel app" or "Design for Google Maps" - core travel platform framework
- **Framework:** Users → Jobs → Core Loop → Key Features → Tradeoffs → Success Metrics
- **Users:** Who are the users? (Travelers, Commuters, Transportation providers), What are their needs? (Trip planning, Navigation, Transportation options)
- **Jobs:** What jobs do users need done? (Plan trips, Navigate routes, Book transportation, Find parking), Job priority (Frequency, Urgency)
- **Core Loop:** What is the engagement loop? (Plan trip → Navigate/use service → Complete trip → Return for next trip), How does it drive retention? (Regular commutes, Trip planning habits)
- **Key Features:** Core features (Maps/navigation, Route planning, Transportation booking, Parking), Supporting features (Search, Reviews, Real-time updates, Offline mode)
- **Tradeoffs:** Accuracy vs speed, Real-time vs offline, Features vs simplicity
- **Success Metrics:** Usage metrics (Trips planned, Navigation sessions, Bookings), Retention metrics (Daily/weekly active users, Repeat usage)

**Concrete Examples:**
- "Design travel app: Users (Travelers, commuters), Jobs (Plan trips, navigate, book, find parking), Core Loop (Plan → Navigate → Complete → Return), Key Features (Maps, route planning, booking, parking), Tradeoffs (Accuracy vs speed, Real-time vs offline), Success Metrics (Trips, navigation sessions, retention)"
- "Design Google Maps for kids: Users (Kids, parents), Jobs (Navigate safely, learn, have fun), Core Loop (Open app → Get directions → Follow → Complete → Return), Key Features (Simple navigation, safety features, parental controls), Tradeoffs (Simplicity vs features, Safety vs freedom), Success Metrics (Usage, safety, retention)"

**Representative Questions (Do 5 only):**
- Q449: Design a product to help travelers at airports. How would you go about building it? (travel product design angle)
- Q647: Design Google Maps for kids. (maps for kids angle)
- Q1310: How would you design parking features on Google Maps? (parking feature angle)
- Q1786: Redesign Google Maps to increase engagement with small businesses. (maps redesign angle)
- Q2462: What would be your strategy to improve Google Maps as a product? (maps improvement angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Users → Jobs → Core Loop → Key Features → Tradeoffs → Success Metrics`

**Memorizable Answer:**

When designing a travel platform, I use Users → Jobs → Core Loop → Key Features → Tradeoffs → Success Metrics.

**1️⃣ Users** → Who are the users? (Travelers, Commuters, Transportation providers), What are their needs? (Trip planning, Navigation, Transportation options).

**2️⃣ Jobs** → What jobs do users need done? (Plan trips, Navigate routes, Book transportation, Find parking), Prioritize by Frequency and Urgency.

**3️⃣ Core Loop** → What is the engagement loop? (Plan trip → Navigate/use service → Complete trip → Return for next trip), How does it drive retention? (Regular commutes, Trip planning habits).

**4️⃣ Key Features** → Core features (Maps/navigation, Route planning, Transportation booking, Parking), Supporting features (Search, Reviews, Real-time updates, Offline mode).

**5️⃣ Tradeoffs** → Accuracy vs speed, Real-time vs offline, Features vs simplicity.

**6️⃣ Success Metrics** → Usage metrics (Trips planned, Navigation sessions, Bookings), Retention metrics (Daily/weekly active users, Repeat usage).

**Key Principle:** Design a platform that makes trip planning and navigation easy and reliable.

---

**How to Adapt This Narrative for Each Question:**

- **Q449 (Design product for travelers at airports):** Focus on airport travel
  - "Users: Travelers (passengers), Airport staff, Airlines"
  - "Needs: Navigate airport, Find gates/services, Track flights, Reduce stress"
  - "Jobs: Find gate, Check flight status, Find services (food, shops, lounges), Navigate terminal, Track baggage"
  - "Core Loop: Arrive at airport → Open app → Get directions → Use services → Complete journey → Return for next trip"
  - "Key Features: Airport maps (terminal layout, gate locations), Flight tracking (real-time status, gate changes), Navigation (indoor navigation, directions), Services (food, shops, lounges, restrooms), Notifications (flight updates, gate changes), Offline mode (works without internet)"
  - "Tradeoffs: Accuracy vs speed (prioritize accuracy), Real-time vs offline (support both), Features vs simplicity (keep simple)"
  - "Success Metrics: Usage (airport sessions, navigation usage, service discovery), Retention (repeat usage, user satisfaction, completion rate)"
  - "Prioritize indoor navigation and flight tracking as core features"

- **Q1310 (Design parking features on Google Maps):** Emphasize parking feature
  - "Users: Drivers, Commuters, City planners"
  - "Needs: Find parking, Save time, Reduce stress, Avoid tickets"
  - "Jobs: Find available parking, Reserve parking, Navigate to parking, Pay for parking"
  - "Core Loop: Search destination → See parking options → Select parking → Navigate → Park → Return for next trip"
  - "Key Features: Parking search (near destination, availability), Parking information (price, hours, restrictions), Navigation (directions to parking), Reservation (book in advance), Payment (pay through app), Real-time updates (availability, pricing)"
  - "Tradeoffs: Accuracy vs speed (need real-time accuracy), Features vs simplicity (keep simple), Free vs paid (support both)"
  - "Success Metrics: Usage (parking searches, reservations, navigation to parking), Retention (repeat usage, user satisfaction, completion rate)"
  - "Prioritize real-time availability and easy navigation to parking"

---

### BUCKET 2: Navigation & Trip Planning
**Questions:** ~10 | **Priority:** 🟡 YELLOW (High-yield but needs practice)

**Board Slide Bullets:**
- **What:** "Design navigation" or "Design trip planning" - same framework, with focus on navigation
- **Approach:** Same travel platform framework, with focus on navigation and trip planning
- **Navigation Design:** Route planning (Multiple routes, Traffic-aware, Real-time updates), Turn-by-turn (Clear instructions, Voice guidance, Visual cues), Offline mode (Download maps, Offline navigation)
- **Trip Planning:** Multi-stop planning (Optimize route, Multiple destinations), Pre-trip (Research, Book, Plan), During trip (Navigate, Adjust, Discover)
- **Success Metrics:** Navigation accuracy, Route optimization, User satisfaction, Completion rate

**Concrete Examples:**
- "Design navigation: Route planning (multiple routes, traffic-aware), Turn-by-turn (clear instructions, voice), Offline mode (download maps), Success metrics (accuracy, satisfaction, completion)"
- "Improve trip planning: Multi-stop planning, Pre-trip research, During-trip navigation, Measure planning metrics"

**Representative Questions (Do 5 only):**
- Q647: Design Google Maps for kids. (navigation design angle)
- Q492: Design a solution to map unmapped places in Google Maps. (mapping design angle)
- Q1310: How would you design parking features on Google Maps? (navigation feature angle)
- Q449: Design a product to help travelers at airports. How would you go about building it? (trip planning angle)
- Q1786: Redesign Google Maps to increase engagement with small businesses. (navigation improvement angle)

**❤️ Reusable Narrative (Base Story - Adapt for Each Question):**

**Framework:** `Users → Jobs → Core Loop (Navigation Focus) → Key Features → Tradeoffs → Success Metrics`

**Memorizable Answer:**

When focusing on navigation and trip planning, I use the same travel platform framework but emphasize navigation accuracy and trip planning ease.

**1️⃣ Users & Jobs** → Identify users and their jobs to understand navigation needs.

**2️⃣ Core Loop (Navigation Focus)** → Entry point (How users start - search destination, open app), Core action (Plan route, Navigate, Follow directions), Reward (Reach destination, Save time, Avoid traffic), Return trigger (Next trip, Regular commute, Trip planning).

**3️⃣ Key Features (Navigation)** → Route planning (Multiple routes, Traffic-aware, Real-time updates, ETA), Turn-by-turn navigation (Clear instructions, Voice guidance, Visual cues, Lane guidance), Offline mode (Download maps, Offline navigation, Works without internet), Trip planning (Multi-stop, Pre-trip research, During-trip adjustments).

**4️⃣ Tradeoffs** → Accuracy vs speed (prioritize accuracy), Real-time vs offline (support both), Features vs simplicity (keep simple).

**5️⃣ Success Metrics** → Navigation metrics (Route accuracy, ETA accuracy, Completion rate), Usage (Navigation sessions, Trip planning, Repeat usage), Satisfaction (User ratings, Feedback).

**Key Principle:** Make navigation accurate, reliable, and easy to use.

---

**How to Adapt This Narrative for Each Question:**

- **Q647 (Design Google Maps for kids):** Focus on kids navigation
  - "Users: Kids (primary users), Parents (gatekeepers)"
  - "Needs: Safe navigation, Simple directions, Fun experience, Parental oversight"
  - "Jobs: Navigate to school/friends, Learn directions, Have fun, Stay safe"
  - "Core Loop: Open app → Search destination → Get directions → Follow → Arrive → Return for next trip"
  - "Key Features: Simple navigation (clear, visual, voice), Safety features (parental controls, safe routes, location sharing), Fun elements (kid-friendly UI, gamification), Parental controls (approve destinations, track location, set boundaries), Offline mode (works without internet), Simple search (easy to use)"
  - "Tradeoffs: Simplicity vs features (prioritize simplicity), Safety vs freedom (balance), Fun vs utility (both)"
  - "Success Metrics: Usage (navigation sessions, trip completion), Retention (repeat usage, parent satisfaction, safety incidents)"
  - "Prioritize safety, simplicity, and parental controls"

---

## 🚦 TRAFFIC LIGHT PRIORITIZATION

### 🟢 GREEN (Master - Can explain to non-technical exec)
1. **Travel Platform Design** → Study Bucket 1, practice 5 questions

### 🟡 YELLOW (High-yield but shaky - Practice questions)
2. **Navigation & Trip Planning** → Study Bucket 2, practice 5 questions

---

## ✅ EXECUTIVE CHECKLIST

Before your interview, you should be able to:

- [ ] Walk through travel platform design framework in 2 minutes (Users → Jobs → Core Loop → Key Features → Tradeoffs → Success Metrics)
- [ ] Identify users and their needs (travelers, commuters, providers)
- [ ] Define jobs (plan trips, navigate, book, find parking)
- [ ] Design core loop (plan → navigate → complete → return)
- [ ] Design key features (maps, route planning, booking, parking)
- [ ] Consider tradeoffs (accuracy vs speed, real-time vs offline)
- [ ] Define success metrics (trips, navigation sessions, retention)

---

## 🎯 SUCCESS METRICS

**You're ready when:**
- You can explain the travel platform design framework to a non-technical person in 2 minutes
- You have 2 reusable narratives (one per bucket) that you can adapt
- You've practiced 10 representative questions total (5 per bucket)
- You focus on **Users → Jobs → Core Loop → Key Features → Tradeoffs → Success Metrics framework**, not memorizing answers

**Remember:** P13B_TRAVEL is about designing travel platforms. The framework: Users → Jobs → Core Loop → Key Features → Tradeoffs → Success Metrics. Key focus: Trip planning, navigation, transportation efficiency.
