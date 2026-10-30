import React from 'react';
import { motion } from 'framer-motion';

/* ── 5 Knowledge Hub topics with SVG icons & PDF download paths ── */
const hubTopics = [
  {
    id: 'encyclopedia',
    label: 'Engineering Encyclopedia',
    pdf: '/pdfs/engineering-encyclopedia.pdf',
    color: '#FF6A1F',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 19.5A2.5 2.5 0 016.5 17H20" />
        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z" />
        <path d="M8 7h8M8 11h5" />
      </svg>
    ),
  },
  {
    id: 'ev-database',
    label: 'EV Component Database',
    pdf: '/pdfs/ev-component-database.pdf',
    color: '#3B82F6',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <ellipse cx="12" cy="5" rx="8" ry="3" />
        <path d="M4 5v14a8 3 0 0016 0V5" />
        <path d="M4 12a8 3 0 0016 0" />
      </svg>
    ),
  },
  {
    id: 'cad-standards',
    label: 'CAD Standards Library',
    pdf: '/pdfs/cad-standards-library.pdf',
    color: '#10B981',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <rect x="4" y="3" width="16" height="18" rx="2" />
        <path d="M8 8h8M8 12h8M8 16h5" />
        <path d="M16 3v4h4" />
      </svg>
    ),
  },
  {
    id: 'ai-blog',
    label: 'AI for Engineers Blog',
    pdf: '/pdfs/ai-for-engineers-blog.pdf',
    color: '#8B5CF6',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <path d="M12 2a4 4 0 014 4v1h1a3 3 0 010 6h-1v1a4 4 0 01-8 0v-1H7a3 3 0 010-6h1V6a4 4 0 014-4z" />
        <circle cx="10" cy="10" r="1" fill="currentColor" />
        <circle cx="14" cy="10" r="1" fill="currentColor" />
        <path d="M9 14c.6 1 1.5 1.5 3 1.5s2.4-.5 3-1.5" />
      </svg>
    ),
  },
  {
    id: 'eng-tools',
    label: 'Engineering Tools',
    pdf: '/pdfs/engineering-tools.pdf',
    color: '#F59E0B',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z" />
      </svg>
    ),
  },
];

/* ── Animation variants ── */
const containerVariants = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.15, delayChildren: 0.2 },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 60, scale: 0.8, rotateX: 25 },
  visible: {
    opacity: 1,
    y: 0,
    scale: 1,
    rotateX: 0,
    transition: {
      type: 'spring',
      stiffness: 90,
      damping: 14,
      mass: 0.8,
    },
  },
};

const bannerVariants = {
  hidden: { opacity: 0, y: 40 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.7, ease: [0.22, 1, 0.36, 1] },
  },
};

const KnowledgeHub = () => {
  return (
    <section id="hub">
      <div className="container">
        {/* ── Banner ── */}
        <motion.div
          className="hub-banner"
          variants={bannerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '-60px' }}
        >
          <div>
            <h3>The JC Tech Knowledge Hub</h3>
            <p>
              Free resources built for engineers, not just students — because
              we're not just a course-selling website.
            </p>
          </div>
          <a href="#contact" className="btn btn-primary">
            Get Your Custom Resources
          </a>
        </motion.div>

        {/* ── Hub Cards Grid ── */}
        <motion.div
          className="hub-grid hub-grid--five"
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '-40px' }}
        >
          {hubTopics.map((topic) => (
            <motion.a
              key={topic.id}
              href={topic.pdf}
              download
              className="hub-item hub-item--large"
              variants={itemVariants}
              whileHover={{
                y: -12,
                scale: 1.04,
                boxShadow: `0 24px 48px -12px ${topic.color}55`,
              }}
              whileTap={{ scale: 0.97 }}
              style={{ '--hub-accent': topic.color }}
            >
              {/* Glow ring behind icon */}
              <motion.div
                className="hub-glow"
                initial={{ scale: 0, opacity: 0 }}
                whileInView={{ scale: 1, opacity: 1 }}
                transition={{ delay: 0.4, duration: 0.6, ease: 'easeOut' }}
                viewport={{ once: true }}
              />

              <div className="hub-ic hub-ic--large">{topic.icon}</div>

              <span>{topic.label}</span>

              {/* Download indicator */}
              <div className="hub-download-hint">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4" />
                  <path d="M7 10l5 5 5-5M12 15V3" />
                </svg>
                <small>Download PDF</small>
              </div>
            </motion.a>
          ))}
        </motion.div>
      </div>
    </section>
  );
};

export default KnowledgeHub;
