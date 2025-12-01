import threading
import time

# Shared variable
bank_balance = 0
lock = threading.Lock()

def deposit_without_lock(amount, count):
    global bank_balance
    for _ in range(count):
        # Race condition happens here!
        # Read, Modify, Write is not atomic
        current = bank_balance
        time.sleep(0.00001) # Force context switch
        bank_balance = current + amount

def deposit_with_lock(amount, count):
    global bank_balance
    for _ in range(count):
        # Acquire lock before accessing shared resource
        with lock:
            current = bank_balance
            time.sleep(0.00001)
            bank_balance = current + amount

def run_demo():
    global bank_balance
    
    print("--- Demo 1: Race Condition (No Lock) ---")
    bank_balance = 0
    target_count = 100 
    t1 = threading.Thread(target=deposit_without_lock, args=(1, target_count))
    t2 = threading.Thread(target=deposit_without_lock, args=(1, target_count))
    
    start_time = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    
    print(f"Expected Balance: {target_count * 2}")
    print(f"Actual Balance:   {bank_balance}")
    print(f"Time Taken:       {end_time - start_time:.2f}s")
    print("Notice: The actual balance is likely LESS than expected due to race conditions.\n")

    print("--- Demo 2: Thread Safety (With Lock) ---")
    bank_balance = 0
    t1 = threading.Thread(target=deposit_with_lock, args=(1, target_count))
    t2 = threading.Thread(target=deposit_with_lock, args=(1, target_count))
    
    start_time = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    
    print(f"Expected Balance: {target_count * 2}")
    print(f"Actual Balance:   {bank_balance}")
    print(f"Time Taken:       {end_time - start_time:.2f}s")
    print("Notice: The balance is correct, but it took longer due to locking overhead.")

if __name__ == "__main__":
    run_demo()
