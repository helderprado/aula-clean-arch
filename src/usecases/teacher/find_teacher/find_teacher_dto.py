from pydantic import BaseModel


class FindTeacherInputDto(BaseModel):
    id: str


class FindTeacherOutputDto(BaseModel):
    id: str
    name: str
