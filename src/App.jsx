import './index.css';
import { useEffect } from 'react';
import SvgSymbols from './components/SvgSymbols';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import WhatsAppFloat from './components/WhatsAppFloat';
import Hero from './components/Hero';
import { motion } from 'framer-motion';
import Why from './components/Why';
import About from './components/About';
import Courses from './components/Courses';
import AiSolutions from './components/AiSolutions';
import EvEngineering from './components/EvEngineering';
import Consulting from './components/Consulting';
import CorporateTraining from './components/CorporateTraining';
import Process from './components/Process';
import Industries from './components/Industries';
import KnowledgeHub from './components/KnowledgeHub';
import Blog from './components/Blog';
import Testimonials from './components/Testimonials';
import Founder from './components/Founder';
import Contact from './components/Contact';

function App() {
  useEffect(() => {
    // Nav scroll state
    const navbar = document.getElementById('navbar');
    const handleScroll = () => {
      navbar?.classList.toggle('scrolled', window.scrollY > 40);
    };
    window.addEventListener('scroll', handleScroll);

    // Scroll reveal
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

    // Process line trigger
    const processTrack = document.querySelector('.process-track');
    if (processTrack) {
      const procObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            processTrack.classList.add('in');
            procObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });
      procObserver.observe(processTrack);
    }

    return () => {
      window.removeEventListener('scroll', handleScroll);
      revealObserver.disconnect();
    };
  }, []);

  
  return (
    <div className="no-js">
      {/* Original body content */}
      


{/*  Brand mark: one 0.8 KB inline vector, reused everywhere.
     Standalone copy for email/print/partners: jc-logo.svg  */}
<SvgSymbols />

<a className="skip-link" href="#main">Skip to content</a>


{/*  ============ NAV ============  */}
<Navbar />

<main id="main">
{/*  ============ HERO ============  */}
<Hero />

{/*  ============ ABOUT ============  */}
<motion.div initial={{ y: 40, opacity: 0 }} whileInView={{ y: 0, opacity: 1 }} transition={{ duration: 0.8, ease: "easeOut" }} viewport={{ once: true, margin: "-50px" }}>
<About />
</motion.div>

{/*  ============ COURSES ============  */}
<motion.div initial={{ y: 40, opacity: 0 }} whileInView={{ y: 0, opacity: 1 }} transition={{ duration: 0.8, ease: "easeOut" }} viewport={{ once: true, margin: "-50px" }}>
<Courses />
</motion.div>

{/*  ============ AI SOLUTIONS ============  */}
<motion.div initial={{ y: 40, opacity: 0 }} whileInView={{ y: 0, opacity: 1 }} transition={{ duration: 0.8, ease: "easeOut" }} viewport={{ once: true, margin: "-50px" }}>
<AiSolutions />
</motion.div>

{/*  ============ EV ENGINEERING ============  */}
<EvEngineering />

{/*  ============ CONSULTING ============  */}
<Consulting />

{/*  ============ CORPORATE TRAINING ============  */}
<CorporateTraining />

{/*  ============ PROCESS ============  */}
<Process />

{/*  ============ INDUSTRIES ============  */}
<Industries />

{/*  ============ KNOWLEDGE HUB ============  */}
<KnowledgeHub />

{/*  ============ BLOG ============  */}
<Blog />

{/*  ============ TESTIMONIALS ============  */}
<Testimonials />

{/*  ============ FOUNDER ============  */}
<Founder />

{/*  ============ WHY JC TECH ============  */}
<Why />

{/*  ============ CONTACT ============  */}
<Contact />

</main>

{/*  ============ FOOTER ============  */}
<Footer />

<WhatsAppFloat />



    </div>
  );
}

export default App;
