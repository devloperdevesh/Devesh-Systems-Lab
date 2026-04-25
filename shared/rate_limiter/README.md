# Rate Limiter (Token Bucket)

## Overview

This project implements a production-inspired rate limiter using the Token Bucket algorithm.

It is designed to:

* Control API traffic
* Prevent abuse
* Handle burst requests efficiently

---

## Features

* Per-user rate limiting
* Token Bucket algorithm
* FastAPI integration
* Supports burst traffic

---

## System Architecture

```
Client → API (FastAPI) → RateLimiter → TokenBucket → Decision (Allow / Reject)
```

---

## How It Works

1. Each user is assigned a Token Bucket
2. Every request consumes one token
3. Tokens are refilled over time
4. If tokens are available → request is allowed
5. If tokens are exhausted → request is rejected (HTTP 429)

---

## Core Idea

The system models rate limiting as a bucket of tokens:

* Tokens represent allowed requests
* Tokens refill at a fixed rate
* Requests are processed only if tokens are available

---

## Limitations

* In-memory implementation (not shared across instances)
* Not suitable for distributed systems
* No persistence layer

---

## Future Improvements

* Redis-based distributed rate limiter
* Global rate limiting across multiple services
* Load testing and benchmarking
* Observability (logging and metrics)

---

## Learnings

* Rate limiting strategies (Token Bucket vs Leaky Bucket)
* Handling burst traffic in real systems
* Tradeoffs between performance and accuracy
* Importance of shared state in distributed systems

---

## How to Run

```
python -m uvicorn app.main:app --reload
```

Test endpoint:

```
http://127.0.0.1:8000/test?user_id=dev
```

---

## Goal

To build real-world system design skills by implementing and scaling backend systems step by step.
