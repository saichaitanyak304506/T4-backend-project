from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from app.enums import PricingType, CategoryType

class ToolModel(Base):
    __tablename__ = "tools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    use_case = Column(String, nullable=False)

    category = Column(Enum(CategoryType), nullable=False)
    pricing_type = Column(Enum(PricingType), nullable=False)

    average_rating = Column(Float, default=0.0)

    reviews = relationship(
        "ReviewModel",
        back_populates="tool",
        cascade="all, delete"
    )


from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from app.enums import ReviewStatus

class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)

    status = Column(
        Enum(ReviewStatus),
        default=ReviewStatus.PENDING,
        nullable=False
    )

    tool_id = Column(Integer, ForeignKey("tools.id"))

    tool = relationship("ToolModel", back_populates="reviews")
