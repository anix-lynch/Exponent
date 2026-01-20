#!/usr/bin/env python3
"""
Generate short answers for L14 questions using the System Design (Conceptual) framework.
Each answer follows: Components → Data Flow → Boundaries → Scale Considerations
Tailored to each specific question while maintaining the framework structure.
"""

import csv
import re

def detect_system_type(question_text, notes):
    """Detect the type of system being designed from the question."""
    q_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # System type detection
    if any(word in q_lower for word in ['url shortener', 'tinyurl', 'shorten url', 'bitly']):
        return 'url_shortener'
    elif any(word in q_lower for word in ['recommendation', 'recommend', 'personalized', 'ranking']):
        return 'recommendation'
    elif any(word in q_lower for word in ['data pipeline', 'etl', 'data warehouse', 'data lake']):
        return 'data_pipeline'
    elif any(word in q_lower for word in ['messaging', 'chat', 'message', 'whatsapp', 'slack', 'messenger']):
        return 'messaging'
    elif any(word in q_lower for word in ['storage', 'file storage', 'dropbox', 'drive', 's3']):
        return 'storage'
    elif any(word in q_lower for word in ['search', 'search engine', 'typeahead', 'autocomplete']):
        return 'search'
    elif any(word in q_lower for word in ['streaming', 'live', 'twitch', 'youtube live']):
        return 'streaming'
    elif any(word in q_lower for word in ['payment', 'transaction', 'stripe', 'paypal']):
        return 'payment'
    elif any(word in q_lower for word in ['api', 'endpoint', 'rest api']):
        return 'api'
    elif any(word in q_lower for word in ['ml', 'machine learning', 'model', 'ai', 'llm', 'rag']):
        return 'ml_system'
    elif any(word in q_lower for word in ['cache', 'caching', 'redis', 'memcached']):
        return 'cache'
    elif any(word in q_lower for word in ['rate limit', 'rate limiter']):
        return 'rate_limiter'
    elif any(word in q_lower for word in ['load balancer', 'load balance']):
        return 'load_balancer'
    elif any(word in q_lower for word in ['database', 'db', 'nosql', 'sql']):
        return 'database'
    else:
        return 'generic'

