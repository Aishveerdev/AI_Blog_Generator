from typing import TypedDict, List, Annotated
import operator
from app.schema.plan_schema import Plan
from app.schema.task_schema import Task

class state(TypedDict):
    topic: str
    Plan: Plan
    Task: Task
    sections: List[str]
    final_output: str # final blog