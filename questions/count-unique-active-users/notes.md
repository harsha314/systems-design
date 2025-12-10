# Count Unique Active Users

## Requirements

### Functional Requirements

- count unique active users approximately in a given time window

### Non-Functional Requirements

- ...
- ...

## Entities

## APIs

- GET /unique-active-users?start={start_time}&end={end_time}
  - returns the approximate count of unique active users between start_time and end_time
- POST /log-activity
  - logs user activity with user_id and timestamp

## High-Level Design

- Session Service
  - responsible for tracking user sessions and activity.
  - exposes an API to log user activity and retrieve unique active user counts.

## Deep-dives / Low-Level Design

### Approximate Approach

- Redis Hyperloglog Datastructure to store user ids and get a probablistic count of unique active users through the session service
