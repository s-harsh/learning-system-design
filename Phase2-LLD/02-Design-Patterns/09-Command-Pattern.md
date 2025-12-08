# Command Pattern

> "Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations."

**Type:** Behavioral

## The Problem
You are building a **Smart Home Remote**.
- It has buttons.
- You want to program the buttons: Button A turns on Light, Button B turns on TV.
- **Bad Approach:** Hardcoding.
   ```python
   def press_button_a():
       light.on() # Tied forever to Light
   ```
- **Challenge:** How do you support **Undo**? If I press "Undo", how does the remote know what the last button did?

## The Solution
Turn "Turn On Light" into an object: `LightOnCommand`.
- It has an `execute()` method.
- It has an `undo()` method.
The Remote just holds a list of Command objects.

## Real World Analogies
1.  **Diner Order**: You give an order to a waiter (Command). The waiter queues it. The chef executes it. You can cancel (Undo) before it's cooked.
2.  **Text Editors**: Ctrl+Z (Undo). The editor keeps a stack of every keystroke command.

### Key Components
1.  **Command Interface**: `execute()`, `undo()`.
2.  **Concrete Commands**: `LightOnCommand`, `TVOnCommand`.
3.  **Invoker**: The Remote/Button.
4.  **Receiver**: The Light/TV.

### Code Structure
```python
class Command(ABC):
    def execute(self): pass
    def undo(self): pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()
        
    def undo(self):
        self.light.off() # The reverse logic
```
