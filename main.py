from agent import agent

meeting_notes = """
Project Phoenix kickoff.
- Ali will finish the homepage UI by Friday.
- Sara will draft the marketing copy.
- Hamza to set up backend repo.
Launch target: 31 Aug.
"""

response = agent.run(
    f"Here are meeting notes:\n{meeting_notes}\n\n"
    "First summarize them, then list the action items."
)

print("\n=== Agent Output ===\n")
print(response)
