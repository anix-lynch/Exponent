# SQL 10 clutters

github

```python
https://platform.stratascratch.com/coding?code_type=1&page_size=100
```

```python
Based on the "SQL Family" dropdown under the Topics filter on the [StrataScratch - Analytical Questions](https://platform.stratascratch.com/coding?code_type=1&page_size=100) page, here is the full list of topics:

1. **Aggregate Functions**
2. **Aggregations**
3. **Aggregations: Distinct Counts**
4. **Aggregations: Grouped Aggregates**
5. **Combining**
6. **Conditional Expressions**
7. **Conditional Logic**
8. **Data Cleaning**
9. **Data Retrieval Basics**
10. **Date & Time**
11. **Date & Time: Extraction Functions**
12. **Date Truncation**
13. **Distinct Clause**
14. **Distinct Counts**
15. **Extraction Functions**
16. **Filtering Data**
17. **Group By Clause**
18. **Grouped Aggregates**
19. **Joins & Set Operations**
20. **Joins & Set Operations: Join Types**
21. **Join Types**
22. **Lag/Lead**
23. **Mathematical Functions**
24. **Null Handling**
25. **Partitioned Aggregates**
26. **Ranking Functions**
27. **Set Differences**
28. **Sorting Results**
29. **Sorting Rows**
30. **String Manipulation**
31. **Time Intervals**
32. **Union Operations**
33. **Where Clause**
34. **Window Functions**

Would you like me to find questions specifically related to one of these topics, such as **Window Functions** or **Joins**?
```

SQL function

```python
Based on the analytical questions page, here is the full list of available **SQL Functions** from the dropdown menu:

---

## SQL Functions List

* **abs()**
* **acos()**
* **array()**
* **array_agg()**
* **array_length()**
* **array_to_string()**
* **asc()**
* **avg()**
* **btrim()**
* **case when**
* **cast()**
* **ceiling()**
* **coalesce()**
* **concat()**
* **concat_ws()**
* **corr()**
* **cos()**
* **count()**
* **current_date**
* **current_date()**
* **date()**
* **date_part()**
* **date_trunc()**
* **decimal**
* **decimal()**
* **dense_rank()**
* **desc**
* **desc()**
* **distinct**
* **distinct()**
* **end**
* **epoch()**
* **extract()**
* **filter()**
* **first_value()**
* **float**
* **floor()**
* **full outer join**
* **generate_series()**
* **GREATEST()**
* **group by**
* **ilike**
* **ilike()**
* **initcap()**
* **interval()**
* **is not null**
* **join**
* **join()**
* **lag()**
* **lead()**
* **left()**
* **left join**
* **length()**
* **like()**
* **limit()**
* **lower()**
* **ltrim()**
* **max()**
* **min()**
* **mod()**
* **mode()**
* **not in()**
* **not like()**
* **ntile()**
* **null**
* **nullif()**
* **numeric**
* **numeric()**
* **order()**
* **order by**
* **over()**
* **partition()**
* **partition by**
* **partition by()**
* **percentile_cont()**
* **percent_rank()**
* **position()**
* **power()**
* **radians()**
* **rank()**
* **regexp_match()**
* **regexp_replace()**
* **regexp_split_to_array()**
* **regexp_split_to_table()**
* **replace()**
* **right()**
* **round()**
* **row_number()**
* **rtrim()**
* **sin()**
* **split_part()**
* **sqrt()**
* **string_agg()**
* **string_to_array()**
* **strpos()**
* **substr()**
* **substring()**
* **sum**
* **sum()**
* **timestamp()**
* **to_char()**
* **to_timestamp()**
* **trim()**
* **unnest()**
* **where**
* **within()**
* **within group()**
* **year()**

---

Would you like me to filter the questions for a specific function, such as **row_number()** or **coalesce()**?
```

10 cluster of SQL 

