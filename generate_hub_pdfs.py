"""
Generate 2-page PDF resources for each JC Tech Knowledge Hub topic.
Each PDF is beautifully formatted with JC Tech branding.
"""

from fpdf import FPDF
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "public", "pdfs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# JC Tech brand colors
NAVY = (11, 30, 68)
ORANGE = (255, 106, 31)
DARK_TEXT = (30, 30, 40)
GREY_TEXT = (80, 80, 90)
LIGHT_BG = (245, 247, 250)
WHITE = (255, 255, 255)


class JCTechPDF(FPDF):
    """Custom PDF class with JC Tech branding."""

    def __init__(self, title, subtitle):
        super().__init__()
        self.doc_title = title
        self.doc_subtitle = subtitle

    def header(self):
        # Navy header bar
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 18, "F")
        # Orange accent line
        self.set_fill_color(*ORANGE)
        self.rect(0, 18, 210, 2.5, "F")
        # Brand name in header
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 10)
        self.set_xy(10, 5)
        self.cell(0, 8, "JC TECH  |  Engineering. Intelligence. Innovation.", align="L")
        self.set_xy(-60, 5)
        self.cell(50, 8, "www.jctech.co.in", align="R")
        self.ln(20)

    def footer(self):
        self.set_y(-18)
        self.set_fill_color(*NAVY)
        self.rect(0, self.get_y() + 5, 210, 15, "F")
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "", 8)
        self.cell(0, 12, f"JC Tech Knowledge Hub  |  {self.doc_title}  |  Page {self.page_no()}/{{nb}}", align="C")

    def add_title_section(self):
        """Add the big title block on page 1."""
        self.set_fill_color(*LIGHT_BG)
        self.rect(10, 28, 190, 38, "F")
        # Title
        self.set_xy(16, 32)
        self.set_text_color(*NAVY)
        self.set_font("Helvetica", "B", 22)
        self.cell(0, 12, self.doc_title)
        # Subtitle
        self.set_xy(16, 46)
        self.set_text_color(*ORANGE)
        self.set_font("Helvetica", "I", 11)
        self.cell(0, 8, self.doc_subtitle)
        # Orange bar under title
        self.set_fill_color(*ORANGE)
        self.rect(16, 62, 50, 2, "F")
        self.ln(46)

    def section_heading(self, text):
        self.ln(5)
        self.set_text_color(*NAVY)
        self.set_font("Helvetica", "B", 13)
        self.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        # Small orange underline
        x = self.get_x()
        y = self.get_y()
        self.set_fill_color(*ORANGE)
        self.rect(x, y, 30, 1.2, "F")
        self.ln(5)

    def body_text(self, text):
        self.set_text_color(*DARK_TEXT)
        self.set_font("Helvetica", "", 10.5)
        self.multi_cell(0, 6.2, text)
        self.ln(2)

    def bullet_list(self, items):
        self.set_text_color(*GREY_TEXT)
        self.set_font("Helvetica", "", 10)
        for item in items:
            x = self.get_x()
            self.set_fill_color(*ORANGE)
            self.rect(x + 2, self.get_y() + 2, 2.5, 2.5, "F")
            self.set_x(x + 8)
            self.multi_cell(170, 6, item)
            self.ln(1.5)

    def key_value_box(self, pairs):
        """Render a shaded box with key-value pairs."""
        self.set_fill_color(*LIGHT_BG)
        start_y = self.get_y()
        self.rect(14, start_y, 182, len(pairs) * 8 + 8, "F")
        self.set_xy(18, start_y + 4)
        for key, val in pairs:
            self.set_text_color(*NAVY)
            self.set_font("Helvetica", "B", 10)
            self.cell(50, 7, key + ":")
            self.set_text_color(*DARK_TEXT)
            self.set_font("Helvetica", "", 10)
            self.cell(0, 7, val, new_x="LMARGIN", new_y="NEXT")
            self.set_x(18)
        self.ln(6)


