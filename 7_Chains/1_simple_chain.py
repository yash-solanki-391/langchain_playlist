from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
promt = PromptTemplate(
    template="Wrie a 5 interesting facts about {topic}",
    input_variables=["topic"],
    validate_template=True
)

model = ChatOpenAI(model="gpt-4", temperature=0.9)

parser = StrOutputParser()

chain= promt | model | parser

response = chain.invoke({
    "topic": "cricket"
})  
print(response)
