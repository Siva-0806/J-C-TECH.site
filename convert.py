import re
import os

with open('index2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract CSS
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
css_content = style_match.group(1) if style_match else ''
with open('src/index.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Extract Body
body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
body_content = body_match.group(1) if body_match else ''

# Remove scripts
body_content = re.sub(r'<script.*?>.*?</script>', '', body_content, flags=re.DOTALL)

# Convert HTML comments to JSX comments
body_content = re.sub(r'<!--(.*?)-->', r'{/* \1 */}', body_content, flags=re.DOTALL)

# Fix class -> className
body_content = re.sub(r'\bclass=', 'className=', body_content)

# Fix for -> htmlFor
body_content = re.sub(r'\bfor=', 'htmlFor=', body_content)

# Fix SVG/HTML attributes
attr_replacements = {
    'stroke-width': 'strokeWidth',
    'stroke-linecap': 'strokeLinecap',
    'stroke-linejoin': 'strokeLinejoin',
    'fill-rule': 'fillRule',
    'clip-rule': 'clipRule',
    'clip-path': 'clipPath',
    'stroke-miterlimit': 'strokeMiterlimit',
    'autocomplete': 'autoComplete',
    'tabindex': 'tabIndex'
}
for old, new in attr_replacements.items():
    body_content = re.sub(rf'\b{old}=', f'{new}=', body_content)

# Fix inline styles (if any)
# Quick regex to fix style="position:absolute" -> style={{position: "absolute"}}
# This is basic and might need manual tweaking if there are complex styles.
def replace_style(match):
    style_str = match.group(1)
    # just a very naive conversion
    props = []
    for prop in style_str.split(';'):
        prop = prop.strip()
        if not prop: continue
        if ':' in prop:
            k, v = prop.split(':', 1)
            k = k.strip()
            v = v.strip()
            # camelCase key
            k_parts = k.split('-')
            k_camel = k_parts[0] + ''.join(x.title() for x in k_parts[1:])
            props.append(f'{k_camel}: "{v}"')
    return 'style={{' + ', '.join(props) + '}}'

body_content = re.sub(r'style="([^"]*)"', replace_style, body_content)

# Fix unclosed tags (input, img, hr, br)
body_content = re.sub(r'<(input|img|hr|br)([^>]*?)(?<!/)>', r'<\1\2 />', body_content)

jsx = f"""import './index.css';
import {{ useEffect }} from 'react';

function App() {{
  useEffect(() => {{
    // Nav scroll state
    const navbar = document.getElementById('navbar');
    const handleScroll = () => {{
      navbar?.classList.toggle('scrolled', window.scrollY > 40);
    }};
    window.addEventListener('scroll', handleScroll);

    // Scroll reveal
    const revealObserver = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          entry.target.classList.add('in');
          revealObserver.unobserve(entry.target);
        }}
      }});
    }}, {{ threshold: 0.15, rootMargin: '0px 0px -60px 0px' }});
    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

    // Process line trigger
    const processTrack = document.querySelector('.process-track');
    if (processTrack) {{
      const procObserver = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
          if (entry.isIntersecting) {{
            processTrack.classList.add('in');
            procObserver.unobserve(entry.target);
          }}
        }});
      }}, {{ threshold: 0.5 }});
      procObserver.observe(processTrack);
    }}

    return () => {{
      window.removeEventListener('scroll', handleScroll);
      revealObserver.disconnect();
    }};
  }}, []);

  const toggleMobileNav = () => {{
    const mobileNav = document.getElementById('mobileNav');
    const hamburger = document.getElementById('hamburger');
    if (mobileNav && hamburger) {{
      const open = mobileNav.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', String(open));
      hamburger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }}
  }};

  const closeMobileNav = () => {{
    document.getElementById('mobileNav')?.classList.remove('open');
  }};

  return (
    <div className="no-js">
      {{/* Original body content */}}
      {body_content}
    </div>
  );
}}

export default App;
"""

# Small adjustments to hamburger logic since it's now in React
jsx = jsx.replace('id="hamburger"', 'id="hamburger" onClick={toggleMobileNav}')
# Fix all mobile nav links
jsx = jsx.replace('<div id="mobileNav" aria-label="Mobile">', '<div id="mobileNav" aria-label="Mobile" onClick={closeMobileNav}>')

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(jsx)

print("Conversion complete.")
