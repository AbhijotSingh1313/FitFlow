from pydantic import BaseModel


class WorkoutCreate(BaseModel):
    date: str
    level_id: int


class WorkoutResponse(BaseModel):
    id: int
    date: str

    class Config:
        from_attributes = True