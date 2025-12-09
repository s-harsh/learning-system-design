import os

def create_svg_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename}")

def main():
    base_dir = r"c:\Harsh\Learning\learning-system-design\Phase2-LLD\03-Schema-Design"
    os.makedirs(base_dir, exist_ok=True)

    # Style constants
    bg_color = "#121212"
    card_bg = "#1e1e1e"
    text_color = "#e0e0e0"
    accent_blue = "#61dafb"
    accent_green = "#4caf50"
    accent_red = "#f44336"
    accent_yellow = "#ffeb3b"
    font_family = "Consolas, monospace"

    svg_content = f"""<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        <style>
            text {{ font-family: {font_family}; fill: {text_color}; }}
            .title {{ font-size: 24px; font-weight: bold; fill: {accent_blue}; }}
            .section-title {{ font-size: 16px; font-weight: bold; fill: {accent_yellow}; }}
            .card {{ fill: {card_bg}; stroke: #333; stroke-width: 1; rx: 10; }}
            .small-text {{ font-size: 12px; fill: #aaa; }}
            .table-box {{ fill: #333; stroke: #555; }}
        </style>
        
        <!-- Main Title -->
        <text x="400" y="40" text-anchor="middle" class="title">Day 10: Protection & Foundation</text>

        <!-- Left Side: Proxy Pattern -->
        <rect x="20" y="70" width="370" height="300" class="card" />
        <text x="205" y="100" text-anchor="middle" class="section-title">1. The Proxy (The Bouncer)</text>
        
        <!-- Client -->
        <circle cx="80" cy="200" r="20" fill="#fff" />
        <text x="80" y="240" text-anchor="middle" class="small-text">User</text>

        <!-- Proxy -->
        <rect x="160" y="160" width="80" height="80" fill="{accent_blue}" rx="5" />
        <text x="200" y="205" text-anchor="middle" fill="#000" font-weight="bold">PROXY</text>
        <text x="200" y="270" text-anchor="middle" class="small-text" fill="{accent_green}">✅ Security</text>

        <!-- Real Server -->
        <rect x="300" y="170" width="60" height="60" fill="{accent_red}" rx="5" opacity="0.5"/>
        <text x="330" y="205" text-anchor="middle" fill="#fff" font-size="10">DB (VIP)</text>

        <!-- Arrows -->
        <line x1="100" y1="200" x2="160" y2="200" stroke="#fff" stroke-width="2" marker-end="url(#arrow)" />
        <line x1="240" y1="200" x2="300" y2="200" stroke="#fff" stroke-width="2" stroke-dasharray="4" marker-end="url(#arrow)" />


        <!-- Right Side: Schema Design -->
        <rect x="410" y="70" width="370" height="300" class="card" />
        <text x="595" y="100" text-anchor="middle" class="section-title">2. Schema Design (Normalization)</text>

        <!-- Bad Table -->
        <text x="500" y="140" text-anchor="middle" class="small-text" fill="{accent_red}">❌ Un-Normalized</text>
        <rect x="440" y="150" width="120" height="60" class="table-box" />
        <line x1="440" y1="170" x2="560" y2="170" stroke="#555" />
        <text x="450" y="165" font-size="10">Student | Course</text>
        <text x="450" y="185" font-size="10" fill="#aaa">Harsh | Math, Phy</text>

        <!-- Good Tables -->
        <text x="700" y="140" text-anchor="middle" class="small-text" fill="{accent_green}">✅ 3rd Normal Form</text>
        <rect x="640" y="150" width="100" height="50" class="table-box" />
        <text x="690" y="165" text-anchor="middle" font-size="10">Students</text>
        
        <rect x="640" y="210" width="100" height="50" class="table-box" />
        <text x="690" y="225" text-anchor="middle" font-size="10">Courses</text>

        <rect x="640" y="270" width="100" height="50" class="table-box" />
        <text x="690" y="285" text-anchor="middle" font-size="10">Enrollment</text>

        <!-- Arrow -->
        <line x1="570" y1="180" x2="630" y2="180" stroke="#fff" stroke-width="2" marker-end="url(#arrow)" />

        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="#fff" />
            </marker>
        </defs>
    </svg>"""
    
    create_svg_file(os.path.join(base_dir, "day10_summary_card.svg"), svg_content)

if __name__ == "__main__":
    main()
