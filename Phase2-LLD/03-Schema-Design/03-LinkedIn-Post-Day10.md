# Day 10: The Gatekeepers & The Foundation 🏛️

"Code is ephemeral. It changes every sprint. Data is forever."

Today, Day 10 of my System Design journey, I mastered the **Front** and the **Back** of scalable systems.

### 1. The Front: Advanced Proxies (Netflix & Uber) 🛡️
I moved beyond basic "Load Balancers" to understand the patterns that power Big Tech:
- **The CDN Proxy (Netflix)**: Streaming doesn't happen from the US. It happens from a "Caching Proxy" in your city.
- **The API Gateway (Uber)**: Your phone doesn't call 5 services. It calls one "Aggregator Proxy" that stitches User+Location+Ride data into one response.

### 2. The Back: Schema Design (The Lost Art) �️
If you screw up the database schema, no amount of clean code will save you.
I dove deep into **Normalization**:
- **1NF**: Atomic values (No lists in cells!).
- **2NF**: No Partial Dependencies (Respect the Primary Key).
- **3NF**: No Transitive Dependencies (Don't store 'Instructor Phone' in the 'Student' table).

We applied this to build a full **Library Management System** schema from scratch. 📚

---

### 🧠 The takeaway
To be a System Architect, you need to understand:
1.  **Infrastructure** (Proxies/CDNs) to handle the Traffic.
2.  **Data Modeling** (Normalization) to handle the Truth.

*I've pushed the Advanced Proxy notes and the full Library Schema to the repo!* 👇

#SystemDesign #DatabaseDesign #SQL #Nginx #CDN #Normalization #SoftwareArchitecture #Learning
