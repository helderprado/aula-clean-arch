from abc import ABC, abstractmethod
from typing import List
from .entities.question_entity import Question
from .entities.exam_entity import Exam
from domain.exam.entities.question_entity import Question


class ExamRepositoryInterface(ABC):

    @abstractmethod
    def register_exam(self, exam: Exam) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_question_to_exam(self, question: Question) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_exam(self, exam_id: int) -> Exam:
        raise NotImplementedError

    @abstractmethod
    def submit_answered_questions(
        self, exam_id: int, student_id: int, answered_questions: List[Question]
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_submited_exam_result(
        self, exam_id: int, student_id: int
    ) -> List[Question]:
        raise NotImplementedError
