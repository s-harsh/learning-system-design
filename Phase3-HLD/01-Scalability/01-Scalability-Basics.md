# High-Level Design (HLD): Scalability Masterclass 🚀

> "Scalability is the property of a system to handle a growing amount of work by adding resources to the system."

This guide delves effectively into the **physics** of computing systems. We move beyond High-Level abstractions to understand *why* systems fail and *how* to scale them.

---

## 1. Vertical Scaling (Scaling Up) 🔼
*Also known as: Scale Up*

This is the process of adding more power (CPU, RAM, DISK) to an existing machine.

### The Hardware Architecture
To understand why Vertical Scaling fails, you must understand the server motherboard.
1.  **CPU Socket Limits**: A motherboard has physical slots for CPUs. You cannot just "add more". Standard servers have 2 sockets. High-end have 4 or 8.
2.  **Bus Speed Saturation**: Even if you have 128 Cores, they all talk to RAM over the **Front Side Bus** (or QPI/Infinity Fabric). This bus has a bandwidth limit. If 128 cores try to read RAM at once, the *bus* becomes the bottleneck, not the CPU.
3.  **NUMA (Non-Uniform Memory Access)**: In massive servers, RAM is split between CPUs. CPU 1 accessing CPU 2's RAM is slow. This latency kills performance in "Mega-Servers".

### The Cost Curve (Moore's Law Inverse)
*   A 64GB RAM stick costs $X$.
*   A 128GB RAM stick costs $3X$.
*   A 256GB RAM stick costs $10X$.
Buying the "biggest beast" is **economically inefficient**.

### The Verdict
*   **Use Case**: Database Masters (e.g., a massive PostgreSQL primary node), caching layers that need low latency.
*   **Ceiling**: Hard physical limit. You eventually hit a wall.

---

## 2. Horizontal Scaling (Scaling Out) ➡️
*Also known as: Scale Out*

This involves adding more *nodes* (computers) to a system, such that they act as a single logical unit.

### Core Philosophy: Shared-Nothing Architecture
In a perfect horizontally scaled system, **Node A knows nothing about Node B**.
If Node A crashes, Node B doesn't care. It just takes the extra load.

### The "Stateless" Requirement 🧠
This is the hardest part for developers moving from Monoliths to Distributed Systems.
*   **Stateful (Bad for Scaling)**: Saving `user_id` or `shopping_cart` in the web server's RAM.
    *   *Why?* If User requests Server A (cart created), then next request hits Server B (cart is empty).
*   **Stateless (Good)**: The Server processes logic but stores *nothing*.
    *   *Where does state go?*
        1.  **Client-Side**: JWT (JSON Web Tokens). The User holds their own session data in the browser cookie.
        2.  **External Store**: Redis/Memcached. All servers talk to a shared Redis cluster to fetch sessions.

---

## 3. The Load Balancer (LB) ⚖️
The Gateway to your system.

### Layer 4 vs Layer 7 Load Balancing (The Deep Dive)

#### Layer 4 (Transport Layer - TCP/UDP)
*   **What it sees**: IP Addresses and Ports. `Src: 1.2.3.4:5000 -> Dst: 9.9.9.9:80`.
*   **How it works**: It modifies the Destination IP (NAT) and forwards the packet.
*   **Packet Inspection**: It does NOT look inside the packet. It doesn't know if it's HTTP, FTP, or Garbage.
*   **Performance**: Extremely fast (millions of requests/sec). Logic is often handled by hardware (ASICs).
*   **Example**: LVS (Linux Virtual Server), AWS Network Load Balancer.

#### Layer 7 (Application Layer - HTTP/HTTPS)
*   **What it sees**: Everything. Headers, Cookies, URL Path, Body.
*   **How it works**: It **terminates** the TCP connection. It reads the request. It opens a *new* connection to the backend server.
    *   *Cost*: This "Double Connection" (Client->LB, LB->Server) is CPU intensive.
*   **Features**:
    *   **SSL Termination**: The LB decrypts the HTTPS, sending plain HTTP to servers (offloading CPU work).
    *   **Path Routing**: `/api` -> Backend Service. `/images` -> S3 Bucket.
    *   **Rate Limiting**: "Block IP if > 100 req/sec".
*   **Example**: Nginx, HAProxy, AWS Application Load Balancer.

---

## 4. Advanced Load Balancing Algorithms

### A. Round Robin (The Default)
Cycle through servers: A, B, C, A, B, C...
*   *Issue*: If User A requests a heavy Report (10s) and User B requests a Favicon (10ms), Server A gets stuck.

### B. Least Connections (Adaptive)
The LB tracks active connections.
*   Server A: 50 active.
*   Server B: 2 active.
*   *Decision*: Send next request to Server B.
*   *Benefit*: Naturally handles "Heavy Requests".

### C. Consistent Hashing (The Pro Move)
Used in Databases and Caches (like Discord/Uber).
Imagine a hash ring (0-360 degrees). Servers are points on the ring.
*   `Hash(User_IP) -> Angle`.
*   Walk clockwise to find the first server.
*   *Why?* If you add a server, keys get re-distributed minimally. Standard "Modulo Hashing" would reshuffle everything!

---

## 5. Scaling the Database (The Real Bottleneck) 💾
Your app scales infinitely. Your Database does not.

### A. Replication (Read Scaling)
*   **Master Node**: Handles WRITES (INSERT, UPDATE).
*   **Slave Nodes**: Copy data from Master. Handle READS.
*   *Trade-off*: **Consistency**. If I write to Master, it takes 100ms to copy to Slave. If I read from Slave immediately, I might see old data (Eventual Consistency).

### B. Sharding (Write Scaling)
Split the data across multiple servers.
*   **Horizontal Partitioning**:
    *   Users A-M -> DB Server 1.
    *   Users N-Z -> DB Server 2.
*   *Complexity*: JOINs are impossible across servers. You must handle logic in code.

---

## Summary Checklist for Day 12
1.  **Vertical Scaling**: Fast, simple, limited by Physics/Cost.
2.  **Horizontal Scaling**: Infinite, complex, requires Statelessness.
3.  **L4 LB**: Fast, blind packet forwarding.
4.  **L7 LB**: Smart, CPU heavy, understands HTTP/SSL.
5.  **DB Scaling**: Read Replicas for Reads, Sharding for Writes.
