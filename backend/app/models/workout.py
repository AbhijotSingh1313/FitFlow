from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.session import Base


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    date = Column(String)

    workout_exercises = relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete"
    )