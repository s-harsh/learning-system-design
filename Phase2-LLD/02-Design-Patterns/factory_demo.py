"""
Day 7: Factory Method Pattern Demo
Scenario: A Payment Processing System.
We want to process payments (Credit Card, PayPal, Crypto) without modifying the main client code.
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. The Product Interface
# ==========================================
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

# ==========================================
# 2. Concrete Products
# ==========================================
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        # Specific PayPal logic (API calls, etc.)
        print(f"✅ Processed ${amount} via PayPal API.")

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        # Specific Stripe logic
        print(f"✅ Processed ${amount} via Stripe (Credit Card).")

class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"✅ Processed ${amount} via Bitcoin Network.")

# ==========================================
# 3. The Creator (Factory)
# ==========================================
class PaymentFactory(ABC):
    @abstractmethod
    def create_processor(self) -> PaymentProcessor:
        pass

    # The core business logic uses the product interface
    def perform_transaction(self, amount: float):
        processor = self.create_processor()
        print(f"Initiating transaction for ${amount}...")
        processor.process_payment(amount)
        print("Transaction Complete.\n")

# ==========================================
# 4. Concrete Creators
# ==========================================
class PayPalFactory(PaymentFactory):
    def create_processor(self) -> PaymentProcessor:
        return PayPalProcessor()

class StripeFactory(PaymentFactory):
    def create_processor(self) -> PaymentProcessor:
        return StripeProcessor()

class CryptoFactory(PaymentFactory):
    def create_processor(self) -> PaymentProcessor:
        return CryptoProcessor()


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("--- Factory Method Pattern Demo ---\n")

    # Client code works with factories, not concrete product classes
    # This simulates configuration-driven logic
    
    # User selects "Stripe" in settings
    factory: PaymentFactory = StripeFactory()
    factory.perform_transaction(100.50)

    # User switches to "PayPal"
    factory = PayPalFactory()
    factory.perform_transaction(50.00)

    # User is a tech bro
    factory = CryptoFactory()
    factory.perform_transaction(0.05)
