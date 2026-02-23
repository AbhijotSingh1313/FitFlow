

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database.session import Base

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    muscle_group = Column(String, nullable=False)

    level_id = Column(Integer, ForeignKey("levels.id"), nullable=True)

    default_sets = Column(Integer)
    default_reps = Column(Integer)

    # IMPORTANT
    is_custom = Column(Boolean, default=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    level = relationship("Level")