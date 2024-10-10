from fastapi import APIRouter, HTTPException, Depends
import traceback
from infrastructure.api.database import get_session
from sqlalchemy.orm import Session

from infrastructure.exam.sqlalchemy.exam_repository import ExamRepository
from usecases.exam.add_question_to_exam.add_question_to_exam_dto import (
    AddQuestionToExamInputDto,
)
from usecases.exam.add_question_to_exam.add_question_to_exam_usecase import (
    AddQuestionToExamUseCase,
)
from usecases.exam.find_exam.find_exam_dto import FindExamInputDto
from usecases.exam.find_exam.find_exam_usecase import FindExamUseCase
from usecases.exam.register_exam.register_exam_dto import RegisterExamInputDto
from usecases.exam.register_exam.register_exam_usecase import RegisterExamUseCase


router = APIRouter(prefix="/exams", tags=["Exams"])


@router.post("/")
def register_exam(
    request: RegisterExamInputDto,
    session: Session = Depends(get_session),
):
    try:
        exam_repository = ExamRepository(session=session)
        usecase = RegisterExamUseCase(exam_repository=exam_repository)
        output = usecase.execute(input=request)
        return output

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/add_question_to_exam")
def add_question_to_exam(
    request: AddQuestionToExamInputDto,
    session: Session = Depends(get_session),
):
    try:
        exam_repository = ExamRepository(session=session)
        usecase = AddQuestionToExamUseCase(exam_repository=exam_repository)
        teacher = usecase.execute(input=request)
        return teacher

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{exam_id}")
def find_exam(
    exam_id: int,
    session: Session = Depends(get_session),
):
    try:
        exam_repository = ExamRepository(session=session)
        usecase = FindExamUseCase(exam_repository=exam_repository)
        output = usecase.execute(input=FindExamInputDto(id=exam_id))
        return output

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))
