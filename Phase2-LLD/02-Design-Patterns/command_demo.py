"""
Day 9: Command Pattern Demo
Scenario: Smart Remote Control with UNDO functionality.
We turn requests (Light On, Door Open) into objects.
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. Receiver (The Smart Devices)
# ==========================================
class Light:
    def on(self): print("💡 Light is ON")
    def off(self): print("🌑 Light is OFF")

class GarageDoor:
    def open(self): print("🚪 Garage Door is OPEN")
    def close(self): print("🚧 Garage Door is CLOSED")

# ==========================================
# 2. Command Interface
# ==========================================
class Command(ABC):
    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self): pass

# ==========================================
# 3. Concrete Commands
# ==========================================
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self): self.light.on()
    def undo(self): self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self): self.light.off()
    def undo(self): self.light.on()

class GarageOpenCommand(Command):
    def __init__(self, door: GarageDoor):
        self.door = door
        
    def execute(self): self.door.open()
    def undo(self): self.door.close()

# ==========================================
# 4. Invoker (The Remote)
# ==========================================
class SmartRemote:
    def __init__(self):
        self.history = [] # For Undo History

    def press_button(self, command: Command):
        print(f"[Remote] Executing {command.__class__.__name__}...")
        command.execute()
        self.history.append(command)

    def press_undo(self):
        if not self.history:
            print("[Remote] Nothing to undo.")
            return

        last_command = self.history.pop()
        print(f"[Remote] Undoing {last_command.__class__.__name__}...")
        last_command.undo()

# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("--- Command Pattern Demo: Smart Remote ---\n")

    # 1. Setup Devices
    living_room_light = Light()
    garage = GarageDoor()

    # 2. Create Commands
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)
    garage_open = GarageOpenCommand(garage)

    # 3. Use Remote
    remote = SmartRemote()

    remote.press_button(light_on)   # Turn Light ON
    remote.press_button(garage_open) # Open Garage

    print("\n--- Oops! Hit Undo ---")
    remote.press_undo() # Closes garage
    remote.press_undo() # Turns light OFF
    remote.press_undo() # Nothing left
