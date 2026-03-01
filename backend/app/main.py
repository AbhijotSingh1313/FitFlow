from fastapi import FastAPI
from app.core.config import settings
from app.database.session import engine, Base, SessionLocal

# Models
from app.models import user
from app.models.profile import Profile
from app.models.workout import Workout
from app.models.level import Level
from app.models.exercise import Exercise
import app.models.workout_exercise
# Routers
from app.api.user_routes import router as user_router
from app.api.profile_routes import router as profile_router
from app.api.workout_routes import router as workout_router
from app.api import level_routes
from app.api import exercise_routes


# Create FastAPI app


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include Routers

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(profile_router)
app.include_router(workout_router)
app.include_router(level_routes.router)
app.include_router(exercise_routes.router)

# Root endpoint

@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} backend is alive"}


# Seed Levels

def seed_levels():
    db = SessionLocal()

    existing = db.query(Level).first()
    if not existing:
        levels = [
            Level(name="Beginner"),
            Level(name="Intermediate"),
            Level(name="Advanced")
        ]
        db.add_all(levels)
        db.commit()

    db.close()


# Seed Exercises

def seed_exercises():
    db = SessionLocal()

    if db.query(Exercise).first():
        db.close()
        return

    # Get levels
    beginner = db.query(Level).filter(Level.name == "Beginner").first()
    intermediate = db.query(Level).filter(Level.name == "Intermediate").first()
    advanced = db.query(Level).filter(Level.name == "Advanced").first()

    exercises = [

        #Beginner
        Exercise(
            name="Push Ups",
            muscle_group="Chest",
            category="Chest",
            level_id=beginner.id,
            default_sets=3,
            default_reps=12,
            is_predefined=True,
            is_custom=False
        ),
        Exercise(
            name="Incline Push Ups",
            muscle_group="Chest",
            category="Chest",
            level_id=beginner.id,
            default_sets=3,
            default_reps=10,
            is_predefined=True,
            is_custom=False
        ),
        Exercise(
            name="Bodyweight Squats",
            muscle_group="Legs",
            category="Legs",
            level_id=beginner.id,
            default_sets=3,
            default_reps=15,
            is_predefined=True,
            is_custom=False
        ),
        Exercise(
            name="Lunges",
            muscle_group="Legs",
            category="Legs",
            level_id=beginner.id,
            default_sets=3,
            default_reps=12,
            is_predefined=True,
            is_custom=False
        ),

        #Intermediate
        Exercise(
            name="Bench Press",
            muscle_group="Chest",
            category="Chest",
            level_id=intermediate.id,
            default_sets=4,
            default_reps=10,
            is_predefined=True,
            is_custom=False
        ),
        Exercise(
            name="Incline Dumbbell Press",
            muscle_group="Chest",
            category="Chest",
            level_id=intermediate.id,
            default_sets=4,
            default_reps=10,
            is_predefined=True,
            is_custom=False
        ),
        Exercise(
            name="Pull Ups",
            muscle_group="Back",
            category="Back",
            level_id=intermediate.id,
            default_sets=4,
            default_reps=8,
            is_predefined=True,
            is_custom=False
        ),

        #Advanced
        Exercise(
            name="Incline Barbell Press",
            muscle_group="Chest",
            category="Chest",
            level_id=advanced.id,
            default_sets=5,
            default_reps=8,
            is_predefined=True,
            is_custom=False
        ),
        Exercise(
            name="Weighted Pull Ups",
            muscle_group="Back",
            category="Back",
            level_id=advanced.id,
            default_sets=5,
            default_reps=6,
            is_predefined=True,
            is_custom=False
        ),
    ]

    db.add_all(exercises)
    db.commit()
    db.close()


# Run Seed Functions

seed_levels()
seed_exercises()