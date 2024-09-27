from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from schemas.todo import SchemaBaseTodo, SchemaTodo, SchemaUpdateTodo
import crud

router = APIRouter(prefix="/todos", tags=["FastAPI with router"])


@router.post("/", response_model=SchemaTodo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: SchemaBaseTodo, db: Session = Depends(get_db)):
    return crud.create_task(db, todo)


@router.get("/", response_model=list[SchemaTodo], status_code=status.HTTP_200_OK)
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todos = crud.get_tasks(db, skip=skip, limit=limit)
    return todos


@router.get("/{todo_id}", response_model=SchemaTodo, status_code=status.HTTP_200_OK)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_task(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return db_todo


@router.put("/{todo_id}", response_model=SchemaTodo, status_code=status.HTTP_200_OK)
def update_todo(todo_id: int, todo: SchemaUpdateTodo, db: Session = Depends(get_db)):
    db_todo = crud.get_task(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return crud.update_task(db=db, todo=todo, todo_id=todo_id)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_task(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    crud.delete_task(db=db, todo_id=todo_id)
