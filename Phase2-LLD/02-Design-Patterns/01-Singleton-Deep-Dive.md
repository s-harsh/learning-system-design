# Singleton Pattern

> "Ensure a class has only one instance and provide a global point of access to it."

**Type:** Creational

## The Problem
Sometimes, you need exactly *one* of something.
- One Database Connection Pool.
- One Configuration Manager.
- One Logger.

If you create multiple instances, you might get:
- Inconsistent overlapping logs.
- Connections limit errors.
- Different config settings in different parts of the app.

## The Solution
Make the class responsible for keeping track of its sole instance.
1.  **Private Constructor**: Prevent direct instantiation (`new Singleton()`).
2.  **Static Field**: Hold the one instance.
3.  **Static Method**: `getInstance()` to returns the instance.

---

## ⚠️ The Controversy: "Singleton is an Anti-Pattern"
Singleton is the most hated pattern because:
1.  **Global State**: It's essentially a fancy global variable. Global state is hard to debug.
2.  **Tight Coupling**: Code that uses Singleton is hard to unit test because you can't easily mock it.
    - *Fix:* Use Dependency Injection instead of calling `Singleton.getInstance()` directly in your business logic.

---

## Thread Safety (The Interview Trap)
In a multi-threaded web server (like Django/Flask/Node), two requests might try to create the Singleton at the exact same millisecond.
If you aren't careful, you might end up with **two** instances.

### 1. Naive Implementation (Not Safe)
```python
class NaiveSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
             # Point of failure! Two threads can enter here at once.
            cls._instance = super(NaiveSingleton, cls).__new__(cls)
        return cls._instance
```

### 2. Thread-Safe Implementation (Double-Checked Locking)
We use a **Lock** to ensure only one thread enters the creation block.

```python
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double check inside the lock
                if cls._instance is None:
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance
```

---

## Common Python Way: The Module
In Python, **modules are singletons by default**.
If you import `my_module` in 10 different files, Python executes the module body only once.

`config.py`
```python
settings = {"db": "localhost"}
```

`main.py`
```python
import config
print(config.settings["db"])
```
This is often the most "Pythonic" implementation.
