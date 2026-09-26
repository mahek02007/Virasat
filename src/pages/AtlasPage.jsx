import { useEffect, useMemo, useRef, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import data from '../data';
import SiteHeader from '../components/SiteHeader';
import Footer from '../components/Footer';
import SearchBox from '../components/SearchBox';
import useAmbience from '../hooks/useAmbience';
import { fetchRegions, fetchContent, fetchPlaces } from '../lib/api';
import HeritageDetailModal from '../components/HeritageDetailModal';

const zones = [['all', 'All Regions'], ['north', 'Northern Valleys'], ['west', 'Western Desert & Coast'], ['central', 'Central Heartland'], ['east', 'Eastern Delta'], ['south', 'Southern Peninsula'], ['northeast', 'Northeastern Hills']];
const pilotRegionIds = ['rajasthan', 'maharashtra', 'tamil-nadu', 'kerala', 'jammu-kashmir', 'west-bengal', 'gujarat', 'madhya-pradesh', 'odisha', 'assam'];

// ---------------------------------------------------------------------------
// Normalise API RegionSummary → the shape used by map/popover components.
// The API returns snake_case; the original static data used camelCase and a
// nested `coords` object.  We keep both representations compatible here so
// every downstream component can use the same field access pattern.
// ---------------------------------------------------------------------------
function normaliseRegion(r, fallbackRegion) {
  return {
    ...r,
    // coords object expected by AtlasMap / RegionPopover
    coords: {
      x: r.coord_x ?? r.coords?.x ?? fallbackRegion?.coords?.x ?? 50,
      y: r.coord_y ?? r.coords?.y ?? fallbackRegion?.coords?.y ?? 50,
    },
    // camelCase aliases for colour accent
    colorAccent: r.color_accent ?? null,
  };
}

// ---------------------------------------------------------------------------
// Hook: useRegionsData
// Fetches from GET /api/v1/regions and falls back to static window data if
// the backend is unavailable (so the atlas still renders in offline dev).
// ---------------------------------------------------------------------------
function useRegionsData() {
  const staticById = useMemo(
    () => new Map((data?.regions ?? []).map((region) => [region.id, region])),
    []
  );
  const staticRegions = useMemo(
    () => (data?.regions ?? []).map((region) => normaliseRegion(region, region)),
    [staticById]
  );
  const [regions, setRegions] = useState(staticRegions);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;
    fetchRegions()
      .then((apiRegions) => {
        if (cancelled) return;
        const normalised = apiRegions.map((region) =>
          normaliseRegion(region, staticById.get(region.id) || staticById.get(region.slug))
        );
        // Merge API data with static data so any region missing from the
        // backend (e.g. not yet seeded) still appears on the map.
        const apiIds = new Set(normalised.map((r) => r.id));
        const staticOnly = staticRegions.filter((r) => !apiIds.has(r.id));
        setRegions([...normalised, ...staticOnly]);
        setLoading(false);
      })
      .catch((err) => {
        if (cancelled) return;
        console.warn('[Virasat] Could not reach API; falling back to static data.', err.message);
        setError(err.message);
        setLoading(false);
        // Keep staticRegions already set as the fallback
      });
    return () => { cancelled = true; };
  }, [staticById, staticRegions]);

  return { regions, loading, error };
}

// ---------------------------------------------------------------------------
// Components (UI unchanged from original)
// ---------------------------------------------------------------------------

function RegionPopover({ region, onExplore }) {
  if (!region) return null;
  let left = region.coords.x;
  if (left < 22) left = 22;
  if (left > 78) left = 78;
  return (
    <div className="region-popover-card active" style={{ left: `${left}%`, top: `${region.coords.y}%` }}>
      <div className="popover-header">
        <div className="popover-name-block">
          <span className="popover-region-name">{region.name}</span>
          <span className="popover-devanagari">{region.devanagari || ''}</span>
        </div>
        <span className="popover-status-badge">{region.badge || 'Available'}</span>
      </div>
      <p className="popover-tagline">{region.tagline}</p>
      <div className="popover-categories-chips">
        {(region.categories || []).map(category => (
          <span className="popover-category-chip" key={category}>{category}</span>
        ))}
      </div>
      <p className="popover-summary">{region.summary}</p>
      <button className="popover-explore-cta" onClick={() => onExplore(region.id)}>
        Explore {region.name} →
      </button>
    </div>
  );
}