def create_engineering_encyclopedia():
    pdf = JCTechPDF("Engineering Encyclopedia", "A Comprehensive Reference for Modern Engineers")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=25)

    # PAGE 1
    pdf.add_page()
    pdf.add_title_section()

    pdf.section_heading("What is the Engineering Encyclopedia?")
    pdf.body_text(
        "The JC Tech Engineering Encyclopedia is a curated, ever-growing digital reference that spans "
        "the core disciplines of modern engineering. From fundamental mechanical principles to cutting-edge "
        "AI-driven manufacturing, this encyclopedia is designed to be the single source of truth for "
        "practicing engineers, students, and technical decision-makers."
    )

    pdf.section_heading("Core Disciplines Covered")
    pdf.bullet_list([
        "Mechanical Engineering: Thermodynamics, fluid mechanics, machine design, vibration analysis, and material science.",
        "Electrical & Electronics: Circuit theory, power systems, embedded systems, signal processing, and control theory.",
        "Manufacturing & Production: CNC machining, additive manufacturing, casting, forging, welding, and quality control (Six Sigma, SPC).",
        "Automotive & EV Engineering: Powertrain design, battery technology, motor controllers, regenerative braking, and thermal management.",
        "Computer-Aided Engineering: FEA, CFD, topology optimization, CAD/CAM workflows, and simulation-driven design.",
        "AI & Automation in Engineering: Machine learning for predictive maintenance, generative design, robotic process automation, and digital twins.",
    ])

    pdf.section_heading("How to Use This Resource")
    pdf.body_text(
        "Each topic in the encyclopedia includes a concise definition, mathematical formulations where applicable, "
        "real-world application examples, and references to industry standards (ISO, ASME, SAE, BIS). "
        "Engineers can search by keyword, browse by discipline, or follow curated learning paths."
    )

    # PAGE 2
    pdf.add_page()
    pdf.section_heading("Featured Topics (Sample Entries)")

    pdf.key_value_box([
        ("Stress-Strain Curve", "Relationship between applied force and material deformation; elastic vs. plastic region."),
        ("Reynolds Number", "Dimensionless ratio predicting laminar vs. turbulent flow (Re = rho * v * D / mu)."),
        ("GD&T (Geometric Dimensioning)", "ASME Y14.5 standard for defining tolerances on engineering drawings."),
        ("Regenerative Braking", "Energy recovery system converting kinetic energy back to electrical storage in EVs."),
    ])

    pdf.section_heading("Why JC Tech Built This")
    pdf.body_text(
        "Most engineering references online are fragmented, outdated, or hidden behind paywalls. "
        "We built the Engineering Encyclopedia to democratize technical knowledge. Whether you are a "
        "fresh graduate preparing for interviews or a senior engineer refreshing a concept before a design review, "
        "this resource saves you time and ensures accuracy."
    )

    pdf.section_heading("Key Statistics")
    pdf.bullet_list([
        "500+ engineering terms and definitions curated by industry experts.",
        "Covers 6 major engineering disciplines with cross-references.",
        "Updated quarterly with new topics and industry trends.",
        "Used by 10,000+ engineers and students worldwide.",
    ])

    pdf.section_heading("Access & Updates")
    pdf.body_text(
        "The Engineering Encyclopedia is freely available through the JC Tech Knowledge Hub. "
        "Subscribe to our newsletter for quarterly updates, or contact us for custom enterprise editions "
        "tailored to your organization's technical domains.\n\n"
        "Visit: www.jctech.co.in | Email: info@jctech.co.in"
    )

    pdf.output(os.path.join(OUTPUT_DIR, "engineering-encyclopedia.pdf"))
    print("  [OK] engineering-encyclopedia.pdf")


