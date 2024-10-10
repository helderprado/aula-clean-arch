from domain.teacher.teacher_entity import Teacher
from domain.teacher.teacher_repository_interface import TeacherRepositoryInterface
from infrastructure.teacher.sqlalchemy.teacher_model import TeacherModel
from sqlalchemy.orm.session import Session
from typing import List


class TeacherRepository(TeacherRepositoryInterface):

    def __init__(self, session: Session):
        self.session: Session = session

    def register_teacher(self, teacher: Teacher) -> None:

        teacher_model = TeacherModel(name=teacher.name)

        self.session.add(teacher_model)
        self.session.commit()

        return None

    def find_teacher(self, id: int) -> Teacher:

        teacher_model: TeacherModel = self.session.query(TeacherModel).get(id)

        return Teacher(id=teacher_model.id, name=teacher_model.name)

    def list_teachers(self) -> List[Teacher]:

        teacher_models: List[TeacherModel] = self.session.query(TeacherModel).all()

        teachers = []

        for teacher_model in teacher_models:
            teachers.append(Teacher(id=teacher_model.id, name=teacher_model.name))

        return teachers
