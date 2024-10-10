from sqlalchemy import Column, String, Integer, DateTime
from infrastructure.api.database import Base


class ExamModel(Base):
    __tablename__ = "tb_exams"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    course_id = Column(Integer)
    teacher_id = Column(Integer)
