# 🧘 Single Responsibility Principle (SRP): The Master Key to Sanity

> **"Gather together the things that change for the same reasons. Separate those things that change for different reasons."**  
> — *Robert C. Martin (Uncle Bob)*

You requested depth. Let's go deep.

Most developers think SRP means *"A class should do one thing."*
Reference: *"A function should do one thing."*
**SRP is different.**

SRP is about **PEOPLE**, not just code.
**The Real Definition:**
> **"A module should be responsible to one, and only one, actor."**

---

## 🏗️ The Real-World Scenario: The "God" Order Class

Imagine you are a backend engineer at an E-commerce giant (like Amazon or Flipkart). You are working on the checkout system.

You open the codebase and find a file named `OrderManager.java` (or `.py`). It is 4,000 lines long.

### The "God Class" Anti-Pattern 👹

This class looks like this (conceptually):

```python
class OrderManager:
    def process_order(self, order_id):
        # 1. Verification Logic
        order = self.db.get(order_id)
        if order.status != 'PENDING':
            raise Exception("Invalid order")

        # 2. Inventory Logic
        if self.inventory_api.check_stock(order.items) == False:
            raise Exception("Out of stock")
            
        # 3. Payment Logic
        payment_gateway = StripeGateway()
        payment_result = payment_gateway.charge(order.total_price)
        if not payment_result.success:
            raise Exception("Payment failed")

        # 4. Tax/Invoicing Logic (The specific problem area)
        tax = order.total_price * 0.18 # GST
        pdf = self.generate_invoice_pdf(order, tax)
        
        # 5. Notification Logic
        email_client.send(order.user_email, "Your order is confirmed", attachment=pdf)
```

### Why is this efficient code actually a DISASTER? 💣

It works, right? Ideally, yes. But software changes.
Let's see what happens in a real team environment.

#### The "Change" Request
Two different departments come to your desk on the same day:

1.  **The CFO (Accounting Team)**: "Hey, looking at the invoice generation (Step 4)... we need to change the invoice format to include the new company QR code for tax compliance."
2.  **The COO (Logistics Team)**: "Hey, for Inventory (Step 2), we are switching from 'Warehouse A' to 'Warehouse B', so we need to update the stock check logic."

#### The Conflict
*   **Developer A** opens `OrderManager.py` to fix the **Invoice**.
*   **Developer B** opens `OrderManager.py` to fix the **Inventory**.

They both edit the same file. They both commit.
**GIT MERGE CONFLICT.** 💥

But wait, it gets worse.

#### The "Accidental Coupling" Bug 🐛
Developer A (Accounting) notices a helper function `format_address(user)` inside the class. They change it to match the standard strictly required for Tax Invoices (e.g., adding "STATE CODE: 29").

**Result**: The **Inventory** system (which also used `format_address` to print shipping labels) breaks because the shipping API rejects the "STATE CODE" string.

**You just broke Shipping by fixing Invoicing.**
This is why large codebases become "fragile." You touch one corner, and the opposite corner breaks.

---

## 🛠️ The Refactor: Decoupling by "Actor"

We need to split this class based on **who asks for changes**.

### 1. The Inventory Service (Actor: COO / Logistics)
Responsible *only* for checking stock. If Logistics changes warehouses, only this file changes.

```python
class InventoryService:
    def reserve_stock(self, items):
        # Call Warehouse API
        # Handle stock locking
        pass
```

### 2. The Invoice Service (Actor: CFO / Accounting)
Responsible *only* for tax rules and PDF generation.

```python
class InvoiceService:
    def generate_invoice(self, order):
        # Calculate GST
        # Draw PDF
        pass
```

### 3. The Notification Service (Actor: Marketing / Product)
Responsible *only* for talking to users.

```python
class EmailService:
    def send_confirmation(self, email, invoice_file):
        # Connect to SMTP/SendGrid
        pass
```

### 4. The Payment Processor (Actor: Finance)
Responsible *only* for the transaction.

```python
class PaymentProcessor:
    def process_payment(self, total):
        # Talk to Stripe/Razorpay
        pass
```

### 5. The Order Orchestrator (The Conductor) 🎻
This is the *only* place that ties them together. It contains **no business logic**, only **flow logic**.

```python
class OrderOrchestrator:
    def __init__(self, inventory, payment, invoice, email):
        # Dependency Injection (We will learn this in 'D')
        self.inventory = inventory
        self.payment = payment
        self.invoice = invoice
        self.email = email

    def place_order(self, order):
        # 1. Step: Inventory
        if not self.inventory.reserve_stock(order.items):
            raise Exception("Out of stock")
        
        # 2. Step: Payment
        self.payment.process_payment(order.total)
        
        # 3. Step: Post-Sales (Invoice + Email)
        pdf = self.invoice.generate_invoice(order)
        self.email.send_confirmation(order.email, pdf)
```

---

## 🏆 The Outcome

Now, let's replay the scenario:

1.  **CFO wants new QR codes?** -> You edit `InvoiceService.py`.
2.  **COO wants new Warehouse?** -> You edit `InventoryService.py`.

*   **Conflict?** Zero. They are different files.
*   **Risk?** Zero. Changing the PDF generation code literally *cannot* break the Inventory API call. They don't even know each other exists.

### Summary: How to spot SRP violations?
Ask yourself: **"What are the names of the people/departments who would ask me to change this class?"**
If the answer is "The Accountant AND The Operations Manager", split the class.
