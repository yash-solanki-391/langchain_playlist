from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel



from dotenv import load_dotenv

load_dotenv()
prompt1 = PromptTemplate(
    template="Generate short and simple notes from following text \n {text}",
    input_variables=["text"],
    validate_template=True
)

prompt2 = PromptTemplate(
    template="Generate 5 MCQ from following text \n {text}",
    input_variables=["text"],
    validate_template=True
)

prompt3 = PromptTemplate(
    template="Merge the following notes and MCQs into a single well formatted text \n Notes: {notes} \n MCQs: {mcq}",
    input_variables=["notes", "mcq"],
    validate_template=True
)

model = ChatOpenAI(model="gpt-4", temperature=0.9)



parser = StrOutputParser()

parallel_chain = RunnableParallel(
    notes=prompt1 | model | parser,
    mcq=prompt2 | model | parser
)

text = """
Narendra Damodardas Modi was born on 17 September 1950 in Vadnagar, Mehsana district, in what is now Gujarat. He was the third of six children born to Damodardas Mulchand Modi and Hiraben Modi. His family belonged to the "Other Backward Class," among the marginalised sections of society. He grew up in a poor but loving family. When Modi was younger, he used to help his father sell tea at the Vadnagar Railway Station, and subsequently he and his brother ran a tea stall near a bus stop
In the 2014 and 2019 Parliamentary elections, Modi led the Bharatiya Janata Party to record wins, securing absolute majority on both occasions. The last time a political party secured such an absolute majority was in the elections of 1984. Prime Minister of India
Although the BJP failed to secure a majority on its own in the 2024 Lok Sabha elections, the BJP-led NDA alliance won 293 of the 543 seats in the Lok Sabha, paving the way for Modi to become the country's prime minister for a third consecutive term. Encyclopedia Britannica
In 2024, Modi became the first non-Congress leader to win three consecutive general elections, with Jawaharlal Nehru being the only other person to achieve this feat
"""

response = parallel_chain.invoke({
    "text": text
})  
print(response)


merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain
chain.invoke({
     "text": text
})

chain.get_graph().print_ascii()