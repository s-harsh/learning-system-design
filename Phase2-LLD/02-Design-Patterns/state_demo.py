"""
Day 9: State Pattern Demo
Scenario: Document Workflow System.
A document transitions between DRAFT, MODERATION, and PUBLISHED states.
Behavior of 'publish()' changes depending on the state.
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. The Context (The Document)
# ==========================================
class Document:
    def __init__(self):
        self.state = DraftState() # Initial State
    
    def change_state(self, state):
        self.state = state
        print(f"🔄 State transitions to: {state.__class__.__name__}")
        
    def publish(self):
        self.state.publish(self)

    def edit(self):
        self.state.edit(self)

# ==========================================
# 2. State Interface
# ==========================================
class State(ABC):
    @abstractmethod
    def publish(self, document): pass

    @abstractmethod
    def edit(self, document): pass

# ==========================================
# 3. Concrete States
# ==========================================
class DraftState(State):
    def publish(self, document):
        # Logic: Can't publish directly, must go to moderation
        print("📝 Draft submitted for moderation.")
        document.change_state(ModerationState())

    def edit(self, document):
        print("✏️ Editing Draft... Content updated.")

class ModerationState(State):
    def publish(self, document):
        # Logic: Review successful, now we publish
        print("✅ Review successful. Publishing document.")
        document.change_state(PublishedState())

    def edit(self, document):
        print("❌ Cannot edit document while in Moderation.")

class PublishedState(State):
    def publish(self, document):
        print("⚠️ Document is already published.")

    def edit(self, document):
        print("❌ Cannot edit. Use 'Create New Version' instead.")

# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("--- State Pattern Demo: Workflow ---\n")

    # 1. New Document (Draft)
    doc = Document()
    
    # 2. Work in Draft State
    doc.edit()        # Allowed
    doc.publish()     # Moves to Moderation
    
    print("\n--- In Moderation now ---")
    doc.edit()        # Blocked
    doc.publish()     # Moves to Published
    
    print("\n--- In Published now ---")
    doc.publish()     # Blocked
    doc.edit()        # Blocked
