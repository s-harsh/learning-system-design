import os

def create_svg_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename}")

def main():
    base_dir = r"c:\Harsh\Learning\learning-system-design\Phase3-HLD\01-Scalability"
    os.makedirs(base_dir, exist_ok=True)

    # Style constants
    bg_color = "#121212"
    card_bg = "#1e1e1e"
    text_color = "#e0e0e0"
    accent_blue = "#61dafb"
    accent_green = "#4caf50"
    accent_red = "#f44336"
    accent_yellow = "#ffeb3b"
    accent_purple = "#bb86fc"
    font_family = "Consolas, monospace"

    svg_content = f"""<svg width="900" height="600" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        <style>
            text {{ font-family: {font_family}; fill: {text_color}; }}
            .title {{ font-size: 24px; font-weight: bold; fill: {accent_blue}; }}
            .section {{ font-size: 18px; font-weight: bold; fill: {accent_yellow}; }}
            .card {{ fill: {card_bg}; stroke: #333; stroke-width: 1; rx: 10; }}
            .server {{ fill: #333; stroke: #555; stroke-width: 2; rx: 5; }}
            .lb {{ fill: {accent_blue}; stroke: #fff; stroke-width: 2; rx: 10; }}
            .redis {{ fill: {accent_red}; stroke: #fff; stroke-width: 2; rx: 10; }}
            .packet {{ fill: #fff; }}
            .arrow {{ stroke: #fff; stroke-width: 2; marker-end: url(#arrow); }}
            .small-text {{ font-size: 10px; fill: #aaa; }}
        </style>
        
        <text x="450" y="40" text-anchor="middle" class="title">Day 12: Scaling Physics & The Gatekeepers</text>

        <!-- SECTION 1: SCALING PHYSICS -->
        <rect x="20" y="70" width="420" height="500" class="card" />
        <text x="230" y="100" text-anchor="middle" class="section">1. Scaling Physics</text>

        <!-- Vertical Failure -->
        <text x="30" y="140" font-weight="bold" fill="{accent_red}">A. Vertical (Limit)</text>
        <rect x="30" y="160" width="120" height="140" stroke="{accent_red}" fill="#220000" rx="5" />
        <text x="90" y="180" text-anchor="middle" fill="{accent_red}" font-size="12">MOTHERBOARD</text>
        
        <!-- Sockets -->
        <rect x="50" y="200" width="35" height="35" fill="#444" />
        <rect x="95" y="200" width="35" height="35" fill="#444" />
        <text x="90" y="260" text-anchor="middle" class="small-text">No Space for CPU #3!</text>
        <text x="90" y="280" text-anchor="middle" font-size="12">🧱</text>

        <!-- Horizontal Success -->
        <text x="240" y="140" font-weight="bold" fill="{accent_green}">B. Horizontal (Stateless)</text>
        
        <!-- Servers -->
        <rect x="240" y="160" width="50" height="60" class="server" style="stroke:{accent_green}"/>
        <text x="265" y="190" text-anchor="middle">S1</text>
        
        <rect x="310" y="160" width="50" height="60" class="server" style="stroke:{accent_green}"/>
        <text x="335" y="190" text-anchor="middle">S2</text>

        <rect x="380" y="160" width="50" height="60" class="server" style="stroke:{accent_green}"/>
        <text x="405" y="190" text-anchor="middle">S3</text>

        <!-- Shared State (Redis) -->
        <rect x="280" y="280" width="110" height="40" class="redis" />
        <text x="335" y="305" text-anchor="middle" fill="#000" font-weight="bold">Redis (State)</text>

        <!-- Lines to Redis -->
        <line x1="265" y1="220" x2="300" y2="280" stroke="#555" stroke-dasharray="2" />
        <line x1="335" y1="220" x2="335" y2="280" stroke="#555" stroke-dasharray="2" />
        <line x1="405" y1="220" x2="370" y2="280" stroke="#555" stroke-dasharray="2" />
        
        <text x="335" y="340" text-anchor="middle" class="small-text">Any server can answer.</text>


        <!-- SECTION 2: THE GATEKEEPERS -->
        <rect x="460" y="70" width="420" height="500" class="card" />
        <text x="670" y="100" text-anchor="middle" class="section">2. The Gatekeepers (Load Balancers)</text>

        <!-- L4 LB -->
        <text x="490" y="140" font-weight="bold" fill="{accent_purple}">A. Layer 4 (Transport)</text>
        
        <!-- Packet Incoming -->
        <text x="480" y="185" class="small-text">IP: 1.2.3.4</text>
        <line x1="530" y1="180" x2="570" y2="180" class="arrow"/>
        
        <!-- LB Box -->
        <rect x="570" y="160" width="80" height="40" class="lb" fill="{accent_purple}"/>
        <text x="610" y="185" text-anchor="middle" fill="#000">L4 LB</text>
        
        <!-- Outgoing -->
        <line x1="650" y1="180" x2="700" y2="150" class="arrow"/>
        <line x1="650" y1="180" x2="700" y2="210" class="arrow"/>

        <text x="610" y="220" text-anchor="middle" class="small-text">"I just throw packets."</text>


        <!-- L7 LB -->
        <text x="490" y="300" font-weight="bold" fill="{accent_blue}">B. Layer 7 (Application)</text>
        
        <!-- Packet Incoming -->
        <text x="480" y="355" class="small-text">GET /images</text>
        <line x1="540" y1="350" x2="570" y2="350" class="arrow"/>

        <!-- LB Box -->
        <rect x="570" y="330" width="80" height="40" class="lb" />
        <text x="610" y="355" text-anchor="middle" fill="#000">L7 LB</text>

        <!-- Routing -->
        <path d="M 650 350 L 700 320" stroke="{accent_blue}" stroke-width="2" marker-end="url(#arrow)" />
        <rect x="700" y="300" width="70" height="40" class="server"/>
        <text x="735" y="325" text-anchor="middle" font-size="10">ImageServer</text>

        <path d="M 650 350 L 700 380" stroke="{accent_blue}" stroke-width="2" marker-end="url(#arrow)" />
        <rect x="700" y="360" width="70" height="40" class="server"/>
        <text x="735" y="385" text-anchor="middle" font-size="10">AppServer</text>
        
        <text x="610" y="400" text-anchor="middle" class="small-text">"I read the URL."</text>

        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="#fff" />
            </marker>
        </defs>
    </svg>"""
    
    create_svg_file(os.path.join(base_dir, "day12_scalability.svg"), svg_content)

if __name__ == "__main__":
    main()
