"""
Virasat — Places Router
Endpoints:
  GET /api/v1/places
  GET /api/v1/places/{slug}
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/v1/places", tags=["Places"])


@router.get("", response_model=list[schemas.PlaceSummary], summary="List all heritage places")
def list_places(
    region_id: Optional[str] = Query(None, description="Filter by region (e.g. maharashtra, odisha)"),
    db: Session = Depends(get_db),
):
    query = db.query(models.Place)
    if region_id:
        query = query.filter(models.Place.region_id == region_id.lower())
    places = query.all()
    return [schemas.PlaceSummary.model_validate(p) for p in places]


@router.get("/{slug}", response_model=schemas.PlaceDetail, summary="Get place details by slug")
def get_place(slug: str, db: Session = Depends(get_db)):
    place = db.query(models.Place).filter(models.Place.slug == slug).first()
    if not place:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Place '{slug}' not found",
        )

    # Associated content items
    content_summaries = []
    for c in place.content_items:
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

    return schemas.PlaceDetail(
        id=place.id,
        region_id=place.region_id,
        name=place.name,
        slug=place.slug,
        latitude=place.latitude,
        longitude=place.longitude,
        address=place.address,
        description=place.description,
        created_at=place.created_at,
        content_items=content_summaries,
    )
