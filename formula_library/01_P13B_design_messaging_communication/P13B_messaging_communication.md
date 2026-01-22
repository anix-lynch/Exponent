# P13B - Messaging/Communication Platforms

**Formula:** `Users → Jobs → Core Loop → Key Features → Tradeoffs → Success Metrics`

**Intent:** Messaging apps, chat platforms, communication tools. Focus on real-time communication, reliability, and network effects.

---

## 🧠 Mental Model (ASCII Tree)

```
Messaging/Communication Platform Design
│
├─ 1) Users
│   ├─ Who are the users?
│   │   ├─ Individual users
│   │   ├─ Groups/teams
│   │   └─ Businesses
│   │
│   └─ What are their needs?
│       ├─ Real-time communication
│       ├─ Reliability
│       └─ Privacy
│
├─ 2) Jobs
│   ├─ What jobs do users need done?
│   │   ├─ Send messages
│   │   ├─ Receive messages
│   │   ├─ Organize conversations
│   │   └─ Share media/files
│   │
│   └─ Job priority
│       ├─ Urgency
│       └─ Frequency
│
├─ 3) Core Loop
│   ├─ What is the engagement loop?
│   │   ├─ Receive message
│   │   ├─ Read/respond
│   │   ├─ Send message
│   │   └─ Wait for response
│   │
│   └─ How does it drive retention?
│       ├─ Daily communication
│       └─ Network effects
│
├─ 4) Key Features
│   ├─ Core features
│   │   ├─ Messaging
│   │   ├─ Notifications
│   │   ├─ Media sharing
│   │   └─ File sharing
│   │
│   └─ Supporting features
│       ├─ Search
│       ├─ Organization
│       ├─ Privacy
│       └─ Group features
│
├─ 5) Tradeoffs
│   ├─ Real-time vs reliability
│   ├─ Privacy vs features
│   └─ Simplicity vs functionality
│
└─ 6) Success Metrics
    ├─ Communication metrics
    │   ├─ Messages sent/received
    │   ├─ Response time
    │   └─ Delivery rate
    │
    └─ Retention metrics
        ├─ Daily active users
        ├─ Network growth
        └─ Engagement
```

---

## 📌 Sample Questions

- "Design a messaging app"
- "Design a chat feature"
- "Design communication for teams"

---

## 🎯 Key Principles

- **Real-time**: Prioritize instant delivery
- **Reliability**: Messages must be delivered
- **Network effects**: Value increases with users
- **Privacy**: Protect user communications
- **Simplicity**: Easy to use, minimal friction

---

## 🔗 Related Patterns

- **P13B_Social_Community**: Use for social messaging features
- **P4 (Cohort/Retention)**: Use for measuring network growth
