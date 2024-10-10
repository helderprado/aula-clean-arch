from typing import List
from pydantic import BaseModel


class ListStudentsInputDto(BaseModel):
    pass


class StudentOutputDto(BaseModel):
    id: int
    name: str


class ListStudentsOutputDto(BaseModel):
    students: List[StudentOutputDto]
