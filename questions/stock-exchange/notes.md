# Stock Exchange

## Requirements

### Functional Requirements

- Users should be able to place orders to buy and sell stocks.
- Users should be able to view real-time stock prices.

### Non-Functional Requirements

- Highly Consistent Transactions with minimal latency.
- Scale to handle around 1 million concurrent users.
- minimize connections to the central stock exchange system.

## Entities

## High-Level Design

1. Pricing Service

- uses volume-weighted average price (VWAP) to determine stock prices.
- aggregates data from multiple sources to provide accurate pricing.

1. Order Management Service
1. User Service

## Deepdives / Low-Level Design

1. Pricing Service

- uses web-sockets to provide real-time updates to users.
- uses caching to most queried stock prices.

1. Order Management Service
1. User Service
