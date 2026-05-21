from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough, RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.9)

prompt = PromptTemplate(
    template="Generate a joke about {topic}",
    input_variables=["topic"],
    validate_template=True
)
parser = StrOutputParser()

def word_count(text:str) -> int:
    return len(text.split())

joke_gen_chain = RunnableSequence(prompt, model, parser)


parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'word_count':RunnableLambda(word_count)
    }
)

final_chain = joke_gen_chain | parallel_chain
response = final_chain.invoke({
    "topic": "cricket"
})
print(response)
final_chain.get_graph().print_ascii()
