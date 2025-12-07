# 🧩 Liskov Substitution Principle (LSP): The Inheritance Trap

> **"If S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desirable properties of the program."**  
> — *Barbara Liskov*

In plain English: **"Don't advertise what you can't deliver."**

If your child class says "I am a File", but crashes when I try to run `.write()`, you have lied to me. You violated LSP.

---

## 🏗️ The Real-World Scenario: The File System

You are building a cloud storage system (like Dropbox). You have a base class for `File`.

### The Violation (The "Fake" Child) ❌

```python
class File:
    def read(self):
        print("Reading data...")
        
    def write(self, data):
        print(f"Writing {data} to disk...")

class ReadOnlyFile(File):
    # INHERITANCE TRAP! 
    # ReadOnlyFile "IS A" File, right? So we inherit.
    
    def write(self, data):
        # WAIT! I can't write. I'm read-only.
        raise Exception("Error: This file is read-only!")
```

### The Crash 💥
Somewhere in your app, you have a function that auto-saves all open files.

```python
def auto_save_all(files: list[File]):
    for f in files:
        if isinstance(f, File):
            # The code trusts the "File" type contract
            f.write("Autosave Data") # CRASHES when it hits a ReadOnlyFile!
```

**Why this is dangerous:**
The function `auto_save_all` did nothing wrong. It asked for a `File`. The `File` class promised a `.write()` method. The `ReadOnlyFile` broke that promise.

---

## 🛠️ The Refactor: Hierarchy Separation

If a class can't do everything the parent does, **it shouldn't be a child**.
We need to separate the capabilities.

### Method 1: Split the Interfaces

```python
class Readable(ABC):
    @abstractmethod
    def read(self): pass

class Writable(ABC):
    @abstractmethod
    def write(self, data): pass

# Now we compose them exactly as needed

class TextFile(Readable, Writable):
    def read(self): ...
    def write(self, data): ...

class LogFile(Readable, Writable):
    def read(self): ...
    def write(self, data): ...

class SystemConfig(Readable): # ONLY Readable. No Write method exists.
    def read(self): ...
```

### The Fix

Now, the `auto_save_all` function changes its signature to ask for **what it actually needs**.

```python
def auto_save_all(writables: list[Writable]): 
    # I only accept things that CAN write.
    # Passing a SystemConfig (ReadOnly) here will be a type error BEFORE the code runs.
    for w in writables:
        w.write("Autosave Data")
```

---

## 🏭 Industry Warning: The "Empty Method" Smell

If you ever see code like this, it's an LSP violation 99% of the time:

```python
class Penguin(Bird):
    def fly(self):
        # "Pass" means "I do nothing". 
        # But the caller EXPECTS flight.
        pass 
```

Or:

```python
class Ostrich(Bird):
    def fly(self):
        return None # Returning unexpected Null
```

**Rule of Thumb:**
If your specific class implementation does **less** than the base class (by throwing errors or doing nothing), you have structured your inheritance wrong.
