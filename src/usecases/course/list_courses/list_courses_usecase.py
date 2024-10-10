from typing import Any
from domain.__seedwork.usecase_interface import UseCaseInterface
from domain.course.course_repository_interface import CourseRepositoryInterface
from usecases.course.list_courses.list_courses_dto import (
    ListCoursesInputDto,
    ListCoursesOutputDto,
    CourseOutputDto,
)


class ListCoursesUseCase(UseCaseInterface):

    course_repository: CourseRepositoryInterface

    def __init__(self, course_repository: CourseRepositoryInterface):
        self.course_repository = course_repository

    def execute(self, input: ListCoursesInputDto) -> ListCoursesOutputDto:

        courses = self.course_repository.list_courses()

        output = []

        for course in courses:
            output.append(CourseOutputDto(id=course.id, name=course.name))

        return ListCoursesOutputDto(courses=courses)
