import React from 'react';
import { motion } from 'framer-motion';
import { Network, Box, Zap } from 'lucide-react';
import './FloatingServiceCards.css';

const cards = [
  {
    icon: <Network size={22} strokeWidth={1.5} />,
    title: "AI Solutions",
    subtitle: "Intelligent Engineering & Automation",
    marginLeft: 0,
  },
  {
    icon: <Box size={22} strokeWidth={1.5} />,
    title: "Engineering Design",
    subtitle: "Product Design & Simulation",
    marginLeft: 40,
  },
  {
    icon: <Zap size={22} strokeWidth={1.5} />,
    title: "EV Engineering",
    subtitle: "Future Mobility Systems",
    marginLeft: 80,
  }
];

const FloatingServiceCards = () => {
  return (
    <div className="fc-wrapper">
      {cards.map((card, index) => (
        <motion.div
          key={index}
          className="fc-card"
          style={{ marginLeft: `${card.marginLeft}px` }}
          initial={{ opacity: 0, x: -40 }}
          animate={{ opacity: 1, x: 0, y: [0, -8, 0] }}
          transition={{
            opacity: { duration: 0.6, delay: 0.4 + index * 0.15 },
            x: { duration: 0.6, delay: 0.4 + index * 0.15 },
            y: {
              duration: 4,
              repeat: Infinity,
              ease: "easeInOut",
              delay: index * 0.4
            }
          }}
          whileHover={{
            scale: 1.03,
            rotateX: 5,
            rotateY: 5,
            transition: { duration: 0.2 }
          }}
        >
          <div className="fc-icon">{card.icon}</div>
          <div className="fc-content">
            <div className="fc-title">{card.title}</div>
            <div className="fc-subtitle">{card.subtitle}</div>
          </div>
        </motion.div>
      ))}
    </div>
  );
};

export default FloatingServiceCards;
