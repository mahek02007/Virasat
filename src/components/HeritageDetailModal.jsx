import { useState, useEffect, useCallback } from 'react';
import { fetchContentItem, fetchPlace } from '../lib/api';

/**
 * HeritageDetailModal
 * Renders full detail view for either a Content Item or a Place from FastAPI.
 *
 * Props:
 * - isOpen: boolean
 * - onClose: () => void
 * - type: 'content' | 'place'
 * - slug: string
 * - initialData: object (fallback/pre-loaded summary)
 * - onNavigatePlace: (placeSlug) => void (optional override)
 * - onNavigateContent: (contentSlug) => void (optional override)
 */
export default function HeritageDetailModal({
  isOpen,
  onClose,
  type = 'content',
  slug,
  initialData = null,
  onNavigatePlace,
  onNavigateContent
}) {
  const [currentType, setCurrentType] = useState(type);
  const [currentSlug, setCurrentSlug] = useState(slug);
  const [detail, setDetail] = useState(initialData);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Sync state when props change
  useEffect(() => {
    setCurrentType(type);
    setCurrentSlug(slug);
    setDetail(initialData);
  }, [type, slug, initialData]);

  // Fetch full details from FastAPI backend
  const loadDetail = useCallback(async (t, s) => {
    if (!s) return;
    setLoading(true);
    setError(null);
    try {
      if (t === 'content') {
        const data = await fetchContentItem(s);
        setDetail(data);
      } else if (t === 'place') {
        const data = await fetchPlace(s);
        setDetail(data);
      }
    } catch (err) {
      console.warn(`[Virasat] Failed to fetch ${t} detail for "${s}":`, err.message);
      setError(err.message || 'Unable to retrieve archive record.');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    if (isOpen && currentSlug) {
      loadDetail(currentType, currentSlug);
    }
  }, [isOpen, currentType, currentSlug, loadDetail]);

  // Escape key handler
  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const handlePlaceClick = (placeSlug) => {
    if (onNavigatePlace) {
      onNavigatePlace(placeSlug);
    } else {
      setCurrentType('place');
      setCurrentSlug(placeSlug);
      setDetail(null);
    }
  };

  const handleContentClick = (contentSlug) => {
    if (onNavigateContent) {
      onNavigateContent(contentSlug);
    } else {
      setCurrentType('content');
      setCurrentSlug(contentSlug);
      setDetail(null);
    }
  };

  const isContent = currentType === 'content';
  const title = detail?.title || detail?.name || initialData?.title || initialData?.name || 'Heritage Archive';
  const subtitle = detail?.subtitle || detail?.region_id || initialData?.subtitle || '';
  const description = detail?.description || detail?.summary || initialData?.summary || initialData?.description || '';
  const primaryImg = detail?.media_items?.[0]?.url || detail?.primary_image || initialData?.image || null;

  return (
    <div
      className="auth-modal-backdrop heritage-modal-backdrop"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-labelledby="heritageModalTitle"
    >
      <div
        className="auth-modal-card heritage-modal-card"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="heritage-modal-header">
          <div className="heritage-modal-badge-row">
            <span className="heritage-modal-type-badge">
              {isContent
                ? (detail?.content_type || 'HERITAGE CONTENT').toUpperCase().replace(/_/g, ' ')
                : 'HERITAGE PLACE & SITE'}
            </span>
            {detail?.region_id && (
              <span className="heritage-modal-region-badge">
                📍 {detail.region_id.toUpperCase()}
              </span>
            )}
            {detail?.unesco_status && (
              <span className="heritage-modal-unesco-badge">
                🏛️ {detail.unesco_status}
              </span>
            )}
            {detail?.is_gi_tagged && (
              <span className="heritage-modal-gi-badge">
                🏷️ GI TAGGED {detail.gi_year ? `(${detail.gi_year})` : ''}
              </span>
            )}
          </div>
          <button
            type="button"
            className="auth-modal-close-btn"
            onClick={onClose}
            aria-label="Close details"
          >
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2.5">
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
          </button>
        </div>

        {/* Content Body */}
        <div className="heritage-modal-scroll-body">
          {loading && !detail && (
            <div className="heritage-modal-loading">
              <div className="heritage-loading-spinner" />
              <p>Consulting Virasat Cultural Archives…</p>
            </div>
          )}

          {error && !detail && (
            <div className="heritage-modal-error">
              <span style={{ fontSize: '2rem' }}>⚠️</span>
              <h4>Archive Retrieval Notice</h4>
              <p>{error}</p>
              <button
                type="button"
                className="heritage-modal-retry-btn"
                onClick={() => loadDetail(currentType, currentSlug)}
              >
                ↻ Retry Archive Query
              </button>
            </div>
          )}

          {/* Title & Subtitle */}
          <div className="heritage-modal-title-group">
            <h2 id="heritageModalTitle" className="heritage-modal-title">
              {title}
            </h2>
            {subtitle && (
              <p className="heritage-modal-subtitle">{subtitle}</p>
            )}
          </div>

          {/* Media Banner / Image */}
          {primaryImg && (
            <div className="heritage-modal-media-frame">
              <img
                src={primaryImg.startsWith('/') || primaryImg.startsWith('http') ? primaryImg : `/${primaryImg}`}
                alt={detail?.media_items?.[0]?.alt_text || title}
                className="heritage-modal-img"
              />
              {detail?.media_items?.[0]?.attribution && (
                <span className="heritage-modal-attribution">
                  Source: {detail.media_items[0].attribution}
                </span>
              )}
            </div>
          )}

          {/* Quick Meta Row */}
          <div className="heritage-modal-meta-grid">
            {detail?.period && (
              <div className="heritage-meta-item">
                <span className="meta-label">Period / Era</span>
                <span className="meta-value">{detail.period}</span>
              </div>
            )}
            {detail?.historical_era && (
              <div className="heritage-meta-item">
                <span className="meta-label">Dynasty / History</span>
                <span className="meta-value">{detail.historical_era}</span>
              </div>
            )}
            {detail?.address && (
              <div className="heritage-meta-item heritage-meta-item-full">
                <span className="meta-label">Location & Address</span>
                <span className="meta-value">{detail.address}</span>
              </div>
            )}
            {detail?.latitude != null && detail?.longitude != null && (
              <div className="heritage-meta-item">
                <span className="meta-label">Geo Coordinates</span>
                <span className="meta-value">
                  {detail.latitude.toFixed(4)}° N, {detail.longitude.toFixed(4)}° E
                </span>
              </div>
            )}
          </div>

          {/* Description */}
          <div className="heritage-modal-section">
            <h4 className="section-label">CULTURAL NARRATIVE & OVERVIEW</h4>
            <div className="heritage-modal-desc">
              {description.split('\n\n').map((paragraph, i) => (
                <p key={i}>{paragraph}</p>
              ))}
            </div>
          </div>

          {/* Associated Place (if viewing content item) */}
          {isContent && detail?.place && (
            <div className="heritage-modal-section">
              <h4 className="section-label">ASSOCIATED HERITAGE SITE</h4>
              <button
                type="button"
                className="heritage-associated-place-card"
                onClick={() => handlePlaceClick(detail.place.slug)}
              >
                <div className="place-icon-box">🏛️</div>
                <div className="place-text-box">
                  <span className="place-name">{detail.place.name}</span>
                  <span className="place-sub">{detail.place.address || 'Explore site details'}</span>
                </div>
                <span className="place-arrow">View Site →</span>
              </button>
            </div>
          )}

          {/* Associated Content Items (if viewing place) */}
          {!isContent && Array.isArray(detail?.content_items) && detail.content_items.length > 0 && (
            <div className="heritage-modal-section">
              <h4 className="section-label">HERITAGE AT THIS SITE</h4>
              <div className="heritage-associated-content-grid">
                {detail.content_items.map((ci) => (
                  <button
                    key={ci.id || ci.slug}
                    type="button"
                    className="heritage-associated-item-pill"
                    onClick={() => handleContentClick(ci.slug)}
                  >
                    <span className="item-pill-title">{ci.title}</span>
                    <span className="item-pill-type">{(ci.subtype || ci.content_type).replace(/_/g, ' ')}</span>
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Item Metadata Attributes */}
          {detail?.item_metadata && Object.keys(detail.item_metadata).length > 0 && (
            <div className="heritage-modal-section">
              <h4 className="section-label">KEY ATTRIBUTES</h4>
              <div className="heritage-metadata-chips">
                {Object.entries(detail.item_metadata).map(([k, v]) => (
                  <div className="meta-chip" key={k}>
                    <span className="meta-chip-k">{k.replace(/_/g, ' ')}:</span>
                    <span className="meta-chip-v">{String(v)}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Tags */}
          {Array.isArray(detail?.tags) && detail.tags.length > 0 && (
            <div className="heritage-modal-section">
              <h4 className="section-label">TAGS & SUBJECTS</h4>
              <div className="heritage-modal-tags">
                {detail.tags.map((tag) => (
                  <span className="heritage-tag-pill" key={tag}>
                    #{tag}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* Sources and References */}
          {Array.isArray(detail?.sources) && detail.sources.length > 0 && (
            <div className="heritage-modal-section">
              <h4 className="section-label">VERIFIED SOURCES & ARCHIVES</h4>
              <ul className="heritage-sources-list">
                {detail.sources.map((src) => (
                  <li key={src.id || src.title} className="heritage-source-item">
                    <span className="source-title">{src.title}</span>
                    {src.publisher && <span className="source-publisher"> — {src.publisher}</span>}
                    {src.citation_text && <p className="source-citation">{src.citation_text}</p>}
                    {src.url && (
                      <a
                        href={src.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="source-link"
                      >
                        External Archive Link ↗
                      </a>
                    )}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="heritage-modal-footer">
          <button
            type="button"
            className="heritage-modal-close-action-btn"
            onClick={onClose}
          >
            Close Archive
          </button>
        </div>
      </div>
    </div>
  );
}
