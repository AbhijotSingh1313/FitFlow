from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from app.database.session import Base


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True, index=True)

    workout_id = Column(Integer, ForeignKey("workouts.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=True)

    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Integer)

    is_custom = Column(Boolean, default=False)
    custom_name = Column(String, nullable=True)

    workout = relationship("Workout", back_populates="workout_exercises")
    exercise = relationship("Exercise")