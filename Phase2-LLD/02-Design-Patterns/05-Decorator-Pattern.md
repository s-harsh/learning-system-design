# Decorator Pattern

> "Attach new responsibilities to an object dynamically."

**Type:** Structural

## The Problem
You want to add features to a class, but:
1.  **Inheritance Explosion**: If you have a `Coffee` class and want to support `Milk`, `Sugar`, `Whip`, in any combination, you'd end up with `CoffeeWithMilkAndSugar`, `CoffeeWithWhip`, etc.
2.  **Runtime Flexibility**: You want to decide at *runtime* whether to wrap an object, not at compile time.

## The Solution
Wrap the original object inside a "Decorator" class that has the same interface.
- The Decorator calls the original object's method.
- Then adds its own behavior before or after.

## Real World Analogies
1.  **Matryoshka Dolls**: You put a doll inside a bigger doll.
2.  **Clothing**: You (Component) wear a Shirt (Decorator 1) and a Jacket (Decorator 2). You are still "You", but warmer.

## Python's `@decorator` Syntax vs The Pattern
**Note:** Python has a built-in feature called "decorators" (`@my_decorator`), which is similar in spirit but applied to **functions/classes** at definition time.
The **Gang of Four Decorator Pattern** is about wrapping **objects** at runtime.

### Example: Coffee Shop

#### The Component Interface
```python
class Coffee(ABC):
    def get_cost(self): pass
    def get_description(self): pass
```

#### Concrete Component
```python
class SimpleCoffee(Coffee):
    def get_cost(self): return 5
    def get_description(self): return "Coffee"
```

#### The Decorator
```python
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee # The wrapped object

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()
```

#### Concrete Decorators
```python
class Milk(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 2 # Add logic

    def get_description(self):
        return self._coffee.get_description() + ", Milk"
```

#### Usage
```python
my_coffee = SimpleCoffee()
my_coffee = Milk(my_coffee) # Wrap it 
my_coffee = Sugar(my_coffee) # Wrap it again!
# Now my_coffee is a Sugar-wrapped Milk-wrapped Coffee.
```
