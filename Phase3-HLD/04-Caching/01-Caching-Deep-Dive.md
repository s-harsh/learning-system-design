# Caching Deep Dive: The Art of Doing Nothing ⚡

> "The fastest code is the code that never runs."

Caching is the layer between your fast Application and your slow Database.
But adding a cache introduces the hardest problem in distributed systems: **Consistency**.

## 1. Caching Strategies (The Write Patterns) 📝

### A. Write-Around (The Lazy)
*   **Flow**: App writes to DB. App reads from DB -> Updates Cache.
*   **Pros**: Cache only holds data that is *actually read*. Good for "Cold" data.
*   **Cons**: First read is always a "Cache Miss" (Slow).

### B. Write-Through (The Safe)
*   **Flow**: App writes to Cache AND DB at the same time (Synchronously).
*   **Pros**: **Strong Consistency**. Data in Cache is always equal to DB.
*   **Cons**: High Write Latency (Must wait for both).

### C. Write-Back (The Fast & Dangerous) 🏎️
*   **Flow**: App writes *only* to Cache. Return "Success".
*   **Async**: The Cache counts the writes (Dirty pages) and syncs to DB later (e.g., every 5s).
*   **Pros**: Massive Write Throughput. (Think: Facebook Likes, Google Docs typing).
*   **Cons**: **Data Loss**. If Cache crashes before syncing, the data is gone forever.

---

## 2. Eviction Policies (Who dies?) 💀
When the cache is full, who gets kicked out?

### A. LRU (Least Recently Used) - The Gold Standard
*   **Logic**: Throw away the guy who hasn't been touched in the longest time.
*   **Implementation**: Doubly Linked List + HashMap. O(1).
*   **Use Case**: Social Media feeds, standard web apps.

### B. LFU (Least Frequently Used) - The Analytics Choice
*   **Logic**: Throw away the guy with the lowest *count* of hits.
*   **Problem**: A video viral yesterday (High Count) stays in cache today even if nobody watches it. (Cache Pollution).

### C. ARC (Adaptive Replacement Cache) - The Genius
*   **Logic**: It dynamically balances between LRU (Recency) and LFU (Frequency) based on workload.
*   **Status**: Used by IBM and ZFS. (Previously patented).

---

## 3. The Nightmare: Cache Stampede (Thundering Herd) 🐘
Scenario: You cache a heavy SQL query result (`Key=Dashboard_Stats`). TTL = 60s.
*   **T=59s**: Cache is hot. 1000 requests/sec served instantly.
*   **T=60s**: **Cache Expires**.
*   **T=60.1s**: 1000 requests hit the Cache. MISS.
*   **Result**: 1000 requests hit the Database at the EXACT same time.
*   **Consequence**: **DB CPU spikes to 100%. System crashes.**

### The Fix: Probabilistic Early Expiration 🎲
Don't wait for 60s.
When a request comes at T=55s, roll a dice.
*   If (Random < Gap * Beta): Recompute the value *early* and update cache.
*   **Result**: One unlucky user recomputes it at 58s. When 60s comes, the cache is already fresh. No stampede.
