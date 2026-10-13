"""
generate_blog_pdfs.py
Generates high-fidelity, professional PDF whitepapers/articles for JC Tech blog section.
"""

import os
import pymupdf

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "public", "blogs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Page geometry (A4)
PAGE_W = 595.28
PAGE_H = 841.89
M_LEFT = 54.0
M_RIGHT = 54.0
M_TOP = 50.0
M_BOTTOM = 52.0
CONTENT_W = PAGE_W - M_LEFT - M_RIGHT
MAX_Y = PAGE_H - M_BOTTOM

# Colors (RGB normalized 0.0 - 1.0)
C_NAVY_DARK = (7/255, 19/255, 49/255)       # #071331
C_NAVY_HEAD = (11/255, 30/255, 68/255)      # #0B1E44
C_ORANGE = (255/255, 122/255, 47/255)       # #FF7A2F
C_ORANGE_DARK = (224/255, 86/255, 22/255)   # #E05616
C_TEXT = (45/255, 55/255, 72/255)           # #2D3748
C_MUTED = (100/255, 116/255, 139/255)       # #64748B
C_BORDER = (226/255, 232/255, 240/255)      # #E2E8F0
C_BOX_BG = (255/255, 247/255, 237/255)      # #FFF7ED
C_BOX_BORDER = (254/255, 215/255, 170/255)  # #FED7AA
C_BADGE_BG = (255/255, 241/255, 232/255)    # #FFF1E8


