from typing import Any
from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.course.course_repository_interface import CourseRepositoryInterface
from usecases.course.register_course.register_course_dto import (
    RegisterCourseInputDto,
    RegisterCourseOutputDto,
)
from domain.course.course_entity import Course


class RegisterCourseUseCase(UseCaseInterface):

    course_repository: CourseRepositoryInterface

    def __init__(self, course_repository: CourseRepositoryInterface):
        self.course_repository = course_repository

    def execute(self, input: RegisterCourseInputDto) -> None:

        course = Course(name=input.name)

        self.course_repository.register_course(course=course)

        return RegisterCourseOutputDto(message="curso registrado com sucesso.")
