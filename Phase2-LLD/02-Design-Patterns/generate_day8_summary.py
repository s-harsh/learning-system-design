import os

def create_svg_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename}")

def main():
    base_dir = r"c:\Harsh\Learning\learning-system-design\Phase2-LLD\02-Design-Patterns"
    os.makedirs(base_dir, exist_ok=True)

    # Style constants
    bg_color = "#121212"
    card_bg = "#1e1e1e"
    text_color = "#e0e0e0"
    accent_blue = "#61dafb"
    accent_green = "#4caf50"
    accent_red = "#f44336"
    accent_yellow = "#ffeb3b"
    accent_purple = "#c792ea"
    font_family = "Consolas, monospace"

    svg_content = f"""<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        <style>
            text {{ font-family: {font_family}; fill: {text_color}; }}
            .title {{ font-size: 28px; font-weight: bold; fill: {accent_blue}; }}
            .section-title {{ font-size: 18px; font-weight: bold; fill: {accent_yellow}; }}
            .card {{ fill: {card_bg}; stroke: #333; stroke-width: 1; rx: 10; }}
            .code {{ font-size: 12px; fill: #dcdcaa; }}
            .small-text {{ font-size: 11px; fill: #aaa; }}
            .box {{ fill: #333; stroke: {text_color}; stroke-width: 1; }}
        </style>
        
        <!-- Main Title -->
        <text x="400" y="40" text-anchor="middle" class="title">System Design Day 8: Structural Patterns</text>

        <!-- Quadrant 1: Builder -->
        <rect x="20" y="70" width="370" height="250" class="card" />
        <text x="205" y="100" text-anchor="middle" class="section-title">1. Builder Pattern</text>
        <text x="205" y="120" text-anchor="middle" class="small-text">Step-by-step Creation</text>
        
        <rect x="40" y="140" width="100" height="30" fill="{accent_green}" rx="5"/>
        <text x="90" y="160" text-anchor="middle" fill="#111" font-weight="bold">Base</text>
        
        <text x="160" y="160" text-anchor="middle" font-size="20">+</text>
        
        <rect x="190" y="140" width="100" height="30" fill="{accent_yellow}" rx="5"/>
        <text x="240" y="160" text-anchor="middle" fill="#111" font-weight="bold">Option A</text>

        <text x="205" y="200" text-anchor="middle" font-size="20">⬇</text>
        <text x="205" y="220" text-anchor="middle" font-size="20">.build()</text>

        <rect x="115" y="240" width="180" height="50" fill="{accent_blue}" rx="5"/>
        <text x="205" y="270" text-anchor="middle" fill="#111" font-weight="bold">Complex Object</text>


        <!-- Quadrant 2: Adapter -->
        <rect x="410" y="70" width="370" height="250" class="card" />
        <text x="595" y="100" text-anchor="middle" class="section-title">2. Adapter Pattern</text>
        <text x="595" y="120" text-anchor="middle" class="small-text">Incompatible Interfaces</text>

        <!-- Round Plug -->
        <circle cx="460" cy="180" r="20" fill="{accent_green}" />
        <text x="460" y="220" text-anchor="middle" font-size="10">Round Plug</text>
        
        <!-- Adapter -->
        <path d="M 520 160 L 600 160 L 600 200 L 520 200 Z" fill="#444" stroke="{accent_purple}" stroke-width="2"/>
        <circle cx="530" cy="180" r="15" fill="#222" /> <!-- Hole for Round -->
        <rect x="580" y="170" width="20" height="20" fill="#222" /> <!-- Hole for Square -->
        <text x="560" y="230" text-anchor="middle" fill="{accent_purple}">Adapter</text>

        <!-- Square Socket -->
        <rect x="660" y="160" width="40" height="40" fill="{accent_red}" />
        <text x="680" y="220" text-anchor="middle" font-size="10">Square Socket</text>


        <!-- Quadrant 3: Decorator -->
        <rect x="20" y="340" width="370" height="240" class="card" />
        <text x="205" y="370" text-anchor="middle" class="section-title">3. Decorator Pattern</text>
        <text x="205" y="390" text-anchor="middle" class="small-text">Dynamic Wrappers (Matryoshka)</text>

        <!-- Core -->
        <circle cx="205" cy="480" r="20" fill="{accent_blue}" />
        <text x="205" y="485" text-anchor="middle" fill="#111" font-size="10">Obj</text>

        <!-- Wrapper 1 -->
        <circle cx="205" cy="480" r="40" fill="none" stroke="{accent_yellow}" stroke-width="3" stroke-dasharray="5,5"/>
        <text x="205" y="430" text-anchor="middle" font-size="10" fill="{accent_yellow}">Wrapper 1 (Milk)</text>

        <!-- Wrapper 2 -->
        <circle cx="205" cy="480" r="60" fill="none" stroke="{accent_purple}" stroke-width="3" />
        <text x="205" y="560" text-anchor="middle" font-size="10" fill="{accent_purple}">Wrapper 2 (Whip)</text>


        <!-- Quadrant 4: Facade -->
        <rect x="410" y="340" width="370" height="240" class="card" />
        <text x="595" y="370" text-anchor="middle" class="section-title">4. Facade Pattern</text>
        <text x="595" y="390" text-anchor="middle" class="small-text">Simple Interface for Complexity</text>

        <!-- The Wall -->
        <rect x="540" y="420" width="110" height="120" fill="#333" stroke="{accent_blue}" stroke-width="2" rx="5"/>
        <text x="595" y="450" text-anchor="middle" font-weight="bold">Facade</text>
        <rect x="560" y="480" width="70" height="30" fill="{accent_green}" rx="5"/>
        <text x="595" y="500" text-anchor="middle" fill="#111" font-size="10">Start()</text>

        <!-- Complexity Behind -->
        <line x1="650" y1="450" x2="720" y2="420" stroke="#555" stroke-dasharray="4"/>
        <line x1="650" y1="480" x2="720" y2="480" stroke="#555" stroke-dasharray="4"/>
        <line x1="650" y1="510" x2="720" y2="540" stroke="#555" stroke-dasharray="4"/>
        
        <rect x="720" y="410" width="40" height="20" fill="#444"/>
        <rect x="720" y="470" width="40" height="20" fill="#444"/>
        <rect x="720" y="530" width="40" height="20" fill="#444"/>
        
        <text x="740" y="570" text-anchor="middle" font-size="10" fill="#aaa">Messy Subsystem</text>

        <!-- Client -->
        <circle cx="450" cy="480" r="20" fill="#bbb"/>
        <text x="450" y="520" text-anchor="middle" font-size="10">User</text>
        <line x1="470" y1="480" x2="540" y2="480" stroke="{text_color}" marker-end="url(#arrowhead)"/>

        <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="{text_color}" />
            </marker>
        </defs>
    </svg>"""
    
    create_svg_file(os.path.join(base_dir, "day8_summary_card.svg"), svg_content)

if __name__ == "__main__":
    main()
