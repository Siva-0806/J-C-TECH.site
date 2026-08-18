import React, { useState, useEffect } from 'react';

const Navbar = () => {
  const [mobileOpen, setMobileOpen] = useState(false);

  // Close mobile menu on resize to desktop
  useEffect(() => {
    const onResize = () => {
      if (window.innerWidth > 768) setMobileOpen(false);
    };
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);

  // Prevent body scroll when mobile menu is open
  useEffect(() => {
    document.body.style.overflow = mobileOpen ? 'hidden' : '';
    return () => { document.body.style.overflow = ''; };
  }, [mobileOpen]);

  const closeMenu = () => setMobileOpen(false);

  return (
    <header>
      <nav id="navbar" aria-label="Primary">
        <div className="container">
          <a href="#hero" className="nav-brand" onClick={closeMenu}>
            <span className="logo-badge"><svg className="logo" role="img" aria-label="JC Tech logo"><use href="#jc-logo"></use></svg></span>
            <div>
              <span>JC Tech</span>
              <small>Learn from Real Industry Experience</small>
            </div>
          </a>
          <div className="nav-links">
            <a href="#hero">Home</a>
            <a href="#about">About</a>
            <a href="#courses">Courses</a>
            <a href="#ai-solutions">AI Solutions</a>
            <a href="#ev">EV Engineering</a>
            <a href="#consulting">Consulting</a>
            <a href="#corporate">Corporate Training</a>
            <a href="#blog">Blog</a>
            <a href="#contact">Contact</a>
          </div>
          <div className="nav-cta">
            <a href="#contact" className="nav-cta-btn">Book Consultation</a>
          </div>
          {/* Hamburger — visible only on mobile */}
          <button
            className={`hamburger${mobileOpen ? ' open' : ''}`}
            aria-label={mobileOpen ? 'Close menu' : 'Open menu'}
            aria-expanded={mobileOpen}
            onClick={() => setMobileOpen(o => !o)}
          >
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </nav>

      {/* Mobile full-screen drawer */}
      <nav id="mobileNav" className={mobileOpen ? 'open' : ''} aria-label="Mobile navigation">
        <a href="#hero" onClick={closeMenu}>Home</a>
        <a href="#about" onClick={closeMenu}>About</a>
        <a href="#courses" onClick={closeMenu}>Courses</a>
        <a href="#ai-solutions" onClick={closeMenu}>AI Solutions</a>
        <a href="#ev" onClick={closeMenu}>EV Engineering</a>
        <a href="#consulting" onClick={closeMenu}>Consulting</a>
        <a href="#corporate" onClick={closeMenu}>Corporate Training</a>
        <a href="#blog" onClick={closeMenu}>Blog</a>
        <a href="#contact" onClick={closeMenu}>Contact</a>
        <a href="#contact" className="nav-cta-btn" onClick={closeMenu}>Book Consultation</a>
      </nav>
    </header>
  );
};

export default Navbar;
