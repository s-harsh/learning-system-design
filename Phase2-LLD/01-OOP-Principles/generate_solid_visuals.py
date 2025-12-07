import math

def create_solid_visuals():
    generate_srp_svg()
    generate_dip_svg()
    generate_solid_card_svg()
    generate_ocp_svg()
    generate_lsp_svg()
    generate_isp_svg()

def generate_srp_svg(filename="solid_srp_sketch.svg"):
    width, height = 800, 500
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#f8f9fa;">'
    svg += f'<rect width="100%" height="100%" fill="#f8f9fa"/>'
    
    # Title
    svg += text(400, 40, "SRP: Single Responsibility Principle", 24, "#1f2937", "bold", "middle")
    
    # LEFT SIDE: THE GOD CLASS
    svg += text(200, 80, "❌ The 'God' Class", 18, "#ef4444", "bold", "middle")
    
    # Box
    svg += rect(50, 100, 300, 300, "#fee2e2", "#ef4444")
    svg += text(200, 130, "OrderManager", 16, "#991b1b", "bold", "middle")
    
    fn_style = 'font-family="monospace" font-size="14" fill="#7f1d1d"'
    svg += f'<text x="70" y="160" {fn_style}>- process_order()</text>'
    svg += f'<text x="70" y="190" {fn_style}>- check_inventory() 📦</text>'
    svg += f'<text x="70" y="220" {fn_style}>- charge_credit_card() 💳</text>'
    svg += f'<text x="70" y="250" {fn_style}>- send_email_smtp() 📧</text>'
    svg += f'<text x="70" y="280" {fn_style}>- generate_pdf_invoice() 📄</text>'
    svg += f'<text x="70" y="310" {fn_style}>- log_to_file() 💾</text>'
    
    svg += text(200, 360, "Files touched: 1", 14, "#ef4444", "normal", "middle")
    svg += text(200, 380, "Merge Conflicts: HIGH 🔥", 14, "#ef4444", "bold", "middle")

    # ARROW
    svg += f'<path d="M 370 250 L 430 250" stroke="#9ca3af" stroke-width="4" marker-end="url(#arrowhead)"/>'
    svg += f'<defs><marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#9ca3af"/></marker></defs>'

    # RIGHT SIDE: SRP COMPLIANT
    svg += text(600, 80, "✅ Decoupled Services", 18, "#10b981", "bold", "middle")
    
    # Small Boxes
    colors = [("#dbeafe", "#1e40af"), ("#d1fae5", "#065f46"), ("#fce7f3", "#9d174d")]
    labels = ["Start", "Inventory", "Payment", "Email"]
    
    # Orchestrator
    svg += rect(480, 100, 240, 60, "#f3f4f6", "#374151")
    svg += text(600, 135, "OrderOrchestrator", 14, "#1f2937", "bold", "middle")
    
    # Lines down
    svg += line(600, 160, 500, 200)
    svg += line(600, 160, 600, 200)
    svg += line(600, 160, 700, 200)
    
    # Service 1
    svg += rect(450, 200, 100, 80, "#dbeafe", "#2563eb")
    svg += text(500, 230, "Inventory", 12, "#1e3a8a", "bold", "middle")
    svg += text(500, 250, "Service", 12, "#1e3a8a", "bold", "middle")
    
    # Service 2
    svg += rect(550, 200, 100, 80, "#d1fae5", "#059669")
    svg += text(600, 230, "Payment", 12, "#064e3b", "bold", "middle")
    svg += text(600, 250, "Service", 12, "#064e3b", "bold", "middle")

    # Service 3
    svg += rect(650, 200, 100, 80, "#fce7f3", "#db2777")
    svg += text(700, 230, "Notification", 12, "#831843", "bold", "middle")
    svg += text(700, 250, "Service", 12, "#831843", "bold", "middle")
    
    svg += text(600, 360, "Files touched: 4", 14, "#059669", "normal", "middle")
    svg += text(600, 380, "Merge Conflicts: NONE ✨", 14, "#059669", "bold", "middle")

    svg += "</svg>"
    save(filename, svg)

