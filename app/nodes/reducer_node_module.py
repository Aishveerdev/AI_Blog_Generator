from app.state.state_module import BlogState

from pathlib import Path

def reducer(state: BlogState) -> dict:
    
    title = state["Plan"].blog_title
    sections = sorted(state["sections"], key=lambda x: x["order"])
    body = "\n\n".join([section["content"] for section in sections])

    final_md = f"# {title}\n\n{body}\n"

    # ---- save to file ----
    filename = title.lower().replace(" ", "_") + ".md"
    output_path = Path(filename)
    output_path.write_text(final_md, encoding="utf-8")

    return {"final": final_md}