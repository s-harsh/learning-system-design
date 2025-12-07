# Builder Pattern

> "Construct a complex object using a step-by-step approach."

**Type:** Creational

## The Problem: Telescoping Constructors
Imagine you are building a `Pizza` class.
- It *must* have size.
- It *can* have cheese, pepperoni, mushrooms, bacon, pineapple (optional).

### ❌ Bad: The Constructor Nightmare
```python
# User has to remember the order of 10 arguments!
pizza = Pizza(12, True, False, True, True, False)
```
What does `True, False, True` mean? It's impossible to read.

### ❌ Bad Alternative: Default Params (Better, but still messy)
```python
pizza = Pizza(size=12, pepperoni=True, bacon=True)
# This works for simple cases, but if the object construction logic is complex 
# (e.g. "If bacon is true, cook time +2 mins"), this logic pollutes the main class.
```

## The Solution: The Builder
We extract the object construction code out of its own class and move it to a separate object called a `Builder`.

### ✅ Good: Fluent Builder
```python
pizza = (PizzaBuilder(size=12)
         .add_cheese()
         .add_pepperoni()
         .add_bacon()
         .bake())
```

## Key Components
1.  **Product**: The complex object (Pizza).
2.  **Builder**: Interface defining creation steps.
3.  **Concrete Builder**: Implements the steps.
4.  **Director (Optional)**: Executes steps in a specific order (e.g., `make_pepperoni_special` runs a specific sequence).

## When to use?
- When you need to create an object with **many optional parameters**.
- When the creation process involves **complex logic** (validation, dependency checks) that shouldn't live in the main class's `__init__`.
- When you want to create immutable objects (the Builder collects separate parts, then `build()` returns the final frozen object).

## Real World Examples
1.  **SQL Query Builders**: 
    ```python
    query = (QueryBuilder()
             .select("*")
             .from_table("users")
             .where("age > 18")
             .limit(10)
             .build())
    ```
2.  **HTTP Request Builders**:
    ```java
    Request request = new Request.Builder()
        .url("https://api.example.com")
        .post(body)
        .build();
    ```