function AtlasMap({ regions, zone, selected, setSelected, navigate }) {
  const pilotRegions = pilotRegionIds
    .map(id => regions.find(r => r.id === id || r.slug === id))
    .filter(Boolean);

  return (
    <div className="atlas-map-card">
      <div className="map-frame-header">
        <div className="map-frame-title-group">
          <span className="map-frame-compass-icon">✧</span>
          <div>
            <h3 className="map-frame-title">Cultural Atlas of Bharat</h3>
            <span className="map-frame-subtitle">भारत का सांस्कृतिक मानचित्र</span>
          </div>
        </div>
        <span className="map-instructions-pill">✦ Hover region to preview • Click to explore</span>
      </div>
      <div className="map-canvas-container">
        <img src="/assets/india_map_cultural.jpg" alt="Textured cultural map of India" className="map-base-image" />
        <div
          className="map-interactive-layer"
          onClick={event => {
            if (!event.target.closest('.region-beacon') && !event.target.closest('.region-popover-card'))
              setSelected(null);
          }}
        >
          {regions.map(region => (
            <button
              key={region.id}
              className={`region-beacon ${zone !== 'all' && zone !== region.zone ? 'dimmed' : ''} ${selected?.id === region.id ? 'active' : ''}`}
              style={{ left: `${region.coords.x}%`, top: `${region.coords.y}%` }}
              onMouseEnter={() => setSelected(region)}
              onFocus={() => setSelected(region)}
              onClick={() => navigate(region.id)}
              aria-label={`Explore ${region.name} - ${region.tagline}`}
            >
              <span className="beacon-core">
                <span className="beacon-pulse" style={{ background: region.colorAccent || 'rgba(200,90,50,0.45)' }} />
                <span className="beacon-dot" style={{ background: region.colorAccent || 'var(--ei-terracotta)' }} />
              </span>
              <span className="beacon-label">{region.name}</span>
            </button>
          ))}
          <RegionPopover region={selected} onExplore={navigate} />
        </div>
      </div>
      <div className="map-quick-regions-bar">
        <span className="quick-regions-label">Pilot Regions:</span>
        {pilotRegions.map(region => (
          <button
            className={`quick-region-pill ${selected?.id === region.id ? 'active' : ''}`}
            key={region.id}
            onMouseEnter={() => setSelected(region)}
            onClick={() => navigate(region.id)}
          >
            {region.name}
          </button>
        ))}
      </div>
    </div>
  );
}

function GuidesCard() {
  const greetings = data.userJourney.avatarGreetings;
  const [index, setIndex] = useState(0);
  const [speaking, setSpeaking] = useState(false);
  const speak = () => {
    const greeting = greetings[index];
    if (!window.speechSynthesis) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(greeting.speechText || greeting.text);
    utterance.lang = greeting.langCode;
    utterance.onend = () => setSpeaking(false);
    setSpeaking(true);
    window.speechSynthesis.speak(utterance);
  };
  return (
    <div className="cultural-guides-card">
      <div className="guides-header">
        <h3 className="guides-title">Cultural Guides</h3>
        <span className="guides-badge">Living Bharat</span>
      </div>
      <div className={`avatar-speech-bubble ${speaking ? 'speaking' : ''}`}>
        <div className="bubble-actions-row">
          <button className="btn-cycle-greeting" onClick={() => { setIndex((index + 1) % greetings.length); speak(); }}>↻ Switch</button>
          <button className="btn-voiceover-greeting" onClick={speak}>🔊 {speaking ? 'Speaking...' : 'Listen'}</button>
        </div>
        <div className="bubble-greeting-native">{greetings[index].text}</div>
        <div className="bubble-greeting-roman">{greetings[index].roman}</div>
      </div>
      <button className="avatar-frame" onClick={() => { setIndex((index + 1) % greetings.length); speak(); }}>
        <img src="/assets/namaste_avatar.jpg" alt="Cultural guides of India greeting visitors" className="avatar-image" />
        <span className="avatar-caption-bar">Cultural Harmony • 5 Living Traditions of India</span>
      </button>
    </div>
  );
}