class ArticleBuilder:
    def __init__(self, category, title, subtitle, filename, short_title):
        self.category = category
        self.title = title
        self.subtitle = subtitle
        self.filename = filename
        self.short_title = short_title
        self.doc = pymupdf.open()
        self.current_page = None
        self.cur_y = M_TOP

    def _add_page(self):
        page = self.doc.new_page(width=PAGE_W, height=PAGE_H)
        self.current_page = page
        is_first = (len(self.doc) == 1)

        # Top border accent bar
        page.draw_rect(pymupdf.Rect(M_LEFT, 24, PAGE_W - M_RIGHT, 27), fill=C_ORANGE, color=None)

        if not is_first:
            # Running header for page 2+
            page.insert_text(pymupdf.Point(M_LEFT, 42), "JC TECH  •  TECHNICAL ARTICLE", fontname="helv", fontsize=8, color=C_MUTED)
            page.insert_text(pymupdf.Point(PAGE_W - M_RIGHT - 180, 42), self.short_title, fontname="helv", fontsize=8, color=C_MUTED)
            page.draw_line(pymupdf.Point(M_LEFT, 48), pymupdf.Point(PAGE_W - M_RIGHT, 48), color=C_BORDER, width=0.6)
            self.cur_y = 66
        else:
            self.cur_y = 38

        return page

    def _ensure_space(self, needed_height):
        if self.current_page is None or (self.cur_y + needed_height > MAX_Y):
            self._add_page()

    def draw_header(self):
        page = self._add_page()

        # Top Brand Bar
        page.insert_text(pymupdf.Point(M_LEFT, self.cur_y + 16), "JC TECH", fontname="hebo", fontsize=18, color=C_NAVY_DARK)
        page.insert_text(pymupdf.Point(M_LEFT + 86, self.cur_y + 14), "ENGINEERING INTELLIGENCE", fontname="hebo", fontsize=8.5, color=C_ORANGE)
        page.insert_text(pymupdf.Point(PAGE_W - M_RIGHT - 140, self.cur_y + 14), "ARTICLE & WHITEPAPER", fontname="helv", fontsize=8, color=C_MUTED)

        self.cur_y += 26
        page.draw_line(pymupdf.Point(M_LEFT, self.cur_y), pymupdf.Point(PAGE_W - M_RIGHT, self.cur_y), color=C_BORDER, width=0.8)
        self.cur_y += 16

        # Category Badge
        cat_text = f"  {self.category.upper()}  "
        cat_w = pymupdf.get_text_length(cat_text, fontname="hebo", fontsize=8) + 12
        page.draw_rect(pymupdf.Rect(M_LEFT, self.cur_y, M_LEFT + cat_w, self.cur_y + 16), fill=C_BADGE_BG, color=C_ORANGE, width=0.6)
        page.insert_text(pymupdf.Point(M_LEFT + 6, self.cur_y + 11.5), self.category.upper(), fontname="hebo", fontsize=8, color=C_ORANGE_DARK)
        self.cur_y += 24

        # Title
        title_rect = pymupdf.Rect(M_LEFT, self.cur_y, PAGE_W - M_RIGHT, self.cur_y + 60)
        rem = page.insert_textbox(title_rect, self.title, fontname="hebo", fontsize=18, color=C_NAVY_DARK, lineheight=1.2)
        used_title = (title_rect.height - rem) if rem >= 0 else 48
        self.cur_y += used_title + 8

        # Subtitle
        sub_rect = pymupdf.Rect(M_LEFT, self.cur_y, PAGE_W - M_RIGHT, self.cur_y + 40)
        rem = page.insert_textbox(sub_rect, self.subtitle, fontname="hebi", fontsize=11, color=C_MUTED, lineheight=1.25)
        used_sub = (sub_rect.height - rem) if rem >= 0 else 24
        self.cur_y += used_sub + 12

        # Metadata Bar
        page.draw_rect(pymupdf.Rect(M_LEFT, self.cur_y, PAGE_W - M_RIGHT, self.cur_y + 22), fill=(0.97, 0.98, 0.99), color=C_BORDER, width=0.5)
        meta_txt = "Published by JC Tech  •  Industry Insights Series  •  www.jctech.co.in"
        page.insert_text(pymupdf.Point(M_LEFT + 10, self.cur_y + 14), meta_txt, fontname="helv", fontsize=8, color=C_MUTED)
        self.cur_y += 32

    def add_section_heading(self, heading_text):
        self._ensure_space(42)
        self.cur_y += 10
        # Draw small vertical accent bar
        self.current_page.draw_rect(pymupdf.Rect(M_LEFT, self.cur_y, M_LEFT + 3.5, self.cur_y + 13), fill=C_ORANGE, color=None)

        h_rect = pymupdf.Rect(M_LEFT + 10, self.cur_y - 2, PAGE_W - M_RIGHT, self.cur_y + 25)
        rem = self.current_page.insert_textbox(h_rect, heading_text, fontname="hebo", fontsize=12.5, color=C_NAVY_HEAD, lineheight=1.1)
        used = (h_rect.height - rem) if rem >= 0 else 18
        self.cur_y += used + 6

    def add_subheading(self, subhead_text):
        self._ensure_space(28)
        self.cur_y += 6
        rect = pymupdf.Rect(M_LEFT, self.cur_y, PAGE_W - M_RIGHT, self.cur_y + 24)
        rem = self.current_page.insert_textbox(rect, subhead_text, fontname="hebo", fontsize=10.5, color=C_NAVY_DARK, lineheight=1.15)
        used = (rect.height - rem) if rem >= 0 else 16
        self.cur_y += used + 4

    def add_paragraph(self, text):
        # Estimate text height: ~10pt font, 14pt leading, ~95 chars per line
        est_lines = max(1, len(text) / 88)
        est_height = est_lines * 14.5 + 8

        # If it doesn't fit on current page and we are near the bottom, advance page
        if self.cur_y + min(est_height, 45) > MAX_Y:
            self._add_page()

        rect = pymupdf.Rect(M_LEFT, self.cur_y, PAGE_W - M_RIGHT, MAX_Y)
        rem = self.current_page.insert_textbox(rect, text, fontname="helv", fontsize=9.5, color=C_TEXT, lineheight=1.4)

        if rem >= 0:
            used = rect.height - rem
            self.cur_y += used + 7
        else:
            # Overflows page: split or put on next page
            self._add_page()
            rect = pymupdf.Rect(M_LEFT, self.cur_y, PAGE_W - M_RIGHT, MAX_Y)
            rem = self.current_page.insert_textbox(rect, text, fontname="helv", fontsize=9.5, color=C_TEXT, lineheight=1.4)
            used = (rect.height - rem) if rem >= 0 else 30
            self.cur_y += used + 7

    def add_bullet(self, bold_prefix, text_body):
        self._ensure_space(24)
        # Bullet circle
        bullet_y = self.cur_y + 6.5
        self.current_page.draw_circle(pymupdf.Point(M_LEFT + 6, bullet_y), 2.2, fill=C_ORANGE, color=None)

        full_text = f"{bold_prefix} {text_body}" if bold_prefix else text_body
        rect = pymupdf.Rect(M_LEFT + 16, self.cur_y, PAGE_W - M_RIGHT, MAX_Y)
        rem = self.current_page.insert_textbox(rect, full_text, fontname="helv", fontsize=9.5, color=C_TEXT, lineheight=1.35)
        used = (rect.height - rem) if rem >= 0 else 20
        self.cur_y += used + 5

    def add_callout_box(self, text, title="KEY TAKEAWAY"):
        box_w = CONTENT_W
        # Estimate box height
        est_lines = max(1, len(text) / 85)
        box_h = est_lines * 14 + 32
        self._ensure_space(box_h + 10)

        box_rect = pymupdf.Rect(M_LEFT, self.cur_y, M_LEFT + box_w, self.cur_y + box_h)
        # Draw background and border
        self.current_page.draw_rect(box_rect, fill=C_BOX_BG, color=C_BOX_BORDER, width=0.8)
        # Left thick accent bar
        self.current_page.draw_rect(pymupdf.Rect(M_LEFT, self.cur_y, M_LEFT + 4, self.cur_y + box_h), fill=C_ORANGE, color=None)

        # Title
        self.current_page.insert_text(pymupdf.Point(M_LEFT + 16, self.cur_y + 14), title, fontname="hebo", fontsize=8.5, color=C_ORANGE_DARK)

        # Text
        text_rect = pymupdf.Rect(M_LEFT + 16, self.cur_y + 19, M_LEFT + box_w - 14, self.cur_y + box_h - 6)
        self.current_page.insert_textbox(text_rect, text, fontname="hebi", fontsize=9.5, color=C_NAVY_DARK, lineheight=1.35)

        self.cur_y += box_h + 10

    def finalize(self):
        # Draw footers on all pages
        total_pages = len(self.doc)
        for i, page in enumerate(self.doc):
            p_num = i + 1
            footer_y = PAGE_H - 34
            # Divider
            page.draw_line(pymupdf.Point(M_LEFT, footer_y - 8), pymupdf.Point(PAGE_W - M_RIGHT, footer_y - 8), color=C_BORDER, width=0.6)
            # Left footer
            page.insert_text(pymupdf.Point(M_LEFT, footer_y), "© JC Tech  •  Learn from Real Industry Experience  •  support@jctech.co.in", fontname="helv", fontsize=8, color=C_MUTED)
            # Right footer
            p_txt = f"Page {p_num} of {total_pages}"
            page.insert_text(pymupdf.Point(PAGE_W - M_RIGHT - 52, footer_y), p_txt, fontname="hebo", fontsize=8, color=C_MUTED)

        out_path = os.path.join(OUTPUT_DIR, self.filename)
        self.doc.save(out_path)
        print(f"Generated: {out_path} ({total_pages} pages)")
        return out_path


