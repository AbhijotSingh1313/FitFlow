
from sqlalchemy import Column, Integer, String
from app.database.session import Base

class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)