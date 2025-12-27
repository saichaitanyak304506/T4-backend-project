from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from app.enums import PricingType, CategoryType, ReviewStatus


class ToolCreate(BaseModel):
    name: str
    use_case: str
    category: CategoryType
    pricing_type: PricingType


class ToolResponse(BaseModel):

    id: int
    name: str
    use_case: str
    category: CategoryType
    pricing_type: PricingType
    average_rating: float

    model_config = ConfigDict(from_attributes=True)


class ReviewCreate(BaseModel):
    tool_id: int
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None


class ReviewResponse(BaseModel):

    id: int
    rating: int
    comment: Optional[str]
    status: ReviewStatus

    model_config = ConfigDict(from_attributes=True)