# ==========================================
# BUILD ARTICLE 1: AI Drawing Search
# ==========================================
def build_article_1():
    ab = ArticleBuilder(
        category="AI for Engineering",
        title="How AI Is Changing Drawing Search on the Shop Floor",
        subtitle="A Practical Look at Why Search, Not Automation, Is AI's First Real Win in Manufacturing",
        filename="how-ai-is-changing-drawing-search.pdf",
        short_title="How AI Is Changing Drawing Search"
    )
    ab.draw_header()

    ab.add_paragraph(
        "In modern manufacturing, every second counts. Engineers, machine operators, and production teams regularly depend on technical drawings to understand component dimensions, tolerances, materials, and manufacturing requirements. However, finding the right drawing at the right time can be surprisingly difficult. With thousands of drawings stored across folders, shared drives, and legacy systems, searching for a specific document often becomes a time-consuming task. This is where Artificial Intelligence (AI) is making a meaningful difference—not by replacing workers or automating entire production lines, but by making information easier to find."
    )

    ab.add_section_heading("The Challenge of Finding the Right Drawing")
    ab.add_paragraph(
        "Manufacturing companies often maintain years of engineering drawings in different formats, including PDFs, scanned documents, CAD files, and printed archives. Traditional search systems rely heavily on filenames, part numbers, or manually entered keywords. If a drawing is saved under an unfamiliar name or contains handwritten notes, locating it can become a frustrating process."
    )
    ab.add_paragraph(
        "For example, an operator may need a drawing of a particular metal bracket but know only its shape, approximate dimensions, or intended application. A conventional search may fail because the operator does not know the exact part number. Delays in finding the correct drawing can interrupt workflows, reduce productivity, and increase the risk of using outdated information."
    )

    ab.add_section_heading("How AI Makes Drawing Search Smarter")
    ab.add_paragraph(
        "AI-powered drawing search changes the way manufacturing teams access technical information. Instead of relying exclusively on filenames, AI can analyze document content, recognize text through Optical Character Recognition (OCR), interpret technical symbols, and use visual similarity to identify relevant drawings."
    )
    ab.add_paragraph(
        "With natural-language search, a worker might enter a query such as \"Find the stainless-steel bracket with four mounting holes.\" The system can identify potentially relevant drawings based on available text, extracted metadata, and visual features. Depending on the system's capabilities, users may also search using part descriptions, dimensions, or an uploaded reference image."
    )
    ab.add_paragraph(
        "This approach makes engineering knowledge more accessible, even to employees who are unfamiliar with the original file structure. It can also reduce dependence on a few experienced employees who know exactly where older drawings are stored."
    )

    ab.add_section_heading("Why Search Comes Before Automation")
    ab.add_paragraph(
        "Automation is often presented as the ultimate goal of industrial AI. However, successful automation depends on reliable information. Machines and production systems cannot consistently make the right decisions if the underlying drawings, specifications, or revisions are difficult to locate."
    )
    ab.add_paragraph(
        "AI-powered search offers a practical starting point because it can work alongside existing manufacturing systems without requiring companies to redesign their entire production process. It helps employees retrieve information faster, supports better decision-making, and creates a foundation for future digital transformation."
    )
    ab.add_paragraph(
        "Of course, AI search is not infallible. Search results must be checked against approved engineering documents, revision histories, and applicable quality procedures before production begins. AI should help locate the right information, not replace engineering verification."
    )

    ab.add_section_heading("The Future of Drawing Search")
    ab.add_paragraph(
        "As AI technology advances, drawing search will become more contextual, visual, and integrated with manufacturing workflows. Engineers may be able to discover similar components, identify reusable designs, and access related manufacturing instructions from a single search interface."
    )
    ab.add_paragraph(
        "The first real win for AI on the shop floor may not be a fully autonomous factory. It may simply be helping a worker find the correct drawing in seconds instead of spending several minutes searching through folders."
    )

    ab.add_callout_box(
        "In manufacturing, productivity begins with information. When the right drawing is easier to find, the entire production process becomes more efficient, connected, and reliable.",
        title="CORE LESSON FOR MANUFACTURERS"
    )

    ab.finalize()


