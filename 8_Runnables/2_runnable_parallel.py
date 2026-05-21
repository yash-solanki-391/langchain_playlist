from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, chain
from dotenv import load_dotenv

load_dotenv()
promt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"],
    validate_template=True
)

promt2 = PromptTemplate(
    template="generate linked post about {topic}",
    input_variables=["topic"],
    validate_template=True
)       

model = ChatOpenAI(model="gpt-4", temperature=0.9)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(promt1, model, parser),
        "linked_post": RunnableSequence(promt2, model, parser)
    }
)

result = parallel_chain.invoke({
    "topic": "cricket"
})

print(result)

parallel_chain.get_graph().print_ascii()

