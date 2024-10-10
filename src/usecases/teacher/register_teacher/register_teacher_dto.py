from pydantic import BaseModel


class RegisterTeacherInputDto(BaseModel):
    name: str


class RegisterTeacherOutputDto(BaseModel):
    message: str
