from sqlalchemy.orm import Session
from app.repositories.user_repo import create_user
from app.core.security import hash_password
from app.repositories.user_repo import get_user_by_email
from app.core.security import verify_password
def register_user(db: Session, email: str, password: str):
    
    existing_user = get_user_by_email(db, email)
    if existing_user:
        return None
    password_hash = hash_password(password)
    user = create_user(db, email=email, password_hash=password_hash)
    return user
def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user
from app.repositories.user_repo import get_user_by_email
