# State Pattern

> "Allow an object to alter its behavior when its internal state changes. The object will appear to change its class."

**Type:** Behavioral

## The Problem
You are building a **Document Management System**.
A document behaves differently depending on its state:
- **Draft**: Can be edited. Can be submitted for review.
- **Moderation**: Cannot be edited. Can be Approved or Rejected.
- **Published**: Cannot be edited. Can be expired.
- **Expired**: Sent to archive.

### ❌ Bad: Massive Switch Statements
```python
class Document:
    def publish(self):
        if self.state == "DRAFT":
            print("Error: Must review first")
        elif self.state == "MODERATION":
            self.state = "PUBLISHED"
            print("Published!")
        elif self.state == "PUBLISHED":
            print("Already published")
```
As you add states (e.g., "Archived", "Rejected"), this `publish` method (and every other method like `edit`, `expire`, `delete`) becomes unmaintainable.

## The Solution
Create a class for each State.
The Document delegates the method call to the State object.
- `DraftState.publish()` -> "Error, send to review first".
- `ModerationState.publish()` -> "Transition to PublishedState".

## Real World Analogies
1.  **Vending Machine**: Behavior of buttons changes if you have inserted money or not.
2.  **Phone**: The "Volume Up" button rings louder if screen is off, but increases video volume if YouTube is open.

### Key Components
1.  **Context**: The object (Document) with the current state.
2.  **State Interface**: Defines behavior for all actions (`publish()`, `edit()`).
3.  **Concrete States**: `Draft`, `Published` classes implementing the behavior.

### Code Structure
```python
class State(ABC):
    def publish(self, doc): pass

class DraftState(State):
    def publish(self, doc):
        print("Moving to review...")
        doc.state = ModerationState() 

class Document:
    def __init__(self):
        self.state = DraftState()
    
    def publish(self):
        self.state.publish(self)
```
