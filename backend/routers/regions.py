"""
Virasat — Regions Router
Endpoints:
  GET /api/v1/regions
  GET /api/v1/regions/{slug}
  GET /api/v1/regions/{slug}/content
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional

from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/v1/regions", tags=["Regions"])


@router.get("", response_model=list[schemas.RegionSummary], summary="List all regions")
def list_regions(
    zone: Optional[str] = Query(None, description="Filter by zone (e.g. west, east, north, south)"),
    status_filter: Optional[str] = Query(None, alias="status", description="Filter by status (e.g. available, coming_soon)"),
    db: Session = Depends(get_db),
):
    query = db.query(models.Region)
    if zone:
        query = query.filter(models.Region.zone == zone.lower())
    if status_filter:
        query = query.filter(models.Region.status == status_filter.lower())

    regions = query.all()
    results = []
    for r in regions:
        # Calculate content count
        count = db.query(func.count(models.ContentItem.id)).filter(models.ContentItem.region_id == r.id).scalar() or 0
        summary_data = schemas.RegionSummary(
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
        )
        results.append(summary_data)
    return results


@router.get("/{slug}", response_model=schemas.RegionDetail, summary="Get region by slug or ID")
def get_region(slug: str, db: Session = Depends(get_db)):
    region = db.query(models.Region).filter(
        (models.Region.slug == slug) | (models.Region.id == slug)
    ).first()
    if not region:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Region '{slug}' not found",
        )

    places = db.query(models.Place).filter(models.Place.region_id == region.id).all()
    
    # Exclude raw "fact" type from general featured content list or include all
    content_items = db.query(models.ContentItem).filter(
        models.ContentItem.region_id == region.id,
        models.ContentItem.content_type != "fact"
    ).all()

    place_summaries = [schemas.PlaceSummary.model_validate(p) for p in places]
    content_summaries = []
    for c in content_items:
        primary_media = c.media_items[0].url if c.media_items else None
        item_summary = schemas.ContentItemSummary(
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
        )
        content_summaries.append(item_summary)

    total_content_count = db.query(func.count(models.ContentItem.id)).filter(models.ContentItem.region_id == region.id).scalar() or 0

    return schemas.RegionDetail(
        id=region.id,
        name=region.name,
        slug=region.slug,
        devanagari=region.devanagari,
        tagline=region.tagline,
        status=region.status,
        is_pilot=region.is_pilot,
        zone=region.zone,
        coord_x=region.coord_x,
        coord_y=region.coord_y,
        summary=region.summary,
        color_accent=region.color_accent,
        badge=region.badge,
        categories=region.categories or [],
        highlights=region.highlights or [],
        content_count=total_content_count,
        created_at=region.created_at,
        places=place_summaries,
        featured_content=content_summaries,
    )


@router.get("/{slug}/content", response_model=list[schemas.ContentItemSummary], summary="Get all content items for a region")
def get_region_content(
    slug: str,
    content_type: Optional[str] = Query(None, description="Filter by content_type (e.g. monument, art_craft, performing_art, festival_ritual, cuisine, fact)"),
    subtype: Optional[str] = Query(None, description="Filter by subtype"),
    is_gi_tagged: Optional[bool] = Query(None, description="Filter by GI tag status"),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    region = db.query(models.Region).filter(
        (models.Region.slug == slug) | (models.Region.id == slug)
    ).first()
    if not region:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Region '{slug}' not found",
        )

    query = db.query(models.ContentItem).filter(models.ContentItem.region_id == region.id)
    if content_type:
        query = query.filter(models.ContentItem.content_type == content_type.lower())
    if subtype:
        query = query.filter(models.ContentItem.subtype == subtype.lower())
    if is_gi_tagged is not None:
        query = query.filter(models.ContentItem.is_gi_tagged == is_gi_tagged)

    items = query.offset(offset).limit(limit).all()

    results = []
    for c in items:
        primary_media = c.media_items[0].url if c.media_items else None
        item_summary = schemas.ContentItemSummary(
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
        )
        results.append(item_summary)
    return results
