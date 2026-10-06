# Week 1: OpenClaw Architecture Fundamentals

## Deliverable

**Architecture documentation with a workflow diagram showing how user queries flow from WhatsApp through OpenClaw skills to the MLS databases.**

## 1. Overview

Users can ask questions through WhatsApp message. OpenClaw receives the message, decides what skill or tool is good, and gets information from the MLS database. After that, it sends the result back to the user through WhatsApp.

## 2. Workflow Diagram

```text
User
  |
  | User sends a message
  ↓ 
WhatsApp
  |
  | Message enters OpenClaw
  ↓
OpenClaw Runtime / Orchestrator
  |
  | Orchestrator handles the request
  ↓
Skill Select
  |
  | A skill is selected
  ↓
Tool Execute
  |
  | A tool is executed
  ↓
MLS MySQL Database
  |
  | MLS data is retrieved
  ↓
Session / Memory Update
  |
  | Session / Memory is updated
  ↓
Response Generate
  |
  | Response is sent through WhatsApp
  ↓
WhatsApp
  |
  | Send it to the user
  ↓
User
```
