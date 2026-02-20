from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.models.user import User


def create_profile(db: Session, user_email: str, data):
    user = db.query(User).filter(User.email == user_email).first()

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