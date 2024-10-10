from pydantic import BaseModel


class FindCourseInputDto(BaseModel):
    id: str


class FindCourseOutputDto(BaseModel):
    id: str
    name: str
