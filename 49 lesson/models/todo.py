from database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    complete: Mapped[bool] = mapped_column(default=False)
