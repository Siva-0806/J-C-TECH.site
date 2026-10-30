import React from 'react';

const Why = () => {
  return (
    <section id="why">
  <div className="container">
    <div className="section-head center reveal">
      <div className="eyebrow" style={{ color: 'var(--orange-500)', fontWeight: 900, fontSize: '2rem', textTransform: 'uppercase', letterSpacing: '2px' }}>Why JC TECH?</div>
      <h2 style={{ color: 'var(--white)' }}>Engineered for Your Success</h2>
      <p style={{ color: '#93A2C4', fontWeight: 'bold' }}>We bridge the gap between academic theory and industrial reality. Here is how we build the next generation of engineers.</p>
    </div>
    <div className="why-grid stagger">
      <div className="why-card reveal">
        <div className="why-ic"><svg viewBox="0 0 24 24" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M12 18v3"/></svg></div>
        <h4>Real Industrial Projects</h4>
        <p>Dive into actual blueprints and problem-solving scenarios pulled directly from active manufacturing floors instead of relying on textbook theories.</p>
      </div>
      <div className="why-card reveal">
        <div className="why-ic"><svg viewBox="0 0 24 24" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg></div>
        <h4>Industry Standard Methodologies</h4>
        <p>Master how the best global engineering firms operate by utilizing proven methodologies like DFMEA, GD&T, and Agile engineering principles.</p>
      </div>
      <div className="why-card reveal">
        <div className="why-ic"><svg viewBox="0 0 24 24" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
        <h4>Learn from Engineering Failures &amp; Successes</h4>
        <p>Gain unique, hard-earned insights by reverse-engineering real-world product failures and analyzing the architecture of successful market launches.</p>
      </div>
      <div className="why-card reveal">
        <div className="why-ic"><svg viewBox="0 0 24 24" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4.9 4.9l2.8 2.8M16.3 16.3l2.8 2.8M2 12h4M18 12h4M4.9 19.1l2.8-2.8M16.3 7.7l2.8-2.8"/></svg></div>
        <h4>AI Integrated Engineering</h4>
        <p>Bridge the gap between traditional mechanical design and the future with our advanced Artificial Intelligence and Python automation curriculum.</p>
      </div>
      <div className="why-card reveal">
        <div className="why-ic"><svg viewBox="0 0 24 24" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg></div>
        <h4>Career Mentoring</h4>
        <p>Receive dedicated guidance on resume building, technical interview preparation, and strategically navigating the modern engineering job market.</p>
      </div>
      <div className="why-card reveal">
        <div className="why-ic"><svg viewBox="0 0 24 24" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/></svg></div>
        <h4>Engineering Consulting Experience</h4>
        <p>Benefit directly from our active corporate consulting practice, ensuring everything you learn matches exactly what top industries demand today.</p>
      </div>
    </div>
  </div>
</section>
  );
};

export default Why;
