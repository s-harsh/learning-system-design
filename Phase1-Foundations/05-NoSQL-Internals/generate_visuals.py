import random
import math

def create_random_io_svg(filename="random_io_sketch.svg"):
    width = 800
    height = 500
    
    # White Background (Paper/Whiteboard look)
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff;">'
    svg_content += f'<rect width="100%" height="100%" fill="#ffffff"/>'
    
    # Title
    svg_content += f'<text x="50" y="50" font-family="Segoe UI, sans-serif" font-size="28" fill="#333333" font-weight="bold">The Problem: Random I/O (B-Trees)</text>'
    
    # Draw Disk Platter (Big Circle)
    center_x, center_y = 400, 280
    radius = 180
    svg_content += f'<circle cx="{center_x}" cy="{center_y}" r="{radius}" fill="#f8f9fa" stroke="#333333" stroke-width="3"/>'
    svg_content += f'<circle cx="{center_x}" cy="{center_y}" r="20" fill="#333333" stroke="none"/>' # Spindle
    
    # Draw Tracks (Concentric Circles)
    for r in [60, 100, 140]:
        svg_content += f'<circle cx="{center_x}" cy="{center_y}" r="{r}" fill="none" stroke="#e9ecef" stroke-width="2" stroke-dasharray="5,5"/>'

    # Draw Data Blocks (Scattered Red Squares)
    targets = []
    for i in range(8):
        angle = random.uniform(0, 2 * math.pi)
        r = random.choice([60, 100, 140])
        x = center_x + r * math.cos(angle)
        y = center_y + r * math.sin(angle)
        targets.append((x, y))
        svg_content += f'<rect x="{x-10}" y="{y-10}" width="20" height="20" fill="#ffcccc" stroke="#dc2626" stroke-width="2"/>'
        svg_content += f'<text x="{x-5}" y="{y+5}" font-family="monospace" font-size="10" fill="#dc2626">{i+1}</text>'

    # Draw Seek Path (Zig-Zag Arrows)
    path_d = f"M {targets[0][0]} {targets[0][1]}"
    for i in range(1, len(targets)):
        path_d += f" L {targets[i][0]} {targets[i][1]}"
    
    svg_content += f'<path d="{path_d}" fill="none" stroke="#dc2626" stroke-width="3" stroke-dasharray="8,4"/>'
    
    # Label
    svg_content += f'<text x="50" y="480" font-family="Segoe UI, sans-serif" font-size="16" fill="#666666">Disk Head jumps randomly to find blocks 1 -> 8. Slow!</text>'

    svg_content += '</svg>'
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {filename}")

def create_lsm_svg(filename="lsm_sequential_sketch.svg"):
    width = 800
    height = 500
    
    # White Background
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff;">'
    svg_content += f'<rect width="100%" height="100%" fill="#ffffff"/>'
    
    # Title
    svg_content += f'<text x="50" y="50" font-family="Segoe UI, sans-serif" font-size="28" fill="#333333" font-weight="bold">The Solution: Sequential I/O (LSM Trees)</text>'

    # 1. MemTable (RAM Box)
    svg_content += f'<rect x="50" y="150" width="200" height="250" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="3"/>'
    svg_content += f'<text x="100" y="190" font-family="Segoe UI, sans-serif" font-size="20" fill="#1e40af" font-weight="bold">MemTable</text>'
    svg_content += f'<text x="120" y="215" font-family="Segoe UI, sans-serif" font-size="14" fill="#64748b">(RAM)</text>'
    
    # List items in MemTable
    for i in range(5):
        y = 250 + (i * 35)
        svg_content += f'<rect x="70" y="{y}" width="160" height="25" rx="2" fill="#dbeafe" stroke="#93c5fd" stroke-width="1"/>'
        svg_content += f'<text x="80" y="{y+17}" font-family="monospace" font-size="12" fill="#1e3a8a">KEY_{i}: VAL_{i}</text>'

    # 2. Big Arrow (Flush)
    svg_content += f'<path d="M 270 275 L 350 275" stroke="#333333" stroke-width="3" marker-end="url(#arrow)"/>'
    svg_content += f'<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#333333" /></marker></defs>'
    svg_content += f'<text x="280" y="265" font-family="Segoe UI, sans-serif" font-size="14" fill="#666666" font-weight="bold">FLUSH</text>'

    # 3. SSTables (Disk Stack)
    start_x = 370
    for i in range(3):
        x = start_x + (i * 140)
        # File Icon Shape
        svg_content += f'<rect x="{x}" y="150" width="120" height="250" rx="2" fill="#f0fdf4" stroke="#16a34a" stroke-width="3"/>'
        svg_content += f'<text x="{x+20}" y="190" font-family="Segoe UI, sans-serif" font-size="16" fill="#15803d" font-weight="bold">SSTable {i+1}</text>'
        
        # Lines representing data
        for j in range(6):
            y = 230 + (j * 30)
            svg_content += f'<line x1="{x+15}" y1="{y}" x2="{x+105}" y2="{y}" stroke="#86efac" stroke-width="4"/>'
            
    # Label
    svg_content += f'<text x="50" y="480" font-family="Segoe UI, sans-serif" font-size="16" fill="#666666">Data is appended sequentially. No jumping. Fast!</text>'

    svg_content += '</svg>'
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {filename}")

