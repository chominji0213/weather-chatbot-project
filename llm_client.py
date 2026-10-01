from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from weather_tool import get_weather

#from rich import print as rprint

def build_agent():
    llm = init_chat_model("gemini-3.1-flash-lite", model_provider="google_genai")
    memory = MemorySaver()

    agent = create_agent(
        model=llm,
        tools=[get_weather],
        system_prompt="너는 날씨에 대해 물어보면 대답하는 챗봇이야. 날씨에 대해서 요약해서 대답하고, 모르는 도시에 대해 질문하면 모르겠다고 대답해",
        checkpointer=memory
    )

    return agent


def ask(agent, user_message: str, thread_id: str) -> str:
    config = {
        'configurable': {'thread_id': thread_id}
        }
    result = agent.invoke({"messages": [HumanMessage(content=user_message)]}, config)
    final_answer = result['messages'][-1].content[0]['text']

    return final_answer
