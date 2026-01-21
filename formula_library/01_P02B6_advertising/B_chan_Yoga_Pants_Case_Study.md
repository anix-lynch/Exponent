# B chan yoga pants ads — end-to-end case study (clean + memorizable)

---

## Actors

* **Advertiser**: Amazon yoga pants seller
* **Platform**: Facebook
* **Creator**: B chan (yoga video, private)
* **Audience**: B chan's friends

---

## Setup

* B chan has **1,500 friends**
* Video is **private**
* **600 friends watched** in 24 hours
* Facebook allows **1 ad slot per view**

---

## What actually happens (timeline)

### 1️⃣ Content creates attention (Creator side)

* 600 video views happen
* This creates **600 ad opportunities**
* B chan does **not** choose ads
* Advertiser does **not** see B chan

---

### 2️⃣ Facebook runs auctions (Platform side)

For **each of the 600 views**, Facebook asks:

> "Do I have an eligible advertiser willing to pay enough to show an ad to *this person* right now?"

Results:

* Ads eligible for **420 views**
* No eligible ad for **180 views**

```
Fill rate = 420 / 600 = 70%
```

📌 Fill rate is a **platform KPI**, not creator or advertiser KPI.

---

### 3️⃣ Ads are shown (Inventory realized)

* **420 ad impressions** happen
* These impressions may include yoga pants ads or other advertisers

📌 Impressions = what *actually* showed, not what *could* show.

---

### 4️⃣ Pricing happens (CPM)

* Winning auction CPM = **$8**
* Total advertiser spend:

```
(420 / 1000) × $8 = $3.36
```

* Facebook keeps a cut
* B chan gets **$0** unless monetization is enabled

📌 CPM is **platform revenue metric**, advertiser experiences it as **cost**.

---

### 5️⃣ Advertiser outcome (Demand side)

Amazon seller now looks at:

* CTR
* CPC
* Conversion rate
* ROAS

They **do not care** about:

* fill rate
* creator identity
* private vs public video

They only ask:

> "Did I sell yoga pants?"

---

## Why fill rate was not 100%

Not because:
❌ "Facebook dislikes B chan"
❌ "Friends didn't like the content"

But because:

* Some viewers didn't match targeting
* Some bids were below Facebook's floor
* Frequency caps applied
* UX rules skipped ads

👉 Facebook prefers **no ad** over **low-value ad**

---

## Ownership summary (memorize this)

```
Creator (B chan)
→ creates attention (views)

Platform (Facebook)
→ monetizes attention
→ owns impressions, fill rate, CPM

Advertiser (Amazon seller)
→ buys audience
→ owns CTR, CPC, conversions, ROAS
```

---

## One-sentence takeaway (interview-ready)

> **In the B chan yoga pants case, the creator supplies attention, the platform decides when and how that attention is monetized, and the advertiser only cares whether the impressions they bought converted.**

---

## Key Learnings

1. **Fill rate is a platform KPI** - measures how well platform monetizes inventory
2. **Impressions ≠ opportunities** - only what actually shows counts
3. **CPM is platform revenue** - but advertiser experiences as cost
4. **Advertiser only cares about outcomes** - CTR, CPC, conversions, ROAS
5. **Platform optimizes for quality** - prefers no ad over low-value ad

---

## Interview Application

Use this case to explain:

* How advertising platforms work end-to-end
* The difference between platform KPIs and advertiser KPIs
* Why fill rate might be < 100%
* How auctions determine which ads show
* The relationship between creator, platform, and advertiser
