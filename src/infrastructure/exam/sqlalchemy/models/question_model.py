from sqlalchemy import Column, ForeignKey, Integer, DateTime, String
from infrastructure.api.database import Base


class QuestionModel(Base):
    __tablename__ = "tb_questions"

    id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey("tb_exams.id", ondelete="CASCADE"))
    date = Column(DateTime)
    question = Column(String)
    answer = Column(String)
