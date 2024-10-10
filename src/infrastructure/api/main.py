from fastapi import FastAPI
from infrastructure.api.routers import courses_routers
from infrastructure.api.routers import student_routers
from infrastructure.api.routers import teacher_routers

app = FastAPI()

app.include_router(courses_routers)
app.include_router(student_routers)
app.include_router(teacher_routers)
