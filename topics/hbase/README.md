Excellent — Apache **HBase** is a great next step for learning about **NoSQL columnar data stores**, especially for handling massive, sparse datasets and time-series data.

Your laptop (8 GB RAM, i5 12th gen) can comfortably run **HBase in standalone mode** for learning purposes.

Below is a **set of 3 progressive HBase projects (beginner → advanced)** with **clear functional and non-functional requirements**, all designed to use **freely available APIs or public datasets**.

---

## 🟢 **Project 1 — IoT Sensor Data Storage & Querying (Beginner)**

**Goal:** Understand HBase data modeling (row keys, column families, schema design) and CRUD operations.

### Functional Requirements

1. Simulate IoT temperature sensors:

   - Use Python to generate data: `{device_id, timestamp, temperature, humidity}` every second.

2. Store data in an HBase table:

   - **Table:** `iot_data`
   - **Row key:** `device_id#timestamp`
   - **Column families:**

     - `metrics:temperature`
     - `metrics:humidity`

3. Write scripts to:

   - Insert sensor readings into HBase using the **HappyBase** Python client.
   - Retrieve:

     - Last 10 readings per device.
     - Average temperature per device (using client-side aggregation).

4. Visualize retrieved data using Matplotlib (optional).

### Non-Functional Requirements

- Run HBase in **standalone mode** (`hbase-daemon.sh start master`).
- Store max 100k records.
- Write latency < 200 ms per operation.
- Keep JVM memory usage ≤ 2 GB.

**You’ll learn:**
HBase shell commands, table creation, data modeling, CRUD via Python (HappyBase).

---

## 🟡 **Project 2 — Real-Time Twitter Feed Archival (Intermediate)**

**Goal:** Work with semi-structured real-time data and time-based row keys.

### Functional Requirements

1. Collect tweets via **Twitter API v2** or **free simulation** (you can replay JSON tweets from a static dataset).
2. Define schema for table `tweets_archive`:

   - **Row key:** `date#tweet_id`
   - **Column families:**

     - `user:username`, `user:followers_count`
     - `tweet:text`, `tweet:language`, `tweet:hashtags`

3. Batch insert tweets (e.g., every 30 seconds).
4. Retrieve:

   - All tweets for a date.
   - Tweets containing specific hashtags.
   - Top users by follower count (basic client-side aggregation).

5. Create an API (Flask/FastAPI) for reading data from HBase.

### Non-Functional Requirements

- Use **HappyBase batch()** to minimize network overhead.
- Up to 1M tweets stored.
- Read latency ≤ 300 ms for 1k rows.
- Configurable retention (delete data older than 7 days).

**You’ll learn:**
Efficient row key design, batch writes, time-series storage, and simple REST data access.

---

## 🔴 **Project 3 — Clickstream Analytics with HBase + Spark (Advanced)**

**Goal:** Integrate HBase with Apache Spark for scalable analytics and aggregations.

### Functional Requirements

1. Use a **public clickstream dataset** such as:

   - [Online Retail Dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/online+retail)
   - Or generate synthetic logs: `{user_id, session_id, timestamp, page, duration}`

2. Store in HBase table `clickstream`:

   - **Row key:** `user_id#timestamp`
   - **Column families:**

     - `session:page`, `session:duration`

3. Use **Spark (PySpark) + HBase Connector** to:

   - Load HBase table as DataFrame.
   - Compute per-user session metrics:

     - Total session duration
     - Most visited pages
     - Average time per page

4. Write aggregated metrics back into another table: `user_metrics`.

### Non-Functional Requirements

- Run Spark in local mode and HBase in standalone mode.
- Batch processing time < 5 minutes for 500k rows.
- Ensure stable HBase connection with Spark connector.
- Modular code: ETL → Analytics → Results writing.

**You’ll learn:**
HBase–Spark integration, data aggregation, efficient schema design, and performance tuning.

---

### 🔼 Suggested Progression

| Level | Project                 | Key Concepts                           |
| :---- | :---------------------- | :------------------------------------- |
| 🟢 1  | IoT Sensor Data Storage | Schema design, CRUD ops                |
| 🟡 2  | Twitter Feed Archival   | Time-based keys, batch writes          |
| 🔴 3  | Clickstream Analytics   | Spark + HBase integration, aggregation |

---

### 🧰 Setup Guide (Local Environment)

**Install HBase (Standalone Mode):**

```bash
wget https://archive.apache.org/dist/hbase/2.5.7/hbase-2.5.7-bin.tar.gz
tar -xzf hbase-2.5.7-bin.tar.gz
cd hbase-2.5.7
```

Edit `conf/hbase-site.xml`:

```xml
<property>
  <name>hbase.rootdir</name>
  <value>file:///tmp/hbase</value>
</property>
<property>
  <name>hbase.zookeeper.property.dataDir</name>
  <value>/tmp/zookeeper</value>
</property>
```

Start HBase:

```bash
./bin/start-hbase.sh
./bin/hbase shell
```

**Python Client:**

```bash
pip install happybase thrift
```

Test connection:

```python
import happybase
connection = happybase.Connection('localhost')
print(connection.tables())
```

---

### ⚡ APIs and Data Sources You Can Use

| Source                                                                               | API Type           | Example Usage                     |
| :----------------------------------------------------------------------------------- | :----------------- | :-------------------------------- |
| [Fake Sensor Data (custom script)](https://pypi.org/project/fake-sensor/)            | Python-generated   | IoT project                       |
| [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api)                  | Free tier          | Tweets project                    |
| [Online Retail Dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/online+retail) | CSV                | Clickstream analytics             |
| [Mockaroo](https://www.mockaroo.com/)                                                | Free synthetic API | Generate tabular clickstream data |

---

Would you like me to turn this into a **structured 8-week learning roadmap** (setup → CRUD → API integration → analytics → Spark integration) like I did for Spark and Elasticsearch? It would make it easy to follow step-by-step.
