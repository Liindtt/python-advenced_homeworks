from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Date, Boolean, DateTime
from sqlalchemy import func, ForeignKey
from datetime import datetime, date
from typing import List


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    birth_date: Mapped[date] = mapped_column(Date)
    email: Mapped[str] = mapped_column(String(30))
    is_budget: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())

    grades: Mapped[List['Grade']] = relationship(back_populates="student")

    def __repr__(self):
        return (f"Student(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name}, "
                f"birth_date={self.birth_date}, email={self.email}, is_budget={self.is_budget}, "
                f"created_at={self.created_at})")


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject: Mapped[str] = mapped_column(String(30))
    score: Mapped[int] = mapped_column(Integer)
    student_id: Mapped[int] = mapped_column(ForeignKey(Student.id))

    student: Mapped['Student'] = relationship(back_populates="grades")

    def __repr__(self):
        return f"Grade(id={self.id}, subject={self.subject}, score={self.score}, student={self.student}\n"

