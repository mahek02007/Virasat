import { useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';
import SiteHeader from '../components/SiteHeader';
import Footer from '../components/Footer';
import useAmbience from '../hooks/useAmbience';

const pillarsData = [
  {
    tag: 'PILLAR 01',
    title: 'DISCOVER',
    highlight: "Explore India's Diverse Regions",
    text: "Traverse interactive regional maps from the high passes of Ladakh to Kerala’s sacred groves. Unlock states, districts, and indigenous tribal belts rich in architecture and lore.",
    actionText: 'Explore Cultural Atlas',
    link: '/atlas',
    iconClass: 'icon-discover',
    glowClass: 'pillar-glow-gold',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6" />
        <line x1="8" y1="2" x2="8" y2="18" />
        <line x1="16" y1="6" x2="16" y2="22" />
      </svg>
    )
  },
  {
    tag: 'PILLAR 02',
    title: 'EXPERIENCE',
    highlight: 'Stories, Traditions & Sensory Arts',
    text: 'Witness Ghoomar rhythms, taste Rajasthani spices, decode temple sculpture mudras, and listen to master artisans keep centuries-old handloom crafts alive.',
    actionText: 'Living Journeys',
    link: '/atlas#featuredHeritageSection',
    iconClass: 'icon-experience',
    glowClass: 'pillar-glow-terracotta',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
        <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
      </svg>
    )
  },
  {
    tag: 'PILLAR 03',
    title: 'PLAY',
    highlight: 'Quizzes, Quests & Cultural Badges',
    text: 'Test your knowledge through visual challenges, solve folklore puzzles, complete streaks, and collect authentic digital heritage cards and cultural avatar regalia.',
    actionText: 'Badges & Challenges',
    link: '/atlas',
    iconClass: 'icon-play',
    glowClass: 'pillar-glow-indigo',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="12" cy="8" r="7" />
        <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88" />
      </svg>
    )
  }
];

