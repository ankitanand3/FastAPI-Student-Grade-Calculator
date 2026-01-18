# FastAPI app entry point & 
from app.storage.student_store import engine, SessionLocal, Base
from app.models.student import Student
from fastapi import FastAPI, HTTPException
from app.api.endpoints.students import router

app = FastAPI()
app.include_router(router)
Base.metadata.create_all(bind=engine)

