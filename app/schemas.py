from pydantic import BaseModel
from typing import List, Optional

class ProfileSchema(BaseModel):
    name: str
    email: str
    education: str
    github: Optional[str]
    linkedin: Optional[str]
    portfolio: Optional[str]

class ProjectSchema(BaseModel):
    title: str
    description: str
    skills: List[str]
    link: Optional[str]