function JourneyCard() {
  const journey = data.userJourney;
  return (
    <div className="journey-progress-card">
      <div className="journey-card-header">
        <div className="journey-title-group">
          <span className="journey-compass-icon">✧</span>
          <h3 className="journey-title">Your Journey</h3>
        </div>
        <span className="journey-rank-badge">{journey.rank}</span>
      </div>
      <div className="journey-stat-row">
        <div>
          <span className="journey-count-text">{journey.exploredCount} / {journey.totalRegions}</span>
          <span className="journey-count-sub">regions explored</span>
        </div>
        <span className="journey-percent-text">{journey.progressPercent}% Discovered</span>
      </div>
      <div className="journey-progress-track">
        <div className="journey-progress-fill" style={{ width: `${journey.progressPercent}%` }} />
      </div>
      <div className="milestone-reward-box">
        <div className="reward-icon-badge">🏰</div>
        <div className="reward-info-group">
          <span className="reward-label">Next Reward Unlocked</span>
          <span className="reward-name">Mehrangarh Royal Seal Card</span>
          <span className="reward-sub">Explore Rajasthan to claim full regalia badge</span>
        </div>
      </div>
    </div>
  );
}

function FactSection() {
  const [index, setIndex] = useState(0);
  const fact = data.facts[index];
  return (
    <section className="did-you-know-section" id="didYouKnowSection">
      <div className="dyk-card">
        <div className="dyk-content-side">
          <div className="dyk-badge-row">
            <span className="dyk-eyebrow">💡 DID YOU KNOW?</span>
            <span className="dyk-region-pill">{fact.region}</span>
          </div>
          <h3 className="dyk-quote">"{fact.quote}"</h3>
          <p className="dyk-description">{fact.description}</p>
          <div className="dyk-actions">
            <a href={fact.exploreLink} className="dyk-story-link">Explore this story →</a>
            <button className="btn-dyk-next" onClick={() => setIndex((index + 1) % data.facts.length)}>Next Heritage Fact ↻</button>
          </div>
        </div>
        <div className="dyk-visual-side">
          <div className="dyk-diya-badge">🪔</div>
        </div>
      </div>
    </section>
  );
}

