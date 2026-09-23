"""
Virasat — Cultural Facts Router (v1)
Endpoints:
  GET /api/v1/facts
  GET /api/v1/facts/random
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from typing import Optional

from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/v1/facts", tags=["Cultural Facts"])


def _content_to_fact_out(item: models.ContentItem, db: Session) -> schemas.FactOut:
    meta = item.item_metadata or {}
    region = db.query(models.Region).filter(models.Region.id == item.region_id).first()
    region_name = region.name if region else item.region_id

    return schemas.FactOut(
        id=item.id,
        slug=item.slug,
        region_id=item.region_id,
        region_name=region_name,
        tag=meta.get("tag", item.subtitle or "HERITAGE FACT"),
        region_label=meta.get("region_label", f"{region_name}, India"),
        quote=meta.get("quote", item.title),
        description=item.description,
        explore_link=meta.get("explore_link", f"/heritage/{item.slug}"),
    )


@router.get("", response_model=list[schemas.FactOut], summary="List cultural facts")
def list_facts(
    region_id: Optional[str] = Query(None, description="Filter by region (e.g. maharashtra, odisha)"),
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    query = db.query(models.ContentItem).filter(models.ContentItem.content_type == "fact")
    if region_id:
        query = query.filter(models.ContentItem.region_id == region_id.lower())
    items = query.limit(limit).all()
    return [_content_to_fact_out(item, db) for item in items]


@router.get("/random", response_model=schemas.FactOut, summary="Get a random cultural fact")
def get_random_fact(
    region_id: Optional[str] = Query(None, description="Optional region filter"),
    db: Session = Depends(get_db),
):
    query = db.query(models.ContentItem).filter(models.ContentItem.content_type == "fact")
    if region_id:
        query = query.filter(models.ContentItem.region_id == region_id.lower())
    fact_item = query.order_by(func.random()).first()

    if not fact_item:
        # Fallback if no facts are found
        return schemas.FactOut(
            id=0,
            slug="kailasa-monolith",
            region_id="maharashtra",
            region_name="Maharashtra",
            tag="MONOLITHIC MARVEL",
            region_label="Ellora, Maharashtra",
            quote="The Kailasa Temple at Ellora was carved top-down from a single basalt cliff.",
            description="Over 200,000 tonnes of rock were removed over 18 years to sculpt this freestanding temple.",
            explore_link="/heritage/ellora-kailasa-temple",
        )

    return _content_to_fact_out(fact_item, db)
