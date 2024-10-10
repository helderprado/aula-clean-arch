from domain.course.course_entity import Course
from domain.course.course_repository_interface import CourseRepositoryInterface
from infrastructure.course.sqlalchemy.course_model import CourseModel
from sqlalchemy.orm.session import Session
from typing import List


class CourseRepository(CourseRepositoryInterface):

    def __init__(self, session: Session):
        self.session: Session = session

    def register_course(self, course: Course) -> None:

        course_model = CourseModel(name=course.name)

        self.session.add(course_model)
        self.session.commit()

        return None

    def find_course(self, id: int) -> Course:

        course_model: CourseModel = self.session.query(CourseModel).get(id)

        return Course(id=course_model.id, name=course_model.name)

    def list_courses(self) -> List[Course]:

        course_models: List[CourseModel] = self.session.query(CourseModel).all()

        courses = []

        for course_model in course_models:

            courses.append(Course(id=course_model.id, name=course_model.name))

        return courses