# ==========================================
# BUILD ARTICLE 2: Battery Management Systems
# ==========================================
def build_article_2():
    ab = ArticleBuilder(
        category="EV Engineering",
        title="Battery Management Systems, Explained for Design Engineers",
        subtitle="What Every Mechanical Engineer Should Know Before Their First EV Project",
        filename="battery-management-systems-explained.pdf",
        short_title="Battery Management Systems Explained"
    )
    ab.draw_header()

    ab.add_paragraph(
        "Electric vehicles (EVs) are transforming the automotive industry, creating new opportunities and challenges for mechanical engineers. While battery cells and electric motors receive much of the attention, one critical component ensures that an EV battery operates safely and efficiently: the Battery Management System (BMS). For mechanical engineers entering EV design, understanding how a BMS works is essential for developing reliable, durable, and high-performance battery systems."
    )

    ab.add_section_heading("What Is a Battery Management System?")
    ab.add_paragraph(
        "A Battery Management System is an electronic control system that monitors and manages a rechargeable battery pack. It measures important parameters such as voltage, current, and temperature to ensure that the battery operates within its permitted limits."
    )
    ab.add_paragraph(
        "A BMS helps prevent overcharging, excessive discharging, overheating, and other conditions that could damage battery cells or create safety risks. It also estimates the State of Charge (SoC), which indicates how much usable charge remains, and the State of Health (SoH), which reflects the battery's condition compared with its original performance."
    )
    ab.add_paragraph(
        "Although the BMS is primarily an electronic system, its performance depends heavily on mechanical design decisions."
    )

    ab.add_section_heading("Why Mechanical Engineers Need to Understand BMS")
    ab.add_paragraph(
        "Battery performance is not determined by electrical components alone. Temperature, vibration, packaging, cooling, and structural protection all influence battery reliability. Mechanical engineers play an important role in addressing these factors."
    )

    ab.add_subheading("1. Thermal Management")
    ab.add_paragraph(
        "Battery cells generate heat during charging and discharging. Excessive or uneven temperatures can accelerate degradation and, under severe conditions, contribute to thermal runaway. The BMS monitors cell temperatures and can request cooling, reduce charging or discharging power, or disconnect the battery when necessary. Mechanical engineers design the cooling plates, airflow paths, thermal interfaces, and enclosures that help maintain suitable operating temperatures."
    )

    ab.add_subheading("2. Battery Pack Design and Packaging")
    ab.add_paragraph(
        "A battery pack must fit within the vehicle while protecting its cells from impact, moisture, dust, and other environmental conditions. Engineers must consider enclosure materials, sealing, mounting points, service access, and available space for electrical and cooling components. The BMS also needs suitable locations for sensors, wiring, and control electronics."
    )

    ab.add_subheading("3. Cell Balancing and Battery Life")
    ab.add_paragraph(
        "Individual cells may develop small differences in voltage and capacity over time. Cell balancing helps manage these differences so that the pack can operate effectively within its limits. Mechanical engineers should understand how cell arrangement, thermal uniformity, and module construction affect the consistency of cell performance."
    )

    ab.add_subheading("4. Safety and Reliability")
    ab.add_paragraph(
        "Battery packs must withstand vibration, mechanical shock, and challenging operating environments. Mechanical design must account for structural strength, electrical insulation clearances, thermal barriers, and appropriate protection against external damage. The BMS provides monitoring and protective control, while the mechanical system helps prevent hazards from developing."
    )

    ab.add_section_heading("Key BMS Parameters to Know")
    ab.add_bullet("State of Charge (SoC):", "An estimate of the battery's remaining charge available for driving.")
    ab.add_bullet("State of Health (SoH):", "An estimate of the battery's condition, degradation, and ageing compared to factory baseline.")
    ab.add_bullet("State of Power (SoP):", "An estimate of the power the battery can safely deliver or accept under current temperature conditions.")
    ab.add_bullet("Cell Voltage:", "The voltage of an individual battery cell, continuously monitored to identify abnormal conditions.")
    ab.add_bullet("Temperature Monitoring:", "Thermistor arrays used to manage active cooling loops and protect cells against extremes.")
    ab.add_bullet("Thermal Runaway:", "An uncontrolled, self-heating exothermic reaction requiring rigorous physical barriers and isolation.")

    ab.add_section_heading("Building Better EV Battery Systems")
    ab.add_paragraph(
        "A successful EV battery design requires collaboration between mechanical, electrical, electronics, and software engineers. Mechanical engineers should understand the BMS sufficiently to translate its requirements into practical decisions about cooling, packaging, materials, sensors, and safety provisions."
    )
    ab.add_paragraph(
        "Before starting an EV project, become familiar with battery cell specifications, thermal simulation, cooling-system design, enclosure development, and relevant battery safety standards. Most importantly, treat the battery pack as an integrated system rather than a collection of separate components."
    )

    ab.add_callout_box(
        "The key takeaway: A Battery Management System protects and optimizes battery operation, but mechanical engineering makes that operation physically possible, thermally stable, and structurally reliable. Understanding both sides is a valuable first step toward designing safer and more efficient electric vehicles.",
        title="SYSTEM INTEGRATION PRINCIPLE"
    )

    ab.finalize()


