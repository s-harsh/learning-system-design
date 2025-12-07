# Deep Dive: SOLID Principles & The Art of Low-Level Design 🧱

> "Software design is an investment. It is about how much change allows you to innovate in the future."

Welcome to **Phase 2: Low-Level Design (LLD)**. While Phase 1 (System Design) was about how boxes (servers) talk to each other, Phase 2 is about how the **code inside those boxes** is organized.

You might ask: *"Why do I care? I can just write function scripts."*
In a startup, you write fast. In a unicorn (scale-up), you **manage complexity**. SOLID is the toolkit for managing complexity.

---

## 🌎 The Big Picture: Why Industry Obsesses Over SOLID

Imagine you are building a **Payment System** like Stripe.
1.  **Day 1**: You support Credit Cards. You write a big `if/else` block.
2.  **Day 50**: You need to support PayPal, Crypto, and Apple Pay.
3.  **The Crisis**: To add Crypto, you have to open the file that handles Credit Cards. You accidentally delete a line. **Credit Cards stop working.**

This is called **Coupling**. SOLID principles are designed to **decouple** your code so you can add features (Crypto) without breaking existing ones (Credit Cards).

---

## 1. Single Responsibility Principle (SRP) 🎯
> **"A class should have only one reason to change."**

### ❌ The Symptom (The "God Class")
You have a class `UserManager` that:
1.  Registers the user.
2.  Validates the email format.
3.  Sends the welcome email.
4.  Logs the activity to a file.

**Why it's bad:** If the **Email Provider** changes (e.g., from SMTP to SendGrid), you risk breaking the **User Registration** logic because they are in the same file.

### ✅ The Solution
Split responsibilities into small, focused classes.

### 🐍 Code Example (Python)

**Bad Way:**
```python
class User:
    def __init__(self, name: str):
        self.name = name
    
    def save_to_db(self):
        # Database logic mixed with business logic
        print(f"Saving {self.name} to Database...")
    
    def send_email(self, message: str):
        # Notification logic mixed with business logic
        print(f"Sending email to {self.name}: {message}")

# Usage
u = User("Harsh")
u.save_to_db()
u.send_email("Welcome!")
```

**Good Way (SRP Compliant):**
```python
# 1. Pure Data Class
class User:
    def __init__(self, name: str):
        self.name = name

# 2. Repository (Handles DB)
class UserRepository:
    def save(self, user: User):
        print(f"Saving {user.name} to Database...")

# 3. Notification Service (Handles Email)
class EmailService:
    def send_welcome_email(self, user: User):
        print(f"Sending welcome email to {user.name}...")

# Usage orchestration
u = User("Harsh")
repo = UserRepository()
email = EmailService()

repo.save(u)
email.send_welcome_email(u)
```

---

## 2. Open/Closed Principle (OCP) 🚪
> **"Software entities should be Open for extension, but Closed for modification."**

### ❌ The Symptom (The "If/Else Hell")
You have a function `process_payment(type)` that has a switch statement: `if type == 'credit': ... elif type == 'paypal': ...`.
Every time you add a payment method, you must **modify** this tested, production file.

### ✅ The Solution
Use **Polymorphism** (Interfaces/Abstract Classes). New features = **New Files**, not changing old files.

### 🏭 Industry Use Case: Plugins
VS Code extensions, Chrome plugins, and Payment Gateways all use OCP. The core browser code doesn't change when you install an AdBlocker; the AdBlocker simply *extends* the browser.

### 🐍 Code Example

**Bad Way:**
```python
class PaymentProcessor:
    def pay(self, amount, type):
        if type == "credit":
            print(f"Paying ${amount} via Credit Card")
        elif type == "paypal":
            print(f"Paying ${amount} via PayPal")
        # To add Bitcoin, I MUST modify this class. Risk!
```

**Good Way (OCP Compliant):**
```python
from abc import ABC, abstractmethod

# 1. Define the Interface (The Contract)
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# 2. Implement Extensions (New Files)
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} via Credit Card 💳")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} via PayPal 🅿️")

class Bitcoin(PaymentMethod): # Added later! No need to touch CreditCard code.
    def pay(self, amount):
        print(f"Paying ${amount} via Bitcoin 🪙")

# 3. Usage (The Processor doesn't care WHAT method it is)
class PaymentProcessor:
    def process(self, amount, method: PaymentMethod):
        method.pay(amount)

processor = PaymentProcessor()
processor.process(100, Bitcoin())
```

---

## 3. Liskov Substitution Principle (LSP) 🧩
> **"Subtypes must be substitutable for their base types."**

### ❌ The Symptom (The "Fake Child")
You inherit from a parent class but break its rules.
*   **Classic Example**: A `Square` inherits from `Rectangle` but changing width also changes height, breaking the expectation of a Rectangle where width/height are independent.
*   **Industry Example**: You have a `FileSystem` class with `read()` and `write()`. You create a `ReadOnlyFileSystem` subclass but `write()` throws an error. This violates LSP because code expecting a `FileSystem` will crash if it tries to write.

