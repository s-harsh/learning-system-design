# Proxy Pattern 🛡️

*Listen up, because this is how we protect our infrastructure from melting down.*

In production, you never let clients talk directly to your expensive resources. You don't let a random intern's script query the Production Database master node directly. You put something in the middle.

That "Middleman" is the **Proxy**.

## The Core Concept
The Proxy is a class that **pretends** to be the real object. It has the same interface. The client thinks it's talking to the Real Object, but it's talking to the Proxy.

The Proxy intercepts the call, does some "bouncers work" (Security, Caching, Logging), and *then* (maybe) passes it to the Real Object.

## Types of Proxies (Use Cases)

### 1. Protection Proxy (The Bouncer) 🔐
**Scenario**: You have a `SensitiveFile`. You don't want just anyone reading it.
**Usage**: The Proxy checks `if user.is_admin()` before calling `real_file.read()`. If they aren't admin, it throws a 403 Forbidden. The real file never even knows usage was attempted.

### 2. Remote Proxy (The Diplomat) 📡
**Scenario**: The object lives on a different server (e.g., gRPC calls).
**Usage**: The local object you call looks like a normal method `service.get_user()`, but behind the scenes, the Proxy serializes your request, sends it over the network, waits, deserializes the response, and gives it to you. You don't know it went over the wire.

### 3. Virtual Proxy (Lazy Loading) 😴
**Scenario**: You have a `HighResImage` (500MB).
**Usage**: You don't want to load it into memory until the user actually scrolls to it. The Proxy is a lightweight placeholder. When `.draw()` is finally called, *then* the Proxy loads the heavy image.

## Industry Reality Check
**Nginx** is a Reverse **Proxy**.
When you hit `google.com`, you aren't hitting the server with the Python/Go code. You hit their Proxy (Load Balancer).
- It terminates SSL.
- It caches static assets (images).
- It blocks DDOS attacks.
Only "clean" traffic gets to the application.

### Code Structure
```python
class RealServer:
    def handle_request(self):
        print("Processing request (Expensive)...")

class ProxyServer:
    def __init__(self, real_server):
        self.real_server = real_server
        self.cache = {}

    def handle_request(self):
        if self.check_access():
            self.real_server.handle_request()
            self.log_access()
        else:
            print("Access Denied.")
```
