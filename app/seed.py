from .database import SessionLocal, engine
from . import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

db.query(models.Project).delete()
db.query(models.Profile).delete()
db.commit()

profile = models.Profile(
    name="Dev Sharma",
    email="sdev43083@gmail.com",
    education="BTech CSE (AI & ML) from Manipal University Jaipur",
    github="https://github.com/BlackIron007/",
    linkedin="https://www.linkedin.com/in/dev-sharma-1184a8281/",
    portfolio="https://www.github.com/BlackIron007/"
)

db.add(profile)
db.commit()

projects = [
    models.Project(
        title="Automated Attendance & Analytics System",
        description="Built a distributed system that processes face images for real-time attendance and analytics.",
        skills="python,fastapi,sql,distributed systems",
        link="https://github.com/BlackIron007/face-recognition-project"
    ),
    models.Project(
        title="AI-Driven Personalized Recommender System",
        description="An end-to-end personalized recommendation platform combining content-based, collaborative, and context-aware techniques with full experiment tracking and performance analytics",
        skills="python,flask,redis, recommender systems, typescript, react, postgresql",
        link="https://github.com/BlackIron007/ai-blog-platform"
    ),
    models.Project(
        title="Cortex: AI Agent Creation Platform",
        description="An AI-based platform enabling non-coders to create custom AI agents using natural language prompts.",
        skills="python,langchain,streamlit",
        link="https://github.com/BlackIron007/Cortex"
    )
]

db.add_all(projects)
db.commit()
db.close()