function FeaturedSection({ onOpenDetail }) {
  const [tab, setTab] = useState('content'); // 'content' | 'places'
  const [contentList, setContentList] = useState([]);
  const [placesList, setPlacesList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [usingFallback, setUsingFallback] = useState(false);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);

    Promise.allSettled([
      fetchContent({ limit: 12 }),
      fetchPlaces(),
    ])
      .then(([contentRes, placesRes]) => {
        if (cancelled) return;
        let hasData = false;
        if (contentRes.status === 'fulfilled' && Array.isArray(contentRes.value) && contentRes.value.length > 0) {
          setContentList(contentRes.value);
          hasData = true;
        }
        if (placesRes.status === 'fulfilled' && Array.isArray(placesRes.value) && placesRes.value.length > 0) {
          setPlacesList(placesRes.value);
          hasData = true;
        }
        if (!hasData) {
          setUsingFallback(true);
        }
        setLoading(false);
      })
      .catch(() => {
        if (cancelled) return;
        setUsingFallback(true);
        setLoading(false);
      });

    return () => {
      cancelled = true;
    };
  }, []);

  const renderContentCards = () => {
    if (usingFallback || contentList.length === 0) {
      return data.featuredHeritage.map(card => (
        <div
          key={card.id}
          className="heritage-card react-heritage-clickable"
          onClick={() => onOpenDetail({ type: 'content', slug: card.id, initialData: card })}
          role="button"
          tabIndex={0}
          onKeyDown={e => {
            if (e.key === 'Enter') onOpenDetail({ type: 'content', slug: card.id, initialData: card });
          }}
        >
          <div className="card-image-box">
            <img src={`/${card.image}`} alt={card.title} className="card-img" />
            <span className="card-category-badge">{card.category}</span>
          </div>
          <div className="card-body">
            <h3 className="card-title">{card.title}</h3>
            <span className="card-subtitle">{card.subtitle}</span>
            <p className="card-summary">{card.summary}</p>
            <div className="card-footer-row">
              <span className="card-read-time">{card.readTime}</span>
              <span className="card-explore-arrow">Explore Details →</span>
            </div>
          </div>
        </div>
      ));
    }

    return contentList.map(item => {
      const fallbackImg = '/assets/featured_dance.jpg';
      const imgUrl = item.primary_image || fallbackImg;
      return (
        <div
          key={item.id || item.slug}
          className="heritage-card react-heritage-clickable"
          onClick={() => onOpenDetail({ type: 'content', slug: item.slug, initialData: item })}
          role="button"
          tabIndex={0}
          onKeyDown={e => {
            if (e.key === 'Enter') onOpenDetail({ type: 'content', slug: item.slug, initialData: item });
          }}
        >
          <div className="card-image-box">
            <img
              src={imgUrl.startsWith('http') || imgUrl.startsWith('/') ? imgUrl : `/${imgUrl}`}
              alt={item.title}
              className="card-img"
            />
            <span className="card-category-badge">
              {(item.subtype || item.content_type).replace(/_/g, ' ')}
            </span>
          </div>
          <div className="card-body">
            <h3 className="card-title">{item.title}</h3>
            <span className="card-subtitle">
              {item.subtitle || item.period || (item.region_id && item.region_id.toUpperCase())}
            </span>
            <p className="card-summary">{item.summary}</p>
            <div className="card-footer-row">
              <span className="card-read-time">
                {item.unesco_status ? '🏛️ UNESCO' : item.is_gi_tagged ? '🏷️ GI Tagged' : 'Living Heritage'}
              </span>
              <span className="card-explore-arrow">Explore Details →</span>
            </div>
          </div>
        </div>
      );
    });
  };

  const renderPlaceCards = () => {
    if (placesList.length === 0) {
      return (
        <p style={{ gridColumn: '1 / -1', textAlign: 'center', color: '#c5b49e', padding: '2rem' }}>
          No heritage places listed yet.
        </p>
      );
    }

    return placesList.map(place => (
      <div
        key={place.id || place.slug}
        className="heritage-card react-heritage-clickable"
        onClick={() => onOpenDetail({ type: 'place', slug: place.slug, initialData: place })}
        role="button"
        tabIndex={0}
        onKeyDown={e => {
          if (e.key === 'Enter') onOpenDetail({ type: 'place', slug: place.slug, initialData: place });
        }}
      >
        <div className="card-image-box place-card-image-box">
          <div className="place-card-banner">
            <span className="place-card-pin">🏛️</span>
            <span className="place-card-region">{place.region_id?.toUpperCase()}</span>
          </div>
          <span className="card-category-badge">HERITAGE SITE</span>
        </div>
        <div className="card-body">
          <h3 className="card-title">{place.name}</h3>
          <span className="card-subtitle">
            {place.address || (place.latitude != null ? `${place.latitude.toFixed(2)}° N, ${place.longitude.toFixed(2)}° E` : '')}
          </span>
          <p className="card-summary">{place.description || 'Sacred landmark and heritage site.'}</p>
          <div className="card-footer-row">
            <span className="card-read-time">Monument & Site</span>
            <span className="card-explore-arrow">View Site Archive →</span>
          </div>
        </div>
      </div>
    ));
  };

  return (
    <section className="featured-heritage-section" id="featuredHeritageSection">
      <div className="featured-section-header">
        <span className="featured-eyebrow">CURATED EXPLORATIONS</span>
        <h2 className="featured-title">Featured Heritage & Places</h2>
        <p className="featured-subtitle">Explore living arts, ancient sanctums, and timeless celebrations from live archives.</p>
        
        {/* API Switcher Tabs */}
        <div className="featured-tabs-strip">
          <button
            type="button"
            className={`featured-tab-pill ${tab === 'content' ? 'active' : ''}`}
            onClick={() => setTab('content')}
          >
            Living Traditions & Arts ({usingFallback ? 'Offline Archive' : contentList.length || '...'})
          </button>
          <button
            type="button"
            className={`featured-tab-pill ${tab === 'places' ? 'active' : ''}`}
            onClick={() => setTab('places')}
          >
            Sacred Places & Monuments ({placesList.length || '...'})
          </button>
        </div>
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', color: '#c8943b', padding: '3rem' }}>
          <div className="heritage-loading-spinner" style={{ margin: '0 auto 1rem' }} />
          <p>Retrieving curated heritage items from Virasat API…</p>
        </div>
      ) : (
        <div className="featured-cards-grid">
          {tab === 'content' ? renderContentCards() : renderPlaceCards()}
        </div>
      )}
    </section>
  );
}

// ---------------------------------------------------------------------------
// Atlas loading / error overlays
// ---------------------------------------------------------------------------

function MapLoadingOverlay() {
  return (
    <div className="atlas-map-card" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: 420 }}>
      <div style={{ textAlign: 'center', color: 'var(--ei-gold, #c8943b)', padding: '2rem' }}>
        <div style={{ fontSize: '2rem', marginBottom: '0.75rem' }}>🗺️</div>
        <p style={{ margin: 0, fontFamily: 'inherit', fontSize: '0.95rem', opacity: 0.8 }}>Loading cultural atlas…</p>
      </div>
    </div>
  );
}

