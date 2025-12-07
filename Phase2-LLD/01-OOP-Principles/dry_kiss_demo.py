"""
Day 7: DRY (Don't Repeat Yourself) & KISS (Keep It Simple, Stupid)
Demo: Refactoring "WET" and "Complex" code into Clean Code.
"""

import math

# ==========================================
# 1. DRY Principle Demo
# Scenario: calculating area and perimeter for shapes
# ==========================================

print("--- 1. DRY Principle Demo ---")

# ❌ BAD: WET Code (Write Everything Twice)
# If we decide to change precision or logic, we have to fix it in 4 places.
def analyze_circle_wet(radius):
    area = 3.14159 * radius * radius
    perimeter = 2 * 3.14159 * radius
    print(f"Circle (R={radius}): Area={area:.2f}, Perimeter={perimeter:.2f}")

def analyze_cylinder_wet(radius, height):
    base_area = 3.14159 * radius * radius
    lateral_area = 2 * 3.14159 * radius * height
    total_area = 2 * base_area + lateral_area
    print(f"Cylinder (R={radius}, H={height}): Surface Area={total_area:.2f}")

# ✅ GOOD: DRY Code
# Single Source of Truth for Circle Math
class CircleMath:
    PI = 3.14159
    
    @staticmethod
    def area(radius):
        return CircleMath.PI * (radius ** 2)
    
    @staticmethod
    def circumference(radius):
        return 2 * CircleMath.PI * radius

def analyze_circle_dry(radius):
    area = CircleMath.area(radius)
    circ = CircleMath.circumference(radius)
    print(f"DRY Circle (R={radius}): Area={area:.2f}, Circ={circ:.2f}")

def analyze_cylinder_dry(radius, height):
    base_area = CircleMath.area(radius)
    # Lateral area is effectively a rectangle: circumference * height
    lateral_area = CircleMath.circumference(radius) * height
    total_area = (2 * base_area) + lateral_area
    print(f"DRY Cylinder (R={radius}, H={height}): Surface Area={total_area:.2f}")

analyze_circle_wet(5)
analyze_cylinder_wet(5, 10)
print("...")
analyze_circle_dry(5)
analyze_cylinder_dry(5, 10)
print("\n")


# ==========================================
# 2. KISS Principle Demo
# Scenario: Filtering a list of even numbers from input
# ==========================================

print("--- 2. KISS Principle Demo ---")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ❌ BAD: Over-Engineered (Enterprise Style)
# Unnecessary abstraction layers for a trivial task
class NumberProcessor:
    def __init__(self, data):
        self.data = data
        
    def filter_data(self, strategy_func):
        result = []
        for item in self.data:
            if strategy_func(item):
                result.append(item)
        return result

class EvenNumberStrategy:
    def is_valid(self, number):
        # Bitwise operator just to show off, instead of simple modulo
        return (number & 1) == 0

processor = NumberProcessor(data)
strategy = EvenNumberStrategy()
result_complex = processor.filter_data(strategy.is_valid)
print(f"Complex Result: {result_complex}")


# ✅ GOOD: KISS (Keep It Simple, Stupid)
# Pythonic, readable, one logical line.
result_simple = [x for x in data if x % 2 == 0]
print(f"Simple Result:  {result_simple}")
