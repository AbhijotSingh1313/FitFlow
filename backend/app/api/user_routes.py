from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate
from app.services.user_service import register_user
from app.database.dependency import get_db
from app.schemas.user_schema import UserLogin
from app.services.user_service import login_user
from fastapi import HTTPException
from app.core.auth import create_access_token
from app.core.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

router = APIRouter()


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    created_user = register_user(db, email=user.email, password=user.password)

    if not created_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return {"id": created_user.id, "email": created_user.email}


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    existing_user = login_user(
        db,
        form_data.username,   # email goes here
        form_data.password
    )

    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token({"sub": existing_user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me")
def read_current_user(current_user: str = Depends(get_current_user)):
    return {"logged_in_as": current_user}
