from pydantic import BaseModel
from typing import List
from app.schema.task_schema import Task

class Plan(BaseModel):
    blog_title : str
    tasks: List[Task]
