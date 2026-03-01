from sqlalchemy.orm import Session
from app.models.workout import Workout
from app.models.user import User
from fastapi import HTTPException
from app.models.workout_exercise import WorkoutExercise
from app.models.exercise import Exercise

def create_workout(db: Session, user_email: str, data):
    user = db.query(User).filter(User.email == user_email).first()

    workout = Workout(
        user_id=user.id,
        date=data.date
    )

    db.add(workout)
    db.commit()
    db.refresh(workout)

    # generate exercises from selected level
    generate_exercises_from_level(db, workout.id, data.level_id)

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
def generate_exercises_from_level(db, workout_id: int, level_id: int):
    exercises = db.query(Exercise).filter(
        Exercise.level_id == level_id
    ).all()

    for ex in exercises:
        workout_ex = WorkoutExercise(
            workout_id=workout_id,
            exercise_id=ex.id,
            sets=ex.default_sets,
            reps=ex.default_reps,
            is_custom=False
        )
        db.add(workout_ex)

    db.commit()