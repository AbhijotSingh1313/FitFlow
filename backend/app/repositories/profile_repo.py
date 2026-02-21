from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.models.user import User
from fastapi import HTTPException

def create_profile(db: Session, user_email: str, data):
    user = db.query(User).filter(User.email == user_email).first()

    existing_profile = db.query(Profile).filter(Profile.user_id == user.id).first()
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile already exists")

    profile = Profile(
        name=data.name,
        age=data.age,
        height=data.height,
        weight=data.weight,
        goal=data.goal,
        user_id=user.id
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def get_my_profile(db: Session, user_email: str):
    user = db.query(User).filter(User.email == user_email).first()
    return db.query(Profile).filter(Profile.user_id == user.id).first()

def update_my_profile(db: Session, user_email: str, data):
    user = db.query(User).filter(User.email == user_email).first()

    profile = db.query(Profile).filter(Profile.user_id == user.id).first()

    profile.name = data.name
    profile.age = data.age
    profile.height = data.height
    profile.weight = data.weight
    profile.goal = data.goal

    db.commit()
    db.refresh(profile)
    return profile

def delete_my_profile(db: Session, user_email: str):
    user = db.query(User).filter(User.email == user_email).first()

    profile = db.query(Profile).filter(Profile.user_id == user.id).first()

    if profile:
        db.delete(profile)
        db.commit()

    return {"message": "Profile deleted"}