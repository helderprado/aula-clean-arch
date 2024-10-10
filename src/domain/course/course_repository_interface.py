from abc import ABC, abstractmethod
from src.domain.course.course_entity import Course
from typing import List


class CourseRepositoryInterface(ABC):

    @abstractmethod
    def register_course(self, course: Course) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_course(self, id: int) -> Course:
        raise NotImplementedError

    @abstractmethod
    def list_courses(self) -> List[Course]:
        raise NotImplementedError
