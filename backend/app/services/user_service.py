from sqlalchemy.orm import Session
from app.repositories.user_repo import create_user


def register_user(db: Session, email: str, password: str):
    # for now we store plain password (temporary) later we will hash it
    password_hash = password

    user = create_user(db, email=email, password_hash=password_hash)

    return user
