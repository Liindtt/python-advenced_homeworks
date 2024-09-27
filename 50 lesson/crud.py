from sqlalchemy.orm import Session
from models.todo import Todo
from schemas.todo import SchemaUpdateTodo, SchemaBaseTodo


def get_task(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Todo).offset(skip).limit(limit).all()


def create_task(db: Session, todo: SchemaBaseTodo):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_task(db: Session, todo: SchemaUpdateTodo, todo_id: int):
    db_todo = get_task(db, todo_id)
    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_task(db: Session, todo_id: int):
    db_todo = get_task(db, todo_id)
    db.delete(db_todo)
    db.commit()
    return db
