# 🧠 AutoGPT-style Web Agent

This project demonstrates a minimal AutoGPT-style agent using OpenAI's GPT-3.5 API + LangChain + Selenium.

## 💡 Goal
Accepts a natural language goal (e.g., "Find a hotel in Chicago under $200"), plans intermediate steps using a ReAct loop, interacts with webpages using Selenium, and returns results.

## 🚀 Stack
- LangChain
- OpenAI GPT-3.5
- Selenium WebDriver
- Python 3.10+

## 📂 Structure
- scripts/agent.py — entry point
- tools/browser_control.py — web search interface
- tools/memory_logger.py — stores all thoughts/actions
- logs/ — execution logs

## 🧪 Example Run
```bash
python scripts/agent.py
```
Enter a goal like: "Search for cheap hotels in Chicago for this weekend"

## 🧲 Target Labs
OpenAI, DeepMind, Gemini, Meta, FAIR
