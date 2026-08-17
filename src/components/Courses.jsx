import React from 'react';

const Courses = () => {
  return (
    <section id="courses">
  <div className="container">
    <div className="section-head reveal">
      <div className="eyebrow">Courses, Organized by Career Path</div>
      <h2>Choose Where You Want to Go — We'll Build the Path</h2>
      <p style={{ color: 'var(--navy-800)' }}>Instead of a list of software names, we organize learning by the career you're building toward.</p>
    </div>
    <div className="course-grid stagger">
      <div className="course-card reveal">
        <span className="course-num">Path 01</span>
        <h4>Engineering Design</h4>
        <ul>
          <li>CERTIFIED PRODUCT DESIGN</li>
          <li>MASTERS IN INDUSTRIAL DESIGN</li>
          <li>MASTERS IN AUTOMOTIVE DESIGN</li>
          <li>MASTERS IN CAD / CAM ENGINEER</li>
          <li>Reverse engineering / Remastering</li>
          <li>CERTIFIED IN CAE</li>
          <li>CERTIFIED CAM PROGRAMMER</li>
          <li>MASTERS IN R&D DESIGN</li>
          <li>CERTIFIED In WIRING HARNESS DESIGN</li>
          <li>Industries required skills</li>
          <li>Interview preparations</li>
        </ul>
      </div>
      <div className="course-card reveal">
        <span className="course-num">Path 02</span>
        <h4>Artificial Intelligence</h4>
        <ul>
          <li>Python</li>
          <li>Machine Learning</li>
          <li>Deep Learning</li>
          <li>NLP</li>
          <li>Computer Vision</li>
          <li>Generative AI</li>
          <li>Power BI</li>
          <li>Tableau</li>
        </ul>
      </div>
      <div className="course-card reveal">
        <span className="course-num">Path 03</span>
        <h4>Electric Vehicle</h4>
        <ul>
          <li>Introduction to Electric Vehicles</li>
          <li>EV Architecture & Energy Flow</li>
          <li>Battery & BMS</li>
          <li>Motors & Controls</li>
          <li>EV HV-LV systems</li>
          <li>EV Standards & Regulations</li>
          <li>EV Data & AI Applications</li>
          <li>Hands-on EV Projects</li>
        </ul>
      </div>
      <div className="course-card reveal">
        <span className="course-num">Path 04</span>
        <h4>Engineering Automation</h4>
        <ul>
          <li>Engineering Data & Digital Workflow</li>
          <li>Programming Fundamentals for Engineers</li>
          <li>Excel, Power BI & Tableau</li>
          <li>Design Automation</li>
          <li>BOM & Engineering Documentation Automation</li>
          <li>Fixture Design Automation</li>
          <li>Wiring Harness Automation</li>
          <li>Robotic Process Automation – RPA</li>
          <li>Hands on Projects</li>
        </ul>
      </div>
    </div>
  </div>
</section>
  );
};

export default Courses;
