from pydantic import BaseModel


class AddQuestionToExamInputDto(BaseModel):
    exam_id: int
    question: str
    answer: str


class AddQuestionToExamOutputDto(BaseModel):
    message: str
