from typing import Optional, List
from domain.exam.entities.exam_entity import Exam
from domain.exam.entities.question_entity import Question
from pydantic import BaseModel


class AnsweredQuestionDto(BaseModel):
    question_id: int
    student_answer: str


class Student:

    id: Optional[int] = None
    name: str

    def __init__(self, name: str, id: Optional[int] = None):
        self.id = id
        self.name = name

    def submit_exam(
        self, exam: Exam, student_answers: List[AnsweredQuestionDto]  # Adiciona o self
    ) -> List[Question]:

        questions_answered: List[Question] = []

        for student_answer in student_answers:
            question = exam.find_question(question_id=student_answer.question_id)

            if question:
                question.register_student_answer(
                    student_answer=student_answer.student_answer
                )
                questions_answered.append(question)

        return questions_answered
