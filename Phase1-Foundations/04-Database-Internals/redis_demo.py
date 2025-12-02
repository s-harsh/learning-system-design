import time
import heapq

# --- Mock Redis Implementation ---
class MockRedis:
    def __init__(self):
        self.store = {} # Key-Value Store
        self.sorted_sets = {} # For Leaderboards
        
    def get(self, key):
        """Simulate getting a value (Instant)"""
        return self.store.get(key)
    
    def set(self, key, value):
        """Simulate setting a value"""
        self.store[key] = value
        
    def zadd(self, key, member, score):
        """Simulate adding to a Sorted Set (Leaderboard)"""
        if key not in self.sorted_sets:
            self.sorted_sets[key] = {}
        self.sorted_sets[key][member] = score
        
    def zrevrange(self, key, start, end):
        """Simulate getting top players (Sorted by score desc)"""
        if key not in self.sorted_sets:
            return []
        # Sort by score descending
        sorted_items = sorted(self.sorted_sets[key].items(), key=lambda x: x[1], reverse=True)
        return sorted_items[start:end+1]

    def incr(self, key):
        """Simulate incrementing a counter"""
        self.store[key] = self.store.get(key, 0) + 1
        return self.store[key]

    def expire(self, key, seconds):
        """Simulate setting an expiration (Mock)"""
        print(f"[Redis] Key '{key}' will expire in {seconds}s")

# --- 1. Caching Demo ---

# Simulated Database (Slow)
def get_user_from_db(user_id):
    print(f"[Database] Fetching User {user_id}... (Simulating 2s delay)")
    time.sleep(2) # Simulate slow disk read
    return f"User_Data_{user_id}"

def caching_demo():
    print("\n--- 1. Caching Demo (Cache-Aside Pattern) ---")
    redis = MockRedis()
    user_id = 101
    
    # First Request: Cache Miss
    print("Request 1: Get User 101")
    start = time.time()
    
    # 1. Check Redis
    data = redis.get(user_id)
    if data:
        print("[App] Found in Cache!")
    else:
        print("[App] Not in Cache. Asking DB...")
        # 2. Fetch from DB
        data = get_user_from_db(user_id)
        # 3. Save to Redis
        redis.set(user_id, data)
        print("[App] Saved to Cache.")
        
    print(f"Time Taken: {time.time() - start:.2f}s")
    
    # Second Request: Cache Hit
    print("\nRequest 2: Get User 101 (Again)")
    start = time.time()
    
    # 1. Check Redis
    data = redis.get(user_id)
    if data:
        print(f"[App] Found in Cache! Data: {data}")
    
    print(f"Time Taken: {time.time() - start:.4f}s")
    print("Notice: The second request was instant!")

# --- 2. Leaderboard Demo ---

def leaderboard_demo():
    print("\n--- 2. Leaderboard Demo (Sorted Sets) ---")
    redis = MockRedis()
    key = "game_scores"
    
    print("[Game] Adding players...")
    redis.zadd(key, "Alice", 100)
    redis.zadd(key, "Bob", 500)
    redis.zadd(key, "Charlie", 300)
    redis.zadd(key, "Dave", 1200)
    
    print("[Game] Fetching Top 3 Players...")
    top_players = redis.zrevrange(key, 0, 2)
    
    for rank, (player, score) in enumerate(top_players, 1):
        print(f"#{rank}: {player} - {score} pts")
        
    print("Notice: Redis sorted them automatically!")

# --- 3. Rate Limiter Demo ---

def rate_limiter_demo():
    print("\n--- 3. Rate Limiter Demo (INCR + EXPIRE) ---")
    redis = MockRedis()
    user_ip = "192.168.1.1"
    limit = 5
    
    print(f"[API] Limit is {limit} requests per minute.")
    
    for i in range(1, 11):
        # 1. Increment the counter for this IP
        count = redis.incr(user_ip)
        
        # 2. If it's the first request, set expiration (window)
        if count == 1:
            redis.expire(user_ip, 60)
            
        # 3. Check limit
        if count > limit:
            print(f"Request {i}: 🛑 BLOCKED (Count: {count})")
        else:
            print(f"Request {i}: ✅ Allowed (Count: {count})")
        
        time.sleep(0.1)

if __name__ == "__main__":
    caching_demo()
    leaderboard_demo()
    rate_limiter_demo()
