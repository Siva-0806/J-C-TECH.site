import React from 'react';

const paths = [
  {
    num: 'Path 01',
    title: 'Engineering Design',
    bg: '/path01-engineering-design.jpg',
    items: [
      'Certified Product Design',
      'Masters in Industrial Design',
      'Masters in Automotive Design',
      'Masters in CAD / CAM Engineer',
      'Reverse Engineering / Remastering',
      'Certified in CAE',
      'Certified CAM Programmer',
      'Masters in R&D Design',
      'Certified in Wiring Harness Design',
      'Industries Required Skills',
      'Interview Preparations',
    ],
  },
  {
    num: 'Path 02',
    title: 'Artificial Intelligence',
    bg: '/path02-artificial-intelligence.jpg',
    items: [
      'Python',
      'Machine Learning',
      'Deep Learning',
      'NLP',
      'Computer Vision',
      'Generative AI',
      'Power BI',
      'Tableau',
    ],
  },
  {
    num: 'Path 03',
    title: 'Electric Vehicle',
    bg: '/path03-electric-vehicle.jpg',
    items: [
      'Introduction to Electric Vehicles',
      'EV Architecture & Energy Flow',
      'Battery & BMS',
      'Motors & Controls',
      'EV HV-LV systems',
      'EV Standards & Regulations',
      'EV Data & AI Applications',
      'Hands-on EV Projects',
    ],
  },
  {
    num: 'Path 04',
    title: 'Engineering Automation',
    bg: '/path04-engineering-automation.jpg',
    items: [
      'Engineering Data & Digital Workflow',
      'Programming Fundamentals for Engineers',
      'Excel, Power BI & Tableau',
      'Design Automation',
      'BOM & Engineering Documentation Automation',
      'Fixture Design Automation',
      'Wiring Harness Automation',
      'Robotic Process Automation – RPA',
      'Hands on Projects',
    ],
  },
];

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
          {paths.map((path) => (
            <div
              key={path.num}
              className="course-card reveal"
              style={{ backgroundImage: `url(${path.bg})` }}
            >
              <div className="course-card-overlay" />
              <div className="course-card-content">
                <span className="course-num">{path.num}</span>
                <h4>{path.title}</h4>
                <ul>
                  {path.items.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>
                <a href="#contact" className="course-cta-btn">View Course →</a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Courses;
