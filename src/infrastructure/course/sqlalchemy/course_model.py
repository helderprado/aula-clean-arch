from sqlalchemy import Column, String, Integer
from infrastructure.api.database import Base


class CourseModel(Base):
    __tablename__ = "tb_courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
