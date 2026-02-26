from app.services.llm_service import worker_llm
from app.schema.task_schema import Task
from app.schema.plan_schema import Plan
from app.state.state_module import BlogState
from langchain_core.messages import SystemMessage , HumanMessage
from app.prompts.worker_prompt import system_prompt


def worker (state:BlogState) -> BlogState   :
    # task:Task = state["Task"] # contains the task details like title and description # contains the overall plan details including the blog title and all the tasks
   
    task = state["Task"]
    prompt = f"""
        You are a professional blog writer.
        Section Title:{task.title}
        Task Description:{task.description}
        Instructions:
        - Write only the section content.
        - Do not add explanations.
        - WRITE AT MAX 2 PARAGRAPHS.
    """
    response = worker_llm.invoke(prompt)
    return {"sections":
             [
         {"content": response.text.strip(),
          "order": task.id }
         ]
            }


#test code to verify worker node functionality
if __name__ == "__main__":
    from app.schema.plan_schema import Plan
    from app.schema.task_schema import Task

    # Create test task
    test_task = Task(
        id=1,
        title="Test Section",
        description="This is a test task to verify worker execution."
    )

    # Create test plan
    test_plan = Plan(
        blog_title="Test Blog",
        tasks=[test_task]
    )

    # Fake state
    test_state = {
        "Plan": test_plan,
        "Task": test_task
    }

    # Call worker
    result = worker(test_state)

    print("\nWorker Output:\n")
    print(result)