def create_ev_component_database():
    pdf = JCTechPDF("EV Component Database", "Your Complete Reference for Electric Vehicle Components")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=25)

    # PAGE 1
    pdf.add_page()
    pdf.add_title_section()

    pdf.section_heading("Overview")
    pdf.body_text(
        "The JC Tech EV Component Database is a meticulously organized catalog of every critical component "
        "in modern electric vehicles. Designed for automotive engineers, EV startups, procurement teams, and "
        "students, this database provides specifications, supplier information, design considerations, and "
        "comparative data for informed decision-making in EV development."
    )

    pdf.section_heading("Component Categories")
    pdf.bullet_list([
        "Battery Systems: Li-ion cells (NMC, LFP, NCA), battery packs, BMS (Battery Management System), thermal management modules, and cell balancing circuits.",
        "Electric Motors: BLDC, PMSM, induction motors, switched reluctance motors -- torque curves, efficiency maps, and cooling strategies.",
        "Power Electronics: DC-DC converters, onboard chargers (OBC), inverters (IGBT/SiC/GaN), and high-voltage distribution units (PDU).",
        "Charging Infrastructure: AC Level 1/2, DC fast charging (CCS, CHAdeMO, GB/T), wireless charging pads, and V2G (Vehicle-to-Grid) systems.",
        "Drivetrain & Transmission: Single-speed reducers, multi-speed transmissions, differential units, and half-shaft assemblies for EV applications.",
        "Auxiliary Systems: Electric power steering (EPS), electric AC compressors, 12V accessory batteries, and regenerative braking controllers.",
    ])

    pdf.section_heading("Data Fields Per Component")
    pdf.key_value_box([
        ("Specifications", "Voltage, current, power rating, weight, dimensions, operating temperature range."),
        ("Suppliers", "OEM and tier-1 supplier list with region availability and lead times."),
        ("Standards", "Compliance info -- AIS 156, ISO 6469, IEC 61851, SAE J1772, UN ECE R100."),
        ("Cost Estimate", "Approximate unit pricing at volume tiers (100, 1K, 10K units)."),
    ])

    # PAGE 2
    pdf.add_page()
    pdf.section_heading("Sample Entry: Lithium Iron Phosphate (LFP) Cell")
    pdf.key_value_box([
        ("Chemistry", "LiFePO4 (LFP)"),
        ("Nominal Voltage", "3.2V per cell"),
        ("Energy Density", "90-160 Wh/kg"),
        ("Cycle Life", "2000-5000 cycles at 80% DoD"),
        ("Thermal Runaway Risk", "Very Low (inherently stable cathode)"),
        ("Common Suppliers", "CATL, BYD, EVE Energy, Gotion High-Tech"),
        ("Applications", "Electric buses, commercial EVs, energy storage systems"),
    ])

    pdf.section_heading("How Engineers Use This Database")
    pdf.body_text(
        "1. Component Selection: Compare multiple components side-by-side using spec sheets.\n"
        "2. Design Validation: Cross-reference component specs with vehicle-level requirements.\n"
        "3. Supplier Scouting: Identify and evaluate suppliers for procurement negotiations.\n"
        "4. Learning & Training: Students and junior engineers use entries as study material for EV systems."
    )

    pdf.section_heading("Database Growth & Roadmap")
    pdf.bullet_list([
        "Current: 350+ components across 6 major categories.",
        "Q1 2027: Adding fuel cell components and hydrogen storage systems.",
        "Q2 2027: Interactive comparison tool on the JC Tech web platform.",
        "Ongoing: Community contributions from EV engineers worldwide.",
    ])

    pdf.section_heading("Get Involved")
    pdf.body_text(
        "The EV Component Database is a living resource. If you are a component manufacturer or an EV engineer "
        "with expertise, we invite you to contribute data and reviews. Contact us to become a knowledge partner.\n\n"
        "Visit: www.jctech.co.in | Email: ev@jctech.co.in"
    )

    pdf.output(os.path.join(OUTPUT_DIR, "ev-component-database.pdf"))
    print("  [OK] ev-component-database.pdf")


