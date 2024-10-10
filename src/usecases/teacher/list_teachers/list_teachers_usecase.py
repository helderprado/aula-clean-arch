from typing import Any
from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.teacher.teacher_repository_interface import TeacherRepositoryInterface
from usecases.teacher.list_teachers.list_teachers_dto import (
    ListTeachersInputDto,
    ListTeachersOutputDto,
    TeacherOutputDto,
)


class ListTeachersUseCase(UseCaseInterface):

    teacher_repository: TeacherRepositoryInterface

    def __init__(self, teacher_repository: TeacherRepositoryInterface):
        self.teacher_repository = teacher_repository

    def execute(self, input: ListTeachersInputDto) -> ListTeachersOutputDto:

        teachers = self.teacher_repository.list_teachers()

        output = []

        for teacher in teachers:
            output.append(TeacherOutputDto(id=teacher.id, name=teacher.name))

        return ListTeachersOutputDto(teachers=output)
