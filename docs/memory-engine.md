# F.R.I.D.A.Y Memory Engine v1

## Goal

Allow F.R.I.D.A.Y to remember important information about users across conversations and devices.

---

## Memory Types

### 1. Profile Memory

Permanent user facts.

Examples:

* Name = Alex Carter
* Nickname = Falcon
* Field = Computer Engineering
* DOB = 15 March 2002

---

### 2. Preference Memory

User likes and dislikes.

Examples:

* Favorite Anime = Fullmetal Alchemist
* Favorite Programming Language = Python
* Preferred Response Style = Concise
* Interested In = Artificial Intelligence

---

### 3. Project Memory

Ongoing work and long-term goals.

Examples:

* Building an AI Assistant
* Developing a Smart Home System
* Participating in a Robotics Competition

---

### 4. Conversation Memory

Recent messages only.

Purpose:

Maintain context during an active conversation.

Retention:

Last 20 messages.

---

## Memory Lifecycle

User Message

↓

Memory Extractor

↓

Store Important Facts

↓

Retrieve Relevant Facts

↓

Inject Into Prompt

↓

Model Response

---

## Retrieval Rules

Always Load:

* Profile Memory

Load When Relevant:

* Preferences
* Projects

Never Load:

* Entire Chat History

---

## Forgetting Rules

Users can:

* Delete Memory
* Update Memory
* View Memory

Commands:

/profile

/remember

/forget

---

## Future Enhancements

* Semantic Memory Search
* Vector Database Integration
* Automatic Importance Ranking
* Cross-Device Synchronization
* Memory Summarization
* Multi-User Shared Memory
