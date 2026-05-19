from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4", temperature=0.9)

# prompt_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} expert."),
#     HumanMessage(content="Explain in simple term what is {topic} in the field of {domain}."),
# ])

#in chat prompt template we can not use SystemMessage, HumanMessage and AIMessage directly, we have to use tuple with the first element as the type of message and second element as the content of the message, this is because chat prompt template is designed to work with different types of messages and it needs to know the type of message to process it accordingly.

prompt_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert."),
    ('human', "Explain in simple term what is {topic}"),]
)
prompt = prompt_template.invoke({'domain': 'software', 'topic': 'machine learning'})

print(prompt)
# response = model.invoke(prompt)
# print(response.content)