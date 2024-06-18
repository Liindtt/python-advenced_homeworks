from database import Session as SessionMaker, engine
from models import Base, Student, Grade
from sqlalchemy import select, func, delete, update
from datetime import date


def re_create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


# Table Student
# Операція Create для таблиць Student та Grade
def add_student(first_name: str, last_name: str, birth_date: date, email: str, is_budget: bool,
                subject: str, score: int, subject1: str, score1: int):
    with SessionMaker() as session:
        new_student = Student(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            email=email,
            is_budget=is_budget,
            grades=[
                Grade(subject=subject, score=score),
                Grade(subject=subject1, score=score1)
            ]
        )
        session.add(new_student)
        session.commit()


def get_all_students():
    with SessionMaker() as session:
        stmt = select(Student).order_by(Student.last_name)
        result = session.scalars(stmt)
        for row in result:
            print(row)


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
        result = session.execute(stmt).scalar()
        print(f'Загальна кількість студентів: {result}')


# Table Grade
# Операція Read
def get_grade_info():
    with SessionMaker() as session:
        stmt = select(Grade.id, Grade.subject, Grade.score, Grade.student_id, Grade.student).join(Grade)
        result = session.execute(stmt)
        for row in result:
            print(row)


# Операція Update
def update_grade_by_id(user_id: int, new_subject: str, new_score: int):
    with SessionMaker() as session:
        stmt = (
            update(Grade).
            where(Grade.id == user_id).
            values(subject=new_subject, score=new_score)
        )
        session.execute(stmt)
        session.commit()
        pass


# Операція Delete
def delete_grade_by_id(user_id: int):
    with SessionMaker() as session:
        stmt = delete(Grade).where(Grade.id == user_id)
        session.execute(stmt)
        session.commit()


# •	Отримання списку студентів та їх оцінок з певного заданого предмета, відсортувавши по дані по прізвищу.
def get_all_info(subject: str):
    with SessionMaker() as session:
        stmt = select(Student.id, Student.first_name, Student.last_name, Grade.subject, Grade.score
                      ).join(Student.grades).where(Grade.subject == subject).order_by(Student.last_name)
        result = session.execute(stmt)
        for row in result:
            print(row)


# •	Отримання всіх оцінок певного студента за його прізвищем.
def get_student_scores_by_last_name(user_last_name: str):
    with SessionMaker() as session:
        stmt = select(Student.last_name, Grade.subject, Grade.score
                      ).join(Student.grades).where(Student.last_name == user_last_name)
        result = session.execute(stmt)
        for row in result:
            print(row)


# •	Отримання середньої оцінки по кожному предмету.
def get_avg_subjects_scores():
    with SessionMaker() as session:
        stmt = select(Grade.subject, func.avg(Grade.score).label('average_score')
                      ).group_by(Grade.subject)
        result = session.execute(stmt)
        for row in result:
            print(f"Subject: {row.subject}, Average Score: {row.average_score:.2f}")
