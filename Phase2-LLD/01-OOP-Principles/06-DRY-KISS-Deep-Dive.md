# DRY (Don't Repeat Yourself) & KISS (Keep It Simple, Stupid)

While SOLID principles tackle architectural structure, **DRY** and **KISS** are the daily hygiene habits of a great software engineer. They seem obvious, but they are the most frequently violated principles in practice.

---

## 1. DRY: Don't Repeat Yourself

> "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system."  
> — *The Pragmatic Programmer*

### The Misconception
Most juniors think DRY means "Don't type the same characters twice."  
**False.**  
DRY is about **knowledge**, not just text. If two pieces of code look different but represent the same *business rule*, and you have to update both when the rule changes, you have violated DRY.

### The "Rule of Three" (When to DRY)
Don't extract a function the first time you copy-paste code. Wait.
1.  **First time:** Write the code.
2.  **Second time:** Copy it (shamefully).
3.  **Third time:** Refactor into a shared abstraction.

*Premature usage of DRY leads to rigid, coupled code ("Spaghetti").*

### Real-World Example: Validation Logic

#### ❌ Bad: WET (Write Everything Twice)
```python
def register_user(username, age):
    if len(username) < 4:
        raise ValueError("Username too short")
    if age < 18:
        raise ValueError("Too young")
    # ... logic ...

def update_profile(username, age):
    if len(username) < 4:  # <-- DUPLICATED KNOWLEDGE
        raise ValueError("Username too short")
    if age < 18:           # <-- DUPLICATED KNOWLEDGE
        raise ValueError("Too young")
    # ... logic ...
```
*Issue: If the username rule changes to 6 characters, you start a bug hunt.*

#### ✅ Good: DRY
```python
def validate_user_rules(username, age):
    if len(username) < 4:
        raise ValueError("Username too short")
    if age < 18:
        raise ValueError("Too young")

def register_user(username, age):
    validate_user_rules(username, age)
    # ...

def update_profile(username, age):
    validate_user_rules(username, age)
    # ...
```

### ⚠️ The Anti-Pattern: Incidental Duplication
Sometimes code *looks* the same but has different reasons to change. **Do not DRY this out.**

Example: A `Product` class and an `Order` class both have `tax_calculation`.
- If `Product` tax depends on *category*.
- If `Order` tax depends on *shipping location*.
- Initially, both might just be `price * 0.2`.
- **Do not merge them.** They will diverge later. Merging them creates unnecessary coupling.

---

## 2. KISS: Keep It Simple, Stupid

> "Complexity is your enemy. Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

### The Philosophy
Systems work best if they are kept simple rather than made complex. Unnecessary complexity makes code hard to test, hard to debug, and hard to maintain.

### Signs you are violating KISS
1.  **Over-Engineering**: Solving problems you *might* have in the future (YAGNI).
2.  **Clever One-Liners**: Writing dense Python list comprehensions that require a PhD to read.
3.  **Abuse of Patterns**: Using a Strategy Pattern when a simplistic `if/else` was enough.

### Example: Finding an Item

#### ❌ Bad: Over-Engineered (Resume Driven Development)
```python
class SearchStrategy(ABC):
    @abstractmethod
    def search(self, data, target): pass

class LinearSearch(SearchStrategy):
    def search(self, data, target):
        return [x for x in data if x == target]

class SearchContext:
    def __init__(self, strategy):
        self.strategy = strategy
    def execute(self, data, target):
        return self.strategy.search(data, target)

# Usage
ctx = SearchContext(LinearSearch())
result = ctx.execute(users, "Alice")
```
*Why? Unless you are literally swapping algorithms at runtime dynamically, this is garbage.*

#### ✅ Good: KISS
```python
def find_user(users, name):
    return next((u for u in users if u.name == name), None)
```
*Simple. Readable. Done.*

---

## Summary Checklist

| Principle | Mantra | When to apply | Warning |
| :--- | :--- | :--- | :--- |
| **DRY** | Single point of truth. | When logic is duplicated > 2 times. | Don't couple unrelated concepts just because they look similar. |
| **KISS** | Simple > Clever. | Always. Prioritize readability. | Simple doesn't mean "easy". It takes effort to simplify. |
