from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader = TextLoader("9_Docuemtn_loader/content.txt")
model = ChatOpenAI(model="gpt-4", temperature=0.9)

docs = loader.load()

# print(type(docs))
# print(docs[0].page_content)
# print(len(docs))


prompt = PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"],
    validate_template=True
)

parser = StrOutputParser()  

chain = prompt | model | parser

response = chain.invoke({
    "text": docs[0].page_content
})  

print(response)