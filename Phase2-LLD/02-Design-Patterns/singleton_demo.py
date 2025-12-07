"""
Day 7: Singleton Pattern Demo
Shows:
1. Standard Singleton (Naive)
2. Thread-Safe Singleton (Double-Checked Locking)
3. The "Borg" (Monostate) Pattern - Python specific flavor
"""

import threading
import time

print("--- 1. Classic Singleton (Naive) ---")

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating the Singleton Instance...")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Careful! __init__ is called every time __new__ returns an instance.
        # usually you want to initialize data only once.
        if not hasattr(self, "initialized"):
            self.data = "Database Connection Info"
            self.initialized = True

s1 = Singleton()
s2 = Singleton()

print(f"s1 is s2? {s1 is s2}")  # True
print(f"s1 data: {s1.data}")


print("\n--- 2. Thread Safety Test ---")

def test_singleton():
    s = Singleton()
    print(f"Instance ID: {id(s)}")

# If we run this quickly in threads, a naive singleton *might* fail, 
# though Python's GIL actually protects us a bit here for simple ops. 
# But let's look at the robust implementation.

print("--- 3. Thread-Safe Singleton ---")

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    # Simulate slow work (e.g., DB connection)
                    # This increases chance of race condition in naive code
                    time.sleep(0.1) 
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

# Let's verify with threads
def get_instance():
    s = ThreadSafeSingleton()
    print(f"Got Safe Instance: {id(s)}")

threads = []
print("Launching 5 threads...")
for i in range(5):
    t = threading.Thread(target=get_instance)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads should have same ID.")
