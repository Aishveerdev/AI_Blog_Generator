from urllib import response

from app.schema.plan_schema import Plan
from app.services.llm_service import planner_llm 
from app.state.state_module import BlogState
from app.prompts.planner_prompt import system_message_prompt
from rich import print
import json

def planner(state:BlogState) -> dict:

    # Extracting the topic from state
    topic = state['topic']   

    # Attaching structured schema with LLM
    structured_llm = planner_llm.with_structured_output(Plan)
    message = f"""
        {system_message_prompt}
        Topic: {topic}
        """
    
    # Making an inference call to LLM to get the plan
    response = structured_llm.invoke(message)
    # print(response)
    return {"Plan": response}


# if __name__ == "__main__":
#     topic = input("Enter the blog topic: ")
#     initial_state = {
#         "topic": topic
#     }
#     result = planner(initial_state)
#     # Saving the plan to a json file for reference
#     with open("results/plan_output.json", "w") as f:
#         json.dump(result["Plan"].model_dump(), f, indent=4)