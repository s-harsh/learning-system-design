# Day 14: The Algorithm That Saved The Internet (Consistent Hashing) 🍩

"How does Discord know which server sends you audio?"
"How does Amazon DynamoDB distribute PetaBytes of data?"

The answer is **Consistent Hashing**.
If you only know `Hash(ID) % N`, you will fail the System Design Interview.

### 1. The Rookie Mistake: Modulo Hashing ➗
You have 10 servers. You do `User_ID % 10`.
*   **Disaster**: When Server 10 crashes, your divisor becomes `9`.
*   **Result**: **100% of Keys move**. Your cache is flushed. Your DB melts.
*   **Status**: 503 Service Unavailable.

### 2. The Pro Solution: The Ring Topology �
Imagine a clock face (0-360°).
Servers sit at 12:00, 4:00, and 8:00.
Data sits at 2:00.
**Rule**: Data belongs to the first server it meets moving **Clockwise**. (So 2:00 -> 4:00).
*   **Benefit**: If 4:00 crashes, data just slides to 8:00. The data at 12:00 stays put.
*   **Math**: Only `k/N` keys move. (Zero Downtime Rebalancing).

### 3. The Deep Dive: Virtual Nodes (VNodes) 👻
*   *Problem*: What if "Server A" gets lucky and owns 50% of the ring? (Hotspot).
*   *Solution*: Don't put "Server A" on the ring once. Hash it **100 times** (`A_1`, `A_2`... `A_100`).
*   *Result*: Server A is scattered randomly. Load is perfectly balanced statistically.

### 4. Advanced: Replication & Google's Jump Hash 🧠
*   **Replication**: In Cassandra, data doesn't just stop at one server. It walks the ring and copies itself to the **Next N-1 Neighbors** (N=3).
*   **Jump Consistent Hash**: Google developed a memory-efficient alternative that uses no storage but requires sequential server naming.

*Full visual guide + Python Implementation in the repo 👇*

#SystemDesign #Scalability #ConsistentHashing #Discord #DynamoDB #Engineering #SoftwareArchitecture
