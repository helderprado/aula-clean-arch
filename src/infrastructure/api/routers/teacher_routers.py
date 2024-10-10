from fastapi import APIRouter, HTTPException, Depends
import traceback
from infrastructure.api.database import get_session
from sqlalchemy.orm import Session
from usecases.teacher.find_teacher.find_teacher_dto import FindTeacherInputDto
from usecases.teacher.list_teachers.list_teachers_dto import ListTeachersInputDto
from usecases.teacher.register_teacher.register_teacher_dto import (
    RegisterTeacherInputDto,
)
from usecases.teacher.register_teacher.register_teacher_usecase import (
    RegisterTeacherUseCase,
)
from usecases.teacher.find_teacher.find_teacher_usecase import FindTeacherUseCase
from usecases.teacher.list_teachers.list_teachers_usecase import ListTeachersUseCase
from infrastructure.teacher.sqlalchemy.teacher_repository import TeacherRepository

router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.post("/")
def register_teacher(
    request: RegisterTeacherInputDto,
    session: Session = Depends(get_session),
):
    try:
        teacher_repository = TeacherRepository(session=session)
        usecase = RegisterTeacherUseCase(teacher_repository=teacher_repository)
        output = usecase.execute(input=request)
        return output

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{teacher_id}")
def find_teacher(
    teacher_id: int,
    session: Session = Depends(get_session),
):
    try:
        teacher_repository = TeacherRepository(session=session)
        usecase = FindTeacherUseCase(teacher_repository=teacher_repository)
        teacher = usecase.execute(input=FindTeacherInputDto(id=teacher_id))
        return teacher

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/")
def list_teachers(
    session: Session = Depends(get_session),
):
    try:
        teacher_repository = TeacherRepository(session=session)
        usecase = ListTeachersUseCase(teacher_repository=teacher_repository)
        teachers = usecase.execute(input=ListTeachersInputDto())
        return teachers

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))
