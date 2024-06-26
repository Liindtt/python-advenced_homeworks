from models import Base, Student, Course
from database import Session as SessionMaker, engine
from random import randint, sample
from sqlalchemy import select
from faker import Faker


def re_create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def add_data():
    fake = Faker(locale="uk_UA")
    with SessionMaker() as session:
        courses = [
            Course(course_name="Database", description=fake.text(), hours=randint(30, 90)),
            Course(course_name="English", description=fake.text(), hours=randint(30, 90)),
            Course(course_name="Frontend", description=fake.text(), hours=randint(30, 90)),
            Course(course_name="Python", description=fake.text(), hours=randint(30, 90)),
            Course(course_name="Math", description=fake.text(), hours=randint(30, 90))
        ]

        students = [Student(first_name=fake.first_name(), last_name=fake.last_name(),
                            courses=sample(courses, k=randint(1, len(courses)))) for _ in range(7)]

        session.add_all(students)
        session.add_all(courses)
        session.commit()


def get_student_courses(user_id: int):
    with SessionMaker() as session:
        stmt = select(Student).where(Student.id == user_id)
        student = session.scalars(stmt).one_or_none()
        if student:
            print(f"ID {student.id} | {student.first_name} {student.last_name} studying in:\n"
                  f"{[(course.id, course.course_name) for course in student.courses]}")


def get_course_students(user_course_name: str):
    with SessionMaker() as session:
        stmt = select(Course).where(Course.course_name == user_course_name)
        course = session.scalars(stmt).one_or_none()
        if course:
            print(f"ID {course.id} | {course.course_name} include these students:\n"
                  f"{[(student.id, student.first_name, student.last_name) for student in course.students]}")