def create_cad_standards_library():
    pdf = JCTechPDF("CAD Standards Library", "Industry-Grade Drafting & Modeling Standards for Engineers")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=25)

    # PAGE 1
    pdf.add_page()
    pdf.add_title_section()

    pdf.section_heading("Purpose of the CAD Standards Library")
    pdf.body_text(
        "Inconsistent CAD practices cost companies thousands of hours in rework, miscommunication, and "
        "manufacturing errors. The JC Tech CAD Standards Library provides a unified set of rules, templates, "
        "and best practices for 2D drafting and 3D modeling that align with international standards "
        "(ISO 128, ASME Y14.5, BIS SP 46) and industry best practices from automotive, aerospace, and "
        "heavy machinery sectors."
    )

    pdf.section_heading("What's Included")
    pdf.bullet_list([
        "Drawing Templates: Pre-configured title blocks, border layouts, and layer standards for AutoCAD, SolidWorks, CATIA, and Creo.",
        "GD&T Quick Reference: Complete symbol library with application rules per ASME Y14.5-2018 and ISO 1101.",
        "Dimensioning Standards: Rules for linear, angular, radial, and ordinate dimensioning with tolerance callouts.",
        "Part Numbering Systems: Intelligent and sequential part numbering conventions for assembly management.",
        "Revision Control: Standards for revision blocks, ECN (Engineering Change Notice) workflows, and version tracking.",
        "3D Modeling Best Practices: Feature tree organization, reference geometry naming, multi-body vs. assembly strategies.",
    ])

    pdf.section_heading("Supported CAD Platforms")
    pdf.key_value_box([
        ("2D Drafting", "AutoCAD, DraftSight, LibreCAD"),
        ("3D Parametric", "SolidWorks, CATIA V5/V6, Creo Parametric, Siemens NX"),
        ("Simulation", "ANSYS Mechanical, Abaqus, SimScale"),
        ("Data Exchange", "STEP (AP214/AP242), IGES, JT, 3D PDF"),
    ])

    # PAGE 2
    pdf.add_page()
    pdf.section_heading("Sample Standard: Drawing Layer Convention")
    pdf.key_value_box([
        ("0-GEOMETRY", "Primary part geometry (visible edges) -- Color: White, Lineweight: 0.35mm"),
        ("1-HIDDEN", "Hidden lines -- Color: Grey (8), Linetype: HIDDEN, Lineweight: 0.18mm"),
        ("2-CENTER", "Center lines and axes -- Color: Red, Linetype: CENTER, Lineweight: 0.18mm"),
        ("3-DIMENSION", "All dimensions and tolerances -- Color: Green, Lineweight: 0.25mm"),
        ("4-HATCH", "Section hatching and fill patterns -- Color: Yellow, Lineweight: 0.18mm"),
        ("5-TEXT", "Notes, callouts, and annotations -- Color: Cyan, Lineweight: 0.25mm"),
    ])

    pdf.section_heading("Why Standards Matter in CAD")
    pdf.body_text(
        "A 2023 industry survey revealed that 67% of manufacturing defects traceable to design originated from "
        "ambiguous or non-standard drawings. CAD standards eliminate interpretation errors, speed up design reviews, "
        "enable seamless collaboration between teams and suppliers, and ensure regulatory compliance."
    )

    pdf.section_heading("Implementation Guide")
    pdf.bullet_list([
        "Step 1: Download the template pack for your CAD platform from the JC Tech Knowledge Hub.",
        "Step 2: Import templates into your CAD environment and set as default for new projects.",
        "Step 3: Train your team using the included quick-reference cards and video walkthroughs.",
        "Step 4: Establish a review checklist to audit drawings against the standard before release.",
    ])

    pdf.section_heading("Download & Support")
    pdf.body_text(
        "All templates and reference documents are available for free download. Enterprise clients can request "
        "customized standards aligned with their internal processes.\n\n"
        "Visit: www.jctech.co.in | Email: cad@jctech.co.in"
    )

    pdf.output(os.path.join(OUTPUT_DIR, "cad-standards-library.pdf"))
    print("  [OK] cad-standards-library.pdf")


