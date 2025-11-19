# Count Unique Active Users

- count unique active users approximately in a given time window

## Approximate Approach

- Redis Hyperloglog Datastructure to store user ids and get a probablistic count of unique active users through the session service
