from pydantic import BaseModel
from typing import List


class AnsweredQuestionDto(BaseModel):
    question_id: int
    student_answer: str


class SubmitExamInputDto(BaseModel):
    student_id: int
    exam_id: int
    answered_questions: List[AnsweredQuestionDto]


class SubmitExamOutputDto(BaseModel):
    message: str
