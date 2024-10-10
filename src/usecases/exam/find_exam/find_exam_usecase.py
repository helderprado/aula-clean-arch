from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.exam.exam_repository import ExamRepositoryInterface
from usecases.exam.find_exam.find_exam_dto import (
    FindExamInputDto,
    FindExamOutputDto,
    QuestionOutputDto,
)


class FindExamUseCase(UseCaseInterface):

    exam_repository: ExamRepositoryInterface

    def __init__(self, exam_repository: ExamRepositoryInterface):
        self.exam_repository = exam_repository

    def execute(self, input: FindExamInputDto) -> FindExamOutputDto:

        exam = self.exam_repository.find_exam(exam_id=input.id)

        output = FindExamOutputDto(
            id=exam.id,
            date=exam.date,
            course_id=exam.course_id,
            teacher_id=exam.teacher_id,
            questions=[
                QuestionOutputDto(
                    id=question.id,
                    date=question.date,
                    exam_id=question.exam_id,
                    question=question.question,
                    answer=question.answer,
                )
                for question in exam.questions
            ],
        )

        return output
