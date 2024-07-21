from pymongo import MongoClient, ASCENDING, DESCENDING
from bson.objectid import ObjectId
from models import Student
from typing import List, Optional, Dict, Any


class ManagerDB:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['students']

    def insert_student(self, students: List[Student]):
        try:
            result = self.collection.insert_many([student.dict() for student in students])
            print(f'Students inserted with id\'s: {result.inserted_ids}')
        except Exception as e:
            print(f'Error inserting students: {e}')

    def get_students(self, sort_key: Optional[str] = None, sort_order: Optional[int] = ASCENDING,
                     projection: Optional[Dict[str, int]] = None) -> List[Dict[str, Any]]:
        try:
            cursor = self.collection.find({}, projection)
            if sort_key:
                cursor = cursor.sort(sort_key, sort_order)
            return list(cursor)
        except Exception as e:
            print(f'Error getting students: {e}')
            return []

    def update_student(self, student_id: str, update_data: Dict[str, Any]):
        try:
            result = self.collection.update_one({"_id": ObjectId(student_id)}, {"$set": update_data})
            print(f'Student updated, matched: {result.matched_count}, modified: {result.modified_count}')
        except Exception as e:
            print(f'Error updating student: {e}')

    def delete_student(self, student_id: str):
        try:
            result = self.collection.delete_one({"_id": ObjectId(student_id)})
            print(f'Student deleted, deleted count: {result.deleted_count}')
        except Exception as e:
            print(f'Error deleting student: {e}')

    def filter_students(self, filter_criteria: Dict[str, Any],
                        projection: Optional[Dict[str, int]] = None) -> List[Dict[str, Any]]:
        try:
            return list(self.collection.find(filter_criteria, projection))
        except Exception as e:
            print(f'Error filtering students: {e}')
            return []
