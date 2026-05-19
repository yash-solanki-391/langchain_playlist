# from typing import TypedDict
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv 

# load_dotenv()
# class Review(TypedDict):
#     summary: str
#     sentiment: int

# model = ChatOpenAI(model="gpt-4", temperature=0.9)  

# review = """I recently purchased the XYZ product and I am extremely satisfied with it. The build quality is excellent, and it performs exceptionally well. The customer service was also very responsive and helpful when I had a question about the setup. Overall, I would highly recommend this product to anyone in the market for something like this."""

# structured_model = model.with_structured_output(Review)
# response = structured_model.invoke(review)
# print(response)
# print(type(response))
# print(response["summary"])
# print(response["sentiment"])
    


from typing import  Optional, List, TypedDict, Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 

load_dotenv()
class Review(TypedDict):
    key_themes: Annotated[List[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review either negative, neutral, or positive"]
    pros: Annotated[Optional[List[str]], "List down the pros mentioned in the review in a list"]
    cons: Annotated[Optional[List[str]], "List down the cons mentioned in the review in a list"]

model = ChatOpenAI(model="gpt-4", temperature=0.9)  

review = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for bloatware-why do I need five different Samsung apps fothing pill to swallow.
Pros:
Insanely powerful processor (great for gaming and productivity) Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors
I
handad use. Also, Samsung's One UI still comes with oglelready provides? The $1,300 price tag is also a hard
"""

structured_model = model.with_structured_output(Review)
response = structured_model.invoke(review)
print(response)
print(type(response))
print(response["summary"])
print(response["sentiment"])
    


