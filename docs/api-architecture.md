# F.R.I.D.A.Y API Architecture v1

## Goal

Create a central backend that powers all F.R.I.D.A.Y clients.

Clients:

* Mobile App
* Web App
* Telegram Bot
* Desktop App (Future)

---

## Architecture

Clients

↓

API Layer

↓

Core Services

├── Memory Engine
├── Tool Engine
├── Document Engine
└── Model Engine

↓

Database

---

## Request Flow

User Message

↓

API

↓

Memory Retrieval

↓

Tool Check

↓

Model Selection

↓

Response Generation

↓

Return Response

---

## API Endpoints

### Chat

POST /chat

Purpose:

Send messages to F.R.I.D.A.Y.

---

### Memory

GET /memory

POST /memory

DELETE /memory

Purpose:

Manage user memories.

---

### Documents

POST /documents/upload

GET /documents

POST /documents/query

Purpose:

Upload and query files.

---

### Tools

GET /weather

GET /news

POST /calculator

Purpose:

Access tools.

---

### Profile

GET /profile

POST /profile

Purpose:

User profile management.

---

## Authentication

Future:

* Email Login
* Google Login
* GitHub Login

---

## Design Principles

1. Client Independent
2. Model Independent
3. Scalable
4. Open Source
5. API First
