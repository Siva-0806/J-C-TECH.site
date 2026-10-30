import React from 'react';

const Footer = () => {
  return (
    <footer>
  <div className="container">
    <div className="footer-top">
      <div>
        <div className="footer-brand"><span className="logo-badge"><svg className="logo" role="img" aria-label="JC Tech logo"><use href="#jc-logo"></use></svg></span><span>JC Tech</span></div>

        <div className="subtagline">Learn from Real Industry Experience</div>
        <p style={{ marginTop: '1.5rem', color: '#93a2c4', fontSize: '0.9rem', lineHeight: '1.6' }}>
          <strong>JC Tech</strong><br/>
          Plot NO. 87, AMUDHAM COLONY<br/>
          NANDIVARAM-GUDUVANCHERY ,<br/>
          CHENGALPET DIST ,<br/>
          TAMILNADU , INDIA -603202
        </p>
      </div>
      <div className="footer-col">
        <h5>Company</h5>
        <a href="#about">About</a>
        <a href="#founder">Founder</a>
        <a href="#contact">Contact</a>
      </div>
      <div className="footer-col">
        <h5>Programs</h5>
        <a href="#courses">Courses</a>
        <a href="#corporate">Corporate Training</a>
        <a href="#consulting">Consulting</a>
        <a href="#ai-solutions">AI Solutions</a>
      </div>
      <div className="footer-col">
        <h5>Resources</h5>
        <a href="#hub">Knowledge Hub</a>
        <a href="#blog">Blog</a>
        <a href="#ev">EV Engineering</a>
        <a href="#industries">Industries</a>
      </div>
    </div>
    <div className="footer-bottom">
      <p>© 2026 JC Tech. All rights reserved.</p>
    </div>
  </div>
</footer>
  );
};

export default Footer;
