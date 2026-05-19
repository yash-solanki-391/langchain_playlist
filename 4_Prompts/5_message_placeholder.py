from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4", temperature=0.9)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful coding expert."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", '{query}'),
])




prompt_value = prompt.invoke({
    "chat_history": [
        HumanMessage(content="Hi"),
        AIMessage(content="Hello!"),
        HumanMessage(content="What is Python?"),
        AIMessage(content="Python is a programming language.")
    ],

    "query": "Explain decorators"
})

print(prompt_value)