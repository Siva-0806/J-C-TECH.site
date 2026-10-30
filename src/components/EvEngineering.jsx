import React from 'react';
import evImage from '../assets/EV.png';

const EvEngineering = () => {
  return (
    <section id="ev">
  <div className="container">
    <div className="ev-wrap">
      <div className="ev-visual reveal">
        <div className="glow"></div>
        <img src={evImage} alt="EV Engineering" style={{ width: '100%', height: 'auto', display: 'block', objectFit: 'contain', position: 'relative', zIndex: 2 }} />
      </div>
      <div>
        <div className="section-head reveal">
          <div className="eyebrow">Electric Vehicle Engineering</div>
          <h2>Full-Stack EV Systems, Taught the Way Industry Builds Them</h2>
          <p>From cells to charging infrastructure — the complete EV engineering stack.</p>
        </div>
        <div className="ev-list stagger">
          <div className="ev-item reveal"><span className="num">01</span>Battery Systems</div>
          <div className="ev-item reveal"><span className="num">02</span>Motor Systems</div>
          <div className="ev-item reveal"><span className="num">03</span>Charging</div>
          <div className="ev-item reveal"><span className="num">04</span>Thermal Management</div>
          <div className="ev-item reveal"><span className="num">05</span>Safety</div>
          <div className="ev-item reveal"><span className="num">06</span>Harness</div>
          <div className="ev-item reveal"><span className="num">07</span>Standards</div>
        </div>
      </div>
    </div>
  </div>
</section>
  );
};

export default EvEngineering;
