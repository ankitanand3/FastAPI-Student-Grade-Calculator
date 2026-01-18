 # Business logic for calculations
from app.models.schemas import StudentBase

def percentage_calculation(student: StudentBase) -> float:
    total = student.math + student.physics + student.chemistry + student.english + student.biology
    percentage = (total/500)*100
    return percentage


def grade_calculation(student: StudentBase) -> str:
    grade = None
    percentage = percentage_calculation(student)
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def ranks(students: list):
    sorted_students = sorted(students, key=lambda s: percentage_calculation(s), reverse=True)
    return sorted_students

