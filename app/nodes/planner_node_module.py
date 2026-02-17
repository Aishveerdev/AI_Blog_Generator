from prompt_toolkit import prompt
from app.schema.plan_schema import Plan
from app.services.llm_service import planner_llm 
from app.graph.state_module import state
from langchain_core.messages import SystemMessage , HumanMessage
from app.prompts.planner_prompt import system_message_prompt

def planner(state:state) -> dict:
    topic = state['topic']    
    # Use structured output
    structured_llm = planner_llm.with_structured_output(Plan)

    message = f"""
        {system_message_prompt}
        Topic: {topic}
        """
    response = structured_llm.invoke(message)
    return {"Plan": response}