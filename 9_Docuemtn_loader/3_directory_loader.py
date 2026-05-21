from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader = DirectoryLoader("9_Docuemtn_loader/mypdfs/", glob="*.pdf", loader_cls=PyPDFLoader)

# docs = loader.load()

# print(type(docs))
# print(docs[40].page_content)
# print(docs[40].metadata)
# print(len(docs))


documents = loader.load()
documents = loader.lazy_load()

for doc in documents:
    print(doc.metadata)


