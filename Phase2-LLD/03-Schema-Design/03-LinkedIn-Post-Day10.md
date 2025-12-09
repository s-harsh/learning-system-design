# Day 10: How Netflix & Uber use Proxies 🚀

We all know a Proxy "hides the server". But big tech uses them for much more than that.
Today I learned the **Real-World Proxy Patterns** that power the apps we use daily.

### 1. The CDN Proxy (Netflix Analogy) 🎬
Why does Netflix stream instantly?
Because you aren't streaming from their main server in US. You are streaming from a **Caching Proxy** in your city.
-   **First User** fetches the video from US -> Proxy caches it.
-   **You (Second User)** fetch it from the Proxy.
-   **The Pattern**: A "Virtual Proxy" that handles expensive resources (4K video) smartly.

### 2. The API Gateway (Uber Analogy) 🚗
When you open an app, it needs your Profile, Ride History, and Nearby Cars.
Does it send 3 requests? No.
It sends **One Request** to an **API Gateway Proxy**.
-   The Proxy "fans out" the request to 3 microservices internally.
-   It stitches the answers together.
-   It sends one clean JSON back to your phone.
-   **The Pattern**: An "Aggregator Proxy" to check multiple services behind one interface.

---

### 🧠 Key Takeaway
Proxies aren't just firewall guards. They are:
1.  **Caches** (CDN).
2.  **Aggregators** (Gateways).
3.  **Bouncers** (Security).

*I've visualised these architectures in the repo!* 👇

#SystemDesign #Architecture #Netflix #Uber #ProxyPattern #SoftwareEngineering #Learning
