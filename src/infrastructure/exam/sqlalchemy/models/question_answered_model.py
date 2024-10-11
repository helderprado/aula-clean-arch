from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from infrastructure.api.database import Base


class QuestionAnsweredModel(Base):
    __tablename__ = "tb_questions_answereds"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("tb_exams.id", ondelete="CASCADE"))
    exam_id = Column(Integer, ForeignKey("tb_exams.id", ondelete="CASCADE"))
    question_id = Column(Integer, ForeignKey("tb_questions.id", ondelete="CASCADE"))
    student_answer = Column(String)
    result = Column(Boolean)
