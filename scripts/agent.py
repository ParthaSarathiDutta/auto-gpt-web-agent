""" Main ReAct agent script """
from tools.browser_control import BrowserTool
from tools.memory_logger import MemoryLogger
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.schema import SystemMessage, HumanMessage

# Setup tools
browser = BrowserTool()
logger = MemoryLogger()

tools = [
    Tool(name="BrowserTool", func=browser.search_and_extract, description="Used to browse and extract info"),
]

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Run the agent
if __name__ == "__main__":
    print("Agent is ready. Enter your goal:")
    user_goal = input()
    logger.log(f"User goal: {user_goal}")
    result = agent.run(user_goal)
    logger.log(f"Final result: {result}")
    print("✅ Done")