export default function LandingPage() {
  const [audioPlaying, toggleAudio] = useAmbience();
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animId;
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    const handleResize = () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    };
    window.addEventListener('resize', handleResize);

    const particleCount = 28;
    const particles = [];

    class Particle {
      constructor() {
        this.reset();
      }
      reset() {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.size = Math.random() * 2.2 + 0.8;
        this.speedY = -(Math.random() * 0.45 + 0.15);
        this.speedX = (Math.random() - 0.5) * 0.35;
        this.opacity = Math.random() * 0.6 + 0.2;
        this.fadeSpeed = Math.random() * 0.008 + 0.003;
        this.increasing = Math.random() > 0.5;
      }
      update() {
        this.y += this.speedY;
        this.x += this.speedX;

        if (this.increasing) {
          this.opacity += this.fadeSpeed;
          if (this.opacity >= 0.85) this.increasing = false;
        } else {
          this.opacity -= this.fadeSpeed;
          if (this.opacity <= 0.15) this.increasing = true;
        }

        if (this.y < -10 || this.x < -10 || this.x > width + 10) {
          this.y = height + 10;
          this.x = Math.random() * width;
        }
      }
      draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(212, 175, 55, ${this.opacity})`;
        ctx.shadowBlur = 8;
        ctx.shadowColor = 'rgba(245, 200, 80, 0.6)';
        ctx.fill();
        ctx.shadowBlur = 0;
      }
    }

    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }

    const animateParticles = () => {
      ctx.clearRect(0, 0, width, height);
      particles.forEach((p) => {
        p.update();
        p.draw();
      });
      animId = requestAnimationFrame(animateParticles);
    };

    animateParticles();

    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return (
    <div className="virasat-canvas react-page">
      {/* Red Fort Hero Background with Layered Depth Overlays */}
      <div className="laal-fort-bg-container" aria-hidden="true">
        <img
          src="/assets/red_fort_source.png"
          alt="Historic Red Fort at sunset"
          className="laal-fort-img"
          id="laalFortImg"
        />
        <div className="bg-vignette-overlay" />
        <div className="bg-parchment-gradient" />
        <div className="bg-ornamental-arch" />
        <canvas ref={canvasRef} className="particles-canvas" id="particlesCanvas" />
      </div>

      <SiteHeader onAudioToggle={toggleAudio} audioPlaying={audioPlaying} />

      {/* HERO SECTION */}
      <main className="hero-section" id="hero">
        <div className="hero-content-wrapper">
          {/* Grand Project Identity Positioned Directly Above the Flag in the Sky */}
          <div className="hero-sky-identity">
            <div className="devanagari-sky-badge">
              <span className="devanagari-text">विरासत</span>
              <span className="sky-divider">•</span>
              <span className="sky-badge-label">The Living Heritage of India</span>
            </div>

            <h1 className="hero-title-virasat" id="heroVirasatTitle">
              VIRASAT
            </h1>

            <p className="hero-tagline-text">The Heritage of India</p>
          </div>

          {/* PRIMARY CALL TO ACTION */}
          <div className="hero-cta-group">
            <Link
              to="/atlas"
              className="btn-primary-cta"
              id="primaryCtaBtn"
              aria-label="Try Virasat - Begin your cultural journey"
            >
              <span className="cta-shimmer" />
              <span className="cta-content">
                <span className="cta-title">Try Virasat</span>
                <span className="cta-subtitle">Begin your cultural journey</span>
              </span>
              <span className="cta-icon-wrapper">
                <svg
                  className="cta-arrow-icon"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M5 12h14" />
                  <path d="m12 5 7 7-7 7" />
                </svg>
              </span>
            </Link>

            {/* Explicit Guest Pill Beside Hero CTA */}
            <div className="cta-secondary-row">
              <Link to="/atlas" className="btn-guest-subtle" id="heroGuestBtn">
                <span className="sparkle-icon">✦</span>
                <span>
                  Instant Access: <strong>Continue as Guest</strong>
                </span>
                <span className="badge-free">No Sign Up Needed</span>
              </Link>
              <span className="or-separator">or</span>
              <Link to="/atlas" className="btn-signin-link" id="heroSignInLink">
                Sign In to save progress
              </Link>
            </div>
          </div>
        </div>

        <a href="#pillarsSection" className="scroll-cue" aria-label="Scroll to discover">
          <span style={{ fontSize: '0.75rem', letterSpacing: '0.12em', textTransform: 'uppercase' }}>Discover</span>
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M7 10l5 5 5-5" />
          </svg>
        </a>
      </main>

      {/* FIRST-IMPRESSION TRIAD: DISCOVER, EXPERIENCE, PLAY */}
      <section className="pillars-section" id="pillarsSection">
        <div className="section-ornament-header">
          <div className="ornament-line" />
          <div className="ornament-lotus">
            <svg viewBox="0 0 32 32" width="24" height="24" fill="currentColor">
              <path d="M16 2 C16 9 10 14 6 18 C10 18 14 16 16 12 C18 16 22 18 26 18 C22 14 16 9 16 2 Z M16 13 C14 17 9 20 4 21 C8 23 13 22 16 18 C19 22 24 23 28 21 C23 20 18 17 16 13 Z M16 19 C13 23 9 25 3 26 C9 28 14 27 16 23 C18 27 23 28 29 26 C23 25 19 23 16 19 Z" />
            </svg>
          </div>
          <div className="ornament-line" />
        </div>

        <div className="pillars-container">
          <div className="pillars-intro">
            <span className="section-eyebrow">THE VIRASAT EXPERIENCE</span>
            <h2 className="section-title">A Living World of Heritage</h2>
            <p className="section-desc">
              Experience India not as static history, but through immersive regional narratives, living crafts, and
              interactive quests.
            </p>
          </div>

          {/* The 3 Core Pillars */}
          <div className="pillars-grid">
            {pillarsData.map((pillar) => (
              <Link
                key={pillar.title}
                to={pillar.link}
                className="pillar-card"
                tabIndex={0}
                style={{ textDecoration: 'none', color: 'inherit' }}
              >
                <div className="pillar-card-border" />
                <div className={`pillar-accent-glow ${pillar.glowClass}`} />

                <div className="pillar-header">
                  <div className={`pillar-icon-box ${pillar.iconClass}`}>{pillar.icon}</div>
                  <span className="pillar-tag">{pillar.tag}</span>
                </div>

                <div className="pillar-body">
                  <h3 className="pillar-title">{pillar.title}</h3>
                  <p className="pillar-highlight">{pillar.highlight}</p>
                  <p className="pillar-text">{pillar.text}</p>
                </div>

                <div className="pillar-footer">
                  <span className="pillar-action-pill">
                    <span>{pillar.actionText}</span>
                    <svg viewBox="0 0 20 20" width="16" height="16" fill="currentColor">
                      <path
                        fillRule="evenodd"
                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </span>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* PROJECT OVERVIEW / MANIFESTO SECTION */}
      <section className="project-overview-section" id="projectOverview">
        <div className="overview-container">
          <div className="overview-grid">
            <div className="overview-text-side">
              <span className="section-eyebrow">OUR PHILOSOPHY</span>
              <h2 className="overview-title">Learning Heritage as a Living World</h2>
              <p className="overview-quote">
                “India is not a single monolith of the past — it is a vibrant tapestry of living expressions, indigenous
                ingenuity, and timeless wisdom.”
              </p>
              <p className="overview-paragraph">
                Virasat reimagines cultural documentation. Instead of fragmented encyclopedias or dry textbook pages,
                we unite verified historical archives, regional folk arts, indigenous tribal practices, and AI-guided
                conversational companionship into one cohesive digital journey.
              </p>
              <div className="features-checklist">
                <div className="check-item">
                  <span className="check-bullet">✦</span>
                  <span>Vetted by cultural historians & traditional practitioners</span>
                </div>
                <div className="check-item">
                  <span className="check-bullet">✦</span>
                  <span>Respectful, authentic regional avatar customization</span>
                </div>
                <div className="check-item">
                  <span className="check-bullet">✦</span>
                  <span>Frictionless entry for students, travelers & enthusiasts</span>
                </div>
              </div>

              <div className="overview-cta-box">
                <Link to="/atlas" className="btn-primary-cta sm" id="overviewCtaBtn">
                  <span className="cta-content">
                    <span className="cta-title">ENTER VIRASAT</span>
                  </span>
                  <span className="cta-icon-wrapper">
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2.5">
                      <path d="M5 12h14M12 5l7 7-7 7" />
                    </svg>
                  </span>
                </Link>
                <Link to="/atlas" className="btn-guest-inline" id="overviewGuestBtn">
                  or continue directly as Guest
                </Link>
              </div>
            </div>

            <div className="overview-visual-side">
              {/* Royal Heritage Card Frame displaying the Logo & Fort details */}
              <div className="heritage-showcase-frame">
                <div className="frame-inner-border">
                  <div className="showcase-logo-badge">
                    <img src="/assets/emblem_clean.png" alt="Virasat Emblem" className="showcase-emblem" />
                  </div>
                  <h4 className="showcase-title">VIRASAT</h4>
                  <p className="showcase-subtitle">The Heritage of India</p>

                  <div className="showcase-pillars-summary">
                    <div className="summary-pill">
                      <span className="dot-gold" /> Tangible & Intangible Heritage
                    </div>
                    <Link
                      to="/atlas"
                      className="summary-pill"
                      style={{ cursor: 'pointer', textDecoration: 'none', color: 'inherit' }}
                      title="Explore 28 States & 8 UTs"
                    >
                      <span className="dot-terracotta" /> 28 States & 8 UTs
                    </Link>
                    <div className="summary-pill">
                      <span className="dot-indigo" /> Gamified Quest Journeys
                    </div>
                  </div>

                  <div className="showcase-card-footer">
                    <span className="monument-caption">Featured Gateway: Lal Qila (Red Fort), Delhi</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  );
}