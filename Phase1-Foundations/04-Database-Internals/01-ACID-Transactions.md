# Lesson 4.1: Database Internals - ACID & Transactions

When you send money to a friend, two things happen:
1.  Money leaves your account.
2.  Money enters their account.

If the power goes out after step 1 but before step 2, the money vanishes. **Transactions** prevent this.

---

## 1. The ACID Properties
Every reliable database (Postgres, MySQL, Oracle) guarantees these four properties.

### ⚛️ A - Atomicity ("All or Nothing")
*   **Definition**: A transaction is treated as a single unit. Either **all** steps succeed, or **none** of them do.
*   **Mechanism**: **Write-Ahead Logging (WAL)**. Before writing to the actual database file, the DB writes the action to a log. If it crashes, it reads the log to "undo" (rollback) or "redo" (commit) pending changes.
*   **Real-World Failure**: **Flexcoin (2014)**. A Bitcoin bank shut down because hackers exploited a race condition. They sent thousands of withdrawal requests simultaneously. The database didn't treat them atomically, allowing the same coins to be withdrawn multiple times (Double Spend).

### 🛡️ C - Consistency ("Follow the Rules")
*   **Definition**: The database must move from one valid state to another. It must obey all constraints (e.g., "Balance cannot be negative", "User ID must exist").
*   **Mechanism**: Constraints (Foreign Keys, Unique Keys, Checks).
*   **Example**: If you try to transfer $100 but only have $50, the DB rejects the transaction to maintain the "No Negative Balance" rule.

### 🔒 I - Isolation ("Don't Interfere")
*   **Definition**: Multiple transactions running at the same time should not affect each other.
*   **Mechanism**: **Locks** (Row-level, Table-level) and **MVCC** (Multi-Version Concurrency Control).
*   **The Problem**: If User A reads a row while User B is writing to it, what does User A see? The old value? The new value? Or a mix?

### 💾 D - Durability ("Written in Stone")
*   **Definition**: Once a transaction is "Committed", it stays saved even if the server catches fire immediately after.
*   **Mechanism**: **fsync()**. The DB forces the OS to flush data from RAM to the physical Hard Disk/SSD before saying "Success".

---

## 2. Isolation Levels (The "Danger Zone")

Why do we have different levels? Because **Safety kills Speed**.
The more you isolate transactions, the slower your database gets. You choose the level based on how much "weirdness" your app can tolerate.

### Level 1: Read Uncommitted (The "Dirty" Level)
*   **The Logic**: "I don't care if the data is real, just give it to me fast."
*   **The Problem (Dirty Read)**:
    1.  Transaction A updates Alice's balance from $100 to $200 (but hasn't committed yet).
    2.  Transaction B reads Alice's balance as $200.
    3.  Transaction A crashes and rolls back to $100.
    4.  **Result**: Transaction B is working with $200, which **never existed**.
*   **Why use it?**: almost never. Maybe for rough analytics where exact numbers don't matter.

### Level 2: Read Committed (The Default)
*   **The Logic**: "Only show me data that is definitely saved."
*   **The Fix**: You cannot read uncommitted changes.
*   **The Problem (Non-Repeatable Read)**:
    1.  Transaction A reads Alice's balance: $100.
    2.  Transaction B updates Alice's balance to $200 and commits.
    3.  Transaction A reads Alice's balance again: $200.
    4.  **Result**: Transaction A sees two different values for the same row in the same transaction. This breaks logic like "If balance is $100, do X".
*   **Why use it?**: It's the default in Postgres/Oracle because it's a good balance of speed and sanity.

### Level 3: Repeatable Read (The "Snapshot")
*   **The Logic**: "If I read it once, it shouldn't change until I'm done."
*   **The Fix**: The DB takes a "snapshot" of the row when you first read it. Even if someone else changes it, you see the old version.
*   **The Problem (Phantom Read)**:
    1.  Transaction A runs `SELECT count(*) FROM users WHERE age > 18`. Result: 10.
    2.  Transaction B inserts a *new* user with age 20.
    3.  Transaction A runs the same query. Result: 11.
    4.  **Result**: The rows didn't change, but a *new* "phantom" row appeared.
