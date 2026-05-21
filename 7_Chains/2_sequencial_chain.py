from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
promt1 = PromptTemplate(
    template="Wrie a detailed report on {topic}",
    input_variables=["topic"],
    validate_template=True
)

promt2 = PromptTemplate(
    template="Summarize the following report in one line: {report}",
    input_variables=["report"],
    validate_template=True
)

model = ChatOpenAI(model="gpt-4", temperature=0.9)

parser = StrOutputParser()

chain= promt1 | model | parser | promt2 | model | parser

response = chain.invoke({
})  
print(response)


chain.get_graph().print_ascii()