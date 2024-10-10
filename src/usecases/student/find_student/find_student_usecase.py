from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.student.student_repository_interface import StudentRepositoryInterface
from usecases.student.find_student.find_student_dto import (
    FindStudentInputDto,
    FindStudentOutputDto,
)


class FindStudentUseCase(UseCaseInterface):

    Student_repository: StudentRepositoryInterface

    def __init__(self, Student_repository: StudentRepositoryInterface):
        self.Student_repository = Student_repository

    def execute(self, input: FindStudentInputDto) -> FindStudentOutputDto:

        Student = self.Student_repository.find_student(id=input.id)

        return FindStudentOutputDto(id=Student.id, name=Student.name)
