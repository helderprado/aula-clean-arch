from typing import List
from pydantic import BaseModel


class ListTeachersInputDto(BaseModel):
    pass


class TeacherOutputDto(BaseModel):
    id: int
    name: str


class ListTeachersOutputDto(BaseModel):
    teachers: List[TeacherOutputDto]
