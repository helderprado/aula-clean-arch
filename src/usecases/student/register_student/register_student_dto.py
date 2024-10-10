from pydantic import BaseModel


class RegisterStudentInputDto(BaseModel):
    name: str


class RegisterStudentOutputDto(BaseModel):
    message: str
