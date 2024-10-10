from typing import List
from pydantic import BaseModel
from domain.course.course_entity import Course


class ListCoursesInputDto(BaseModel):
    pass


class CourseOutputDto(BaseModel):
    id: int
    name: str


class ListCoursesOutputDto(BaseModel):
    courses: List[CourseOutputDto]
