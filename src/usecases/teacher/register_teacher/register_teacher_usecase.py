from typing import Any
from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.teacher.teacher_repository_interface import TeacherRepositoryInterface
from usecases.teacher.register_teacher.register_teacher_dto import (
    RegisterTeacherInputDto,
    RegisterTeacherOutputDto,
)
from domain.teacher.teacher_entity import Teacher


class RegisterTeacherUseCase(UseCaseInterface):

    teacher_repository: TeacherRepositoryInterface

    def __init__(self, teacher_repository: TeacherRepositoryInterface):
        self.teacher_repository = teacher_repository

    def execute(self, input: RegisterTeacherInputDto) -> None:

        teacher = Teacher(name=input.name)

        self.teacher_repository.register_teacher(teacher=teacher)

        return RegisterTeacherOutputDto(message="professor registrado com sucesso.")
