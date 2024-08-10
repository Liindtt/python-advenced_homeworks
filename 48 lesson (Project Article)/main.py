from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from models import Base, Article
from sqlalchemy import select
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def main(request: Request, db: Session = Depends(get_db)):
    stmt = select(Article)
    articles = db.scalars(stmt).all()
    return templates.TemplateResponse("article.html", {"request": request, "article_list": articles})


@app.post("/add")
async def add_article(title: str = Form(), author: str = Form(), year: int = Form(), db: Session = Depends(get_db)):
    new_article = Article(title=title, author=author, year=year)
    db.add(new_article)
    db.commit()

    return RedirectResponse(url=app.url_path_for("main"), status_code=status.HTTP_303_SEE_OTHER)


@app.get("/addnew")
async def addnew(request: Request):
    return templates.TemplateResponse("addnew.html", {"request": request})


@app.get("/edit/{user_id}")
async def edit(request: Request, user_id: int, db: Session = Depends(get_db)):
    stmt = select(Article).where(Article.id == user_id)
    article = db.scalars(stmt).first()
    return templates.TemplateResponse("edit.html", {"request": request, "article": article})


@app.post("/update/{user_id}")
async def update(request: Request, user_id: int, title: str = Form(...), author: str = Form(...),
                 year: str = Form(...), db: Session = Depends(get_db)):
    stmt = select(Article).where(Article.id == user_id)
    article = db.execute(stmt).scalar_one_or_none()
    article.title = title
    article.author = author
    article.year = year
    db.commit()
    return RedirectResponse(url=app.url_path_for("main"), status_code=status.HTTP_303_SEE_OTHER)


@app.get("/delete/{user_id}")
async def delete(request: Request, user_id: int, db: Session = Depends(get_db)):
    stmt = select(Article).where(Article.id == user_id)
    users = db.execute(stmt).scalar_one_or_none()
    db.delete(users)
    db.commit()
    return RedirectResponse(url=app.url_path_for("main"), status_code=status.HTTP_303_SEE_OTHER)
