# Multi-Agent AI Real Estate Assistant

A production-oriented multi-agent AI system for natural-language
property search, market analytics, semantic recommendations, and
real-estate knowledge retrieval.

> 🚧 Currently in development — Week 2

This project is being developed as part of an AI Agentic Engineering
internship. The system is built incrementally, with new agent
capabilities added throughout the program.

---

## Overview

The goal of this project is to build a conversational real-estate
assistant that combines AI agents with structured MLS data.

Rather than relying on a single agent for every task, the system is
designed around specialized agents responsible for different
capabilities such as property search, market analysis,
recommendations, and knowledge retrieval.

As development progresses, these agents will be coordinated through
a multi-agent orchestration layer and exposed through conversational
interfaces.

---

## 12-Week Roadmap & Current Progress

| Status | Week | Module | Primary Focus |
|:---:|:---:|---|---|
| ✅ | Week 0 | Environment Setup | OpenClaw install, MySQL import, WhatsApp config, API keys |
| ✅ | Week 1 | Architecture Fundamentals | OpenClaw runtime, skills, sessions, tool calling, memory |
| 🚧 | Week 2 | NL Property Search | NLP query parsing over `rets_property` |
| ⬜ | Week 3 | Database Integration | Parameterized MySQL queries, pagination, result formatting |
| ⬜ | Week 4 | Conversational Agent | Multi-turn session memory, follow-up handling |
| ⬜ | Week 5 | Market Analytics | SQL aggregations over `california_sold` comps data |
| ⬜ | Week 6 | Embeddings & Vector Search | Semantic property matching with OpenAI embeddings |
| ⬜ | Week 7 | Recommendation Engine | Similarity scoring across `rets_property` & sold comps |
| ⬜ | Week 8 | RAG Pipeline | Document-aware agent with MLS field definitions |
| ⬜ | Week 9 | Multi-Agent Orchestration | Coordinator routing across all specialized agents |
| ⬜ | Week 10 | WhatsApp Layer | End-to-end WhatsApp AI communication interface |
| ⬜ | Week 11 | Email Agents & Safety | Automated email workflows with approval guardrails |
| ⬜ | Week 12 | Capstone Demo | Full production multi-agent assistant presentation |

---

## Planned Architecture

```text
                           User
                             │
                             ▼
                    Communication Layer
                     (WhatsApp / Email)
                             │
                             ▼
                  Multi-Agent Orchestrator
                             │
        ┌─────────┬──────────┼─────────┬─────────┐
        │         │          │         │         │
        ▼         ▼          ▼         ▼         ▼
    Property    Market    Recomm.     RAG      Email
     Search    Analytics   Agent     Agent     Agent
      Agent     Agent                  │
        │         │          │         ▼
        │         │          │  Knowledge Sources
        │         │          │
        └─────────┴──────────┘
                  │
                  ▼
             Data Layer
        Active + Historical
             MLS Records
```
