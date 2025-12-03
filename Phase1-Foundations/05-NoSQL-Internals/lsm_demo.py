import time
import json
import os

class LSMTree:
    def __init__(self, memtable_limit=3):
        self.memtable = {}
        self.memtable_limit = memtable_limit
        self.sstables = []  # List of filenames
        self.wal_file = "wal.log"
        
        # Ensure clean state
        if os.path.exists(self.wal_file):
            os.remove(self.wal_file)

    def write(self, key, value):
        """Writes to MemTable and WAL."""
        print(f"📝 WRITE: {key} -> {value}")
        
        # 1. Append to Write-Ahead Log (WAL) for durability
        with open(self.wal_file, "a") as f:
            f.write(f"{key}:{value}\n")
        
        # 2. Write to In-Memory MemTable
        self.memtable[key] = value
        
        # 3. Check if MemTable is full
        if len(self.memtable) >= self.memtable_limit:
            self.flush_to_disk()

    def flush_to_disk(self):
        """Flushes MemTable to a new SSTable on disk."""
        filename = f"sstable_{int(time.time())}.json"
        print(f"⚠️  MEMTABLE FULL! Flushing to {filename}...")
        
        # Sort keys for efficient searching (SSTable property)
        sorted_data = dict(sorted(self.memtable.items()))
        
        with open(filename, "w") as f:
            json.dump(sorted_data, f)
            
        self.sstables.append(filename)
        self.memtable.clear()  # Reset MemTable
        
        # Clear WAL since data is now persisted in SSTable
        open(self.wal_file, 'w').close()
        print("✅ FLUSH COMPLETE. MemTable cleared.")

    def read(self, key):
        """Reads from MemTable first, then checks SSTables (Newest -> Oldest)."""
        print(f"🔍 READ: Searching for '{key}'...")
        
        # 1. Check MemTable (Fastest)
        if key in self.memtable:
            print(f"   Found in MemTable: {self.memtable[key]}")
            return self.memtable[key]
        
        # 2. Check SSTables (Newest to Oldest)
        for filename in reversed(self.sstables):
            try:
                with open(filename, "r") as f:
                    data = json.load(f)
                    if key in data:
                        print(f"   Found in {filename}: {data[key]}")
                        return data[key]
            except FileNotFoundError:
                continue
                
        print("   ❌ Key not found.")
        return None

# --- Simulation ---
if __name__ == "__main__":
    db = LSMTree(memtable_limit=3)
    
    print("--- 🚀 Starting LSM Tree Simulation ---")
    
    # 1. Fill MemTable
    db.write("user:1", "Alice")
    db.write("user:2", "Bob")
    db.write("user:3", "Charlie") # Triggers Flush 1
    
    time.sleep(1) # Ensure unique timestamp for filename
    
    # 2. Fill MemTable again
    db.write("user:4", "Dave")
    db.write("user:1", "Alice_Updated") # Update existing key
    db.write("user:5", "Eve") # Triggers Flush 2
    
    print("\n--- 🔍 Reading Data ---")
    db.read("user:2") # Should be in first SSTable
    db.read("user:1") # Should find "Alice_Updated" in second SSTable (shadows the old one)
    db.read("user:99") # Not found
    
    # Cleanup
    print("\n--- 🧹 Cleanup ---")
    if os.path.exists("wal.log"): os.remove("wal.log")
    for sstable in db.sstables:
        if os.path.exists(sstable):
            os.remove(sstable)
            print(f"Deleted {sstable}")