*   **Why use it?**: Financial apps where consistent reports are critical.

### Level 4: Serializable (The "Single File Line")
*   **The Logic**: "Pretend there is no multitasking."
*   **The Fix**: The DB locks everything or kills transactions that conflict.
*   **The Cost**: Extremely slow. High chance of "Serialization Failure" errors (where the DB tells you to retry).
*   **Why use it?**: When data integrity is more important than performance (e.g., preventing double-booking a seat).

| Level | Dirty Read? | Non-Repeatable Read? | Phantom Read? | Speed |
| :--- | :---: | :---: | :---: | :--- |
| **Read Uncommitted** | ✅ Yes | ✅ Yes | ✅ Yes | 🚀 |
| **Read Committed** | ❌ No | ✅ Yes | ✅ Yes | ⚡ |
| **Repeatable Read** | ❌ No | ❌ No | ✅ Yes | 🐢 |
| **Serializable** | ❌ No | ❌ No | ❌ No | 🐌 |

---

## 3. Locking: Optimistic vs Pessimistic

### 😠 Pessimistic Locking ("Trust No One")
*   **Logic**: "I think someone will mess with this data, so I'll lock it first."
*   **Flow**: `SELECT ... FOR UPDATE`. The DB locks the row. No one else can read/write it until you finish.
*   **Use Case**: High-conflict data. Ticketmaster seat booking (only 1 person can grab Seat A1).

### 😊 Optimistic Locking ("Hope for the Best")
*   **Logic**: "I don't think anyone will touch this. I'll check just before I save."
*   **Flow**: You read the row and note its `version_number` (e.g., v1). When you save, you check `WHERE version = 1`. If the version is now v2, your save fails, and you retry.
*   **Use Case**: Low-conflict data. Editing a Google Doc (mostly just you), or updating a user profile.

---

## 4. Practical Exercise
We will write a Python script using `sqlite3` to simulate:
1.  **Atomicity**: A failed bank transfer rolling back.
2.  **Isolation**: One thread locking a row so another has to wait.

---

## 5. Real World Case Study: The BookMyShow Problem 🎟️

You asked: *"If I select a seat, is it blocked until I pay?"*

This is a classic **Concurrency Problem**. If 10,000 people try to book the last Avengers ticket at the same second, how do we ensure only 1 gets it?

### The Wrong Way (Database Locking)
If you used **Pessimistic Locking** (`SELECT FOR UPDATE`) the moment a user clicked a seat:
1.  User A clicks Seat 1.
2.  DB locks the row.
3.  User A takes 10 minutes to find their credit card.
4.  **Result**: The database connection is "held" open for 10 minutes. If 1000 people do this, the database runs out of connections and crashes.

### The Right Way (2-Step Locking)

#### Step 1: The "Soft Lock" (Redis / Cache)
When you click a seat, the system doesn't touch the main database yet.
1.  It sends a request to a fast cache (like **Redis**).
2.  It sets a key: `seat_A1_lock = User_123` with a **TTL (Time To Live)** of 10 minutes.
3.  If User B clicks the seat, the system checks Redis. "Oh, `seat_A1_lock` exists. Sorry, it's taken."
4.  **User Experience**: You see the seat turn grey.

#### Step 2: The "Hard Lock" (Database Transaction)
When you actually click **"Pay Now"**:
1.  The system starts a **Database Transaction**.
2.  It checks: "Is this seat still available?" (Double check).
3.  It updates: `UPDATE seats SET status = 'BOOKED' WHERE id = 'A1'`.
4.  It commits.

### Summary
*   **Selection Phase**: Uses **Redis** (Fast, Temporary, expires automatically).
*   **Payment Phase**: Uses **ACID Database Transaction** (Reliable, Permanent).
