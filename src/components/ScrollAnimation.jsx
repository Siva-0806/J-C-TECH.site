import React, { useEffect, useRef } from 'react';
import { motion } from 'framer-motion';

const ScrollAnimation = ({ children }) => {
  const canvasRef = useRef(null);
  const containerRef = useRef(null);
  const contentRef = useRef(null);
  const overlayRef = useRef(null);
  const welcomeRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');
    const frameCount = 301;
    
    // Set actual resolution of the canvas. Standard 16:9 1080p.
    canvas.width = 1920;
    canvas.height = 1080;

    const currentFrame = index => (
      `/frames/frame${index.toString().padStart(5, '0')}.jpg`
    );

    const images = [];

    // Preload images
    for (let i = 0; i < frameCount; i++) {
      const img = new Image();
      img.src = currentFrame(i);
      images.push(img);
      
      // Draw first frame once it's loaded to avoid blank canvas initially
      if (i === 0) {
        img.onload = () => {
          context.drawImage(img, 0, 0, canvas.width, canvas.height);
        };
      }
    }

    const handleScroll = () => {
      const container = containerRef.current;
      if (!container) return;
      
      const containerTop = container.getBoundingClientRect().top;
      const containerHeight = container.offsetHeight;
      const windowHeight = window.innerHeight;
      
      // Calculate scroll progress within the container (0 to 1)
      let scrollFraction = -containerTop / (containerHeight - windowHeight);
      scrollFraction = Math.max(0, Math.min(1, scrollFraction));

      // Phase 1 (0.0 to 0.1): Welcome quote fades out, animation hasn't started
      const welcomeOpacity = Math.max(0, 1 - (scrollFraction / 0.1));
      
      // Phase 2 (0.1 to 0.8): Image sequence plays
      const animationFraction = Math.max(0, Math.min(1, (scrollFraction - 0.1) / 0.7));
      
      // Phase 3 (0.8 to 1.0): Holds the last frame, Hero section fades in
      const heroOpacity = Math.max(0, (scrollFraction - 0.8) / 0.2);

      // Direct DOM manipulation for buttery smooth 60fps scrolling (no React re-renders)
      if (welcomeRef.current) {
        welcomeRef.current.style.opacity = welcomeOpacity;
        // Slide up slightly as it fades out for a premium feel
        welcomeRef.current.style.transform = `translate(-50%, calc(-50% - ${10 * (1 - welcomeOpacity)}px))`;
      }

      if (contentRef.current) {
        contentRef.current.style.opacity = heroOpacity;
        contentRef.current.style.pointerEvents = heroOpacity > 0.5 ? 'auto' : 'none';
      }
      
      if (overlayRef.current) {
        overlayRef.current.style.background = `linear-gradient(to bottom, rgba(1, 15, 36, ${0.2 + (heroOpacity * 0.7)}) 0%, rgba(1, 15, 36, 1) 100%)`;
      }

      const frameIndex = Math.min(
        frameCount - 1,
        Math.floor(animationFraction * frameCount)
      );

      // Smooth render via RAF
      requestAnimationFrame(() => {
        if (images[frameIndex] && images[frameIndex].complete) {
          context.drawImage(images[frameIndex], 0, 0, canvas.width, canvas.height);
        }
      });
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Trigger once on mount

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div ref={containerRef} style={{ height: '600vh', position: 'relative', width: '100%', backgroundColor: '#000' }}>
      <div style={{ 
        position: 'sticky', 
        top: 0, 
        minHeight: '100vh', 
        width: '100%', 
        display: 'flex', 
        alignItems: 'flex-start', 
        justifyContent: 'center',
        zIndex: 0
      }}>
        <canvas 
          ref={canvasRef} 
          style={{
            width: '100vw',
            height: '100vh',
            objectFit: 'cover',
            position: 'absolute',
            top: 0,
            left: 0
          }} 
        />
        
        {/* Gradient overlay to blend into the dark theme */}
        <div 
          ref={overlayRef}
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            background: `linear-gradient(to bottom, rgba(1, 15, 36, 0.2) 0%, rgba(1, 15, 36, 1) 100%)`,
            pointerEvents: 'none'
          }} 
        />
        
        {/* Welcome Quote (Visible before animation starts) */}
        <div 
          ref={welcomeRef}
          style={{
            position: 'absolute',
            zIndex: 2,
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            textAlign: 'center',
            width: '100%',
            padding: '0 20px',
            color: '#fff', 
            textShadow: '0 2px 20px rgba(0,0,0,0.8)', // Ensures white text is visible over light backgrounds
            display: 'flex',
            flexDirection: 'column',
            gap: '16px',
            pointerEvents: 'none',
            willChange: 'opacity, transform'
          }}>
          <motion.h2 
            initial={{ opacity: 0, y: 30, filter: 'blur(10px)' }}
            animate={{ opacity: 1, y: 0, filter: 'blur(0px)' }}
            transition={{ duration: 1.2, ease: "easeOut" }}
            style={{ color: '#fff', fontSize: 'clamp(3rem, 7vw, 5.5rem)', fontWeight: '900', margin: 0, letterSpacing: '-0.02em', lineHeight: 1.1, textTransform: 'uppercase', background: 'linear-gradient(to right, #ffffff, #93a2c4)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', textShadow: 'none' }}>
            Welcome to JC Tech
          </motion.h2>
          <motion.p 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1, delay: 0.5, ease: "easeOut" }}
            style={{ color: '#FF6A1F', fontSize: 'clamp(1.2rem, 2.5vw, 1.8rem)', margin: 0, maxWidth: '800px', alignSelf: 'center', fontWeight: '500', letterSpacing: '2px', textTransform: 'uppercase' }}>
            Where Engineering Intelligence Meets Industry
          </motion.p>
          <motion.div 
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 0.9, scale: 1 }}
            transition={{ duration: 1, delay: 1.2, ease: "easeOut" }}
            style={{ 
            marginTop: '40px', 
            fontSize: '0.85rem', 
            textTransform: 'uppercase', 
            letterSpacing: '3px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '12px',
            color: '#fff'
          }}>
            Scroll to begin
            <motion.div 
              animate={{ height: ['0px', '50px', '50px', '0px'], opacity: [0, 1, 1, 0], y: [0, 0, 10, 10] }}
              transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
              style={{ width: '2px', background: 'linear-gradient(to bottom, #FF6A1F, transparent)' }} />
          </motion.div>
        </div>
        
        {/* Render the Hero section on top, dynamically fading in at the end */}
        <div 
          ref={contentRef}
          style={{
            position: 'relative',
            width: '100%',
            height: '100%',
            opacity: 0,
            zIndex: 1,
            pointerEvents: 'none',
            display: 'flex',
            flexDirection: 'column',
            willChange: 'opacity'
          }}>
          {children}
        </div>
      </div>
    </div>
  );
};

export default ScrollAnimation;
