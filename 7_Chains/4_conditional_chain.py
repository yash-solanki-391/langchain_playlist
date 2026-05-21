from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal




load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.9)
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback as positive or negative:\n {feedback}\n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()},
    validate_template=True
)

# prompt1 = PromptTemplate(
#     template="Classify the sentiment of the following feedback as positive or negative:\n {feedback}",
#     input_variables=["feedback"],
#     validate_template=True
# )

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n {feedback}",
    input_variables=["feedback"],
    validate_template=True
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n {feedback}",
    input_variables=["feedback"],
    validate_template=True
)


# classify_chain = prompt1 | model | parser2
classify_chain = prompt1 | model | parser2

feedback = "Excellent Customer Support: The company resolved my shipping issue immediately." 
response = classify_chain.invoke({
    "feedback": feedback
}).sentiment
print(response)


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not classify the feedback sentiment.")
)

chain = classify_chain | branch_chain
final_response = chain.invoke({
    "feedback": feedback
})
print(final_response)

chain.get_graph().print_ascii()