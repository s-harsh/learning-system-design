# Factory Method Pattern

> "Define an interface for creating an object, but let subclasses decide which class to instantiate."

**Type:** Creational

## The Problem
Imagine you are building a **Logistics App**.
- Initially, you only handle **Trucks**.
- Your code is full of `new Truck()`.
- Suddenly, your business grows, and you need to handle **Ships**.
- **Issue:** You have to find every `new Truck()` and replace it with complex if/else logic. You have violated the **Open/Closed Principle**.

## The Solution
Don't call `new` directly. Use a special method (the "Factory Method") to create objects. Subclasses override this method to create different objects.

## Key Components
1.  **Product Interface**: Common interface for all objects (e.g., `Transport`).
2.  **Concrete Products**: Specific implementations (e.g., `Truck`, `Ship`).
3.  **Creator**: Class that declares the factory method.
4.  **Concrete Creators**: Subclasses that override the factory method to return a specific product.

---

## Example: Notification System

### ❌ Bad: Tightly Coupled
```python
class NotificationService:
    def send_notification(self, type, message):
        if type == "EMAIL":
            sender = EmailSender() # <--- Hardcoded dependency
            sender.send(message)
        elif type == "SMS":
            sender = SMSSender()   # <--- Hardcoded dependency
            sender.send(message)
```

### ✅ Good: Factory Method
```python
# 1. Product Interface
class Sender(ABC):
    @abstractmethod
    def send(self, msg): pass

# 2. Concrete Products
class EmailSender(Sender):
    def send(self, msg): print(f"Emailing: {msg}")

class SMSSender(Sender):
    def send(self, msg): print(f"SMSing: {msg}")

# 3. Creator
class NotificationFactory(ABC):
    @abstractmethod
    def create_sender(self) -> Sender: pass

    def notify(self, message):
         # The Creator logic relies on the abstract Product, not concrete classes
        sender = self.create_sender()
        sender.send(message)

# 4. Concrete Creators
class EmailNotificationFactory(NotificationFactory):
    def create_sender(self): return EmailSender()

class SMSNotificationFactory(NotificationFactory):
    def create_sender(self): return SMSSender()
```

## When to use?
- When you don't know beforehand the exact types and dependencies of the objects your code should work with.
- When you want to provide users of your library a way to extend its internal components (e.g., adding a new "PushNotification" type without changing your core code).
