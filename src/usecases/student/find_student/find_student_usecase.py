from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.student.student_repository_interface import StudentRepositoryInterface
from usecases.student.find_student.find_student_dto import (
    FindStudentInputDto,
    FindStudentOutputDto,
)


class FindStudentUseCase(UseCaseInterface):

    student_repository: StudentRepositoryInterface

    def __init__(self, student_repository: StudentRepositoryInterface):
        self.student_repository = student_repository

    def execute(self, input: FindStudentInputDto) -> FindStudentOutputDto:

        student = self.student_repository.find_student(id=input.id)

        return FindStudentOutputDto(id=student.id, name=student.name)
