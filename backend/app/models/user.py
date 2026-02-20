from sqlalchemy import Column, Integer, String, Boolean
from app.database.session import Base
from sqlalchemy.orm import relationship

profile = relationship("Profile", back_populates="user", uselist=False)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
