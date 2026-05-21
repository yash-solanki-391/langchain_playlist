from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv

load_dotenv()
prompt1 = PromptTemplate(
    template="write a detailed report about {topic}",
    input_variables=["topic"],
    validate_template=True
)

prompt2 = PromptTemplate(
    template="Summarize the following report in 3 sentences: {report}",
    input_variables=["report"],
    validate_template=True
)   

model = ChatOpenAI(model="gpt-4", temperature=0.9)
parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
    
)

final_chain = report_gen_chain | branch_chain
response = final_chain.invoke({
    "topic": "Russia vs Ukraine "
})
print(response)
final_chain.get_graph().print_ascii()