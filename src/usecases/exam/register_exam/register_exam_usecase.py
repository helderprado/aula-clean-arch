from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.exam.exam_repository import ExamRepositoryInterface
from usecases.exam.register_exam.register_exam_dto import (
    RegisterExamInputDto,
    RegisterExamOutputDto,
)
from domain.exam.entities.exam_entity import Exam
from datetime import datetime


class RegisterExamUseCase(UseCaseInterface):

    exam_repository: ExamRepositoryInterface

    def __init__(self, exam_repository: ExamRepositoryInterface):
        self.exam_repository = exam_repository

    def execute(self, input: RegisterExamInputDto) -> RegisterExamOutputDto:

        exam = Exam(
            date=datetime.now(), course_id=input.course_id, teacher_id=input.teacher_id
        )

        self.exam_repository.register_exam(exam=exam)

        return RegisterExamOutputDto(message="exame cadastrado com sucesso.")
