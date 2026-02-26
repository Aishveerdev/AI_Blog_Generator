from typing import TypedDict, List, Annotated
import operator
from app.schema.plan_schema import Plan 
from app.schema.task_schema import Task

class BlogState(TypedDict):
    topic: str
    Plan: Plan
    Task: Task
    blog_title :str
    sections: Annotated[list[str] , operator.add]
    final_output: str # final blog

