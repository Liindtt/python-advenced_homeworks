from database_manager import ManagerDB
from models import UpdateStudent
from utils import parse_sort_order, generate_fake_students


if __name__ == "__main__":
    db_manager = ManagerDB(uri="mongodb://localhost:27017/", db_name="university")

    # Insert fake students
    fake_students = generate_fake_students(2)
    db_manager.insert_student(fake_students)

    # Get all students, sorted by year_of_admission in ascending order, projecting only last_name and email
    students = db_manager.get_students(sort_key="year_of_admission", sort_order=parse_sort_order("asc"),
                                       projection={"last_name": 1, "year_of_admission": 1})
    print(f"Students: {students}")

    # Update a student (example)
    # Note: Replace the id below with an actual id from your database
    update_data = UpdateStudent(email="john.newemail@example.com")
    db_manager.update_student(student_id="669d173ae33a9145ac2f05d8", update_data=update_data.dict(exclude_unset=True))

    # Delete a student (example)
    # Note: Replace the id below with an actual id from your database
    db_manager.delete_student(student_id="669d173ae33a9145ac2f05d9")

    # Filter students by year_of_admission
    filtered_students = db_manager.filter_students(filter_criteria={"year_of_admission": 2021})
    print(f"Filtered Students: {filtered_students}")
