# Devesh Systems Lab

A structured repository for designing and building distributed systems from first principles.

---

## Overview

This repository focuses on learning system design through implementation.

Each system is:

* Designed with real-world constraints
* Implemented from scratch
* Evaluated under scale and failure scenarios

The goal is to develop a deep understanding of how systems behave beyond theoretical design.

---

## What This Repository Covers

Every system follows a consistent structure:

1. Requirements and constraints
2. High-Level Design (HLD)
3. Low-Level Design (LLD)
4. Implementation (Python)
5. Bottlenecks and scaling challenges
6. Tradeoffs and observations

---

## Systems

* Rate Limiter (in progress)
* URL Shortener (planned)
* Notification System (planned)
* Chat System (planned)

---

## Approach

Systems are built incrementally:

* Start with a simple working design
* Identify bottlenecks under load
* Introduce optimizations
* Evolve toward scalable architectures

This approach emphasizes understanding:

* Why systems fail
* Where scaling breaks
* How tradeoffs impact design decisions

---

## Focus Areas

* Concurrency and asynchronous systems
* Caching and data access patterns
* Event-driven architecture
* Fault tolerance and reliability
* Latency and throughput optimization

---

## Tech Stack

* Python
* FastAPI
* Redis
* Kafka
* PostgreSQL

---

## Repository Structure

```id="repo-structure"
systems/        # Complete system implementations
shared/         # Reusable components (rate limiter, retry, etc.)
infra/          # Infrastructure configurations (Redis, Kafka, Docker)
docs/           # Core system design concepts
experiments/    # Benchmarks, failures, and optimizations
```

---

## Status

Work in progress.

Systems are continuously refined to improve:

* Scalability
* Reliability
* Performance

---

## Purpose

This repository is not a collection of examples.

It is a structured effort to:

* Build real systems
* Understand their limitations
* Improve them through iteration

The focus is on clarity, correctness, and depth.

---
