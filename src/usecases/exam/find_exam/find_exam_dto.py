from pydantic import BaseModel
from datetime import datetime
from typing import List


class FindExamInputDto(BaseModel):
    id: int


class QuestionOutputDto(BaseModel):
    id: int
    date: datetime
    exam_id: int
    question: str
    answer: str


class FindExamOutputDto(BaseModel):
    id: int
    date: datetime
    course_id: int
    teacher_id: int
    questions: List[QuestionOutputDto]
