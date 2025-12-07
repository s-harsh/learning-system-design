import os

def create_svg_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename}")

def main():
    base_dir = r"c:\Harsh\Learning\learning-system-design\Phase2-LLD\02-Design-Patterns"
    os.makedirs(base_dir, exist_ok=True)

    # Style constants
    bg_color = "#1e1e1e"
    text_color = "#e0e0e0"
    accent_blue = "#61dafb"
    accent_green = "#4caf50"
    accent_red = "#f44336"
    accent_yellow = "#ffeb3b"
    font_family = "Consolas, monospace"

    style = f"""
        <style>
            text {{ font-family: {font_family}; fill: {text_color}; }}
            .title {{ font-size: 24px; font-weight: bold; fill: {accent_blue}; }}
            .subtitle {{ font-size: 16px; fill: {accent_yellow}; }}
            .code {{ font-size: 14px; fill: #dcdcaa; }}
            .box {{ fill: #2d2d2d; stroke: {accent_blue}; stroke-width: 2; rx: 10; }}
            .bad-box {{ fill: #2d2d2d; stroke: {accent_red}; stroke-width: 2; rx: 10; }}
            .good-box {{ fill: #2d2d2d; stroke: {accent_green}; stroke-width: 2; rx: 10; }}
            .arrow {{ stroke: {text_color}; stroke-width: 2; marker-end: url(#arrowhead); }}
        </style>
        <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="{text_color}" />
            </marker>
        </defs>
    """

    # 1. DRY Concept Visual
    dry_svg = f"""<svg width="600" height="300" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        {style}
        <text x="300" y="40" text-anchor="middle" class="title">DRY (Don't Repeat Yourself)</text>
        
        <!-- WET Side -->
        <rect x="50" y="80" width="200" height="180" class="bad-box" />
        <text x="150" y="110" text-anchor="middle" fill="{accent_red}" font-weight="bold">WET (Bad)</text>
        <text x="70" y="140" class="code">def area(r):</text>
        <text x="80" y="160" class="code">return 3.14 * r * r</text>
        
        <text x="70" y="200" class="code">def vol(r, h):</text>
        <text x="80" y="220" class="code"># Repetition!</text>
        <text x="80" y="240" class="code">base = 3.14 * r * r</text>

        <!-- DRY Side -->
        <rect x="350" y="80" width="200" height="180" class="good-box" />
        <text x="450" y="110" text-anchor="middle" fill="{accent_green}" font-weight="bold">DRY (Good)</text>
        <text x="370" y="140" class="code">class Math:</text>
        <text x="380" y="160" class="code">PI = 3.14</text>
        
        <text x="370" y="200" class="code">def area(r):</text>
        <text x="380" y="220" class="code"># Single Truth</text>
        <text x="380" y="240" class="code">return PI * r**2</text>
    </svg>"""
    create_svg_file(os.path.join(base_dir, "day7_dry.svg"), dry_svg)

    # 2. Singleton Visual
    singleton_svg = f"""<svg width="600" height="300" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        {style}
        <text x="300" y="40" text-anchor="middle" class="title">Singleton Pattern</text>
        <text x="300" y="70" text-anchor="middle" class="subtitle">Ensuring One Instance</text>

        <!-- The Class -->
        <rect x="200" y="100" width="200" height="150" class="box" />
        <rect x="200" y="100" width="200" height="40" fill="#333" stroke="{accent_blue}" stroke-width="2" />
        <text x="300" y="125" text-anchor="middle" font-weight="bold" font-size="18">Database</text>
        
        <text x="220" y="160" class="code">- instance: static</text>
        <line x1="200" y1="170" x2="400" y2="170" stroke="{accent_blue}" />
        <text x="220" y="190" class="code">+ getInstance()</text>
        <text x="220" y="210" class="code">- __init__() (private)</text>

        <!-- Clients -->
        <circle cx="100" cy="200" r="30" fill="#555" />
        <text x="100" y="205" text-anchor="middle" font-size="12">Client A</text>
        
        <circle cx="500" cy="200" r="30" fill="#555" />
        <text x="500" y="205" text-anchor="middle" font-size="12">Client B</text>

        <!-- Arrows -->
        <line x1="130" y1="200" x2="200" y2="150" class="arrow" />
        <line x1="470" y1="200" x2="400" y2="150" class="arrow" />

    </svg>"""
    create_svg_file(os.path.join(base_dir, "day7_singleton.svg"), singleton_svg)

    # 3. Factory Visual
    factory_svg = f"""<svg width="600" height="350" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        {style}
        <text x="300" y="40" text-anchor="middle" class="title">Factory Method</text>
        <text x="300" y="70" text-anchor="middle" class="subtitle">Decoupling Creation from Logic</text>

        <!-- Creator -->
        <rect x="220" y="100" width="160" height="60" class="box" />
        <text x="300" y="125" text-anchor="middle" font-weight="bold">LogisticsApp</text>
        <text x="300" y="145" text-anchor="middle" font-size="12" fill="#aaa">create_transport()</text>

        <!-- Products -->
        <rect x="50" y="250" width="120" height="50" class="good-box" />
        <text x="110" y="280" text-anchor="middle">Truck</text>

        <rect x="240" y="250" width="120" height="50" class="good-box" />
        <text x="300" y="280" text-anchor="middle">Ship</text>

        <rect x="430" y="250" width="120" height="50" class="good-box" />
        <text x="490" y="280" text-anchor="middle">Drone</text>

        <!-- Arrows -->
        <line x1="300" y1="160" x2="110" y2="250" class="arrow" />
        <line x1="300" y1="160" x2="300" y2="250" class="arrow" />
        <line x1="300" y1="160" x2="490" y2="250" class="arrow" />

    </svg>"""
    create_svg_file(os.path.join(base_dir, "day7_factory.svg"), factory_svg)

if __name__ == "__main__":
    main()
