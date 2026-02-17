from app.services.llm_service import worker_llm
from app.schema.task_schema import Task
from app.schema.plan_schema import Plan
from app.graph.state_module import state
from langchain_core.messages import SystemMessage , HumanMessage
from app.prompts.worker_prompt import system_prompt



def worker (state:state):
    task:Task = state["Task"] # contains the task details like title and description
    blog_title = state["Plan"].blog_title
    topic = state["topic"]

    messages = [[
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=(
                f"blog title: {blog_title}\n"
                f"Topic: {topic}\n"
                f"Task description: {task.description}\n"
                f"section : {task.title}\n"
                "return only section content in markdown format with no other text"
            )
        )
    ]]
    print(state)

    response = worker_llm.invoke(messages)
    return {"sections": [response.content]}

    