import { Link } from 'react-router-dom';

export default function SiteHeader({ atlas = false, onAudioToggle, audioPlaying = false, search, onSignIn }) {
  return (
    <header className={atlas ? 'home-header' : 'virasat-header'} id={atlas ? 'atlasHeader' : 'mainHeader'}>
      <div className={atlas ? 'home-header-container' : 'header-container'}>
        <Link to="/" className={atlas ? 'home-brand-link' : 'brand-link'} id="brandHomeLink" aria-label="Virasat Home">
          {atlas ? (
            <>
              <div className="home-brand-logo-frame">
                <img src="/assets/emblem_clean.png" alt="Virasat Emblem" className="home-brand-emblem" />
              </div>
              <div className="home-brand-text">
                <span className="home-brand-name">VIRASAT</span>
                <span className="home-brand-sub">The Heritage of India</span>
              </div>
            </>
          ) : (
            <img src="/assets/logo_source.jpg" alt="Virasat — Heritage of India" className="brand-full-logo" />
          )}
        </Link>

        <nav className={atlas ? 'home-nav-links' : 'main-nav'} aria-label="Primary Navigation">
          {atlas ? (
            <>
              <Link to="/atlas" className="home-nav-link nav-link active">
                <span className="nav-num">01</span> Discover
              </Link>
              <a href="#featuredHeritageSection" className="home-nav-link nav-link">
                <span className="nav-num">02</span> Experience
              </a>
              <a href="#didYouKnowSection" className="home-nav-link nav-link">
                <span className="nav-num">03</span> Stories
              </a>
              <a href="/#projectOverview" className="home-nav-link nav-link">
                <span className="nav-num">04</span> About
              </a>
            </>
          ) : (
            <>
              <a href="#pillarsSection" className="nav-link">
                <span className="nav-num">01</span> Discover
              </a>
              <a href="#pillarsSection" className="nav-link" data-pillar="experience">
                <span className="nav-num">02</span> Experience
              </a>
              <a href="#pillarsSection" className="nav-link" data-pillar="play">
                <span className="nav-num">03</span> Play
              </a>
              <a href="#projectOverview" className="nav-link">
                <span className="nav-num">04</span> About
              </a>
            </>
          )}
        </nav>

        <div className={atlas ? 'home-header-actions' : 'header-actions'}>
          <button
            id="ambientSoundToggle"
            className={`audio-pill-btn ${audioPlaying ? 'playing' : ''}`}
            onClick={onAudioToggle}
            aria-label="Toggle Cultural Soundscape"
            title="Atmosphere: Tanpura Ambience"
          >
            <span className="audio-icon-wave">
              <span /><span /><span /><span />
            </span>
            <span className="audio-label">Ambience</span>
            <span className="audio-status" id="audioStatusText">{audioPlaying ? 'Live' : 'Off'}</span>
          </button>

          {atlas ? (
            search
          ) : (
            <>
              <Link to="/atlas" className="btn-guest-quick" id="quickGuestBtn" title="Explore immediately without signing in">
                <span className="guest-dot" />
                Continue as Guest
              </Link>
              <Link to="/atlas" className="btn-signin-nav" id="navSignInBtn" onClick={onSignIn} title="Sign In to save progress">
                <svg className="icon-user" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                  <circle cx="12" cy="7" r="4" />
                </svg>
                Sign In
              </Link>
            </>
          )}
        </div>
      </div>
    </header>
  );
}