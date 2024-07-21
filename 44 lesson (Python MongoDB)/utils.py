from faker import Faker
from models import Student
from typing import List

faker = Faker()


def generate_fake_students(num: int) -> List[Student]:
    students = []
    for _ in range(num):
        student = Student(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            year_of_admission=faker.random_int(min=2000, max=2024)
        )
        students.append(student)
    return students


def parse_sort_order(order: str) -> int:
    if order.lower() == 'asc':
        return 1
    elif order.lower() == 'desc':
        return -1
    else:
        raise ValueError("Sort order must be 'asc' or 'desc'")
