from pydantic import BaseModel, EmailStr
from typing import Optional


class Student(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    year_of_admission: int


class UpdateStudent(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    year_of_admission: Optional[int] = None
