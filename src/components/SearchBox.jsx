import { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';

export default function SearchBox({ data }) {
  const [query, setQuery] = useState('');
  const normalized = query.trim().toLowerCase();
  const results = useMemo(() => normalized ? data.searchIndex.filter(item => item.title.toLowerCase().includes(normalized) || item.subtitle.toLowerCase().includes(normalized) || item.queryMatch?.some(keyword => keyword.includes(normalized))) : [], [data, normalized]);
  const resultHref = item => item.regionId === 'maharashtra' || item.regionId === 'odisha' ? `/regions/${item.regionId}` : item.url;
  return <div className="search-wrapper">
    <div className="search-input-box">
      <span className="search-icon" aria-hidden="true">⌕</span>
      <input className="search-input" value={query} onChange={event => setQuery(event.target.value)} placeholder="Search a place or heritage..." aria-label="Search places, monuments, arts, or traditions" />
      {query && <button className="search-clear-btn visible" onClick={() => setQuery('')} aria-label="Clear search input">✕</button>}
      <kbd className="search-kbd">⌘K</kbd>
    </div>
    {normalized && <div className="search-results-dropdown active" role="listbox">
      {results.length ? results.slice(0, 8).map(item => <div className="search-item" key={`${item.type}-${item.title}`}><Link to={resultHref(item)}><div className="search-item-info"><span className="search-item-title">{item.title}</span><span className="search-item-sub">{item.subtitle}</span></div><span className="search-item-type">{item.type}</span></Link></div>) : <div className="search-empty-state">No heritage matches found for <strong>&quot;{query}&quot;</strong></div>}
    </div>}
  </div>;
}