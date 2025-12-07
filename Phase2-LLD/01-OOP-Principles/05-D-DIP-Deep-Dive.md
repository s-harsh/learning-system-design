# 🔌 Dependency Inversion Principle (DIP): The "Plug" Mentality

> **"High-level modules should not depend on low-level modules. Both should depend on abstractions."**  
> **"Abstractions should not depend on details. Details should depend on abstractions."**

This is the hardest principle to understand initially, but it is the **most important** for building large systems.

It is basically **Dependency Injection (DI)**.

---

## 🏗️ The Real-World Scenario: The Analytics Service

You are building a system to track user "Page Views".
You decide to store logs in **SQL** (Postgres).

### The Tight Coupling (Violation) ❌

```python
# Low-Level Module (The Detail)
class PostgresDatabase:
    def insert(self, data):
        print(f"INSERT INTO logs VALUES ({data})")

# High-Level Module (The Business Logic)
class AnalyticsService:
    def __init__(self):
        # ERROR: Direct dependency on the low-level class!
        self.db = PostgresDatabase() 
        
    def track_view(self, url):
        # Logic...
        self.db.insert(f"Viewed {url}")
```

### The Problem
1.  **Vendor Lock-In**: What if your boss says "SQL is too slow for logs. Use **MongoDB**"?
    *   You have to **open `AnalyticsService`** and find/replace `PostgresDatabase` with `MongoDatabase`.
    *   You violated OCP (Open/Closed) because you modified the high-level code.
2.  **Testing**: What if I want to unit test `AnalyticsService` on my laptop without installing Postgres?
    *   I can't. The class creates a real DB connection in its constructor.

---

## 🛠️ The Refactor: Dependency Injection

We flip the dependency.
*   **Before**: Analytics -> Postgres
*   **After**: Analytics -> **Interface** <- Postgres

### Step 1: Create the Interface (The "Socket")

```python
class IDatabase(ABC):
    @abstractmethod
    def insert(self, data): pass
```

### Step 2: Implement the Details (The "Plugs")

```python
class PostgresDatabase(IDatabase):
    def insert(self, data):
        print(f"Postgres: {data}")

class MongoDatabase(IDatabase):
    def insert(self, data):
        print(f"MongoDB: {data}")

class FakeDatabase(IDatabase): # For Testing!
    def insert(self, data):
        print(f"FakeDB (Memory): {data}")
```

### Step 3: Inject the Dependency

The `AnalyticsService` no longer creates the database. It **asks** for it.

```python
class AnalyticsService:
    # "I don't care what DB it is. Just give me something that fits the IDatabase socket."
    def __init__(self, db: IDatabase): 
        self.db = db
        
    def track_view(self, url):
        self.db.insert(f"Viewed {url}")
```

---

## 🔌 Using the System (Wiring it up)

This "wiring" usually happens in your `main.py` or a DI Framework (like Spring Boot or Dagger).

```python
# 1. Setup for Production
real_db = MongoDatabase() # or Postgres
prod_service = AnalyticsService(real_db) # Plug it in
prod_service.track_view("/home")

# 2. Setup for Unit Testing
test_db = FakeDatabase()
test_service = AnalyticsService(test_db) # Plug in the fake
test_service.track_view("/home")
```

### Why "Inversion"?
In the bad code, the flow of control was:
`Service` -> `creates` -> `Database`.
(The Service controlled the Database).

In the good code, the flow is:
`Main` -> `creates` -> `Database`
`Main` -> `injects` -> `Service`.
(The control is inverted. The Service is passive; it receives its dependencies).

### 🏭 Industry Example: Power Plugs
*   **High-Level**: Your Laptop.
*   **Low-Level**: The Electricity Grid.
*   **Interface**: The Wall Socket (3-pin plug).

Your laptop does not depend on "Nuclear Power" or "Wind Power". It depends on the "Socket".
The power company can switch from Coal to Solar (change the low-level detail), and as long as they power the socket (the interface), your laptop (high-level) never needs to change.
