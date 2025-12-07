import math

def create_h3_hierarchy_svg(filename="h3_aperture7_sketch.svg"):
    width = 600
    height = 600
    
    # White Background
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff;">'
    svg_content += f'<rect width="100%" height="100%" fill="#ffffff"/>'
    
    # Title
    svg_content += f'<text x="50" y="50" font-family="Segoe UI, sans-serif" font-size="24" fill="#333333" font-weight="bold">H3 Hierarchy: Aperture 7 🌸</text>'
    svg_content += f'<text x="50" y="80" font-family="Segoe UI, sans-serif" font-size="14" fill="#666666">1 Parent Hexagon ≈ 7 Child Hexagons</text>'

    center_x, center_y = 300, 320
    parent_radius = 200
    
    # Helper to draw hex
    def draw_hex(cx, cy, r, fill, stroke, stroke_width, opacity=1.0):
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30 # Pointy top
            angle_rad = math.radians(angle_deg)
            px = cx + r * math.cos(angle_rad)
            py = cy + r * math.sin(angle_rad)
            points.append(f"{px},{py}")
        return f'<polygon points="{" ".join(points)}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" opacity="{opacity}"/>'

    # 1. Draw Parent Hexagon (Big, Faint)
    svg_content += draw_hex(center_x, center_y, parent_radius, "#f3f4f6", "#9ca3af", 4)
    svg_content += f'<text x="{center_x-40}" y="{center_y-160}" font-family="Segoe UI, sans-serif" font-size="16" fill="#6b7280" font-weight="bold">Parent (Res N)</text>'

    # 2. Draw 7 Child Hexagons (Res N+1)
    # The math for Aperture 7 is roughly: Child Radius = Parent Radius / 2.6
    # And they are rotated. For this sketch, we'll place them geometrically to look "close enough".
    child_radius = parent_radius / 2.6
    
    # Center Child
    svg_content += draw_hex(center_x, center_y, child_radius, "#dbeafe", "#2563eb", 2)
    
    # 6 Neighbors
    # Distance to neighbor center is roughly 1.732 * child_radius
    dist = math.sqrt(3) * child_radius
    
    # H3 children are rotated ~19 degrees relative to parent. 
    # For the sketch, we just align them to fill the space visually.
    for i in range(6):
        angle_deg = 60 * i - 30 + 30 # Offset to fit in the corners
        angle_rad = math.radians(angle_deg)
        cx = center_x + dist * math.cos(angle_rad)
        cy = center_y + dist * math.sin(angle_rad)
        svg_content += draw_hex(cx, cy, child_radius, "#dbeafe", "#2563eb", 2)

    svg_content += f'<text x="{center_x-30}" y="{center_y+5}" font-family="Segoe UI, sans-serif" font-size="12" fill="#1e40af">Center</text>'
    
    # Annotation
    svg_content += f'<text x="50" y="550" font-family="Segoe UI, sans-serif" font-size="14" fill="#666666">Notice: Children don\'t fit perfectly! (The "Fractal" Edge)</text>'

    svg_content += '</svg>'
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    create_h3_hierarchy_svg()