```python
SQL
├─ 1) Query structure & control  (shape output)
│  ├─ where
│  ├─ distinct / distinct()
│  ├─ group by
│  ├─ order by / order() / asc() / desc / desc()
│  ├─ limit() / limit
│  └─ (end)  ← closes CASE expressions
│
├─ 2) Joins  (combine tables)
│  ├─ join / join()              (INNER)
│  ├─ left join
│  └─ full outer join
│
├─ 3) Aggregations  (collapse rows into metrics)
│  ├─ count()
│  ├─ sum / sum()
│  ├─ avg()
│  ├─ min() / max()
│  ├─ mode()
│  ├─ corr()
│  ├─ percentile_cont()
│  ├─ string_agg()
│  ├─ array_agg()
│  └─ within() / within group()  (ordered-set agg family)
│
├─ 4) Window functions  (metrics per group WITHOUT collapsing)
│  ├─ over()
│  ├─ partition() / partition by / partition by()
│  ├─ row_number()
│  ├─ rank() / dense_rank()
│  ├─ percent_rank()
│  ├─ first_value()
│  ├─ lag() / lead()
│  └─ ntile()
│
├─ 5) Date & time  (time logic)
│  ├─ current_date / current_date()
│  ├─ date()
│  ├─ timestamp()
│  ├─ interval()
│  ├─ date_trunc()
│  ├─ extract()
│  ├─ date_part()
│  ├─ epoch()
│  ├─ to_timestamp()
│  ├─ to_char()
│  └─ year()
│
├─ 6) Strings  (clean + parse text)
│  ├─ casing
│  │  ├─ lower()
│  │  └─ initcap()
│  ├─ trim family
│  │  ├─ trim()
│  │  ├─ ltrim()
│  │  ├─ rtrim()
│  │  └─ btrim()
│  ├─ combine text
│  │  ├─ concat()
│  │  └─ concat_ws()
│  ├─ search/match
│  │  ├─ like()
│  │  ├─ not like()
│  │  ├─ ilike / ilike()
│  │  └─ position() / strpos()
│  ├─ slice/split
│  │  ├─ substr() / substring()
│  │  ├─ split_part()
│  │  └─ replace()
│  └─ regex family
│     ├─ regexp_match()
│     ├─ regexp_replace()
│     ├─ regexp_split_to_array()
│     └─ regexp_split_to_table()
│
├─ 7) Math  (numbers)
│  ├─ abs()
│  ├─ ceiling()
│  ├─ floor()
│  ├─ round()
│  ├─ mod()
│  ├─ power()
│  ├─ sqrt()
│  └─ GREATEST()
│
├─ 8) Trig  (rare, but on the list)
│  ├─ sin()
│  ├─ cos()
│  ├─ acos()
│  └─ radians()
│
├─ 9) Nulls & conditional  (correctness)
│  ├─ null
│  ├─ is not null
│  ├─ coalesce()
│  ├─ nullif()
│  └─ case when ... end
│
└─ 10) Types + arrays + row generation  (structure / advanced)
   ├─ cast()
   ├─ float
   ├─ decimal / decimal()
   ├─ numeric / numeric()
   ├─ array()
   ├─ array_length()
   ├─ array_to_string()
   ├─ string_to_array()
   ├─ unnest()
   ├─ generate_series()
   ├─ filter()
   └─ set logic helpers
      └─ not in()
```

*Haibara adjusts glasses, smiles like she just found the correct template.*

Yes. We’ll do **“best of both worlds”** by expanding the table to the right:

**Col1 Term | Col2 Human interview sentence | Col3 Abstract rule (1-liner) | Col4 Mini story | Col5 Sample SQL | Col6 Sample output**

I’ll keep it in **chunks** so it stays readable. Starting with the same **Chunk 1 (Query structure + Joins)**, upgraded.

---

