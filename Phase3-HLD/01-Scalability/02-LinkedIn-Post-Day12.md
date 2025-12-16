# Day 12: Why "Super Computers" Don't Scale (Physics vs Code) ⚛️

"Why can't I just buy a bigger server?"
I asked this today as I started **High-Level Design (HLD)**.
The answer wasn't code. It was Physics.

### 1. The Vertical Scaling Trap (The Brick Wall) 🧱
You can upgrade RAM from 8GB -> 128GB.
But you can't go to 100,000 GB.
Why?
*   **Socket Limits**: A motherboard only fits 2-4 CPUs.
*   **Bus Saturation**: Even if you have 128 cores, they fight over the memory bus.
*   **NUMA Bottlenecks**: Accessing RAM across sockets adds latency.
**Verdict**: Vertical Scaling is expensive and finite.

### 2. The Horizontal Scaling Truth (Shared-Nothing) ➡️
The only way to hit 1 Million Concurrent Users is **Horizontal Scaling**.
Buy 1,000 cheap servers. Connect them.

But here is the catch: **Statelessness**.
If Server 1 saves your Session ID in RAM, and the Load Balancer routes your next request to Server 2... you are logged out.
**The Fix**: Move state out to redis. Treat servers like disposable calculators.

### 3. The Gatekeepers (L4 vs L7 Load Balancers) ⚖️
I learned that not all Load Balancers are the same.
*   **Layer 4 (Transport)**: Dumb & Fast. It looks at IP+Port and throws the packet.
*   **Layer 7 (Application)**: Smart & Slow. It reads your Cookies/Headers and decides: "Oh, this is an image? Send to S3."

System Design is about understanding these trade-offs.
Do you want the raw speed of L4 or the intelligence of L7?

*I wrote a deep-dive "Masterclass" on this in the repo 👇*

#SystemDesign #Scalability #Architecture #LoadBalancer #DistributedSystems #Engineering #Learning #SoftwareArchitecture
