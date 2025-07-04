from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI(title="Smart Meeting Agent")

class NoteIn(BaseModel):
    notes: str

@app.post("/analyze")
def analyze(in_data: NoteIn):
    result = agent.run(
        f"Here are meeting notes:\n{in_data.notes}\n\nSummarize and extract tasks."
    )
    return {"result": result}
