from fastapi import APIRouter, HTTPException, Depends
import traceback
from infrastructure.api.database import get_session
from sqlalchemy.orm import Session

from infrastructure.exam.sqlalchemy.exam_repository import ExamRepository
from infrastructure.student.sqlalchemy.student_repository import StudentRepository
from usecases.student.find_student.find_student_dto import FindStudentInputDto
from usecases.student.find_student.find_student_usecase import FindStudentUseCase
from usecases.student.list_students.list_students_dto import ListStudentsInputDto
from usecases.student.list_students.list_students_usecase import ListStudentsUseCase
from usecases.student.register_student.register_student_dto import (
    RegisterStudentInputDto,
)
from usecases.student.register_student.register_student_usecase import (
    RegisterStudentUseCase,
)
from usecases.student.submit_exam.submit_exam_dto import SubmitExamInputDto
from usecases.student.submit_exam.submit_exam_usecase import SubmitExamUseCase
from usecases.student.verify_exam_result.verify_exam_result_dto import (
    VerifyExamResultInputDto,
)
from usecases.student.verify_exam_result.verify_exam_result_usecase import (
    VerifyExamResultUseCase,
)

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/")
def register_student(
    request: RegisterStudentInputDto,
    session: Session = Depends(get_session),
):
    try:
        student_repository = StudentRepository(session=session)
        usecase = RegisterStudentUseCase(student_repository=student_repository)
        output = usecase.execute(input=request)
        return output

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{student_id}")
def find_student(
    student_id: int,
    session: Session = Depends(get_session),
):
    try:
        student_repository = StudentRepository(session=session)
        usecase = FindStudentUseCase(student_repository=student_repository)
        Student = usecase.execute(input=FindStudentInputDto(id=student_id))
        return Student

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/")
def list_students(
    session: Session = Depends(get_session),
):
    try:
        student_repository = StudentRepository(session=session)
        usecase = ListStudentsUseCase(student_repository=student_repository)
        Students = usecase.execute(input=ListStudentsInputDto())
        return Students

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/submit_exam/")
def submit_exam(
    request: SubmitExamInputDto,
    session: Session = Depends(get_session),
):
    try:
        student_repository = StudentRepository(session=session)
        exam_repository = ExamRepository(session=session)
        usecase = SubmitExamUseCase(
            student_repository=student_repository, exam_repository=exam_repository
        )
        output = usecase.execute(input=request)
        return output

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/verify_exam_result/")
def verify_exam_result(
    request: VerifyExamResultInputDto,
    session: Session = Depends(get_session),
):
    try:
        student_repository = StudentRepository(session=session)
        exam_repository = ExamRepository(session=session)
        usecase = VerifyExamResultUseCase(
            student_repository=student_repository, exam_repository=exam_repository
        )
        output = usecase.execute(input=request)
        return output

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=404, detail=str(e))
