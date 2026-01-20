# P13B - Messaging/Communication Platforms

**Formula:** `Users → Jobs → Core Loop → Key Features → Tradeoffs → Success Metrics`

**Intent:** Messaging apps, chat, notifications, communication. Focus on real-time communication, reliability, and user engagement.

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
│   │   └─ Group chat
│   │
│   └─ Supporting features
│       ├─ Read receipts
│       ├─ Typing indicators
│       └─ Message search
│
├─ 5) Tradeoffs
│   ├─ Privacy vs features
│   ├─ Real-time vs battery
│   └─ Simplicity vs functionality
│
└─ 6) Success Metrics
    ├─ Engagement metrics
    │   ├─ Messages sent
    │   ├─ Daily active users
    │   └─ Response rate
    │
    └─ Quality metrics
        ├─ Delivery reliability
        └─ User satisfaction
```

---

## 📌 Sample Questions

- "Design a group chat application"
- "Design a file upload feature for an AI chat application"
- "How would you redesign Slack for education?"

---

## 🎯 Key Principles

- **Real-time reliability**: Messages must be delivered quickly and reliably
- **Privacy**: Protect user communications
- **Simplicity**: Easy to use, minimal friction
- **Network effects**: More users = more value
- **Cross-platform**: Work across devices

---

## 🔗 Related Patterns

- **P13B_Social_Community**: Similar network effects
- **P13B_General**: Other consumer platform subcategories
