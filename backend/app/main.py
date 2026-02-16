from fastapi import FastAPI
from app.core.config import settings
from app.database.session import engine, Base
from app.models import user

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)


@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} backend is alive"}
Base.metadata.create_all(bind=engine)
