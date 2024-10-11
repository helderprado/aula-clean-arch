from typing import Optional
from datetime import datetime


class Question:

    id: Optional[int] = None
    date: datetime
    exam_id: int
    question: str
    answer: str
    student_answer: Optional[str] = None
    student_answer_result: Optional[bool] = None

    def __init__(
        self,
        exam_id: int,
        date: datetime,
        question: str,
        answer: str,
        id: Optional[int] = None,
        student_answer: Optional[str] = None,
        student_answer_result: Optional[bool] = None,
    ):
        self.id = id
        self.exam_id = exam_id
        self.date = date
        self.question = question
        self.answer = answer
        self.student_answer = student_answer
        self.student_answer_result = student_answer_result

    def register_student_answer(self, student_answer: str) -> None:
        """Registra a resposta do aluno e avalia o resultado."""
        self.student_answer = student_answer

        if self.answer.lower() == student_answer.lower():
            self.student_answer_result = True
        else:
            self.student_answer_result = False

        return None
