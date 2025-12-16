# Day 15: Why "Fast" Code is Actually Just "Risky" Code ⚡

There is an old saying in Computer Science: "The fastest code is the code that never runs." This is the philosophy behind **Caching**, the practice of storing expensive database results in fast, temporary memory like Redis. However, simply adding a cache introduces one of the hardest problems in distributed systems: **Cache Invalidation**. If you don't update your cache correctly, users see old data, but if you update it too aggressively, you crash your database.

The most critical decision you make is the **Write Strategy**. Most beginners choose **Write-Through Caching**, where the application writes to the Database and the Cache simultaneously. This is the "safe" approach used by banking apps because it guarantees **Strong Consistency**—data is never lost, and the cache is always fresh. However, it adds latency because the user has to wait for two writes to complete before seeing a success message.

For high-scale feedback loops (like **Facebook Likes** or **Google Docs** typing), engineers switch to **Write-Back Caching**. Here, the application writes *only* to the Cache and returns "Success" instantly (sub-millisecond latency). The Cache tracks "dirty pages" and asynchronously syncs them to the Database every few seconds. This provides massive throughput but comes with a terrifying risk: if the Cache server crashes before the sync, that data is lost forever. This is why social media counts are often "eventually consistent"—speed is prioritized over perfect accuracy.

Another silent killer is the **Thundering Herd** problem (or Cache Stampede). Imagine a celebrity tweets, and their profile is cached for 60 seconds. At T=60s, the cache expires. Instantly, 10,000 users request the profile, miss the cache, and all 10,000 requests hit the database simultaneously. This crushes the DB CPU. **Reddit** solves this using **Probabilistic Early Expiration** (or X-Fetch). Instead of waiting for the strict 60s limit, they allow a small percentage of requests to recompute the cache *before* it expires (e.g., at 58s), ensuring the cache is refreshed without a massive spike in traffic.

But Caching isn't just about managing valid data; it's about defending against **Invalid Data**. A common attack vector is **Cache Penetration**, where a malicious user requests thousands of non-existent keys (e.g., `User_ID=-1`). Since these keys aren't in the cache, they punch straight through to the database, causing a DOS attack. Smart Engineers defend against this using **Bloom Filters**—a probabilistic data structure that tells you if a key *definitely doesn't exist* before you even touch the database.

Finally, we must ask: "Who dies?" When the cache is full, **Eviction Policies** decide what to delete. While **LRU (Least Recently Used)** is the standard, it has a fatal flaw: "Scan Resistance". If a user runs a one-time script reading the entire database, LRU blindly caches everything, flushing out your actual hot data. Modern systems use **ARC (Adaptive Replacement Cache)** or **TinyLFU** to intelligently distinguish between "One-time wonders" and "True frequent users."

*Full diagrams and deep dive in the repo 👇*

#SystemDesign #Caching #Redis #Scaling #Facebook #Engineering #SoftwareArchitecture
