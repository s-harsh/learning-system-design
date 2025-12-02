import sqlite3
import threading
import time
import os

DB_NAME = "bank.db"

def setup_db():
    """Reset the database for the demo."""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, name TEXT, balance INTEGER)")
    cursor.execute("INSERT INTO accounts (id, name, balance) VALUES (1, 'Alice', 1000)")
    cursor.execute("INSERT INTO accounts (id, name, balance) VALUES (2, 'Bob', 1000)")
    conn.commit()
    conn.close()
    print("[Setup] Database reset. Alice: $1000, Bob: $1000")

def atomicity_demo():
    """Demonstrates Atomicity: If one part fails, EVERYTHING rolls back."""
    print("\n--- 1. Atomicity Demo (Rollback) ---")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        print("[Transaction] Step 1: Withdraw $500 from Alice...")
        cursor.execute("UPDATE accounts SET balance = balance - 500 WHERE id = 1")
        
        print("[Transaction] Step 2: Simulating a CRASH before depositing to Bob! 💥")
        raise Exception("Power Failure!")
        
        # This line will never run
        cursor.execute("UPDATE accounts SET balance = balance + 500 WHERE id = 2")
        conn.commit()
        
    except Exception as e:
        print(f"[Error] {e}")
        print("[System] Rolling back transaction...")
        conn.rollback()
        
    conn.close()
    
    # Verify balances
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    alice = cursor.execute("SELECT balance FROM accounts WHERE id=1").fetchone()[0]
    bob = cursor.execute("SELECT balance FROM accounts WHERE id=2").fetchone()[0]
    conn.close()
    
    print(f"[Result] Alice: ${alice}, Bob: ${bob}")
    if alice == 1000:
        print("✅ SUCCESS: Money was not lost. The withdrawal was undone.")
    else:
        print("❌ FAILURE: Money vanished!")

def locking_demo_thread_1():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    print("[Thread 1] Starting transaction (Exclusive Lock)...")
    cursor.execute("BEGIN EXCLUSIVE TRANSACTION")
    cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 1")
    print("[Thread 1] Alice's balance updated. Sleeping for 2 seconds (holding lock)...")
    time.sleep(2)
    conn.commit()
    print("[Thread 1] Commit done. Lock released.")
    conn.close()

def locking_demo_thread_2():
    time.sleep(0.5) # Wait for Thread 1 to start
    conn = sqlite3.connect(DB_NAME, timeout=5) # Wait up to 5s for lock
    cursor = conn.cursor()
    print("[Thread 2] Trying to read Alice's balance...")
    
    start = time.time()
    try:
        cursor.execute("SELECT balance FROM accounts WHERE id = 1")
        res = cursor.fetchone()
        print(f"[Thread 2] Read success! Balance: {res[0]}")
    except sqlite3.OperationalError:
        print("[Thread 2] ❌ Could not read! Database is locked.")
    
    print(f"[Thread 2] Waited {time.time() - start:.2f}s for the lock.")
    conn.close()

def isolation_demo():
    """Demonstrates Locking: Thread 2 cannot read while Thread 1 is writing."""
    print("\n--- 2. Isolation/Locking Demo ---")
    t1 = threading.Thread(target=locking_demo_thread_1)
    t2 = threading.Thread(target=locking_demo_thread_2)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    setup_db()
    atomicity_demo()
    isolation_demo()
