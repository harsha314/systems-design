# Stream Processing

## Usecases

1. Metric/Log time grouping : Grouping into tumbling window, hopping(continuous) window of logs
2. Change Data Capture : Moving data from Database to Search Index
3. Event Sourcing : Storing events in an event store and projecting views from them

## Message Processing

1. Exactly Once per message : Idempotence, 2-Phase Commit
2. Atleast Once per message : Fault Tolerance Brokers, Disk Persistence and Consumer Acknowledgements

## Message Broker Types

1. In-memory Broker : RabbbitMQ, ActiveMQ, Amaazon SQS
2. Log-based Broker : Apache Kafka, Amazon Kinesis
