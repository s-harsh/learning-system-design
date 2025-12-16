import os

def create_svg_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename}")

def main():
    base_dir = r"c:\Harsh\Learning\learning-system-design\Phase3-HLD\05-Message-Queues"
    os.makedirs(base_dir, exist_ok=True)

    # Style constants
    bg_color = "#121212"
    text_color = "#e0e0e0"
    rabbit_color = "#ff6600" # Orange
    kafka_color = "#2196f3" # Blue
    box_fill = "#222"
    font_family = "Consolas, monospace"

    svg_content = f"""<svg width="900" height="500" xmlns="http://www.w3.org/2000/svg" style="background-color:{bg_color}">
        <style>
            text {{ font-family: {font_family}; fill: {text_color}; }}
            .title {{ font-size: 24px; font-weight: bold; fill: #fff; }}
            .subtitle {{ font-size: 18px; font-weight: bold; }}
            .box {{ fill: {box_fill}; stroke: #555; stroke-width: 2; rx: 5; }}
            .msg {{ rx: 2; ry: 2; }}
            .arrow {{ stroke: #fff; stroke-width: 2; marker-end: url(#arrow); }}
            .label {{ font-size: 14px; font-weight: bold; }}
            .small-text {{ font-size: 12px; fill: #aaa; }}
        </style>
        
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="#fff" />
            </marker>
        </defs>

        <text x="450" y="40" text-anchor="middle" class="title">RabbitMQ (Queue) vs Kafka (Log)</text>

        <!-- LEFT PANEL: RabbitMQ -->
        <g transform="translate(50, 80)">
            <text x="150" y="0" text-anchor="middle" class="subtitle" fill="{rabbit_color}">RabbitMQ 🐰</text>
            <text x="150" y="20" text-anchor="middle" class="small-text">Smart Broker, Push Model</text>

            <!-- Broker Box -->
            <rect x="50" y="50" width="200" height="150" fill="#333" stroke="{rabbit_color}" stroke-width="2" rx="10"/>
            <text x="150" y="70" text-anchor="middle" fill="#fff">Broker Memory</text>

            <!-- Queue Items -->
            <rect x="80" y="100" width="30" height="30" fill="{rabbit_color}" class="msg"><title>Msg 3</title></rect>
            <rect x="120" y="100" width="30" height="30" fill="{rabbit_color}" class="msg"><title>Msg 2</title></rect>
            
            <!-- Consumer -->
            <rect x="100" y="250" width="100" height="50" class="box" />
            <text x="150" y="280" text-anchor="middle">Consumer</text>

            <!-- Push Arrow -->
            <line x1="150" y1="200" x2="150" y2="250" class="arrow"/>
            <text x="160" y="230" class="small-text">Push!</text>

            <!-- Gone Msg -->
            <text x="200" y="120" class="small-text" fill="#777">Msg 1 (Gone)</text>
            <text x="150" y="320" text-anchor="middle" class="small-text" style="font-style:italic">"I delete msg after read"</text>
        </g>

        <!-- RIGHT PANEL: Kafka -->
        <g transform="translate(500, 80)">
            <text x="150" y="0" text-anchor="middle" class="subtitle" fill="{kafka_color}">Apache Kafka 🪵</text>
            <text x="150" y="20" text-anchor="middle" class="small-text">Dumb Broker, Pull Model</text>

            <!-- Broker Box -->
            <rect x="50" y="50" width="250" height="150" fill="#333" stroke="{kafka_color}" stroke-width="2" rx="10"/>
            <text x="175" y="70" text-anchor="middle" fill="#fff">Disk Storage (Log)</text>

            <!-- Log Strip -->
            <rect x="70" y="100" width="210" height="40" fill="#111" stroke="#555"/>
            <!-- Messages persisted -->
            <rect x="75" y="105" width="30" height="30" fill="{kafka_color}"><title>0</title></rect> <text x="90" y="125" text-anchor="middle" font-size="10" fill="black">0</text>
            <rect x="110" y="105" width="30" height="30" fill="{kafka_color}"><title>1</title></rect> <text x="125" y="125" text-anchor="middle" font-size="10" fill="black">1</text>
            <rect x="145" y="105" width="30" height="30" fill="{kafka_color}"><title>2</title></rect> <text x="160" y="125" text-anchor="middle" font-size="10" fill="black">2</text>
            <rect x="180" y="105" width="30" height="30" fill="#555"><title>3</title></rect> <text x="195" y="125" text-anchor="middle" font-size="10" fill="white">3</text>

            <!-- Consumer -->
            <rect x="100" y="250" width="150" height="50" class="box" />
            <text x="175" y="270" text-anchor="middle">Consumer</text>
            <text x="175" y="290" text-anchor="middle" fill="{kafka_color}" font-weight="bold">Idx: 2</text>

            <!-- Pull Arrow -->
            <path d="M 175 250 L 175 220" stroke="#fff" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
            <text x="185" y="230" class="small-text">Poll()</text>

            <text x="175" y="320" text-anchor="middle" class="small-text" style="font-style:italic">"I keep msg for 7 days"</text>
        </g>

    </svg>"""
    
    create_svg_file(os.path.join(base_dir, "day16_message_queues.svg"), svg_content)

if __name__ == "__main__":
    main()
