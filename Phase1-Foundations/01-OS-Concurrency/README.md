# Lesson 1: OS Basics - Concurrency vs Parallelism

In system design, understanding how your code executes is crucial. Two key concepts are **Concurrency** and **Parallelism**.

## 1. The Definitions

### 🧵 Concurrency (Dealing with lots of things at once)
Concurrency is about **structure**. It's when an application is making progress on more than one task at the same time (concurrently).
- **Example**: A single-core CPU switching between running Spotify and Chrome. It *looks* like they are running at the same time, but the CPU is just switching very fast (Context Switching).
- **Key Idea**: "I can handle multiple tasks, but I might not be doing them at the exact same instant."

### 🚀 Parallelism (Doing lots of things at once)
Parallelism is about **execution**. It's when an application literally runs multiple tasks at the exact same instant.
- **Example**: A multi-core CPU where Core 1 runs Spotify and Core 2 runs Chrome.
- **Key Idea**: "I am actually doing two things right now."

> **Note**: You can have concurrency without parallelism (single core), but parallelism requires hardware support (multi-core).

---

## 2. Processes vs Threads

### 📦 Process
- An instance of a program in execution (e.g., opening a new Chrome tab might start a new process).
- **Heavyweight**: Has its own memory space.
- **Isolated**: If one process crashes, others are usually fine.
- **Communication**: Harder (Inter-Process Communication - IPC).

### 🧵 Thread
- A unit of execution *within* a process.
- **Lightweight**: Shares memory with other threads in the same process.
- **Fast**: Context switching between threads is faster than processes.
- **Risk**: If one thread crashes or corrupts memory, the whole process might crash.
- **Communication**: Easy (Shared variables), but dangerous (Race Conditions!).

---

## 3. The "Race Condition" Problem
When two threads try to modify the same shared variable at the same time, the result depends on who gets there first. This is a **Race Condition**.

**Example**:
1.  `BankBalance = 100`
2.  Thread A reads 100.
3.  Thread B reads 100.
4.  Thread A adds 10 -> Writes 110.
5.  Thread B adds 20 -> Writes 120.
6.  **Result**: 120 (Thread A's update is lost!).

**Solution**: Use **Locks** (Mutex) to ensure only one thread can access the variable at a time.

---

## 5. Semaphores (The "Nightclub Bouncer")

While a **Mutex** allows only **1** thread to access a resource, a **Semaphore** allows **N** threads.

### The Analogy
- **Mutex**: Key to a single-person restroom. Only 1 person can enter.
- **Semaphore**: Bouncer at a club with capacity 50. 50 people can enter; the 51st has to wait.

### Real-World Use Case: Connection Pooling
Databases (like Postgres) can crash if you open 10,000 connections at once.
- **Solution**: Use a Semaphore initialized to 50.
- The first 50 requests get a connection.
- Request #51 waits until one of the first 50 finishes and releases the connection.

---

## 6. Practical Exercise
We will write a Python script to demonstrate:
1.  **Concurrency**: Running two functions "at the same time".
2.  **Race Condition**: Seeing what happens when we don't use locks.
3.  **Locks**: Fixing the race condition.
