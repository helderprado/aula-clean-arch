from typing import Optional


class QuestionAnswered:

    id: Optional[int]
    question_id: int
    student_answer: str
    result: int

    def __init__(
        self,
        question_id: int,
        result: int,
        student_answer: str,
        id: Optional[int],
    ):
        self.id = id
        self.question_id = question_id
        self.student_answer = student_answer
        self.result = result
