from pydantic import BaseModel
from typing import List, Optional


class WorkoutCreate(BaseModel):
    date: str
    level_id: int


class WorkoutExerciseResponse(BaseModel):
    id: int
    exercise_id: Optional[int]
    sets: Optional[int]
    reps: Optional[int]
    weight: Optional[int]
    is_custom: bool
    custom_name: Optional[str]

    class Config:
        from_attributes = True


class WorkoutResponse(BaseModel):
    id: int
    date: str
    workout_exercises: List[WorkoutExerciseResponse]

    class Config:
        from_attributes = True