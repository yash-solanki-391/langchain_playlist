from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4", temperature=0.9)

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break
    chat_history.append(HumanMessage(content=user_input))   

    response = model.invoke(chat_history)
    print(f"Chatbot: {response.content}")
    chat_history.append(AIMessage(content=response.content))


print(chat_history)