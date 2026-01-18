# Reusable dependency injection
from app.storage.student_store import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


