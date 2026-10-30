import re
import os

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    app_jsx = f.read()

# Make components directory
os.makedirs('src/components', exist_ok=True)

components = []

def extract_and_replace(pattern, comp_name, content, imports=[], is_main=False):
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return content
    
    comp_content = match.group(0)
    
    # Save component
    jsx = "import React from 'react';\n"
    if imports:
        jsx += "\n".join(imports) + "\n"
    
    jsx += f"\nconst {comp_name} = () => {{\n"
    
    # If this component needs toggleMobileNav (e.g. Navbar)
    if comp_name == "Navbar":
        jsx += """
  const toggleMobileNav = () => {
    const mobileNav = document.getElementById('mobileNav');
    const hamburger = document.getElementById('hamburger');
    if (mobileNav && hamburger) {
      const open = mobileNav.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', String(open));
      hamburger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
  };

  const closeMobileNav = () => {
    document.getElementById('mobileNav')?.classList.remove('open');
  };
"""
    
    jsx += f"  return (\n    {comp_content}\n  );\n}};\n\nexport default {comp_name};\n"
    
    with open(f'src/components/{comp_name}.jsx', 'w', encoding='utf-8') as f:
        f.write(jsx)
        
    components.append(comp_name)
    
    # Replace in content
    return content.replace(comp_content, f"<{comp_name} />")

# The order of extraction matters, from inside out or sequentially
# We have <header>, sections inside <main>, <footer>, wa-float
new_app = app_jsx

# Extract SVG Symbols
new_app = extract_and_replace(r'<svg width="0" height="0".*?</svg>', 'SvgSymbols', new_app)

# Extract Header/Navbar
new_app = extract_and_replace(r'<header>.*?</header>', 'Navbar', new_app)

# Extract Footer
new_app = extract_and_replace(r'<footer>.*?</footer>', 'Footer', new_app)

# Extract WhatsApp Float
new_app = extract_and_replace(r'<a className="wa-float".*?</a>', 'WhatsAppFloat', new_app)

# Extract Sections inside main
sections = [
    (r'<section id="hero">.*?</section>', 'Hero'),
    (r'<section id="why">.*?</section>', 'Why'),
    (r'<section id="about">.*?</section>', 'About'),
    (r'<section id="courses">.*?</section>', 'Courses'),
    (r'<section id="ai-solutions">.*?</section>', 'AiSolutions'),
    (r'<section id="ev">.*?</section>', 'EvEngineering'),
    (r'<section id="consulting">.*?</section>', 'Consulting'),
    (r'<section id="corporate">.*?</section>', 'CorporateTraining'),
    (r'<section id="process">.*?</section>', 'Process'),
    (r'<section id="industries">.*?</section>', 'Industries'),
    (r'<section id="hub">.*?</section>', 'KnowledgeHub'),
    (r'<section id="blog">.*?</section>', 'Blog'),
    (r'<section id="testimonials">.*?</section>', 'Testimonials'),
    (r'<section id="founder">.*?</section>', 'Founder'),
    (r'<section id="careers">.*?</section>', 'Careers'),
    (r'<section id="contact">.*?</section>', 'Contact'),
]

for pattern, name in sections:
    new_app = extract_and_replace(pattern, name, new_app)

# Clean up App.jsx
# Remove toggleMobileNav and closeMobileNav from App.jsx
new_app = re.sub(r'const toggleMobileNav = \(\) => \{.*?\};\n\n  const closeMobileNav = \(\) => \{.*?\};\n', '', new_app, flags=re.DOTALL)

# Add imports to App.jsx
import_statements = "\n".join([f"import {comp} from './components/{comp}';" for comp in components])
new_app = new_app.replace("import { useEffect } from 'react';", f"import {{ useEffect }} from 'react';\n{import_statements}")

# Write back App.jsx
with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(new_app)

print("Split components successfully!")
