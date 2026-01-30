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

@app.get("/search")
def search(q: str, db: Session = Depends(get_db)):
    return db.query(models.Project).filter(
        (models.Project.title.contains(q)) |
        (models.Project.description.contains(q)) |
        (models.Project.skills.contains(q))
    ).all()

@app.get("/skills/top")
def top_skills(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    skill_count = {}

    for p in projects:
        for skill in p.skills.split(","):
            skill = skill.strip()
            skill_count[skill] = skill_count.get(skill, 0) + 1

    return sorted(skill_count.items(), key=lambda x: x[1], reverse=True)