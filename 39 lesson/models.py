from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Date, Boolean, DateTime
from sqlalchemy import func
from datetime import datetime, date


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

    def __repr__(self):
        return (f"Student(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name}, "
                f"birth_date={self.birth_date}, email={self.email}, is_budget={self.is_budget}, "
                f"created_at={self.created_at})\n")
