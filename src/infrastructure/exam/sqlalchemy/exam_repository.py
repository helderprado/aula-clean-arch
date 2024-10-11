from sqlalchemy.orm.session import Session
from typing import List
from domain.exam.entities.exam_entity import Exam
from domain.exam.entities.question_entity import Question
from infrastructure.exam.sqlalchemy.models.exam_model import ExamModel
from infrastructure.exam.sqlalchemy.models.question_model import QuestionModel
from infrastructure.exam.sqlalchemy.models.question_answered_model import (
    QuestionAnsweredModel,
)
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

        exam_model: ExamModel | None = self.session.query(ExamModel).get(exam_id)

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
            questions=[],
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

    def submit_answered_questions(
        self, exam_id: int, student_id: int, answered_questions: List[Question]
    ) -> None:

        for answered_question in answered_questions:
            answered_question_model = QuestionAnsweredModel(
                student_id=student_id,
                exam_id=exam_id,
                question_id=answered_question.id,
                student_answer=answered_question.student_answer,
                result=answered_question.student_answer_result,
            )

            self.session.add(answered_question_model)

        self.session.commit()

        return None

    def find_submited_exam_result(
        self, exam_id: int, student_id: int
    ) -> List[Question]:

        question_answered_models_joined = (
            self.session.query(QuestionAnsweredModel, QuestionModel)
            .join(
                QuestionModel,
                QuestionModel.id == QuestionAnsweredModel.question_id,
            )
            .filter(
                QuestionAnsweredModel.exam_id == exam_id,
                QuestionAnsweredModel.student_id == student_id,
            )
            .all()
        )

        questions_answereds = []

        for question_answered_model_joined in question_answered_models_joined:

            question_answered_model: QuestionAnsweredModel = (
                question_answered_model_joined[0]
            )
            question_model: QuestionModel = question_answered_model_joined[1]

            question = Question(
                id=question_model.id,
                exam_id=question_model.exam_id,
                date=question_model.date,
                question=question_model.question,
                answer=question_model.answer,
            )

            question.register_student_answer(
                student_answer=question_answered_model.student_answer
            )

            questions_answereds.append(question)

        return questions_answereds
