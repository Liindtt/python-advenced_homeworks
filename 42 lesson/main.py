from operations import re_create_tables, get_student_courses, add_data, get_course_students, get_student_profile_by_id
from random import randint

if __name__ == '__main__':
    re_create_tables()
    add_data()
    # get_student_courses(randint(1, 7))
    # get_course_students("Math")
    get_student_profile_by_id(1)
