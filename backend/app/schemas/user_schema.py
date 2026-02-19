from pydantic import BaseModel, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value):

        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not re.search(r"[A-Za-z]", value):
            raise ValueError("Password must contain a letter")

        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain a number")

        if not re.search(r"[!@#$%^&*()_\-+=<>?/{}~|]", value):
            raise ValueError("Password must contain a special symbol")

        return value
class UserLogin(BaseModel):
    email: EmailStr
    password: str
