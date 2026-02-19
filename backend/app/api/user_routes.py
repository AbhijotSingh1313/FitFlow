from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate
from app.services.user_service import register_user
from app.database.dependency import get_db
from app.schemas.user_schema import UserLogin
from app.services.user_service import login_user
from fastapi import HTTPException
from app.core.auth import create_access_token

router = APIRouter()


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    created_user = register_user(db, email=user.email, password=user.password)

    if not created_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return {"id": created_user.id, "email": created_user.email}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = login_user(db, user.email, user.password)

    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": existing_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
