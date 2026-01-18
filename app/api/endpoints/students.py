# Student CRUD endpoints
from fastapi import APIRouter, Depends
from app.models.schemas import StudentCreate, StudentOut
from app.models.student import Student
from app.services.grade_calculator import grade_calculation, percentage_calculation, ranks
from app.core.dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/students')
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, roll_no=student.roll_no, math=student.math, physics=student.physics, chemistry=student.chemistry, english=student.english, biology=student.biology)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@router.get('/students/marks')
def get_all_students(db: Session = Depends(get_db)):
    all_students = db.query(Student).all()
    sorted_students = ranks(all_students)
    result = []
    for index, student in enumerate(sorted_students, 1):
       result.append( StudentOut(
            name=student.name,
            roll_no=student.roll_no,
            math=student.math,
            physics=student.physics,
            chemistry=student.chemistry,
            english=student.english,
            biology=student.biology,
            percentage=percentage_calculation(student),
            grade=grade_calculation(student),
            rank=index
        ))
        
    return result