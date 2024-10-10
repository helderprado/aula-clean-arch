from typing import Any
from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.course.course_repository_interface import CourseRepositoryInterface
from usecases.course.find_course.find_course_dto import (
    FindCourseInputDto,
    FindCourseOutputDto,
)
from domain.course.course_entity import Course


class FindCourseUseCase(UseCaseInterface):

    course_repository: CourseRepositoryInterface

    def __init__(self, course_repository: CourseRepositoryInterface):
        self.course_repository = course_repository

    def execute(self, input: FindCourseInputDto) -> FindCourseOutputDto:

        course = self.course_repository.find_course(id=input.id)

        return FindCourseOutputDto(id=course.id, name=course.name)