def create_compaction_svg(filename="lsm_compaction_sketch.svg"):
    width = 800
    height = 500
    
    # White Background
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff;">'
    svg_content += f'<rect width="100%" height="100%" fill="#ffffff"/>'
    
    # Title
    svg_content += f'<text x="50" y="50" font-family="Segoe UI, sans-serif" font-size="28" fill="#333333" font-weight="bold">The Cleanup: Compaction 🧹</text>'
    svg_content += f'<text x="50" y="80" font-family="Segoe UI, sans-serif" font-size="14" fill="#666666">Merging small files into big ones & removing deleted data.</text>'

    # --- Level 0 (Before) ---
    svg_content += f'<text x="100" y="140" font-family="Segoe UI, sans-serif" font-size="16" fill="#333333" font-weight="bold">Level 0 (Fragmented)</text>'
    
    # Draw 4 small SSTables
    data_labels = ["A:1", "B:2", "A:9 (Upd)", "Del:B"]
    colors = ["#dbeafe", "#dbeafe", "#dcfce7", "#fee2e2"] # Blue, Blue, Green (New), Red (Delete)
    
    for i in range(4):
        x = 50 + (i * 110)
        y = 160
        # File Box
        svg_content += f'<rect x="{x}" y="{y}" width="90" height="120" rx="2" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>'
        # Data Block
        svg_content += f'<rect x="{x+10}" y="{y+40}" width="70" height="30" rx="2" fill="{colors[i]}" stroke="none"/>'
        svg_content += f'<text x="{x+15}" y="{y+60}" font-family="monospace" font-size="12" fill="#333333">{data_labels[i]}</text>'
        svg_content += f'<text x="{x+25}" y="{y+110}" font-family="Segoe UI, sans-serif" font-size="10" fill="#94a3b8">File {i+1}</text>'

    # --- Merge Arrow ---
    svg_content += f'<path d="M 400 300 L 400 360" stroke="#333333" stroke-width="3" marker-end="url(#arrow)"/>'
    svg_content += f'<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#333333" /></marker></defs>'
    svg_content += f'<text x="410" y="340" font-family="Segoe UI, sans-serif" font-size="14" fill="#666666" font-style="italic">Merge & Sort</text>'

    # --- Level 1 (After) ---
    svg_content += f'<text x="100" y="400" font-family="Segoe UI, sans-serif" font-size="16" fill="#333333" font-weight="bold">Level 1 (Compacted)</text>'
    
    # Draw 1 Big SSTable
    # File Box
    svg_content += f'<rect x="250" y="380" width="300" height="100" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="3"/>'
    
    # Data Blocks (Merged)
    # A:9 (Kept), B (Deleted - Gone)
    final_data = ["A:9 (Latest)", "C:5 (Existing)"]
    for i in range(2):
        x = 270 + (i * 140)
        svg_content += f'<rect x="{x}" y="410" width="120" height="40" rx="2" fill="#bbf7d0" stroke="none"/>'
        svg_content += f'<text x="{x+15}" y="435" font-family="monospace" font-size="14" fill="#166534">{final_data[i]}</text>'

    # Annotation
    svg_content += f'<text x="560" y="430" font-family="Segoe UI, sans-serif" font-size="12" fill="#dc2626">"B" was removed!</text>'
    svg_content += f'<text x="560" y="450" font-family="Segoe UI, sans-serif" font-size="12" fill="#166534">"A" updated!</text>'

    svg_content += '</svg>'
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {filename}")

