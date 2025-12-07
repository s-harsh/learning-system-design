"""
SOLID Principles - Interactive Demo
This script demonstrates the "Good" way to implement SOLID principles.
Run this script to see the outputs.
"""

from abc import ABC, abstractmethod

print("=== 1. Single Responsibility Principle (SRP) ===")

class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        print(f"[DB] Saving user '{user.name}' to database...")

class EmailService:
    def send_welcome(self, user):
        print(f"[Email] Sending welcome email to '{user.name}'...")

# Orchestration
user = User("Harsh")
repo = UserRepository()
emailer = EmailService()

repo.save(user)
emailer.send_welcome(user)
print("\n")


print("=== 2. Open/Closed Principle (OCP) ===")

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} via Credit Card 💳")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} via PayPal 🅿️")

class Crypto(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} via Crypto (Bitcoin) 🪙")

class PaymentProcessor:
    def process(self, amount, method: PaymentMethod):
        method.pay(amount)

processor = PaymentProcessor()
processor.process(150, CreditCard())
processor.process(50, Crypto())
print("\n")


print("=== 3. Liskov Substitution Principle (LSP) ===")
# Example: Geometric Shapes properly abstracted

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

def print_area(shape: Shape):
    print(f"Area of {shape.__class__.__name__}: {shape.area()}")

print_area(Rectangle(4, 5))
print_area(Square(4))
print("\n")


print("=== 4. Interface Segregation Principle (ISP) ===")

class Printer(ABC):
    @abstractmethod
    def print_doc(self): pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self): pass

class FancyOfficeMachine(Printer, Scanner):
    def print_doc(self): print("FancyMachine: Printing...")
    def scan_doc(self): print("FancyMachine: Scanning...")

class BudgetHomePrinter(Printer):
    def print_doc(self): print("BudgetPrinter: Printing...")
    # NOTE: No scan_doc() here. We are not forced to implement it!

office = FancyOfficeMachine()
home = BudgetHomePrinter()

office.scan_doc()
home.print_doc()
print("\n")


print("=== 5. Dependency Inversion Principle (DIP) ===")

class NotificationSender(ABC):
    @abstractmethod
    def send(self, msg):
        pass

class SMSSender(NotificationSender):
    def send(self, msg):
        print(f"[SMS] {msg}")

class StackOverflowSender(NotificationSender): # Just for fun
    def send(self, msg):
        print(f"[StackOverflow Alert] {msg}")

class AlertSystem:
    def __init__(self, sender: NotificationSender):
        self.sender = sender
    
    def alert(self, message):
        self.sender.send(message)

# We can easily swap the implementation without changing AlertSystem
system_v1 = AlertSystem(SMSSender())
system_v1.alert("Server is down!")

system_v2 = AlertSystem(StackOverflowSender())
system_v2.alert("Someone downvoted your answer!")
