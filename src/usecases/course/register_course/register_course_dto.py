from pydantic import BaseModel


class RegisterCourseInputDto(BaseModel):
    name: str


class RegisterCourseOutputDto(BaseModel):
    message: str
