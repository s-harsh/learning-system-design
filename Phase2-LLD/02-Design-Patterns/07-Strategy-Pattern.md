# Strategy Pattern

> "Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it."

**Type:** Behavioral

## The Problem
You have a class that needs to do a task, but the *way* it does that task might change.
e.g., A navigation app.
- Calculate Route for Walking.
- Calculate Route for Driving.
- Calculate Route for Transit.

### ❌ Bad: Massive If/Else
```python
class Navigator:
    def build_route(self, mode):
        if mode == "WALK":
            # 50 lines of walking logic
        elif mode == "CAR":
            # 50 lines of driving logic
        elif mode == "BUS":
            # ...
```
This violates the **Open/Closed Principle**. Adding "Bicycling" means modifying the `Navigator` class.

## The Solution
Create a common interface (Strategy) and specific classes for each algorithm.
The Context (Navigator) holds a reference to a Strategy object.

## Real World Analogies
1.  **Travel to Airport**: You just want to "Go to Airport".
    - Strategy A: Take Uber.
    - Strategy B: Take Bus.
    - Strategy C: Drive self.
2.  **Payment Methods**: Checkout page.
    - Strategy A: Credit Card.
    - Strategy B: PayPal.

### Key Components
1.  **Context**: The class using the strategy (e.g., `Navigator`, `ShoppingCart`).
2.  **Strategy Interface**: Defines the method (e.g., `build_route()`, `pay()`).
3.  **Concrete Strategies**: The actual implementations.

### Code Structure
```python
# Interface
class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, A, B): pass

# Concrete Strategies
class WalkingStrategy(RouteStrategy):
    def build_route(self, A, B): return "Walk 500m"

class DrivingStrategy(RouteStrategy):
    def build_route(self, A, B): return "Drive 2km"

# Context
class Navigator:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
        
    def go(self, A, B):
        return self.strategy.build_route(A, B)
```
