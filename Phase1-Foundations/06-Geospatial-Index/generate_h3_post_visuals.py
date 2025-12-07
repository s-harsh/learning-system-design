import math
import random

# --- Helper: Uber Branding ---
def add_uber_header(svg_content, title, subtitle):
    # Black Header Bar
    svg_content += f'<rect x="0" y="0" width="100%" height="80" fill="#000000"/>'
    # "Uber" Text (Simple Sans-Serif representation)
    svg_content += f'<text x="30" y="50" font-family="Segoe UI, Arial, sans-serif" font-size="28" fill="#ffffff" font-weight="bold" letter-spacing="-1">Uber</text>'
    svg_content += f'<text x="100" y="50" font-family="Segoe UI, Arial, sans-serif" font-size="28" fill="#9ca3af" font-weight="normal">Engineering</text>'
    
    # Title & Subtitle below header
    svg_content += f'<text x="30" y="120" font-family="Segoe UI, sans-serif" font-size="24" fill="#000000" font-weight="bold">{title}</text>'
    svg_content += f'<text x="30" y="145" font-family="Segoe UI, sans-serif" font-size="14" fill="#555555">{subtitle}</text>'
    return svg_content

def create_h3_vs_s2_svg(filename="h3_vs_s2_sketch.svg"):
    width = 800
    height = 500
    
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff;">'
    svg_content += f'<rect width="100%" height="100%" fill="#f3f4f6"/>' # Light gray bg
    
    svg_content = add_uber_header(svg_content, "The Geometry Battle", "Why Squares Fail & Hexagons Win")

    # --- LEFT: SQUARE (S2) ---
    svg_content += f'<rect x="100" y="180" width="250" height="250" rx="10" fill="#ffffff" stroke="#e5e7eb" stroke-width="2"/>' # Card
    svg_content += f'<text x="120" y="220" font-family="Segoe UI, sans-serif" font-size="18" fill="#dc2626" font-weight="bold">Square (S2)</text>'
    cx, cy = 225, 320
    size = 50
    
    # Draw 3x3 Grid
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = cx + i * size
            y = cy + j * size
            fill = "#fee2e2" if i == 0 and j == 0 else "#ffffff"
            svg_content += f'<rect x="{x-size/2}" y="{y-size/2}" width="{size}" height="{size}" fill="{fill}" stroke="#dc2626" stroke-width="2"/>'

    # Draw Distance Arrows
    svg_content += f'<line x1="{cx}" y1="{cy}" x2="{cx+size}" y2="{cy}" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>'
    svg_content += f'<text x="{cx+10}" y="{cy-10}" font-family="monospace" font-size="10">1.0</text>'
    svg_content += f'<line x1="{cx}" y1="{cy}" x2="{cx+size}" y2="{cy-size}" stroke="#dc2626" stroke-width="3" marker-end="url(#arrow_red)"/>'
    svg_content += f'<text x="{cx+30}" y="{cy-30}" font-family="monospace" font-size="10" fill="#dc2626">1.41 ❌</text>'


    # --- RIGHT: HEXAGON (H3) ---
    svg_content += f'<rect x="450" y="180" width="250" height="250" rx="10" fill="#ffffff" stroke="#e5e7eb" stroke-width="2"/>' # Card
    svg_content += f'<text x="470" y="220" font-family="Segoe UI, sans-serif" font-size="18" fill="#16a34a" font-weight="bold">Hexagon (H3)</text>'
    hx, hy = 575, 320
    r = 35
    
    def draw_hex(cx, cy, radius, fill, stroke):
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.radians(angle_deg)
            px = cx + radius * math.cos(angle_rad)
            py = cy + radius * math.sin(angle_rad)
            points.append(f"{px},{py}")
        return f'<polygon points="{" ".join(points)}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'

    # Draw Center Hex
    svg_content += draw_hex(hx, hy, r, "#dcfce7", "#16a34a")
    
    # Draw 6 Neighbors
    dist = math.sqrt(3) * r
    for i in range(6):
        angle_deg = 60 * i - 30 + 30
        angle_rad = math.radians(angle_deg)
        nx = hx + dist * math.cos(angle_rad)
        ny = hy + dist * math.sin(angle_rad)
        svg_content += draw_hex(nx, ny, r, "#ffffff", "#16a34a")
        
        if i == 0:
            svg_content += f'<line x1="{hx}" y1="{hy}" x2="{nx}" y2="{ny}" stroke="#16a34a" stroke-width="3" marker-end="url(#arrow_green)"/>'
            svg_content += f'<text x="{hx+20}" y="{hy-10}" font-family="monospace" font-size="10" fill="#16a34a">1.0 ✅</text>'

    # Definitions
    svg_content += '<defs>'
    svg_content += '<marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#333" /></marker>'
    svg_content += '<marker id="arrow_red" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#dc2626" /></marker>'
    svg_content += '<marker id="arrow_green" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#16a34a" /></marker>'
    svg_content += '</defs>'

    svg_content += '</svg>'
    with open(filename, "w", encoding="utf-8") as f: f.write(svg_content)
    print(f"Generated {filename}")

