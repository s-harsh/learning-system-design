import os

def create_svg_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename}")

def main():
    base_dir = r"c:\Harsh\Learning\learning-system-design\Phase2-LLD\04-LLD-Practice-Problems"
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

    svg_content = f"""<svg width="800" height="450" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        <style>
            text {{ font-family: {font_family}; fill: {text_color}; }}
            .title {{ font-size: 24px; font-weight: bold; fill: {accent_blue}; }}
            .section-title {{ font-size: 16px; font-weight: bold; fill: {accent_yellow}; }}
            .card {{ fill: {card_bg}; stroke: #333; stroke-width: 1; rx: 10; }}
            .small-text {{ font-size: 12px; fill: #aaa; }}
            .box {{ fill: #333; stroke: {accent_blue}; stroke-width: 2; rx: 5; }}
            .arrow {{ stroke: #fff; stroke-width: 2; marker-end: url(#arrow); }}
        </style>
        
        <!-- Main Title -->
        <text x="400" y="40" text-anchor="middle" class="title">Day 11: LLD Practice (Parking Lot)</text>

        <!-- Container -->
        <rect x="50" y="70" width="700" height="350" class="card" />

        <!-- 1. The Requirement (Input) -->
        <text x="100" y="110" font-weight="bold" fill="{accent_green}">1. The Requirements</text>
        <text x="100" y="140" class="small-text">- Multiple Floors</text>
        <text x="100" y="160" class="small-text">- Vehicle Types (Car, Bike)</text>
        <text x="100" y="180" class="small-text">- Hourly Pricing</text>
        <text x="100" y="200" class="small-text">- Concurrency!</text>

        <!-- Arrow to Design -->
        <line x1="250" y1="150" x2="300" y2="150" class="arrow" />

        <!-- 2. The OOP Design (Center) -->
        <text x="400" y="110" text-anchor="middle" font-weight="bold" fill="{accent_yellow}">2. Object-Oriented Design</text>
        
        <!-- Abstract Vehicle -->
        <rect x="350" y="140" width="100" height="40" class="box" stroke-dasharray="4"/>
        <text x="400" y="165" text-anchor="middle" font-size="12">Vehicle (Abs)</text>
        
        <!-- Inheritance -->
        <path d="M 380 180 L 380 200" stroke="#fff" stroke-width="1" />
        <path d="M 420 180 L 420 200" stroke="#fff" stroke-width="1" />
        
        <rect x="360" y="200" width="40" height="30" fill="#333" stroke="#555"/>
        <text x="380" y="220" text-anchor="middle" font-size="10">Car</text>
        
        <rect x="400" y="200" width="40" height="30" fill="#333" stroke="#555"/>
        <text x="420" y="220" text-anchor="middle" font-size="10">Bike</text>

        <!-- Strategy Pattern -->
        <rect x="330" y="250" width="140" height="40" class="box" style="stroke: {accent_red}"/>
        <text x="400" y="275" text-anchor="middle" font-size="12">PricingStrategy</text>
        <text x="500" y="275" class="small-text" fill="{accent_red}">&lt;&lt;Interface&gt;&gt;</text>

        <!-- Arrow to DB -->
        <line x1="500" y1="150" x2="550" y2="150" class="arrow" />

        <!-- 3. The Database (Storage) -->
        <text x="650" y="110" text-anchor="middle" font-weight="bold" fill="{accent_blue}">3. Storage & Locks</text>

        <rect x="600" y="140" width="100" height="80" class="box" style="stroke: #aaa"/>
        <text x="650" y="165" text-anchor="middle" font-size="12">ParkingSpots</text>
        <line x1="600" y1="180" x2="700" y2="180" stroke="#aaa" />
        <text x="610" y="200" font-size="10" fill="{accent_green}">id: 101</text>
        <text x="610" y="215" font-size="10" fill="{accent_red}">occupied: true</text>
        
        <!-- Lock Info -->
        <text x="650" y="260" text-anchor="middle" font-size="12" fill="{accent_yellow}">⚡ Optimistic Lock</text>
        <text x="650" y="280" text-anchor="middle" class="small-text">Version / Status Check</text>

        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="#fff" />
            </marker>
        </defs>
    </svg>"""
    
    create_svg_file(os.path.join(base_dir, "day11_parking_lot.svg"), svg_content)

if __name__ == "__main__":
    main()
