from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, Table, Column
from typing import List


class Base(DeclarativeBase):
    ...


StudentCourse = Table(
    "StudentCourse",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))

    courses: Mapped[List["Course"]] = relationship(secondary=StudentCourse, back_populates="students")

    def __repr__(self):
        return f"Student({self.id=}, {self.first_name=}, {self.last_name=})"


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(120))
    hours: Mapped[int] = mapped_column(Integer)

    students: Mapped[List["Student"]] = relationship(secondary=StudentCourse, back_populates="courses")

    def __repr__(self):
        return f"Course({self.id=}, {self.course_name=}, {self.description}, {self.hours})"
