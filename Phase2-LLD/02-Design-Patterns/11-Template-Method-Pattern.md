# Template Method Pattern

> "Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure."

**Type:** Behavioral

## The Problem
You have two classes: `CSVDataMiner` and `PDFDataMiner`.
Both do essentially the same thing:
1.  Open File (Same for both).
2.  Extract Raw Data (Different).
3.  Parse Data (Different).
4.  Analyze Data (Same implementation).
5.  Send Report (Same).

**Code Duplication** occurs in steps 1, 4, and 5.

## The Solution
Create an abstract base class `DataMiner`.
Define a method `mine_data()` (The Template) that calls the steps in order.
Implement the common steps in the base class.
Force subclasses to implement the unique steps (`abstractmethod`).

## Real World Analogies
1.  **House Building**:
    - Foundation (Same).
    - Walls (Wood vs Brick - Varies).
    - Roof (Tile vs Metal - Varies).
    - Wiring (Same).
2.  **Cooking Pasta**:
    - Boil Water (Same).
    - Add Pasta (Same).
    - Add Sauce (Tomato vs Pesto vs Alfredo - Varies).

### Code Structure
```python
class DataMiner(ABC):
    def mine_data(self, path):
        # The Template Method
        self.open_file(path)
        data = self.extract_data() # Abstract
        analysis = self.analyze_data(data) # Hook or Common
        self.send_report(analysis)

    @abstractmethod
    def extract_data(self): pass
```
