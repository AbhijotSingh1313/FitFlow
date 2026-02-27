
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.level import Level
from app.schemas.level_schema import LevelResponse
from app.core.auth import get_current_user

router = APIRouter(prefix="/levels", tags=["Levels"])


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all levels (Beginner, Intermediate, Advanced)
@router.get("", response_model=list[LevelResponse])
def get_levels(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    levels = db.query(Level).all()
    return levels


# Get single level by ID
@router.get("/{level_id}", response_model=LevelResponse)
def get_level(
    level_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    level = db.query(Level).filter(Level.id == level_id).first()

    if not level:
        raise HTTPException(status_code=404, detail="Level not found")

    return level