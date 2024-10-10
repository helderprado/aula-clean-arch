from fastapi import FastAPI
from infrastructure.api.routers import (
    courses_routers,
    student_routers,
    teacher_routers,
    exam_routers,
)
from infrastructure.api.database import create_tables

app = FastAPI()

app.include_router(courses_routers.router)
app.include_router(student_routers.router)
app.include_router(teacher_routers.router)
app.include_router(exam_routers.router)

create_tables()
