from pydantic import BaseModel
from typing import List


class Task(BaseModel):
    id : int
    title : str
    description : str # will tell the agent what to do in more detail