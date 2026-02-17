from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate
from app.services.user_service import register_user
from app.database.dependency import get_db

router = APIRouter()


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    created_user = register_user(db, email=user.email, password=user.password)
    return {"id": created_user.id, "email": created_user.email}
