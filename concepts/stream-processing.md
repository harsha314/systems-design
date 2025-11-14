## Stream Processing

### Usecases

1. Metric/Log time grouping : Grouping into tumbling window, hopping(continuous) window of logs
2. Change Data Capture : Moving data from Database to Search Index

<!-- Draw markdown to show data flow of CDC -->

```mermaid
flowchart TD

    subgraph DB["Source Database"]
        A["Tables(OLTP)"]
    end

    A -->|Row-level Changes (Inserts/Updates/Deletes)| B[CDC Connector (Debezium / Maxwell / GoldenGate)]

    B -->|Change Events (JSON/Avro)| C[Message Broker (Kafka / Pulsar / Kinesis)]

    subgraph StreamProcessing["Stream Processing Engine"]
        D[Stream Processor (Flink / Spark Streaming / Kafka Streams)]
    end

    C -->|Continuous Event Stream| D

    D -->|Transformed or Enriched Streams| E[Sinks (Data Lakes, Warehouses, Search Indexes, Caches)]

    D -->|Materialized or Realtime Views| F[Serving Layer (APIs / Dashboards)]

```
