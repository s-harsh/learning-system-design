# Day 8: Structural Engineering... for Code 🏗️

After laying the foundation with SOLID, today was about **Structure**. 
In Day 8 of my System Design journey, I learned how to connect incompatible objects, wrap them in new behaviors, and hide complexity behind a single button.

Here’s the breakdown:

### 1️⃣ Builder Pattern 🍕
- **Problem**: `new Pizza(12, true, false, true, true, false...)`. Telescoping constructors are a nightmare.
- **Solution**: `PizzaBuilder().size(12).cheese().bake()`. Fluent, readable, and clean.

### 2️⃣ Adapter Pattern 🔌
- **Problem**: Your app speaks JSON. The new library speaks XML.
- **Solution**: Don't rewrite the app. Write an **Adapter**. Just like a Travel Plug allows your US charger to work in a UK socket, the Adapter Pattern makes incompatible interfaces collaborate.

### 3️⃣ Decorator Pattern ☕
- **Problem**: You want `Coffee`, `CoffeeWithMilk`, `CoffeeWithMilkAndSugar`... Inheritance explosion!
- **Solution**: Wrap objects at runtime.
- `Sugar(Milk(Coffee()))`. It's like Russian Matryoshka dolls. The object sits inside layers of behavior.

### 4️⃣ Facade Pattern 🎭
- **Problem**: To watch a movie, you have to: `Amplifier.on()`, `Projector.on()`, `Lights.dim()`, `Screen.down()`.
- **Solution**: `HomeTheater.watchMovie()`. The Facade provides a simple interface to a complex subsystem.

---

### 🧠 Key Takeaway
**Structural Patterns** are about relations between classes. They are the "glue" and "duct tape" of software engineering. They help you integrate legacy code and third-party libraries without polluting your own clean architecture.

👇 *Code and Visuals in the repo!*

#SystemDesign #DesignPatterns #Python #SoftwareArchitecture #AdapterPattern #Decorator #Learning
