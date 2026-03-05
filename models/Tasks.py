from sqlalchemy import Boolean, Column, Integer, String
from core.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(100), nullable=True)
    is_completed = Column(Boolean, default=False)
