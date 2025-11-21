# **Elasticsearch — Amazon SDE II Interview Notes (Improved Edition)**

These notes are optimised for **Amazon SDE II** system design + troubleshooting interviews, focusing on depth, clarity, and real-world production concepts.

---

# ✅ **1. Core Concepts**

## **Document & Index**

- Elasticsearch stores data as **JSON documents**.
- **Index** = logical namespace containing documents.
- Each index internally contains **multiple shards**.

## **Mapping (Schema)**

Defines field types and how they are indexed.

- **Text** → analyzed for full‑text search.
- **Keyword** → not analyzed; for exact match, sort, aggregations.
- Other types: number, boolean, date, geo-point, nested, object.
- Mapping must be carefully designed — otherwise search results become inconsistent.

## **Inverted Index**

Foundation of ES search — maps each token → list of docs containing it.

---

# ✅ **2. Lucene & Scoring Fundamentals**

Elasticsearch is built on **Apache Lucene**.

## **Ranking Algorithms**

- **TF-IDF (old versions)**
- **BM25 (default)**

  - Improves scoring by accounting for term saturation.

## **Why this matters in interviews**

You may be asked:

- _"How does Elasticsearch decide which document is more relevant?"_
- _"Why is keyword exact match not returning expected results?"_

---

# ✅ **3. CRUD & Important REST APIs**

| Operation              | API Example                         |
| ---------------------- | ----------------------------------- |
| Create Index           | `PUT /products`                     |
| Insert Document        | `POST /products/_doc`               |
| Bulk Insert            | `POST /_bulk`                       |
| Search                 | `POST /products/_search`            |
| Update                 | `POST /products/_update/{id}`       |
| Optimistic Concurrency | Use `if_seq_no` + `if_primary_term` |

---

# ✅ **4. Search Queries You Should Know**

## **Match Query (full-text)**

Uses analyzers, token filters, stemming.

## **Term Query (exact value match)**

No analysis — used for keyword fields.

## **Bool Query (must, should, filter)**

Most common enterprise search pattern.

## **Aggregations**

Equivalent of SQL GROUP BY.

- `terms` – top values
- `date_histogram` – time series
- `avg`, `sum`, `max`, `cardinality`

## **Autocomplete / Suggestions**

- Completion suggester
- N-gram analyzers

---

# ✅ **5. Distributed Architecture (Amazon-style interview focus)**

## **Shards & Replicas**

- **Primary shard** → handles indexing
- **Replica shards** → serve reads, provide HA
- Default: 1 shard, 1 replica.

## **How Elasticsearch scales**

- Scale **horizontally** by adding more nodes.
- Cluster automatically distributes shards.

## **What SDE-II interviewers expect**

- Ability to explain **shard allocation**, **cluster rebalance**.
- Understanding of **write amplification** & **segment merges**.
- How ES ensures **near real-time** search.

---

# ✅ **6. Near Real‑Time (NRT) Search**

Elasticsearch is not immediately consistent.

### Why?

- Writes go to in‑memory buffer.
- Refresh interval (default 1s) creates a new search segment.

### Interview Question

_"Why does Elasticsearch not show my recently indexed document immediately?"_
→ Because refresh interval controls visibility, not commit.

---

# ✅ **7. Performance Best Practices**

## **Avoid Deep Pagination**

- `from + size` is expensive (linear skip).
- Use **search_after** or **scroll API** for deep traversal.

## **Bulk API**

- Use `_bulk` to index 5k–10k docs per batch.
- Prevents small write overhead.

## **Fielddata & Keyword fields**

- Sorting on `text` fields causes expensive fielddata loading.
- Always define `.keyword` subfield.

## **Use Filters for Caching**

- Filters (`filter` clause in bool query) are cached.
- Must/should affects scoring → not cached.

---

# ✅ **8. Reliability, Fault Tolerance & Failure Modes**

### **Scenario: Node Failure**

- Replica becomes primary.
- Cluster reallocates missing replicas.
- Temporary **yellow → green** cluster state.

### **Scenario: Split Brain (old versions)**

Solved using **Zen Discovery** and quorum-based master election.

### **Scenario: Slow Searches**

- Too many shards on single node.
- Inefficient mapping.
- Uncached aggregations.

### **Scenario: OutOfMemoryError**

- Large aggregations → heap pressure.
- Too many fields → fielddata explosion.

---

# ✅ **9. Real-World System Design Topics**

## **1. Designing a Search System for Amazon Products**

Be ready to explain:

- Document modeling
- Analyzers for multilingual support
- Synonym handling
- Autocomplete strategy
- Ranking signals (BM25 + business rules)
- Caching layer (Redis before ES)
- Write pipeline using Kafka → Logstash → ES

## **2. Handling 1M Queries per Second**

Expect to discuss:

- Hot/warm architecture
- Index lifecycle management (ILM)
- Tiered storage
- Replicas for read scaling

## **3. Monitoring & Observability**

Mention:

- Slow logs
- Cluster stats
- Elasticsearch cat APIs (`/_cat/indices`, `/_cat/nodes`)

---

# ✅ **10. Common Pitfalls**

### **❌ Why match query fails to match**

Because field is `keyword`, so it’s not analyzed.

### **❌ Why sorting on text fields is slow**

ES must load full fielddata into heap.

### **❌ Incorrect shard count**

Too many shards = overhead
Too few shards = cannot scale horizontally

### **❌ Wrong mapping leads to reindexing**

Mappings are immutable — types cannot be changed.

---

# ✅ **11. Elasticsearch Internals (for strong candidates)**

## **Segments**

- Data stored as immutable segment files.
- Merge policy merges small segments → optimized search.

## **Write Path**

1. Write to transaction log
2. Write to in‑memory buffer
3. Refresh → creates segment
4. Flush → persists to disk

## **Read Path**

1. Query is broadcast to relevant shards
2. Each shard computes scores
3. Coordinator node merges results
