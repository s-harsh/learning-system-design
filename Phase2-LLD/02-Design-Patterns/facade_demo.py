"""
Day 8: Facade Pattern Demo
Scenario: A Smart Home System.
Turning on "Movie Mode" involves complex interactions with Lights, TV, and Sound System.
The Facade simplifies this to a single button press.
"""

# ==========================================
# 1. Complex Subsystem Classes
# ==========================================
class DVDPlayer:
    def on(self):
        print("DVD Player: ON")
    
    def play(self, movie):
        print(f"DVD Player: Playing '{movie}'")
        
    def off(self):
        print("DVD Player: OFF")

class Projector:
    def on(self):
        print("Projector: ON")
        
    def set_input(self, input_source):
        print(f"Projector: Input set to {input_source}")
        
    def off(self):
        print("Projector: OFF")

class SoundSystem:
    def on(self):
        print("Sound System: ON")
        
    def set_volume(self, level):
        print(f"Sound System: Volume set to {level}")
        
    def off(self):
        print("Sound System: OFF")

class SmartLights:
    def dim(self, percentage):
        print(f"Lights: Dimming to {percentage}%")
        
    def on(self):
        print("Lights: ON (100%)")

# ==========================================
# 2. The Facade
# ==========================================
class HomeTheaterFacade:
    def __init__(self, dvd, projector, sound, lights):
        self.dvd = dvd
        self.projector = projector
        self.sound = sound
        self.lights = lights

    def watch_movie(self, movie):
        print("\n--- Get ready to watch a movie... ---")
        self.lights.dim(10)
        self.projector.on()
        self.projector.set_input("DVD")
        self.sound.on()
        self.sound.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("\n--- Shutting down movie theater... ---")
        self.lights.on()
        self.projector.off()
        self.sound.off()
        self.dvd.off()

# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("--- Facade Pattern Demo: Smart Home ---")

    # 1. Setup the complex world
    dvd = DVDPlayer()
    projector = Projector()
    sound = SoundSystem()
    lights = SmartLights()

    # 2. Wrapper
    home_theater = HomeTheaterFacade(dvd, projector, sound, lights)

    # 3. Simple Usage
    # The client doesn't need to know about amps, projectors, or inputs
    home_theater.watch_movie("Interstellar")
    
    # ... 2 hours later ...
    home_theater.end_movie()
