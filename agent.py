import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI          # ✅ new path
from langchain_community.tools import Tool                     # (same class)
from langchain.agents import initialize_agent                  # still here

load_dotenv()   # loads OPENAI_API_KEY

# --- LLM wrapper (chat model) ---------------------------
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.2
)

# --- TOOL 1: summary ------------------------------------
def summarize_notes(notes: str) -> str:
    prompt = (
        "Summarize the meeting in 3‑4 bullet points:\n\n"
        f"{notes}\n\nSummary:"
    )
    return llm.invoke(prompt).content          # ChatOpenAI returns a Message

# --- TOOL 2: task extractor -----------------------------
def extract_tasks(notes: str) -> str:
    prompt = (
        "List action items as \"- [Person] — [Task]\":\n\n"
        f"{notes}\n\nTasks:"
    )
    return llm.invoke(prompt).content

tools = [
    Tool(
        name="Summarizer",
        func=summarize_notes,
        description="Summarize meeting notes"
    ),
    Tool(
        name="TaskExtractor",
        func=extract_tasks,
        description="Extract tasks and assignees"
    ),
]

# --- Build the ReAct agent ------------------------------
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)
