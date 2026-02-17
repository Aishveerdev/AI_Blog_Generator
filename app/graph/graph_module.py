from langgraph.graph import StateGraph, START, END
from app.graph.state_module import state
from app.nodes.fanout_node_module import fanout
from app.nodes.planner_node_module import planner
from app.nodes.worker_node_module import worker
from app.nodes.reducer_node_module import reducer
from app.schema.plan_schema import Plan
from app.schema.task_schema import Task




g = StateGraph(state)
g.add_node("planner", planner)
g.add_node("fanout_node", fanout)
g.add_node("worker", worker)
g.add_node("reducer", reducer)


g.add_edge(START, "planner")
g.add_conditional_edges("planner", fanout, ["worker"])
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

    print("\n===== FINAL OUTPUT =====\n")
    print(result["final_output"])
