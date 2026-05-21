from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader,CSVLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader = CSVLoader("9_Docuemtn_loader/cricket_players_data.csv")

docs = loader.load()

print(type(docs))
print(docs[0].page_content)
print(len(docs))
