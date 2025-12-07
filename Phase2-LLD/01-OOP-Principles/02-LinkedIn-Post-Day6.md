# Day 6: SOLID Principles (LinkedIn Post Draft)

**Headline Idea:** The difference between a Junior dev and a Senior Architect? It's not code speed. It's code *stability*.

---

**[Post Content]**

Day 6 of my System Design Learning Journey: **The Art of Low-Level Design (SOLID)** 🏗️

We often obsess over "System Design" (Kafka, Redis, Kubernetes). But if the code *inside* your microservice is a tangled mess, no amount of Kubernetes will save you.

Today I did a deep dive into the **SOLID Principles**.
(And no, it's not just interview theory. It's about money. 💸)

Here is what I learned about writing code that doesn't break:

1️⃣ **SRP (Single Responsibility Principle)**: Stop writing "God Classes". If your `OrderManager` handles Payments AND Emails, you are one typo away from breaking the checkout flow just to change an email subject line.
👉 *Rule: "A class should have only one reason to change (one 'Actor')."*

2️⃣ **OCP (Open/Closed Principle)**: The secret to "Plug-and-Play". You should be able to add "Bitcoin Support" without touching the existing "Credit Card" code.
👉 *Rule: "Open for Extension, Closed for Modification."*

3️⃣ **LSP (Liskov Substitution Principle)**: Don't lie to your compiler. If you create a `ReadOnlyFile` class that inherits from `File` but crashes when `.write()` is called, you’ve built a trap for your future self.
👉 *Rule: "Subtypes must be substitutable for their base types."*

4️⃣ **ISP (Interface Segregation Principle)**: Don't be greedy. Don't force a "Smart Lightbulb" implementation to define a `brew_coffee()` method just because it shares an interface with a "Smart Kitchen".
👉 *Rule: "Many small interfaces > One giant interface."*

5️⃣ **DIP (Dependency Inversion Principle)**: My favorite. Stop hard-coding specific databases. Depend on the "Socket" (Interface), not the "Power Plant" (Postgres/Mongo).
👉 *Rule: "Inject dependencies. Don't create them."*

🛑 **The Hard Truth:**
SOLID code takes *longer* to write on Day 1.
But it takes **10x less time** to debug on Day 100.

It’s an investment. And like all investments, compound interest is magic. 📈

What’s the hardest SOLID principle for you to strictly follow? For me, it's definitely ISP (I love giant interfaces 😅).

#SystemDesign #SOLID #SoftwareArchitecture #CleanCode #LearningJourney #100DaysOfCode #Developer
