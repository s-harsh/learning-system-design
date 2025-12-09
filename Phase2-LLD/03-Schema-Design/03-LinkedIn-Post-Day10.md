# Day 10: The Gatekeepers & The Foundation 🏛️

"Code is ephemeral. It changes every sprint. Data is forever."

Today, Day 10 of my System Design journey, I stopped writing code and started designing the **Backbone** of software.

Here is the breakdown:

### 1. The Proxy Pattern 🛡️
I learned that you never let a user talk directly to your Production DB. You put a **Gatekeeper** in the middle.
- **The Concept**: "The Club Bouncer".
- **The Job**: Security (Auth check), Caching (Returning data fast), and Lazy Loading (Don't load the 1GB file until needed).
- **Real World**: Nginx, Cloudflare, CDN. They are all Proxies protecting your app.

### 2. Schema Design: The Lost Art 🗄️
If you screw up the database schema, no amount of clean code will save you.
I dove deep into **Normalization**:
- **1NF**: Atomic values (No lists in cells!).
- **2NF**: No Partial Dependencies (Respect the Primary Key).
- **3NF**: No Transitive Dependencies (Don't store 'Instructor Phone' in the 'Student' table).

We applied this to build a full **Library Management System** schema from scratch. 📚

---

### 🧠 The Senior Dev Insight
A Junior Dev rushes to write `class User`.
A Senior Dev grabs a whiteboard and draws an **Entity-Relationship (ER) Diagram**.
Because refactoring code is cheap. Migrating 10 Million rows of bad data is expensive.

*I've pushed the Proxy implementation and the full Library Schema to the repo!* 👇

#SystemDesign #DatabaseDesign #SQL #ProxyPattern #SoftwareArchitecture #Learning #100DaysOfCode
