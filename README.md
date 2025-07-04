# 🤖 Smart Agent — LangChain OpenAI Agent

A basic Python-based AI agent using LangChain and OpenAI GPT-3.5 for meeting note summarization and task extraction.

## 🚀 Features

- Uses `LangChain` and `OpenAI` to summarize meeting notes
- Extracts action items assigned to team members
- CLI-based output with Thought → Action → Observation trace
- Modular design with custom tools

## 🧠 Technologies

- Python 3.11+
- LangChain
- OpenAI API
- dotenv

## 🗂️ Project Structure

smart-agent/

├── agent.py # LangChain tools & agent setup

├── main.py # Entry point

├── helper.py # (optional) Error handler for rate-limiting

├── .env # OpenAI API Key (not committed)

├── requirements.txt # Python dependencies

├── .gitignore # Prevents secrets and venv from being pushed

└── README.md # Project info

## ⚙️ Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/smart-agent.git
cd smart-agent

# Create virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

Create a .env file and add your OpenAI key:
OPENAI_API_KEY=your-api-key-here


Then run:
python main.py
```
