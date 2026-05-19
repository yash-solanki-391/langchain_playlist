from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4", temperature=0.9)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of India?"),
]   

response = model.invoke(messages)
print(response.content)
messages.append(AIMessage(content=response.content))
print(messages)
