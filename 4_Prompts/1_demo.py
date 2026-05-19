# from langchain_core.prompts import PromptTemplate, load_prompt
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv  
# load_dotenv()  # Load environment variables from .env file

# chat_model = ChatOpenAI(model="gpt-4", temperature=0.9)

# # prompt_template = load_prompt("4_Prompts/important_skills_prompt.json")

# prompt_template = PromptTemplate(
#     template="What are the important {skill} skills for a {role}?",
#     input_variables=["role", "skill"],
#     validate_template=True
# )

# final_prompt = prompt_template.invoke({
#     "role": "data scientist",
#     "skill": "technical",
# })
# response = chat_model.invoke(final_prompt)
# print(response.content)




#diiference betweeen prompt template and fstring
#1. default validation in prompt template
#2. prompt template can be saved and loaded from json file
#3. Reusable
#4. Langchain Ecosystem integration





from urllib import response

from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file

chat_model = ChatOpenAI(model="gpt-4", temperature=0.9)

# prompt_template = load_prompt("4_Prompts/important_skills_prompt.json")

prompt_template = PromptTemplate(
    template="What are the important {skill} skills for a {role}?",
    input_variables=["role", "skill"],
    validate_template=True
)

chain = prompt_template | chat_model     #Langchain Ecosystem integration, chaining the prompt template with the chat model, we can not do this with f-strings
result = chain.invoke({
    "role": "data scientist",
    "skill": "technical",
})
print(result.content)



