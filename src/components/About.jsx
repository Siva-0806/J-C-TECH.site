import React from 'react';

const About = () => {
  return (
    <section id="about">
  <div className="container">
    <div className="about-wrap">
      <div>
        <div className="section-head reveal">
          <div className="eyebrow">About JC Tech</div>
          <h2>An Engineering Intelligence Company, Not a Training Institute</h2>
        </div>
        <div className="about-copy reveal">
          <p>JC Tech is an Engineering Intelligence Company dedicated to bridging the gap between academic knowledge and industrial excellence.</p>
          <p>Founded by <b>Gopinath Chidambaram</b>, an engineering professional with more than 25 years of experience in Product Design, CAD, Project Management, Wiring Harness Engineering and Artificial Intelligence, JC Tech focuses on practical learning, innovation and industry transformation.</p>
          <p>Our mission is to prepare engineers for Industry 4.0 by combining engineering fundamentals with AI-powered technologies.</p>
        </div>
        <div className="pillars reveal">
          <div className="pillar"><span className="dot"></span>Integrity</div>
          <div className="pillar"><span className="dot"></span>Innovation</div>
          <div className="pillar"><span className="dot"></span>Continuous Learning</div>
          <div className="pillar"><span className="dot"></span>Practical Engineering</div>
          <div className="pillar"><span className="dot"></span>Customer Success</div>
          <div className="pillar"><span className="dot"></span>Leadership</div>
        </div>
      </div>
      <div className="vm-cards reveal">
        <div className="vm-card">
          <h4>Our Vision</h4>
          <p>To become India's most trusted Engineering Intelligence Company by integrating CAD, Artificial Intelligence, Electric Vehicles and Industrial Consulting.</p>
        </div>
        <div className="vm-card alt">
          <h4>Our Mission</h4>
          <p>We simplify complex engineering technologies through practical education, AI-driven innovation and industrial consulting.</p>
        </div>
        <div style={{ borderRadius: '24px', overflow: 'hidden', boxShadow: '0 12px 40px -12px rgba(0,0,0,0.15)', marginTop: '8px' }}>
          <img src="/About.jpg" alt="About JC Tech" style={{ width: '100%', height: '380px', display: 'block', objectFit: 'cover', objectPosition: 'center' }} />
        </div>
      </div>
    </div>
  </div>
</section>
  );
};

export default About;
