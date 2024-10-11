from typing import Any
from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.student.student_repository_interface import StudentRepositoryInterface
from domain.exam.exam_repository import ExamRepositoryInterface
from usecases.student.submit_exam.submit_exam_dto import (
    SubmitExamInputDto,
    SubmitExamOutputDto,
)


class SubmitExamUseCase(UseCaseInterface):

    student_repository: StudentRepositoryInterface
    exam_repository: ExamRepositoryInterface

    def __init__(
        self,
        student_repository: StudentRepositoryInterface,
        exam_repository: ExamRepositoryInterface,
    ):
        self.student_repository = student_repository
        self.exam_repository = exam_repository

    def execute(self, input: SubmitExamInputDto) -> None:

        exam = self.exam_repository.find_exam(exam_id=input.exam_id)
        student = self.student_repository.find_student(id=input.student_id)

        questions_exam_results = student.submit_exam(
            exam=exam, student_answers=input.answered_questions
        )

        self.exam_repository.submit_answered_questions(
            exam_id=exam.id,
            student_id=student.id,
            answered_questions=questions_exam_results,
        )

        return SubmitExamOutputDto(message="prova registrada com sucesso.")
