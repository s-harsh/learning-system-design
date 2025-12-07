"""
Day 8: Decorator Pattern Demo
Scenario: A Coffee Shop Ordering System.
We dynamicially add ingredients to a base beverage.
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. Component Interface
# ==========================================
class Beverage(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

# ==========================================
# 2. Concrete Component (The Base Object)
# ==========================================
class Espresso(Beverage):
    def get_cost(self):
        return 2.00

    def get_description(self):
        return "Espresso"

class Tea(Beverage):
    def get_cost(self):
        return 1.50

    def get_description(self):
        return "Tea"

# ==========================================
# 3. Decorator (The Wrappers)
# ==========================================
class AddonDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

# ==========================================
# 4. Concrete Decorators
# ==========================================
class Milk(AddonDecorator):
    def get_cost(self):
        return self._beverage.get_cost() + 0.50

    def get_description(self):
        return self._beverage.get_description() + ", Milk"

class Mocha(AddonDecorator):
    def get_cost(self):
        return self._beverage.get_cost() + 0.75

    def get_description(self):
        return self._beverage.get_description() + ", Mocha"

class Whip(AddonDecorator):
    def get_cost(self):
        return self._beverage.get_cost() + 1.00

    def get_description(self):
        return self._beverage.get_description() + ", Whip"

# ==========================================
# Usage
# ==========================================
if __name__ == "__main__":
    print("--- Decorator Pattern Demo: Coffee Shop ---\n")

    # Order 1: Simple Espresso
    beverage1 = Espresso()
    print(f"Order 1: {beverage1.get_description()} = ${beverage1.get_cost():.2f}")

    # Order 2: Espresso + Milk + Mocha
    # We wrap the object layer by layer
    beverage2 = Espresso()
    beverage2 = Milk(beverage2)
    beverage2 = Mocha(beverage2)
    
    print(f"Order 2: {beverage2.get_description()} = ${beverage2.get_cost():.2f}")

    # Order 3: Tea + Whip + Whip (Double Whip)
    beverage3 = Tea()
    beverage3 = Whip(beverage3)
    beverage3 = Whip(beverage3)

    print(f"Order 3: {beverage3.get_description()} = ${beverage3.get_cost():.2f}")
