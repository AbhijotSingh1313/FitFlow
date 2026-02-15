from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)


@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} backend is alive"}
