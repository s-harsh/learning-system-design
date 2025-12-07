# 🔪 Interface Segregation Principle (ISP): Don't Be Greedy

> **"Clients should not be forced to depend upon interfaces that they do not use."**  
> — *Robert C. Martin*

This principle is about **empathy for the consumer** of your API.
Don't make me import a 50MB library just to use one function.
Don't make me implement 20 methods just to create a simple mock object.

---

## 🏗️ The Real-World Scenario: The Smart Device

Imagine you are designing an interface for Smart Home devices (Alexa-enabled).

### The "Fat" Interface (Violation) ❌

You create one "Universal" interface that covers *everything* a device might arguably do.

```python
class ISmartDevice(ABC):
    @abstractmethod
    def turn_on(self): pass
    
    @abstractmethod
    def turn_off(self): pass
    
    @abstractmethod
    def set_temperature(self, temp): pass # For AC/Thermostat
    
    @abstractmethod
    def change_channel(self, channel): pass # For TV
    
    @abstractmethod
    def start_brewing(self): pass # For Coffee Maker
```

### The Problem
You are building a **Smart Lightbulb**. It just turns on and off.
But because you implemented `ISmartDevice`, you are forced to do this:

```python
class SmartBulb(ISmartDevice):
    def turn_on(self):
        print("Light is On")

    def turn_off(self):
        print("Light is Off")

    # Useless Garbage methods strictly required by the Interface
    def set_temperature(self, temp):
        raise Exception("I am a lightbulb, I have no temperature!")

    def change_channel(self, channel):
        raise Exception("I am not a TV!")

    def start_brewing(self):
        raise Exception("I cannot make coffee (yet)")
```

This is "Interface Pollution". The `SmartBulb` class is polluted with methods it doesn't need.

---

## 🛠️ The Refactor: Role-Based Interfaces

Split the "God Interface" into small, granular roles.

```python
# 1. The Basics
class ISwitchable(ABC):
    @abstractmethod
    def turn_on(self): pass
    
    @abstractmethod
    def turn_off(self): pass

# 2. Specific Roles
class IThermostat(ABC):
    @abstractmethod
    def set_temperature(self, temp): pass

class IMediaDevice(ABC):
    @abstractmethod
    def change_channel(self, channel): pass

class ICoffeeMaker(ABC):
    @abstractmethod
    def start_brewing(self): pass
```

### The Clean Implementation

Now, classes only sign the contracts they actually intend to fulfill.

```python
class SmartBulb(ISwitchable): # Only has on/off
    def turn_on(self): ...
    def turn_off(self): ...

class SmartTV(ISwitchable, IMediaDevice): # Has on/off AND channels
    def turn_on(self): ...
    def change_channel(self): ...

class SmartNestHub(ISwitchable, IThermostat, IMediaDevice): # A complex device
    def turn_on(self): ...
    def set_temperature(self): ...
    def change_channel(self): ... 
```

---

## 🏭 Industry Example: AWS SDK for JavaScript v3

In **AWS SDK v2**, you used to do:
`import AWS from 'aws-sdk';`
This imported support for S3, EC2, DynamoDB, SageMaker, and 200 other services. The package size was huge (Mb's).

In **AWS SDK v3**, they applied **ISP**:
`import { S3Client } from '@aws-sdk/client-s3';`
`import { DynamoDBClient } from '@aws-sdk/client-dynamodb';`

You only import the specific "Interface" you need. This reduces the bundle size appropriately. This is ISP applied at the package architecture level.
