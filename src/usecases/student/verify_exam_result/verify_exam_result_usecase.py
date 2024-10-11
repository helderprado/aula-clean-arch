from typing import Any
from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.student.student_repository_interface import StudentRepositoryInterface
from domain.exam.exam_repository import ExamRepositoryInterface
from usecases.student.verify_exam_result.verify_exam_result_dto import (
    VerifyExamResultInputDto,
    VerifyExamResultOutputDto,
    QuestionAnsweredDto,
)


class VerifyExamResultUseCase(UseCaseInterface):

    student_repository: StudentRepositoryInterface
    exam_repository: ExamRepositoryInterface

    def __init__(
        self,
        student_repository: StudentRepositoryInterface,
        exam_repository: ExamRepositoryInterface,
    ):
        self.student_repository = student_repository
        self.exam_repository = exam_repository

    def execute(self, input: VerifyExamResultInputDto) -> VerifyExamResultOutputDto:

        answered_questions = self.exam_repository.find_submited_exam_result(
            exam_id=input.exam_id, student_id=input.student_id
        )

        output = []

        for answered_question in answered_questions:
            output.append(
                QuestionAnsweredDto(
                    id=answered_question.id,
                    exam_id=answered_question.exam_id,
                    date=answered_question.date,
                    question=answered_question.question,
                    answer=answered_question.answer,
                    student_answer=answered_question.student_answer,
                    student_answer_result=answered_question.student_answer_result,
                )
            )

        return VerifyExamResultOutputDto(questions=output)
