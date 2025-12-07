# Facade Pattern

> "Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use."

**Type:** Structural

## The Problem
Your code needs to work with a complex library or framework that has dozens of objects.
To perform a simple action (e.g., "Upload Video"), you have to:
1.  Initialize `VideoEncoder`.
2.  Set `Bitrate`.
3.  Connect to `CloudStorage`.
4.  Authenticate `User`.
5.  Upload chunks.

If you do this in your client code, your business logic becomes tightly coupled to the implementation details of the video library.

## The Solution
Create a **Facade** class.
- It exposes a simple method: `uploadVideo(file)`.
- Internally, it handles all the messy initialization and orchestration.

## Real World Analogies
1.  **Car Dashboard**: You press "Start Button".
    - Behind the scenes: Fuel injection, Starter motor, Spark plugs, Battery check.
    - You don't need to know this.
2.  **Customer Support**: You call one number.
    - They route you to billing, technical, or logistics.
    - You don't have to call 5 different departments yourself.

## Example: Home Theater System

### Complex Subsystem Classes
```python
class Amplifier:
    def on(self): ...
    def set_volume(self, level): ...

class Projector:
    def on(self): ...
    def set_input(self, source): ...

class Lights:
    def dim(self, level): ...
```

### The Facade
```python
class HomeTheaterFacade:
    def __init__(self, amp, projector, lights):
        self.amp = amp
        self.projector = projector
        self.lights = lights

    def watch_movie(self, movie):
        print(f"Get ready to watch {movie}...")
        self.lights.dim(10)
        self.projector.on()
        self.projector.set_input("BluRay")
        self.amp.on()
        self.amp.set_volume(5)
```

### Client Code
```python
# Simple!
home_theater.watch_movie("Inception")
```
