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
            .section-title {{ font-size: 14px; font-weight: bold; fill: {accent_yellow}; }}
            .card {{ fill: {card_bg}; stroke: #333; stroke-width: 1; rx: 10; }}
            .small-text {{ font-size: 10px; fill: #aaa; }}
        </style>
        
        <!-- Main Title -->
        <text x="400" y="40" text-anchor="middle" class="title">Behavoral Patterns (Day 9)</text>

        <!-- 1. Strategy -->
        <rect x="20" y="70" width="240" height="150" class="card" />
        <text x="140" y="95" text-anchor="middle" class="section-title">Strategy</text>
        <text x="140" y="115" text-anchor="middle" class="small-text">Swap Algorithms</text>
        <rect x="50" y="130" width="60" height="40" fill="#333" stroke="{accent_green}" stroke-dasharray="4"/>
        <text x="80" y="155" text-anchor="middle" font-size="20">🔄</text>
        <rect x="170" y="130" width="60" height="40" fill="#333" stroke="{accent_blue}"/>
        <rect x="180" y="130" width="60" height="40" fill="#333" stroke="{accent_red}" transform="translate(10, 10)" opacity="0.5"/>

        <!-- 2. Observer -->
        <rect x="280" y="70" width="240" height="150" class="card" />
        <text x="400" y="95" text-anchor="middle" class="section-title">Observer</text>
        <text x="400" y="115" text-anchor="middle" class="small-text">Pub/Sub Notification</text>
        <circle cx="400" cy="150" r="15" fill="{accent_red}" /> <!-- Subject -->
        <line x1="400" y1="150" x2="350" y2="180" stroke="#555" stroke-width="2" marker-end="url(#arrow)"/>
        <line x1="400" y1="150" x2="450" y2="180" stroke="#555" stroke-width="2" marker-end="url(#arrow)"/>
        <circle cx="350" cy="180" r="10" fill="{accent_blue}" />
        <circle cx="450" cy="180" r="10" fill="{accent_blue}" />

        <!-- 3. Command -->
        <rect x="540" y="70" width="240" height="150" class="card" />
        <text x="660" y="95" text-anchor="middle" class="section-title">Command</text>
        <text x="660" y="115" text-anchor="middle" class="small-text">Request as Object (Undo)</text>
        <rect x="620" y="140" width="80" height="30" fill="{accent_purple}" rx="5"/>
        <text x="660" y="160" text-anchor="middle" fill="#111" font-size="10">Execute()</text>
        <text x="660" y="190" text-anchor="middle" font-size="12">↩ Undo</text>

        <!-- 4. State -->
        <rect x="140" y="240" width="240" height="150" class="card" />
        <text x="260" y="265" text-anchor="middle" class="section-title">State</text>
        <text x="260" y="285" text-anchor="middle" class="small-text">Behavior changes with State</text>
        <circle cx="220" cy="320" r="20" fill="none" stroke="{accent_yellow}"/>
        <text x="220" y="325" text-anchor="middle" font-size="10" fill="{accent_yellow}">Draft</text>
        <line x1="240" y1="320" x2="280" y2="320" stroke="#fff" marker-end="url(#arrow)"/>
        <circle cx="300" cy="320" r="20" fill="none" stroke="{accent_green}"/>
        <text x="300" y="325" text-anchor="middle" font-size="10" fill="{accent_green}">Pub</text>

        <!-- 5. Template Method -->
        <rect x="420" y="240" width="240" height="150" class="card" />
        <text x="540" y="265" text-anchor="middle" class="section-title">Template Method</text>
        <text x="540" y="285" text-anchor="middle" class="small-text">Algorithm Skeleton</text>
        <rect x="500" y="310" width="80" height="15" fill="#444"/>
        <rect x="500" y="330" width="80" height="15" fill="{accent_blue}"/>
        <rect x="500" y="350" width="80" height="15" fill="#444"/>
        <text x="590" y="340" font-size="10" fill="{accent_blue}">← Varies</text>

        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="#888" />
            </marker>
        </defs>
    </svg>"""
    
    create_svg_file(os.path.join(base_dir, "day9_summary_card.svg"), svg_content)

if __name__ == "__main__":
    main()
