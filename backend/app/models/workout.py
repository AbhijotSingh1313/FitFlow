from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class Workout(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))

    sets = Column(Integer)
    reps = Column(Integer)
    time = Column(Integer)
    weight = Column(Integer)
    date = Column(String)

    exercise = relationship("Exercise")