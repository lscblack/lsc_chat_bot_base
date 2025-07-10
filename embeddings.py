import ollama
from typing import List

def get_embeddings(texts: List[str], model: str = "nomic-embed-text") -> List[List[float]]:
    return [
        ollama.embeddings(model=model, prompt=text)['embedding']
        for text in texts
    ]