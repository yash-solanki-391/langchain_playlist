from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader = PyPDFLoader("9_Docuemtn_loader/mypdfs/QUIZE MASTER SEM 4.pdf")
model = ChatOpenAI(model="gpt-4", temperature=0.9)

docs = loader.load()

print(type(docs))
print(docs[0].page_content)
print(len(docs))
