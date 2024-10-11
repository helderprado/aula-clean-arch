from pydantic import BaseModel
from typing import List
from datetime import datetime


class VerifyExamResultInputDto(BaseModel):
    student_id: int
    exam_id: int


class QuestionAnsweredDto(BaseModel):
    id: int
    exam_id: int
    date: datetime
    question: str
    answer: str
    student_answer: str
    student_answer_result: bool


class VerifyExamResultOutputDto(BaseModel):
    questions: List[QuestionAnsweredDto]
