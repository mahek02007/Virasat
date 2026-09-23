"""
Virasat — Content Router
Endpoints:
  GET /api/v1/content
  GET /api/v1/content/{slug}
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/v1/content", tags=["Content"])


@router.get("", response_model=list[schemas.ContentItemSummary], summary="List content items")
def list_content(
    region_id: Optional[str] = Query(None, description="Filter by region (e.g. maharashtra, odisha)"),
    content_type: Optional[str] = Query(None, description="Filter by content_type (e.g. monument, art_craft, performing_art, festival_ritual, cuisine, fact)"),
    subtype: Optional[str] = Query(None, description="Filter by subtype"),
    is_gi_tagged: Optional[bool] = Query(None, description="Filter by GI tag"),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    query = db.query(models.ContentItem)
    if region_id:
        query = query.filter(models.ContentItem.region_id == region_id.lower())
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


@router.get("/{slug}", response_model=schemas.ContentItemDetail, summary="Get full content item details by slug")
def get_content_item(slug: str, db: Session = Depends(get_db)):
    item = db.query(models.ContentItem).filter(models.ContentItem.slug == slug).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content item '{slug}' not found",
        )

    place_summary = schemas.PlaceSummary.model_validate(item.place) if item.place else None
    media_list = [schemas.MediaOut.model_validate(m) for m in item.media_items]
    source_list = [schemas.SourceOut.model_validate(s) for s in item.sources]

    return schemas.ContentItemDetail(
        id=item.id,
        region_id=item.region_id,
        place_id=item.place_id,
        slug=item.slug,
        title=item.title,
        subtitle=item.subtitle,
        content_type=item.content_type,
        subtype=item.subtype,
        summary=item.summary,
        description=item.description,
        period=item.period,
        is_gi_tagged=item.is_gi_tagged,
        gi_year=item.gi_year,
        unesco_status=item.unesco_status,
        historical_era=item.historical_era,
        tags=item.tags or [],
        item_metadata=item.item_metadata or {},
        created_at=item.created_at,
        updated_at=item.updated_at,
        place=place_summary,
        media_items=media_list,
        sources=source_list,
    )