def create_ai_for_engineers_blog():
    pdf = JCTechPDF("AI for Engineers Blog", "How Artificial Intelligence Is Transforming Engineering Practice")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=25)

    # PAGE 1
    pdf.add_page()
    pdf.add_title_section()

    pdf.section_heading("About the AI for Engineers Blog")
    pdf.body_text(
        "The AI for Engineers Blog by JC Tech bridges the gap between cutting-edge artificial intelligence research "
        "and practical engineering applications. Unlike generic AI blogs, every article is written from an engineer's "
        "perspective -- focusing on real-world implementation, tool reviews, workflow integration, and ROI analysis "
        "for manufacturing, design, and product development environments."
    )

    pdf.section_heading("Featured Article Categories")
    pdf.bullet_list([
        "Generative Design & Topology Optimization: How AI algorithms create lighter, stronger parts that humans wouldn't conceive.",
        "Predictive Maintenance with ML: Using sensor data and machine learning to predict equipment failures before they happen.",
        "AI-Powered Quality Inspection: Computer vision systems for automated defect detection on production lines.",
        "Natural Language Processing for Engineering: AI tools that search technical documents, auto-generate reports, and extract specs from datasheets.",
        "Digital Twins & Simulation: Creating AI-enhanced virtual replicas of physical systems for testing and optimization.",
        "AI in CAD/CAM: Smart feature recognition, automated dimensioning, and intelligent assembly constraint suggestion.",
    ])

    pdf.section_heading("Recent Highlights")
    pdf.key_value_box([
        ("Article", "How AI Is Changing Drawing Search on the Shop Floor"),
        ("Published", "October 2026"),
        ("Summary", "Explores AI systems that let operators search CAD databases using natural language queries."),
        ("Impact", "60% reduction in drawing retrieval time reported by pilot customers."),
    ])

    # PAGE 2
    pdf.add_page()
    pdf.section_heading("Why Engineers Need AI Literacy")
    pdf.body_text(
        "The World Economic Forum estimates that 85% of engineering roles will require AI competency by 2030. "
        "Yet most engineers receive zero AI training in their degree programs. The AI for Engineers Blog fills "
        "this critical gap by providing:\n\n"
        "- Jargon-free explanations of ML concepts relevant to engineering.\n"
        "- Step-by-step tutorials using Python, TensorFlow, and industry-specific tools.\n"
        "- Case studies from Indian manufacturing and automotive companies.\n"
        "- Monthly tool reviews of AI-powered engineering software."
    )

    pdf.section_heading("Top 5 AI Tools Every Engineer Should Know")
    pdf.bullet_list([
        "ChatGPT / Claude / Gemini: For technical documentation, code generation, and research assistance.",
        "nTopology: AI-driven generative design for lattice structures and lightweight components.",
        "Cognex ViDi: Deep learning-based visual inspection for manufacturing quality control.",
        "MATLAB + AI Toolbox: Signal processing, predictive modeling, and control system optimization.",
        "Autodesk Fusion 360 AI: Generative design, automated mesh refinement, and cloud simulation.",
    ])

    pdf.section_heading("Contributing to the Blog")
    pdf.body_text(
        "We welcome guest articles from practicing engineers who have implemented AI solutions in their workflows. "
        "Share your experience, challenges, and results with the JC Tech community. Published authors receive "
        "recognition on our platform and professional networking opportunities."
    )

    pdf.section_heading("Stay Updated")
    pdf.body_text(
        "New articles are published every week. Subscribe to the JC Tech newsletter for direct delivery "
        "to your inbox, or follow us on LinkedIn for daily AI + Engineering insights.\n\n"
        "Visit: www.jctech.co.in/blog | Email: blog@jctech.co.in"
    )

    pdf.output(os.path.join(OUTPUT_DIR, "ai-for-engineers-blog.pdf"))
    print("  [OK] ai-for-engineers-blog.pdf")


