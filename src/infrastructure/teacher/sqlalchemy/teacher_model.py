from sqlalchemy import Column, String, Integer
from infrastructure.api.database import Base


class TeacherModel(Base):
    __tablename__ = "tb_teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
