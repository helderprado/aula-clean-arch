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
        self, date: datetime, course_id: int, teacher_id: int, id: Optional[int] = None
    ):
        self.id = id
        self.date = date
        self.course_id = course_id
        self.teacher_id = teacher_id

    def add_question(self, question: Question):
        self.questions.append(question)
