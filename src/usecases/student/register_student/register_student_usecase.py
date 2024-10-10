from typing import Any
from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.student.student_repository_interface import StudentRepositoryInterface
from usecases.student.register_student.register_student_dto import (
    RegisterStudentInputDto,
    RegisterStudentOutputDto,
)
from domain.student.student_entity import Student


class RegisterStudentUseCase(UseCaseInterface):

    student_repository: StudentRepositoryInterface

    def __init__(self, student_repository: StudentRepositoryInterface):
        self.student_repository = student_repository

    def execute(self, input: RegisterStudentInputDto) -> None:

        student = Student(name=input.name)

        self.student_repository.register_student(student=student)

        return RegisterStudentOutputDto(message="estudante registrado com sucesso.")
