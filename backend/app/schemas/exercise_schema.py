from pydantic import BaseModel

class ExerciseResponse(BaseModel):
    id: int
    name: str
    category: str
    level_id: int
    is_predefined: bool

    class Config:
        from_attributes = True