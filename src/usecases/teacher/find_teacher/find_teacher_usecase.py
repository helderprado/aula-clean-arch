from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.teacher.teacher_repository_interface import TeacherRepositoryInterface
from usecases.teacher.find_teacher.find_teacher_dto import (
    FindTeacherInputDto,
    FindTeacherOutputDto,
)


class FindTeacherUseCase(UseCaseInterface):

    teacher_repository: TeacherRepositoryInterface

    def __init__(self, teacher_repository: TeacherRepositoryInterface):
        self.teacher_repository = teacher_repository

    def execute(self, input: FindTeacherInputDto) -> FindTeacherOutputDto:

        teacher = self.teacher_repository.find_teacher(id=input.id)

        return FindTeacherOutputDto(id=teacher.id, name=teacher.name)
