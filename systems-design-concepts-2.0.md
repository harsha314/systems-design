
# System Design Topics

- [Youtube Playlist](https://www.youtube.com/playlist?list=PLjTveVh7FakLdTmm42TMxbN8PvVn5g4KJ)

## DB Indexes

### Hash Indexes

### B-Tree Indexes

### LSM Tree + SSTable Indexes

## ACID Transactions

### Read Committed Isolation

### Snapshot Isolation

### Write Skew and Phantom Skew

### Achieving ACID : Serial Execution

### Two Phase Locking

### Serializable Snapshot Isolation

## Column Oriented Storage

- column oriented storage can take column specific compressions like parquet file format to compress the column and only decompress the data only when the column data is requested
- usually uses LSM-Tree + SSTable Index
- Examples : Apache HBase, Apache Cassandra

## Data Serialization Frameworks

## Replication

### Intro to Replication

### Dealing with Stale reads

### Single Leader Replication

### Multi Leader Replication

### Dealing with Write Conflicts

### Conflit Free Replicated Data Types

### Leaderless Replication

### Quorums

## Introduction to Partitioning

### Two Phase Commit - Distributed Transactions

### Consistent Hashing - Rebalancing Partitions

### Linearizable Databases

## Distributed Consensus

### Zookeeper

## SQL vs NoSQL

### MySQL vs PostgreSQL

### VoltDB

### Google Spanner

### MongoDB vs Apache Cassandra

### HBase vs Cassandra

### MapReduce

### Apache Spark

## Stream Processing

### Message Queues

### Apache Flink

## Search Indexes

### ElasticSearch

## Time Series Databases

## Graph Databases

## Geospatial Indexes

## Distributed Caching

### Distributed Cache Writes

### Cache Evictions

### Redis vs Memcached

### Content Delivery Networks

## Object Stores

## Load Balancing

## TCP vs UDP

## Long Polling, Websockets, Server Sent Events

## Monoliths vs Microservice Architecture

# Common System Design Questions

1. URL Shortener
1. Twitter/Instagram
1. Whatsapp
1. Web Crawler
1. Youtube/Netflix
1. Amazon
1. Uber/Lyft
1. Notification Service
1. In-memory Key-Value Store
1. Scalable Log & Monitoring System
