/**
 * Virasat — API Client
 * Communicates with the FastAPI backend via VITE_API_BASE_URL.
 * All fetch calls go through the helpers below so the base URL is
 * defined in one place and never hard-coded elsewhere.
 */

const BASE_URL = (import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000').replace(/\/$/, '');

async function apiFetch(path, options = {}) {
  const url = `${BASE_URL}${path}`;
  const res = await fetch(url, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  });
  if (!res.ok) {
    const text = await res.text().catch(() => res.statusText);
    const err = new Error(`API ${res.status}: ${text}`);
    err.status = res.status;
    throw err;
  }
  return res.json();
}

// ── Regions ──────────────────────────────────────────────────────────────────

/**
 * GET /api/v1/regions
 * Returns an array of RegionSummary objects.
 * @param {{ zone?: string, status?: string }} params Optional query params.
 */
export async function fetchRegions(params = {}) {
  const qs = new URLSearchParams();
  if (params.zone) qs.set('zone', params.zone);
  if (params.status) qs.set('status', params.status);
  const query = qs.toString() ? `?${qs}` : '';
  return apiFetch(`/api/v1/regions${query}`);
}

/**
 * GET /api/v1/regions/{slug}
 * Returns a RegionDetail object (includes places + featured_content).
 * @param {string} slug Region slug or ID.
 */
export async function fetchRegion(slug) {
  return apiFetch(`/api/v1/regions/${encodeURIComponent(slug)}`);
}

/**
 * GET /api/v1/regions/{slug}/content
 * Returns an array of ContentItemSummary objects for the region.
 * @param {string} slug Region slug or ID.
 * @param {{ content_type?: string, subtype?: string, is_gi_tagged?: boolean, limit?: number, offset?: number }} params
 */
export async function fetchRegionContent(slug, params = {}) {
  const qs = new URLSearchParams();
  if (params.content_type) qs.set('content_type', params.content_type);
  if (params.subtype) qs.set('subtype', params.subtype);
  if (params.is_gi_tagged != null) qs.set('is_gi_tagged', String(params.is_gi_tagged));
  if (params.limit != null) qs.set('limit', String(params.limit));
  if (params.offset != null) qs.set('offset', String(params.offset));
  const query = qs.toString() ? `?${qs}` : '';
  return apiFetch(`/api/v1/regions/${encodeURIComponent(slug)}/content${query}`);
}
