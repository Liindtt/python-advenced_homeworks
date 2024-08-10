from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Boolean

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title:  Mapped[str] = mapped_column(String(50))
    complete: Mapped[bool] = mapped_column(Boolean, default=False)

