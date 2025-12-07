# Introduction to Design Patterns

> "Design patterns are solutions to recurring problems in software design."

They are not code; they are **blueprints**. You customize them to solve a particular design problem in your code.

## Why Learn Patterns?
1.  **Shared Vocabulary**: Instead of saying, *"I created a class that ensures only one instance exists and gives global access to it,"* you say, *"I used a Singleton."*
2.  **Proven Solutions**: These patterns have survived decades of engineering trials. They work.
3.  **Code Reusability**: They help decouple code, making it modular and easier to test.

---

## The Three Categories

### 1. Creational Patterns (Construction)
*Focus: How objects are created.*
They abstract the instantiation process. They help make a system independent of how its objects are created, composed, and represented.

| Pattern | Description | Real-world Analogy |
| :--- | :--- | :--- |
| **Singleton** | Ensure a class has only one instance. | The President of a country. |
| **Factory Method** | Delegate object creation to subclasses. | A logistics company (Truck vs Ship). |
| **Builder** | Construct complex objects step by step. | Subway Sandwich assembly line. |
| **Prototype** | Copy an existing object. | Cell division / Dolly the sheep. |

### 2. Structural Patterns (Structure)
*Focus: How objects are connected.*
They form larger structures from small objects. They are concerned with how classes and objects are composed to form larger structures.

| Pattern | Description | Real-world Analogy |
| :--- | :--- | :--- |
| **Adapter** | Make incompatible interfaces work together. | Power plug adapter (US to EU). |
| **Decorator** | Add responsibilities dynamically. | Wearing a coat over a shirt (layers). |
| **Facade** | Simple interface to a complex system. | Car dashboard (hides engine complexity). |
| **Proxy** | A placeholder for another object. | Credit card (proxy for cash). |

### 3. Behavioral Patterns (Communication)
*Focus: How objects talk to each other.*
They are concerned with algorithms and the assignment of responsibilities between objects.

| Pattern | Description | Real-world Analogy |
| :--- | :--- | :--- |
| **Observer** | Notify subscribers of changes. | Newsletter / YouTube bell icon. |
| **Strategy** | Swap algorithms at runtime. | Maps (Walk vs Drive vs Transit). |
| **Command** | Turn a request into an object. | Restaurant order ticket. |
| **State** | Alter behavior when internal state changes. | Phone (Silent vs Ring mode). |

---

## The Golden Rule of Patterns
**Don't force them.**
If a simple `if` statement works, don't use the Strategy pattern. Use patterns only when:
1.  The problem matches the pattern's intent.
2.  The added complexity pays off in flexibility.
