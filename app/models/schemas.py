from pydantic import BaseModel, Field, ConfigDict

class StudentBase(BaseModel):
    name: str = Field(...)
    roll_no: int = Field(..., gt=0)
    math: int = Field(..., ge=0, le=100)
    physics: int = Field(..., ge=0, le=100)
    chemistry: int = Field(..., ge=0, le=100)
    english: int = Field(..., ge=0, le=100)
    biology: int = Field(..., ge=0, le=100)


class StudentCreate(StudentBase):
    pass


class StudentOut(StudentBase):
    percentage: float
    grade: str
    rank: int

    model_config = ConfigDict(from_attributes=True)