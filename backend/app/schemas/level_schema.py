from pydantic import BaseModel

class LevelResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True