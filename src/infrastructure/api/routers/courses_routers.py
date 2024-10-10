from fastapi import APIRouter, HTTPException, Depends
import traceback
from infrastructure.api.database import get_session
from sqlalchemy.orm import Session
from usecases.course.register_course.register_course_dto import RegisterCourseInputDto
from usecases.course.register_course.register_course_usecase import (
    RegisterCourseUseCase,
)
from infrastructure.course.sqlalchemy.course_repository import CourseRepository

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("/")
def register_course(
    request: RegisterCourseInputDto,
    session: Session = Depends(get_session),
):
    try:
        course_repository = CourseRepository(session=session)
        usecase = RegisterCourseUseCase(course_repository=course_repository)
        output = usecase.execute(input=request)
        return output

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))
