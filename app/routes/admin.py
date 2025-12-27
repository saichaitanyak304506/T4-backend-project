from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.enums import CategoryType, PricingType,ReviewStatus
from app.database import get_db
from app.models import ToolModel, ReviewModel
from app.schemas import ReviewCreate

router = APIRouter(prefix="/reviews", tags=["Reviews"])



@router.put("/reviews/{review_id}/approve")
def approve_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    review.status = ReviewStatus.APPROVED
    db.commit()

    approved_reviews = db.query(ReviewModel).filter(
        ReviewModel.tool_id == review.tool_id,
        ReviewModel.status == ReviewStatus.APPROVED
    ).all()

    avg_rating = sum(r.rating for r in approved_reviews) / len(approved_reviews)

    tool = db.query(ToolModel).filter(ToolModel.id == review.tool_id).first()
    tool.average_rating = avg_rating
    db.commit()

    return {"message": "Review approved & rating updated"}

