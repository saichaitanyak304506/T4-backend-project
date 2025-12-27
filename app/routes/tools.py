from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models import ReviewModel, ToolModel
from app.schemas import ToolResponse,ReviewCreate
from app.enums import CategoryType, PricingType,ReviewStatus

router = APIRouter(prefix="/tools", tags=["Tools"])


@router.get("/", response_model=list[ToolResponse])
def get_tools(
    category: Optional[CategoryType] = None,
    pricing_type: Optional[PricingType] = None,
    min_rating: Optional[float] = Query(None, ge=1, le=5),
    db: Session = Depends(get_db)
):
    query = db.query(ToolModel)

    if category:
        query = query.filter(ToolModel.category == category)

    if pricing_type:
        query = query.filter(ToolModel.pricing_type == pricing_type)

    if min_rating:
        query = query.filter(ToolModel.average_rating >= min_rating)

    return query.all()