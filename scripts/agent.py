""" Upgraded AutoGPT-style Web Agent with ReAct loop """
from tools.browser_control import BrowserTool
from tools.memory_logger import log_thought_action
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

# Setup tools
browser = BrowserTool()

tools = [
    Tool(
        name="SearchTool",
        func=browser.search_and_extract,
        description="Use to search for information online"
    ),
    Tool(
        name="ClickTool",
        func=browser.click_link_by_text,
        description="Use to click a hyperlink that partially matches a phrase"
    ),
    Tool(
        name="FormTool",
        func=browser.fill_form_and_submit,
        description="Use to fill in a form input and optionally click a submit button"
    )
]

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent
if __name__ == "__main__":
    print("Agent is ready. Enter your goal:")
    user_goal = input()
    log_thought_action(f"User goal: {user_goal}")
    result = agent.run(user_goal)
    log_thought_action(f"Final result: {result}")
    print("Done")
