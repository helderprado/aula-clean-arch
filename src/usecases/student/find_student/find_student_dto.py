from pydantic import BaseModel


class FindStudentInputDto(BaseModel):
    id: str


class FindStudentOutputDto(BaseModel):
    id: str
    name: str
