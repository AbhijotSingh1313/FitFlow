from fastapi import FastAPI
from app.core.config import settings
from app.database.session import engine, Base
from app.models import user
from app.models.profile import Profile
from app.api.user_routes import router as user_router
from app.api.profile_routes import router as profile_router
from app.models.workout import Workout
from app.api.workout_routes import router as workout_router
from app.models.level import Level
from app.models.exercise import Exercise

# Create app FIRST
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(profile_router)
app.include_router(workout_router)
# Root endpoint
@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} backend is alive"}