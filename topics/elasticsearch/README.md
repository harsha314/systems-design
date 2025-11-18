# Elasticsearch

## Core Concepts

### Document & Index

- **Document** Store
- **Index** : Collection of Documents

### Mapping

- Schema definition consisting of fields and their data types
- Text, Keyword, Date, Number, Boolean, Geo-point, etc.
- Text vs Keyword:
  - Text: Analyzed for full-text search
  - Keyword: Not analyzed, for exact matches, sorting, aggregations

### Search Index

- Foundation of ES search — maps each token → list of docs containing it.
- Inverted index for fast full-text search.

#### **Ranking Algorithms**

- **TF-IDF (old versions)**
- **BM25 (default)**

  - Improves scoring by accounting for term saturation.

- **Reciprocal Rank Fusion** :

---

## REST API Operations

- **Create Index** : PUT /{index}
  body : {"mappings": { ... }, "settings": { ... } }
- **Add Document** : POST /{index}/\_doc :
  body: { "field1": "value1", "field2": "value2", ... }
- **Search Documents** : GET /{index}/\_search :
  body: { "query": { ... }, "aggs": { ... } }
- **Update Document** : POST /{index}/\_update/{id} :
  body: { "doc": { "field": "new_value" } }
- **Update Document by version** :
  POST /{index}/\_update/{id}?if_seq_no={seq_no}&if_primary_term={primary_term} :
  body: { "doc": { "field": "new_value" } }

---

## Search Queries

- **Match Query (full-text)** : Uses analyzers, token filters, stemming.
- **Term Query (exact value match)** : No analysis — used for keyword fields.
- **Bool Query (must, should, filter)** : Most common enterprise search pattern.
- **Aggregations** : Equivalent of SQL GROUP BY.

  - `terms` – top values
  - `date_histogram` – time series
  - `avg`, `sum`, `max`, `cardinality`

- **Autocomplete / Suggestions**

  - Completion suggester
  - N-gram analyzers

## Distributed Architecture

### **Shards & Replicas**

- **Primary shard** → handles indexing
- **Replica shards** → serve reads, provide HA
- Default: 1 shard, 1 replica.

### **How Elasticsearch scales**

- Scale **horizontally** by adding more nodes.
- Cluster automatically distributes shards.

### **What SDE-II interviewers expect**

- Ability to explain **shard allocation**, **cluster rebalance**.
- Understanding of **write amplification** & **segment merges**.
- How ES ensures **near real-time** search.

## Elasticsearch Hands-On Projects

### 🔍 **Project 1 — News Article Search Engine (Beginner)**

**Goal:** Learn core Elasticsearch concepts — indexing, querying, and ranking text data.

#### Functional Requirements

1. Collect data from a **free News API** such as:

   - [NewsData.io](https://newsdata.io/) or [GNews](https://gnews.io/)

2. Create an Elasticsearch index `news_articles` with fields:

   - `title`, `content`, `source`, `published_at`, `category`

3. Ingest at least 1,000 news articles via Elasticsearch REST API or `elasticsearch-py`.
4. Implement keyword search with:

   - Full-text search (`match`, `multi_match`)
   - Filters by date or category

5. Return top 10 relevant results for a given query (e.g., _“AI regulation”_).

#### Non-Functional Requirements

- Run **Elasticsearch locally via Docker** (`docker run elasticsearch:8.x`).
- Indexing time ≤ 2 minutes for 1k documents.
- Search latency ≤ 300 ms per query.
- Data stored in JSON format.
- Lightweight UI (optional) — simple Flask app for searching.

**You’ll learn:**
Indexing, analyzers, tokenizers, mapping, search scoring, REST APIs.

---

### ⚙️ **Project 2 — Twitter or Reddit Trend Analyzer (Intermediate)**

**Goal:** Work with real-time data ingestion and analytics queries.

#### Functional Requirements

1. Fetch live or recent posts using:

   - **Twitter API v2 (free tier)** or **Reddit JSON API** (no key needed).

2. Create an index `social_trends` with fields:

   - `platform`, `username`, `text`, `timestamp`, `sentiment`

3. Stream data every few seconds and index into Elasticsearch.
4. Run analytics queries:

   - Top 10 trending keywords (via `terms` aggregation)
   - Average sentiment per topic
   - Time-based histogram of posts

5. Expose REST endpoints for queries (via Flask/FastAPI).

#### Non-Functional Requirements

- Micro-batch indexing (e.g., 100 documents/second max).
- Elasticsearch heap ≤ 2 GB.
- Auto-delete documents older than 7 days (Index Lifecycle Management or cron cleanup).
- Logging + error handling for failed API calls.

**You’ll learn:**
Bulk indexing, aggregations, simple NLP preprocessing, working with streaming APIs.

---

### 🧠 **Project 3 — Product Search & Recommendation Engine (Advanced)**

**Goal:** Combine structured + unstructured data with ranking and suggest features.

### Functional Requirements

1. Use a public **e-commerce dataset**, e.g.:

   - [Kaggle’s Amazon Product Data](https://www.kaggle.com/datasets?search=amazon+product)
   - Or [Fake Store API](https://fakestoreapi.com/)

2. Create an index `products` with fields:

   - `title`, `description`, `price`, `category`, `rating`, `review_count`

3. Implement:

   - **Full-text search** (title + description)
   - **Category filter + price range**
   - **Autocomplete** (completion suggester)
   - **“More like this”** product recommendations

4. Build a small web UI for search and suggestions (Flask/React).

#### Non-Functional Requirements

- Support 100k documents (subset large datasets if needed).
- Response time < 400 ms for search.
- Use proper analyzers (lowercase, stopwords, n-grams for autocomplete).
- Scalable mapping — index template for future categories.

**You’ll learn:**
Advanced queries, custom analyzers, suggesters, relevancy tuning, ranking, UI integration.

---

#### 🔼 Suggested Progression

| Level | Project                          | Key Concepts                       |
| :---- | :------------------------------- | :--------------------------------- |
| 🟢 1  | News Article Search              | Indexing & full-text search        |
| 🟡 2  | Twitter/Reddit Trend Analyzer    | Aggregations & real-time ingestion |
| 🔴 3  | Product Search & Recommendations | Advanced queries & suggesters      |

---

#### 🧰 Setup Notes

- **Elasticsearch Local Setup:**

  ```bash
  docker run -d --name elasticsearch -p 9200:9200 \
  -e "discovery.type=single-node" \
  -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" \
  elasticsearch:8.15.0
  ```

- **Python Client:**

  ```bash
  pip install elasticsearch requests pandas flask
  ```

- **Test API Call:**

  ```bash
  curl -X GET "localhost:9200/_cluster/health?pretty"
  ```

---

Would you like me to extend this into a **structured 8-week learning plan** (with setup, data ingestion, querying, analytics, and UI milestones) — similar to what I did for Spark?
