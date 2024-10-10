from sqlalchemy.orm.session import Session
from typing import List
from domain.exam.entities.exam_entity import Exam
from domain.exam.entities.question_entity import Question
from infrastructure.exam.sqlalchemy.models.exam_model import ExamModel
from infrastructure.exam.sqlalchemy.models.question_model import QuestionModel
from domain.exam.exam_repository import ExamRepositoryInterface


class ExamRepository(ExamRepositoryInterface):

    def __init__(self, session: Session):
        self.session: Session = session

    def register_exam(self, exam: Exam) -> None:

        exam_model = ExamModel(
            date=exam.date,
            course_id=exam.course_id,
            teacher_id=exam.teacher_id,
        )

        self.session.add(exam_model)
        self.session.commit()

        return None

    def add_question_to_exam(self, question: Question) -> None:

        question_model = QuestionModel(
            date=question.date,
            exam_id=question.exam_id,
            question=question.question,
            answer=question.answer,
        )

        self.session.add(question_model)
        self.session.commit()

        return None

    def find_exam(self, exam_id: int) -> Exam:

        exam_model = self.session.query(ExamModel).filter_by(id=exam_id).first()

        if exam_model is None:
            raise ValueError(f"não foi encontrado uma prova com o id {exam_id}")

        questions_from_exam_models = (
            self.session.query(QuestionModel)
            .filter(QuestionModel.exam_id == exam_id)
            .all()
        )

        exam = Exam(
            id=exam_model.id,
            date=exam_model.date,
            course_id=exam_model.course_id,
            teacher_id=exam_model.teacher_id,
        )

        for question_from_exam_model in questions_from_exam_models:
            question = Question(
                id=question_from_exam_model.id,
                date=question_from_exam_model.date,
                exam_id=question_from_exam_model.exam_id,
                question=question_from_exam_model.question,
                answer=question_from_exam_model.answer,
            )
            exam.add_question(question=question)

        return exam
