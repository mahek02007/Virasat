import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <footer className="virasat-footer">
      <div className="footer-container">
        <div className="footer-brand-side">
          <div className="footer-brand">
            <div className="footer-logo-frame">
              <img src="/assets/emblem_clean.png" alt="Virasat Emblem" className="footer-logo" />
            </div>
            <div>
              <span className="footer-title">VIRASAT</span>
              <span className="footer-sub">The Heritage of India</span>
            </div>
          </div>
          <p className="footer-mission">
            Preserving, celebrating, and experiencing India's rich cultural tapestry through modern digital exploration.
          </p>
        </div>

        <div className="footer-links-group">
          <div className="footer-col">
            <span className="footer-heading">Platform</span>
            <Link to="/" className="f-link">Home</Link>
            <Link to="/atlas#culturalAtlasSection" className="f-link">Discover</Link>
            <Link to="/atlas#featuredHeritageSection" className="f-link">Experience</Link>
            <Link to="/atlas" className="f-link">Play</Link>
          </div>

          <div className="footer-col">
            <span className="footer-heading">Access</span>
            <Link to="/atlas" className="f-link" id="footerGuestBtn">Continue as Guest</Link>
            <Link to="/atlas" className="f-link" id="footerSignInBtn">Sign In</Link>
            <a href="/#projectOverview" className="f-link">About Project</a>
          </div>

          <div className="footer-col">
            <span className="footer-heading">Authenticity</span>
            <span className="f-text">National Cultural Repository</span>
            <span className="f-text">Ministry of Culture</span>
            <span className="f-text">INTACH Research Protocols</span>
          </div>
        </div>
      </div>

      <div className="footer-bottom-bar">
        <p className="copyright-text">© 2026 Virasat — The Heritage of India. Designed for timeless cultural discovery.</p>
        <div className="footer-devanagari">सत्यमेव जयते • विविधता में एकता</div>
      </div>
    </footer>
  );
}