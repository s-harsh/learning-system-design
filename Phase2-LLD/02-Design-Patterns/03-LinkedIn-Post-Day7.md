# Day 7: The Art of NOT Coding (and Design Patterns) 🏗️

Today wasn't just about writing code; it was about knowing *when* to write it.

We wrapped up the foundational principles with **DRY** and **KISS**, and then opened the door to the massive world of **Design Patterns**.

Here’s what we covered in **System Design Day 7**:

### 1️⃣ DRY (Don't Repeat Yourself) & KISS
- **DRY** is about knowledge, not just text. If you have to update the same business rule in two places, you've failed.
- **But wait!** Don't DRY too early. The "Rule of Three" saves you from coupling unrelated code.
- **KISS** (Keep It Simple, Stupid) is the antidote to "Resume Driven Development". If a simple `if` works, don't build a Strategy Factory Proxy.

### 2️⃣ Singleton Pattern 🦄
- The most loved and hated pattern.
- **Use Case**: One Database Connection, One Logger, One Config.
- **The Trap**: In a multi-threaded app, a naive Singleton creates multiple instances. We learned how to lock it down (literally) with thread-safe implementation.

### 3️⃣ Factory Method 🏭
- Stop calling `new Truck()`.
- Use a factory to decouple *creation* from *logic*.
- Deep Dive: How to build a Payment Processor that switches between Stripe, PayPal, and Crypto without touching the main code.

---

### 💡 The "Aha!" Moment
Design patterns are just **blueprints**. You don't memorize them to pass an exam; you learn them to have a shared vocabulary with other engineers.
Instead of explaining your 20 lines of spaghetti code, you just say: *"I used a Factory here."* And everyone nods.

**Tomorrow:** We enter the **Structural Patterns** (Adapter, Decorator, Facade).

👇 *Check the repo for Python implementations of Thread-Safe Singleton & Factory Method.*

#SystemDesign #CleanCode #Python #DesignPatterns #SoftwareEngineering #LearningJourney
