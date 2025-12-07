# Adapter Pattern

> "Wrap an incompatible object in an adapter to make it compatible with another class."

**Type:** Structural

## The Problem
You have an existing app that works with `JSON`.
You want to integrate a 3rd party Analytics Library, but it only accepts `XML`.
- You can't change the 3rd party library code.
- You shouldn't change your whole app to use XML just for this one feature.

## The Solution
Create an **Adapter**.
- It implements the interface your client expects (JSON-like).
- It wraps the incompatible object (XML Library).
- It translates calls from one format to the other.

## Real World Analogies
1.  **Power Adapter**: US Plug (Client) -> US-to-EU Adapter -> EU Socket (Service).
2.  **Card Reader**: SD Card (Service) -> USB Adapter -> Laptop USB Port (Client).

## Implementation Ways
1.  **Object Adapter** (Composition): The adapter holds an instance of the wrapped class. (Most common).
2.  **Class Adapter** (Inheritance): The adapter inherits from both classes. (Less flexible, avoids Multiple Inheritance issues in some languages).

## Example: Analytics Library

### Old Interface (Client Expects This)
```python
def log_event(self, json_data):
    # Expects dict/json
    pass
```

### New Library (Service Has This)
```python
def send_xml_data(self, xml_string):
    # Expects string like "<root>...</root>"
    pass
```

### The Adapter
```python
class XmlAdapter:
    def __init__(self, xml_library):
        self.lib = xml_library

    def log_event(self, json_data):
        # 1. Translate JSON -> XML
        xml = self._convert_to_xml(json_data)
        # 2. Call the service
        self.lib.send_xml_data(xml)
```
