from pydantic import BaseModel

class ProfileCreate(BaseModel):
    name: str
    age: int
    height: int
    weight: int
    goal: str


class ProfileResponse(ProfileCreate):
    id: int

    class Config:
        from_attributes = True