from sqlalchemy import (create_engine, MetaData, ForeignKey,
                        Table, Column, Integer, String, Float,
                        select, delete, insert, update, func)

engine = create_engine("sqlite:///uni.db", echo=True)
metadata = MetaData()

# creating students table
table_students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(20), nullable=False),
    Column("last_name", String(30), nullable=False),
    Column("bday", String(10), nullable=False)
)

# creating grades table
table_grades = Table(
    "grades",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("subject", String(30), nullable=False),
    Column("score", Float, nullable=False),
    Column("student_id", Integer, ForeignKey("students.id"), nullable=False)
)

metadata.drop_all(engine)
metadata.create_all(engine)


def insert_data():
    with engine.connect() as conn:
        conn.execute(insert(table_students), [
            {"name": "Yaroslav", "last_name": "Nykolaichyk", "bday": "10-07-2003"},
            {"name": "Yuriy", "last_name": "Onyskiv", "bday": "09-05-2001"},
            {"name": "Yana", "last_name": "Fil", "bday": "02-07-2003"},
        ])
        conn.execute(insert(table_grades), [
            {"subject": "Math", "score": 90.6, "student_id": 1},
            {"subject": "Chemistry", "score": 64.2, "student_id": 1},
            {"subject": "Math", "score": 96.0, "student_id": 2},
            {"subject": "Chemistry", "score": 81.2, "student_id": 2},
            {"subject": "Math", "score": 71.9, "student_id": 3},
            {"subject": "Chemistry", "score": 51.2, "student_id": 3},
        ])
        conn.commit()


def get_sorted_student_s_scores_by_last_name():
    with (engine.connect() as conn):
        stmt = select(table_students.c.id, table_students.c.name, table_students.c.last_name,
                      table_grades.c.subject, table_grades.c.score
                      ).select_from(table_students.join(table_grades)
                                    ).order_by(table_students.c.last_name)
        result = conn.execute(stmt)
        for row in result:
            print(row)


def get_student_scores_by_last_name(user_last_name: str):
    with engine.connect() as conn:
        stmt = select(table_students.c.id, table_students.c.name, table_students.c.last_name,
                      table_grades.c.subject, table_grades.c.score
                      ).select_from(table_students.join(table_grades)
                                    ).where(table_students.c.last_name == user_last_name)
        result = conn.execute(stmt)
        for row in result:
            print(row)


def get_avg_subjects_scores():
    with engine.connect() as conn:
        stmt = select(table_grades.c.subject, func.avg(table_grades.c.score).label('average_score')
                      ).group_by(table_grades.c.subject)
        result = conn.execute(stmt)
        for row in result:
            print(f"Subject: {row.subject}, Average Score: {row.average_score:.2f}")


def get_data():
    with engine.connect() as connection:
        result = connection.execute(select(table_students).order_by(table_students.c.name))
        for row in result:
            print(row)


def update_data(new_name: str):
    with engine.connect() as conn:
        conn.execute(update(table_students).where(table_students.c.id == 2).values(name=new_name))
        conn.commit()


def delete_column(user_id: int):
    with engine.connect() as conn:
        conn.execute(delete(table_students).where(table_students.c.id == user_id))
        conn.commit()


insert_data()
get_sorted_student_s_scores_by_last_name()
get_student_scores_by_last_name("Onyskiv")
get_avg_subjects_scores()
