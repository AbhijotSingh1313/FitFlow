from fastapi import FastAPI
from app.core.config import settings
from app.database.session import engine, Base
from app.models import user
from app.api.user_routes import router as user_router
from app.models.profile import Profile
app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)


@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} backend is alive"}
Base.metadata.create_all(bind=engine)
app.include_router(user_router, prefix="/users", tags=["Users"])
