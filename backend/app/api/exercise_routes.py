from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.database.session import SessionLocal
from app.models.exercise import Exercise
from app.schemas.exercise_schema import ExerciseResponse
from app.core.auth import get_current_user

router = APIRouter(prefix="/exercises", tags=["Exercises"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=List[ExerciseResponse])
def get_exercises(
    level_id: Optional[int] = Query(None),
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    query = db.query(Exercise)

    if level_id:
        query = query.filter(Exercise.level_id == level_id)

    if category:
        query = query.filter(Exercise.category == category)

    return query.all()