import React from 'react';

const CorporateTraining = () => {
  const cards = [
    { title: "AI for Engineers", desc: "Applied AI foundations for practicing engineers." },
    { title: "CAD Training", desc: "Production-ready 3D modeling and real design workflows." },
    { title: "EV Fundamentals", desc: "Core EV systems for teams entering electric mobility." },
    { title: "Wiring Harness Design", desc: "End-to-end harness engineering practice." },
    { title: "GD&T", desc: "Precision dimensioning and tolerancing mastery." },
    { title: "Design Standards", desc: "Industry and organizational design standards." },
    { title: "Python for Engineers", desc: "Automation and scripting built for engineering teams." }
  ];

  return (
    <section id="corporate">
      <div className="container">
        <div className="section-head reveal">
          <div className="eyebrow">Corporate Training</div>
          <h2>Upskill Your Engineering Team, On Their Turf</h2>
          <p>On-site and cohort-based programs built around your industry's real workflows.</p>
        </div>
        <div className="corp-scroll-wrapper">
          <div className="corp-scroll">
            {cards.map((c, i) => (
              <div className="corp-card" key={i}>
                <h4>{c.title}</h4>
                <p>{c.desc}</p>
              </div>
            ))}
            {cards.map((c, i) => (
              <div className="corp-card" key={`dup-${i}`}>
                <h4>{c.title}</h4>
                <p>{c.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default CorporateTraining;
