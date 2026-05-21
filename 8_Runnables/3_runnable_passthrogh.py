from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
promt1 = PromptTemplate(
    template="Generate a joke about {topic}",
    input_variables=["topic"],
    validate_template=True
)

promt2 = PromptTemplate(
    template="Explain the joke: {joke}",
    input_variables=["joke"],
    validate_template=True
)   

model = ChatOpenAI(model="gpt-4", temperature=0.9)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(promt1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(promt2, model, parser)
    }
)

final_chain = joke_gen_chain | parallel_chain
response = final_chain.invoke({
    "topic": "cricket"
})  
print(response)
final_chain.get_graph().print_ascii()