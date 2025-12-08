# Day 9: Objects that Talk to Each other 🗣️

Day 8 was about Structure. **Day 9 is about Behavior.**
In System Design, it's not enough to just organize classes; they need to communicate, adapt, and react. Today I dove into **Behavioral Design Patterns**.

Here are the Top 5 I implemented:

### 1. Strategy Pattern ♟️
- **The specific implementation**: "Swap algorithms at runtime."
- **Example**: Switching from Credit Card to PayPal without changing the Checkout class.

### 2. Observer Pattern 📡
- **The specific implementation**: "Don't call us, we'll notify you."
- **Example**: YouTube subscribers getting notified when a video is uploaded. (Pub/Sub).

### 3. Command Pattern 🎮
- **The specific implementation**: "Turn a request into an object."
- **Example**: Implementing "Undo" in a text editor. Every keystroke is a stored object that can be reversed.

### 4. State Pattern 🚦
- **The specific implementation**: "Change behavior based on internal state."
- **Example**: A Document workflow (`Draft` -> `Review` -> `Published`). The `publish()` button does different things in each state.

### 5. Template Method Pattern 📄
- **The specific implementation**: "Define the skeleton, let subclasses fill the details."
- **Example**: A Data Miner that always Opens and Closes files the same way, but parses CSVs differently from PDFs.

---

### 🧠 Key Takeaway
Behavioral patterns are the key to **Loose Coupling**. They allow objects to interact without knowing too much about each other. This makes systems flexible, testable, and maintainable.

*Code, Deep Dives, and Demos are in the repo!*

#SystemDesign #DesignPatterns #Python #BehavioralPatterns #Coding #SoftwareEngineering #Learning
