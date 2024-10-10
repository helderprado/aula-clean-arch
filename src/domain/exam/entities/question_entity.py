from typing import Optional
from datetime import datetime


class Question:

    id: Optional[int] = None
    date: datetime
    exam_id: int
    question: str
    answer: str

    def __init__(
        self,
        exam_id: int,
        date: datetime,
        question: str,
        answer: str,
        id: Optional[int] = None,
    ):
        self.id = id
        self.exam_id = exam_id
        self.date = date
        self.question = question
        self.answer = answer

    def verify_result(self, student_answer: str):
        if self.answer == student_answer:
            return True
        else:
            return False
