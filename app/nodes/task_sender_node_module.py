from langgraph.graph import END
from langgraph.types import Send
from app.state.state_module import BlogState , Plan , Task
from app.schema.plan_schema import Plan


def task_sender_node(state: BlogState) -> dict:
    # This node does not modify state
    return {}


def task_sender_router(state: BlogState):
    plan = state["Plan"]
    tasks = plan.tasks
    return[
        Send(
            "worker",
            {
                "Task": task,
                "order": task.id
            }
        )
        for task in tasks
    ]
   
    

