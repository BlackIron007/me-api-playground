from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/profile")
def get_profile(db: Session = Depends(get_db)):
    return db.query(models.Profile).first()

@app.get("/projects")
def get_projects(skill: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Project)
    if skill:
        query = query.filter(models.Project.skills.contains(skill))
    return query.all()