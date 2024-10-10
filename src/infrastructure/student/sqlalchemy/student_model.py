from sqlalchemy import Column, String, Integer
from infrastructure.api.database import Base


class StudentModel(Base):
    __tablename__ = "tb_students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