def create_engineering_tools():
    pdf = JCTechPDF("Engineering Tools", "Essential Digital Tools & Utilities for Modern Engineers")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=25)

    # PAGE 1
    pdf.add_page()
    pdf.add_title_section()

    pdf.section_heading("What Are JC Tech Engineering Tools?")
    pdf.body_text(
        "JC Tech Engineering Tools is a curated collection of free digital utilities designed to solve everyday "
        "engineering problems quickly and accurately. From unit converters and material selectors to stress "
        "calculators and tolerance stack-up analyzers, these tools eliminate manual calculations and reduce "
        "design errors. Every tool is validated against textbook solutions and industry-standard software."
    )

    pdf.section_heading("Tool Categories")
    pdf.bullet_list([
        "Unit Conversion Suite: Comprehensive converter covering SI, Imperial, and engineering-specific units (torque, pressure, flow rate, hardness).",
        "Material Property Lookup: Searchable database of mechanical properties (yield strength, UTS, modulus, density, CTE) for 200+ materials.",
        "Stress & Deflection Calculators: Beam bending, torsion, column buckling, pressure vessel, and contact stress calculations.",
        "Tolerance Stack-Up Analyzer: Worst-case and statistical (RSS) tolerance analysis for multi-part assemblies.",
        "Gear Design Calculator: Spur, helical, and bevel gear sizing with Lewis beam strength and AGMA methodology.",
        "Fastener Selection Guide: Bolt grade selection, torque-tension calculator, and thread engagement depth validator.",
    ])

    pdf.section_heading("How It Works")
    pdf.body_text(
        "Each tool provides a clean input interface where you enter your known values. The tool performs "
        "validated calculations and displays results with full formula breakdowns, unit labels, and "
        "applicable standard references. Results can be exported as PDF reports for documentation."
    )

    # PAGE 2
    pdf.add_page()
    pdf.section_heading("Featured Tool: Beam Deflection Calculator")
    pdf.key_value_box([
        ("Supported Beams", "Simply supported, cantilever, fixed-fixed, overhanging, continuous"),
        ("Load Types", "Point load, UDL, triangular, moment, combined loading"),
        ("Outputs", "Max deflection, slope, bending moment diagram, shear force diagram"),
        ("Standards", "Validated against Timoshenko & Gere, Roark's Formulas for Stress & Strain"),
        ("Export", "PDF report with diagrams and calculation steps"),
    ])

    pdf.section_heading("Featured Tool: Tolerance Stack-Up Analyzer")
    pdf.key_value_box([
        ("Methods", "Worst-case arithmetic, Root Sum of Squares (RSS), Monte Carlo simulation"),
        ("Inputs", "Nominal dimension, tolerance, distribution type per component"),
        ("Outputs", "Assembly gap/interference, Cpk prediction, probability of fit"),
        ("Use Case", "Multi-part assembly validation before prototyping"),
    ])

    pdf.section_heading("Upcoming Tools (Roadmap)")
    pdf.bullet_list([
        "Weld Strength Calculator (AWS D1.1 compliant) -- Q1 2027",
        "Thermal Expansion Interference Fit Calculator -- Q1 2027",
        "Fatigue Life Estimator (S-N curve and Miner's Rule) -- Q2 2027",
        "Hydraulic Cylinder Sizing Tool -- Q2 2027",
        "Spring Design Calculator (compression, extension, torsion) -- Q3 2027",
    ])

    pdf.section_heading("Access the Tools")
    pdf.body_text(
        "All Engineering Tools are available free of charge through the JC Tech Knowledge Hub. "
        "No login required for basic tools; advanced features available with a free JC Tech account. "
        "Enterprise API access is available for companies wanting to embed these calculators into their "
        "internal engineering portals.\n\n"
        "Visit: www.jctech.co.in/tools | Email: tools@jctech.co.in"
    )

    pdf.output(os.path.join(OUTPUT_DIR, "engineering-tools.pdf"))
    print("  [OK] engineering-tools.pdf")


if __name__ == "__main__":
    print("Generating JC Tech Knowledge Hub PDFs...")
    create_engineering_encyclopedia()
    create_ev_component_database()
    create_cad_standards_library()
    create_ai_for_engineers_blog()
    create_engineering_tools()
    print("\nAll 5 PDFs generated successfully in:", OUTPUT_DIR)
