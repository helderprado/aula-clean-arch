from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.student.student_repository_interface import StudentRepositoryInterface
from usecases.student.list_students.list_students_dto import (
    ListStudentsInputDto,
    ListStudentsOutputDto,
    StudentOutputDto,
)


class ListStudentsUseCase(UseCaseInterface):

    student_repository: StudentRepositoryInterface

    def __init__(self, student_repository: StudentRepositoryInterface):
        self.student_repository = student_repository

    def execute(self, input: ListStudentsInputDto) -> ListStudentsOutputDto:

        students = self.student_repository.list_students()

        output = []

        for student in students:
            output.append(StudentOutputDto(id=student.id, name=student.name))

        return ListStudentsOutputDto(students=students)
