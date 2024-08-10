from fastapi import FastAPI, Request, Form, status, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from models import Base, Todo
from database import SessionLocal, engine
from sqlalchemy import select

Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todo")
async def todo_main(request: Request, db: Session = Depends(get_db)):
    stmt = select(Todo)
    todos = db.scalars(stmt).all()
    return templates.TemplateResponse("todo.html", {"request": request, "todo_list": todos})


@app.post("/todo/add")
def todo_add(title: str = Form(), db: Session = Depends(get_db)):
    new_todo = Todo(title=title)
    db.add(new_todo)
    db.commit()

    return RedirectResponse(url=app.url_path_for("todo_main"), status_code=status.HTTP_303_SEE_OTHER)


@app.get("/todo/update/{idx}")
def todo_update(idx: int, db: Session = Depends(get_db)):
    stmt = select(Todo).where(Todo.id == idx)
    todo = db.execute(stmt).scalars().first()
    if todo:
        todo.complete = not todo.complete
        db.commit()

    return RedirectResponse(url=app.url_path_for("todo_main"), status_code=status.HTTP_302_FOUND)


@app.get("/todo/delete/{idx}")
def todo_delete(idx: int, db: Session = Depends(get_db)):
    stmt = select(Todo).where(Todo.id == idx)
    todo = db.execute(stmt).scalars().first()
    if todo:
        db.delete(todo)
        db.commit()

    return RedirectResponse(url=app.url_path_for("todo_main"), status_code=status.HTTP_302_FOUND)
