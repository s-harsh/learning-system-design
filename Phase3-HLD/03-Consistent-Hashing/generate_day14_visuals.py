import os
import math

def create_svg_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename}")

def main():
    base_dir = r"c:\Harsh\Learning\learning-system-design\Phase3-HLD\03-Consistent-Hashing"
    os.makedirs(base_dir, exist_ok=True)

    # Style constants
    bg_color = "#121212"
    text_color = "#e0e0e0"
    accent_server = "#61dafb" # Blue
    accent_user = "#ffeb3b"   # Yellow
    ring_color = "#333"
    font_family = "Consolas, monospace"
    
    # Ring Geometry
    cx, cy = 400, 300
    radius = 180

    svg_content = f"""<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        <style>
            text {{ font-family: {font_family}; fill: {text_color}; }}
            .title {{ font-size: 24px; font-weight: bold; fill: {accent_server}; }}
            .ring {{ fill: none; stroke: {ring_color}; stroke-width: 10; }}
            .server-node {{ fill: {accent_server}; stroke: #fff; stroke-width: 2; }}
            .user-node {{ fill: {accent_user}; stroke: #fff; stroke-width: 1; }}
            .label {{ font-size: 14px; font-weight: bold; }}
            .arrow {{ stroke: #fff; stroke-width: 1; stroke-dasharray: 4; marker-end: url(#arrow); }}
        </style>
        
        <text x="400" y="50" text-anchor="middle" class="title">Consistent Hashing Ring 🍩</text>

        <!-- The Ring -->
        <circle cx="{cx}" cy="{cy}" r="{radius}" class="ring" />

        <!-- Server A at 0 degrees (Top) -->
        <circle cx="{cx}" cy="{cy - radius}" r="15" class="server-node" />
        <text x="{cx}" y="{cy - radius - 25}" text-anchor="middle" class="label" fill="{accent_server}">Server A (0)</text>

        <!-- Server B at 120 degrees -->
        <circle cx="{cx + radius * 0.866}" cy="{cy + radius * 0.5}" r="15" class="server-node" />
        <text x="{cx + radius * 0.866 + 20}" y="{cy + radius * 0.5}" text-anchor="start" class="label" fill="{accent_server}">Server B (120)</text>

        <!-- Server C at 240 degrees -->
        <circle cx="{cx - radius * 0.866}" cy="{cy + radius * 0.5}" r="15" class="server-node" />
        <text x="{cx - radius * 0.866 - 20}" y="{cy + radius * 0.5}" text-anchor="end" class="label" fill="{accent_server}">Server C (240)</text>
        
        <!-- User 1 (Mapped to Server B) -->
        <!-- Placed at 60 degrees -->
        <circle cx="{cx + radius * 0.866 * 0.5}" cy="{cy - radius * 0.5 * 0.866 + radius * 0.1}" r="8" class="user-node" />
        <text x="{cx + radius * 0.5 + 20}" y="{cy - radius * 0.7}" class="label" fill="{accent_user}">Key: John (60)</text>
        <!-- Arrow Clockwise to Server B -->
        <path d="M {cx + radius * 0.6} {cy - radius * 0.5} Q {cx + radius * 0.9} {cy} {cx + radius * 0.866} {cy + radius * 0.4}" fill="none" class="arrow" />


        <!-- VNode Explanation Box -->
        <rect x="50" y="480" width="700" height="100" fill="#222" rx="10" />
        <text x="70" y="510" font-weight="bold" fill="#fff">Handling HotSpots (Virtual Nodes):</text>
        <text x="70" y="535" font-size="12" fill="#aaa">Instead of 1 circle per server, Server A puts 100 random tokens (A1, A2, A3) on the ring.</text>
        <text x="70" y="555" font-size="12" fill="#aaa">This ensures data distribution is statistically even.</text>

        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="#fff" />
            </marker>
        </defs>
    </svg>"""
    
    create_svg_file(os.path.join(base_dir, "day14_consistent_hashing.svg"), svg_content)

if __name__ == "__main__":
    main()
