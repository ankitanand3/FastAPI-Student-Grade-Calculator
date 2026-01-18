# Pydantic schemas for validation

from sqlalchemy import Column, Integer, String
from app.storage.student_store import Base

class Student(Base):
    __tablename__ = 'students'
    name = Column(String, index= True, nullable=False)
    roll_no = Column(Integer, primary_key=True, nullable=False)
    math = Column(Integer, nullable=False)
    physics = Column(Integer, nullable=False)
    chemistry = Column(Integer, nullable=False)
    english = Column(Integer, nullable=False)
    biology = Column(Integer, nullable=False)
