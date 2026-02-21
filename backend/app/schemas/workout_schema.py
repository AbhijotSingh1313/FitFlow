from pydantic import BaseModel

class WorkoutCreate(BaseModel):
    exercise: str
    sets: int
    reps: int
    weight: int
    date: str

class WorkoutResponse(WorkoutCreate):
    id: int

    class Config:
        from_attributes = True