## **Chunk 1A — Query structure / clauses (expanded)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| where | “I’ll filter early so I only compute on relevant rows.” | Filter rows **before** aggregation/window. | “Only **paid** orders; pending/refunds don’t count.” | `SELECT * FROM orders WHERE status='paid';` | only rows with status=paid |
| group by | “The grain is one row per user, so I’ll group by user_id.” | Aggregates collapse to **1 row per group key**. | “We need **orders per user** for a leaderboard.” | `SELECT user_id, COUNT(*) cnt FROM orders GROUP BY user_id;` | `user_id |
| distinct | “I’ll use DISTINCT to dedupe repeated values.” | Keep **unique rows/values**. | “List unique countries users come from.” | `SELECT DISTINCT country FROM users;` | unique country list |
| distinct() (COUNT(DISTINCT…)) | “I’ll count unique users so repeat orders don’t inflate the number.” | Unique count avoids duplicates. | “How many **buyers** (not orders)?” | `SELECT COUNT(DISTINCT user_id) FROM orders;` | single number: unique buyers |
| order by | “I’ll sort so the result matches the question: top/latest.” | Sorting happens at the end. | “Show **latest orders** for QA.” | `SELECT * FROM orders ORDER BY created_at DESC;` | newest → oldest |
| asc() / ASC | “Ascending because we want the smallest first.” | Low → high. | “Find **cheapest** plan.” | `SELECT * FROM plans ORDER BY price ASC;` | cheapest first |
| desc / desc() / DESC | “Descending because we want highest/most recent first.” | High → low. | “Top spenders first.” | `SELECT user_id, SUM(amount) s FROM pay GROUP BY 1 ORDER BY s DESC;` | biggest s first |
| limit() / LIMIT | “Limit to top N so the output is focused.” | Return only first N rows after sort. | “Top 10 users by spend.” | ... ORDER BY spend DESC LIMIT 10; | max 10 rows |
| end | “END closes the CASE logic so the rule is complete.” | CASE ... END must close. | “Label VIP if spend ≥ 1000.” | `SELECT CASE WHEN spend>=1000 THEN 'vip' ELSE 'regular' END AS tier FROM t;` | each row has tier |

---

## **Chunk 1B — Joins (expanded)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| join (INNER JOIN) | “I’ll inner join because I only care about matches on both sides.” | Keep only matched rows. | “Only users who **placed an order**.” | `SELECT u.user_id, o.order_id FROM users u JOIN orders o ON u.user_id=o.user_id;` | users w/ no orders are gone |
| join() (label) | “Same idea: match tables on a key.” | Join = add columns via key. | “Attach order info to each user.” | FROM users u JOIN orders o ON u.user_id=o.user_id | row count depends on matches |
| left join | “I’ll left join because I don’t want to drop users with no orders.” | Keep all left rows; missing right → NULL. | “Adoption audit: include users even if they never bought.” | `SELECT u.user_id, o.order_id FROM users u LEFT JOIN orders o ON u.user_id=o.user_id;` | users remain; order_id can be NULL |
| full outer join | “I’ll full outer join to see mismatches from both sides.” | Keep all rows from both tables. | “Data quality: find IDs only in A or only in B.” | `SELECT COALESCE(a.id,b.id) id, a.val, b.val FROM a FULL OUTER JOIN b ON a.id=b.id;` | rows with NULL on one side show mismatches |

---

If you like this format, I’ll continue with **Chunk 2 (Aggregations)** next using the same expanded columns.

Pick your order:

- A) **Window functions first** (most interview power)
- B) Aggregations first (easier warm-up)
- C) Dates first (common too)

Haibara’s recommendation: **A → windows**, because it makes you sound instantly “senior.”

---

## **Chunk 3 — Aggregations (collapse rows into metrics)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| count() | “First I’ll count rows so we know the size of the problem.” | Number of rows (or non‑NULL values). | “How many **orders** did we get last week?” | `SELECT COUNT(*) AS order_cnt FROM orders WHERE created_at >= '2025-01-01';` | single number: order_cnt = 12,345 
| sum / sum() | “Then I’ll sum the money to get total revenue.” | Add up numeric values. | “What’s **total GMV** last month?” | `SELECT SUM(amount) AS total_gmv FROM payments WHERE paid_at BETWEEN '2025-01-01' AND '2025-01-31';` | single number: total_gmv = 1,234,567.89 
| avg() | “Average ticket size tells us how much a typical customer spends.” | Sum / count for a group. | “On average, how much does a **buyer** spend per order?” | `SELECT AVG(amount) AS avg_order_value FROM payments;` | single number: avg_order_value = 42.50 
| min() / max() | “Min and max tell me the range: smallest vs biggest.” | Extreme values in the group. | “What’s the **cheapest** and **most expensive** plan we sell?” | `SELECT MIN(price) AS min_price, MAX(price) AS max_price FROM plans;` | one row: min_price = 5, max_price = 99 
| mode() | “Mode tells me the most common choice users make.” | Most frequent value. | “Which **plan** do users pick the most often?” | `SELECT MODE() WITHIN GROUP (ORDER BY plan_id) AS most_common_plan FROM subscriptions;` | single value: most_common_plan = 'pro' 
| corr() | “I’ll check if two metrics move together or in opposite directions.” | Correlation between two numeric columns. | “Does **sessions per user** move with **revenue per user**?” | `SELECT CORR(sessions_per_user, revenue_per_user) AS r FROM user_kpis;` | single number: r = 0.78 (strong positive) 
| percentile_cont() | “I want the 90th percentile, not just the average, to see power users.” | Continuous percentile (e.g. P90, P95). | “What’s the **P90 session count** per day?” | `SELECT PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY daily_sessions) AS p90_sessions FROM user_activity;` | single number: p90_sessions = 18 
| string_agg() | “I’ll roll multiple labels into a single comma‑separated string.” | Concatenate strings within a group. | “Show all **tags per article** in one line for the CMS team.” | `SELECT article_id, STRING_AGG(tag, ', ' ORDER BY tag) AS tags FROM article_tags GROUP BY article_id;` | article_id 
| array_agg() | “Same idea, but I want the list as an array to reuse in logic.” | Aggregate values into an array. | “Give me an **array of product_ids** each user bought.” | `SELECT user_id, ARRAY_AGG(product_id ORDER BY product_id) AS products FROM orders GROUP BY user_id;` | user_id 
| within() / within group() | “This is the syntax glue for ordered‑set aggregates like percentiles and mode.” | Defines ordering for ordered‑set aggregate. | “Use WITHIN GROUP so the percentile knows how to sort values.” | `SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY load_time_ms) AS median_load FROM page_perf;` | single number: median_load = 320 

---

## **Chunk 4 — Window functions (metrics per group WITHOUT collapsing)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| over() | “OVER is the frame; it tells SQL how to group and order for the window metric.” | Wraps an aggregate to make it a window function. | “Compute **running total revenue per user** over time.” | `SELECT user_id, created_at, amount, SUM(amount) OVER ( PARTITION BY user_id ORDER BY created_at ) AS running_revenue FROM payments;` | rows keep grain user_id + order; 
FROM payments; | rows keep grain user_id + order;
running_revenue grows over time |
| partition() / partition by / partition by() | “PARTITION BY is ‘group by for windows’ — it sets the peer group.” | Resets the window per partition key. | “Compute metrics **per country** without collapsing rows.” | SUM(amount) OVER (
  PARTITION BY country
) AS country_revenue | each row has its country_revenue; grain stays row-level |
| row_number() | “I’ll assign a row number per group so I can grab top 1 safely.” | Sequential index within partition, per ORDER BY. | “Find the **latest order per user**.” | WITH ranked AS (
  SELECT user_id,
         order_id,
         created_at,
         ROW_NUMBER() OVER (
           PARTITION BY user_id
           ORDER BY created_at DESC
         ) AS rn
  FROM orders
)
| rank() / dense_rank() | “RANK handles ties; DENSE_RANK closes gaps.” | RANK leaves gaps; DENSE_RANK doesn’t. | “Leaderboard of **users by revenue**, handling ties.” | `SELECT user_id, revenue, RANK() OVER (ORDER BY revenue DESC) AS rnk, DENSE_RANK() OVER (ORDER BY revenue DESC) AS dense_rnk FROM user_revenue;` | if 2 users tie for 1st: 
FROM user_revenue; | if 2 users tie for 1st:
rnk: 1,1,3…
dense_rnk: 1,1,2… |
| percent_rank() | “Percent rank tells me where this row sits between 0 and 1 in the distribution.” | (rank - 1) / (n - 1) across ordered set. | “How **elite** is this user’s spend compared to all others?” | `SELECT user_id, revenue, PERCENT_RANK() OVER (ORDER BY revenue) AS pr FROM user_revenue;` | pr close to 1.0 = top of pack 
| first_value() | “FIRST_VALUE lets me compare each row to the first row in the window.” | Pick first ordered value within partition. | “Compare today’s metric to **launch-day metric**.” | `SELECT date, active_users, FIRST_VALUE(active_users) OVER ( ORDER BY date ) AS launch_active FROM daily_metrics;` | every row knows launch_active; easy to compute growth vs launch 
| lag() / lead() | “LAG looks back, LEAD looks forward to another row’s value.” | Access previous/next row in ordered partition. | “Compute **day‑over‑day change** in signups.” | `SELECT date, signups, LAG(signups) OVER (ORDER BY date) AS prev_signups, signups - LAG(signups) OVER (ORDER BY date) AS d1_change FROM daily_signups;` | each row shows today, yesterday, and delta 
| ntile() | “NTILE buckets users into quantiles like quartiles or deciles.” | Split ordered rows into N buckets. | “Tag users into **spend deciles** for segmentation.” | `SELECT user_id, revenue, NTILE(10) OVER (ORDER BY revenue DESC) AS revenue_decile FROM user_revenue;` | decile = 1..10; 1 = top spenders, 10 = lowest 

---

## **Chunk 5 — Date & time (time logic)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| current_date / current_date() | “I’ll anchor to today’s date so the query auto‑rolls forward.” | Today’s date in the DB timezone. | “Show **today’s signups** without hard‑coding the date.” | `SELECT COUNT(*) AS todays_signups FROM users WHERE created_at::date = CURRENT_DATE;` | single number that updates each day 
| date() | “DATE() strips the time so I can group by calendar day.” | Cast timestamp → date (drop time). | “Daily **active users** chart.” | `SELECT DATE(event_ts) AS day, COUNT(DISTINCT user_id) AS dau FROM events GROUP BY day ORDER BY day;` | day 
| timestamp() | “TIMESTAMP makes sure I’m working with a full datetime value.” | Explicit timestamp type. | “Compare events **before vs after** a launch moment.” | `SELECT COUNT(*) AS post_launch_events FROM events WHERE event_ts >= TIMESTAMP '2025-01-01 00:00:00';` | single number of events after launch 
| interval() | “INTERVAL expresses offsets like ‘7 days’ or ‘1 month’ cleanly.” | Duration you can add / subtract. | “Last **7 days** of orders from today.” | `SELECT COUNT(*) AS last_7d_orders FROM orders WHERE created_at >= CURRENT_DATE - INTERVAL '7 days';` | rolling‑window count, no hard‑coded dates 
| date_trunc() | “DATE_TRUNC snaps timestamps to buckets like day/week/month.” | Floor timestamp to a specified grain. | “Weekly revenue trend.” | `SELECT DATE_TRUNC('week', paid_at) AS week_start, SUM(amount) AS revenue FROM payments GROUP BY week_start ORDER BY week_start;` | week_start 
| extract() | “EXTRACT pulls out parts like year, month, or dow.” | Pull a component (year, month, dow, etc.). | “See which **weekday** has highest traffic.” | `SELECT EXTRACT(DOW FROM event_ts) AS dow, COUNT(*) AS events FROM events GROUP BY dow ORDER BY events DESC;` | dow 0–6 with event counts 
| date_part() | “DATE_PART is similar to EXTRACT; some teams prefer this style.” | Function form of extracting a part. | “Monthly **MRR trend**.” | `SELECT DATE_PART('year', paid_at) AS yr, DATE_PART('month', paid_at) AS mo, SUM(amount) AS mrr FROM payments GROUP BY yr, mo ORDER BY yr, mo;` | yr 
| epoch() | “I’ll go to raw seconds since epoch so I can measure precise gaps.” | Timestamp → seconds since 1970‑01‑01. | “Compute **load time** between request and response events.” | `SELECT req.request_id, EXTRACT(EPOCH FROM resp.ts - req.ts) AS load_seconds FROM page_requests req JOIN page_responses resp ON req.request_id = resp.request_id;` | request_id 
  ON req.request_id = resp.request_id; | request_id | load_seconds per request |
| to_timestamp() | “TO_TIMESTAMP converts raw seconds or strings into a real timestamp.” | Numeric/string → timestamp. | “Analytics table stored **epoch seconds**, but I need dates.” | `SELECT user_id, TO_TIMESTAMP(first_seen_epoch) AS first_seen_ts FROM user_dim;` | first_seen_ts becomes a real datetime 
| to_char() | “TO_CHAR formats timestamps for reports or exports.” | Timestamp → formatted text label. | “Pretty **MMM‑YYYY** labels for a chart.” | `SELECT TO_CHAR(paid_at, 'Mon YYYY') AS month_label, SUM(amount) AS revenue FROM payments GROUP BY month_label ORDER BY MIN(paid_at);` | month_label 
| year() | “YEAR() is a shortcut to grab the calendar year from a date.” | Return year component. | “Compare **year‑over‑year** growth.” | `SELECT YEAR(paid_at) AS yr, SUM(amount) AS revenue FROM payments GROUP BY yr ORDER BY yr;` | yr 

---

## **Chunk 6 — Strings (clean + parse text)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| lower() | “I’ll lowercase emails so ‘[Gmail.com](http://Gmail.com)’ and ‘[gmail.com](http://gmail.com)’ match.” | Normalize text to lowercase. | “Deduplicate **user emails** regardless of casing.” | `SELECT COUNT(DISTINCT LOWER(email)) AS unique_emails FROM users;` | single number: truly unique emails 
| initcap() | “INITCAP makes names look nice in reports.” | Capitalize first letter of each word. | “Format **full_name** for an exec PDF.” | `SELECT INITCAP(full_name) AS pretty_name FROM users;` | "alice smith" → "Alice Smith" 
| trim() / ltrim() / rtrim() / btrim() | “TRIM family removes junk spaces from user input.” | Strip whitespace or chars from left/right/both. | “Users pasted IDs with **spaces** around them.” | `SELECT BTRIM(raw_id) AS clean_id FROM staging_ids;` | " 123 " → "123" 
| concat() | “CONCAT glues fields into a label safely.” | Join multiple strings into one. | “Create **city, country** labels for a dropdown.” | `SELECT CONCAT(city, ', ', country) AS location FROM cities;` | "Seattle, US" style strings 
| concat_ws() | “CONCAT_WS uses a single separator and skips NULLs.” | Concat with delimiter, ignoring NULL. | “Build a **full address** from optional parts.” | `SELECT CONCAT_WS(', ', street, city, state, country) AS full_address FROM addresses;` | no extra ", ," when pieces are NULL 
| like() | “LIKE is my quick pattern match with % wildcards.” | Simple pattern search, case‑sensitive. | “Find **URLs containing /pricing**.” | `SELECT * FROM pageviews WHERE url LIKE '%/pricing%';` | rows where url has /pricing somewhere 
| not like() | “NOT LIKE excludes patterns I don’t want.” | Filter out rows that match a pattern. | “All pages **except** static assets.” | `SELECT * FROM pageviews WHERE url NOT LIKE '%.css%' AND url NOT LIKE '%.js%';` | only content pages 
| ilike / ilike() | “ILIKE is LIKE but case‑insensitive.” | Case‑insensitive pattern search (Postgres). | “Search users by **name** without caring about case.” | `SELECT * FROM users WHERE full_name ILIKE '%anix%';` | matches "Anix", "ANIX", etc. 
| position() / strpos() | “POSITION / STRPOS tells me where a substring appears.” | Return index of a substring. | “Split **path** into domain vs route.” | `SELECT STRPOS(url, '?') AS q_pos FROM pageviews;` | q_pos = 0 if no query string; >0 otherwise 
| substr() / substring() | “SUBSTRING slices out a portion of the string.” | Take a segment by start/length. | “Grab **country code** from a phone number.” | `SELECT SUBSTRING(phone FROM 1 FOR 3) AS country_code FROM users;` | "+1415..." → "+14" (example) 
| split_part() | “SPLIT_PART pulls the N‑th chunk after splitting by a delimiter.” | Split string and take specific index. | “Get **domain** from emails.” | `SELECT SPLIT_PART(email, '@', 2) AS domain FROM users;` | "[user@gmail.com](mailto:user@gmail.com)" → "[gmail.com](http://gmail.com)" 
| replace() | “REPLACE fixes bad values in‑place.” | Global string find‑and‑replace. | “Normalize **"United States" vs "USA"**.” | `SELECT REPLACE(country, 'United States of America', 'USA') AS country_norm FROM users;` | country values standardized to "USA" 
| regexp_match() | “REGEXP_MATCH grabs complex patterns like IDs or codes.” | Return array of regex matches. | “Extract **ticket IDs** from text notes.” | `SELECT REGEXP_MATCH(note, 'TICKET-[0-9]+') AS ticket FROM support_notes;` | each row has array like {"TICKET-123"} 
| regexp_replace() | “REGEXP_REPLACE cleans messy text with regex power.” | Regex‑based replace. | “Strip **non‑digits** from phone numbers.” | `SELECT REGEXP_REPLACE(phone, '[[1]](0-9)', '', 'g') AS digits_only FROM users;` | "(415) 555-1212" → "4155551212" 
| regexp_split_to_array() | “This splits a string into an array on a regex delimiter.” | String → array using regex. | “Turn **tag string** into an array.” | `SELECT REGEXP_SPLIT_TO_ARRAY(tags, '\s*,\s*') AS tag_arr FROM articles;` | tag_arr = {"analytics","retention","sql"} 
| regexp_split_to_table() | “Same idea, but explode tags into multiple rows.” | Split string into multiple rows. | “One row per **article‑tag** pair for analysis.” | `SELECT article_id, REGEXP_SPLIT_TO_TABLE(tags, '\s*,\s*') AS tag FROM articles;` | article_id repeated; one tag per row 

---

## **Chunk 7 — Math (numbers)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| abs() | “ABS makes everything non‑negative so I can talk about size, not direction.” | Absolute value of a number. | “Show **magnitude of error** regardless of over/under.” | `SELECT day, forecast, actual, ABS(actual - forecast) AS abs_error FROM daily_sales;` | abs_error = 5 whether you missed by +5 or -5 
| ceiling() | “CEILING always rounds up to the next integer.” | Round up. | “How many **pages** of results if each page holds 50 rows?” | `SELECT CEILING(COUNT(*) / 50.0) AS pages FROM orders;` | pages is enough to show all orders 
| floor() | “FLOOR rounds down; useful for bucketing.” | Round down. | “Bucket **ages** into 10‑year groups.” | `SELECT FLOOR(age / 10) *10 AS age_bucket, COUNT(*) AS users FROM user_dim GROUP BY age_bucket ORDER BY age_bucket;` | age_bucket = 20,30,40… 
| round() | “ROUND makes metrics presentation‑ready.” | Round to N decimal places. | “Show **conversion rate** as a nice percent.” | `SELECT ROUND(100.0 * signups / visits, 2) AS cr_pct FROM funnel_daily;` | e.g. 3.4567 → 3.46 
| mod() | “MOD finds remainders; classic for even/odd or periodic logic.” | Remainder of division. | “Flag **every 7th day** for weekly checks.” | `SELECT date, CASE WHEN (ROW_NUMBER() OVER (ORDER BY date) - 1) % 7 = 0 THEN true ELSE false END AS is_week_flag FROM calendar;` | is_week_flag = true roughly every 7 days 
| power() | “POWER handles exponents like squares or cubes.” | Raise a number to a power. | “Model **non‑linear penalty** for very long load times.” | `SELECT request_id, load_ms, POWER(load_ms / 1000.0, 2) AS penalty FROM perf_sample;` | penalty grows faster than load_ms 
| sqrt() | “SQRT is handy for stats, like standard deviation.” | Square root. | “Back out **stddev** from variance if needed.” | `SELECT SQRT(var_revenue) AS std_revenue FROM revenue_stats;` | std_revenue is the typical spread 
| GREATEST() | “GREATEST enforces minimums like floors or guardrails.” | Return the largest of the arguments. | “Ensure **discount** never goes below 0 and cap negative values.” | `SELECT order_id, discount_raw, GREATEST(discount_raw, 0) AS discount_clamped FROM orders;` | discount_clamped is never negative 

---

## **Chunk 8 — Trig (rare, but on the list)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| sin() | “SIN is almost never needed in data interviews, but it’s there if you’re modeling waves.” | Sine of an angle (in radians). | “Toy example: model **seasonality** as a sine wave over months.” | `SELECT month, SIN(2 *PI()* month / 12.0) AS seasonality_factor FROM generate_series(1,12) AS month;` | values between -1 and 1 over 12 months 
| cos() | “COS is the cosine twin of SIN; also rarely used.” | Cosine of an angle (in radians). | “Phase‑shift a **seasonal curve** by 90 degrees.” | `SELECT month, COS(2 *PI()* month / 12.0) AS shifted_factor FROM generate_series(1,12) AS month;` | another -1 to 1 wave, shifted relative to SIN 
| acos() | “ACOS is the inverse cosine; extremely niche in SQL analytics.” | Inverse cosine, returning an angle. | “Given a **similarity score**, recover an angle (toy ML example).” | `SELECT sim_score, ACOS(sim_score) AS angle FROM similarities;` | angle in radians; sim_score must be in [-1,1] 
| radians() | “RADIANS converts degrees to radians for trig functions.” | degrees → radians. | “If some source stores **angles in degrees**, convert before SIN/COS.” | `SELECT angle_degrees, RADIANS(angle_degrees) AS angle_rad, SIN(RADIANS(angle_degrees)) AS sin_val FROM angles;` | angle_rad usable with trig; sin_val is sine of that angle 

---

## **Chunk 9 — Nulls & conditional (correctness)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| null | “NULL means ‘unknown / missing’, not zero and not empty.” | NULL = no value; it breaks normal comparisons. | “Some users have **no last_login** yet.” | `SELECT user_id, last_login FROM users WHERE last_login IS NULL;` | only users who never logged in 
| is not null | “IS NOT NULL filters to rows where the value actually exists.” | Checks presence, not content. | “Only users with a known **signup_source**.” | `SELECT * FROM users WHERE signup_source IS NOT NULL;` | rows where signup_source has some value 
| coalesce() | “COALESCE gives me a default when data is missing.” | First non‑NULL value in the list. | “Show **0** when there is no recorded discount.” | `SELECT order_id, COALESCE(discount_amount, 0) AS discount FROM orders;` | no more NULL discounts; they become 0 
| nullif() | “NULLIF turns bad sentinel values into real NULLs.” | Return NULL if two expressions are equal. | “Treat **-1** as ‘unknown’ age instead of real age.” | `SELECT user_id, NULLIF(age, -1) AS age_clean FROM users;` | age_clean is NULL where age was -1 
| case when ... end | “CASE lets me write if/else logic directly in SQL.” | Conditional branching inside a query. | “Bucket users into **LTV tiers**.” | `SELECT user_id, CASE WHEN ltv >= 1000 THEN 'gold' WHEN ltv >= 200 THEN 'silver' ELSE 'bronze' END AS ltv_tier FROM users;` | each user labeled gold / silver / bronze 

---

## **Chunk 10 — Types + arrays + row generation (structure / advanced)**

| **Term** | **Human language (sticky interview sentence)** | **Abstract rule (fast brain)** | **Mini story (case study)** | **Sample SQL** | **Sample output** |
| --- | --- | --- | --- | --- | --- |
| cast() | “CAST makes types match so joins and comparisons behave.” | Convert a value from one type to another. | “IDs stored as **text** in one table, **int** in another.” | `SELECT * FROM a JOIN b ON CAST(a.user_id AS INT) = b.user_id;` | join works instead of silently failing 
| float / decimal / numeric | “I pick data types based on precision vs storage vs safety.” | float ≈, decimal/numeric = exact. | “Use **DECIMAL** for money, FLOAT for metrics.” | CREATE TABLE payments (
  amount DECIMAL(10,2),
  tax_rate FLOAT
); | money is precise; ratios can be approximate |
| array() | “ARRAY lets me build a small list inline.” | Create an array literal. | “Whitelist a few **test user_ids**.” | `SELECT * FROM users WHERE user_id = ANY(ARRAY[101,102,103]);` | only the whitelisted users 
| array_length() | “ARRAY_LENGTH tells me how many elements live inside the array.” | Length of array dimension. | “How many **devices per user**?” | `SELECT user_id, ARRAY_LENGTH(device_ids, 1) AS device_count FROM user_devices;` | device_count = 0,1,2… 
| array_to_string() | “ARRAY_TO_STRING turns arrays into readable labels.” | Join array elements into a string with a delimiter. | “Show **all roles** for a user as one comma string.” | `SELECT user_id, ARRAY_TO_STRING(roles, ', ') AS role_list FROM user_roles;` | roles = {"admin","editor"} → "admin, editor" 
| string_to_array() | “STRING_TO_ARRAY is the reverse: split text into an array.” | String → array on a delimiter. | “Turn **tag string** into an array for containment checks.” | `SELECT article_id, STRING_TO_ARRAY(tags, ',') AS tag_arr FROM articles;` | tag_arr = {"analytics","retention","sql"} 
| unnest() | “UNNEST explodes arrays so each element becomes its own row.” | Expand array into a set of rows. | “One row per **user‑device** pair.” | `SELECT user_id, UNNEST(device_ids) AS device_id FROM user_devices;` | user_id repeated across multiple device_id rows 
| generate_series() | “GENERATE_SERIES creates a virtual table of numbers or dates.” | On‑the‑fly sequence generator. | “Build a **date spine** to left join metrics onto.” | `SELECT d::date AS day FROM GENERATE_SERIES( '2025-01-01', '2025-01-31', INTERVAL '1 day' ) AS d;` | one row per day in January 2025 
) AS d; | one row per day in January 2025 |
| filter() | “FILTER inside aggregates lets me count subsets cleanly.” | Conditionally include rows in aggregate. | “Count **active vs inactive** users in one pass.” | `SELECT COUNT(*) FILTER (WHERE status = 'active') AS active_users, COUNT(*) FILTER (WHERE status = 'inactive') AS inactive_users FROM users;` | two metrics from one scan 
| not in() | “NOT IN removes a small blocked list from results.” | Exclude matches from a value list. | “Drop **internal test accounts** from metrics.” | `SELECT * FROM users WHERE email NOT IN ( '[test@company.com](mailto:test@company.com)', '[qa@company.com](mailto:qa@company.com)' );` | all real users, no test accounts 
); | all real users, no test accounts |