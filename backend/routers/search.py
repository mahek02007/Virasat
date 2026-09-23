"""
Virasat — Search Router (v1)
Endpoints:
  GET /api/v1/search?q=...
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/v1/search", tags=["Search"])


@router.get("", response_model=schemas.SearchResult, summary="Unified search across regions, content items, and places")
def unified_search(
    q: str = Query(..., min_length=1, description="Search query string"),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    pattern = f"%{q.strip().lower()}%"

    # Search regions
    region_records = db.query(models.Region).filter(
        or_(
            func.lower(models.Region.name).like(pattern),
            func.lower(models.Region.summary).like(pattern),
            func.lower(models.Region.tagline).like(pattern),
            func.lower(models.Region.devanagari).like(pattern),
        )
    ).limit(5).all()

    matched_regions = []
    for r in region_records:
        count = db.query(func.count(models.ContentItem.id)).filter(models.ContentItem.region_id == r.id).scalar() or 0
        matched_regions.append(schemas.RegionSummary(
            id=r.id,
            name=r.name,
            slug=r.slug,
            devanagari=r.devanagari,
            tagline=r.tagline,
            status=r.status,
            is_pilot=r.is_pilot,
            zone=r.zone,
            coord_x=r.coord_x,
            coord_y=r.coord_y,
            summary=r.summary,
            color_accent=r.color_accent,
            badge=r.badge,
            categories=r.categories or [],
            highlights=r.highlights or [],
            content_count=count,
        ))

    # Search content items (excluding raw facts from main search unless matched)
    content_records = db.query(models.ContentItem).filter(
        or_(
            func.lower(models.ContentItem.title).like(pattern),
            func.lower(models.ContentItem.subtitle).like(pattern),
            func.lower(models.ContentItem.description).like(pattern),
            func.lower(models.ContentItem.summary).like(pattern),
            func.lower(models.ContentItem.content_type).like(pattern),
            func.lower(models.ContentItem.subtype).like(pattern),
        )
    ).limit(limit).all()

    matched_content = []
    for c in content_records:
        primary_media = c.media_items[0].url if c.media_items else None
        matched_content.append(schemas.ContentItemSummary(
            id=c.id,
            region_id=c.region_id,
            place_id=c.place_id,
            slug=c.slug,
            title=c.title,
            subtitle=c.subtitle,
            content_type=c.content_type,
            subtype=c.subtype,
            summary=c.summary,
            period=c.period,
            is_gi_tagged=c.is_gi_tagged,
            gi_year=c.gi_year,
            unesco_status=c.unesco_status,
            historical_era=c.historical_era,
            tags=c.tags or [],
            primary_image=primary_media,
        ))

    # Search places
    place_records = db.query(models.Place).filter(
        or_(
            func.lower(models.Place.name).like(pattern),
            func.lower(models.Place.address).like(pattern),
            func.lower(models.Place.description).like(pattern),
        )
    ).limit(limit).all()

    matched_places = [schemas.PlaceSummary.model_validate(p) for p in place_records]

    total = len(matched_regions) + len(matched_content) + len(matched_places)

    return schemas.SearchResult(
        query=q,
        total_results=total,
        regions=matched_regions,
        content_items=matched_content,
        places=matched_places,
    )