function MapErrorBanner({ message }) {
  return (
    <div
      style={{
        background: 'rgba(200,60,30,0.12)',
        border: '1px solid rgba(200,60,30,0.35)',
        borderRadius: '8px',
        color: '#c83c1e',
        fontSize: '0.82rem',
        padding: '0.6rem 1rem',
        marginBottom: '0.75rem',
      }}
      role="alert"
    >
      ⚠️ Could not reach the Virasat API — showing cached atlas data. ({message})
    </div>
  );
}

// ---------------------------------------------------------------------------
// AtlasPage (main export)
// ---------------------------------------------------------------------------

export default function AtlasPage() {
  const navigate = useNavigate();
  const [zone, setZone] = useState('all');
  const [selected, setSelected] = useState(null);
  const [audioPlaying, toggleAudio] = useAmbience();

  const { regions, loading, error } = useRegionsData();

  const selectedFromHash = useMemo(
    () => regions.find(r => r.id === window.location.hash.slice(1) || r.slug === window.location.hash.slice(1)),
    [regions]
  );

  useEffect(() => {
    if (selectedFromHash) setSelected(selectedFromHash);
    const dismiss = event => {
      if (
        !event.target.closest('.region-popover-card') &&
        !event.target.closest('.region-beacon') &&
        !event.target.closest('.quick-region-pill')
      )
        setSelected(null);
    };
    document.addEventListener('click', dismiss);
    return () => document.removeEventListener('click', dismiss);
  }, [selectedFromHash]);

  const goToRegion = id => {
    const cleanId = String(id).toLowerCase().trim();
    if (cleanId === 'maharashtra' || cleanId === 'odisha' || cleanId === 'puri')
      navigate(`/regions/${cleanId === 'puri' ? 'odisha' : cleanId}`);
    else
      window.location.href = `explore.html?region=${encodeURIComponent(cleanId)}`;
  };

  const [activeDetail, setActiveDetail] = useState({
    isOpen: false,
    type: 'content',
    slug: '',
    initialData: null,
  });

  const handleOpenDetail = ({ type, slug, initialData }) => {
    setActiveDetail({
      isOpen: true,
      type: type || 'content',
      slug,
      initialData: initialData || null,
    });
  };

  const handleCloseDetail = () => {
    setActiveDetail(prev => ({ ...prev, isOpen: false }));
  };

  return (
    <div className="home-page-body react-page">
      <SiteHeader atlas onAudioToggle={toggleAudio} audioPlaying={audioPlaying} search={<SearchBox data={data} />} />
      <main>
        <section className="cultural-atlas-section" id="culturalAtlasSection">
          <div className="atlas-section-header">
            <span className="atlas-eyebrow">INTERACTIVE CULTURAL ATLAS</span>
            <h1 className="atlas-title">Explore India</h1>
            <p className="atlas-subtitle">Choose a region and begin your cultural journey.</p>
            <div className="zone-filters-strip" role="tablist">
              {zones.map(([id, label]) => (
                <button
                  className={`zone-filter-pill ${zone === id ? 'active' : ''}`}
                  data-zone={id}
                  key={id}
                  onClick={() => { setZone(id); setSelected(null); }}
                  role="tab"
                  aria-selected={zone === id}
                >
                  {label}
                </button>
              ))}
            </div>
          </div>
          <div className="atlas-composition-layout">
            <div style={{ flex: 1, minWidth: 0 }}>
              {error && <MapErrorBanner message={error} />}
              {loading
                ? <MapLoadingOverlay />
                : <AtlasMap regions={regions} zone={zone} selected={selected} setSelected={setSelected} navigate={goToRegion} />
              }
            </div>
            <div className="atlas-journey-column">
              <GuidesCard />
              <JourneyCard />
            </div>
          </div>
        </section>
        <FactSection />
        <FeaturedSection onOpenDetail={handleOpenDetail} />
      </main>
      <Footer />
      <HeritageDetailModal
        isOpen={activeDetail.isOpen}
        onClose={handleCloseDetail}
        type={activeDetail.type}
        slug={activeDetail.slug}
        initialData={activeDetail.initialData}
        onNavigatePlace={(placeSlug) => handleOpenDetail({ type: 'place', slug: placeSlug })}
        onNavigateContent={(contentSlug) => handleOpenDetail({ type: 'content', slug: contentSlug })}
      />
    </div>
  );
}
