# CDN Architecture: The Edge of the Internet 🌐

A Content Delivery Network (CDN) is just a "Cache that lives closer to the user".
But how does it know where you are?

## 1. The Magic of Anycast DNS 🪄
Servers usually have Unique IPs (Unicast).
In Anycast, **100 servers share the SAME IP Address** (e.g., Cloudflare `1.1.1.1`).

*   **You (India)** -> Ping `1.1.1.1` -> Internet Routers send you to Mumbai Pop.
*   **User (London)** -> Pings `1.1.1.1` -> Internet Routers send them to London Pop.
*   **Mechanism**: BGP (Border Gateway Protocol). The network takes the "Shortest Path" automatically.

## 2. Push vs Pull CDNs

### A. Pull CDN (Standard)
*   **How**: You leave content on your Origin Server.
*   **Request**: User asks CDN for `image.jpg`. CDN doesn't have it. CDN "Pulls" it from Origin, saves it, and serves it.
*   **Pros**: Zero maintenance. Just change DNS CNAME.

### B. Push CDN (Netflix style)
*   **How**: You manually "Upload" (Push) content to specific CDN regions.
*   **Request**: User asks for `movie.mp4`. It MUST be there. If not, 404 Error.
*   **Pros**: Perfect for massive files where "First Miss" latency is unacceptable (Video Streaming).

---

## 3. Edge Computing (Cloudflare Workers / Lambda@Edge) ⚡
Modern CDNs don't just cache static files (Images/CSS). They run CODE.

*   **Use Case**: Image Resizing.
    *   User asks for `profile_pic.jpg?width=200`.
    *   Edge Server checks cache. Miss.
    *   Edge Server fetches full image, **Resizes it to 200px locally**, caches it, and serves it.
    *   **Benefit**: Your main server never sees the CPU load of resizing images.

## Summary Checklist
1.  **Static Assets?** -> Use Pull CDN (Cloudfront/Cloudflare).
2.  **Global Routing?** -> Anycast DNS.
3.  **Heavy Video?** -> Push CDN.
4.  **Custom Logic?** -> Edge Functions.
