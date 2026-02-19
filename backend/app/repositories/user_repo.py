from sqlalchemy.orm import Session
from app.models import User


def create_user(db: Session, email: str, password_hash: str):
    user = User(
        email=email,
        password_hash=password_hash
    )

    db.add(user)      # to put into session
    db.commit()       # to save permanently
    db.refresh(user)  # to get saved data 

    return user
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
