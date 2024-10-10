from pydantic import BaseModel


class RegisterExamInputDto(BaseModel):
    course_id: int
    teacher_id: int


class RegisterExamOutputDto(BaseModel):
    message: str