def generate_l14_short_answer(question_text, notes):
    """Generate a tailored short answer following L14 framework."""
    
    question_lower = question_text.lower()
    system_type = detect_system_type(question_text, notes)
    
    parts = []
    
    # 1. DEFINE THE GOAL - Tailored to system type
    goal_lines = []
    goal_lines.append("🎯 Define the GOAL: Clarify what problem we're solving")
    
    if system_type == 'url_shortener':
        goal_lines.append("  👥 Primary user goal: shorten long URLs for sharing, trackability, and convenience")
        goal_lines.append("  📊 Success metric: low latency redirects (<50ms), high availability, URL uniqueness")
        goal_lines.append("  🚫 Non-goals: URL expiration, custom aliases, analytics (initially)")
    elif system_type == 'recommendation':
        goal_lines.append("  👥 Primary user goal: surface relevant content/products to users based on preferences")
        goal_lines.append("  📊 Success metric: click-through rate, engagement, relevance score, latency")
        goal_lines.append("  🚫 Non-goals: real-time updates, explainability, A/B testing (initially)")
    elif system_type == 'data_pipeline':
        goal_lines.append("  👥 Primary user goal: process, transform, and deliver data reliably and efficiently")
        goal_lines.append("  📊 Success metric: data freshness, throughput, accuracy, cost per GB")
        goal_lines.append("  🚫 Non-goals: real-time processing, data quality checks (initially)")
    elif system_type == 'messaging':
        goal_lines.append("  👥 Primary user goal: enable real-time communication between users reliably")
        goal_lines.append("  📊 Success metric: message delivery latency, delivery guarantees, availability")
        goal_lines.append("  🚫 Non-goals: video calls, file sharing, group management (initially)")
    elif system_type == 'storage':
        goal_lines.append("  👥 Primary user goal: store and retrieve files reliably with high availability")
        goal_lines.append("  📊 Success metric: upload/download speed, durability, storage cost, availability")
        goal_lines.append("  🚫 Non-goals: file versioning, sharing, search (initially)")
    elif system_type == 'search':
        goal_lines.append("  👥 Primary user goal: quickly find relevant results from large datasets")
        goal_lines.append("  📊 Success metric: search latency, relevance, result ranking quality")
        goal_lines.append("  🚫 Non-goals: autocomplete, spell correction, personalization (initially)")
    elif system_type == 'streaming':
        goal_lines.append("  👥 Primary user goal: deliver live content to viewers with low latency")
        goal_lines.append("  📊 Success metric: stream latency, buffering rate, concurrent viewers, quality")
        goal_lines.append("  🚫 Non-goals: video on demand, chat, monetization (initially)")
    elif system_type == 'payment':
        goal_lines.append("  👥 Primary user goal: process transactions securely and reliably")
        goal_lines.append("  📊 Success metric: transaction success rate, latency, fraud detection, availability")
        goal_lines.append("  🚫 Non-goals: refunds, disputes, multi-currency (initially)")
    elif system_type == 'ml_system':
        goal_lines.append("  👥 Primary user goal: serve ML models with low latency and high accuracy")
        goal_lines.append("  📊 Success metric: inference latency, model accuracy, throughput, cost per prediction")
        goal_lines.append("  🚫 Non-goals: model training, feature engineering, A/B testing (initially)")
    else:
        goal_lines.append("  👥 Primary user goal: what is the main user need or business objective?")
        goal_lines.append("  📊 Success metric: latency, reliability, accuracy, cost, what defines success?")
        goal_lines.append("  🚫 Non-goals: explicitly say what's out of scope, what we're NOT building")
    
    goal_lines.append("  ⚠️ Rule: If the goal isn't clear, architecture will be wrong")
    parts.append("\n".join(goal_lines))
    
    # 2. IDENTIFY CORE COMPONENTS - Tailored to system type
    component_lines = []
    component_lines.append("🧩 Identify CORE COMPONENTS: Define what blocks exist")
    
    if system_type == 'url_shortener':
        component_lines.append("  📱 Clients: web browsers, mobile apps, API consumers")
        component_lines.append("  🔗 API gateway: handle shorten and redirect requests")
        component_lines.append("  🆔 ID generator: create unique short codes (base62, UUID, counter)")
        component_lines.append("  💾 URL store: database mapping short_code → long_url")
        component_lines.append("  💨 Cache: Redis/CDN for hot redirects (read-heavy workload)")
    elif system_type == 'recommendation':
        component_lines.append("  📱 Clients: web, mobile apps requesting recommendations")
        component_lines.append("  🎯 Recommendation service: compute personalized rankings")
        component_lines.append("  👤 User profile store: user preferences, history, behavior")
        component_lines.append("  📦 Item catalog: product/content metadata and features")
        component_lines.append("  🤖 ML models: ranking algorithms, collaborative filtering, embeddings")
    elif system_type == 'data_pipeline':
        component_lines.append("  📥 Ingestion: batch jobs, stream processors, API collectors")
        component_lines.append("  ⚙️ Processing: ETL/ELT engines (Spark, Flink, Dataflow)")
        component_lines.append("  💾 Storage: data lake (S3), warehouse (Snowflake), staging DB")
        component_lines.append("  📊 Transformation: data cleaning, aggregation, enrichment")
        component_lines.append("  📈 Orchestration: schedulers (Airflow), workflow managers")
    elif system_type == 'messaging':
        component_lines.append("  📱 Clients: mobile apps, web clients sending/receiving messages")
        component_lines.append("  💬 Message service: handle send, receive, delivery status")
        component_lines.append("  📨 Message queue: Kafka/RabbitMQ for reliable delivery")
        component_lines.append("  💾 Message store: database for message history and metadata")
        component_lines.append("  🔔 Presence service: track online/offline status, push notifications")
    elif system_type == 'storage':
        component_lines.append("  📱 Clients: web, mobile apps uploading/downloading files")
        component_lines.append("  📤 Upload service: handle file uploads, chunking, validation")
        component_lines.append("  💾 Object storage: S3/GCS for file storage, metadata DB")
        component_lines.append("  🔄 Replication: ensure durability across regions")
        component_lines.append("  📥 CDN: cache popular files for fast downloads")
    elif system_type == 'search':
        component_lines.append("  📱 Clients: search UI, API consumers")
        component_lines.append("  🔍 Search service: query processing, ranking, result assembly")
        component_lines.append("  📚 Index: inverted index, document store, ranking data")
        component_lines.append("  🔄 Indexer: crawl, parse, and build search indexes")
        component_lines.append("  💨 Cache: popular queries, autocomplete suggestions")
    elif system_type == 'streaming':
        component_lines.append("  📱 Clients: viewers on web, mobile, TV apps")
        component_lines.append("  🎥 Encoder: transcode video to multiple quality levels")
        component_lines.append("  📡 CDN: deliver video chunks to viewers globally")
        component_lines.append("  📊 Analytics: track views, engagement, quality metrics")
        component_lines.append("  💾 Origin server: store master video files")
    elif system_type == 'payment':
        component_lines.append("  📱 Clients: merchants, payment gateways, mobile apps")
        component_lines.append("  💳 Payment processor: authorize, capture, settle transactions")
        component_lines.append("  🏦 Bank gateway: communicate with payment networks")
        component_lines.append("  🔒 Fraud detection: ML models to detect suspicious transactions")
        component_lines.append("  💾 Transaction store: database for transaction history, reconciliation")
    elif system_type == 'ml_system':
        component_lines.append("  📱 Clients: applications making inference requests")
        component_lines.append("  🤖 Model serving: load models, handle inference requests")
        component_lines.append("  📊 Feature store: serve features for model input")
        component_lines.append("  ⚙️ Preprocessing: data transformation, feature engineering")
        component_lines.append("  📈 Monitoring: track model performance, drift, latency")
    else:
        component_lines.append("  📱 Clients: web, mobile, internal tools, what are the entry points?")
        component_lines.append("  📥 Ingestion: APIs, SDKs, event collectors, how does data enter?")
        component_lines.append("  ⚙️ Processing: sync vs async, how is data processed?")
        component_lines.append("  💾 Storage: hot / warm / cold, where is data stored?")
        component_lines.append("  🖥️ Compute: stateless vs stateful, how is computation handled?")
    
    component_lines.append("  ⚠️ Rule: Name boxes before wiring arrows")
    parts.append("\n".join(component_lines))
    
    # 3. DATA FLOW - Tailored to system type
    flow_lines = []
    flow_lines.append("🔄 Data FLOW: Describe how data moves end-to-end")
    
    if system_type == 'url_shortener':
        flow_lines.append("  ✍️ Write path: client → API → generate short_code → store (DB) → cache")
        flow_lines.append("  📖 Read path: client → API → cache lookup → DB fallback → redirect")
        flow_lines.append("  ⏳ Async: analytics pipeline (track clicks, generate reports)")
        flow_lines.append("  ❌ Failure: cache miss → DB timeout → return error or default")
    elif system_type == 'recommendation':
        flow_lines.append("  📖 Request path: client → API → fetch user profile → compute recommendations → rank → return")
        flow_lines.append("  ✍️ Write path: user actions → event stream → update user profile → retrain models (async)")
        flow_lines.append("  ⏳ Async: model training, feature computation, index updates")
        flow_lines.append("  ❌ Failure: model unavailable → fallback to popularity-based, cache stale results")
    elif system_type == 'data_pipeline':
        flow_lines.append("  📥 Ingest: source systems → message queue → batch/stream processor")
        flow_lines.append("  ⚙️ Transform: raw data → cleaned → transformed → aggregated → loaded")
        flow_lines.append("  💾 Store: processed data → data warehouse → serve to dashboards/APIs")
        flow_lines.append("  ❌ Failure: retry failed jobs, dead letter queue, data quality checks")
    elif system_type == 'messaging':
        flow_lines.append("  ✍️ Send: sender → message service → queue → store → push to recipient")
        flow_lines.append("  📖 Receive: recipient → message service → fetch from store → deliver")
        flow_lines.append("  ⏳ Async: offline message delivery, read receipts, typing indicators")
        flow_lines.append("  ❌ Failure: message retry, dead letter queue, delivery status tracking")
    elif system_type == 'storage':
        flow_lines.append("  📤 Upload: client → upload service → chunk file → store in object storage → update metadata")
        flow_lines.append("  📥 Download: client → CDN check → object storage → stream to client")
        flow_lines.append("  ⏳ Async: file replication, thumbnail generation, virus scanning")
        flow_lines.append("  ❌ Failure: upload retry, partial upload resume, storage replication")
    else:
        flow_lines.append("  📖 Request path (read): how do read requests flow through the system?")
        flow_lines.append("  ✍️ Write path (create/update): how do write requests flow through?")
        flow_lines.append("  ⏳ Async paths: queues, streams, retries, how are async ops handled?")
        flow_lines.append("  ❌ Failure paths: timeouts, backpressure, how are failures handled?")
    
    flow_lines.append("  ⚠️ Rule: Always describe the happy path first")
    parts.append("\n".join(flow_lines))
    
    # 4. BOUNDARIES & CONSTRAINTS - Tailored to system type
    boundary_lines = []
    boundary_lines.append("🚧 Boundaries & CONSTRAINTS: Identify what limits us")
    
    if system_type == 'url_shortener':
        boundary_lines.append("  ⏱️ Latency: redirects must be <50ms (read-heavy, cache-first)")
        boundary_lines.append("  🔒 Consistency: strong consistency on writes (URL uniqueness)")
        boundary_lines.append("  📈 Throughput: 100M redirects/day, 1K writes/sec")
        boundary_lines.append("  💰 Cost: minimize storage (short codes are small), maximize cache hit rate")
    elif system_type == 'recommendation':
        boundary_lines.append("  ⏱️ Latency: recommendations must be <100ms (user-facing)")
        boundary_lines.append("  🔒 Consistency: eventual consistency OK (user profiles update async)")
        boundary_lines.append("  📈 Throughput: 1M requests/sec during peak, handle cold starts")
        boundary_lines.append("  💰 Cost: balance model complexity vs inference cost")
    elif system_type == 'data_pipeline':
        boundary_lines.append("  ⏱️ Latency: batch processing acceptable (hourly/daily), not real-time")
        boundary_lines.append("  🔒 Consistency: eventual consistency OK, data freshness SLA")
        boundary_lines.append("  📈 Throughput: handle TB/PB scale, process within time window")
        boundary_lines.append("  💰 Cost: optimize compute costs, use spot instances where possible")
    elif system_type == 'messaging':
        boundary_lines.append("  ⏱️ Latency: message delivery <1s for online users")
        boundary_lines.append("  🔒 Consistency: at-least-once delivery guarantee, message ordering")
        boundary_lines.append("  📈 Throughput: 1M messages/sec, handle message bursts")
        boundary_lines.append("  💰 Cost: optimize storage (message retention policies)")
    elif system_type == 'storage':
        boundary_lines.append("  ⏱️ Latency: upload/download speed, minimize time to first byte")
        boundary_lines.append("  🔒 Consistency: strong consistency for metadata, eventual for replication")
        boundary_lines.append("  📈 Throughput: handle large files, concurrent uploads/downloads")
        boundary_lines.append("  💰 Cost: optimize storage costs (tiering, compression, deduplication)")
    else:
        boundary_lines.append("  ⏱️ Latency SLOs: what are the latency requirements?")
        boundary_lines.append("  🔒 Consistency: strong vs eventual consistency?")
        boundary_lines.append("  📈 Throughput: how many requests per second must we handle?")
        boundary_lines.append("  💰 Cost ceilings: what are the budget constraints?")
    
    boundary_lines.append("  ⚠️ Rule: Constraints shape architecture more than features")
    parts.append("\n".join(boundary_lines))
    
    # 5. SCALE & FAILURE MODES - Tailored to system type
    scale_lines = []
    scale_lines.append("📈 Scale & FAILURE MODES: Consider what breaks at 10×")
    
    if system_type == 'url_shortener':
        scale_lines.append("  🐌 Bottlenecks: DB becomes bottleneck on writes, cache misses on reads")
        scale_lines.append("  ⚠️ Single points: ID generator, database, cache")
        scale_lines.append("  🚦 Backpressure: rate limit writes, queue redirects if cache down")
        scale_lines.append("  💨 Caching: cache 80%+ of redirects, use CDN for global distribution")
        scale_lines.append("  🔀 Sharding: shard by short_code hash, replicate DB for reads")
    elif system_type == 'recommendation':
        scale_lines.append("  🐌 Bottlenecks: model inference, feature store lookups, ranking computation")
        scale_lines.append("  ⚠️ Single points: model serving, feature store, user profile DB")
        scale_lines.append("  🚦 Backpressure: queue requests, return cached/stale recommendations")
        scale_lines.append("  💨 Caching: cache popular recommendations, pre-compute for hot users")
        scale_lines.append("  🔀 Sharding: shard user profiles, distribute model serving")
    elif system_type == 'data_pipeline':
        scale_lines.append("  🐌 Bottlenecks: processing time, storage I/O, network bandwidth")
        scale_lines.append("  ⚠️ Single points: orchestrator, data warehouse, source systems")
        scale_lines.append("  🚦 Backpressure: queue jobs, parallelize processing, auto-scale workers")
        scale_lines.append("  💨 Caching: cache intermediate results, materialized views")
        scale_lines.append("  🔀 Partitioning: partition data by time/region, process in parallel")
    elif system_type == 'messaging':
        scale_lines.append("  🐌 Bottlenecks: message queue, message store, push notification service")
        scale_lines.append("  ⚠️ Single points: message queue, database, push service")
        scale_lines.append("  🚦 Backpressure: queue messages, rate limit sends, batch notifications")
        scale_lines.append("  💨 Caching: cache recent messages, user presence, connection state")
        scale_lines.append("  🔀 Sharding: shard by user_id, partition message queues")
    elif system_type == 'storage':
        scale_lines.append("  🐌 Bottlenecks: object storage I/O, metadata DB, network bandwidth")
        scale_lines.append("  ⚠️ Single points: object storage, metadata DB, upload service")
        scale_lines.append("  🚦 Backpressure: rate limit uploads, queue large files, throttle downloads")
        scale_lines.append("  💨 Caching: CDN for popular files, cache metadata")
        scale_lines.append("  🔀 Sharding: shard by file_id, replicate across regions")
    else:
        scale_lines.append("  🐌 Bottlenecks: DB, network, fan-out, where will it slow down?")
        scale_lines.append("  ⚠️ Single points of failure: what components have no redundancy?")
        scale_lines.append("  🚦 Backpressure: how do we handle overload?")
        scale_lines.append("  💨 Caching: where can we cache to reduce load?")
        scale_lines.append("  🔀 Sharding / partitioning: how do we distribute data?")
    
    scale_lines.append("  ⚠️ Rule: Talk about failure BEFORE optimization")
    parts.append("\n".join(scale_lines))
    
    # Join with double newlines (blank line between sections)
    return "\n\n".join(parts)


def process_l14_csv(input_file, output_file):
    """Process L14 CSV and add/update short_answer column."""
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # Get original fieldnames and remove duplicates
        original_fieldnames = list(reader.fieldnames)
        seen = set()
        fieldnames = []
        for field in original_fieldnames:
            if field not in seen:
                fieldnames.append(field)
                seen.add(field)
        
        # Add short_answer if it doesn't exist
        if 'short_answer' not in fieldnames:
            fieldnames.append('short_answer')
        
        for row in reader:
            short_answer = generate_l14_short_answer(row['question_text'], row.get('notes', ''))
            row['short_answer'] = short_answer
            rows.append(row)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {len(rows)} tailored short answers in {output_file}")


if __name__ == '__main__':
    input_file = 'pattern_bank_answered/25_L14_system_design_conceptual.csv'
    output_file = 'pattern_bank_answered/25_L14_system_design_conceptual.csv'
    process_l14_csv(input_file, output_file)
