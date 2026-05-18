from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents=[
    "Virat Kohli is a great batsman. He is known for his aggressive batting style.",
    "Sachin Tendulkar is a legendary cricketer. He is known as the God of Cricket.",
    "MS dhoni is a former captain of Indian cricket team. He is known for his cool and calm nature.",
    "Jasprit Bumrah is a fast bowler. He is known for his unique bowling action.",
    "Ishan Kishan is a wicket keeper batsman. he is currently playing for Mumbai Indians in IPL.",
]


query = "Tell me about MS Dhoni"
query_embedding = embeddings.embed_query(query)
document_embeddings = embeddings.embed_documents(documents)
scores = cosine_similarity([query_embedding], document_embeddings)[0]
#cosine_similarity used to is used to measure How similar two vectors are using Cosine Similarity
#MOST IMPORTANT IDEA Cosine similarity measures: The angle between two vectors NOT their actual size/magnitude.
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)[0]

print(query)
print(documents[index])
print(f"Similarity Score: {np.round(score, 2)}")