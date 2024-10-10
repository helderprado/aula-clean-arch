from abc import ABC, abstractmethod
from src.domain.teacher.teacher_entity import Teacher
from typing import List


class TeacherRepositoryInterface(ABC):

    @abstractmethod
    def register_teacher(self, teacher: Teacher) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_teacher(self, id: int) -> Teacher:
        raise NotImplementedError

    @abstractmethod
    def list_teachers(self) -> List[Teacher]:
        raise NotImplementedError
