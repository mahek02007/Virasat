import { Link, useLocation } from 'react-router-dom';

export default function SiteHeader({ atlas = false, onAudioToggle, audioPlaying = false, search }) {
  const location = useLocation();
  return (
    <header className={atlas ? 'home-header' : 'virasat-header'}>
      <div className={atlas ? 'home-header-container' : 'header-container'}>
        <Link to="/" className={atlas ? 'home-brand-link' : 'brand-link'} aria-label="Virasat Home">
          {atlas ? (
            <>
              <div className="home-brand-logo-frame"><img src="/assets/emblem_clean.png" alt="Virasat Emblem" className="home-brand-emblem" /></div>
              <div className="home-brand-text"><span className="home-brand-name">VIRASAT</span><span className="home-brand-sub">The Heritage of India</span></div>
            </>
          ) : <img src="/assets/logo_source.jpg" alt="Virasat — Heritage of India" className="brand-full-logo" />}
        </Link>
        <nav className={atlas ? 'home-nav-links' : 'main-nav'} aria-label="Primary Navigation">
          <Link to={atlas ? '/atlas' : '#pillarsSection'} className="home-nav-link nav-link active"><span className="nav-num">01</span> Discover</Link>
          <a href={atlas ? '#featuredHeritageSection' : '#pillarsSection'} className={atlas ? 'home-nav-link' : 'nav-link'}><span className="nav-num">02</span> Experience</a>
          <a href={atlas ? '#didYouKnowSection' : '#pillarsSection'} className={atlas ? 'home-nav-link' : 'nav-link'}><span className="nav-num">03</span> {atlas ? 'Stories' : 'Play'}</a>
          <a href={atlas ? '/#projectOverview' : '#projectOverview'} className={atlas ? 'home-nav-link' : 'nav-link'}><span className="nav-num">04</span> About</a>
        </nav>
        <div className={atlas ? 'home-header-actions' : 'header-actions'}>
          <button className={`audio-pill-btn ${audioPlaying ? 'playing' : ''}`} onClick={onAudioToggle} aria-label="Toggle Cultural Soundscape">
            <span className="audio-icon-wave"><span /><span /><span /><span /></span><span className="audio-label">Ambience</span><span className="audio-status">{audioPlaying ? 'Live' : 'Off'}</span>
          </button>
          {atlas ? search : <Link to="/atlas" className="btn-guest-quick"><span className="guest-dot" /> Continue as Guest</Link>}
        </div>
      </div>
    </header>
  );
}