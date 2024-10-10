from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.exam.exam_repository import ExamRepositoryInterface
from domain.exam.entities.question_entity import Question
from datetime import datetime
from usecases.exam.add_question_to_exam.add_question_to_exam_dto import (
    AddQuestionToExamInputDto,
    AddQuestionToExamOutputDto,
)


class RegisterExamUseCase(UseCaseInterface):

    exam_repository: ExamRepositoryInterface

    def __init__(self, exam_repository: ExamRepositoryInterface):
        self.exam_repository = exam_repository

    def execute(self, input: AddQuestionToExamInputDto) -> AddQuestionToExamOutputDto:

        question = Question(
            date=datetime.now(),
            exam_id=input.exam_id,
            question=input.question,
            answer=input.answer,
        )

        self.exam_repository.add_question_to_exam(question=question)

        return AddQuestionToExamOutputDto(
            message="questão adicionada na prova com sucesso."
        )