def generate_dip_svg(filename="solid_dip_sketch.svg"):
    width, height = 800, 400
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff;">'
    svg += f'<rect width="100%" height="100%" fill="#ffffff"/>'
    
    svg += text(400, 40, "DIP: Dependency Inversion (The Power Plug)", 24, "#1f2937", "bold", "middle")
    
    # LEFT: High Level Module (Laptop)
    svg += rect(50, 150, 200, 150, "#e0e7ff", "#4338ca")
    svg += text(150, 200, "High Logic", 16, "#312e81", "bold", "middle")
    svg += text(150, 230, "(Your Laptop)", 14, "#6366f1", "normal", "middle")
    
    # The Wire
    svg += line(250, 225, 350, 225, "#1f2937", 8)
    
    # CENTER: Interface (The Socket)
    svg += circle(360, 225, 40, "#f3f4f6", "#4b5563")
    svg += text(360, 230, "Interface", 12, "#1f2937", "bold", "middle")
    # Socket holes
    svg += circle(350, 215, 4, "#000", "#000")
    svg += circle(370, 215, 4, "#000", "#000")
    svg += circle(360, 240, 4, "#000", "#000")
    
    # RIGHT: Low Level Modules (Plugs)
    
    # Option A
    svg += line(400, 225, 500, 150, "#9ca3af", 2, True)
    svg += rect(500, 120, 150, 60, "#dcfce7", "#16a34a")
    svg += text(575, 155, "MySQL DB", 14, "#14532d", "bold", "middle")
    
    # Option B
    svg += line(400, 225, 500, 225, "#9ca3af", 2, True)
    svg += rect(500, 195, 150, 60, "#fef3c7", "#d97706")
    svg += text(575, 230, "MongoDB", 14, "#78350f", "bold", "middle")
    
    # Option C
    svg += line(400, 225, 500, 300, "#9ca3af", 2, True)
    svg += rect(500, 270, 150, 60, "#fee2e2", "#dc2626")
    svg += text(575, 305, "Test Mock DB", 14, "#7f1d1d", "bold", "middle")
    
    svg += text(400, 360, "The Laptop doesn't care who powers it.", 16, "#374151", "italic", "middle")
    
    svg += "</svg>"
    save(filename, svg)

def generate_solid_card_svg(filename="solid_summary_card.svg"):
    width, height = 800, 600
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#111827;">'
    svg += f'<rect width="100%" height="100%" fill="#111827"/>'
    
    # Header
    svg += text(400, 60, "SOLID Principles Cheatsheet", 32, "#f3f4f6", "bold", "middle")
    svg += text(400, 95, "Architecture Requirements for Scalable Systems", 16, "#9ca3af", "normal", "middle")

    # Grid
    y_start = 140
    gap = 85
    
    data = [
        ("S", "Single Responsibility", "Startups Killer", "Don't create God Classes. Split by 'Actor'."),
        ("O", "Open/Closed", "Plugin Architecture", "Add features by adding files, not editing files."),
        ("L", "Liskov Substitution", "Trust The Type", "If it looks like a Duck, it better Quack."),
        ("I", "Interface Segregation", "Don't Be Greedy", "Split giant interfaces into small roles."),
        ("D", "Dependency Inversion", "Plug & Play", "Inject Dependencies. Depend on abstractions.")
    ]
    
    colors = ["#ef4444", "#eab308", "#22c55e", "#3b82f6", "#a855f7"]
    
    for i, (char, name, tag, desc) in enumerate(data):
        y = y_start + (i * gap)
        
        # Letter Box
        svg += rect(50, y, 70, 70, colors[i], colors[i])
        svg += text(85, y+50, char, 40, "#ffffff", "bold", "middle")
        
        # Text
        svg += text(140, y+25, name, 20, colors[i], "bold", "start")
        svg += text(140, y+55, desc, 16, "#d1d5db", "normal", "start")
        
        # Tag
        svg += rect(600, y+20, 160, 30, "#374151", "#4b5563")
        svg += text(680, y+40, tag, 12, "#e5e7eb", "bold", "middle")

    svg += text(400, 570, "Keep it SOLID. Keep it Scalable.", 14, "#6b7280", "italic", "middle")
    
    svg += "</svg>"
    save(filename, svg)

def generate_ocp_svg(filename="solid_ocp_sketch.svg"):
    width, height = 800, 450
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff;">'
    svg += f'<rect width="100%" height="100%" fill="#ffffff"/>'
    
    svg += text(400, 40, "OCP: Open/Closed Principle", 24, "#1f2937", "bold", "middle")
    svg += text(400, 70, "Open for Extension, Closed for Modification", 16, "#4b5563", "italic", "middle")
    
    # Core System (Closed Box)
    svg += rect(300, 150, 200, 150, "#f3f4f6", "#1f2937")
    svg += text(400, 200, "Core System", 18, "#111827", "bold", "middle")
    svg += text(400, 230, "(tested & stable)", 14, "#4b5563", "normal", "middle")
    svg += text(400, 260, "🔒 CLOSED", 16, "#dc2626", "bold", "middle")
    
    # Plugins (Extensions)
    # 1. Top
    svg += rect(350, 80, 100, 50, "#dbeafe", "#2563eb")
    svg += text(400, 110, "Plugin A", 14, "#1e3a8a", "bold", "middle")
    svg += line(400, 130, 400, 150, "#2563eb", 3)
    
    # 2. Right
    svg += rect(550, 200, 100, 50, "#d1fae5", "#059669")
    svg += text(600, 230, "Plugin B", 14, "#064e3b", "bold", "middle")
    svg += line(500, 225, 550, 225, "#059669", 3)

    # 3. Left
    svg += rect(150, 200, 100, 50, "#fce7f3", "#db2777")
    svg += text(200, 230, "Plugin C", 14, "#831843", "bold", "middle")
    svg += line(250, 225, 300, 225, "#db2777", 3)
    
    # Label
    svg += text(400, 380, "✅ New features attach as 'Plugins'. We never open the Core box.", 16, "#059669", "bold", "middle")

    svg += "</svg>"
    save(filename, svg)

