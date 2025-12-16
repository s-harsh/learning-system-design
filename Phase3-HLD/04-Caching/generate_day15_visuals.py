import os

def create_svg_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename}")

def main():
    base_dir = r"c:\Harsh\Learning\learning-system-design\Phase3-HLD\04-Caching"
    os.makedirs(base_dir, exist_ok=True)

    # Style constants
    bg_color = "#121212"
    text_color = "#e0e0e0"
    accent_green = "#4caf50"
    accent_red = "#f44336"
    accent_blue = "#61dafb"
    box_fill = "#222"
    font_family = "Consolas, monospace"

    svg_content = f"""<svg width="900" height="500" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        <style>
            text {{ font-family: {font_family}; fill: {text_color}; }}
            .title {{ font-size: 24px; font-weight: bold; fill: {accent_blue}; }}
            .box {{ fill: {box_fill}; stroke: #555; stroke-width: 2; rx: 5; }}
            .arrow {{ stroke: #fff; stroke-width: 2; marker-end: url(#arrow); }}
            .label {{ font-size: 16px; font-weight: bold; }}
            .small-text {{ font-size: 12px; fill: #aaa; }}
            .step {{ font-size: 14px; fill: {accent_blue}; font-weight: bold; }}
        </style>
        
        <text x="450" y="40" text-anchor="middle" class="title">Write-Through vs Write-Back</text>

        <!-- Defs for arrow -->
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="#fff" />
            </marker>
        </defs>

        <!-- PANEL 1: Write-Through -->
        <g transform="translate(50, 80)">
            <text x="150" y="0" text-anchor="middle" class="label" fill="{accent_green}">Write-Through (Safe)</text>
            
            <!-- App -->
            <rect x="100" y="30" width="100" height="50" class="box" />
            <text x="150" y="60" text-anchor="middle">Application</text>

            <!-- Cache -->
            <rect x="100" y="150" width="100" height="50" class="box" stroke="{accent_green}"/>
            <text x="150" y="180" text-anchor="middle">Cache</text>

            <!-- DB -->
            <rect x="100" y="270" width="100" height="50" class="box" />
            <text x="150" y="300" text-anchor="middle">Database</text>

            <!-- Arrows -->
            <line x1="150" y1="80" x2="150" y2="150" class="arrow"/>
            <text x="160" y="120" class="step">1. Write</text>

            <line x1="150" y1="200" x2="150" y2="270" class="arrow"/>
            <text x="160" y="240" class="step">2. Sync Write</text>

            <path d="M 200 295 Q 260 200 200 65" fill="none" class="arrow" stroke="{accent_green}" stroke-dasharray="4"/>
            <text x="210" y="180" class="step">3. Confirm</text>
            
            <text x="150" y="350" text-anchor="middle" class="small-text">Slow but Consistent</text>
        </g>

        <!-- PANEL 2: Write-Back -->
        <g transform="translate(500, 80)">
            <text x="150" y="0" text-anchor="middle" class="label" fill="{accent_red}">Write-Back (Fast)</text>
            
            <!-- App -->
            <rect x="100" y="30" width="100" height="50" class="box" />
            <text x="150" y="60" text-anchor="middle">Application</text>

            <!-- Cache -->
            <rect x="100" y="150" width="100" height="50" class="box" stroke="{accent_red}"/>
            <text x="150" y="180" text-anchor="middle">Cache (Dirty)</text>

            <!-- DB -->
            <rect x="100" y="270" width="100" height="50" class="box" />
            <text x="150" y="300" text-anchor="middle">Database</text>

            <!-- Arrows -->
            <line x1="150" y1="80" x2="150" y2="150" class="arrow"/>
            <text x="160" y="120" class="step">1. Write</text>

            <path d="M 200 175 Q 240 120 200 65" fill="none" class="arrow" stroke="{accent_green}" stroke-dasharray="4"/>
            <text x="220" y="120" class="step">2. Confirm (FAST)</text>

            <line x1="150" y1="200" x2="150" y2="270" class="arrow" stroke-dasharray="5"/>
            <text x="160" y="240" class="step" fill="#aaa">3. Async Sync (Later)</text>
            
            <text x="150" y="350" text-anchor="middle" class="small-text">Risk of Data Loss!</text>
        </g>

    </svg>"""
    
    create_svg_file(os.path.join(base_dir, "day15_caching_strategies.svg"), svg_content)

if __name__ == "__main__":
    main()
