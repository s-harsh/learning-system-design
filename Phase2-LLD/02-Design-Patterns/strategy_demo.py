"""
Day 9: Strategy Pattern Demo
Scenario: E-Commerce Discount Engine.
We want to apply different discount rules at runtime (Seasonal, Member, Bulk).
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. The Strategy Interface
# ==========================================
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass

# ==========================================
# 2. Concrete Strategies
# ==========================================
class NoDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price

class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.90  # 10% off

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.80  # 20% off

class BulkBuyDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        # If over $1000, take $100 off, else normal price
        if price > 1000:
            return price - 100
        return price

# ==========================================
# 3. The Context
# ==========================================
class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.strategy = discount_strategy
        self.items = []

    def add_item(self, price):
        self.items.append(price)

    def set_strategy(self, discount_strategy: DiscountStrategy):
        # We can change strategy at runtime!
        print(f"--> Switching strategy to: {discount_strategy.__class__.__name__}")
        self.strategy = discount_strategy

    def checkout(self):
        total = sum(self.items)
        final_price = self.strategy.apply_discount(total)
        print(f"Total: ${total:.2f} | Final Bill: ${final_price:.2f}")

# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("--- Strategy Pattern Demo: Pricing Engine ---\n")

    # 1. Normal User
    cart = ShoppingCart(NoDiscount())
    cart.add_item(100)
    cart.add_item(500)
    cart.checkout()

    # 2. User logs in (becomes VIP)
    cart.set_strategy(VIPDiscount())
    cart.checkout()

    # 3. Holiday Season Starts
    cart.set_strategy(SeasonalDiscount())
    cart.checkout()
    
    # 4. Big Spender
    cart.add_item(1000) # Total now 1600
    cart.set_strategy(BulkBuyDiscount())
    cart.checkout()
