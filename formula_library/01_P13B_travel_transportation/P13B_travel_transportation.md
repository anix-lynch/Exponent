# P13B - Travel/Transportation Platforms

**Formula:** `Users → Jobs → Core Loop → Key Features → Tradeoffs → Success Metrics`

**Intent:** Travel apps, navigation, transportation, parking. Focus on trip planning, navigation, and transportation efficiency.

---

## 🧠 Mental Model (ASCII Tree)

```
Travel/Transportation Platform Design
│
├─ 1) Users
│   ├─ Who are the users?
│   │   ├─ Travelers
│   │   ├─ Commuters
│   │   └─ Transportation providers
│   │
│   └─ What are their needs?
│       ├─ Trip planning
│       ├─ Navigation
│       └─ Transportation options
│
├─ 2) Jobs
│   ├─ What jobs do users need done?
│   │   ├─ Plan trips
│   │   ├─ Navigate routes
│   │   ├─ Book transportation
│   │   └─ Find parking
│   │
│   └─ Job priority
│       ├─ Frequency
│       └─ Urgency
│
├─ 3) Core Loop
│   ├─ What is the engagement loop?
│   │   ├─ Plan trip
│   │   ├─ Navigate/use service
│   │   ├─ Complete trip
│   │   └─ Return for next trip
│   │
│   └─ How does it drive retention?
│       ├─ Regular commutes
│       └─ Trip planning habits
│
├─ 4) Key Features
│   ├─ Core features
│   │   ├─ Maps/navigation
│   │   ├─ Route planning
│   │   ├─ Booking
│   │   └─ Real-time updates
│   │
│   └─ Supporting features
│       ├─ Reviews/ratings
│       ├─ Saved locations
│       └─ Trip history
│
├─ 5) Tradeoffs
│   ├─ Accuracy vs speed
│   ├─ Offline vs online
│   └─ Cost vs convenience
│
└─ 6) Success Metrics
    ├─ Usage metrics
    │   ├─ Trips planned
    │   ├─ Navigation sessions
    │   └─ Bookings completed
    │
    └─ Quality metrics
        ├─ Route accuracy
        └─ User satisfaction
```

---

## 📌 Sample Questions

- "Design a parking solution for navigation apps"
- "Design a Meta product for space travel"
- "Design a Google-branded inflight entertainment system"

---

## 🎯 Key Principles

- **Real-time accuracy**: Provide up-to-date information
- **Offline capability**: Work without internet connection
- **Multi-modal**: Support different transportation types
- **Context-aware**: Understand user's current situation
- **Reliability**: Critical for navigation and booking

---

## 🔗 Related Patterns

- **P2B2 (On-Demand Metrics)**: Use for transportation metrics
- **P13B_Social_Community, P13B_General**: Other consumer platform subcategories