def create_discord_partitioning_svg(filename="discord_partitioning_sketch.svg"):
    width = 800
    height = 600
    
    # White Background
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff;">'
    svg_content += f'<rect width="100%" height="100%" fill="#ffffff"/>'
    
    # Title
    svg_content += f'<text x="50" y="50" font-family="Segoe UI, sans-serif" font-size="28" fill="#333333" font-weight="bold">Discord\'s Secret: Time Buckets ⏳</text>'
    svg_content += f'<text x="50" y="80" font-family="Segoe UI, sans-serif" font-size="14" fill="#666666">How to handle 1 Million users in one channel without crashing.</text>'

    # --- SCENARIO 1: The Problem (Hot Partition) ---
    svg_content += f'<text x="100" y="140" font-family="Segoe UI, sans-serif" font-size="18" fill="#dc2626" font-weight="bold">The Problem: Hot Partition</text>'
    
    # Server Box (Overloaded)
    svg_content += f'<rect x="100" y="160" width="120" height="140" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="3"/>'
    svg_content += f'<text x="125" y="190" font-family="Segoe UI, sans-serif" font-size="14" fill="#991b1b" font-weight="bold">Node A</text>'
    
    # Incoming Messages (Crowded)
    for i in range(10):
        y = 210 + (i * 8)
        svg_content += f'<rect x="110" y="{y}" width="100" height="4" fill="#ef4444"/>'
    
    svg_content += f'<text x="240" y="230" font-family="Segoe UI, sans-serif" font-size="14" fill="#dc2626">"General Chat" (All Messages)</text>'
    svg_content += f'<text x="240" y="250" font-family="Segoe UI, sans-serif" font-size="12" fill="#666666">One server takes 100% load.</text>'


    # --- SCENARIO 2: The Solution (Time Buckets) ---
    svg_content += f'<text x="100" y="360" font-family="Segoe UI, sans-serif" font-size="18" fill="#16a34a" font-weight="bold">The Solution: Time Buckets</text>'
    
    # 3 Servers (Distributed)
    nodes = ["Node A", "Node B", "Node C"]
    times = ["12:00 - 12:10", "12:10 - 12:20", "12:20 - 12:30"]
    colors = ["#dbeafe", "#dcfce7", "#f3e8ff"] # Blue, Green, Purple
    strokes = ["#2563eb", "#16a34a", "#9333ea"]
    
    for i in range(3):
        x = 100 + (i * 200)
        y = 400
        # Server Box
        svg_content += f'<rect x="{x}" y="{y}" width="140" height="120" rx="4" fill="{colors[i]}" stroke="{strokes[i]}" stroke-width="3"/>'
        svg_content += f'<text x="{x+40}" y="{y+30}" font-family="Segoe UI, sans-serif" font-size="14" fill="{strokes[i]}" font-weight="bold">{nodes[i]}</text>'
        
        # Bucket Label
        svg_content += f'<rect x="{x+10}" y="{y+50}" width="120" height="30" rx="2" fill="#ffffff" stroke="{strokes[i]}" stroke-width="1"/>'
        svg_content += f'<text x="{x+20}" y="{y+70}" font-family="monospace" font-size="12" fill="#333333">{times[i]}</text>'
        
        # Messages (Distributed)
        for j in range(3):
            msg_y = y + 90 + (j * 8)
            svg_content += f'<rect x="{x+20}" y="{msg_y}" width="100" height="4" fill="{strokes[i]}"/>'

    svg_content += f'<text x="100" y="560" font-family="Segoe UI, sans-serif" font-size="14" fill="#666666">Load is spread across 3 servers based on TIME. No single server dies!</text>'

    svg_content += '</svg>'
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    create_random_io_svg()
    create_lsm_svg()
    create_compaction_svg()
    create_discord_partitioning_svg()
