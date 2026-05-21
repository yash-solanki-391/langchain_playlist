from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader = WebBaseLoader("https://www.iana.org/help/example-domains")
model = ChatOpenAI(model="gpt-4", temperature=0.9)

docs = loader.load()

print(type(docs))
print(docs[0].page_content)
print(len(docs))
