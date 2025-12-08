# Observer Pattern

> "Define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing."

**Type:** Behavioral

## The Problem
You have a `StockMarket` class.
- Millions of users want to know when Apple (AAPL) hits $200.
- **Bad Approach:** Each user repeatedly polls the stock market: `market.get_price("AAPL")` every second.
- **Result:** The server crashes under load (DDOS yourself).

## The Solution
Invert the control. Users **Subscribe** (Observer) to the Market (Subject).
When the price changes, the Market **Notifies** all subscribers.
(Also known as **Pub/Sub**).

## Real World Analogies
1.  **YouTube / Newsletter**: You subscribe once. You get notified whenever a new video/email is out. You don't refresh the channel page every minute.
2.  **MVC Architecture**: The Model updates, and the Views (UI) automatically redraw.

### Key Components
1.  **Subject (Publisher)**: Maintains a list of observers. Has `attach()`, `detach()`, and `notify()` methods.
2.  **Observer (Subscriber)**: Has an `update()` method that gets called by the Subject.

### Code Structure
```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class User(Observer):
    def update(self, message):
        print(f"User received: {message}")
```

## When to use?
- When changes to one object require changing others, and you don't know how many objects need to be changed.
- When an object should be able to notify other objects without making assumptions about who these objects are (Loose Coupling).
