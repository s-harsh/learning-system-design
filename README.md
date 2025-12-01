# System Design Learning Roadmap: Zero to Architect

This roadmap is designed to take you from a basic understanding of coding to mastering High-Level Design (HLD) and Low-Level Design (LLD), enabling you to build scalable solutions like Netflix or Instagram.

## 🗺️ Roadmap Overview

- **Phase 1: Foundations (0-2 Months)** - Networking, Database Internals, OS basics.
- **Phase 2: Low-Level Design (LLD) (2-3 Months)** - OOP, Design Patterns, Schema Design.
- **Phase 3: High-Level Design (HLD) (3-5 Months)** - Scalability, Distributed Systems, Components.
- **Phase 4: Real-World Architectures (Ongoing)** - Case Studies (Netflix, Uber, etc.).

---

## 🏗️ Phase 1: The Foundations
*Before designing systems, you must understand the building blocks.*

### 1. Computer Science Basics
- **Operating Systems**: Concurrency, Multithreading, Process vs Thread, Locks, Semaphores.
- **Networking**: HTTP/HTTPS, TCP/UDP, DNS, OSI Model, WebSockets, REST vs GraphQL vs gRPC.

### 2. Database Internals
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability.
- **Indexing**: B-Trees, LSM Trees (How databases read/write fast).
- **Transactions & Locking**: Optimistic vs Pessimistic locking.
- **SQL vs NoSQL**: When to use Postgres vs MongoDB vs Cassandra.

---

## 🧩 Phase 2: Low-Level Design (LLD)
*Focus on code maintainability, extensibility, and object-oriented design.*

### 1. Object-Oriented Programming (OOP)
- **Solid Principles**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.
- **DRY (Don't Repeat Yourself)** & **KISS (Keep It Simple, Stupid)**.

### 2. Design Patterns
*Don't memorize all, master the most used:*
- **Creational**: Singleton, Factory, Builder.
- **Structural**: Adapter, Decorator, Facade, Proxy.
- **Behavioral**: Observer, Strategy, Command.

### 3. Schema Design
- **ER Diagrams**: Entity-Relationship modeling.
- **Normalization**: 1NF, 2NF, 3NF (and when to denormalize for performance).

### 4. LLD Practice Problems
- Design a Parking Lot.
- Design a Movie Ticket Booking System.
- Design an Elevator System.
- Design a Splitwise-like app.

---

## 🚀 Phase 3: High-Level Design (HLD)
*Focus on scalability, availability, and reliability.*

### 1. Core Concepts
- **Scalability**: Vertical vs Horizontal Scaling.
- **Availability**: 99.9% vs 99.999% (The "Nines").
- **CAP Theorem**: Consistency, Availability, Partition Tolerance.
- **Consistent Hashing**: For distributed caching/storage.

### 2. System Components
- **Load Balancers**: Nginx, HAProxy (L4 vs L7 balancing).
- **Caching**: Redis, Memcached (Caching strategies: Write-through, Write-back, Look-aside).
- **Message Queues**: Kafka, RabbitMQ (Pub-Sub models).
- **Databases**: Sharding, Replication (Master-Slave, Master-Master).
- **CDN**: Content Delivery Networks (Cloudflare, AWS CloudFront).

### 3. API Design
- **RESTful Best Practices**: Resource naming, status codes.
- **Idempotency**: Ensuring safe retries.
- **Rate Limiting**: Algorithms (Token Bucket, Leaky Bucket).

---

## 🏢 Phase 4: Real-World Architectures
*Deconstruct famous systems to understand how they handle scale.*

### 1. Netflix (Video Streaming)
- **Key Challenges**: Storing massive video files, adaptive bitrate streaming, global content delivery.
- **Tech**: CDN (Open Connect), Microservices, Cassandra.

### 2. Instagram (Photo/Video Feed)
- **Key Challenges**: Infinite scroll feed generation, image storage, celebrity (hot) users.
- **Tech**: Sharding by UserID, Pre-generating feeds (Fan-out on write).

### 3. Uber (Ride Hailing)
- **Key Challenges**: Real-time location tracking, matching algorithms, surge pricing.
- **Tech**: QuadTrees/Geohashing for location, WebSocket for real-time updates.

### 4. WhatsApp (Chat)
- **Key Challenges**: Real-time delivery, message ordering, offline support.
- **Tech**: Erlang, XMPP protocol (customized).

---

## 📚 Resources

### 📺 YouTube Channels (Best for Visual Learners)
1.  **[ByteByteGo (Alex Xu)](https://www.youtube.com/@ByteByteGo)** - Excellent animations, clear explanations.
2.  **[Gaurav Sen](https://www.youtube.com/@GKcs)** - Deep dives into system components and interview questions.
3.  **[Hussein Nasser](https://www.youtube.com/@hnasr)** - Great for backend engineering concepts (databases, networking).
4.  **[Exponent](https://www.youtube.com/@tryexponent)** - Mock interviews to see how it's done in practice.
5.  **[System Design Fight Club](https://www.youtube.com/@SDFC)** - Advanced discussions.

### 📖 Books (Best for Deep Dives)
1.  **"Designing Data-Intensive Applications" (DDIA)** by Martin Kleppmann - *The Bible of System Design.* (Must Read).
2.  **"System Design Interview – An Insider's Guide" (Vol 1 & 2)** by Alex Xu - *Best for interview prep.*
3.  **"Building Microservices"** by Sam Newman.

### 💻 GitHub Repositories
1.  **[System Design Primer](https://github.com/donnemartin/system-design-primer)** - Comprehensive guide with diagrams.
2.  **[Awesome System Design](https://github.com/madd86/awesome-system-design)** - Curated list of resources.

---

## 🛠️ How to Implement & Document (Real-Life Application)

### 1. Build "Toy" Versions of Real Systems
Don't just read. Build.
- **Project 1: URL Shortener (TinyURL)**
    - *Focus*: Database sharding, unique ID generation (Snowflake), redirection.
- **Project 2: Real-time Chat App**
    - *Focus*: WebSockets, message persistence, online status.
- **Project 3: E-commerce Inventory System**
    - *Focus*: Concurrency (handling race conditions), database locking.

### 2. Document Your Learning (The "Feynman Technique")
Writing helps you cement your knowledge and showcases your skills to employers.

**Where to write:**
- **Personal Blog**: Hashnode, Medium, or a custom Next.js blog.
- **GitHub**: Create a repo called `learning-system-design` and push your notes/diagrams.

**How to structure a "System Design Case Study" blog post:**
1.  **The Problem**: "Designing a system to handle 1M requests/sec for..."
2.  **Requirements**: Functional (what it does) & Non-Functional (latency, availability).
3.  **High-Level Diagram**: Use **[Excalidraw](https://excalidraw.com/)** or **[Draw.io](https://app.diagrams.net/)** to draw the architecture.
4.  **Deep Dive**: Explain *why* you chose Redis over Memcached, or why you used NoSQL.
5.  **Trade-offs**: "I chose consistency over availability because..." (Shows maturity).

### 3. Contribute to Open Source
Find projects that use distributed systems (e.g., databases, queues) and try to understand one small part of their codebase.
