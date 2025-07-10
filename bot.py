from data_loader import load_text_documents
from embeddings import get_embeddings
from vector_db import store_embeddings, query_embedding
import ollama

current_model = "llama3"

def prepare():
    texts = load_text_documents("./data")
    embeds = get_embeddings(texts)
    store_embeddings(texts, embeds)

def ask(user_input: str) -> str:
    global current_model
    if user_input.startswith("/switch"):
        _, new_model = user_input.split(maxsplit=1)
        current_model = new_model.strip()
        return f"[Switched to model: {current_model}]"

    embed = get_embeddings([user_input])[0]
    context = query_embedding(embed)
    prompt = f"Context: {context}\n\nUser: {user_input}\n\nAnswer:"

    try:
        response = ollama.chat(
            model=current_model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[Error with model '{current_model}': {str(e)}]"

if __name__ == "__main__":
    prepare()
    print(f"[Default model: {current_model}]")
    while True:
        q = input("You: ")
        if q.lower() in ["exit", "quit"]:
            break
        print("Bot:", ask(q))
