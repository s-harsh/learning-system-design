"""
Day 10: Proxy Pattern Demo 🛡️

Scenario 1: Protection Proxy.
We have a 'Database' that only 'Admins' can delete from.
Scenario 2: Virtual/Caching Proxy.
We have a slow network call. We cache the result so we don't hit the network twice.
"""

from abc import ABC, abstractmethod
import time

# ==========================================
# Interface (Common for Real & Proxy)
# ==========================================
class DatabaseInterface(ABC):
    @abstractmethod
    def execute_query(self, query: str, user_role: str):
        pass

# ==========================================
# 1. The Real Object (The Sensitive Component)
# ==========================================
class RealDatabase(DatabaseInterface):
    def execute_query(self, query: str, user_role: str):
        # Simulate an expensive or dangerous operation
        print(f"⚡ [RealDB] Executing SQL: '{query}'...")
        time.sleep(0.5) # Simulate latency
        return f"Result for {query}"

# ==========================================
# 2. Protection Proxy (The Bouncer)
# ==========================================
class DatabaseProxy(DatabaseInterface):
    def __init__(self):
        self._real_db = RealDatabase()
        self._cache = {} # Simple in-memory cache

    def execute_query(self, query: str, user_role: str):
        print(f"\n🔍 [Proxy] Intercepting query: '{query}' from user: '{user_role}'")

        # 1. Security Check (Protection Proxy)
        if "DELETE" in query or "DROP" in query:
            if user_role != "ADMIN":
                print("🛑 [Proxy] ACCESS DENIED: Only Admins can DELETE/DROP.")
                return "403 Forbidden"
        
        # 2. Caching Check (Caching Proxy)
        # If we just ran this query, return the cached version.
        if query in self._cache:
            print("📦 [Proxy] Returning CACHED result. (Network call saved!)")
            return self._cache[query]

        # 3. Forward to Real Object
        print("✅ [Proxy] Access Granted. Forwarding to Real DB...")
        result = self._real_db.execute_query(query, user_role)
        
        # 4. Store in Cache
        self._cache[query] = result
        return result

# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("--- Proxy Pattern Demo ---\n")
    
    db = DatabaseProxy()

    # Case 1: Regular User trying to Read (Allowed)
    # First time: Hits Real DB
    print(db.execute_query("SELECT * FROM users", "USER")) 
    
    # Second time: Hits Cache (Fast)
    print(db.execute_query("SELECT * FROM users", "USER"))

    # Case 2: Regular User trying to Delete (blocked)
    print(db.execute_query("DELETE FROM users", "USER"))

    # Case 3: Admin trying to Delete (Allowed)
    print(db.execute_query("DELETE FROM users", "ADMIN"))
