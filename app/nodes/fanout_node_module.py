from langgraph.types import Send
from app.graph.state_module import state
from app.schema.plan_schema import Plan
from app.schema.task_schema import Task


def fanout(state:state) -> list[Send]:

    plan:Plan = state["Plan"]
    tasks: list[Task] = plan.tasks

    return [
        Send(
            "worker",
            {
                "Task": task,          # one task per worker
                "Plan": plan, # optional but useful
                "topic": state["topic"]
            }
        )
                for task in tasks
        ]