def generate_lsp_svg(filename="solid_lsp_sketch.svg"):
    width, height = 800, 500
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#fff1f2;">'
    svg += f'<rect width="100%" height="100%" fill="#fff1f2"/>'
    
    svg += text(400, 40, "LSP: The Substitution Trap", 24, "#881337", "bold", "middle")
    
    # Parent Class
    svg += rect(300, 100, 200, 80, "#e5e7eb", "#374151")
    svg += text(400, 130, "Parent: Bird", 18, "#111827", "bold", "middle")
    svg += text(400, 160, ".fly() ✅", 16, "#059669", "bold", "middle")
    
    # Child 1 (Good)
    svg += line(350, 180, 250, 250, "#9ca3af", 2)
    svg += rect(150, 250, 200, 80, "#dcfce7", "#16a34a")
    svg += text(250, 280, "Child: Sparrow", 16, "#14532d", "bold", "middle")
    svg += text(250, 310, ".fly() -> Flies away", 14, "#14532d", "normal", "middle")
    
    # Child 2 (Bad)
    svg += line(450, 180, 550, 250, "#9ca3af", 2)
    svg += rect(450, 250, 200, 80, "#fee2e2", "#dc2626")
    svg += text(550, 280, "Child: Ostrich/Toy", 16, "#7f1d1d", "bold", "middle")
    svg += text(550, 310, ".fly() -> CRASH! 💥", 14, "#dc2626", "bold", "middle")
    
    # Code snippet area
    svg += rect(200, 380, 400, 80, "#1f2937", "#000")
    svg += text(400, 410, "def make_bird_fly(bird):", 14, "#f3f4f6", "monospace", "middle")
    svg += text(400, 440, "    bird.fly() # Boom if Ostrich!", 14, "#f87171", "monospace", "middle")

    svg += "</svg>"
    save(filename, svg)

def generate_isp_svg(filename="solid_isp_sketch.svg"):
    width, height = 800, 500
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color:#f0f9ff;">'
    svg += f'<rect width="100%" height="100%" fill="#f0f9ff"/>'
    
    svg += text(400, 40, "ISP: Interface Segregation", 24, "#0c4a6e", "bold", "middle")
    
    # The Violation (Fat Interface)
    svg += text(200, 100, "❌ The 'Fat' Interface", 18, "#dc2626", "bold", "middle")
    
    svg += rect(100, 130, 200, 200, "#fee2e2", "#dc2626")
    svg += text(200, 160, "ISmartDevice", 16, "#7f1d1d", "bold", "middle")
    svg += line(100, 170, 300, 170, "#dc2626", 1)
    
    svg += text(120, 200, "- turn_on()", 14, "#7f1d1d", "normal", "start")
    svg += text(120, 230, "- turn_off()", 14, "#7f1d1d", "normal", "start")
    svg += text(120, 260, "- scan_document() 😨", 14, "#ef4444", "bold", "start")
    svg += text(120, 290, "- brew_coffee() 😨", 14, "#ef4444", "bold", "start")
    
    svg += text(200, 380, "Lightbulb forced to brew coffee?", 14, "#dc2626", "italic", "middle")


    # Attributes arrow
    svg += text(400, 230, "VS", 30, "#9ca3af", "bold", "middle")

    # The Solution (Segregated)
    svg += text(600, 100, "✅ Segregated roles", 18, "#059669", "bold", "middle")
    
    # Interface 1
    svg += rect(500, 130, 200, 80, "#d1fae5", "#059669")
    svg += text(600, 160, "ISwitchable", 14, "#064e3b", "bold", "middle")
    svg += text(600, 190, "(On / Off)", 12, "#064e3b", "normal", "middle")
    
    # Interface 2
    svg += rect(500, 230, 200, 80, "#dbeafe", "#2563eb")
    svg += text(600, 260, "IPrinter", 14, "#1e3a8a", "bold", "middle")
    svg += text(600, 290, "(Scan / Print)", 12, "#1e3a8a", "normal", "middle")

    svg += text(600, 380, "Classes only pick what they need.", 14, "#059669", "italic", "middle")

    svg += "</svg>"
    save(filename, svg)

# --- Helpers ---
def rect(x, y, w, h, fill, stroke):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="2" rx="8" />'

def circle(cx, cy, r, fill, stroke):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2" />'

def line(x1, y1, x2, y2, stroke="#000", w=2, dashed=False):
    dash = 'stroke-dasharray="5,5"' if dashed else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{w}" {dash} />'

def text(x, y, content, size, fill, weight, anchor):
    return f'<text x="{x}" y="{y}" font-family="Segoe UI, Verdana, sans-serif" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{content}</text>'

def save(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    create_solid_visuals()
