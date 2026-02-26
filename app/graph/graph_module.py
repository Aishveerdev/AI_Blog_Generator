from langgraph.graph import StateGraph, START, END
from app.state.state_module import BlogState
from app.nodes.task_sender_node_module import task_sender_node, task_sender_router
from app.nodes.planner_node_module import planner
from app.nodes.worker_node_module import worker
from app.nodes.reducer_node_module import reducer
from app.schema.plan_schema import Plan
from app.schema.task_schema import Task




g = StateGraph(BlogState)
g.add_node("planner", planner)
g.add_node("task_sender", task_sender_node)
g.add_node("worker", worker)
g.add_node("reducer", reducer)


g.add_edge(START, "planner")
g.add_edge("planner", "task_sender")
g.add_conditional_edges("task_sender", task_sender_router)
g.add_edge("worker", "reducer")
g.add_edge("reducer", END)


application = g.compile()

if __name__ == "__main__":
    topic = input("Enter topic: ")

    initial_state = {
        "topic": topic,
        "sections": [],
        "final_output": ""
    }

    result = application.invoke(initial_state)