def create_surge_heatmap_svg(filename="h3_surge_heatmap_sketch.svg"):
    width = 800
    height = 600
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#e5e7eb;">'
    
    # --- Map Background (Roads) ---
    svg_content += f'<rect width="100%" height="100%" fill="#f3f4f6"/>'
    # Random Roads
    for i in range(0, width, 100):
        svg_content += f'<line x1="{i}" y1="0" x2="{i}" y2="{height}" stroke="#e5e7eb" stroke-width="8"/>'
        svg_content += f'<line x1="{i}" y1="0" x2="{i}" y2="{height}" stroke="#ffffff" stroke-width="6"/>'
    for i in range(0, height, 100):
        svg_content += f'<line x1="0" y1="{i}" x2="{width}" y2="{i}" stroke="#e5e7eb" stroke-width="8"/>'
        svg_content += f'<line x1="0" y1="{i}" x2="{width}" y2="{i}" stroke="#ffffff" stroke-width="6"/>'

    svg_content = add_uber_header(svg_content, "Surge Pricing Heatmap", "Real-time Demand Smoothing")
    
    # --- The Heatmap ---
    start_x, start_y = 100, 180
    r = 30
    dist_x = math.sqrt(3) * r
    dist_y = 1.5 * r
    
    def draw_hex(cx, cy, radius, fill, opacity):
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.radians(angle_deg)
            px = cx + radius * math.cos(angle_rad)
            py = cy + radius * math.sin(angle_rad)
            points.append(f"{px},{py}")
        return f'<polygon points="{" ".join(points)}" fill="{fill}" stroke="#ffffff" stroke-width="1" opacity="{opacity}"/>'

    center_col, center_row = 8, 6
    
    for row in range(12):
        for col in range(15):
            cx = start_x + col * dist_x
            cy = start_y + row * dist_y
            if row % 2 == 1: cx += dist_x / 2
            
            dist = math.sqrt((row - center_row)**2 + (col - center_col)**2)
            
            # Uber Surge Colors (Purple/Blue gradient usually, but let's stick to Red/Orange for heat)
            # Actually, Uber uses a lot of Purple/Black. Let's try a "Night Mode" surge.
            if dist < 2: 
                fill = "#9333ea" # Purple (High)
                opacity = 0.9
                label = "2.5x"
            elif dist < 4: 
                fill = "#c084fc" # Light Purple
                opacity = 0.7
                label = ""
            elif dist < 6: 
                fill = "#e9d5ff" # Very Light Purple
                opacity = 0.5
                label = ""
            else: 
                fill = "#ffffff"
                opacity = 0.0
                label = ""
            
            if opacity > 0:
                svg_content += draw_hex(cx, cy, r, fill, opacity)
                if label and random.random() > 0.5: # Randomly label some
                    svg_content += f'<text x="{cx-10}" y="{cy+5}" font-family="Segoe UI" font-size="12" fill="#ffffff" font-weight="bold">{label}</text>'

    # --- UI Overlay (Phone Frame Look) ---
    svg_content += f'<rect x="600" y="500" width="180" height="80" rx="10" fill="#000000" opacity="0.9"/>'
    svg_content += f'<text x="620" y="530" font-family="Segoe UI" font-size="14" fill="#9ca3af">Current Surge</text>'
    svg_content += f'<text x="620" y="560" font-family="Segoe UI" font-size="24" fill="#ffffff" font-weight="bold">2.5x ⚡</text>'

    svg_content += '</svg>'
    with open(filename, "w", encoding="utf-8") as f: f.write(svg_content)
    print(f"Generated {filename}")

def create_soccer_ball_svg(filename="h3_soccer_ball_sketch.svg"):
    width = 600
    height = 600
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff;">'
    svg_content += f'<rect width="100%" height="100%" fill="#ffffff"/>'
    
    svg_content = add_uber_header(svg_content, "The Secret Projection", "Earth is an Icosahedron (20 Faces)")

    cx, cy = 300, 350
    r = 160
    
    # Draw Icosahedron
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30
        angle_rad = math.radians(angle_deg)
        px = cx + r * math.cos(angle_rad)
        py = cy + r * math.sin(angle_rad)
        points.append((px, py))
    
    # Faces (Uber Blue)
    svg_content += f'<polygon points="{points[0][0]},{points[0][1]} {points[2][0]},{points[2][1]} {points[4][0]},{points[4][1]}" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
    svg_content += f'<polygon points="{points[1][0]},{points[1][1]} {points[3][0]},{points[3][1]} {points[5][0]},{points[5][1]}" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
    
    for i in range(6):
        p1 = points[i]
        p2 = points[(i+1)%6]
        svg_content += f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="#000000" stroke-width="3"/>'
        svg_content += f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{cx}" y2="{cy}" stroke="#000000" stroke-width="1" stroke-dasharray="5,5"/>'

    # The Pentagon Label
    svg_content += f'<circle cx="{points[0][0]}" cy="{points[0][1]}" r="18" fill="#000000" stroke="#ffffff" stroke-width="2"/>'
    svg_content += f'<text x="{points[0][0]-5}" y="{points[0][1]+5}" font-family="bold" font-size="14" fill="#ffffff">P</text>'
    
    svg_content += f'<text x="50" y="550" font-family="Segoe UI, sans-serif" font-size="14" fill="#000000">"P" = The 12 Hidden Pentagons (Vertices)</text>'

    svg_content += '</svg>'
    with open(filename, "w", encoding="utf-8") as f: f.write(svg_content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    create_h3_vs_s2_svg()
    create_surge_heatmap_svg()
    create_soccer_ball_svg()
