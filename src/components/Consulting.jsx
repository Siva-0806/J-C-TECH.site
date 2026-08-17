import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { CheckCircle2 } from 'lucide-react';
import bgImage from '../assets/consulting.jpg';
import './Consulting.css';

const servicesData = [
  {
    id: 1,
    num: '01',
    title: 'CAD Consulting',
    description: 'Transform product ideas into manufacturing-ready designs with expert CAD modeling, assemblies, technical drawings, reverse engineering, and design optimization using industry-standard engineering workflows.',
    features: ['3D CAD Modeling', 'Technical Drawings', 'Reverse Engineering', 'Design Validation']
  },
  {
    id: 2,
    num: '02',
    title: 'Product Development',
    description: 'Accelerate your product development lifecycle from concept to prototype with engineering expertise, simulation-driven design, validation, and manufacturing support.',
    features: ['Product Design', 'Prototype Development', 'Design Optimization', 'Manufacturing Support']
  },
  {
    id: 3,
    num: '03',
    title: 'AI for Manufacturing',
    description: 'Leverage Artificial Intelligence to improve production efficiency, predictive maintenance, quality inspection, and intelligent decision-making across modern manufacturing systems.',
    features: ['Predictive Maintenance', 'Computer Vision', 'Process Automation', 'Production Analytics']
  },
  {
    id: 4,
    num: '04',
    title: 'EV System Consulting',
    description: 'Develop next-generation electric mobility solutions with consulting on battery systems, motor selection, BMS, charging infrastructure, thermal management, and EV architecture.',
    features: ['Battery Pack Design', 'Battery Management System', 'Motor & Controller', 'Charging Systems']
  },
  {
    id: 5,
    num: '05',
    title: 'Wiring Harness Consulting',
    description: 'Design reliable automotive and industrial wiring harnesses with optimized routing, connector selection, protection strategies, and compliance with global standards.',
    features: ['Harness Routing', 'Connector Selection', 'Electrical Schematics', 'Manufacturing Documentation']
  },
  {
    id: 6,
    num: '06',
    title: 'Process Improvement',
    description: 'Optimize engineering and manufacturing workflows through Lean methodologies, automation strategies, productivity analysis, and continuous improvement initiatives.',
    features: ['Lean Engineering', 'Workflow Optimization', 'Cost Reduction', 'Performance Analysis']
  },
  {
    id: 7,
    num: '07',
    title: 'Digital Engineering',
    description: 'Enable digital transformation using CAD, CAE, PLM, Digital Twins, simulation technologies, and connected engineering workflows.',
    features: ['Digital Twin', 'PLM Integration', 'Engineering Simulation', 'Automation']
  },
  {
    id: 8,
    num: '08',
    title: 'Technical Documentation',
    description: 'Produce industry-standard engineering documentation including SOPs, manuals, assembly guides, compliance reports, BOMs, and technical specifications.',
    features: ['SOP Documentation', 'User Manuals', 'BOM Creation', 'Engineering Reports']
  }
];

const Consulting = () => {
  const [activeService, setActiveService] = useState(servicesData[0]);

  return (
    <section 
      id="consulting"
      style={{
        background: `linear-gradient(rgba(4, 11, 26, 0.90), rgba(4, 11, 26, 0.90)), url(${bgImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundAttachment: 'fixed',
        padding: '100px 0'
      }}
    >
      <div className="container">
        <div className="section-head reveal">
          <div className="eyebrow" style={{ color: 'var(--orange-500)' }}>Engineering Consulting</div>
          <h2 style={{ color: 'var(--white)' }}>When Your Team Needs Answers, Not Another Course</h2>
          <p style={{ color: '#93A2C4' }}>Hands-on consulting engagements for manufacturing and engineering organizations.</p>
        </div>
        
        <div className="consult-layout">
          {/* Left Column: Vertical Boxes */}
          <div className="consult-vertical-list stagger">
            {servicesData.map((service) => {
              const isActive = activeService.id === service.id;
              return (
                <div 
                  key={service.id}
                  className={`consult-vbox reveal ${isActive ? 'active' : ''}`}
                  onClick={() => setActiveService(service)}
                  role="button"
                  tabIndex={0}
                  onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') setActiveService(service); }}
                >
                  <div className="vbox-left">
                    <span className="vbox-num">{service.num}</span>
                    <h4 className="vbox-title">{service.title}</h4>
                  </div>
                  <span className="vbox-arrow">↗</span>
                </div>
              );
            })}
          </div>

          {/* Right Column: Description & Deliverables Panel */}
          <div className="consult-detail-wrapper">
            <AnimatePresence mode="wait">
              <motion.div 
                key={activeService.id}
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                transition={{ duration: 0.28, ease: "easeOut" }}
                className="consult-detail-panel"
              >
                <div className="panel-badge-row">
                  <span className="panel-badge">CONSULTING SERVICE {activeService.num}</span>
                </div>

                <h3 className="panel-heading">{activeService.title}</h3>
                
                <p className="panel-desc">
                  {activeService.description}
                </p>

                <div className="panel-features-section">
                  <div className="features-title">Core Deliverables & Capabilities:</div>
                  <div className="panel-features-grid">
                    {activeService.features.map((feature, i) => (
                      <div key={i} className="feature-item">
                        <CheckCircle2 size={18} className="feature-icon" />
                        <span>{feature}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </motion.div>
            </AnimatePresence>
          </div>
        </div>

      </div>
    </section>
  );
};

export default Consulting;
