import React from 'react';

const Testimonials = () => {
  return (
    <section id="testimonials">
  <div className="container">
    <div className="section-head reveal">
      <div className="eyebrow">Testimonials</div>
      <h2>What Students, Companies and Industry Say</h2>
    </div>
    <div className="test-grid stagger">
      <div className="test-card reveal">
        <span className="test-badge">Student Review</span>
        <p className="test-quote">The project-based approach meant I was solving real design problems from week one, not just watching software tutorials.</p>
        <div className="test-person">
          <div className="test-avatar">SR</div>
          <div><b>Sanjay R.</b><span>Mechanical Design Trainee</span></div>
        </div>
      </div>
      <div className="test-card reveal">
        <span className="test-badge">Corporate Review</span>
        <p className="test-quote">JC Tech's on-site AI training gave our design team automation skills we now use in daily production work.</p>
        <div className="test-person">
          <div className="test-avatar">PK</div>
          <div><b>Priya K.</b><span>Engineering Manager</span></div>
        </div>
      </div>
      <div className="test-card reveal">
        <span className="test-badge">Industry Feedback</span>
        <p className="test-quote">Their consulting team cut our BOM review time significantly with a well-scoped automation solution.</p>
        <div className="test-person">
          <div className="test-avatar">AV</div>
          <div><b>Arun V.</b><span>Manufacturing Director</span></div>
        </div>
      </div>
    </div>
  </div>
</section>
  );
};

export default Testimonials;
