from sqlalchemy.orm import Session
from app.models.workout import Workout
from app.models.user import User
from fastapi import HTTPException

def create_workout(db: Session, user_email: str, data):
    user = db.query(User).filter(User.email == user_email).first()

    workout = Workout(
        exercise_id=data.exercise_id,
        sets=data.sets,
        reps=data.reps,
        weight=data.weight,
        date=data.date,
        user_id=user.id
    )

    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout


def get_my_workouts(db: Session, user_email: str):
    user = db.query(User).filter(User.email == user_email).first()
    return db.query(Workout).filter(Workout.user_id == user.id).all()


def delete_workout(db: Session, user_email: str, workout_id: int):
    user = db.query(User).filter(User.email == user_email).first()

    workout = db.query(Workout).filter(
        Workout.id == workout_id,
        Workout.user_id == user.id
    ).first()

    if workout:
        db.delete(workout)
        db.commit()

    return {"message": "Workout deleted"}


def update_workout(db: Session, user_email: str, workout_id: int, data):
    user = db.query(User).filter(User.email == user_email).first()

    workout = db.query(Workout).filter(
        Workout.id == workout_id,
        Workout.user_id == user.id
    ).first()

    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")

    workout.exercise = data.exercise
    workout.sets = data.sets
    workout.reps = data.reps
    workout.weight = data.weight
    workout.date = data.date

    db.commit()
    db.refresh(workout)
    return workout