from datetime import datetime
from typing import Optional, List
from .question_entity import Question


class Exam:

    id: int
    date: datetime
    course_id: int
    teacher_id: int
    questions: List[Question] = []

    def __init__(
        self,
        date: datetime,
        course_id: int,
        teacher_id: int,
        questions: List[Question] = [],
        id: Optional[int] = None,
    ):
        self.id = id
        self.date = date
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.questions = questions

    def add_question(self, question: Question) -> None:
        self.questions.append(question)
        return None

    def find_question(self, question_id: int) -> Optional[Question]:
        for question in self.questions:
            if question.id == question_id:
                return question
        return None
