from domain.student.student_entity import Student
from domain.student.student_repository_interface import StudentRepositoryInterface
from infrastructure.student.sqlalchemy.student_model import StudentModel
from sqlalchemy.orm.session import Session
from typing import List


class StudentRepository(StudentRepositoryInterface):

    def __init__(self, session: Session):
        self.session: Session = session

    def register_student(self, student: Student) -> None:

        student_model = StudentModel(name=student.name)

        self.session.add(student_model)
        self.session.commit()

        return None

    def find_student(self, id: int) -> Student:

        student_model: StudentModel = self.session.query(StudentModel).get(id)

        return Student(id=student_model.id, name=student_model.name)

    def list_students(self) -> List[Student]:

        student_models: List[StudentModel] = self.session.query(StudentModel).all()

        teachers = []

        for student_model in student_models:
            teachers.append(Student(id=student_model.id, name=student_model.name))

        return teachers
