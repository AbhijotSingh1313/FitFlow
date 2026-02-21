from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.schemas.profile_schema import ProfileCreate, ProfileResponse
from app.repositories.profile_repo import create_profile, get_my_profile
from app.core.auth import get_current_user
from app.repositories.profile_repo import update_my_profile
from app.repositories.profile_repo import delete_my_profile
from fastapi import HTTPException

router = APIRouter(prefix="/profile", tags=["Profile"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=ProfileResponse)
def create_my_profile(
    data: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return create_profile(db, current_user, data)


@router.get("/me", response_model=ProfileResponse)
def read_my_profile(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    profile = get_my_profile(db, current_user)

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile

@router.put("/me", response_model=ProfileResponse)
def update_profile(
    data: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return update_my_profile(db, current_user, data)

@router.delete("/me")
def delete_profile(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return delete_my_profile(db, current_user)