# ==========================================
# BUILD ARTICLE 3: GD&T Mistakes
# ==========================================
def build_article_3():
    ab = ArticleBuilder(
        category="CAD & Engineering Design",
        title="GD&T Mistakes That Cost Manufacturers the Most",
        subtitle="The Tolerancing Errors Repeated Across Every Industry We Consult For",
        filename="gdt-mistakes-that-cost-manufacturers.pdf",
        short_title="GD&T Mistakes That Cost Manufacturers"
    )
    ab.draw_header()

    ab.add_paragraph(
        "In manufacturing, precision is everything. A component may look perfect on a drawing, yet fail to fit, function, or assemble correctly on the production floor. Often, the problem is not the machining process itself but how the component's requirements are communicated. Geometric Dimensioning and Tolerancing (GD&T) provides a standardized way to define the allowable variation in a part's geometry. However, when GD&T is applied incorrectly or misunderstood, it can lead to scrap, rework, inspection delays, and costly production failures."
    )
    ab.add_paragraph(
        "Understanding the most common GD&T mistakes is essential for design engineers, manufacturing teams, and quality professionals who want to improve product quality without increasing manufacturing costs unnecessarily."
    )

    ab.add_section_heading("1. Using Tolerances That Are Too Tight")
    ab.add_paragraph(
        "One of the most common mistakes is specifying tighter tolerances than a component's function actually requires. Although tighter tolerances may appear to guarantee better quality, they often demand specialized equipment, slower machining processes, and more frequent inspection."
    )
    ab.add_paragraph(
        "For example, specifying an unnecessarily tight positional tolerance for a non-critical mounting hole can increase production costs without improving the product's performance. Engineers should determine tolerances based on functional requirements, assembly conditions, and manufacturing capabilities."
    )
    ab.add_bullet("The lesson:", "Specify precision where it matters, not everywhere.")

    ab.add_section_heading("2. Choosing the Wrong Datums")
    ab.add_paragraph(
        "Datums establish the reference framework used to manufacture and inspect a component. If the selected datums do not reflect how the part is assembled or functions, inspection results may not represent real-world performance."
    )
    ab.add_paragraph(
        "For instance, a component located by three mounting surfaces during assembly should generally be toleranced using a datum scheme that reflects those functional interfaces. Choosing unrelated surfaces as datums can cause alignment problems and inconsistent measurements. Design engineers should understand how a component is positioned, constrained, and connected before defining its datum reference frame."
    )

    ab.add_section_heading("3. Confusing Position Tolerance With Coordinate Dimensions")
    ab.add_paragraph(
        "Traditional coordinate dimensions specify the location of individual features, but they do not always communicate the functional relationship between those features as effectively as GD&T."
    )
    ab.add_paragraph(
        "Position tolerance controls the permissible variation in a feature's location relative to a defined datum reference frame. Misusing it, or failing to establish the correct datum references, can result in holes that meet individual dimensional requirements but do not align during assembly. Clear feature control frames and appropriate datum references help reduce these problems."
    )

    ab.add_section_heading("4. Ignoring Material Condition Modifiers")
    ab.add_paragraph(
        "Maximum Material Condition (MMC) and Least Material Condition (LMC) modifiers can provide useful design flexibility when applied correctly. They allow certain geometric tolerances to vary according to the actual size of a feature."
    )
    ab.add_paragraph(
        "A common mistake is either overlooking these modifiers when they would be beneficial or applying them without understanding their functional implications. Incorrect use can create confusion during inspection and lead to unnecessary rejection or assembly issues."
    )

    ab.add_section_heading("5. Creating Drawings That Are Difficult to Inspect")
    ab.add_paragraph(
        "A drawing may communicate the design intent to its creator but remain ambiguous to machinists and quality inspectors. Missing datum references, unclear feature control frames, inconsistent dimensioning, and poorly defined inspection requirements can result in different interpretations of the same part."
    )
    ab.add_paragraph(
        "GD&T should communicate measurable requirements that can be verified using appropriate inspection methods, such as coordinate measuring machines (CMMs), gauges, or other suitable measurement equipment. Design reviews involving manufacturing and quality teams can identify these issues early."
    )

    ab.add_section_heading("The Real Cost of Poor GD&T & Conclusion")
    ab.add_paragraph(
        "The financial impact of tolerancing mistakes extends beyond a single rejected component. Incorrect requirements can lead to repeated machining, delayed assembly, inspection disputes, supplier disagreements, and engineering changes. When discovered late in production, these issues become exponentially more expensive to correct."
    )
    ab.add_paragraph(
        "GD&T is more than a collection of symbols on an engineering drawing. It is a communication system that connects design intent with manufacturing reality. Avoiding unnecessarily tight tolerances, selecting functional datums, applying modifiers correctly, and creating inspectable drawings can significantly improve product quality and production efficiency."
    )

    ab.add_callout_box(
        "The most effective tolerancing strategy is not the tightest tolerance possible—it is the right tolerance for the function, manufacturing process, and inspection method.",
        title="TOLERANCING STRATEGY RULE"
    )

    ab.finalize()


if __name__ == "__main__":
    print("Generating JC Tech Blog Whitepaper PDFs...")
    build_article_1()
    build_article_2()
    build_article_3()
    print("All PDFs successfully generated!")
