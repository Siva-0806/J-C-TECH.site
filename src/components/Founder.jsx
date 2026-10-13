import React from 'react';

const Founder = () => {
  return (
    <section id="founder">
  <div className="container">
    <div className="founder-wrap" style={{ alignItems: 'stretch' }}>
      <div className="founder-photo-wrapper">
        <div className="founder-photo reveal">
          <img
            src="/Founder.jpeg"
            alt="Gopinath Chidambaram - Founder of JC Tech"
            className="founder-img"
          />
        </div>
      </div>
      <div className="reveal" style={{ alignSelf: 'center' }}>
        <div className="eyebrow">Founder's Message</div>
        <h2 style={{ color: 'var(--navy-900)', marginBottom: '0.5rem', fontSize: '2.5rem' }}>Gopinath Chidambaram</h2>
        <div className="founder-role" style={{ marginBottom: '1.5rem', color: 'var(--orange-500)', fontSize: '1.1rem', fontWeight: '500' }}>
          Engineering Consultant | Project Manager | CAD Specialist | AI Engineer | Corporate Trainer
        </div>
        
        <p className="founder-quote" style={{ fontStyle: 'normal', color: 'var(--navy-900)', fontSize: '1.1rem', marginBottom: '1rem', lineHeight: '1.7' }}>
          With over 22 years of industrial experience, I have worked across Product Design, Fixture Design, Electrical Wiring Harness Design, Project Management and Manufacturing Engineering. My journey spans leading engineering teams, delivering complex customer projects and continuously adapting to new technologies.
        </p>
        
        <p className="founder-quote" style={{ fontStyle: 'normal', color: 'var(--navy-900)', fontSize: '1.1rem', marginBottom: '2rem', lineHeight: '1.7' }}>
          Today, through JC Tech, my mission is to bridge the gap between academic knowledge and industrial practice by integrating CAD, Artificial Intelligence, Electric Vehicle technologies and engineering consulting into one practical learning ecosystem.
        </p>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', background: 'rgba(11, 30, 68, 0.04)', padding: '2rem', borderRadius: '16px', border: '1px solid rgba(11, 30, 68, 0.1)' }}>
          <div>
            <h4 style={{ color: 'var(--navy-900)', marginBottom: '0.5rem' }}>My Mission</h4>
            <p style={{ color: 'var(--navy-900)', lineHeight: '1.6', margin: 0 }}>To empower engineers with practical knowledge, modern engineering technologies and real industrial experience, enabling them to solve complex engineering problems with confidence and innovation.</p>
          </div>
          <div>
            <h4 style={{ color: 'var(--navy-900)', marginBottom: '0.5rem' }}>Vision</h4>
            <p style={{ color: 'var(--navy-900)', lineHeight: '1.6', margin: 0 }}>To build India's most trusted Engineering Intelligence Company by integrating CAD, Artificial Intelligence, Electric Vehicles and Engineering Consulting into one unified platform for learning, innovation and industrial transformation.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
  );
};

export default Founder;
