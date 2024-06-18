from operations import (re_create_table, add_student, get_all_students, update_student_by_id, delete_student_by_id,
                        get_budget_students, get_count_of_students)
from datetime import date
from faker import Faker
from random import randint


if __name__ == '__main__':
    fake = Faker(locale='uk_UA')
    re_create_table()
    add_student("Yaroslav", "Nykolaichuk", date(2003, 7, 10),
                "lindtt.10.2003@gmail.com", True)
    for _ in range(6):
        add_student(fake.first_name(), fake.last_name(), fake.date_of_birth(minimum_age=18, maximum_age=30),
                    fake.email(), fake.boolean())
    get_all_students()
    update_student_by_id(randint(0, 6), fake.email(), fake.boolean())
    delete_student_by_id(2)
    get_budget_students()
    get_count_of_students()
