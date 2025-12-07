import math

def calculate_square_neighbors():
    """
    Demonstrates the 'Diagonal Problem' in Square Grids.
    Center is (0,0). Side length = 1.
    """
    print("\n--- 🟥 Square Grid Neighbor Distances ---")
    center = (0, 0)
    
    # 8 Neighbors for a square at (0,0)
    neighbors = [
        ("Right", (1, 0)),
        ("Top-Right", (1, 1)), # Diagonal
        ("Top", (0, 1)),
        ("Top-Left", (-1, 1)), # Diagonal
        ("Left", (-1, 0)),
        ("Bottom-Left", (-1, -1)), # Diagonal
        ("Bottom", (0, -1)),
        ("Bottom-Right", (1, -1)) # Diagonal
    ]
    
    for name, (x, y) in neighbors:
        distance = math.sqrt((x - center[0])**2 + (y - center[1])**2)
        print(f"Neighbor {name:12}: Distance = {distance:.2f}")
        
    print("👉 CONCLUSION: Diagonals are ~1.41x further away! Inconsistent.")

def calculate_hex_neighbors():
    """
    Demonstrates the 'Uniformity' in Hexagonal Grids.
    In a hex grid, the distance between the center of a hex
    and the center of ALL 6 neighbors is identical.
    """
    print("\n--- ⬡ Hexagonal Grid Neighbor Distances ---")
    
    # In a flat-top hex grid, distance to neighbors is constant.
    # Let's assume distance unit = 1.
    
    neighbors = ["Top", "Top-Right", "Bottom-Right", "Bottom", "Bottom-Left", "Top-Left"]
    
    for name in neighbors:
        distance = 1.00 # By geometric definition
        print(f"Neighbor {name:12}: Distance = {distance:.2f}")
        
    print("👉 CONCLUSION: All neighbors are exactly 1.00 unit away! Uniform.")

def simulate_surge_pricing():
    """
    Simulates smoothing a price surge from a center point to neighbors.
    """
    print("\n--- 💸 Surge Pricing Smoothing Simulation ---")
    center_price = 2.0 # 2x Surge
    
    # Square Grid Smoothing
    print("🟥 Square Smoothing:")
    # Diagonal neighbors are further, so they should logically get LESS surge influence?
    # Or if we treat them equally, we introduce error because they are physically further.
    diagonal_dist = 1.41
    side_dist = 1.0
    
    # Simple inverse distance weighting
    side_surge = center_price / side_dist
    diag_surge = center_price / diagonal_dist
    
    print(f"   Side Neighbor Surge: {side_surge:.2f}x")
    print(f"   Diag Neighbor Surge: {diag_surge:.2f}x (Big Drop-off!)")
    
    # Hex Grid Smoothing
    print("⬡ Hex Smoothing:")
    dist = 1.0
    hex_surge = center_price / dist
    print(f"   All 6 Neighbors  : {hex_surge:.2f}x (Perfectly Smooth)")

if __name__ == "__main__":
    calculate_square_neighbors()
    calculate_hex_neighbors()
    simulate_surge_pricing()
