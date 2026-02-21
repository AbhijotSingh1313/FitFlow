from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.schemas.workout_schema import WorkoutCreate, WorkoutResponse
from app.repositories.workout_repo import (
    create_workout,
    get_my_workouts,
    delete_workout
)
from app.core.auth import get_current_user  # your JWT dependency

router = APIRouter(prefix="/workouts", tags=["Workouts"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=WorkoutResponse)
def add_workout(
    data: WorkoutCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return create_workout(db, current_user, data)


@router.get("/me", response_model=list[WorkoutResponse])
def read_my_workouts(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return get_my_workouts(db, current_user)


@router.delete("/{workout_id}")
def remove_workout(
    workout_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return delete_workout(db, current_user, workout_id)