### ✅ The Solution
If you find yourself throwing "NotImplementedError" or "NotSupportedException" in an override, you are likely violating LSP. **Don't inherit if you can't fulfill the promise.**

### 🐍 Code Example

**Bad Way:**
```python
class Bird:
    def fly(self):
        print("I can fly!")

class Ostrich(Bird):
    def fly(self):
        # Ostrich is a Bird, but...
        raise Exception("I cannot fly! 🐧")

def make_bird_fly(bird: Bird):
    bird.fly() # Crashes if Ostrich is passed!
```

**Good Way (Hierarchy Refactoring):**
```python
class Bird:
    def eat(self):
        print("I can eat")

class FlyingBird(Bird):
    def fly(self):
        print("I can fly")

class Sparrow(FlyingBird):
    pass

class Ostrich(Bird): # Inherits only basic Bird traits, not flight
    pass

# Usage
def make_bird_fly(bird: FlyingBird): # Contracts are clear
    bird.fly() 
```

---

## 4. Interface Segregation Principle (ISP) 🔪
> **"Many client-specific interfaces are better than one general-purpose interface."**

### ❌ The Symptom (The "Fat Interface")
You have a massive interface `IMachine` with methods: `print()`, `scan()`, `fax()`, `staple()`.
A simple Printer class must implement `fax()` even if it can't fax, just to satisfy the compiler/inheritance.

### ✅ The Solution
Split the big interface into `IPrinter`, `IScanner`, `IFax`.

### 🏭 Industry Use Case: React Props / AWS SDK
Instead of importing the *entire* AWS SDK (which is huge), you import just the client you need (`S3Client`, `DynamoDBClient`). This is modularity at the library level.

### 🐍 Code Example

**Bad Way:**
```python
class MultiFunctionDevice(ABC):
    @abstractmethod
    def print_doc(self): pass
    
    @abstractmethod
    def scan_doc(self): pass
    
    @abstractmethod
    def fax_doc(self): pass

class OldPrinter(MultiFunctionDevice):
    def print_doc(self):
        print("Printing...")
    
    def scan_doc(self):
        # Forced to implement useless method
        raise NotImplementedError("I can't scan!")
        
    def fax_doc(self):
        raise NotImplementedError("I can't fax!")
```

**Good Way:**
```python
class Printer(ABC):
    @abstractmethod
    def print_doc(self): pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self): pass

class ModernMachine(Printer, Scanner): # Multiple Inheritance / Interfaces
    def print_doc(self): print("Printing...")
    def scan_doc(self): print("Scanning...")

class OldPrinter(Printer): # Only implements what it needs
    def print_doc(self): print("Printing...")
```

---

## 5. Dependency Inversion Principle (DIP) 🔌
> **"High-level modules should not depend on low-level modules. Both should depend on abstractions."**

### ❌ The Symptom (tight Coupling)
Your high-level business logic (e.g., `OrderService`) imports a specific database class (e.g., `MySQLConnection`).
If you want to switch to PostgreSQL or MongoDB, you have to rewrite `OrderService`.

### ✅ The Solution
`OrderService` should depend on an interface `IDatabase`. `MySQLConnection` implements that interface. The "dependency" is injected (usually via constructor).

### 🏭 Industry Use Case: Hexagonal Architecture / Clean Architecture
This is how modern backends are built. The "Core Domain" is pure. The database, API, and UI are just plugins that plug into the core.

### 🐍 Code Example

**Bad Way:**
```python
class MySQLDatabase:
    def save(self, data):
        print("Saving to MySQL")

class OrderService:
    def __init__(self):
        # Direct dependency on low-level module
        self.db = MySQLDatabase()
    
    def place_order(self, order):
        self.db.save(order)
```

**Good Way (Dependency Injection):**
```python
class DatabaseInterface(ABC): # Abstraction
    @abstractmethod
    def save(self, data):
        pass

class MacOSPostgres(DatabaseInterface): # Low-level 1
    def save(self, data):
        print("Saving to Postgres on Mac")

class LinuxMySQL(DatabaseInterface): # Low-level 2
    def save(self, data):
        print("Saving to MySQL on Linux")

class OrderService: # High-level
    # We ask for the Abstraction, not the concrete class
    def __init__(self, db: DatabaseInterface):
        self.db = db
    
    def place_order(self, order):
        self.db.save(order)

# Injection happens at the top level
my_db = MacOSPostgres()
service = OrderService(my_db) # We "inject" the dependency
service.place_order("Order #1")
```

---

## Summary Cheat Sheet

| Principle | Acronym | Catchphrase | Key takeaway |
| :--- | :--- | :--- | :--- |
| **S**ingle Responsibility | **SRP** | "Do one thing well." | Split giant classes. |
| **O**pen/Closed | **OCP** | "Add, don't change." | Use interfaces/polymorphism to add features. |
| **L**iskov Substitution | **LSP** | "Don't fake it." | Subclasses must honor the parent's contract. |
| **I**nterface Segregation | **ISP** | "Don't force useless methods." | Split giant interfaces. |
| **D**ependency Inversion | **DIP** | "Depend on abstractions." | Inject dependencies, don't `new` them. |

