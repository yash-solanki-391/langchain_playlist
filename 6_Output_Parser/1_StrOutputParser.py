#without StrOutputParser


# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()
# model = ChatOpenAI(model="gpt-4", temperature=0.9)
# prompt_template1 = PromptTemplate(
#     template="Wrie a detailed report on {topic}",
#     input_variables=["topic"],
#     validate_template=True
# )


# prompt_template2 = PromptTemplate(
#     template="Summarize the following report in one line: {report}",
#     input_variables=["report"],
#     validate_template=True
# )


# prompt1 = prompt_template1.invoke({
#     "topic": "the impact of artificial intelligence on the job market"
# })

# response1 = model.invoke(prompt1)
# print("Detailed Report:")
# print(response1.content)


# prompt2 = prompt_template2.invoke({
#     "report": response1.content
# })
# response2 = model.invoke(prompt2)
# print("\nSummary:")
# print(response2.content)




#with StrOutputParser

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4", temperature=0.9)

parser = StrOutputParser()
prompt_template1 = PromptTemplate(
    template="Wrie a detailed report on {topic}",
    input_variables=["topic"],
    validate_template=True
)


prompt_template2 = PromptTemplate(
    template="Summarize the following report in one line: {report}",
    input_variables=["report"],
    validate_template=True
)


chain = prompt_template1 | model | parser | prompt_template2 | model | parser   #Chaining the prompt templates and the model, and then using StrOutputParser to get the final output as a string

chain_result = chain.invoke({
    "topic": "the impact of artificial intelligence on the job market"
})
print("Summary:")
print(chain_result)