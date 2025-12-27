from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models import ReviewModel, ToolModel
from app.schemas import ToolResponse,ReviewCreate
from app.enums import CategoryType, PricingType,ReviewStatus

router = APIRouter(prefix="/tools", tags=["Tools"])

@router.post("/")
def submit_review(review: ReviewCreate, db: Session = Depends(get_db)):
    tool = db.query(ToolModel).filter(ToolModel.id == review.tool_id).first()

    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")

    new_review = ReviewModel(
        rating=review.rating,
        comment=review.comment,
        tool_id=review.tool_id
    )

    db.add(new_review)
    db.commit()
    

    return {
        "message": "Review submitted successfully",
        "status": new_review.status
    }