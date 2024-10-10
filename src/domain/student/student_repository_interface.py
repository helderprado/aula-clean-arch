from abc import ABC, abstractmethod
from src.domain.student.student_entity import Student
from typing import List


class StudentRepositoryInterface(ABC):

    @abstractmethod
    def register_student(self, Student: Student) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_student(self, id: int) -> Student:
        raise NotImplementedError

    @abstractmethod
    def list_students(self) -> List[Student]:
        raise NotImplementedError
