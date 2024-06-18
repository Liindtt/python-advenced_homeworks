from database import Session as SessionMaker, engine
from models import Base, Student
from sqlalchemy import select, func
from datetime import date


def re_create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def add_student(first_name: str, last_name: str, birth_date: date, email: str, is_budget: bool):
    with SessionMaker() as session:
        new_student = Student(first_name=first_name, last_name=last_name, birth_date=birth_date, email=email,
                              is_budget=is_budget)
        session.add(new_student)
        session.commit()


def get_all_students():
    with SessionMaker() as session:
        stmt = select(Student).order_by(Student.last_name)
        result = session.execute(stmt).all()
        print(result)


def update_student_by_id(user_id: int, email: str, is_budget: bool):
    with SessionMaker() as session:
        user = session.query(Student).get(user_id)
        user.email = email
        user.is_budget = is_budget
        session.commit()


def delete_student_by_id(user_id: int):
    with SessionMaker() as session:
        user = session.query(Student).get(user_id)
        session.delete(user)
        session.commit()


def get_budget_students():
    with SessionMaker() as session:
        stmt = select(Student).where(Student.birth_date >= date(2000, 1, 1),
                                     Student.is_budget == True)
        result = session.execute(stmt).all()
        print(result)


def get_count_of_students():
    with SessionMaker() as session:
        stmt = select(func.count(Student.id))
        result = session.execute(stmt).all()
        print(f'Загальна кількість студентів: {result}')
