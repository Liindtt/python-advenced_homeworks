from operations import (re_create_table, add_student, get_all_info, get_grade_info, delete_grade_by_id,
                        get_student_scores_by_last_name, get_avg_subjects_scores, update_grade_by_id)
from datetime import date
from faker import Faker
from random import randint, choice


if __name__ == '__main__':
    fake = Faker(locale='uk_UA')
    re_create_table()
    add_student("Ярослав", "Николайчук", date(2003, 7, 10),
                "lindtt.10.2003@gmail.com", True, "English", 85, "Chemistry", 79)
    for _ in range(6):
        add_student(fake.first_name(), fake.last_name(), fake.date_of_birth(minimum_age=18, maximum_age=30),
                    fake.email(), fake.boolean(), choice(["Math", "English", "Chemistry"]), randint(35, 100),
                    choice(["Math", "English", "Chemistry"]), randint(35, 100))
    # delete_grade_by_id(12)
    update_grade_by_id(1, "Physics", 99)
    get_grade_info()
    get_all_info(choice(["Math", "English", "Chemistry"]))
    get_student_scores_by_last_name("Николайчук")
    get_avg_subjects_scores()
