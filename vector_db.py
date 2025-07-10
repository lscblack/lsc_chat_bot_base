import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings())
collection = client.get_or_create_collection("chatbot_data")

def store_embeddings(texts, embeddings):
    for i, (text, emb) in enumerate(zip(texts, embeddings)):
        collection.add(
            ids=[f"doc_{i}"],
            documents=[text],
            embeddings=[emb]
        )

def query_embedding(query_embed, k=3):
    return collection.query(
        query_embeddings=[query_embed],
        n_results=k
    )['documents'][0]