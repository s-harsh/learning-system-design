# Day 11: I Designed a Parking Lot (It's Harder Than It Looks) 🚗

"It's just a parking lot. How hard can it be?"

That's what I thought until I tried to design the **Low-Level Design (LLD)** for one today.
It turns out, a Parking Lot is the perfect storm of Object-Oriented Programming and Concurrency.

### 1. The OOP Trap 🕸️
The rookie mistake is to put everything in one class.
*   `ParkingLot.calculatePrice()` ❌
*   `ParkingLot.parkVehicle()` ❌

**The Pro Move (SOLID Principles)**:
*   **Strategy Pattern**: Move pricing logic to a separate `PricingStrategy` class. Why? So you can swap "Hourly Pricing" for "Dynamic Pricing" (Surge) without touching the main code. (Open/Closed Principle).
*   **Polymorphism**: `Vehicle` should be the parent. `Car`, `Bike`, `Truck` inherit from it. The slot doesn't care if it's a Ferrari or a Toyota, it just cares it's a `Vehicle`.

### 2. The Concurrency Nightmare 💥
What happens when 2 cars enter Gate A and Gate B at the exact same millisecond?
They both query the DB: "Is Spot #101 free?"
DB says: "Yes."
Both cars enter. One crash. 💥

**The Solution**:
Optimistic Locking in SQL.
`UPDATE spots SET occupied=true WHERE id=101 AND occupied=false;`
Only one query will succeed. The other will be told "Sorry, try again".

### The Takeaway
System Design isn't about drawing boxes. It's about predicting where things break.
*   Code breaks when requirements change (Use Patterns).
*   Data breaks when traffic spikes (Use Locking).

*Grab the full detailed breakdown and diagram in the repo 👇*

#SystemDesign #LLD #OOP #Programming #SoftwareEngineering #Learning #DesignPatterns
