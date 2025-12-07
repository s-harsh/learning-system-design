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
            .icon-box {{ fill: #333; stroke: {text_color}; stroke-width: 1; }}
        </style>
        
        <!-- Main Title -->
        <text x="400" y="40" text-anchor="middle" class="title">System Design Day 7: The Toolkit</text>

        <!-- Quadrant 1: DRY & KISS -->
        <rect x="20" y="70" width="370" height="250" class="card" />
        <text x="205" y="100" text-anchor="middle" class="section-title">1. Principles (DRY &amp; KISS)</text>
        
        <!-- DRY Visual -->
        <text x="40" y="130" font-weight="bold" fill="{accent_green}">DRY</text>
        <text x="80" y="130" class="small-text">Don't Repeat Yourself</text>
        <rect x="40" y="140" width="100" height="40" fill="#2d2d2d" stroke="{accent_green}" stroke-dasharray="4"/>
        <text x="90" y="165" text-anchor="middle" font-size="10">Single Truth</text>

        <!-- KISS Visual -->
        <text x="210" y="130" font-weight="bold" fill="{accent_purple}">KISS</text>
        <text x="250" y="130" class="small-text">Keep It Simple, Stupid</text>
        <text x="210" y="160" font-size="12">Simple > Clever</text>
        <text x="210" y="180" font-size="12" fill="{accent_red}">No Over-Engineering!</text>

        <rect x="40" y="200" width="330" height="100" fill="#252526" rx="5"/>
        <text x="50" y="220" class="code"># Bad (WET)</text>
        <text x="50" y="235" class="code">def a(): x=1; y=2</text>
        <text x="50" y="250" class="code">def b(): x=1; y=2 # &lt;- Duplicate</text>
        <text x="200" y="220" class="code" fill="{accent_green}"># Good (DRY)</text>
        <text x="200" y="235" class="code">def common(): ...</text>
        <text x="200" y="250" class="code">def a(): common()</text>


        <!-- Quadrant 2: Pattern Categories -->
        <rect x="410" y="70" width="370" height="250" class="card" />
        <text x="595" y="100" text-anchor="middle" class="section-title">2. Design Pattern Types</text>
        
        <circle cx="595" cy="180" r="40" fill="#333" stroke="{accent_blue}" />
        <text x="595" y="185" text-anchor="middle" font-weight="bold" font-size="14">Patterns</text>

        <!-- Branches -->
        <line x1="595" y1="140" x2="595" y2="120" stroke="#555" stroke-width="2"/>
        <line x1="555" y1="180" x2="480" y2="180" stroke="#555" stroke-width="2"/>
        <line x1="635" y1="180" x2="710" y2="180" stroke="#555" stroke-width="2"/>

        <!-- Bubble 1 -->
        <rect x="545" y="120" width="100" height="30" rx="15" fill="#444"/>
        <text x="595" y="140" text-anchor="middle" font-size="12" fill="{accent_yellow}">Creational</text>
        <text x="595" y="160" text-anchor="middle" font-size="10" fill="#aaa">(Construction)</text>

        <!-- Bubble 2 -->
        <rect x="415" y="165" width="90" height="30" rx="15" fill="#444"/>
        <text x="460" y="185" text-anchor="middle" font-size="12" fill="{accent_green}">Structural</text>
        <text x="460" y="205" text-anchor="middle" font-size="10" fill="#aaa">(Connection)</text>

        <!-- Bubble 3 -->
        <rect x="685" y="165" width="90" height="30" rx="15" fill="#444"/>
        <text x="730" y="185" text-anchor="middle" font-size="12" fill="{accent_purple}">Behavioral</text>
        <text x="730" y="205" text-anchor="middle" font-size="10" fill="#aaa">(Communication)</text>


        <!-- Quadrant 3: Singleton -->
        <rect x="20" y="340" width="370" height="240" class="card" />
        <text x="205" y="370" text-anchor="middle" class="section-title">3. Singleton</text>
        <text x="205" y="390" text-anchor="middle" class="small-text">One Instance to rule them all</text>

        <rect x="135" y="410" width="140" height="100" class="icon-box" rx="5"/>
        <rect x="135" y="410" width="140" height="30" fill="#444" rx="5"/>
        <text x="205" y="430" text-anchor="middle" font-weight="bold">Database</text>
        
        <text x="145" y="460" class="code" font-size="10">- static instance</text>
        <text x="145" y="480" class="code" font-size="10">+ getInstance()</text>
        <text x="145" y="500" class="code" font-size="10">- private init()</text>

        <text x="205" y="540" text-anchor="middle" font-size="12" fill="{accent_red}">Thread Safety Required!</text>
        <text x="205" y="560" text-anchor="middle" font-size="11" fill="#aaa">(Use Locks)</text>


        <!-- Quadrant 4: Factory Method -->
        <rect x="410" y="340" width="370" height="240" class="card" />
        <text x="595" y="370" text-anchor="middle" class="section-title">4. Factory Method</text>
        <text x="595" y="390" text-anchor="middle" class="small-text">Decouple creation from logic</text>

        <!-- Client -->
        <circle cx="470" cy="450" r="20" fill="#555"/>
        <text x="470" y="455" text-anchor="middle" font-size="10">Client</text>

        <!-- Factory -->
        <rect x="540" y="430" width="80" height="40" fill="#444" stroke="{accent_blue}" rx="5"/>
        <text x="580" y="455" text-anchor="middle" font-size="12">Factory</text>

        <!-- Arrow -->
        <line x1="490" y1="450" x2="540" y2="450" stroke="{text_color}" marker-end="url(#arrowhead)"/>
        <line x1="620" y1="450" x2="650" y2="450" stroke="{text_color}" marker-end="url(#arrowhead)"/>

        <!-- Products -->
        <rect x="660" y="410" width="60" height="30" fill="{accent_green}" rx="3"/>
        <text x="690" y="430" text-anchor="middle" fill="#111" font-size="10">Stripe</text>

        <rect x="660" y="460" width="60" height="30" fill="{accent_yellow}" rx="3"/>
        <text x="690" y="480" text-anchor="middle" fill="#111" font-size="10">PayPal</text>
        
        <text x="580" y="530" text-anchor="middle" font-size="12" fill="#aaa">"I don't care how it's created,</text>
        <text x="580" y="550" text-anchor="middle" font-size="12" fill="#aaa">just give me a PaymentProcessor"</text>

        <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="{text_color}" />
            </marker>
        </defs>
    </svg>"""
    
    create_svg_file(os.path.join(base_dir, "day7_summary_card.svg"), svg_content)

if __name__ == "__main__":
    main()
