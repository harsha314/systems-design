import genanki

# === 1️⃣ Define the Anki model (card layout) ===
cassandra_model = genanki.Model(
    2078900110,
    'Cassandra Basic Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div style="font-family: Arial; font-size: 18px;">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr id="answer"><div style="font-family: Arial; font-size: 17px;">{{Answer}}</div>',
        },
    ],
    css="""
        .card {
            font-family: Arial;
            font-size: 16px;
            text-align: center;
        }
    """
)

# === 2️⃣ Define the deck ===
cassandra_deck = genanki.Deck(
    1507432819,
    'Apache Cassandra - Mid-Level Engineer Flashcards'
)

# === 3️⃣ Add flashcards ===
flashcards = [
    ("What kind of database is Apache Cassandra?", "A distributed wide-column NoSQL database."),
    ("What are the key design goals of Cassandra?", "Scalability, high availability, and fault tolerance across many nodes."),
    ("What kind of architecture does Cassandra use?", "A peer-to-peer architecture with no single master node."),
    ("How does Cassandra decide which node stores a given piece of data?", "By hashing the partition key and mapping it to a token range on a node."),
    ("What is the replication factor (RF) in Cassandra?", "The number of nodes that store a copy of each piece of data."),
    ("What does a replication factor of 3 mean?", "Each piece of data is stored on three different nodes."),
    ("What is tunable consistency in Cassandra?", "The ability to choose how many replicas must acknowledge a read or write."),
    ("What does QUORUM consistency mean?", "A majority of replicas (more than half) must respond before success."),
    ("What are the main steps of a write operation in Cassandra?", "Write to commit log → write to memtable → flush to SSTable."),
    ("What is the commit log used for?", "Durability — it ensures data isn’t lost on crash before flush."),
    ("What is a memtable?", "An in-memory structure holding recent writes before being flushed to disk."),
    ("What is an SSTable?", "An immutable on-disk data file that stores persisted rows."),
    ("What is compaction in Cassandra?", "Merging SSTables to remove duplicates and deleted data."),
    ("What is a tombstone in Cassandra?", "A marker indicating a deleted or expired row."),
    ("Why can tombstones cause performance problems?", "They accumulate and slow down reads until compaction removes them."),
    ("What does the CAP theorem say about Cassandra?", "It prioritizes Availability and Partition tolerance over Consistency (AP)."),
    ("Can Cassandra provide strong consistency when needed?", "Yes, by using higher consistency levels (e.g. QUORUM or ALL)."),
    ("What is a “hot partition”?", "A partition that receives disproportionate traffic, causing load imbalance."),
    ("How can you avoid hot partitions?", "Use partition keys that distribute data evenly, avoid sequential keys."),
    ("What is the basic data modeling rule in Cassandra?", "Model tables based on query patterns, not on entity relationships."),
    ("Why are joins avoided in Cassandra?", "It doesn’t support joins efficiently; denormalization is preferred."),
    ("What are clustering keys used for?", "Ordering and efficient range queries within a partition."),
    ("What is “read repair”?", "A process that synchronizes replicas during read operations."),
    ("What is “hinted handoff”?", "Temporarily storing a write for an unavailable node to deliver later."),
    ("What is an “anti-entropy repair”?", "A background process that compares and repairs inconsistencies between replicas."),
    ("What happens if a node fails in Cassandra?", "Other replicas continue serving data, ensuring high availability."),
    ("What does NetworkTopologyStrategy control?", "How data is replicated across multiple data centers."),
    ("Why is Cassandra suitable for globally distributed applications?", "It supports multi-data-center replication and local reads."),
    ("What performance issue can arise from too many SSTables?", "Slow reads due to multiple table lookups per query."),
    ("What is the main purpose of compaction?", "To improve read performance and reclaim space."),
    ("Why is Cassandra often described as “eventually consistent”?", "Because replicas may temporarily diverge but converge over time."),
    ("Why is data modeling critical for Cassandra performance?", "Poor partition key design can cause uneven load or huge partitions."),
    ("What’s one advantage of Cassandra over relational databases?", "Linear scalability with commodity hardware."),
    ("What’s one disadvantage of Cassandra compared to RDBMS?", "No support for complex joins or multi-row transactions."),
    ("Why is Cassandra optimized for writes?", "Writes are sequential (append-only) and don’t require random I/O."),
    ("What tool or language is commonly used to interact with Cassandra?", "CQL — Cassandra Query Language."),
    ("What are common compaction strategies in Cassandra?", "SizeTiered and Leveled Compaction Strategies."),
    ("What JVM-related tuning area is important in Cassandra?", "Garbage collection and heap sizing."),
    ("What are the main components of Cassandra storage?", "Commit log, memtable, SSTable."),
    ("What command is used for cluster operations and repairs?", "nodetool"),
    ("What does nodetool status show?", "Node states, token ownership, and data distribution."),
    ("What is “token range” in Cassandra?", "The hash range a node is responsible for storing."),
    ("What does scaling horizontally mean in Cassandra?", "Adding more nodes to the cluster to increase capacity."),
    ("What is the result of a write with consistency level ONE?", "The client gets success after one replica acknowledges the write."),
    ("What is a “partition key”?", "The key used to determine data placement in the cluster."),
    ("What is the purpose of clustering columns?", "To define ordering of rows within a partition."),
    ("What is the main monitoring goal for Cassandra clusters?", "Ensuring even load, healthy replicas, and consistent latency."),
]

for front, back in flashcards:
    note = genanki.Note(
        model=cassandra_model,
        fields=[front, back]
    )
    cassandra_deck.add_note(note)

# === 4️⃣ Export to .apkg file ===
genanki.Package(cassandra_deck).write_to_file('Apache_Cassandra_Flashcards.apkg')

print("✅ Created 'Apache_Cassandra_Flashcards.apkg'")
